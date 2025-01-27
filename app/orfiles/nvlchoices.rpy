## Initialization
init offset = -1

## NVL screen
init python:
    config.empty_window = nvl_show_core
    config.window_hide_transition = dissolve
    config.window_show_transition = dissolve
default options_thais_rumors = 0
default options_eudocia = 0
default options_oldpagos = 0
default options_monastery = 0
default options_monastery_about_necromancers = 0
default options_monastery_about_order = 0
default options_thyrsus = 0
default options_helvius = 0
default options_orentius = 0
default options_foragers = 0
default options_elah = 0
default options_efren = 0
default options_severina = 0
default options_galerocks = 0
default options_aegidia = 0
default options_creeks = 0
default options_cephasgaiane = 0
default options_cephasgaiane_highisland = 0
default options_glaucia = 0
default foragers_quest_daythreshold_display = 0
screen nvl(dialogue, items=None):
    default tt = Tooltip("")
    default tt2 = Tooltip("")
    default attitudeypos = 0
    vbox:
        # xpos 0
        spacing 10
        ypos 63#-800#63
        xmaximum 1530
        xminimum 1530
        # xalign 0.0
        # yalign 0.0
        viewport id "dialogue":
            draggable True # placeholder
            ymaximum 956
            mousewheel True
            arrowkeys True
            vbox:
                spacing 12
                hbox:
                    hbox:
                        xmaximum 714
                        xminimum 714
                        null height 0
                    hbox:
                        style "nvl_window"
                        xmaximum 800
                        xminimum 800
                        yfill False
                        #xpos 0
                        spacing gui.nvl_spacing
                            ## Displays dialogue in either a vpgrid or the vbox.
                        # vpgrid:
                        #     cols 1
                        #     yinitial 1.0
                        use nvl_dialogue(dialogue)
                hbox:
                    hbox:
                        yalign 0.5
                        xmaximum 714
                        xminimum 714
                        if not at_activate and not at_unlock_force and not at_unlock_spell and not at_unlock_knowledge:
                            null height 0
                        elif at_activate or at_unlock_force or at_unlock_spell or at_unlock_knowledge:
                            if tt.value != "" and persistent.showattitudetips:
                                frame:
                                    xalign 1.0
                                    xpadding 24
                                    ypadding 12
                                    yalign 0.5
                                    # ypos 0
                                    xpos 689
                                    if persistent.textstyle == "basic":
                                        text tt.value text_align 0.5 font "philosopher.ttf" line_spacing +5
                                    if persistent.textstyle == "pixel":
                                        text tt.value text_align 0.5 font "munro.ttf" line_spacing +5
                            elif tt2.value != "" and not persistent.showattitudetips:
                                frame:
                                    xalign 1.0
                                    xpadding 24
                                    ypadding 12
                                    yalign 0.5
                                    # ypos 0
                                    xpos 689
                                    if persistent.textstyle == "basic":
                                        text tt2.value text_align 0.5 font "philosopher.ttf" line_spacing +5
                                    if persistent.textstyle == "pixel":
                                        text tt2.value text_align 0.5 font "munro.ttf" line_spacing +5
                            else:
                                null height 0
                    vbox:
                        xmaximum 800
                        xminimum 800
                        if not at_activate and not at_unlock_force and not at_unlock_spell and not at_unlock_knowledge:
                            null height 0
                        elif at_activate or at_unlock_force or at_unlock_spell or at_unlock_knowledge:
                            null height 13
                            hbox:
                                spacing 20
                                xalign 0.5
                                if at_activate:
                                    imagebutton:
                                        focus_mask True
                                        hovered [tt.Action("{color=#f6d6bd}FRIENDLY{/color}\nBe supportive and cordial.")]
                                        if at != "friendly":
                                            idle "gui/attitudes/friendly_idle.png"
                                            hover "gui/attitudes/friendly_hovered.png"
                                            action [SetVariable("at", "friendly")]
                                        else:
                                            idle "gui/attitudes/friendly_active.png"
                                            action NullAction()
                                    imagebutton:
                                        focus_mask True
                                        hovered [tt.Action("{color=#f6d6bd}PLAYFUL{/color}\nUse a joke or a witty comment.")]
                                        if at != "playful":
                                            action [SetVariable("at", "playful")]
                                            idle "gui/attitudes/playful_idle.png"
                                            hover "gui/attitudes/playful_hovered.png"
                                        else:
                                            idle "gui/attitudes/playful_active.png"
                                            action NullAction()
                                    imagebutton:
                                        focus_mask True
                                        hovered [tt.Action("{color=#f6d6bd}DISTANCED{/color}\nHide your emotions.")]
                                        if at != "distanced":
                                            idle "gui/attitudes/distanced_idle.png"
                                            hover "gui/attitudes/distanced_hovered.png"
                                            action [SetVariable("at", "distanced")]
                                        else:
                                            idle "gui/attitudes/distanced_active.png"
                                            action NullAction()
                                    imagebutton:
                                        focus_mask True
                                        hovered [tt.Action("{color=#f6d6bd}INTIMIDATING{/color}\nHint at a threat.")]
                                        if at != "intimidating":
                                            idle "gui/attitudes/intimidating_idle.png"
                                            hover "gui/attitudes/intimidating_hovered.png"
                                            action [SetVariable("at", "intimidating")]
                                        else:
                                            idle "gui/attitudes/intimidating_active.png"
                                            action NullAction()
                                    imagebutton:
                                        focus_mask True
                                        hovered [tt.Action("{color=#f6d6bd}VULNERABLE{/color}\nBe sad, tired, afraid, or hopeless.")]
                                        if at != "vulnerable":
                                            idle "gui/attitudes/vulnerable_idle.png"
                                            hover "gui/attitudes/vulnerable_hovered.png"
                                            action [SetVariable("at", "vulnerable")]
                                        else:
                                            idle "gui/attitudes/vulnerable_active.png"
                                            action NullAction()
                                if at_unlock_force and pc_class == "warrior":
                                    imagebutton:
                                        focus_mask True
                                        if not pc_hp:
                                            idle "gui/attitudes/force_locked.png"
                                            hovered tt.Action("{color=#f6d6bd}FORCE{/color}\nYou are too exhausted. You need to rest."), tt2.Action("You need to rest.")
                                            action NullAction()
                                        elif at_unlock_force:
                                            hovered tt.Action("{color=#f6d6bd}FORCE{/color}\nUse violence or a direct threat.")
                                            if at != "force":
                                                idle "gui/attitudes/force_idle.png"
                                                hover "gui/attitudes/force_hovered.png"
                                                action [SetVariable("at", "force")]
                                            else:
                                                idle "gui/attitudes/force_active.png"
                                                hover "gui/attitudes/force_hovered.png"
                                                action [SetVariable("at", 0)]
                                if at_unlock_spell and pc_class == "mage":
                                    imagebutton:
                                        focus_mask True
                                        if mana >= manacost:
                                            hovered tt.Action("{color=#f6d6bd}SPELL{/color}\n[mana]/5 pneuma left."), tt2.Action("[mana]/5 pneuma left.")
                                        else:
                                            hovered tt.Action("{color=#f6d6bd}SPELL{/color}\nYour soul is too weak. [mana]/5 pneuma left."), tt2.Action("[mana]/5 pneuma left.")
                                        if mana >= manacost:
                                            if at != "spell":
                                                if mana <= 0:
                                                    idle "gui/attitudes/spell_idle0.png"
                                                    hover "gui/attitudes/spell_hovered0.png"
                                                elif mana == 1:
                                                    idle "gui/attitudes/spell_idle1.png"
                                                    hover "gui/attitudes/spell_hovered1.png"
                                                elif mana == 2:
                                                    idle "gui/attitudes/spell_idle2.png"
                                                    hover "gui/attitudes/spell_hovered2.png"
                                                elif mana == 3:
                                                    idle "gui/attitudes/spell_idle3.png"
                                                    hover "gui/attitudes/spell_hovered3.png"
                                                elif mana == 4:
                                                    idle "gui/attitudes/spell_idle4.png"
                                                    hover "gui/attitudes/spell_hovered4.png"
                                                else:
                                                    idle "gui/attitudes/spell_idle5.png"
                                                    hover "gui/attitudes/spell_hovered5.png"
                                                if mana >= manacost:
                                                    action [SetVariable("at", "spell")]
                                                else:
                                                    action NullAction()
                                            else:
                                                if mana <= 0:
                                                    idle "gui/attitudes/spell_active0.png"
                                                    hover "gui/attitudes/spell_hovered0.png"
                                                elif mana == 1:
                                                    idle "gui/attitudes/spell_active1.png"
                                                    hover "gui/attitudes/spell_hovered1.png"
                                                elif mana == 2:
                                                    idle "gui/attitudes/spell_active2.png"
                                                    hover "gui/attitudes/spell_hovered2.png"
                                                elif mana == 3:
                                                    idle "gui/attitudes/spell_active3.png"
                                                    hover "gui/attitudes/spell_hovered3.png"
                                                elif mana == 4:
                                                    idle "gui/attitudes/spell_active4.png"
                                                    hover "gui/attitudes/spell_hovered4.png"
                                                else:
                                                    idle "gui/attitudes/spell_active5.png"
                                                    hover "gui/attitudes/spell_hovered5.png"
                                                action [SetVariable("at", 0)]
                                        else:
                                            if mana <= 0:
                                                idle "gui/attitudes/spell_inactive0.png"
                                                hover "gui/attitudes/spell_hovered0.png"
                                            elif mana == 1:
                                                idle "gui/attitudes/spell_inactive1.png"
                                            elif mana == 2:
                                                idle "gui/attitudes/spell_inactive2.png"
                                            elif mana == 3:
                                                idle "gui/attitudes/spell_inactive3.png"
                                            elif mana == 4:
                                                idle "gui/attitudes/spell_inactive4.png"
                                            else:
                                                idle "gui/attitudes/spell_inactive5.png"
                                            action NullAction()
                                if at_unlock_knowledge and pc_class == "scholar":
                                    imagebutton:
                                        focus_mask True
                                        hovered tt.Action("{color=#f6d6bd}KNOWLEDGE{/color}\nYour education could be of use here.")
                                        if at != "knowledge":
                                            idle "gui/attitudes/knowledge_idle.png"
                                            hover "gui/attitudes/knowledge_hovered.png"
                                            action [SetVariable("at", "knowledge")]
                                        else:
                                            idle "gui/attitudes/knowledge_active.png"
                                            hover "gui/attitudes/knowledge_hovered.png"
                                            action [SetVariable("at", 0)]
                            null height 13
                            if persistent.tutorial_display:
                                if tutorial_attitudes:
                                    frame:
                                        style "tutorial_frame"
                                        # ypos 309
                                        # xpos 1112
                                        xalign 0.5
                                        yalign 0.0
                                        textbutton _("Whenever you meet new people, you can influence how they\nperceive you by selecting one of the {b}attitudes{/b}."):
                                            action SetVariable("tutorial_attitudes", 0)
                                            text_style "tutorial_button_text"
                                            if persistent.textstyle == "basic":
                                                text_size 26
                                            if persistent.textstyle == "pixel":
                                                text_size 28
                                            text_slow_cps True
                                if tutorial_abilities:
                                    frame:
                                        style "tutorial_frame"
                                        xalign 0.5
                                        yalign 0.0
                                        if pc_class == "warrior":
                                            textbutton "If you have any vitality points, you can use\nthe warrior’s training to access unique interactions.":
                                                action SetVariable("tutorial_abilities", 0)
                                                text_style "tutorial_button_text"
                                                text_slow_cps True
                                                if persistent.textstyle == "basic":
                                                    text_size 26
                                                if persistent.textstyle == "pixel":
                                                    text_size 28
                                        if pc_class == "mage" and at != "spell":
                                            textbutton "If you have enough pneuma, you can cast spells\nto access unique interactions.":
                                                action NullAction()
                                                text_style "tutorial_button_text"
                                                text_slow_cps True
                                                if persistent.textstyle == "basic":
                                                    text_size 26
                                                if persistent.textstyle == "pixel":
                                                    text_size 28
                                        if pc_class == "mage" and at == "spell":
                                            textbutton "To restore pneuma, you need to rest.\n ":
                                                action SetVariable("tutorial_abilities", 0)
                                                text_style "tutorial_button_text"
                                                text_slow_cps True
                                                if persistent.textstyle == "basic":
                                                    text_size 26
                                                if persistent.textstyle == "pixel":
                                                    text_size 28
                                        if pc_class == "scholar":
                                            textbutton "On occasion, you can use the scholar’s education\nto unlock unique interactions.":
                                                action SetVariable("tutorial_abilities", 0)
                                                text_style "tutorial_button_text"
                                                text_slow_cps True
                                                if persistent.textstyle == "basic":
                                                    text_size 26
                                                if persistent.textstyle == "pixel":
                                                    text_size 28
                hbox:
                    hbox:
                        xmaximum 714
                        xminimum 714
                        null height 0
                    vbox:
                        xmaximum 800
                        xminimum 800
                        if interface_showline and items:
                            add "gui/dialogueline.png" #ypos 0
                            null height 8
                        else:
                            null height 0
                hbox:
                    hbox:
                        xmaximum 714
                        xminimum 714
                        if (persistent.tutorial_display and tutorial_random and pc_class == "mage" and at != "spell") or (persistent.tutorial_display and tutorial_random and pc_class != "mage"):
                            frame:
                                xalign 1.0
                                yalign 0.5
                                # ypos 0
                                xpos 689
                                style "tutorial_frame"
                                textbutton "The {image=d6} icon marks the actions\nthat involve a random chance.":
                                    action SetVariable("tutorial_random", 0)
                                    text_style "tutorial_button_text"
                                    text_slow_cps True
                        else:
                            null height 0
                    vbox:
                        xmaximum 800
                        xminimum 800
                        spacing 12
                        for i in [ k for k in items
                                 if not k.kwargs.get('condition', None)
                                 or renpy.python.py_eval(k.kwargs['condition']) ]:

                            if questionpreset == "tulia1":
                                if not tulia_about_peninsula:
                                    textbutton '“What should I know about the peninsula?”' action [SetVariable("questionpreset", 0), Jump("tulia_about_peninsula")] style "nvl_button" text_slow_cps True
                                if not tulia_about_asterion1:
                                    textbutton '“Any ideas what happened to the previous roadwarden?”' action [SetVariable("questionpreset", 0), Jump("tulia_about_asterion1")] style "nvl_button" text_slow_cps True
                                if not item_rope:
                                    textbutton '“I’ve lost my rope. Could you spare one?”' action [SetVariable("questionpreset", 0), Jump("militarycamp01askingabouttherope")] style "nvl_button" text_slow_cps True
                                if not tulia_about_hersquad:
                                    textbutton '“What happened to your squad?”' action [SetVariable("questionpreset", 0), Jump("tulia_about_hersquad")] style "nvl_button" text_slow_cps True
                                if not tulia_about_herself:
                                    textbutton '“{color=#f6d6bd}Tulia{/color}, how did you become a lieutenant?”' action [SetVariable("questionpreset", 0), Jump("tulia_about_herself")] style "nvl_button" text_slow_cps True
                                if not tulia_about_hermission:
                                    textbutton '“What was your squad’s mission?”' action [SetVariable("questionpreset", 0), Jump("tulia_about_hermission")] style "nvl_button" text_slow_cps True
                                if tulia_about_hermission and not description_tulia04 and (tulia_friendship+appearance_charisma) < 3:
                                    textbutton 'She doesn’t trust me enough to tell me about her squad’s mission.' action NullAction() style "nvl_button2" text_slow_cps True
                                if tulia_about_hermission and not description_tulia04 and (tulia_friendship+appearance_charisma) >= 3:
                                    textbutton '“About your squad’s mission...”' action [SetVariable("questionpreset", 0), Jump("tulia_about_hermissionp02")] style "nvl_button" text_slow_cps True
                                if not tulia_about_camp:
                                    textbutton '“Anything I should know about this camp?”' action [SetVariable("questionpreset", 0), Jump("tulia_about_camp")] style "nvl_button" text_slow_cps True
                                if not tulia_about_advice:
                                    textbutton '“If you were me, where would you go next?”' action [SetVariable("questionpreset", 0), Jump("tulia_about_advice")] style "nvl_button" text_slow_cps True
                                #################################
                                if not tulia_about_peninsula and not tulia_about_asterion1 and not item_rope:
                                    textbutton 'Before I continue my journey, I need to ask them about the peninsula, the roadwarden, and the rope.' action NullAction() style "nvl_button2" text_slow_cps True
                                elif not tulia_about_peninsula and not tulia_about_asterion1:
                                    textbutton 'Before I continue my journey, I need to ask them about the peninsula and the roadwarden.' action NullAction() style "nvl_button2" text_slow_cps True
                                elif not tulia_about_peninsula and not item_rope:
                                    textbutton 'Before I continue my journey, I need to ask them about the peninsula and the rope.' action NullAction() style "nvl_button2" text_slow_cps True
                                elif not tulia_about_asterion1 and not item_rope:
                                    textbutton 'Before I continue my journey, I need to ask them about the roadwarden and the rope.' action NullAction() style "nvl_button2" text_slow_cps True
                                elif not tulia_about_peninsula:
                                    textbutton 'Before I continue my journey, I need to ask them about the peninsula.' action NullAction() style "nvl_button2" text_slow_cps True
                                elif not tulia_about_asterion1:
                                    textbutton 'Before I continue my journey, I need to ask them about the roadwarden.' action NullAction() style "nvl_button2" text_slow_cps True
                                elif not item_rope:
                                    textbutton 'Before I continue my journey, I need to ask them about the rope.' action NullAction() style "nvl_button2" text_slow_cps True
                                #################################
                                if tulia_questions_main == 2 and tulia_questions_side >= 5 and item_rope:
                                    textbutton '“It’s getting late. We should prepare for the night.”' action [SetVariable("questionpreset", 0), Jump("prolcamp01afterquestions01")] style "nvl_button" text_slow_cps True
                                if tulia_questions_main == 2 and tulia_questions_side < 5 and item_rope:
                                    textbutton '“I know everything I need.”' action [SetVariable("questionpreset", 0), Jump("prolcamp01imdonewithquestions01")] style "nvl_button" text_slow_cps True

                            elif questionpreset == "iason1":
                                if item_rawfishtotalnumber >= 2 and iason_about_fish:
                                    textbutton '{image=cointest} “I have more fish to sell.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("peltnorth_sellingrawfish02")] style "nvl_button" text_slow_cps True
                                if item_rawfishtotalnumber == 1 and iason_about_fish:
                                    textbutton '{image=coingray} I only have a single fish to sell.' action NullAction() style "nvl_button2" text_slow_cps True
                                if not item_rawfishtotalnumber and iason_about_fish:
                                    textbutton '{image=coingray} I have no fish to sell.' action NullAction() style "nvl_button2" text_slow_cps True
                                if not iason_food_berries and iason_food != day and not iason_food_berries_refused:
                                    textbutton 'I could eat something. “Do you have any leftovers?” ' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), SetVariable("iason_food", day), Jump("peltnorthleftoversquestforberries01")] style "nvl_button" text_slow_cps True
                                if item_peltnorthberries == 1 and iason_food_berries != 3:
                                    textbutton 'I put his fruits on the counter.' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), SetVariable("item_peltnorthberries", 0), SetVariable("iason_food", day), Jump("peltnorthleftoversquestforberries04")] style "nvl_button" text_slow_cps True
                                if iason_food == day and iason_food_berries == 2:
                                    textbutton 'I already asked for leftovers today.' action NullAction() style "nvl_button2" text_slow_cps True
                                if iason_food != day and iason_food_berries == 2:
                                    if pc_food < 4:
                                        textbutton '{image=d6} “Any leftovers?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), SetVariable("iason_food", day), Jump("peltnorthleftoversyesorno")] style "nvl_button" text_slow_cps True
                                    else:
                                        textbutton 'I don’t need to eat right now.' action NullAction() style "nvl_button2" text_slow_cps True
                                if quest_foggy2iason == 1 and not quest_foggy2iason_description01:
                                    textbutton '“{color=#f6d6bd}Foggy{/color} has a message for you.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("peltnorthfoggymessage01")] style "nvl_button" text_slow_cps True
                                if not quintus_left_gate and quintus_left_gate_points_argument_iason_about and not iason_about_workforquintus:
                                    textbutton '“There’s this gatekeeper, {color=#f6d6bd}Quintus{/color}...”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("peltnorth_iason_about_workforquintus01")] style "nvl_button" text_slow_cps True
                                if not iason_shop:
                                    textbutton '{image=cointest} “What do you have for sale?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), SetVariable("iason_shop", 1), Jump("peltnorthtrade01")] style "nvl_button" text_slow_cps True
                                if iason_shop == 1:
                                    textbutton '{image=cointest} “Show me your wares.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), SetVariable("iason_shop", 1), Jump("peltnorthtrade03")] style "nvl_button" text_slow_cps True
                                textbutton '{image=cointest} “Do I have anything you’d like to buy?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("peltnorth_selling01")] style "nvl_button" text_slow_cps True
                                if not orentius_met and not whitemarshes_attacked and not whitemarshes_nomoreundead:
                                    if quest_orentius == 1 and quest_orentius_thais_description00 and not quest_orentius_thais_description00betrayal and not thais_defeated and not quest_orentius_thais_description10 and quest_orentius_thais_description03 and not quest_orentius_thais_description03a01 and not orentius_met and not whitemarshes_attacked:
                                        textbutton '“I have a message from {color=#f6d6bd}Thais{/color}. It’s about {color=#f6d6bd}Orentius{/color}.”' action [SetVariable("questionpreset", 0), Jump("peltnorthquest_orentius_thais_description01")] style "nvl_button" text_slow_cps True
                                elif whitemarshes_nomoreundead and not iason_about_nomoreundead:
                                    if orentius_convinced:
                                        textbutton '“The undead of {color=#f6d6bd}White Marshes{/color} are gone, and the village suffered no losses. I thought you should know.”' action [SetVariable("questionpreset", 0), Jump("peltnorthaboutnomoreundead01")] style "nvl_button" text_slow_cps True
                                    elif orentius_banished:
                                        textbutton '“The undead of {color=#f6d6bd}White Marshes{/color} are gone, but I don’t think the village will take any traders in the near future. I thought you should know.”' action [SetVariable("questionpreset", 0), Jump("peltnorthaboutnomoreundead02")] style "nvl_button" text_slow_cps True
                                    elif whitemarshes_destroyed:
                                        textbutton '“The undead of {color=#f6d6bd}White Marshes{/color} may soon leave the bogs, and there’s no one there to control them. I recommend avoiding these territories.”' action [SetVariable("questionpreset", 0), Jump("peltnorthaboutnomoreundead03")] style "nvl_button" text_slow_cps True
                                if not iason_about_asterion1 and quest_asterion == 1 and not asterion_found:
                                    textbutton '“I’m looking for {color=#f6d6bd}Asterion{/color}, the previous roadwarden.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), SetVariable("iason_about_asterion1", 1), Jump("peltnorthasterion01")] style "nvl_button" text_slow_cps True
                                if iason_about_asterion1 and asterion_found and not iason_about_asterion_found:
                                    textbutton '“I found {color=#f6d6bd}Asterion{/color}.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), SetVariable("iason_about_asterion_found", 1), Jump("iason_about_asterion_found01")] style "nvl_button" text_slow_cps True
                                if asterion_highisland_knowsabout and not asterion_found and not iason_about_highisland:
                                    textbutton '“Have you heard anything about {color=#f6d6bd}High Island{/color}?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), SetVariable("", 0), Jump("iason_about_highisland01")] style "nvl_button" text_slow_cps True
                                if ruinedvillage_confront_can and not ruinedvillage_truth and not iason_about_steephouse and quest_ruins_10yclue02:
                                    if iason_about_steephouse_gray:
                                        textbutton '“I want to learn what happened to the ruined village. Let’s talk the price.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("peltnorthaboutruinedvillage01alt", 1), SetVariable("questionpreset", 0), Jump("peltnorthaboutruinedvillage01alt")] style "nvl_button" text_slow_cps True
                                    else:
                                        textbutton '“Let’s talk. You and your group arrived to the peninsula not long before the village in the west was ruined.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("peltnorthaboutruinedvillage01", 1), SetVariable("questionpreset", 0), Jump("peltnorthquestionssteephouse01")] style "nvl_button" text_slow_cps True
                                if not iason_about_directions:
                                    textbutton '“What can you tell me about the peninsula?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("peltnorthaboutpeninsula01")] style "nvl_button" text_slow_cps True
                                if (iason_about_directions and not iason_about_directions_west) or (iason_about_directions and not iason_about_directions_east) or (iason_about_directions and not iason_about_directions_north):
                                    textbutton '“About the peninsula...”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("peltnorthaboutpeninsula01")] style "nvl_button" text_slow_cps True
                                if not iason_about_inn:
                                    textbutton '“I didn’t expect to find an inn of this size in a place such as this.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("peltnorthaboutpeltnorth01")] style "nvl_button" text_slow_cps True
                                if iason_about_inn and not iason_about_inn_bonus1 and not iason_about_inn_bonus2:
                                    textbutton '“About your inn...”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("peltnorthaboutpeltnorth01")] style "nvl_button" text_slow_cps True
                                if not iason_about_quest_glaucia:
                                    textbutton '“Need anything done? I could use a job.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), SetVariable("iason_about_quest_glaucia", 1), Jump("peltnorthaskingforjob01")] style "nvl_button" text_slow_cps True
                                if not iason_about_plague and oldpagos_plague_known:
                                    textbutton '“I bring sad news from {color=#f6d6bd}Old Págos{/color}. The villagers were stricken by a plague.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("iason_about_plague", 1), SetVariable("questionpreset", 0), Jump("peltnorthquestionsplague01")] style "nvl_button" text_slow_cps True
                                if quest_intelforpeltnorth == 1:
                                    textbutton '“About {color=#f6d6bd}Glaucia’s{/color} band...”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("peltnorthaskingforjob02")] style "nvl_button" text_slow_cps True
                                if iason_rumors_introduction:
                                    if iason_friendship >= iason_rumors_threshold: # iason_friendship+appearance_charisma >= iason_rumors_threshold:
                                        textbutton '“I’d like to ask about someone.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("peltnorthrumors01alt")] style "nvl_button" text_slow_cps True
                                    else:
                                        textbutton 'He doesn’t trust me enough to share any gossip.' action NullAction() style "nvl_button2" text_slow_cps True
                                else:
                                    textbutton '“Any rumors worth sharing?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("peltnorthrumors01")] style "nvl_button" text_slow_cps True
                                if peltnorth_bonusnpcs:
                                    textbutton 'I take another look at the main hall.' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 1), SetVariable("questionpreset", 0), Jump("peltnorth01insidechoosenpc")] style "nvl_button" text_slow_cps True
                                textbutton '“That’s all I need.” I go outside.' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("leavingthepeltnorth")] style "nvl_button" text_slow_cps True

                            elif questionpreset == "dalit1":
                                if not dalit_dice_never and dalit_dice < day and dalit_axes < day and coins:
                                    textbutton '{image=d6} “If you have coin, I could throw some dice.”' action [SetVariable("questionpreset", 0), Jump("peltnorthtalkingwithguardsplayingdice00")] style "nvl_button" text_slow_cps True
                                if not dalit_dice_never and dalit_dice < day and dalit_axes < day and coins and pc_hp >= 2:
                                    textbutton '{image=d6} “How about some axe throwing?”' action [SetVariable("questionpreset", 0), Jump("peltnorthtalkingwithguardsaxethrowing00")] style "nvl_button" text_slow_cps True
                                if not dalit_dice_never and dalit_dice < day and dalit_axes < day and coins and pc_hp <= 1:
                                    textbutton 'I’m too tired to throw axes.' action NullAction() style "nvl_button2" text_slow_cps True
                                if not dalit_dice_never and dalit_dice < day and dalit_axes < day and not coins:
                                    textbutton 'I can’t afford to gamble.' action NullAction() style "nvl_button2" text_slow_cps True
                                if (not dalit_dice_never and dalit_dice == day and coins) or (not dalit_dice_never and dalit_axes == day and coins):
                                    textbutton 'We already played today.' action NullAction() style "nvl_button2" text_slow_cps True
                                if dalit_pc_debt and coins >= dalit_pc_debt:
                                    textbutton '“I have the dragons I owe you.”' action [SetVariable("questionpreset", 0), Jump("peltnorthpayingbackthedebt")] style "nvl_button" text_slow_cps True
                                if dalit_pc_debt and coins < dalit_pc_debt:
                                    textbutton 'I don’t have enough to pay back my debt.' action NullAction() style "nvl_button2" text_slow_cps True
                                if quest_recruitahunter == 1:
                                    textbutton '“About the hunters you wanted me to recruit...”' action [SetVariable("questionpreset", 0), Jump("peltnorth_dalit_recruitahunter01")] style "nvl_button" text_slow_cps True
                                elif quest_recruitahunter == 2 and quest_recruitahunter_noonerecruited and not quest_recruitahunter_spokento_shoshi:
                                    textbutton 'Maybe I’ll find a good candidate who’d like to join the hunters.' action NullAction() style "nvl_button2" text_slow_cps True
                                elif quest_recruitahunter == 2 and quest_recruitahunter_noonerecruited and quest_recruitahunter_spokento_shoshi and not quest_recruitahunter_spokento_shoshi_recruited:
                                    textbutton '“I spoke with this strong lumberjack...”' action [SetVariable("questionpreset", 0), Jump("peltnorth_dalit_recruitahunter_shoshi01")] style "nvl_button" text_slow_cps True
                                if not asterion_found and quest_asterion == 1 and quest_gatheracrew == 1 and not dalit_about_highisland_recruitment_done and dalit_about_name:
                                    if not dalit_about_highisland_recruitment:
                                        textbutton '“I could use a skillful hunter on my short journey to {color=#f6d6bd}High Island{/color}.”' action [SetVariable("questionpreset", 0), Jump("dalit_about_highisland_recruitment01")] style "nvl_button" text_slow_cps True
                                    else:
                                        textbutton 'We negotiate the price of her help at {color=#f6d6bd}High Island{/color}.' action [SetVariable("questionpreset", 0), Jump("dalit_about_highisland_recruitment01b")] style "nvl_button" text_slow_cps True
                                if shortcut_pcknowsabout and not dalit_about_shortcut:
                                    textbutton '“Have you ever been at the heart of the woods?”' action [SetVariable("questionpreset", 0), Jump("dalit_about_shortcut01")] style "nvl_button" text_slow_cps True
                                if asterion_highisland_knowsabout and not asterion_found and not dalit_about_highisland:
                                    textbutton '“Do you know anything about {color=#f6d6bd}High Island{/color}?”' action [SetVariable("questionpreset", 0), Jump("peltnorthdalitabouthighisland01")] style "nvl_button" text_slow_cps True
                                if quest_missinghunters == 1 and not dalit_about_missinghunters:
                                    textbutton '“I’m looking for a few hunters from {color=#f6d6bd}Creeks{/color}. {color=#f6d6bd}Vaschel{/color}, {color=#f6d6bd}Dalia{/color}, {color=#f6d6bd}Admon{/color}. Were they here?”' action [SetVariable("questionpreset", 0), Jump("dalit_about_missinghunters01")] style "nvl_button" text_slow_cps True
                                if shortcut_woodenroad_fisheater and dalit_about_wildcreatures and not dalit_bestiary_fisheater:
                                    textbutton '“I’ve seen a weird, human-like creature with gray skin. It was eating a raw fish at the pond in the heart of the woods. Any clue what it could be?”' action [SetVariable("questionpreset", 0), Jump("peltnorthdalitonfisheater")] style "nvl_button" text_slow_cps True
                                if oldtunnel_inside_undead_seen and dalit_about_wildcreatures and not dalit_bestiary_undead_light:
                                    textbutton '“Did you know there are undead that use light?”' action [SetVariable("questionpreset", 0), Jump("peltnorthdalitonundead_light")] style "nvl_button" text_slow_cps True
                                if not dalit_about_quintus and quintus_friendswithdalit and westgate_firsttime and not quintus_left_gate:
                                    textbutton '“I met {color=#f6d6bd}Quintus{/color}, the one who trained with your team. He may need your help.”' action [SetVariable("questionpreset", 0), Jump("peltnorthtalkingwithguardsaboutquintus01")] style "nvl_button" text_slow_cps True
                                if not dalit_about_ilan and foragers_firsttime and dalit_name == "Dalit":
                                    textbutton '“I met {color=#f6d6bd}Ilan{/color}. He says hi.”' action [SetVariable("questionpreset", 0), Jump("peltnorthtalkingwithguardsaboutilan01")] style "nvl_button" text_slow_cps True
                                if quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_peltnorth:
                                    textbutton '“I’d like to put this rod on your watchtower for {color=#f6d6bd}Eudocia{/color}, the enchantress.”' action [SetVariable("questionpreset", 0), Jump("peltnorthtalkingwithguardsaboutbronzerod")] style "nvl_button" text_slow_cps True
                                if not dalit_about_arrow and item_arrow and not galerocks_florus_about_arrow:
                                    textbutton 'I show her the arrow I found near the fallen tree. “Did any of you drop this?”' action [SetVariable("questionpreset", 0), Jump("peltnorthtalkingwithguardsaboutarrow01")] style "nvl_button" text_slow_cps True
                                if dalit_about_name_gray:
                                    if not dalit_about_name and (dalit_friendship+appearance_charisma) > 3 and dalit_name != "Dalit":
                                        textbutton '“I’d like to know more about you.”' action [SetVariable("questionpreset", 0), Jump("peltnorthtalkingwithguardsdalit_nameaa")] style "nvl_button" text_slow_cps True
                                    elif dalit_name == "Dalit" and not dalit_about_name:
                                        textbutton '“{color=#f6d6bd}Dalit{/color}, right?”' action [SetVariable("questionpreset", 0), Jump("peltnorthtalkingwithguardsdalit_nameb")] style "nvl_button" text_slow_cps True
                                    elif not dalit_about_name and (dalit_friendship+appearance_charisma) <= 3:
                                        textbutton 'She doesn’t trust me enough to tell me about herself.' action NullAction() style "nvl_button2" text_slow_cps True
                                else:
                                    if not dalit_about_name and dalit_name != "Dalit":
                                        textbutton '“Tell me about yourself.”' action [SetVariable("questionpreset", 0), Jump("peltnorthtalkingwithguardsdalit_namea")] style "nvl_button" text_slow_cps True
                                    elif dalit_name == "Dalit" and not dalit_about_name:
                                        textbutton '“{color=#f6d6bd}Dalit{/color}, right?”' action [SetVariable("questionpreset", 0), Jump("peltnorthtalkingwithguardsdalit_nameb")] style "nvl_button" text_slow_cps True
                                if (iason_food_berries == 1 and not dalit_about_berries) or (iason_food_berries_refused and not dalit_about_berries):
                                    textbutton '“The innkeep has asked me to forage for berries...”' action [SetVariable("questionpreset", 0), Jump("peltnorthtalkingwithguardsberries")] style "nvl_button" text_slow_cps True
                                if iason_food_berries == 2 and not dalit_about_berries:
                                    textbutton '“I was foraging for berries for the innkeep...”' action [SetVariable("questionpreset", 0), Jump("peltnorthtalkingwithguardsberriesalt")] style "nvl_button" text_slow_cps True
                                if dalit_about_minorquestionALL < 6:
                                    textbutton '“I have some questions about this place.”' action [SetVariable("questionpreset", 0), Jump("peltnorthtalkingwithguardsaboutpeltnorth")] style "nvl_button" text_slow_cps True
                                if oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_knowledge:
                                    textbutton '“I’d like to place some traps in an old tunnel in the far north. Any ideas?”' action [SetVariable("questionpreset", 0), Jump("peltnorthtalkingwithguardsabouttraps01")] style "nvl_button" text_slow_cps True
                                if not dalit_about_goblins and ruinedvillage_part_leftwing_EXPLORED:
                                    textbutton '“I have a job for your crew. There are some goblins in the nearby ruins that pose a danger on the road.”' action [SetVariable("questionpreset", 0), Jump("peltnorthtalkingwithguardsaboutgoblins01")] style "nvl_button" text_slow_cps True
                                if dalit_about_goblins == 1:
                                    textbutton '“About the goblins...”' action [SetVariable("questionpreset", 0), Jump("peltnorthtalkingwithguardsaboutgoblins02")] style "nvl_button" text_slow_cps True
                                if iason_about_pagans_hunterdruid and not dalit_about_druids:
                                    textbutton '“I heard that one of you can tell me something about the local druids.”' action [SetVariable("questionpreset", 0), Jump("peltnorthtalkingwithguardsaboutdruids")] style "nvl_button" text_slow_cps True
                                if dalit_about_creatures and not dalit_beastiary_unlocked:
                                    textbutton '“I’m looking for knowledge about wild creatures.”' action [SetVariable("questionpreset", 0), Jump("peltnorthtalkingwithguardsbeasts01")] style "nvl_button" text_slow_cps True
                                if dalit_about_creatures and dalit_beastiary_unlocked:
                                    textbutton '“I’m looking for knowledge about wild creatures.”' action [SetVariable("questionpreset", 0), Jump("peltnorthtalkingwithguardsbeastsparsers")] style "nvl_button" text_slow_cps True
                                if (quest_recruitahunter_possible and not peltnorth_ban_perm_past and not dalit_pc_debt and not quest_recruitahunter_dalit_started and dalit_about_name and (dalit_friendship+appearance_charisma) >= 6) or (quest_recruitahunter_possible and not peltnorth_ban_perm_past and not dalit_pc_debt and not quest_recruitahunter_dalit_started and dalit_about_name and quest_intelforpeltnorth_description08):
                                    textbutton 'I walk away.' action [SetVariable("questionpreset", 0), Jump("peltnorth_dalit_recruitahunter00")] style "nvl_button" text_slow_cps True
                                else:
                                    textbutton 'I walk away.' action [SetVariable("questionpreset", 0), Jump("leavingthepeltnorth02")] style "nvl_button" text_slow_cps True

                            elif questionpreset == "druidcave1":
                                if not druidcave_druid_forestspeaker:
                                    textbutton '“I know how I should have addressed you. I want to fix my mistake.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcavesupporttyping")] style "nvl_button" text_slow_cps True
                                if not druidcave_druid_about_plague01 and oldpagos_firsttime and not oldpagos_cured:
                                    textbutton '“I bring news from {color=#f6d6bd}Old Págos{/color}. A terrible plague has fallen upon it.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcave_druid_about_plague01")] style "nvl_button" text_slow_cps True
                                if not druidcave_druid_about_plague02 and druidcave_druid_about_plague01 and not item_magicfruit and not pc_foodmagicfruit and not item_magicfruit_lost and not oldpagos_cured:
                                    textbutton 'I don’t have Beholder’s Seed yet.' action NullAction() style "nvl_button2" text_slow_cps True
                                if not druidcave_druid_about_plague02 and druidcave_druid_about_plague01 and item_magicfruit == 1 and not oldpagos_cured:
                                    textbutton '“I have the... fruit that you’ve told me about.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcave_druid_about_plague02")] style "nvl_button" text_slow_cps True
                                if not druidcave_druid_about_plague02 and druidcave_druid_about_plague01 and item_magicfruit_lost and not oldpagos_cured:
                                    textbutton '“I’ve lost the fruit. Will the tree bear another one?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcave_druid_about_plague02failalt")] style "nvl_button" text_slow_cps True
                                if not druidcave_druid_about_plague02 and druidcave_druid_about_plague01 and pc_foodmagicfruit and not oldpagos_cured:
                                    textbutton '“I’ve eaten the fruit. Will the tree bear another one?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcave_druid_about_plague02fail")] style "nvl_button" text_slow_cps True
                                if (quest_healingtheplague_description05 and not quest_healingtheplague_description07 and quarters < (world_daylength-24) and howlersdell_firsttime and not oldpagos_cured) or (quest_healingtheplague_description05alt and not quest_healingtheplague_description07 and quarters < (world_daylength-24) and howlersdell_firsttime and not oldpagos_cured):
                                    textbutton '“I’m ready to take you to {color=#f6d6bd}Old Págos{/color}.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcave_druid_about_plague03")] style "nvl_button" text_slow_cps True
                                if (quest_healingtheplague_description05 and not quest_healingtheplague_description07 and quarters >= (world_daylength-24) and not oldpagos_cured) or (quest_healingtheplague_description05alt and not quest_healingtheplague_description07 and quarters >= (world_daylength-24) and not oldpagos_cured):
                                    textbutton 'It’s too late to take him to Old Págos now.' action NullAction() style "nvl_button2" text_slow_cps True
                                if (quest_healingtheplague_description05 and not quest_healingtheplague_description07 and quarters >= (world_daylength-24) and not howlersdell_firsttime and not oldpagos_cured) or (quest_healingtheplague_description05alt and not quest_healingtheplague_description07 and quarters >= (world_daylength-24) and not howlersdell_firsttime and not oldpagos_cured):
                                    textbutton 'I still haven’t been to Howler’s Dell. I can’t take him to Old Págos.' action NullAction() style "nvl_button2" text_slow_cps True
                                if quest_spiritrock == 1 and galerocks_photios_quest_spiritrock_question_doubt and not druidcave_druid_about_spiritrock:
                                    textbutton '“Can we talk about {color=#f6d6bd}Phoibe{/color}, {color=#f6d6bd}Photios’{/color} daughter?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcaveaboutphoibe01")] style "nvl_button" text_slow_cps True
                                if not druidcave_druid_about_robes and howlersdell_elpis_firsttime == 2:
                                    textbutton '“I wonder why you don’t wear robes, like the druids from {color=#f6d6bd}Howler’s Dell{/color}?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcaveaboutrobes01")] style "nvl_button" text_slow_cps True
                                if not druidcave_druid_about_asterion1 and not quest_asterion == 3:
                                    textbutton '“Have you met {color=#f6d6bd}Asterion{/color}?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcave_druid_about_asterion1")] style "nvl_button" text_slow_cps True
                                if druidcave_druid_about_asterion1 and not druidcave_druid_about_asterion2 and asterion_found:
                                    textbutton '“I found {color=#f6d6bd}Asterion{/color}.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcave_druid_about_asterion2")] style "nvl_button" text_slow_cps True
                                if not druidcave_druid_about_cave:
                                    textbutton '“What can you tell me about this place?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcave_druid_about_cave")] style "nvl_button" text_slow_cps True
                                if not druidcave_druid_about_solitude:
                                    textbutton '“How can you survive in this place, being all by yourself?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcave_druid_about_solitude")] style "nvl_button" text_slow_cps True
                                if not druidcave_druid_about_peninsula:
                                    textbutton '“What can you tell me about the peninsula?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcave_druid_about_peninsula")] style "nvl_button" text_slow_cps True
                                if (quest_intelforpeltnorth == 1 and not druidcave_druid_about_bandits1) or (banditshideout_bandits_pchearedabout == 1 and not druidcave_druid_about_bandits1):
                                    textbutton '“I’ve heard about some bandits. Were they bothering you?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcave_druid_about_bandits1")] style "nvl_button" text_slow_cps True
                                if quest_swampaltar == 1 and not druidcave_druid_about_altar:
                                    textbutton '“Can you tell me anything about the altar near the crossroads in the north?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcave_druid_about_altar")] style "nvl_button" text_slow_cps True
                                if not quest_recruitahunter_spokento_druid and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed:
                                    textbutton '“I’m trying to learn more about this trapper, {color=#f6d6bd}Erastos{/color}...”' action [SetVariable("questionpreset", 0), Jump("druidcave_druid_about_recruitahunter01")] style "nvl_button" text_slow_cps True
                                if pc_class == "scholar" and not druidcave_druid_about_herbs:
                                    textbutton '“I dabble a bit in herbalism... Any chance you’d sell me some of the woundwort you grow here?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcavequestionaboutscholarherbs01")] style "nvl_button" text_slow_cps True
                                if pc_class == "scholar" and druidcave_druid_about_herbs == 1 and not item_blackwoundwort:
                                    textbutton '“I have time now to dig out these woundworts for you.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcavequestionaboutscholarherbs02alt")] style "nvl_button" text_slow_cps True
                                if not druidcave_druid_about_ruins1 and ruinedvillage_firsttime and quest_ruins == 1 and not ruinedvillage_truth:
                                    if ((druidcave_druid_friendship+appearance_charisma) < 11 and druidcave_druid_about_ruins1_gray) or (not oldpagos_cured and druidcave_druid_about_ruins1_gray):
                                        textbutton 'He’s not willing to speak with me about the ruined village.' action NullAction() style "nvl_button2" text_slow_cps True
                                    elif druidcave_druid_about_ruins1_gray:
                                        textbutton '“I deserve to know what happened to the ruined village.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcave_druid_about_ruins1alt")] style "nvl_button" text_slow_cps True
                                    else:
                                        textbutton '“I want to know what happened to the village in the east.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcave_druid_about_ruins1")] style "nvl_button" text_slow_cps True
                                if quest_sleepinggiant < 2 and not giantstatue_pray_knows and giantstatue_firsttime:
                                    if druidcave_druid_about_sleepinggiant_gray:
                                        if (druidcave_druid_friendship+appearance_charisma) < 10:
                                            textbutton 'He’s not willing to teach me about the sleeping giant.' action NullAction() style "nvl_button2" text_slow_cps True
                                        else:
                                            textbutton '“Tell me about the giant from the far east.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcaveonsleepinggiant01alt")] style "nvl_button" text_slow_cps True
                                    else:
                                        textbutton '“Can you help me wake up the giant from the far east?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcaveonsleepinggiant01")] style "nvl_button" text_slow_cps True
                                if quest_reachthepaganvillage == 1 and not druidcave_druid_about_greenmountaintribe1 and druidcave_druid_about_peninsula:
                                    if (druidcave_druid_friendship+appearance_charisma) < 7 and druidcave_druid_about_greenmountaintribe1_gray:
                                        textbutton 'He’s not willing to tell me about The Tribe.' action NullAction() style "nvl_button2" text_slow_cps True
                                    elif (druidcave_druid_friendship+appearance_charisma) >= 7 and druidcave_druid_about_greenmountaintribe1_gray:
                                        textbutton '“I still need to learn more about {color=#f6d6bd}The Tribe of The Green Mountain{/color}.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcaveaboutthegreenmountaintribe02")] style "nvl_button" text_slow_cps True
                                    else:
                                        textbutton '“What can you tell me about {color=#f6d6bd}The Tribe of The Green Mountain{/color}?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcave_druid_about_greenmountaintribe1")] style "nvl_button" text_slow_cps True
                                if not druidcave_druid_about_druids1:
                                    if (druidcave_druid_friendship+appearance_charisma) < 5 and druidcave_druid_about_druids1_gray:
                                        textbutton 'He doesn’t trust me enough to tell me about the druids.' action NullAction() style "nvl_button2" text_slow_cps True
                                    else:
                                        textbutton '“What can you tell me about the druids?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcave_druid_about_druids1")] style "nvl_button" text_slow_cps True
                                if shortcut_pcknowsabout and not druidcave_druid_about_shortcut:
                                    textbutton '“It seems like the path at the heart of the woods is quite dangerous.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcave_druid_about_shortcut01")] style "nvl_button" text_slow_cps True
                                if asterion_highisland_knowsabout and not asterion_found and not druidcave_druid_about_highisland:
                                    if not druidcave_druid_about_highisland_gray:
                                        textbutton '“I need to learn more about {color=#f6d6bd}High Island{/color}.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcave_druid_about_highisland01")] style "nvl_button" text_slow_cps True
                                    elif (druidcave_druid_friendship+appearance_charisma) < druidcave_druid_about_highisland_friendship and druidcave_druid_about_highisland_gray and not howlersdell_elpis_about_highisland:
                                        textbutton 'He doesn’t trust me enough to tell me about the island.' action NullAction() style "nvl_button2" text_slow_cps True
                                    elif howlersdell_elpis_about_highisland and not druidcave_druid_about_highisland_elpis:
                                        textbutton '“{color=#f6d6bd}Elpis{/color} asks you to tell me more about the island, as a favor for her.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcave_druid_about_highisland01alt")] style "nvl_button" text_slow_cps True
                                    else:
                                        textbutton '“Look at my lips. I {i}need{/i} to learn more about {color=#f6d6bd}High Island{/color}.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcave_druid_about_highisland02")] style "nvl_button" text_slow_cps True
                                if quest_missinghunters == 1 and not druidcave_druid_about_missinghunters:
                                    textbutton '“Have any hunters from {color=#f6d6bd}Creeks{/color} visited you recently?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcave_druid_about_missinghunters01")] style "nvl_button" text_slow_cps True
                                if not druidcave_druid_about_job and not quest_empresscarp:
                                    if (druidcave_druid_friendship+appearance_charisma) < 3 and druidcave_druid_about_job_gray and not druidcave_druid_about_spiritrock:
                                        textbutton 'He won’t give me any job right now.' action NullAction() style "nvl_button2" text_slow_cps True
                                    else:
                                        textbutton '“I’m looking for a job.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcave_druid_about_job")] style "nvl_button" text_slow_cps True
                                if quest_empresscarp == 1 and item_empresscarp:
                                    textbutton '“I’ve brought what you had asked for.”' action [SetVariable("questionpreset", 0), Jump("druidcavefirstreward")] style "nvl_button" text_slow_cps True
                                if quest_empresscarp == 1 and not item_empresscarp:
                                    textbutton 'I don’t have the fish that he was asking for.' action NullAction() style "nvl_button2" text_slow_cps True
                                if not druidcave_cave_open:
                                    if (druidcave_druid_friendship+appearance_charisma) < 9 and druidcave_cave_open_gray:
                                        textbutton 'I’m not allowed to entern the cavern.' action NullAction() style "nvl_button2" text_slow_cps True
                                    else:
                                        textbutton '“Can I enter the cavern? I need a place to rest.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcaveaboutenteringthedruidcave01")] style "nvl_button" text_slow_cps True
                                if quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_druidcave:
                                    if quarters <= world_daylength-2:
                                        textbutton '“{color=#f6d6bd}Eudocia{/color}, the enchantress, has asked me to place these bronze rods in high spots across the peninsula. I should be done in about half an hour.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcavecaverninstallingarod01")] style "nvl_button" text_slow_cps True
                                    else:
                                        textbutton 'Maybe I could place Eudocia’s rod among these rocks, but it’s too dark to climb.' action NullAction() style "nvl_button2" text_slow_cps True
                                if item_snakebait and not eudocia_about_flower_druid:
                                    textbutton 'I show him the snake bait. “What can you tell me about this?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcaveonsnakebait")] style "nvl_button" text_slow_cps True
                                if thyrsus_about_druids1 and not druidcave_druid_about_thyrsus:
                                    textbutton '“You were {color=#f6d6bd}Thyrsus’{/color} teacher, am I right?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcaveonthyrsus")] style "nvl_button" text_slow_cps True
                                if (elpis_about_thyrsusgift2 and not druidcave_about_thyrsusgift_druidcomment):
                                    textbutton '“Is there something {color=#f6d6bd}Thyrsus{/color} could do to reunite with his parents?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcave_about_thyrsusgift_druidcomment01")] style "nvl_button" text_slow_cps True
                                if (druidcave_about_thyrsusgift_druidcomment and elpis_about_thyrsusgift2 and not druidcave_about_elpis_about_thyrsusgift2):
                                    textbutton '“I helped another druid find cursed soil in {color=#f6d6bd}Howler’s{/color} forest garden.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcave_about_elpis_about_thyrsusgift2")] style "nvl_button" text_slow_cps True
                                if (druidcave_druid_healing and pc_hp < 4 and not pc_hp_can5) or (druidcave_druid_healing and pc_hp < 5 and pc_hp_can5):
                                    textbutton '“I’m hurt. I’d like to collect my reward.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcave_druid_healing")] style "nvl_button" text_slow_cps True
                                if (druidcave_druid_healing and pc_hp == 4 and not pc_hp_can5) or (druidcave_druid_healing and pc_hp == 5 and pc_hp_can5):
                                    textbutton 'I don’t need him to heal me.' action NullAction() style "nvl_button2" text_slow_cps True
                                if world_deadline < 1000 or (world_deadline == 1000 and day <= 45):
                                    if druidcave_druid_about_druids1 and not druidcave_druid_about_weather:
                                        textbutton '“Since you know so much about nature... Could you predict the weather for me?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcaveaboutweather01")] style "nvl_button" text_slow_cps True
                                    elif druidcave_druid_about_druids1 and druidcave_druid_about_weather and druidcave_druid_about_weather != day:
                                        textbutton '“What sort of weather do you expect for tomorrow?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcaveaboutweather02")] style "nvl_button" text_slow_cps True
                                    elif druidcave_druid_about_druids1 and druidcave_druid_about_weather and druidcave_druid_about_weather == day:
                                        textbutton 'I already asked him about the weather today.' action NullAction() style "nvl_button2" text_slow_cps True
                                if druidcave_cave_open:
                                    textbutton '“I’d like to enter the cavern.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcavecavernregular01")] style "nvl_button" text_slow_cps True
                                if druidcave_cave_open:
                                    textbutton 'I approach the spring.' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcavespring01")] style "nvl_button" text_slow_cps True

                            elif questionpreset == "druidcave2":
                                if item_magicfruit:
                                    textbutton 'I pull out the weird fruit from my bag. “Guess what I found!”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcave_druid_about_plague02instant")] style "nvl_button" text_slow_cps True
                                if pc_foodmagicfruit:
                                    textbutton '“Actually... I’ve already eaten this... fruit. Is there maybe some other way?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcave_druid_about_plague02failinstant")] style "nvl_button" text_slow_cps True
                                if item_magicfruit_lost:
                                    textbutton '“I’ve lost the fruit. Will the tree bear another one?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcave_druid_about_plague02failinstantalt")] style "nvl_button" text_slow_cps True
                                if not druidcave_druid_about_plague01f:
                                    textbutton '“So, I need to {i}offer magic{/i} to the altar. What must we do next?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcave_druid_about_plague01f")] style "nvl_button" text_slow_cps True
                                if not druidcave_druid_about_plague01g:
                                    textbutton '“Tell me more about this... seed.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcave_druid_about_plague01g")] style "nvl_button" text_slow_cps True
                                if not druidcave_druid_about_plague01h:
                                    textbutton '“It sounds like you’re trying to push me into some dark magic, old man.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcave_druid_about_plague01h")] style "nvl_button" text_slow_cps True
                                if not druidcave_druid_about_plague01i and quest_healingtheplague_description00:
                                    textbutton '“Maybe it’s time to ask the druids from the village to help me. I’m sure they could spare some of their pneuma.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcave_druid_about_plague01i")] style "nvl_button" text_slow_cps True
                                if not druidcave_druid_about_plague01k:
                                    textbutton '“Do you have anything I could give to the altar?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcave_druid_about_plague01k")] style "nvl_button" text_slow_cps True
                                if not druidcave_druid_about_plague01j:
                                    textbutton '“What will I get in return for all this trouble?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("druidcave_druid_about_plague01j")] style "nvl_button" text_slow_cps True
                                textbutton '“Fine. I know everything I need.”' action [SetVariable("can_leave", 1), SetVariable("can_rest", 1), SetVariable("can_items", 1), SetVariable("questionpreset", 0), Jump("druidcave_druid_about_plague01z")] style "nvl_button" text_slow_cps True

                            elif questionpreset == "thais1":
                                if not thais_bigmad:
                                    $ options_thais_rumors += 0
                                    if glaucia_about_steephouse3 and ruinedvillage_truth and not thais_rumor_glaucia_revenge:
                                        $ options_thais_rumors += 1
                                    if description_tulia04 and not thais_rumor_soldiers_goal:
                                        $ options_thais_rumors += 1
                                    if description_tulia01 and not thais_rumor_soldiers_leaving:
                                        $ options_thais_rumors += 1
                                    if quest_studyingthegolems and not thais_rumor_monks_golems:
                                        $ options_thais_rumors += 1
                                    if monastery_cave_firsttime and not thais_rumor_monks_cave:
                                        $ options_thais_rumors += 1
                                    if not thais_rumor_creeks_missinghunters:
                                        if quest_missinghunters_vaschelfound == 2 or quest_missinghunters_vaschelfound == 3 or (quest_missinghunters_vaschelfound and quest_missinghunters_vaschelknown and quest_missinghunters):
                                            if quest_missinghunters_daliafound == 2 or quest_missinghunters_daliafound == 3 or (quest_missinghunters_daliafound and quest_missinghunters_daliaknown and quest_missinghunters):
                                                if quest_missinghunters_admonfound == 2 or quest_missinghunters_admonfound == 3 or (quest_missinghunters_admonfound and quest_missinghunters_admonknown and quest_missinghunters):
                                                    $ options_thais_rumors += 1
                                    if creeks_reasonstojoin_problemsknown >= 5 and not thais_rumor_creeks_struggles:
                                        $ options_thais_rumors += 1
                                    if severina_quest_lostmerchants_stayingsilent and not thais_rumor_galerocks_trading:
                                        $ options_thais_rumors += 1
                                    if (item_snakebait_truth and quest_eudociaflower and not thais_rumor_eudocia_snakebait) or (pc_class == "scholar" and quest_eudociaflower and not thais_rumor_eudocia_snakebait):
                                        $ options_thais_rumors += 1
                                    if howlersdell_elpis_about_thais and not thais_rumor_elpis_doubt:
                                        $ options_thais_rumors += 1
                                    if greenmountaintribe_firsttime and not thais_rumor_greenmountaintribe_found:
                                        $ options_thais_rumors += 1
                                    if banditshideout_bandits_pchearedabouthideout and not thais_rumor_glaucia_found:
                                        $ options_thais_rumors += 1
                                    if description_glaucia06 and quest_intelforpeltnorth_description06 and not thais_rumor_glaucia_undead:
                                        $ options_thais_rumors += 1
                                    if (description_iason06 and not thais_rumor_foggylake_purchase) or (foggy_quest_iason_trade and not thais_rumor_foggylake_purchase):
                                        $ options_thais_rumors += 1
                                    if whitemarshes_forestgardenabandoned and not thais_rumor_forestgarden:
                                        $ options_thais_rumors += 1
                                    if foragingground_foraging_vein and not thais_rumor_vein and not foragingground_foraging_vein_sabotaged:
                                        $ options_thais_rumors += 1
                                    if not asterion_found and quest_asterion == 1 and quest_gatheracrew == 1 and not thais_about_highisland_recruitment_done:
                                        if not thais_about_highisland_recruitment:
                                            textbutton '“I believe I can find {color=#f6d6bd}Asterion{/color} on {color=#f6d6bd}High Island{/color}, but I need to take a few fighters with me.”' action [SetVariable("questionpreset", 0), Jump("thais_about_highisland_recruitment01")] style "nvl_button" text_slow_cps True
                                        else:
                                            if quest_ruins_choice == "thais_alliance" or thais_debt:
                                                textbutton '“I need a few of your guards on {color=#f6d6bd}High Island{/color}. The officials will want to learn the truth about {color=#f6d6bd}Asterion{/color}.”' action [SetVariable("questionpreset", 0), Jump("thais_about_highisland_recruitment02")] style "nvl_button" text_slow_cps True
                                            else:
                                                textbutton 'She won’t risk the lives of her people to aid me on High Island.' action NullAction() style "nvl_button2" text_slow_cps True
                                    if item_asterionwine and item_asterionwine_pcknows_1 and not item_asterionwine_pcknows_2 and not thais_about_wine:
                                        textbutton '“I found this bottle of wine. Any ideas what it is?”' action [Jump("howlersdellquestionwine01")] style "nvl_button" text_slow_cps True
                                    if quest_asterion == 1 and not asterion_found and item_asteriontablet and not thais_about_asteriontablet and not item_asteriontablet_read and thais_about_joiningthecity:
                                        textbutton '“Could you read me this tablet?”' action [Jump("howlersdellquestionsthais_about_asteriontablet01")] style "nvl_button" text_slow_cps True
                                    if item_letterwhitemarshes == 1 and quest_readtheletter == 1 and not item_letterwhitemarshes_read and thais_about_joiningthecity:
                                        textbutton 'I show her the troll-bone tablet. “Could you tell me what’s in here?”' action [Jump("howlersdellquestionsthais_about_readtheletter01")] style "nvl_button" text_slow_cps True
                                    if quest_asterion == 1 and not asterion_found and not thais_about_asterion:
                                        textbutton '“I’m looking for {color=#f6d6bd}Asterion{/color}.”' action [Jump("howlersdellquestionsasterion01")] style "nvl_button" text_slow_cps True
                                    if asterion_found and thais_about_asterion and not thais_about_foundasterion:
                                        textbutton '“I found {color=#f6d6bd}Asterion{/color}.”' action [Jump("howlersdellquestionsfoundasterion01")] style "nvl_button" text_slow_cps True
                                    if (thais_about_magicfruit and not druidcave_druid_about_plague02 and druidcave_druid_about_plague01 and item_magicfruit == 1 and not oldpagos_cured and not item_magicfruit_lost) or (thais_about_magicfruit and howlersdell_elpis_about_magicfruit and item_magicfruit == 1 and not item_magicfruit_lost and not oldpagos_cured):
                                        textbutton '“You can have the Seed.”' action [Jump("howlersdellquestionsgivingawaytheseed02")] style "nvl_button" text_slow_cps True
                                    if (not thais_about_magicfruit and not druidcave_druid_about_plague02 and druidcave_druid_about_plague01 and item_magicfruit == 1 and not oldpagos_cured and not item_magicfruit_lost) or (not thais_about_magicfruit and howlersdell_elpis_about_magicfruit and item_magicfruit == 1 and not oldpagos_cured and not item_magicfruit_lost):
                                        textbutton '“I have the Seed of Beholder. What can you give me for it?”' action [Jump("howlersdellquestionsgivingawaytheseed01")] style "nvl_button" text_slow_cps True
                                    if not thais_about_joiningthecity:
                                        textbutton '“What would it take to make you consider joining {color=#f6d6bd}Hovlavan{/color}?”' action [Jump("howlersdellquestionsjoiningthecity01")] style "nvl_button" text_slow_cps True
                                    if not orentius_met and not whitemarshes_attacked and not whitemarshes_nomoreundead:
                                        if not thais_about_necromancers:
                                            textbutton '“Have you heard of the necromancers in the north?”' action [Jump("howlersdellquestionsnecromancers01")] style "nvl_button" text_slow_cps True
                                    elif whitemarshes_nomoreundead and not whitemarshes_attacked and not thais_about_nomoreundead:
                                        if orentius_convinced:
                                            textbutton '“The necromancer of {color=#f6d6bd}White Marshes{/color} has no more control over the village, and his {i}laborers{/i} are gone.”' action [SetVariable("questionpreset", 0), Jump("howlersdellthais_about_nomoreundead01")] style "nvl_button" text_slow_cps True
                                        elif whitemarshes_destroyed:
                                            textbutton '“The necromancer of {color=#f6d6bd}White Marshes{/color} is dead, and his {i}laborers{/i} will soon start to roam through these woods. The bogs should be avoided.”' action [SetVariable("questionpreset", 0), Jump("howlersdellthais_about_nomoreundead02")] style "nvl_button" text_slow_cps True
                                    if not thais_about_hermoney and thais_friendship < 8:
                                        textbutton '“You seem to be fairly well-off, even more so than the other people in the village. What’s your secret?”' action [Jump("howlersdellquestionsabouthermoney01")] style "nvl_button" text_slow_cps True
                                    if not thais_about_howlers:
                                        textbutton '“Tell me about {color=#f6d6bd}Howler’s Dell{/color}.”' action [Jump("howlersdellquestionshowlers01")] style "nvl_button" text_slow_cps True
                                    if not thais_about_steephouse_fail and not ruinedvillage_truth and quest_ruins == 1:
                                        textbutton '“I was in the ruined village, south from here...”' action [Jump("howlersdellquestionssteephouse_fail01")] style "nvl_button" text_slow_cps True
                                    if not quest_recruitahunter_spokento_thais and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed:
                                        if not quest_recruitahunter_spokento_thais_gray:
                                            textbutton '“I have a few questions about {color=#f6d6bd}Erastos{/color}.”' action [SetVariable("questionpreset", 0), Jump("thais_about_recruitahunter01")] style "nvl_button" text_slow_cps True
                                        elif (thais_friendship+appearance_charisma) < 6:
                                            textbutton 'She’s not willing to speak about Erastos with me.' action NullAction() style "nvl_button2" text_slow_cps True
                                        else:
                                            textbutton '“Back to {color=#f6d6bd}Erastos{/color}...”' action [SetVariable("questionpreset", 0), Jump("thais_about_recruitahunter01alt")] style "nvl_button" text_slow_cps True
                                    if quest_bronzerod == 1 and item_bronzerod and thais_about_bronzerod_allowed != -1 and not eudocia_bronzerod_rodin_howlersdell:
                                        if not thais_about_golemsrods:
                                            textbutton '“Do you know {color=#f6d6bd}Eudocia{/color}, the enchantress? I’d like to hang this rod on a watchtower for her.”' action [Jump("howlersdellquestionsgolems01")] style "nvl_button" text_slow_cps True
                                        elif not thais_about_bronzerod_allowed and thais_about_golemsrods and (thais_friendship+howlersdell_reputation+appearance_charisma) >= thais_about_bronzerod_threshold:
                                            textbutton '“About that bronze rod...”' action [Jump("howlersdellquestionsgolems01b")] style "nvl_button" text_slow_cps True
                                        elif not thais_about_bronzerod_allowed and thais_about_golemsrods and (thais_friendship+howlersdell_reputation+appearance_charisma) < thais_about_bronzerod_threshold:
                                            textbutton 'She doesn’t trust me enough to accept placing a golem rod in the village.' action NullAction() style "nvl_button2" text_slow_cps True
                                    if not thais_about_plague and oldpagos_plague_known:
                                        textbutton '“I bring sad news from {color=#f6d6bd}Old Págos{/color}. The villagers were stricken by a plague.”' action [Jump("howlersdellquestionsplague01")] style "nvl_button" text_slow_cps True
                                    if not thais_about_pyrrhos and ruinedvillage_camp_UNLOCKED and not pyrrhos_howlersdell:
                                        textbutton '“What do you think about {color=#f6d6bd}the scavenger{/color} who was here before?”' action [Jump("howlersdellquestionspyrrhos01")] style "nvl_button" text_slow_cps True
                                    if quest_intelforpeltnorth and not thais_about_banditband:
                                        textbutton '“I was in {color=#f6d6bd}Pelt of the North{/color}. The innkeeper feels uneasy about {color=#f6d6bd}Glaucia’s{/color} band.”' action [Jump("howlersdellquestionsbandits01")] style "nvl_button" text_slow_cps True
                                    elif (quest_intelforpeltnorth and thais_about_banditband and not thais_about_banditband2 and banditshideout_villagesasked_aboutattacks >= 3 and not whitemarshes_attacked and quest_intelforpeltnorth_description04) or (quest_intelforpeltnorth and thais_about_banditband and not thais_about_banditband2 and banditshideout_villagesasked_aboutattacks == 2 and not helvius_about_bandits2 and druidcave_druid_about_bandits1 and whitemarshes_attacked and quest_intelforpeltnorth_description04):
                                        textbutton '“I bring news about {color=#f6d6bd}Glaucia’s{/color} band.”' action [Jump("howlersdellquestionsbandits201")] style "nvl_button" text_slow_cps True
                                    elif (quest_intelforpeltnorth and thais_about_banditband and not thais_about_banditband2 and banditshideout_villagesasked_aboutattacks < 3 and not whitemarshes_attacked and quest_intelforpeltnorth_description04) or (quest_intelforpeltnorth and thais_about_banditband and not thais_about_banditband2 and banditshideout_villagesasked_aboutattacks == 2 and not helvius_about_bandits2 and druidcave_druid_about_bandits1 and whitemarshes_attacked and quest_intelforpeltnorth_description04):
                                        textbutton 'She’s waiting for me to learn more about the “raids” in the North.' action NullAction() style "nvl_button2" text_slow_cps True
                                    if not thais_about_greenmountaintribe and quest_reachthepaganvillage:
                                        textbutton '“What can you tell me about {color=#f6d6bd}The Tribe of The Green Mountain{/color}?”' action [Jump("howlersdellquestionsgreenmountaintribe01")] style "nvl_button" text_slow_cps True
                                    if not thais_about_altar and quest_swampaltar == 1:
                                        textbutton '“I saw a weird tree south from here. The one with the altar standing in front of it.”' action [Jump("howlersdellquestionsaltar01")] style "nvl_button" text_slow_cps True
                                    if thais_about_joiningthecity and not thais_quest_all_completed and not thais_quest_all_cancelled:
                                        if not quest_fisherhamlet:
                                            if not quest_fisherhamlet_gray:
                                                textbutton '“Do you need my assistance?”' action [Jump("howlersdellnewquests01")] style "nvl_button" text_slow_cps True
                                            elif quest_fisherhamlet_gray and (thais_friendship + howlersdell_reputation + appearance_charisma) < thais_fisherhamlet_threshold:
                                                textbutton 'She doesn’t trust me enough to give me a job.' action NullAction() style "nvl_button2" text_slow_cps True
                                            elif quest_fisherhamlet_gray and (thais_friendship + howlersdell_reputation + appearance_charisma) >= thais_fisherhamlet_threshold:
                                                textbutton '“I could use some work.”' action [Jump("howlersdellaboutfisherhamlet00")] style "nvl_button" text_slow_cps True
                                        elif quest_fisherhamlet == 1:
                                            textbutton '“About the fishing hamlet...”' action [Jump("howlersdellfisherhamletupdates01")] style "nvl_button" text_slow_cps True
                                        elif quest_fisherhamlet >= 2:
                                            if not quest_orentius_thais_description00:
                                                if whitemarshes_nomoreundead and thais_about_nomoreundead:
                                                    textbutton '“Do you need my assistance?”' action [Jump("howlersdellnewquests02")] style "nvl_button" text_slow_cps True
                                                else:
                                                    if not thais_whitemarshes_gray:
                                                        textbutton '“Do you need my assistance?”' action [Jump("howlersdellnewquests03")] style "nvl_button" text_slow_cps True
                                                    elif thais_whitemarshes_gray and (thais_friendship + howlersdell_reputation + appearance_charisma) < thais_whitemarshes_threshold:
                                                        textbutton 'She doesn’t trust me enough to give me a job.' action NullAction() style "nvl_button2" text_slow_cps True
                                                    elif thais_whitemarshes_gray and (thais_friendship + howlersdell_reputation + appearance_charisma) >= thais_whitemarshes_threshold:
                                                        textbutton '“I could use some work.”' action [Jump("howlersdellnewquests03")] style "nvl_button" text_slow_cps True
                                                    else:
                                                        textbutton '“Do you need my assistance?”' action [Jump("howlersdellnewquests03")] style "nvl_button" text_slow_cps True
                                            elif quest_orentius_thais_description00 and quest_orentius == 1:
                                                if not thais_quest_orentius_betrayal_willadmit or (quest_orentius_thais_description00betrayal and not thais_quest_orentius_betrayal_admitted and thais_quest_orentius_betrayal_willadmit):
                                                    textbutton '“About {color=#f6d6bd}White Marshes{/color}...”' action [Jump("howlersdellorentiusmagicupdates01")] style "nvl_button" text_slow_cps True
                                    if orentius_banished and not thais_about_orentius_banished:
                                        textbutton '“What will happen to {color=#f6d6bd}Orentius{/color} now, that you have him locked here?”' action [Jump("thais_about_orentius_banished01")] style "nvl_button" text_slow_cps True
                                    if item_oceannecklace and not thais_about_necklace:
                                        textbutton 'I grab the necklace I found at the hamlet. “Have you ever seen such a trinket?”' action [SetVariable("questionpreset", 0), Jump("howlersdellthaisoceannecklace01")] style "nvl_button" text_slow_cps True
                                    if quest_howlerssupport and options_thais_rumors:
                                        textbutton '“I bring {i}news{/i} about the other parts of the peninsula.”' action [Jump("howlersdellquestionsrumors01")] style "nvl_button" text_slow_cps True
                                    elif quest_howlerssupport and not options_thais_rumors:
                                        textbutton 'I have no {i}news{/i} to share.' action NullAction() style "nvl_button2" text_slow_cps True
                                    textbutton '“Thank you for your time.”' action [SetVariable("questionpreset", 0), Jump("howlersdellleavingthais01")] style "nvl_button" text_slow_cps True
                                else:
                                    if asterion_found and thais_about_asterion and not thais_about_foundasterion:
                                        textbutton '“I found {color=#f6d6bd}Asterion{/color}.”' action [Jump("howlersdellquestionsfoundasterion01")] style "nvl_button" text_slow_cps True
                                    if (not thais_about_magicfruit and not druidcave_druid_about_plague02 and druidcave_druid_about_plague01 and item_magicfruit == 1 and not oldpagos_cured and not item_magicfruit_lost) or (not thais_about_magicfruit and howlersdell_elpis_about_magicfruit and item_magicfruit == 1 and not oldpagos_cured and not item_magicfruit_lost):
                                        textbutton '“I have the Seed of Beholder. What can you give me for it?”' action [Jump("howlersdellquestionsgivingawaytheseed01fail")] style "nvl_button" text_slow_cps True
                                    if whitemarshes_nomoreundead and not whitemarshes_attacked and not thais_about_nomoreundead:
                                        if orentius_convinced:
                                            textbutton '“The necromancer of {color=#f6d6bd}White Marshes{/color} has no more control over the village, and his {i}laborers{/i} are gone.”' action [SetVariable("questionpreset", 0), Jump("howlersdellthais_about_nomoreundead01")] style "nvl_button" text_slow_cps True
                                        elif whitemarshes_destroyed:
                                            textbutton '“The necromancer of {color=#f6d6bd}White Marshes{/color} is dead, and his {i}laborers{/i} will soon start to roam through these woods. The bogs should be avoided.”' action [SetVariable("questionpreset", 0), Jump("howlersdellthais_about_nomoreundead02")] style "nvl_button" text_slow_cps True
                                    if quest_bronzerod == 1 and item_bronzerod and not thais_about_golemsrods and not eudocia_bronzerod_rodin_howlersdell:
                                        textbutton '“Do you know {color=#f6d6bd}Eudocia{/color}, the enchantress? I’d like to hang this rod on a watchtower for her.”' action [Jump("howlersdellquestionsgolems01fail")] style "nvl_button" text_slow_cps True
                                    if not thais_about_plague and oldpagos_plague_known:
                                        textbutton '“I bring sad news from {color=#f6d6bd}Old Págos{/color}. The villagers were stricken by a plague.”' action [Jump("howlersdellquestionsplague01fail")] style "nvl_button" text_slow_cps True
                                    if quest_intelforpeltnorth and not thais_about_banditband:
                                        textbutton '“I was in {color=#f6d6bd}Pelt of the North{/color}. The innkeeper feels uneasy about {color=#f6d6bd}Glaucia’s{/color} band.”' action [Jump("howlersdellquestionsbanditsMAD01")] style "nvl_button" text_slow_cps True
                                    elif (quest_intelforpeltnorth and thais_about_banditband and not thais_about_banditband2 and banditshideout_villagesasked_aboutattacks >= 3 and not whitemarshes_attacked and quest_intelforpeltnorth_description04) or (quest_intelforpeltnorth and thais_about_banditband and not thais_about_banditband2 and banditshideout_villagesasked_aboutattacks == 2 and not helvius_about_bandits2 and druidcave_druid_about_bandits1 and whitemarshes_attacked and quest_intelforpeltnorth_description04):
                                        textbutton '“I bring news about {color=#f6d6bd}Glaucia’s{/color} band.”' action [Jump("howlersdellquestionsbanditsMAD201")] style "nvl_button" text_slow_cps True
                                    elif (quest_intelforpeltnorth and thais_about_banditband and not thais_about_banditband2 and banditshideout_villagesasked_aboutattacks < 3 and not whitemarshes_attacked and quest_intelforpeltnorth_description04) or (quest_intelforpeltnorth and thais_about_banditband and not thais_about_banditband2 and banditshideout_villagesasked_aboutattacks == 2 and not helvius_about_bandits2 and druidcave_druid_about_bandits1 and whitemarshes_attacked and quest_intelforpeltnorth_description04):
                                        textbutton 'She’s waiting for me to learn more about the “raids” in the North.' action NullAction() style "nvl_button2" text_slow_cps True
                                    textbutton '“Farewell, {color=#f6d6bd}Thais{/color}.”' action [SetVariable("questionpreset", 0), Jump("howlersdellleavingthais02")] style "nvl_button" text_slow_cps True

                            elif questionpreset == "thais2":
                                # remember about $ options_thais_rumors += 1
                                if glaucia_about_steephouse3 and ruinedvillage_truth and not thais_rumor_glaucia_revenge:
                                    textbutton '“{color=#f6d6bd}Glaucia{/color} won’t forgive the way you handled {color=#f6d6bd}Steep House{/color}. Once she runs out of undead to fight with, she’ll target either you, or your people.”' action [SetVariable("thais_rumor_glaucia_revenge", 1), SetVariable("thais_rumor_counter", thais_rumor_counter+1), Jump("howleresdellthais_rumor_glaucia_revenge")] style "nvl_button" text_slow_cps True
                                if description_tulia04 and not thais_rumor_soldiers_goal:
                                    textbutton '“The soldiers who came here in spring were meant to find a good spot for a new outpost.”' action [SetVariable("thais_rumor_soldiers_goal", 1), SetVariable("thais_rumor_counter", thais_rumor_counter+1), Jump("howleresdellthais_rumor_soldiers_goal")] style "nvl_button" text_slow_cps True
                                if description_tulia01 and not thais_rumor_soldiers_leaving:
                                    textbutton '“The squad that made camp at the southern crossroads is now nothing more than two people. They plan to return to {color=#f6d6bd}Hovlavan{/color} before fall.”' action [SetVariable("thais_rumor_soldiers_leaving", 1), SetVariable("thais_rumor_counter", thais_rumor_counter+1), Jump("howleresdellthais_rumor_soldiers_leaving")] style "nvl_button" text_slow_cps True
                                if quest_studyingthegolems and not thais_rumor_monks_golems:
                                    textbutton '“{color=#f6d6bd}The monks{/color} are worried about {color=#f6d6bd}Eudocia’s{/color} golems. They asked me to make sure they’re not a threat.”' action [SetVariable("thais_rumor_monks_golems", 1), SetVariable("thais_rumor_counter", thais_rumor_counter+1), Jump("howleresdellthais_rumor_monks_golems")] style "nvl_button" text_slow_cps True
                                if monastery_cave_firsttime and not thais_rumor_monks_cave:
                                    textbutton '“I’ve been to the caves under {color=#f6d6bd}the monastery{/color}. The monks are trying to engrave the entirety of Wright’s Tablets on the walls.”' action [SetVariable("thais_rumor_monks_cave", 1), SetVariable("thais_rumor_counter", thais_rumor_counter+1), Jump("howleresdellthais_rumor_monks_cave")] style "nvl_button" text_slow_cps True
                                if not thais_rumor_creeks_missinghunters:
                                    if quest_missinghunters_vaschelfound == 2 or quest_missinghunters_vaschelfound == 3 or (quest_missinghunters_vaschelfound and quest_missinghunters_vaschelknown and quest_missinghunters):
                                        if quest_missinghunters_daliafound == 2 or quest_missinghunters_daliafound == 3 or (quest_missinghunters_daliafound and quest_missinghunters_daliaknown and quest_missinghunters):
                                            if quest_missinghunters_admonfound == 2 or quest_missinghunters_admonfound == 3 or (quest_missinghunters_admonfound and quest_missinghunters_admonknown and quest_missinghunters):
                                                textbutton '“{color=#f6d6bd}Creeks{/color} has suffered quite a blow. Three of their best hunters either died, or have disappeared.”' action [SetVariable("thais_rumor_creeks_missinghunters", 1), SetVariable("thais_rumor_counter", thais_rumor_counter+1), Jump("howleresdellthais_rumor_creeks_missinghunters")] style "nvl_button" text_slow_cps True
                                if creeks_reasonstojoin_problemsknown >= 5 and not thais_rumor_creeks_struggles:
                                    textbutton '“The people of {color=#f6d6bd}Creeks{/color} face many struggles...”' action [SetVariable("thais_rumor_creeks_struggles", 1), SetVariable("thais_rumor_counter", thais_rumor_counter+1), Jump("howleresdellthais_rumor_creeks_struggles")] style "nvl_button" text_slow_cps True
                                if severina_quest_lostmerchants_stayingsilent and not thais_rumor_galerocks_trading:
                                    textbutton '“{color=#f6d6bd}Severina{/color} of {color=#f6d6bd}Gale Rocks{/color} tries to get an edge by paying messengers to avoid your village.”' action [SetVariable("thais_rumor_galerocks_trading", 1), SetVariable("thais_rumor_counter", thais_rumor_counter+1), Jump("howleresdellthais_rumor_galerocks_trading")] style "nvl_button" text_slow_cps True
                                if (item_snakebait_truth and quest_eudociaflower and not thais_rumor_eudocia_snakebait) or (pc_class == "scholar" and quest_eudociaflower and not thais_rumor_eudocia_snakebait):
                                    textbutton '“{color=#f6d6bd}Eudocia{/color}, the enchantress, seems to be addicted to snake bait.”' action [SetVariable("thais_rumor_eudocia_snakebait", 1), SetVariable("thais_rumor_counter", thais_rumor_counter+1), Jump("howleresdellthais_rumor_eudocia_snakebait")] style "nvl_button" text_slow_cps True
                                if howlersdell_elpis_about_thais and not thais_rumor_elpis_doubt:
                                    textbutton '“As far as I can tell, {color=#f6d6bd}Elpis{/color} doesn’t hold you in high regard.”' action [SetVariable("thais_rumor_elpis_doubt", 1), SetVariable("thais_rumor_counter", thais_rumor_counter+1), Jump("howleresdellthais_rumor_elpis_doubt")] style "nvl_button" text_slow_cps True
                                if elpis_about_thyrsusgift1 and not thais_rumor_elpis_treason:
                                    textbutton '“{color=#f6d6bd}Elpis{/color} hides something from you. She wants me to go with someone to the forest garden.”' action [SetVariable("thais_rumor_elpis_treason", 1), SetVariable("thais_rumor_counter", thais_rumor_counter+1), Jump("howleresdellthais_rumor_elpis_treason")] style "nvl_button" text_slow_cps True
                                if greenmountaintribe_firsttime and not thais_rumor_greenmountaintribe_found:
                                    textbutton '“I’ve been to {color=#f6d6bd}The Tribe of The Green Mountain{/color}...”' action [SetVariable("thais_rumor_greenmountaintribe_found", 1), SetVariable("thais_rumor_counter", thais_rumor_counter+1), Jump("howleresdellthais_rumor_greenmountaintribe_found")] style "nvl_button" text_slow_cps True
                                if banditshideout_bandits_pchearedabouthideout and not thais_rumor_glaucia_found:
                                    textbutton '“I know the location of the bandits’ hideout.”' action [SetVariable("thais_rumor_glaucia_found", 1), SetVariable("thais_rumor_counter", thais_rumor_counter+1), Jump("howleresdellthais_rumor_glaucia_found")] style "nvl_button" text_slow_cps True
                                if description_glaucia06 and quest_intelforpeltnorth_description06 and not thais_rumor_glaucia_undead:
                                    textbutton '“I’ve learned why {color=#f6d6bd}Glaucia{/color} is so obsessed with taking the necromancers down.”' action [SetVariable("thais_rumor_glaucia_undead", 1), SetVariable("thais_rumor_counter", thais_rumor_counter+1), Jump("howleresdellthais_rumor_glaucia_undead")] style "nvl_button" text_slow_cps True
                                if (description_iason06 and not thais_rumor_foggylake_purchase) or (foggy_quest_iason_trade and not thais_rumor_foggylake_purchase):
                                    textbutton '“Seems like {color=#f6d6bd}[iason_name]{/color} is looking to purchase {color=#f6d6bd}Foggy Lake{/color}.”' action [SetVariable("thais_rumor_foggylake_purchase", 1), SetVariable("thais_rumor_counter", thais_rumor_counter+1), Jump("howleresdellthais_rumor_foggylake_purchase")] style "nvl_button" text_slow_cps True
                                if whitemarshes_forestgardenabandoned and not thais_rumor_forestgarden:
                                    textbutton '“The forest garden at the edge of the bogs is now mostly abandoned.”' action [SetVariable("thais_rumor_forestgarden", 1), SetVariable("thais_rumor_counter", thais_rumor_counter+1), Jump("howleresdellthais_rumor_forestgarden")] style "nvl_button" text_slow_cps True
                                if foragingground_foraging_vein and not thais_rumor_vein and not foragingground_foraging_vein_sabotaged:
                                    textbutton 'I probably should take this news straight to the guild, but... “I found a copper vein. Here, in the North.”' action [SetVariable("thais_rumor_vein", 1), SetVariable("thais_rumor_counter", thais_rumor_counter+1), Jump("howleresdellthais_rumor_vein")] style "nvl_button" text_slow_cps True
                                textbutton '“That’s all I have to say.”' action [SetVariable("questionpreset", 0), Jump("howlersdellquestionsrumors01leaving")] style "nvl_button" text_slow_cps True

                            elif questionpreset == "akakios1":
                                if not akakios_shop_firsttime:
                                    textbutton '{image=cointest} “I don’t need furniture or barrels of food. Do you have anything of use for a traveler?”' action [SetVariable("questionpreset", 0), Jump("howlersdelltraderdescribeswares01")] style "nvl_button" text_slow_cps True
                                else:
                                    if (not akakios_shop_snakebait and akakios_shop_snakebait_available) or not akakios_shop_lantern or not akakios_shop_linen or not akakios_shop_axe or akakios_quest_healingpotion_cangetback == 1:
                                        textbutton '{image=cointest} “What do you have for sale?”' action [SetVariable("questionpreset", 0), Jump("howlersdelltraderdescribeswares02")] style "nvl_button" text_slow_cps True

                                if (akakios_shop_firsttime and howlersdell_elpis_firsttime and not akakios_shop_herbs) or (akakios_shop_firsttime and description_druids02 and not akakios_shop_herbs):
                                    textbutton '“How about some useful herbs, or ointments? You do have druids around here.”' action [SetVariable("questionpreset", 0), Jump("howlersdelltraderakakios_shop_herbs")] style "nvl_button" text_slow_cps True

                                if (akakios_shop_firsttime and not akakios_shop_snakebait_available and quest_eudociaflower) or (akakios_shop_firsttime and not akakios_shop_snakebait_available and aeli_about_sharpeningpotion):
                                    textbutton '“I’m looking for flowers that look like orange tulips, but with much larger leaves. Do you grow anything like that?”' action [SetVariable("questionpreset", 0), Jump("howlersdelltraideraboutsnakebait01")] style "nvl_button" text_slow_cps True
                                textbutton '{image=cointest} “I bring goods to sell.”' action [SetVariable("questionpreset", 0), Jump("howlersdelltradersellingitems01")] style "nvl_button" text_slow_cps True
                                if not akakios_about_asterion and quest_asterion == 1 and not asterion_found:
                                    textbutton '“What can you tell me about {color=#f6d6bd}Asterion{/color}?”' action [SetVariable("questionpreset", 0), Jump("akakios_about_asterion01")] style "nvl_button" text_slow_cps True
                                if quest_thyrsusgift == 1 and not akakios_about_thyrsusgift and not item_thyrsusgift and not elpis_about_thyrsusgift1:
                                    textbutton '“{color=#f6d6bd}Thyrsus{/color} has a rather unusual request for you.”' action [SetVariable("questionpreset", 0), Jump("akakios_about_thyrsusgift")] style "nvl_button" text_slow_cps True
                                if not akakios_quest_healingpotion_about:
                                    textbutton '“Do you need any help? I could use a job.”' action [SetVariable("questionpreset", 0), Jump("howlersdelltraderquest_healingpotion01")] style "nvl_button" text_slow_cps True
                                if quest_healingpotion == 1:
                                    textbutton '“About the potion...”' action [SetVariable("questionpreset", 0), Jump("howlersdelltraderquest_healingpotionupdate01")] style "nvl_button" text_slow_cps True
                                if not quest_recruitahunter_spokento_akakios and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed:
                                    textbutton '“Did you have any issues with {color=#f6d6bd}Erastos{/color}?”' action [SetVariable("questionpreset", 0), Jump("akakios_about_recruitahunter01")] style "nvl_button" text_slow_cps True
                                if quest_healingpotion == 2 and day >= (akakios_quest_healingpotion_deadline+2) and not akakios_about_daughter:
                                    textbutton '“How’s your daughter? Did the potion work?”' action [SetVariable("questionpreset", 0), Jump("howlersdelltraderaskingaboutdaughter")] style "nvl_button" text_slow_cps True
                                if howlersdell_food_free == 1:
                                    textbutton '“{color=#f6d6bd}The mayor{/color} said you have something for me?”' action [SetVariable("questionpreset", 0), Jump("howlersdelltradergivestoken01")] style "nvl_button" text_slow_cps True
                                if item_oceannecklace and not akakios_about_necklace:
                                    textbutton 'I show him the necklace I found at the hamlet. “Have you ever seen such a trinket?”' action [SetVariable("questionpreset", 0), Jump("howlersdelltraderoceannecklace01")] style "nvl_button" text_slow_cps True
                                if not item_earplugs and northernroad_firsttime and not akakios_about_earplugs:
                                    textbutton '“I’m being bothered by the howlers. Anything to plug my ears?”' action [SetVariable("questionpreset", 0), Jump("howlersdelltraderearplugs01")] style "nvl_button" text_slow_cps True
                                textbutton '“Nothing, for now.” I walk away.' action [SetVariable("questionpreset", 0), Jump("howlersdellsquaafterinteraction01")] style "nvl_button" text_slow_cps True

                            elif questionpreset == "elpis1":
                                if not quest_fisherhamlet_description06 and not howlersdell_elpis_about_hamlet1 and rockslide_cleared:
                                    textbutton '“I was asked to speak with you about the rockslide.”' action [SetVariable("questionpreset", 0), Jump("howlersdell_elpis_about_hamlet01")] style "nvl_button" text_slow_cps True
                                elif howlersdell_elpis_about_hamlet1 and not howlersdell_elpis_about_hamlet2:
                                    if (quest_fisherhamlet_description09 or quest_fisherhamlet_description10):
                                        textbutton 'I whisper, making sure that none of the workers can hear me. “The hamlet will stay as it is.”' action [SetVariable("questionpreset", 0), Jump("howlersdell_elpis_about_hamlet02")] style "nvl_button" text_slow_cps True
                                elif howlersdell_elpis_about_hamlet1 and not howlersdell_elpis_about_hamlet3:
                                    if (quest_fisherhamlet_description07 or quest_fisherhamlet_description08):
                                        textbutton 'I whisper, making sure that none of the workers can hear me. “{color=#f6d6bd}Thais{/color} knows the truth about the hamlet.”' action [SetVariable("questionpreset", 0), Jump("howlersdell_elpis_about_hamlet03")] style "nvl_button" text_slow_cps True
                                if not thais_rumor_elpis_treason:
                                    if asterion_highisland_knowsabout and not asterion_found and not howlersdell_elpis_about_highisland:
                                        if ((howlersdell_elpis_friendship+appearance_charisma+(howlersdell_reputation/2)) < 10 and howlersdell_elpis_about_highisland01gray) or (howlersdell_elpis_friendship < 5 and howlersdell_elpis_about_highisland01gray):
                                            textbutton 'She doesn’t trust me enough to tell me about the island.' action NullAction() style "nvl_button2" text_slow_cps True
                                        elif howlersdell_elpis_about_highisland01gray:
                                            textbutton '“Maybe you could help me with {color=#f6d6bd}High Island{/color} after all?”' action [SetVariable("questionpreset", 0), Jump("howlersdellelpishighisland02")] style "nvl_button" text_slow_cps True
                                        else:
                                            textbutton '“I seek knowledge about {color=#f6d6bd}High Island{/color}.”' action [SetVariable("questionpreset", 0), Jump("howlersdellelpishighisland01")] style "nvl_button" text_slow_cps True
                                if quest_thyrsusgift == 1:
                                    if not elpis_about_thyrsusgift0:
                                        textbutton '“{color=#f6d6bd}Thyrsus{/color} has a message for you.”' action [SetVariable("questionpreset", 0), Jump("howlersdellelpis_thyrsusgift1")] style "nvl_button" text_slow_cps True
                                    else:
                                        if not elpis_about_thyrsusgift1 and not elpis_about_thyrsusgift2:
                                            if ((howlersdell_elpis_friendship+appearance_charisma+(howlersdell_reputation)) < 12) and ((howlersdell_elpis_friendship+appearance_charisma) < 4):
                                                textbutton 'She doesn’t trust me enough to help me with Thyrsus’ belongings.' action NullAction() style "nvl_button2" text_slow_cps True
                                            else:
                                                textbutton '“I still need that wand for {color=#f6d6bd}Thyrsus{/color}.”' action [SetVariable("questionpreset", 0), Jump("howlersdellelpis_thyrsusgift1alt")] style "nvl_button" text_slow_cps True
                                        elif elpis_about_thyrsusgift1 and not elpis_about_thyrsusgift2:
                                            textbutton 'She wants me to aid the locals in their mundane work.' action NullAction() style "nvl_button2" text_slow_cps True
                                if quest_ruins_choice == "thais_defeated" and not howlersdell_elpis_about_steephouseandthais:
                                    textbutton '“What’s going to happen with the village after {color=#f6d6bd}Thais’{/color} trial?”' action [SetVariable("questionpreset", 0), Jump("howlersdell_elpis_about_steephouseandthais01")] style "nvl_button" text_slow_cps True
                                if item_magicfruit == 1 and not howlersdell_elpis_about_magicfruit and not druidcave_druid_about_plague01:
                                    textbutton 'I show her the bone-like fruit. “What can you tell me about this?”' action [SetVariable("questionpreset", 0), Jump("howlersdell_elpis_about_magicfruit01")] style "nvl_button" text_slow_cps True
                                if item_magicfruit == 1 and not howlersdell_elpis_about_magicfruit and druidcave_druid_about_plague01:
                                    textbutton 'I show her the Seed of Beholder.' action [SetVariable("questionpreset", 0), Jump("howlersdell_elpis_about_magicfruit01alt")] style "nvl_button" text_slow_cps True
                                if item_magicfruit and howlersdell_elpis_about_magicfruit and not howlersdell_elpis_about_magicfruit_received:
                                    textbutton '“You can take the Seed.”' action [SetVariable("questionpreset", 0), Jump("howlersdell_elpis_about_magicfruit02")] style "nvl_button" text_slow_cps True
                                if not howlersdell_elpis_about_plague and oldpagos_firsttime and thais_about_plague and not oldpagos_cured:
                                    textbutton '“{color=#f6d6bd}Thais{/color} thinks you should know about the plague that has fallen upon {color=#f6d6bd}Old Págos{/color}.”' action [SetVariable("questionpreset", 0), Jump("howlersdell_elpis_about_plague01")] style "nvl_button" text_slow_cps True
                                elif not howlersdell_elpis_about_plague and oldpagos_firsttime and not thais_about_plague:
                                    textbutton '“I need to tell you about the plague that has fallen upon {color=#f6d6bd}Old Págos{/color}.”' action [SetVariable("questionpreset", 0), Jump("howlersdell_elpis_about_plague01alt")] style "nvl_button" text_slow_cps True
                                if not howlersdell_elpis_about_elpis:
                                    textbutton '“Why do you speak for the entire group?”' action [SetVariable("questionpreset", 0), Jump("howlersdell_elpis_about_herself01")] style "nvl_button" text_slow_cps True
                                if not quest_recruitahunter_spokento_elpis and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed:
                                    if not quest_recruitahunter_spokento_elpis_gray:
                                        textbutton '“Can you tell me anything about {color=#f6d6bd}Erastos{/color}?”' action [SetVariable("questionpreset", 0), Jump("elpis_about_recruitahunter01")] style "nvl_button" text_slow_cps True
                                    elif (howlersdell_elpis_friendship+appearance_charisma) < 5 and not quest_fisherhamlet_description06a and not howlersdell_elpis_about_hamlet2 and not thais_rumor_elpis_treason:
                                        textbutton 'She’s not willing to speak about Erastos with me.' action NullAction() style "nvl_button2" text_slow_cps True
                                    else:
                                        if not thais_rumor_elpis_treason:
                                            textbutton '“About {color=#f6d6bd}Erastos{/color}...”' action [SetVariable("questionpreset", 0), Jump("elpis_about_recruitahunter01alt")] style "nvl_button" text_slow_cps True
                                if howlersdell_elpis_about_faith < 5:
                                    textbutton '“Tell me about your faith.”' action [SetVariable("questionpreset", 0), Jump("howlersdell_elpis_about_faith01")] style "nvl_button" text_slow_cps True
                                if not howlersdell_elpis_about_asterion and quest_asterion == 1:
                                    textbutton '“Have you ever met {color=#f6d6bd}Asterion{/color}?”' action [SetVariable("questionpreset", 0), Jump("howlersdell_elpis_about_asterion01")] style "nvl_button" text_slow_cps True
                                if not thais_rumor_elpis_treason:
                                    if not howlersdell_elpis_about_healing:
                                        textbutton '“I’m looking for a healer.”' action [SetVariable("questionpreset", 0), Jump("howlersdell_elpis_about_healing01")] style "nvl_button" text_slow_cps True
                                    elif howlersdell_elpis_about_healing == 1 and howlersdell_elpis_about_plague_cured:
                                        textbutton '“Considering what I did for {color=#f6d6bd}Old Págos{/color}... Don’t you think I’m worthy of your healing abilities?”' action [SetVariable("questionpreset", 0), Jump("howlersdell_elpis_about_healing02")] style "nvl_button" text_slow_cps True
                                    elif howlersdell_elpis_about_healing == 1 and quest_ruins_choice == "thais_defeated":
                                        textbutton '“Considering that I helped you stand against {color=#f6d6bd}Thais{/color}... Don’t you think I’m worthy of your healing abilities?”' action [SetVariable("questionpreset", 0), Jump("howlersdell_elpis_about_healing02")] style "nvl_button" text_slow_cps True
                                    elif howlersdell_elpis_about_healing == 1 and howlersdell_elpis_about_magicfruit_received:
                                        textbutton '“I gave you the Seed... Don’t you think I’m worthy of your healing abilities?”' action [SetVariable("questionpreset", 0), Jump("howlersdell_elpis_about_healing02")] style "nvl_button" text_slow_cps True
                                    elif howlersdell_elpis_about_healing == 1 and item_howlersdelltoken and not howlersdell_elpis_about_magicfruit_received:
                                        textbutton '“I’m a {i}friend{/i} of {color=#f6d6bd}Howler’s Dell{/color}. Will you agree to heal me?”' action [SetVariable("questionpreset", 0), Jump("howlersdell_elpis_about_healing02")] style "nvl_button" text_slow_cps True
                                    elif howlersdell_elpis_about_healing == 2:
                                        if howlersdell_elpis_about_healing_limit == day:
                                            textbutton 'She already healed me today.' action NullAction() style "nvl_button2" text_slow_cps True
                                        elif (pc_hp > 1 and howlersdell_elpis_about_magicfruit_received) or (pc_hp > 1 and howlersdell_elpis_about_plague_cured) or (pc_hp > 0 and not howlersdell_elpis_about_magicfruit_received and not howlersdell_elpis_about_plague_cured):
                                            textbutton 'I need no immediate healing.' action NullAction() style "nvl_button2" text_slow_cps True
                                        else:
                                            textbutton '“I need healing.”' action [SetVariable("questionpreset", 0), Jump("howlersdell_elpis_about_healing03")] style "nvl_button" text_slow_cps True
                                if not howlersdell_elpis_about_archdruid and druidcave_firsttime:
                                    textbutton '“I met an old druid in a cave, south from here...”' action [SetVariable("questionpreset", 0), Jump("howlersdell_elpis_about_archdruid01")] style "nvl_button" text_slow_cps True
                                if not howlersdell_elpis_about_necromancers:
                                    textbutton '“What’s your stance on necromancy?”' action [SetVariable("questionpreset", 0), Jump("howlersdell_elpis_about_necromancers01")] style "nvl_button" text_slow_cps True
                                if not thais_rumor_elpis_treason:
                                    if not howlersdell_elpis_about_job:
                                        textbutton '“Do you need help with anything?”' action [SetVariable("questionpreset", 0), Jump("howlersdell_elpis_about_job01")] style "nvl_button" text_slow_cps True
                                if not thais_rumor_elpis_treason:
                                    if not howlersdell_elpis_about_thais and aegidia_about_thais:
                                        textbutton 'I lower my voice. “I met {color=#f6d6bd}Aegidia{/color}. She says you don’t think much of {color=#f6d6bd}Thais{/color}.”' action [SetVariable("questionpreset", 0), Jump("howlersdell_elpis_about_thais01")] style "nvl_button" text_slow_cps True
                                if not howlersdell_elpis_about_city:
                                    textbutton '“{color=#f6d6bd}Thais{/color} hopes to start negotiations with the merchant guild. What are your thoughts?”' action [SetVariable("questionpreset", 0), Jump("howlersdell_elpis_about_city01")] style "nvl_button" text_slow_cps True

                                if not thais_rumor_elpis_treason:
                                    if asterion_highisland_knowsabout and not howlersdell_elpis_about_asterion_help and quest_gatheracrew == 1 and not asterion_found and not howlersdell_elpis_about_asterion_help_blocked:
                                        if not howlersdell_elpis_about_asterion_help_gray:
                                            textbutton '“I need your help. I know where I can find {color=#f6d6bd}Asterion{/color}, but my journey will be difficult.”' action [SetVariable("questionpreset", 0), Jump("howlersdellelabouthelpingwithasterion01")] style "nvl_button" text_slow_cps True
                                        else:
                                            textbutton '“I still could use help on my journey for {color=#f6d6bd}Asterion{/color}.”' action [SetVariable("questionpreset", 0), Jump("howlersdellelabouthelpingwithasterion01alt")] style "nvl_button" text_slow_cps True
                                if not thais_rumor_elpis_treason:
                                    if howlersdell_elpis_about_asterion_help and quest_asterion == 1 and howlersdell_elpis_about_asterion_help_reward == 1 and not asterion_found:
                                        if (pc_hp < 4 and not pc_hp_can5) or (pc_hp < 5 and pc_hp_can5):
                                            textbutton '“I’m leaving to find {color=#f6d6bd}Asterion{/color}. I want you to heal my wounds.”' action [SetVariable("questionpreset", 0), Jump("howlersdellelabouthelpingwithasterion02")] style "nvl_button" text_slow_cps True
                                        else:
                                            textbutton 'I could ask her to heal my wounds before I leave to find Asterion.' action NullAction() style "nvl_button2" text_slow_cps True
                                textbutton '“Farewell.”' action [SetVariable("questionpreset", 0), Jump("howlersdellleavingdruids01")] style "nvl_button" text_slow_cps True

                            elif questionpreset == "aegidia1":
                                if quest_fisherhamlet and not aegidia_about_hamlet:
                                    $ options_aegidia += 1
                                    textbutton '“The people of {color=#f6d6bd}Howler’s Dell{/color} want me to check on this place. It belongs to them.”' action [SetVariable("questionpreset", 0), Jump("fishinghamletaegidiapcabouthamlet01")] style "nvl_button" text_slow_cps True
                                if quest_explorepeninsula == 1 and not aegidia_about_peninsula:
                                    $ options_aegidia += 1
                                    textbutton '“I’m [pcname], the roadwarden.”' action [SetVariable("questionpreset", 0), Jump("fishinghamletaegidiapcaboutthemself01")] style "nvl_button" text_slow_cps True
                                if shortcut_pcknowsabout and aegidia_about_hamlet and not aegidia_about_shortcut:
                                    $ options_aegidia += 1
                                    textbutton '“Have you ever been at the heart of the woods?”' action [SetVariable("questionpreset", 0), Jump("fishinghamletaegidia_about_shortcut01")] style "nvl_button" text_slow_cps True
                                if asterion_highisland_knowsabout and not asterion_found and aegidia_about_asterion >= 2 and not aegidia_about_highisland:
                                    $ options_aegidia += 1
                                    textbutton '“I think {color=#f6d6bd}Asterion{/color} has sailed to {color=#f6d6bd}High Island{/color}. Do you know anything about it?”' action [SetVariable("questionpreset", 0), Jump("fishinghamletaegidia_about_highisland01")] style "nvl_button" text_slow_cps True
                                if not asterion_found and quest_asterion == 1 and quest_gatheracrew == 1 and aegidia_name and aegidia_about_highisland and not aegidia_about_highisland_recruitment_done:
                                    if not aegidia_about_highisland_recruitment:
                                        $ options_aegidia += 1
                                        textbutton '“I could use your help on the island.”' action [SetVariable("questionpreset", 0), Jump("aegidia_about_highisland_recruitment01")] style "nvl_button" text_slow_cps True
                                    else:
                                        if (aegidia_friendship+appearance_charisma) >= 6:
                                            $ options_aegidia += 1
                                            textbutton '“Please, {color=#f6d6bd}Aegidia{/color}. Help me find {color=#f6d6bd}Asterion{/color}.”' action [SetVariable("questionpreset", 0), Jump("aegidia_about_highisland_recruitment02")] style "nvl_button" text_slow_cps True
                                        elif (aegidia_friendship+appearance_charisma) >= 2 and item_asterionbow:
                                            $ options_aegidia += 1
                                            textbutton '“I know you don’t trust me, but I {i}need{/i} your help on the island. I offer you {color=#f6d6bd}Asterion’s{/color} bow to show my good will.”' action [SetVariable("questionpreset", 0), Jump("aegidia_about_highisland_recruitment02alt")] style "nvl_button" text_slow_cps True
                                        else:
                                            textbutton 'She’s not willing to join my crew.' action NullAction() style "nvl_button2" text_slow_cps True
                                if asterion_found and not aegidia_highisland_joined and aegidia_name and aegidia_about_asterion >= 2 and not aegidia_about_asterion_found:
                                    $ options_aegidia += 1
                                    textbutton '“I found {color=#f6d6bd}Asterion{/color}, but I’m not bringing good news.”' action [SetVariable("questionpreset", 0), Jump("aegidia_about_asterion_found01")] style "nvl_button" text_slow_cps True
                                if ruinedvillage_confront_can and aegidia_about_hamlet and not ruinedvillage_truth and not aegidia_about_steephouse:
                                    $ options_aegidia += 1
                                    textbutton '“Do you have any idea what happened to the village in the south?”' action [SetVariable("questionpreset", 0), Jump("fishinghamletaegidia_about_steephouse01")] style "nvl_button" text_slow_cps True
                                if ruinedvillage_confront_can and aegidia_about_hamlet and ruinedvillage_truth and not aegidia_about_steephouse:
                                    $ options_aegidia += 1
                                    textbutton '“How do you feel about what happened to {color=#f6d6bd}Steep House{/color}?”' action [SetVariable("questionpreset", 0), Jump("fishinghamletaegidia_about_steephouse01alt")] style "nvl_button" text_slow_cps True
                                if ruinedvillage_truth and aegidia_about_hamlet and aegidia_about_steephouse and not aegidia_about_steephouse_truth:
                                    $ options_aegidia += 1
                                    textbutton '“I know what happened to {color=#f6d6bd}Steep House{/color}. Would you like to learn the truth?”' action [SetVariable("questionpreset", 0), Jump("fishinghamletaegidia_about_steephouse02")] style "nvl_button" text_slow_cps True
                                if quest_asterion == 1 and not asterion_found and not aegidia_about_asterion and not aegidia_name:
                                    $ options_aegidia += 1
                                    textbutton '“I’m trying to find {color=#f6d6bd}Asterion{/color}, the previous roadwarden.”' action [SetVariable("questionpreset", 0), Jump("fishinghamletaegidiapcaboutasterion01")] style "nvl_button" text_slow_cps True
                                if quest_asterion == 1 and aegidia_about_asterion < 2 and aegidia_name:
                                    if aegidia_about_asterion_gray:
                                        if (aegidia_friendship+appearance_charisma) >= 2:
                                            $ options_aegidia += 1
                                            textbutton '“Tell me about {color=#f6d6bd}Asterion{/color}.”' action [SetVariable("questionpreset", 0), Jump("fishinghamletaegidiapcaboutasterion01alt")] style "nvl_button" text_slow_cps True
                                        else:
                                            textbutton 'She doesn’t trust me enough to tell me more about Asterion.' action NullAction() style "nvl_button2" text_slow_cps True
                                    else:
                                        $ options_aegidia += 1
                                        textbutton '“Tell me about {color=#f6d6bd}Asterion{/color}.”' action [SetVariable("questionpreset", 0), Jump("fishinghamletaegidiapcaboutasterion01alt")] style "nvl_button" text_slow_cps True
                                if not aegidia_about_herself and not aegidia_name:
                                    $ options_aegidia += 1
                                    textbutton '“Who are you?”' action [SetVariable("questionpreset", 0), Jump("fishinghamletaegidiapcaboutherself01")] style "nvl_button" text_slow_cps True
                                if not aegidia_about_boat and fishinghamlet_areas_seen_07 and not aegidia_about_highisland_recruitment:
                                    $ options_aegidia += 1
                                    textbutton '“I saw your boat. If I was ever in need of borrowing one, would you care?”' action [SetVariable("questionpreset", 0), Jump("fishinghamletaegidiapcaboutboat01")] style "nvl_button" text_slow_cps True
                                if not aegidia_about_necklace1 and item_oceannecklace:
                                    $ options_aegidia += 1
                                    textbutton '“Is this your necklace?”' action [SetVariable("questionpreset", 0), Jump("fishinghamletaegidiapcaboutnecklace01")] style "nvl_button" text_slow_cps True
                                if not aegidia_about_survival and aegidia_about_herself == 2:
                                    $ options_aegidia += 1
                                    textbutton '“How did you manage to survive for so long, all by yourself?”' action [SetVariable("questionpreset", 0), Jump("fishinghamletaegidiapcabouthersurvival01")] style "nvl_button" text_slow_cps True
                                if whitemarshes_destroyed and not aegidia_about_steephouse_truth and aegidia_about_herself:
                                    $ options_aegidia += 1
                                    textbutton '“It may be better for you to leave this place, even before fall. The bogs east from here are overrun by undead.”' action [SetVariable("questionpreset", 0), Jump("fishinghamletaegidia_about_nomoreundead01")] style "nvl_button" text_slow_cps True
                                if aegidia_about_survival and item_fishtrap and aegidia_about_hamlet and not aegidia_about_fishtrap1:
                                    $ options_aegidia += 1
                                    textbutton '“I have a fish trap with me. That basket with a lid. Would you like it?”' action [SetVariable("questionpreset", 0), Jump("fishinghamletaegidiapcaboutfishtrap01")] style "nvl_button" text_slow_cps True
                                if aegidia_about_survival and item_fishtrap and aegidia_about_hamlet and aegidia_about_fishtrap1 and not aegidia_about_fishtrap2:
                                    $ options_aegidia += 1
                                    textbutton '“About that fish trap...”' action [SetVariable("questionpreset", 0), Jump("fishinghamletaegidiapcaboutfishtrap02")] style "nvl_button" text_slow_cps True
                                if not aegidia_about_arrow and item_arrow and aegidia_about_hamlet and not galerocks_florus_about_arrow:
                                    $ options_aegidia += 1
                                    textbutton 'I show her the arrow I found near the fallen tree. “Could you tell me anything about this?”' action [SetVariable("questionpreset", 0), Jump("fishinghamletaegidiapcaboutarrow01")] style "nvl_button" text_slow_cps True
                                if not quest_recruitahunter_spokento_aegidia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed:
                                    textbutton '“I bet you spent some time working with {color=#f6d6bd}Erastos{/color}?”' action [SetVariable("questionpreset", 0), Jump("aegidia_about_recruitahunter01")] style "nvl_button" text_slow_cps True
                                if not aegidia_about_resting:
                                    $ options_aegidia += 1
                                    textbutton '“Is it safe to rest here during the night?”' action [SetVariable("questionpreset", 0), Jump("fishinghamletaegidiapcaboutresting01")] style "nvl_button" text_slow_cps True
                                if not options_aegidia:
                                    textbutton 'I have nothing more to say.' action NullAction() style "nvl_button2" text_slow_cps True
                                textbutton '“It’s time for me to leave.”' action [SetVariable("questionpreset", 0), Jump("fishinghamletaegidiapcabouthamlet00")] style "nvl_button" text_slow_cps True

                            elif questionpreset == "aegidia2":
                                if not aegidia_about_payment:
                                    textbutton '“What’s in it for me?”' action [SetVariable("questionpreset", 0), Jump("fishinghamletaegidiapcabouthamlet04bpre")] style "nvl_button" text_slow_cps True
                                if not aegidia_about_hamletalone:
                                    textbutton '“Why do you want the villagers to stay away?”' action [SetVariable("questionpreset", 0), Jump("fishinghamletaegidiapcabouthamlet04cpre")] style "nvl_button" text_slow_cps True
                                if aegidia_about_hamletalone and not aegidia_about_hamletalone_doubt01:
                                    textbutton '“You don’t have the right to hinder the well-being of the entire village”' action [SetVariable("questionpreset", 0), Jump("fishinghamletaegidiapcabouthamlet04ca")] style "nvl_button" text_slow_cps True
                                if aegidia_about_hamletalone and not aegidia_about_hamletalone_doubt02:
                                    textbutton '“You {i}assume{/i} a lot. You can’t expect all your plans to succeed.”' action [SetVariable("questionpreset", 0), Jump("fishinghamletaegidiapcabouthamlet04cb")] style "nvl_button" text_slow_cps True
                                if aegidia_about_hamletalone and not aegidia_about_hamletalone_doubt03:
                                    textbutton '“The druids don’t control the village. {color=#f6d6bd}Thais{/color} does.”' action [SetVariable("questionpreset", 0), Jump("fishinghamletaegidiapcabouthamlet04cc")] style "nvl_button" text_slow_cps True
                                if aegidia_about_herself < 2 and not aegidia_name:
                                    textbutton '“Who are you, exactly?”' action [SetVariable("questionpreset", 0), Jump("fishinghamletaegidiapcabouthamlet04d")] style "nvl_button" text_slow_cps True
                                if (aegidia_about_herself and not aegidia_about_thais) or (aegidia_name and not aegidia_about_thais):
                                    textbutton '“What do you have against {color=#f6d6bd}Thais{/color}?”' action [SetVariable("questionpreset", 0), Jump("fishinghamletaegidiapcabouthamlet04e")] style "nvl_button" text_slow_cps True
                                if (aegidia_about_payment and aegidia_about_hamletalone and aegidia_about_herself) or (aegidia_about_payment and aegidia_about_hamletalone and aegidia_name):
                                    textbutton '“I’m ready to give you my answer.”' action [SetVariable("questionpreset", 0), Jump("fishinghamletaegidiapcabouthamlet05")] style "nvl_button" text_slow_cps True

                            elif questionpreset == "quintus1":
                                if not westgate_open and quintus_about_gate and item_rations >= quintus_food_gate_amount:
                                    textbutton '“I have your food rations.”' action [SetVariable("questionpreset", 0), Jump("westgatepcgivesfoodrations01")] style "nvl_button" text_slow_cps True
                                elif not westgate_open and quintus_about_gate and item_rations < quintus_food_gate_amount:
                                    textbutton 'I don’t have the [quintus_food_gate_amount] food rations that he has asked for to open the gate.' action NullAction() style "nvl_button2" text_slow_cps True
                                elif westgate_open and quarters <= (world_daylength-12):
                                    textbutton '“I’d like you to open the gate.”' action [SetVariable("questionpreset", 0), Jump("westgateenteringtheforest00")] style "nvl_button" text_slow_cps True
                                elif westgate_open and quarters > (world_daylength-12):
                                    textbutton 'I shouldn’t enter the woods at such late hour.' action NullAction() style "nvl_button2" text_slow_cps True
                                if not quintus_about_plague_cured and oldpagos_cured:
                                    textbutton '“I bring good news from {color=#f6d6bd}Old Págos{/color}. The plague is no more.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("westgateaboutcuredplague01")] style "nvl_button" text_slow_cps True
                                if quest_asterion == 1 and not asterion_found and not quintus_about_asterion:
                                    textbutton '“I’m looking for {color=#f6d6bd}Asterion{/color}.”' action [SetVariable("questionpreset", 0), Jump("westgateaboutasterion01")] style "nvl_button" text_slow_cps True
                                if not quest_recruitahunter_spokento_quintus and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed:
                                    textbutton '“Have you ever met {color=#f6d6bd}Erastos{/color}?”' action [SetVariable("questionpreset", 0), Jump("westgateaboutrecruitahunter01")] style "nvl_button" text_slow_cps True
                                if quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_westgate and not quintus_about_bronzerod:
                                    textbutton '“Do you know {color=#f6d6bd}Eudocia{/color}, the enchantress? I was wondering if you could place this in your tower for her.”' action [SetVariable("questionpreset", 0), Jump("westgateaboutbronzerod01")] style "nvl_button" text_slow_cps True
                                elif quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_westgate and quintus_about_bronzerod and item_rations >= quintus_food_bronzerod_amount:
                                    textbutton '“Here’s the food you asked for. And here’s the bronze rod.”' action [SetVariable("questionpreset", 0), Jump("westgategivesbronzerod01")] style "nvl_button" text_slow_cps True
                                elif quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_westgate and quintus_about_bronzerod and item_rations < quintus_food_bronzerod_amount:
                                    textbutton 'He asked me for [quintus_food_bronzerod_amount] food rations for putting a rod here.' action NullAction() style "nvl_button2" text_slow_cps True
                                if not quintus_about_shortcut:
                                    textbutton '“What can you tell me about the road behind the gate?”' action [SetVariable("questionpreset", 0), Jump("westgateaboutshortcut01")] style "nvl_button" text_slow_cps True
                                if quintus_about_shortcut and not quintus_about_shortcut2:
                                    textbutton '“If no one uses this road... Why are you here?”' action [SetVariable("questionpreset", 0), Jump("westgateaboutshortcut02")] style "nvl_button" text_slow_cps True
                                if asterion_highisland_knowsabout and not asterion_found and not quintus_about_highisland:
                                    textbutton '“Have you ever heard about {color=#f6d6bd}High Island{/color}?”' action [SetVariable("questionpreset", 0), Jump("westgateabouthighisland01")] style "nvl_button" text_slow_cps True
                                if quest_missinghunters == 1 and not quintus_about_missinghunters:
                                    textbutton '“Some time ago, a few people from {color=#f6d6bd}Creeks{/color} left their home to hunt. Have you met them?”' action [SetVariable("questionpreset", 0), Jump("westgateaboutmissinghunters01")] style "nvl_button" text_slow_cps True
                                if shortcut_darkforest_furlesswolf and quintus_about_missinghunters and not quintus_about_vaschel:
                                    textbutton '“I think {color=#f6d6bd}Vaschel’s{/color} died somewhere at the heart of the woods.”' action [SetVariable("questionpreset", 0), Jump("westgateaboutvascheldead01")] style "nvl_button" text_slow_cps True
                                if not quintus_about_oldpagos:
                                    textbutton '“What’s it like to live in {color=#f6d6bd}Old Págos{/color}?”' action [SetVariable("questionpreset", 0), Jump("westgateaboutoldpagos01")] style "nvl_button" text_slow_cps True
                                if (quest_intelforpeltnorth == 1 and not quintus_about_bandits) or (banditshideout_bandits_pchearedabout == 1 and not quintus_about_bandits):
                                    textbutton '“I’ve heard about some bandits. Were they bothering you?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), SetVariable("quintus_about_bandits", 1), Jump("westgateaboutbandits01")] style "nvl_button" text_slow_cps True
                                if (quest_intelforpeltnorth == 1 and quintus_about_bandits == 1) or (banditshideout_firsttime and quintus_about_bandits == 1):
                                    if quintus_about_bandits_gray:
                                        if (quintus_friendship+appearance_charisma) >= 4:
                                            textbutton '“Why are you afraid of {color=#f6d6bd}Glaucia{/color}?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), SetVariable("quintus_about_bandits", 1), Jump("westgateaboutbandits02")] style "nvl_button" text_slow_cps True
                                        else:
                                            textbutton 'He doesn’t trust me enough to say anything about Glaucia.' action NullAction() style "nvl_button2" text_slow_cps True
                                    else:
                                        textbutton '“Why are you afraid of {color=#f6d6bd}Glaucia{/color}?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), SetVariable("quintus_about_bandits", 1), Jump("westgateaboutbandits02")] style "nvl_button" text_slow_cps True
                                if shortcut_ibex_knows and not quintus_about_ibex and not oldpagos_about_ibex:
                                    textbutton '“Any idea who could be the owner of an ibex marked with a red knot?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("westgateaboutibex01")] style "nvl_button" text_slow_cps True
                                if item_gambesonrepairset and not quintus_about_gambesonrepairset and quintus_attitude != "intimidating":
                                    textbutton '“Need any help with your gambeson? With the repair tools I have, we could fix it together in about an hour.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("westgateaboutgambesonrepairset01")] style "nvl_button" text_slow_cps True
                                if not quintus_about_staying:
                                    textbutton '“Shouldn’t you look for a real shelter?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("westgateaboutstaying01")] style "nvl_button" text_slow_cps True
                                if quintus_about_staying and not quintus_about_leaving:
                                    textbutton '“You could at least spend the nighttime in one of the villages.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("westgateaboutleaving1")] style "nvl_button" text_slow_cps True
                                if quintus_about_leaving and westgate_open and not quintus_left_gate_about:
                                    textbutton '“But seriously, you’re tempting the forest. You need to seek shelter.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("quintus_left_gate_about01")] style "nvl_button" text_slow_cps True
                                if quintus_left_gate_about and not quintus_left_gate:
                                    textbutton '“About your {i}duty{/i}...”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("quintus_left_gate_about02alt")] style "nvl_button" text_slow_cps True

                            elif questionpreset == "quintus2":
                                if not quintus_about_plague_cured and oldpagos_cured:
                                    textbutton '“I bring good news from {color=#f6d6bd}Old Págos{/color}. The plague is no more.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("pelt_westgateaboutcuredplague01")] style "nvl_button" text_slow_cps True
                                if quest_asterion == 1 and not asterion_found and not quintus_about_asterion:
                                    textbutton '“I’m looking for {color=#f6d6bd}Asterion{/color}.”' action [SetVariable("questionpreset", 0), Jump("pelt_westgateaboutasterion01")] style "nvl_button" text_slow_cps True
                                if not quest_recruitahunter_spokento_quintus and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed:
                                    textbutton '“Have you ever met {color=#f6d6bd}Erastos{/color}?”' action [SetVariable("questionpreset", 0), Jump("pelt_westgateaboutrecruitahunter01")] style "nvl_button" text_slow_cps True
                                if not quintus_about_shortcut:
                                    textbutton '“What can you tell me about the road behind the gate?”' action [SetVariable("questionpreset", 0), Jump("pelt_westgateaboutshortcut01")] style "nvl_button" text_slow_cps True
                                if not asterion_found and quest_asterion == 1 and quest_gatheracrew == 1 and quintus_left_gate and quintus_about_highisland and not quintus_about_highisland_recruitment:
                                    textbutton '“I need you to return the favor. I’m heading for {color=#f6d6bd}High Island{/color}.”' action [SetVariable("questionpreset", 0), Jump("pelt_westgateabouthighisland_recruitment01")] style "nvl_button" text_slow_cps True
                                if asterion_highisland_knowsabout and not asterion_found and not quintus_about_highisland:
                                    textbutton '“Have you ever heard about {color=#f6d6bd}High Island{/color}?”' action [SetVariable("questionpreset", 0), Jump("pelt_westgateabouthighisland01")] style "nvl_button" text_slow_cps True
                                if quest_missinghunters == 1 and not quintus_about_missinghunters:
                                    textbutton '“Some time ago, a few people from {color=#f6d6bd}Creeks{/color} left their home to hunt. Have you met them?”' action [SetVariable("questionpreset", 0), Jump("pelt_westgateaboutmissinghunters01")] style "nvl_button" text_slow_cps True
                                if shortcut_darkforest_furlesswolf and quintus_about_missinghunters and not quintus_about_vaschel:
                                    textbutton '“I think {color=#f6d6bd}Vaschel’s{/color} died somewhere at the heart of the woods.”' action [SetVariable("questionpreset", 0), Jump("pelt_westgateaboutvascheldead01")] style "nvl_button" text_slow_cps True
                                if not quintus_about_oldpagos:
                                    textbutton '“What’s it like to live in {color=#f6d6bd}Old Págos{/color}?”' action [SetVariable("questionpreset", 0), Jump("pelt_westgateaboutoldpagos01")] style "nvl_button" text_slow_cps True
                                if (quest_intelforpeltnorth == 1 and not quintus_about_bandits) or (banditshideout_bandits_pchearedabout == 1 and not quintus_about_bandits):
                                    textbutton '“I’ve heard about some bandits. Were they bothering you?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), SetVariable("quintus_about_bandits", 1), Jump("pelt_westgateaboutbandits01")] style "nvl_button" text_slow_cps True
                                if (quest_intelforpeltnorth == 1 and quintus_about_bandits == 1) or (banditshideout_firsttime and quintus_about_bandits == 1):
                                    if quintus_about_bandits_gray:
                                        if (quintus_friendship+appearance_charisma) >= 4:
                                            textbutton '“Why are you afraid of {color=#f6d6bd}Glaucia{/color}?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), SetVariable("quintus_about_bandits", 1), Jump("pelt_westgateaboutbandits02")] style "nvl_button" text_slow_cps True
                                        else:
                                            textbutton 'He doesn’t trust me enough to say anything about Glaucia.' action NullAction() style "nvl_button2" text_slow_cps True
                                    else:
                                        textbutton '“Why are you afraid of {color=#f6d6bd}Glaucia{/color}?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), SetVariable("quintus_about_bandits", 1), Jump("pelt_westgateaboutbandits02")] style "nvl_button" text_slow_cps True
                                if shortcut_ibex_knows and not quintus_about_ibex and not oldpagos_about_ibex:
                                    textbutton '“Any idea who could be the owner of an ibex marked with a red knot?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("pelt_westgateaboutibex01")] style "nvl_button" text_slow_cps True
                                textbutton 'I take another look at the main hall.' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 1), SetVariable("questionpreset", 0), Jump("peltnorth01insidechoosenpc")] style "nvl_button" text_slow_cps True
                                textbutton 'I go outside.' action [SetVariable("can_rest", 0), SetVariable("can_items", 1), SetVariable("questionpreset", 0), Jump("leavingthepeltnorth")] style "nvl_button" text_slow_cps True

                            elif questionpreset == "oldpagos":
                                if quest_healingtheplague_description01 and not oldpagos_about_druidsplan and not oldpagos_cured:
                                    $ options_oldpagos += 1
                                    textbutton 'I tell them about the druid’s plan.' action [SetVariable("questionpreset", 0), Jump("oldpagos_about_druidplan01")] style "nvl_button" text_slow_cps True
                                elif quest_healingtheplague_description01 and oldpagos_about_druidsplan == 1 and not oldpagos_cured and (oldpagos_reputation+appearance_charisma) >= 5:
                                    $ options_oldpagos += 1
                                    textbutton '“I still need help with awakening the altar.”' action [SetVariable("questionpreset", 0), Jump("oldpagos_about_awakeningaltar01")] style "nvl_button" text_slow_cps True
                                elif quest_healingtheplague_description01 and oldpagos_about_druidsplan == 1 and not oldpagos_cured and (oldpagos_reputation+appearance_charisma) < 5:
                                    textbutton 'They don’t trust me enough to help me with awakening the altar.' action NullAction() style "nvl_button2" text_slow_cps True
                                if not oldpagos_plague_known and not oldpagos_cured:
                                    $ options_oldpagos += 1
                                    textbutton '“Tell me more about this illness. What does it do?”' action [SetVariable("questionpreset", 0), Jump("oldpagos_about_plague01")] style "nvl_button" text_slow_cps True
                                if oldpagos_plague_known and not oldpagos_cured and not oldpagos_about_harvest:
                                    $ options_oldpagos += 1
                                    textbutton '“Why don’t you harvest your crops?”' action [SetVariable("questionpreset", 0), Jump("oldpagos_about_harvest01")] style "nvl_button" text_slow_cps True
                                if not orentius_met and not whitemarshes_attacked and not whitemarshes_nomoreundead:
                                    if quest_orentius == 1 and quest_orentius_thais_description00 and not quest_orentius_thais_description00betrayal and not thais_defeated and not quest_orentius_thais_description10 and quest_orentius_thais_description03 and not quest_orentius_thais_description03a02:
                                        $ options_oldpagos += 1
                                        textbutton '“I have a delicate matter to discuss. It’s about the necromancers of {color=#f6d6bd}White Marshes{/color}.”' action [SetVariable("questionpreset", 0), Jump("oldpagos_about_quest_orentius_thais_description01")] style "nvl_button" text_slow_cps True
                                elif whitemarshes_nomoreundead and not oldpagos_about_nomoreundead:
                                    if orentius_convinced:
                                        $ options_oldpagos += 1
                                        textbutton '“The undead of {color=#f6d6bd}White Marshes{/color} are gone. I hope you’ll have an opportunity to trade with the tribe in spring.”' action [SetVariable("questionpreset", 0), Jump("oldpagos_about_nomoreundead01")] style "nvl_button" text_slow_cps True
                                    elif orentius_banished:
                                        $ options_oldpagos += 1
                                        textbutton '“The undead of {color=#f6d6bd}White Marshes{/color} are gone, but I wouldn’t expect the tribe to be open to trade in the near future.”' action [SetVariable("questionpreset", 0), Jump("oldpagos_about_nomoreundead02")] style "nvl_button" text_slow_cps True
                                    elif whitemarshes_destroyed:
                                        $ options_oldpagos += 1
                                        textbutton '“Since you’re placed closely to {color=#f6d6bd}White Marshes{/color}, you must double your guards. The village is overtaken by undead.”' action [SetVariable("questionpreset", 0), Jump("oldpagos_about_nomoreundead03")] style "nvl_button" text_slow_cps True
                                if quest_asterion == 1 and not asterion_found and not oldpagos_about_asterion:
                                    $ options_oldpagos += 1
                                    textbutton '“I’m looking for {color=#f6d6bd}Asterion{/color}, the previous roadwarden.”' action [SetVariable("questionpreset", 0), Jump("oldpagos_about_asterion01")] style "nvl_button" text_slow_cps True
                                if not quest_recruitahunter_spokento_tertia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed:
                                    $ options_oldpagos += 1
                                    textbutton '“Have you ever met {color=#f6d6bd}Erastos{/color}?”' action [SetVariable("questionpreset", 0), Jump("oldpagos_about_recruitahunter01")] style "nvl_button" text_slow_cps True
                                if oldpagos_about_asterion and not oldpagos_about_watchtower_directions:
                                    $ options_oldpagos += 1
                                    textbutton '“Which way would you take if you were to travel to the watchtower?”' action [SetVariable("questionpreset", 0), Jump("oldpagos_about_watchtower_directions01")] style "nvl_button" text_slow_cps True
                                if eudocia_about_plague and not oldpagos_about_eudocia_parents:
                                    $ options_oldpagos += 1
                                    textbutton '“{color=#f6d6bd}Eudocia{/color}, the enchantress from the east, wants to know if {color=#f6d6bd}Eulalia{/color} and {color=#f6d6bd}Ireneus{/color} have avoided the sickness.”' action [SetVariable("questionpreset", 0), Jump("oldpagos_about_eudocia_parents01")] style "nvl_button" text_slow_cps True
                                if quest_asterion_description08 and not oldpagos_about_keys and item_asterionkey:
                                    $ options_oldpagos += 1
                                    textbutton '“I happened to recover the key you gave {color=#f6d6bd}Asterion{/color}. I’m ready to return it.”' action [SetVariable("questionpreset", 0), Jump("oldpagosreturningkey01")] style "nvl_button" text_slow_cps True
                                if asterion_highisland_knowsabout and not asterion_found and not oldpagos_about_highisland:
                                    $ options_oldpagos += 1
                                    textbutton '“I’m trying to learn more about {color=#f6d6bd}High Island{/color}.”' action [SetVariable("questionpreset", 0), Jump("oldpagos_about_highisland01")] style "nvl_button" text_slow_cps True
                                if quest_missinghunters == 1 and not oldpagos_about_missinghunters:
                                    $ options_oldpagos += 1
                                    textbutton '“Are there any hunters from {color=#f6d6bd}Creeks{/color} locked in there with you?”' action [SetVariable("questionpreset", 0), Jump("oldpagos_about_missinghunters01")] style "nvl_button" text_slow_cps True
                                if banditshideout_bandits_pchearedabout and not oldpagos_about_bandits:
                                    $ options_oldpagos += 1
                                    textbutton '“Were you bothered by any bandits in recent seasons?”' action [SetVariable("questionpreset", 0), Jump("oldpagos_about_bandits01")] style "nvl_button" text_slow_cps True
                                if ruinedvillage_confront_can and oldpagos_about_howlersdell and not ruinedvillage_truth and not oldpagos_about_steephouse:
                                    if eudocia_about_steephouse and not oldpagos_about_steephouse_eudocia and oldpagos_about_steephouse_gray:
                                        $ options_oldpagos += 1
                                        textbutton '“{color=#f6d6bd}Eudocia{/color} has a message for you. {i}The warden ought to know about {color=#f6d6bd}Steep House{/color}, {color=#f6d6bd}Little Otter{/color}{/i}.”' action [SetVariable("questionpreset", 0), Jump("oldpagos_about_steephouse_eudocia01")] style "nvl_button" text_slow_cps True
                                    elif (oldpagos_reputation+appearance_charisma) >= (oldpagos_about_steephouse_reputation-2) and oldpagos_about_steephouse_gray and item_wingedhourglass_worn:
                                        $ options_oldpagos += 1
                                        textbutton 'I grab the hourglass on my neck and show it to her. “For Wright’s truth, tell me what happened to the village in the south. These people deserve justice!”' action [SetVariable("questionpreset", 0), Jump("oldpagos_about_steephouse02alt")] style "nvl_button" text_slow_cps True
                                    elif (oldpagos_reputation+appearance_charisma) >= oldpagos_about_steephouse_reputation and oldpagos_about_steephouse_gray and not item_wingedhourglass_worn:
                                        $ options_oldpagos += 1
                                        textbutton '“Please, {color=#f6d6bd}Tertia{/color}. I need to learn the truth about the village in the south. These people deserve justice.”' action [SetVariable("questionpreset", 0), Jump("oldpagos_about_steephouse02")] style "nvl_button" text_slow_cps True
                                    elif oldpagos_about_steephouse_gray:
                                        textbutton 'She’s still not willing {i}to break her duty{/i} by telling me about the ruins.' action NullAction() style "nvl_button2" text_slow_cps True
                                    else:
                                        $ options_oldpagos += 1
                                        textbutton '“You told me that {color=#f6d6bd}Thais{/color} had grand plans ten years ago. Is this related to the ruins in the south?”' action [SetVariable("questionpreset", 0), Jump("oldpagos_about_steephouse01")] style "nvl_button" text_slow_cps True
                                if not oldpagos_about_trade and not oldpagos_cured:
                                    $ options_oldpagos += 1
                                    textbutton '“Do you have anything for sale? Maybe some food rations?”' action [SetVariable("questionpreset", 0), Jump("oldpagos_about_trade01")] style "nvl_button" text_slow_cps True
                                if not oldpagos_about_othervillages and not oldpagos_plague_helpfromgalerocks and not oldpagos_cured:
                                    $ options_oldpagos += 1
                                    textbutton '“Don’t you want me to ask the other villages for help?”' action [SetVariable("questionpreset", 0), Jump("oldpagos_about_othervillages01")] style "nvl_button" text_slow_cps True
                                elif (oldpagos_plague_helpfromgalerocks and not oldpagos_about_othervillages) or (oldpagos_cured and not oldpagos_about_othervillages ):
                                    $ options_oldpagos += 1
                                    textbutton '“Why didn’t you want me to ask the other villages for help?”' action [SetVariable("questionpreset", 0), Jump("oldpagos_about_othervillages01")] style "nvl_button" text_slow_cps True
                                if (oldpagos_about_othervillages and oldpagos_about_4villages < 4 and not quest_reachthepaganvillage) or (oldpagos_about_othervillages and oldpagos_about_4villages < 5 and quest_reachthepaganvillage):
                                    if oldpagos_about_othervillages_gray:
                                        if (oldpagos_reputation+appearance_charisma) >= 4:
                                            $ options_oldpagos += 1
                                            textbutton '“I’d like to hear what you have to say about the other villages.”' action [SetVariable("questionpreset", 0), Jump("oldpagos_about_4villages01")] style "nvl_button" text_slow_cps True
                                        else:
                                            textbutton 'She doesn’t trust me enough to say anything more about the other villages.' action NullAction() style "nvl_button2" text_slow_cps True
                                    else:
                                        $ options_oldpagos += 1
                                        textbutton '“I’d like to hear what you have to say about the other villages.”' action [SetVariable("questionpreset", 0), Jump("oldpagos_about_4villages01")] style "nvl_button" text_slow_cps True
                                if westgate_firsttime and not oldpagos_about_quintus:
                                    $ options_oldpagos += 1
                                    if oldpagos_about_watchtower_directions:
                                        textbutton '“I met {color=#f6d6bd}Quintus{/color}. He’s doing... fine.”' action [SetVariable("questionpreset", 0), Jump("oldpagos_about_quintus01")] style "nvl_button" text_slow_cps True
                                    else:
                                        textbutton '“I met {color=#f6d6bd}Quintus{/color}, the gatekeeper. He’s doing... fine.”' action [SetVariable("questionpreset", 0), Jump("oldpagos_about_quintus01")] style "nvl_button" text_slow_cps True
                                if oldpagos_plague_warnedplaces >= 6 and not oldpagos_about_oldpagos_plague_warnedplaces:
                                    $ options_oldpagos += 1
                                    textbutton '“I’ve been in many settlements, warning the locals about the plague. You don’t have to worry about their safety.”' action [SetVariable("questionpreset", 0), Jump("oldpagos_about_warningothervillages01")] style "nvl_button" text_slow_cps True
                                if oldpagos_plague_warnedplaces < 6 and not oldpagos_about_oldpagos_plague_warnedplaces and oldpagos_firsttime_day < (day-2):
                                    $ options_oldpagos += 1
                                    textbutton '(lie) “I’ve been in many settlements, warning the locals about the plague. You don’t have to worry about their safety.”' action [SetVariable("questionpreset", 0), Jump("oldpagos_about_warningothervillages01lie")] style "nvl_button" text_slow_cps True
                                if shortcut_ibex_knows and not oldpagos_about_ibex:
                                    $ options_oldpagos += 1
                                    textbutton '“I found an ibex marked with a red knot. Was it any of yours?”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("oldpagos_about_ibex01")] style "nvl_button" text_slow_cps True
                                if oldpagos_about_bogroadcat_introduction and bogroad_triedtohelp and not oldpagos_about_bogroadcat:
                                    $ options_oldpagos += 1
                                    textbutton '“That weird creature from the bogs you told me about... I’ve quite a story for you.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("oldpagos_about_bogroadmonster01")] style "nvl_button" text_slow_cps True
                                if quest_matchmaking == 1 and not oldpagos_about_matchmaking:
                                    $ options_oldpagos += 1
                                    textbutton '“People from the other tribes are looking for spouses.”' action [SetVariable("can_leave", 0), SetVariable("can_rest", 0), SetVariable("can_items", 0), SetVariable("questionpreset", 0), Jump("oldpagos_about_matchmaking01")] style "nvl_button" text_slow_cps True
                                if not options_oldpagos:
                                    textbutton 'There’s nothing else I can think of.' action NullAction() style "nvl_button2" text_slow_cps True

                            elif questionpreset == "monastery1":
                                if not whitemarshes_firsttime and not aeli_about_necromancers_question01:
                                    $ options_monastery_about_necromancers += 1
                                if whitemarshes_firsttime and not aeli_about_necromancers_question01:
                                    $ options_monastery_about_necromancers += 1
                                if aeli_about_necromancers_question01 and not aeli_about_necromancers_question04:
                                    $ options_monastery_about_necromancers += 1
                                if not aeli_about_necromancers_question02:
                                    $ options_monastery_about_necromancers += 1
                                if sleep_whitemarshes and aeli_about_necromancers_question02 and aeli_about_necromancers_question04 and not aeli_about_necromancers_bloodmagic:
                                    $ options_monastery_about_necromancers += 1
                                if aeli_about_necromancers_question02 and not aeli_about_necromancers_question03:
                                    $ options_monastery_about_necromancers += 1
                                if aeli_about_necromancers_question04 and not aeli_about_necromancers_question05:
                                    $ options_monastery_about_necromancers += 1
                                if not aeli_about_monasteryname:
                                    $ options_monastery_about_order += 1
                                if not aeli_about_thisplace:
                                    $ options_monastery_about_order += 1
                                if not aeli_about_leader and pc_religion != "ordersoftruth" and not monastery_prelate_invited:
                                    $ options_monastery_about_order += 1
                                if not aeli_about_leader and pc_religion == "ordersoftruth" and not monastery_prelate_invited:
                                    $ options_monastery_about_order += 1
                                if not aeli_about_theirfaith:
                                    $ options_monastery_about_order += 1
                                if not aeli_about_aeli:
                                    $ options_monastery_about_order += 1
                                if not aeli_about_hiddenknowledge:
                                    $ options_monastery_about_order += 1
                                if not oldpagos_cured and not aeli_about_plague1:
                                    $ options_monastery += 1
                                    textbutton '“Is there nothing you can do about the plague that has beset {color=#f6d6bd}Old Págos{/color}?”' action [SetVariable("questionpreset", 0), Jump("aeli_about_plague01")] style "nvl_button" text_slow_cps True
                                if not aeli_about_plague2 and oldpagos_cured:
                                    $ options_monastery += 1
                                    textbutton '“I bring news from {color=#f6d6bd}Old Págos{/color}. The plague is no more.”' action [SetVariable("questionpreset", 0), Jump("aeli_about_healedplague01")] style "nvl_button" text_slow_cps True
                                if not monastery_cave_firsttime and monastery_prelate_invited:
                                    if (monastery_friendship+appearance_charisma) > 10:
                                        $ options_monastery += 1
                                        textbutton '“Will {color=#f6d6bd}the prelate{/color} agree to meet with me?”' action [SetVariable("questionpreset", 0), Jump("monasteryrespondingtoinvitationtomeetprelate01")] style "nvl_button" text_slow_cps True
                                    elif (monastery_friendship+appearance_charisma) <= 10:
                                        textbutton 'He’s not willing to take me to the prelate yet.' action NullAction() style "nvl_button2" text_slow_cps True
                                    if aeli_about_asterion and foragingground_foraging_vein and not foragingground_foraging_vein_sabotaged and not aeli_about_copper:
                                        if (monastery_friendship+appearance_charisma) > 7:
                                            $ options_monastery += 1
                                            textbutton 'I should take it directly to the guild, but... “To prove my good will, I’m ready to tell you about the copper vein I found in the North.”' action [Jump("aeli_about_copper01")] style "nvl_button" text_slow_cps True
                                    elif (monastery_friendship+appearance_charisma) <= 7:
                                        textbutton 'I could tell him about the copper vein I found, but I doubt it’ll be enough to convince him.' action NullAction() style "nvl_button2" text_slow_cps True
                                if quest_orentius == 1 and quest_orentius_thais_description00 and not orentius_met and not whitemarshes_attacked and not quest_orentius_thais_description00betrayal and not thais_defeated and not quest_orentius_thais_description10:
                                    if quest_orentius_thais_description03 and not quest_orentius_thais_description03a03:
                                        $ options_monastery += 1
                                        textbutton '“I have a delicate matter to discuss. It’s about {color=#f6d6bd}Orentius{/color}.”' action [SetVariable("questionpreset", 0), Jump("aeli_about_quest_orentius_thais_description01")] style "nvl_button" text_slow_cps True
                                if quest_spiritrock == 1 and galerocks_photios_quest_spiritrock_question_doubt and not aeli_about_spiritrock:
                                    $ options_monastery += 1
                                    textbutton 'I ask him about {color=#f6d6bd}Phoibe{/color} and the spirit rock.' action [SetVariable("questionpreset", 0), Jump("aeli_about_phoibe01")] style "nvl_button" text_slow_cps True
                                if quest_asterion == 1 and not aeli_about_asterion and not asterion_found:
                                    $ options_monastery += 1
                                    textbutton '“What can you tell me about {color=#f6d6bd}Asterion{/color}?”' action [SetVariable("questionpreset", 0), Jump("aeli_about_asterion01")] style "nvl_button" text_slow_cps True
                                if asterion_highisland_knowsabout and not asterion_found and not aeli_about_highisland and not aeli_about_secret_highisland:
                                    $ options_monastery += 1
                                    textbutton '“I seek knowledge about {color=#f6d6bd}High Island{/color}.”' action [SetVariable("questionpreset", 0), Jump("aeli_about_highisland01")] style "nvl_button" text_slow_cps True
                                if not quest_recruitahunter_spokento_aeli and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed:
                                    $ options_monastery += 1
                                    textbutton '“What can you tell me about {color=#f6d6bd}Erastos{/color}?”' action [SetVariable("questionpreset", 0), Jump("aeli_about_recruitahunter01")] style "nvl_button" text_slow_cps True
                                if shortcut_pcknowsabout and not aeli_about_shortcut:
                                    $ options_monastery += 1
                                    textbutton '“Do you know anything interesting about the path leading through the heart of the woods?”' action [SetVariable("questionpreset", 0), Jump("aeli_about_shortcut01")] style "nvl_button" text_slow_cps True
                                if quest_missinghunters == 1 and not aeli_about_missinghunters:
                                    $ options_monastery += 1
                                    textbutton '“I’m looking for a few hunters from {color=#f6d6bd}Creeks{/color}. Were they here?”' action [SetVariable("questionpreset", 0), Jump("monasterymissinghunters01")] style "nvl_button" text_slow_cps True
                                if ruinedvillage_confront_can and not ruinedvillage_truth and not aeli_about_steephouse:
                                    $ options_monastery += 1
                                    textbutton '“What can you tell me about the ruins of the village in the south?”' action [SetVariable("questionpreset", 0), Jump("aeli_about_steephouse01")] style "nvl_button" text_slow_cps True
                                if banditshideout_bandits_pchearedabout and not aeli_about_bandits:
                                    $ options_monastery += 1
                                    textbutton '“I’m trying to learn more about the local bandits.”' action [SetVariable("questionpreset", 0), Jump("aeli_about_bandits01")] style "nvl_button" text_slow_cps True
                                if quest_bronzerod == 1 and item_bronzerod and not aeli_about_bronzerod:
                                    $ options_monastery += 1
                                    textbutton '“{color=#f6d6bd}Eudocia{/color}, the enchantress, wants to place these rods in high points across the peninsula. Can you help me out?”' action [SetVariable("questionpreset", 0), Jump("aeli_about_bronzerod01")] style "nvl_button" text_slow_cps True
                                if not aeli_quest_pens:
                                    if aeli_quest_pens_gray:
                                        if (monastery_friendship+appearance_charisma) < 4:
                                            textbutton 'He doesn’t trust me enough to give me any job, at least for now.' action NullAction() style "nvl_button2" text_slow_cps True
                                        else:
                                            $ options_monastery += 1
                                            textbutton '“Do you need any help? I’m looking for a job.”' action [SetVariable("questionpreset", 0), Jump("aeli_quest_pens_question")] style "nvl_button" text_slow_cps True
                                    else:
                                        $ options_monastery += 1
                                        textbutton '“Do you need any help? I’m looking for a job.”' action [SetVariable("questionpreset", 0), Jump("aeli_quest_pens_question")] style "nvl_button" text_slow_cps True
                                if quest_pensformonastery == 1 or quest_studyingthegolems == 1 or monastery_promise == 1:
                                    textbutton '“About the things you asked me to do...”' action [SetVariable("questionpreset", 0), Jump("aeli_about_quests01")] style "nvl_button" text_slow_cps True
                                if options_monastery_about_order:
                                    $ options_monastery += 1
                                    textbutton '“I have some questions about the monastery.”' action [SetVariable("questionpreset", 0), Jump("aeli_about_monastery01")] style "nvl_button" text_slow_cps True
                                if not monastery_sleep_unlocked and not aeli_about_sleeping1 and not aeli_about_plague2 and not aeli_quest_pens_reward == "shelter":
                                    $ options_monastery += 1
                                    textbutton '“Why can’t I spend a night here?”' action [SetVariable("questionpreset", 0), Jump("aeli_about_sleeping1")] style "nvl_button" text_slow_cps True
                                if not monastery_sleep_unlocked and oldpagos_cured and aeli_about_plague2 and not aeli_quest_pens_reward == "shelter":
                                    $ options_monastery += 1
                                    textbutton '“The plague is gone. Can I spend a night here?”' action [SetVariable("questionpreset", 0), Jump("aeli_about_sleeping2")] style "nvl_button" text_slow_cps True
                                if not item_snakebait_truth and pc_class != "scholar" and item_snakebait and not aeli_about_snakebait:
                                    $ options_monastery += 1
                                    textbutton '“I found some snake bait... Is it safe for humans?”' action [SetVariable("questionpreset", 0), Jump("aeli_about_snakebait01")] style "nvl_button" text_slow_cps True
                                if aeli_about_buyingorselling and aeli_about_plague2 and pc_class != "scholar":
                                    if not aeli_about_sharpeningpotion:
                                        $ options_monastery += 1
                                        textbutton '“With the plague gone... Would you brew something that could help me in my journey?”' action [SetVariable("questionpreset", 0), Jump("aeli_about_sharpeningpotion")] style "nvl_button" text_slow_cps True
                                    elif not aeli_about_sharpeningpotion_timer:
                                        if not item_snakebait and not item_cavemushroom:
                                            textbutton 'He wants me to find him a cave ear mushroom and a snake bait flower.' action NullAction() style "nvl_button2" text_slow_cps True
                                        elif not item_snakebait:
                                            textbutton 'He wants me to find him a snake bait flower.' action NullAction() style "nvl_button2" text_slow_cps True
                                        elif not item_cavemushroom:
                                            textbutton 'He wants me to find him a cave ear mushroom.' action NullAction() style "nvl_button2" text_slow_cps True
                                        else:
                                            $ options_monastery += 1
                                            textbutton '“Here. The mushroom, and the snake bait.”' action [SetVariable("questionpreset", 0), Jump("aeli_about_sharpeningpotion_timer")] style "nvl_button" text_slow_cps True
                                    elif aeli_about_sharpeningpotion_timer >= day:
                                        textbutton 'My “sharpening poison” isn’t ready yet.' action NullAction() style "nvl_button2" text_slow_cps True
                                    elif not aeli_about_sharpeningpotion_collected:
                                        $ options_monastery += 1
                                        textbutton '“I’m here to pick up the poison.”' action [SetVariable("questionpreset", 0), Jump("aeli_about_sharpeningpotion_collected")] style "nvl_button" text_slow_cps True
                                if not orentius_met and not whitemarshes_attacked and not whitemarshes_nomoreundead:
                                    if options_monastery_about_necromancers:
                                        $ options_monastery += 1
                                        textbutton '“What do you know about the necromancers in the North?”' action [SetVariable("questionpreset", 0), Jump("aeli_about_necromancers01")] style "nvl_button" text_slow_cps True
                                    if sleep_whitemarshes and aeli_about_necromancers_question02 and aeli_about_necromancers_question04 and not aeli_about_necromancers_bloodmagic:
                                        $ options_monastery += 1
                                        textbutton '“I saw {color=#f6d6bd}Orentius’{/color} ritual. He strengthens his weak spells with blood magic.”' action [Jump("aeli_about_bloodmagic01")] style "nvl_button" text_slow_cps True
                                elif whitemarshes_nomoreundead and not aeli_about_nomoreundead:
                                    $ options_monastery += 1
                                    if orentius_convinced:
                                        textbutton '“I’ve a lot to say about {color=#f6d6bd}White Marshes{/color}.”' action [SetVariable("questionpreset", 0), Jump("aeli_about_nomoreundead01")] style "nvl_button" text_slow_cps True
                                    elif orentius_banished:
                                        textbutton '“I’ve a lot to say about {color=#f6d6bd}White Marshes{/color}.”' action [SetVariable("questionpreset", 0), Jump("aeli_about_nomoreundead02")] style "nvl_button" text_slow_cps True
                                    elif whitemarshes_destroyed:
                                        textbutton '“I’ve a lot to say about {color=#f6d6bd}White Marshes{/color}.”' action [SetVariable("questionpreset", 0), Jump("aeli_about_nomoreundead03")] style "nvl_button" text_slow_cps True
                                if monastery_cave_firsttime and quest_monasterysupport_description01 and not pc_goal_iwantnewlife_monastery and not pc_goal_iwantnewlife_monastery_rejected and aeli_about_aeli: # and pc_goal == "iwanttostartanewlife" 
                                    if not pc_goal_iwantnewlife_monastery_about:
                                        $ options_monastery += 1
                                        textbutton 'Now that I’ve been inside the {i}library{/i}, I give the monastery another look.' action [SetVariable("questionpreset", 0), Jump("aeli_about_iwantnewlife01")] style "nvl_button" text_slow_cps True
                                    elif pc_goal_iwantnewlife_monastery_about2:
                                        if (not description_druids10 and pc_religion == "theunitedchurch") or pc_religion != "theunitedchurch":
                                            if pc_faithpoints_opportunities >= 8:
                                                if pc_faithpoints >= (pc_faithpoints_opportunities*0.75):
                                                    $ options_monastery += 1
                                                    textbutton 'I look at {color=#f6d6bd}Decima{/color}. “I am of strong faith. Read me.”' action [SetVariable("questionpreset", 0), Jump("aeli_about_iwantnewlife01alt")] style "nvl_button" text_slow_cps True
                                                else:
                                                    textbutton 'According to Decima, my faith is weak.' action NullAction() style "nvl_button2" text_slow_cps True
                                            else:
                                                textbutton 'Decima claims my faith hasn’t been tested yet.' action NullAction() style "nvl_button2" text_slow_cps True
                                if not aeli_about_asteriontablet and item_asteriontablet and not item_asteriontablet_read:
                                    $ options_monastery += 1
                                    textbutton '“I found this wax tablet... Could you read it to me?”' action [SetVariable("questionpreset", 0), Jump("aeli_about_asteriontablet01")] style "nvl_button" text_slow_cps True
                                if item_letterwhitemarshes == 1 and quest_readtheletter == 1 and not item_letterwhitemarshes_read:
                                    $ options_monastery += 1
                                    textbutton '“I was asked to learn what’s on this tablet...”' action [SetVariable("questionpreset", 0), Jump("aeli_about_readtheletter01")] style "nvl_button" text_slow_cps True
                                if (item_thaisletter and not aeli_about_thaisletter and not item_thaisletter_read and not item_thaisletter_readingblocked and not pc_class == "scholar"):
                                    $ options_monastery += 1
                                    textbutton 'I consider asking him to read {color=#f6d6bd}Thais’{/color} letter to me.' action [SetVariable("questionpreset", 0), Jump("aeli_about_thaisletter00")] style "nvl_button" text_slow_cps True
                                elif (item_thaisletter_opened and not aeli_about_thaisletter and not item_thaisletter_read and not pc_class == "scholar"):
                                    $ options_monastery += 1
                                    textbutton 'I grab {color=#f6d6bd}Thais’{/color} letter. “Could you read this scroll to me?”' action [SetVariable("questionpreset", 0), Jump("aeli_about_thaisletter01")] style "nvl_button" text_slow_cps True
                                if aeli_about_buyingorselling and not aeli_about_alchemytable and pc_class == "scholar":
                                    $ options_monastery += 1
                                    textbutton '“I also dabble in alchemy a bit. Can I use your tools to brew?”' action [SetVariable("questionpreset", 0), Jump("aeli_about_brewingscholar01")] style "nvl_button" text_slow_cps True
                                elif aeli_about_buyingorselling and aeli_about_alchemytable and pc_class == "scholar" and not aeli_about_powderedbasalt and not item_powderedrock and not item_blindingpowder and not quest_monasterysupport_description02 and not quest_monasterysupport_description03:
                                    if not aeli_about_powderedbasalt_gray:
                                        $ options_monastery += 1
                                        textbutton '“Still, I know a recipe for the blinding powder that requires a basalt rock crushed on the top of a mountain. Can I get to those trees high up, just for a few minutes?”' action [SetVariable("questionpreset", 0), Jump("aeli_about_powderedbasalt01")] style "nvl_button" text_slow_cps True
                                    elif not quest_monasterysupport_description01 and not quest_monasterysupport_description01lie:
                                        textbutton 'I need to be a {i}friend of the order{/i} if I want to get the powdered basalt from here.' action NullAction() style "nvl_button2" text_slow_cps True
                                    else:
                                        $ options_monastery += 1
                                        textbutton '“I still need to powder a basalt rock. Can you lend me one?”' action [SetVariable("questionpreset", 0), Jump("aeli_about_powderedbasalt01alt")] style "nvl_button" text_slow_cps True
                                if aeli_about_buyingorselling and not aeli_about_buyingorselling_alt and not dolmen_inside_trapdoor and quest_healingpotion and not foggy_about_dolmen_quest:
                                    $ options_monastery += 1
                                    textbutton '“I was asked to look for a healing potion for this trader, {color=#f6d6bd}Akakios{/color}...”' action [SetVariable("questionpreset", 0), Jump("aeli_about_barter01_alt")] style "nvl_button" text_slow_cps True
                                if not aeli_about_buyingorselling:
                                    $ options_monastery += 1
                                    textbutton '“Would you like to barter?”' action [SetVariable("questionpreset", 0), Jump("aeli_about_barter01")] style "nvl_button" text_slow_cps True
                                elif aeli_about_buyingorselling and item_chicken:
                                    if not aeli_about_buyingorselling_chicken_firsttime:
                                        $ options_monastery += 1
                                        textbutton '“You mentioned you lack {i}delicacies{/i}... How about this roast chicken?”' action [SetVariable("questionpreset", 0), Jump("aeli_about_barter02")] style "nvl_button" text_slow_cps True
                                    else:
                                        if not aeli_about_buyingorselling_chicken_day or (aeli_about_buyingorselling_chicken_day and aeli_about_buyingorselling_chicken_day <= (day-3)):
                                            textbutton '{image=cointest} “Here, take this chicken. For two dragons.”' action [SetVariable("questionpreset", 0), Jump("aeli_about_barter03")] style "nvl_button" text_slow_cps True
                                        else:
                                            textbutton '{image=coingray} He’s not interested in another chicken right now.' action NullAction() style "nvl_button2" text_slow_cps True
                                if not options_monastery:
                                    textbutton 'There’s nothing else I can think of.' action NullAction() style "nvl_button2" text_slow_cps True

                            elif questionpreset == "monastery1aboutmonastery":
                                if not aeli_about_monasteryname:
                                    textbutton '“Does this place have a name? Or is it just {i}the monastery{/i}?”' action [SetVariable("questionpreset", 0), Jump("aeli_about_name01")] style "nvl_button" text_slow_cps True
                                if not aeli_about_thisplace:
                                    textbutton '“What can you tell me about your order?”' action [SetVariable("questionpreset", 0), Jump("aeli_about_thisplace01")] style "nvl_button" text_slow_cps True
                                if not aeli_about_leader and pc_religion != "ordersoftruth" and not monastery_prelate_invited:
                                    textbutton '“Does this place have a {i}leader{/i} of sorts?”' action [SetVariable("questionpreset", 0), Jump("aeli_about_leader01")] style "nvl_button" text_slow_cps True
                                if not aeli_about_leader and pc_religion == "ordersoftruth" and not monastery_prelate_invited:
                                    textbutton '“Could I speak with your prelate?”' action [SetVariable("questionpreset", 0), Jump("aeli_about_leader01alt")] style "nvl_button" text_slow_cps True
                                if not aeli_about_theirfaith:
                                    textbutton '“Tell me about your faith.”' action [SetVariable("questionpreset", 0), Jump("aeli_about_theirfaith01")] style "nvl_button" text_slow_cps True
                                if not aeli_about_aeli:
                                    textbutton '“How does one become a monk?”' action [SetVariable("questionpreset", 0), Jump("aeli_about_aeli01")] style "nvl_button" text_slow_cps True
                                if not aeli_about_hiddenknowledge:
                                    textbutton '“I’d like to learn some of your knowledge about the peninsula.”' action [SetVariable("questionpreset", 0), Jump("aeli_about_hiddenknowledge")] style "nvl_button" text_slow_cps True
                                textbutton '“Let’s return to my other questions.”' action [SetVariable("questionpreset", 0), Jump("monasteryafterinteractions01a")] style "nvl_button" text_slow_cps True

                            elif questionpreset == "monastery1aboutnecromancers":
                                if not whitemarshes_firsttime and not aeli_about_necromancers_question01:
                                    textbutton '“I heard I can find them in the northwest.”' action [SetVariable("questionpreset", 0), Jump("aeli_about_necromancers_question01")] style "nvl_button" text_slow_cps True
                                if whitemarshes_firsttime and not aeli_about_necromancers_question01:
                                    textbutton '“What do you think of {color=#f6d6bd}White Marshes{/color}?”' action [SetVariable("questionpreset", 0), Jump("aeli_about_necromancers_question01alt")] style "nvl_button" text_slow_cps True
                                if aeli_about_necromancers_question01 and not aeli_about_necromancers_question04:
                                    textbutton '“Any thoughts on {color=#f6d6bd}Orentius{/color}?”' action [SetVariable("questionpreset", 0), Jump("aeli_about_necromancers_question04")] style "nvl_button" text_slow_cps True
                                if not aeli_about_necromancers_question02:
                                    textbutton '“What’s your stance on necromancy, in general?”' action [SetVariable("questionpreset", 0), Jump("aeli_about_necromancers_question02")] style "nvl_button" text_slow_cps True
                                if sleep_whitemarshes and aeli_about_necromancers_question02 and aeli_about_necromancers_question04 and not aeli_about_necromancers_bloodmagic:
                                    textbutton '“I saw {color=#f6d6bd}Orentius’{/color} ritual. He strengthens his weak spells with blood magic.”' action [Jump("aeli_about_bloodmagic01")] style "nvl_button" text_slow_cps True
                                if aeli_about_necromancers_question02 and not aeli_about_necromancers_question03:
                                    textbutton '“How does one deal with the undead? Or necromancers?”' action [SetVariable("questionpreset", 0), Jump("aeli_about_necromancers_question03")] style "nvl_button" text_slow_cps True
                                if aeli_about_necromancers_question04 and not aeli_about_necromancers_question05:
                                    textbutton '“What was {color=#f6d6bd}White Marshes{/color} like before the priest’s arrival?”' action [SetVariable("questionpreset", 0), Jump("aeli_about_necromancers_question05")] style "nvl_button" text_slow_cps True
                                textbutton '“Let’s return to my other questions.”' action [SetVariable("questionpreset", 0), Jump("monasteryafterinteractions01a")] style "nvl_button" text_slow_cps True

                            elif questionpreset == "eudocia1":
                                if not eudocia_about_selling:
                                    $ options_eudocia += 1
                                    textbutton '{image=cointest} “Do you have anything interesting to sell?”' action [SetVariable("questionpreset", 0), Jump("eudociaaskedaboutshop01")] style "nvl_button" text_slow_cps True
                                elif eudocia_about_selling:
                                    textbutton '{image=cointest} “Let’s trade.”' action [SetVariable("questionpreset", 0), Jump("eudociaaskedaboutshop02")] style "nvl_button" text_slow_cps True
                                if quest_bronzerod > 0 and quest_bronzerod < 3 and not eudocia_about_roadclearing_cleared and eudocia_about_golems:
                                    if (fallentree_firsttime and stonesign_firsttime) or (stonebridge_firsttime and stonesign_firsttime) or (fallentree_firsttime and stonebridge_firsttime):
                                        $ options_eudocia += 1
                                        if not eudocia_about_roadclearing:
                                            textbutton '“The roads around the watchtower are in terrible shape. Why don’t your golems look after them?”' action [SetVariable("questionpreset", 0), Jump("eudocia_about_roadclearing01")] style "nvl_button" text_slow_cps True
                                        else:
                                            textbutton '{image=cointest} “Let’s talk about clearing the roads.”' action [SetVariable("questionpreset", 0), Jump("eudocia_about_roadclearing02")] style "nvl_button" text_slow_cps True
                                if not eudocia_about_spiritrock_problem and quest_spiritrock == 1:
                                    $ options_eudocia += 1
                                    textbutton '“{color=#f6d6bd}Photios{/color} has sent me to buy a {i}spirit rock{/i} for his daughter. He hopes it’s going to enhance {color=#f6d6bd}Phoibe’s{/color} pneuma.”' action [SetVariable("questionpreset", 0), Jump("eudociaaskedaboutshop01av02")] style "nvl_button" text_slow_cps True
                                if not eudocia_about_magicsapling and ruinedvillage_part_leftfield_EXPLORED == 1 and quest_ruins == 1 and eudocia_about_selling:
                                    $ options_eudocia += 1
                                    textbutton '“I found a barren field that may be affected by a curse. Do you have anything I could use to see if I’m right?”' action [SetVariable("questionpreset", 0), Jump("eudociaaskedaboutmagicsapling01")] style "nvl_button" text_slow_cps True
                                if quest_pensformonastery == 1 and not eudocia_about_pens:
                                    $ options_eudocia += 1
                                    textbutton '“I was asked to deliver the writing quills to the monastery.”' action [SetVariable("questionpreset", 0), Jump("eudociahouseaboutpens01")] style "nvl_button" text_slow_cps True
                                if item_arrow and not eudocia_about_arrow:
                                    $ options_eudocia += 1
                                    textbutton '“Surely you filled some arrows with pneuma before? Any ideas where this is from?” I show her the one that I found near the fallen tree.' action [SetVariable("questionpreset", 0), Jump("eudocia_about_arrow01")] style "nvl_button" text_slow_cps True
                                if shortcut_pcknowsabout and not eudocia_about_shortcut:
                                    $ options_eudocia += 1
                                    textbutton '“Have you ever been to the shortcut?”' action [SetVariable("questionpreset", 0), Jump("eudociaaskedaboutshortcut01")] style "nvl_button" text_slow_cps True
                                if asterion_highisland_knowsabout and not asterion_found and not eudocia_about_highisland:
                                    $ options_eudocia += 1
                                    textbutton '“Have you ever heard about {color=#f6d6bd}High Island{/color}?”' action [SetVariable("questionpreset", 0), Jump("eudociaaskedabouthighisland01")] style "nvl_button" text_slow_cps True
                                if quest_missinghunters == 1 and not eudocia_about_missinghunters:
                                    $ options_eudocia += 1
                                    textbutton '“A few hunters recently left {color=#f6d6bd}Creeks{/color}, and haven’t returned so far. {color=#f6d6bd}Dalia{/color}, {color=#f6d6bd}Admon{/color}, {color=#f6d6bd}Vaschel{/color}. Have you met them?”' action [SetVariable("questionpreset", 0), Jump("eudociaaskedaboutmissinghunters01")] style "nvl_button" text_slow_cps True
                                if ruinedvillage_confront_can and not ruinedvillage_truth and quest_ruins_10yclue08 and not eudocia_about_steephouse:
                                    if (eudocia_friendship+appearance_charisma) >= 8 and eudocia_about_parents and eudocia_about_steephouse_gray:
                                        $ options_eudocia += 1
                                        textbutton '“I helped you, {color=#f6d6bd}Eudocia{/color}, and you can see I’m not a scoundrel. What happened to the village in the south?”' action [SetVariable("questionpreset", 0), Jump("eudociaaskedaboutsteephouse02")] style "nvl_button" text_slow_cps True
                                    elif ((eudocia_friendship+appearance_charisma) < 8 and eudocia_about_steephouse_gray) or (not eudocia_about_parents and eudocia_about_steephouse_gray):
                                        textbutton 'She doesn’t want to talk with me about the ruins.' action NullAction() style "nvl_button2" text_slow_cps True
                                    else:
                                        $ options_eudocia += 1
                                        textbutton '“You left {color=#f6d6bd}Old Págos{/color} during the same time when the village in the south collapsed. What happened?”' action [SetVariable("questionpreset", 0), Jump("eudociaaskedaboutsteephouse01")] style "nvl_button" text_slow_cps True
                                if banditshideout_bandits_pchearedabout and not eudocia_about_bandits:
                                    if (eudocia_friendship+appearance_charisma) >= 6 and eudocia_about_bandits_gray:
                                        $ options_eudocia += 1
                                        textbutton '“You seem to be afraid of the bandits, {color=#f6d6bd}Eudocia{/color}.”' action [SetVariable("questionpreset", 0), Jump("eudociaaskedaboutbandits02")] style "nvl_button" text_slow_cps True
                                    elif (eudocia_friendship+appearance_charisma) < 6 and eudocia_about_bandits_gray:
                                        textbutton 'She’s not willing to talk about the bandits.' action NullAction() style "nvl_button2" text_slow_cps True
                                    else:
                                        $ options_eudocia += 1
                                        textbutton '“I’ve heard about some bandits. Don’t they bother you?”' action [SetVariable("questionpreset", 0), Jump("eudociaaskedaboutbandits01")] style "nvl_button" text_slow_cps True
                                if whitemarshes_nomoreundead and not eudocia_about_nomoreundead:
                                    if orentius_convinced:
                                        $ options_eudocia += 1
                                        textbutton '“Great changes are happening in the west. {color=#f6d6bd}White Marshes{/color} is now free of necromancy.”' action [SetVariable("questionpreset", 0), Jump("eudocia_about_nomoreundead01")] style "nvl_button" text_slow_cps True
                                    elif orentius_banished:
                                        $ options_eudocia += 1
                                        textbutton '“The necromancer from {color=#f6d6bd}White Marshes{/color} has been forced to leave the village. The undead are gone.”' action [SetVariable("questionpreset", 0), Jump("eudocia_about_nomoreundead02")] style "nvl_button" text_slow_cps True
                                    elif whitemarshes_destroyed:
                                        $ options_eudocia += 1
                                        textbutton '“I’m afraid these woods may get much more dangerous soon. I hope your golems are capable of facing undead.”' action [SetVariable("questionpreset", 0), Jump("eudocia_about_nomoreundead03")] style "nvl_button" text_slow_cps True
                                if (whitemarshes_firsttime and not eudocia_about_nomoreundead and quest_bronzerod == 1 and not eudocia_about_whitemarshes) or (whitemarshes_firsttime and not eudocia_about_nomoreundead and quest_bronzerod == 2 and not eudocia_about_whitemarshes):
                                    $ options_eudocia += 1
                                    textbutton '“Why did you ask me to place a rod in {color=#f6d6bd}White Marshes{/color} specifically? Is it because of the undead?”' action [SetVariable("questionpreset", 0), Jump("eudocia_about_whitemarshes01")] style "nvl_button" text_slow_cps True
                                if not eudocia_about_herself and eudocia_friendship < 10:
                                    $ options_eudocia += 1
                                    textbutton '“So, what’s your story? Why do you live so far from any village?”' action [SetVariable("questionpreset", 0), Jump("eudocia_about_herself01")] style "nvl_button" text_slow_cps True
                                if not eudocia_about_plague and oldpagos_plague_known and not oldpagos_cured:
                                    $ options_eudocia += 1
                                    textbutton '“I bring news from the West. {color=#f6d6bd}Old Págos{/color} is facing a grave plague.”' action [SetVariable("questionpreset", 0), Jump("eudocia_about_plague01")] style "nvl_button" text_slow_cps True
                                if not eudocia_about_plague and oldpagos_plague_known and oldpagos_cured:
                                    $ options_eudocia += 1
                                    textbutton '“I bring news from the West. {color=#f6d6bd}Old Págos{/color} has faced a grave plague.”' action [SetVariable("questionpreset", 0), Jump("eudocia_about_plague01alt")] style "nvl_button" text_slow_cps True
                                if not eudocia_about_parents and oldpagos_about_eudocia_parents:
                                    $ options_eudocia += 1
                                    textbutton '“I bring news of {color=#f6d6bd}your parents{/color}.”' action [SetVariable("questionpreset", 0), Jump("eudociaaskedaboutparents01")] style "nvl_button" text_slow_cps True
                                if not eudocia_about_plague_cured and eudocia_about_parents and oldpagos_cured:
                                    $ options_eudocia += 1
                                    textbutton '“You should know... The plague of {color=#f6d6bd}Old Págos{/color} is no more.”' action [SetVariable("questionpreset", 0), Jump("eudociaaskedabouthealedplague01")] style "nvl_button" text_slow_cps True
                                if not eudocia_about_monks and description_eudocia03:
                                    $ options_eudocia += 1
                                    textbutton '“I spoke with {color=#f6d6bd}the monks{/color}. They’re quite afraid of you.”' action [SetVariable("questionpreset", 0), Jump("eudociaaskedaboutthedistrustofmonks01")] style "nvl_button" text_slow_cps True
                                if not eudocia_about_chisel and eudocia_about_parents and item_magicchisel == 1:
                                    $ options_eudocia += 1
                                    textbutton 'I show her the chisel from {color=#f6d6bd}Old Págos{/color}. “It used to belong to a sculptor... Do you recognize it?”' action [SetVariable("questionpreset", 0), Jump("eudociaaskedaboutchisel01")] style "nvl_button" text_slow_cps True
                                if eudocia_about_golems < 4:
                                    $ options_eudocia += 1
                                    textbutton '“I have some questions about your golems.”' action [SetVariable("questionpreset", 0), Jump("eudocia_about_golems01")] style "nvl_button" text_slow_cps True
                                if not eudocia_about_golems_gray:
                                    if quest_studyingthegolems_description03 and not quest_studyingthegolems_description03b:
                                        $ options_eudocia += 1
                                        textbutton '“I saw some words on your golems. What do they mean?”' action [SetVariable("questionpreset", 0), Jump("eudociaaskedaboutgolemwords01")] style "nvl_button" text_slow_cps True
                                else:
                                    if quest_studyingthegolems_description03 and not quest_studyingthegolems_description03b and (eudocia_friendship+appearance_charisma) >= 6:
                                        $ options_eudocia += 1
                                        textbutton '“About the words on your golems...”' action [SetVariable("questionpreset", 0), Jump("eudociaaskedaboutgolemwords01alt")] style "nvl_button" text_slow_cps True
                                    elif quest_studyingthegolems_description03 and not quest_studyingthegolems_description03b and (eudocia_friendship+appearance_charisma) < 6:
                                        textbutton 'She doesn’t trust me enough to tell me more about the words on her golems.' action NullAction() style "nvl_button2" text_slow_cps True
                                if eudocia_about_golems_question1 and not eudocia_about_gargoyle:
                                    $ options_eudocia += 1
                                    textbutton '“What’s with the gargoyle?”' action [SetVariable("questionpreset", 0), Jump("eudocia_about_gargoyle01")] style "nvl_button" text_slow_cps True
                                if quest_studyingthegolems_description03b and not eudocia_about_reading and pc_class != "scholar":
                                    $ options_eudocia += 1
                                    textbutton '“Since you have writing on your golems... Could you read some things for me?”' action [SetVariable("questionpreset", 0), Jump("eudociaaskedaboutreading01")] style "nvl_button" text_slow_cps True
                                if not eudocia_about_enchanting:
                                    $ options_eudocia += 1
                                    textbutton '“What can you tell me about enchanting?”' action [SetVariable("questionpreset", 0), Jump("eudocia_about_enchanting01")] style "nvl_button" text_slow_cps True
                                if eudocia_friendship >= eudocia_friendship_tierlevel and quarters >= (world_daylength-12) and not eudocia_sleep_available:
                                    $ options_eudocia += 1
                                    textbutton '“It’s getting late. Can I spend a night in your shed?”' action [SetVariable("questionpreset", 0), Jump("eudocia_about_sleeping02")] style "nvl_button" text_slow_cps True
                                elif not eudocia_about_sleeping and not eudocia_sleep_available:
                                    $ options_eudocia += 1
                                    textbutton '“I need a place to rest. Can I spend a night here?”' action [SetVariable("questionpreset", 0), Jump("eudocia_about_sleeping01")] style "nvl_button" text_slow_cps True
                                if not eudocia_about_job01:
                                    $ options_eudocia += 1
                                    textbutton '“I’m looking for a job.”' action [SetVariable("questionpreset", 0), Jump("eudocia_about_job01")] style "nvl_button" text_slow_cps True
                                elif quest_bronzerod == 1:
                                    if quest_bronzerod_description04 or quest_bronzerod_description05:
                                        if eudocia_bronzerod_installed_paidfor < eudocia_bronzerod_installed:
                                            $ options_eudocia += 1
                                            textbutton '“I want to collect my reward for the bronze rods.”' action [SetVariable("questionpreset", 0), Jump("eudocia_about_job01rewardsuccess01")] style "nvl_button" text_slow_cps True
                                        elif not quest_bronzerod_description07 and not quest_bronzerod_description03:
                                            textbutton 'She already paid me for the rods I placed.' action NullAction() style "nvl_button2" text_slow_cps True
                                    elif quest_bronzerod_description07:
                                        $ options_eudocia += 1
                                        textbutton '“I won’t finish the job.”' action [SetVariable("questionpreset", 0), Jump("eudocia_about_job01rewardfailure01")] style "nvl_button" text_slow_cps True
                                    elif quest_bronzerod_description03:
                                        $ options_eudocia += 1
                                        textbutton '“I won’t finish the job.”' action [SetVariable("questionpreset", 0), Jump("eudocia_about_job01rewardfailure01nomarshes")] style "nvl_button" text_slow_cps True
                                    else:
                                        textbutton 'She waits for me to place at least four bronze rods.' action NullAction() style "nvl_button2" text_slow_cps True
                                if (not eudocia_about_job02 and quest_bronzerod == 2) or (not eudocia_about_job02 and quest_bronzerod == 3):
                                    $ options_eudocia += 1
                                    if quest_bronzerod == 2:
                                        textbutton '“Do you need help with anything else?”' action [SetVariable("questionpreset", 0), Jump("eudocia_about_jobnumber201a")] style "nvl_button" text_slow_cps True
                                    if quest_bronzerod >= 3:
                                        textbutton '“Do you need help with anything else?”' action [SetVariable("questionpreset", 0), Jump("eudocia_about_jobnumber201b")] style "nvl_button" text_slow_cps True
                                if item_snakebait and quest_eudociaflower == 1:
                                    $ options_eudocia += 1
                                    textbutton '“I brought you flowers.”' action [SetVariable("questionpreset", 0), Jump("eudociahousepchasflower01")] style "nvl_button" text_slow_cps True
                                if not eudocia_about_asterion_gray:
                                    if quest_asterion == 1 and not asterion_found and not eudocia_about_asterion:
                                        $ options_eudocia += 1
                                        textbutton '“I’m looking for {color=#f6d6bd}Asterion{/color}, the previous roadwarden.”' action [SetVariable("questionpreset", 0), Jump("eudocia_about_asterion01")] style "nvl_button" text_slow_cps True
                                else:
                                    if quest_asterion == 1 and not asterion_found and not eudocia_about_asterion and (eudocia_friendship+appearance_charisma) >= 8:
                                        $ options_eudocia += 1
                                        textbutton '“I’m looking for {color=#f6d6bd}Asterion{/color}, the previous roadwarden.”' action [SetVariable("questionpreset", 0), Jump("eudocia_about_asterion01")] style "nvl_button" text_slow_cps True
                                    elif quest_asterion == 1 and not asterion_found and not eudocia_about_asterion and (eudocia_friendship+appearance_charisma) < 8:
                                        textbutton 'She doesn’t trust me enough to speak with me about Asterion.' action NullAction() style "nvl_button2" text_slow_cps True
                                if eudocia_about_asterion and asterion_found and not eudocia_about_asterion_found:
                                    $ options_eudocia += 1
                                    textbutton '“{color=#f6d6bd}Asterion{/color} is dead.”' action [SetVariable("questionpreset", 0), Jump("eudocia_about_asterion_found01")] style "nvl_button" text_slow_cps True
                                if item_asterioncloak and eudocia_about_asterion and not eudocia_about_asterion_cloak:
                                    $ options_eudocia += 1
                                    textbutton '“I found {color=#f6d6bd}Asterion’s{/color} cloak...”' action [SetVariable("questionpreset", 0), Jump("eudocia_about_asterion_cloak01")] style "nvl_button" text_slow_cps True
                                if not eudocia_about_enchanting_items and eudocia_friendship < 10:
                                    $ options_eudocia += 1
                                    textbutton '“Could you fill an item of mine with pneuma?”' action [SetVariable("questionpreset", 0), Jump("eudocia_about_enchanting_items01")] style "nvl_button" text_slow_cps True
                                if not eudocia_about_peninsula:
                                    $ options_eudocia += 1
                                    textbutton '“I want to learn more about the peninsula.”' action [SetVariable("questionpreset", 0), Jump("eudocia_about_peninsula01")] style "nvl_button" text_slow_cps True
                                if (eudocia_inside_firsttime and not eudocia_invitation_attempt) or (eudocia_friendship >= eudocia_friendship_tierlevel and not eudocia_invitation_attempt and eudocia_sleep_available):
                                    $ options_eudocia += 1
                                    textbutton 'Maybe it’s the right time to offer her work in the city.' action [SetVariable("questionpreset", 0), Jump("eudocia_about_invitation00")] style "nvl_button" text_slow_cps True
                                if pc_area == "eudociahouseinside":
                                    $ options_eudocia += 1
                                    textbutton 'I go outside.' action [SetVariable("questionpreset", 0), Jump("eudociahouseonthesquare01")] style "nvl_button" text_slow_cps True
                                if not options_eudocia:
                                    textbutton 'There’s nothing else I can think of.' action NullAction() style "nvl_button2" text_slow_cps True

                            elif questionpreset == "eudocia2":
                                if eudocia_about_asterion and not eudocia_invitation_argument_asterion:
                                    $ options_eudocia += 1
                                    textbutton '“You know how easy it is to suddenly disappear in this land. Just think about {color=#f6d6bd}Asterion{/color}.”' action [SetVariable("questionpreset", 0), Jump("eudocia_about_invitation_arguments_asterion01")] style "nvl_button" text_slow_cps True
                                if eudocia_about_chisel and eudocia_about_enchanting and not eudocia_invitation_argument_enchanting:
                                    $ options_eudocia += 1
                                    textbutton '“You know best how much you’ve learned since the day you enchanted that old chisel. In the city, you could speak with other masters, learn how to read scrolls. You’d unlock your potential.”' action [SetVariable("questionpreset", 0), Jump("eudocia_about_invitation_arguments_enchanting01")] style "nvl_button" text_slow_cps True
                                if quest_eudociaflower == 2 and not eudocia_invitation_argument_eudociaflower:
                                    $ options_eudocia += 1
                                    textbutton '“In {color=#f6d6bd}Hovlavan{/color}, you’d find all the snake bait you need. As well as other entertainments.”' action [SetVariable("questionpreset", 0), Jump("eudocia_about_invitation_arguments_eudociaflower01")] style "nvl_button" text_slow_cps True
                                elif quest_eudociaflower == 3 and not eudocia_invitation_argument_eudociaflower:
                                    $ options_eudocia += 1
                                    textbutton '“In {color=#f6d6bd}Hovlavan{/color}, there are countless things to do. Enough to distract you from snake bait.”' action [SetVariable("questionpreset", 0), Jump("eudocia_about_invitation_arguments_eudociaflower02")] style "nvl_button" text_slow_cps True
                                if not eudocia_invitation_argument_threats:
                                    $ options_eudocia += 1
                                    textbutton '“The peninsula is a dangerous place, with little help to offer. I know that better than anyone.”' action [SetVariable("questionpreset", 0), Jump("eudocia_about_invitation_arguments_threats01")] style "nvl_button" text_slow_cps True
                                if not eudocia_invitation_argument_support:
                                    if quest_creekssupport == 2 or quest_galerockssupport == 2 or quest_howlerssupport == 2 or quest_oldpagossupport == 2 or quest_monasterysupport == 2:
                                        $ options_eudocia += 1
                                        textbutton '“The cityfolk will start negotiations with the tribes as well. You don’t have to be left out.”' action [SetVariable("questionpreset", 0), Jump("eudocia_about_invitation_arguments_support01")] style "nvl_button" text_slow_cps True
                                if (eudocia_about_monks and not eudocia_invitation_argument_monks1) or (description_eudocia03 and not eudocia_invitation_argument_monks1) or (quest_studyingthegolems and not eudocia_invitation_argument_monks1):
                                    $ options_eudocia += 1
                                    textbutton '“Can you be sure {color=#f6d6bd}the monks{/color} won’t turn their neighbors against you?”' action [SetVariable("questionpreset", 0), Jump("eudocia_about_invitation_arguments_monks01")] style "nvl_button" text_slow_cps True
                                elif eudocia_invitation_argument_monks1 and monastery_betrayal_blocked and not eudocia_invitation_argument_monks2:
                                    textbutton 'I promised the monks to not betray them.' action NullAction() style "nvl_button2" text_slow_cps True
                                elif eudocia_invitation_argument_monks1 and monastery_betrayal_available and not eudocia_invitation_argument_monks2:
                                    textbutton '“Yet {color=#f6d6bd}Aeli{/color} is already scheming against you. He wanted me to spy on your golems, find their weaknesses.”' action [SetVariable("questionpreset", 0), Jump("eudocia_about_invitation_arguments_monks02")] style "nvl_button" text_slow_cps True
                                if not options_eudocia:
                                    textbutton '“What’s your decision?”' action [SetVariable("questionpreset", 0), Jump("eudocia_about_invitation_conclusion01")] style "nvl_button" text_slow_cps True

                            elif questionpreset == "horseshortcut":
                                if not shortcut_woodenroad_horseaccident_talking:
                                    textbutton 'I calm it down with the sound of my voice. “Relax, {color=#f6d6bd}[horsename]{/color}. Everything’s fine.”' action [SetVariable("questionpreset", 0), Jump("shortcutwoodenroadhorsetalking01")] style "nvl_button" text_slow_cps True
                                if not shortcut_woodenroad_horseaccident_pet:
                                    textbutton 'I pet its head.' action [SetVariable("questionpreset", 0), Jump("shortcutwoodenroadhorseheadpetting01")] style "nvl_button" text_slow_cps True
                                if not shortcut_woodenroad_horseaccident_lookaround:
                                    textbutton 'I give it time to look around.' action [SetVariable("questionpreset", 0), Jump("shortcutwoodenroadhorselookaround01")] style "nvl_button" text_slow_cps True
                                if not shortcut_woodenroad_horseaccident_slowmovements:
                                    textbutton 'I move slowly and show it my hands.' action [SetVariable("questionpreset", 0), Jump("shortcutwoodenroadhorseslowmovements01")] style "nvl_button" text_slow_cps True
                                if not shortcut_woodenroad_horseaccident_chamomile:
                                    textbutton 'I let it smell my flask with chamomile oil.' action [SetVariable("questionpreset", 0), Jump("shortcutwoodenroadhorsechamomile01")] style "nvl_button" text_slow_cps True
                                if not shortcut_woodenroad_horseaccident_lowerhead:
                                    textbutton 'I ask it to lower its head.' action [SetVariable("questionpreset", 0), Jump("shortcutwoodenroadhorselowerhead01")] style "nvl_button" text_slow_cps True
                                if not shortcut_woodenroad_horseaccident_breathcontrol:
                                    textbutton 'I stay calm, and breathe deeply.' action [SetVariable("questionpreset", 0), Jump("shortcutwoodenroadhorsebreathcontrol01")] style "nvl_button" text_slow_cps True
                                if shortcut_woodenroad_horseaccident_relax_level >= 7:
                                    textbutton 'Speaking some nonsense, I get back in the saddle.' action [SetVariable("questionpreset", 0), Jump("shortcutwoodenroadhorseleaving01")] style "nvl_button" text_slow_cps True

                            elif questionpreset == "foggy1":
                                if (foggy_food_meals_available and pc_food < 4 and not foggy_food_meals_available_free) or (foggy_food_meals_available and pc_food < 4 and foggy_food_meals_available_free and foggy_food_meals_available_free_lastmeal == day):
                                    textbutton '“I’d like to eat.”' action [SetVariable("questionpreset", 0), SetVariable("can_rest", 0), Jump("foggylakeregularquestionseating01")] style "nvl_button" text_slow_cps True
                                elif foggy_food_meals_available_free and foggy_food_meals_available_free_lastmeal != day and pc_food < 4:
                                    textbutton '“I’d like my free meal.”' action [SetVariable("questionpreset", 0), SetVariable("can_rest", 0), SetVariable("can_rest", 0), Jump("foggylakeregularquestionseating02")] style "nvl_button" text_slow_cps True
                                elif (foggy_food_meals_available and pc_food == 4) or (foggy_food_meals_available_free and foggy_food_meals_available_free_lastmeal != day and pc_food == 4):
                                    textbutton 'I don’t need to eat right now.' action NullAction() style "nvl_button2" text_slow_cps True
                                if not foggy_about_trade:
                                    textbutton '{image=cointest} “What do you have for sale?”' action [SetVariable("questionpreset", 0), SetVariable("can_rest", 0), Jump("foggylakeregularquestionstrade01")] style "nvl_button" text_slow_cps True
                                else:
                                    textbutton '{image=cointest} “I need to buy something.”' action [SetVariable("questionpreset", 0), SetVariable("can_rest", 0), Jump("foggylakeregularquestionstrade02")] style "nvl_button" text_slow_cps True
                                textbutton '{image=cointest} “I have some things I’m willing to part with.”' action [SetVariable("questionpreset", 0), SetVariable("can_rest", 0), Jump("foggylakeregularquestionsselling01")] style "nvl_button" text_slow_cps True
                                if (asterion_highisland_knowsabout and not asterion_found and foggy_about_highisland and not galerocks_navica_pcknowsabout_highisland and not foggy_aboutnavica and quest_asterion == 1) or (quest_asterion == 1 and asterion_highisland_clues >= 3 and not asterion_found and foggy_about_highisland and not galerocks_navica_pcknowsabout_highisland and not foggy_aboutnavica):
                                    if (foggy_friendship+appearance_charisma) < 10 and foggy_aboutnavica_gray:
                                        textbutton 'She’s not willing to tell me about anyone who saw High Island up close.' action NullAction() style "nvl_button2" text_slow_cps True
                                    elif foggy_aboutnavica_gray:
                                        textbutton '“Help me, {color=#f6d6bd}Foggy{/color}. I need to find someone who knows more about {color=#f6d6bd}High Island{/color}.”' action [SetVariable("questionpreset", 0), SetVariable("can_rest", 0), Jump("foggy_about_navica02")] style "nvl_button" text_slow_cps True
                                    else:
                                        textbutton '“Try to remember. Maybe there’s someone you know of who’s been to {color=#f6d6bd}High Island{/color}?”' action [SetVariable("questionpreset", 0), SetVariable("can_rest", 0), Jump("foggy_about_navica01")] style "nvl_button" text_slow_cps True
                                if asterion_found and not foggy_about_foundasterion:
                                    textbutton '“I found {color=#f6d6bd}Asterion{/color}.”' action [SetVariable("questionpreset", 0), SetVariable("can_rest", 0), Jump("foggylakeregularquestionsfoundasterion01")] style "nvl_button" text_slow_cps True
                                if foragers_caius_spokento and not foggy_about_caius:
                                    textbutton '“I spoke with {color=#f6d6bd}Caius{/color}. I wonder why did you decide to keep him around.”' action [SetVariable("questionpreset", 0), SetVariable("can_rest", 0), Jump("foggylakeregularquestionscaius01")] style "nvl_button" text_slow_cps True
                                if item_oceannecklace and not foggy_about_oceannecklace and not galerocks_rufina_about_necklace:
                                    textbutton 'I show her the ocean necklace. “Any ideas where this comes from?”' action [SetVariable("questionpreset", 0), SetVariable("can_rest", 0), Jump("foggylakeregularquestionsoceannecklace01")] style "nvl_button" text_slow_cps True
                                if not foggy_about_asterion and quest_asterion == 1 and not asterion_found:
                                    textbutton '“I’m looking for {color=#f6d6bd}Asterion{/color}, the previous roadwarden.”' action [SetVariable("questionpreset", 0), SetVariable("can_rest", 0), Jump("foggylakeregularquestionsasterion01")] style "nvl_button" text_slow_cps True
                                if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and (foggy_friendship+appearance_charisma) < 10 and foggy_about_asterion < 2 and quest_asterion == 1 and not asterion_found:
                                    textbutton 'She doesn’t trust me enough to tell me what she knows about Asterion.' action NullAction() style "nvl_button2" text_slow_cps True
                                if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and (foggy_friendship+appearance_charisma) >= 10 and foggy_about_asterion < 2 and quest_asterion == 1 and not asterion_found:
                                    textbutton '“I think I’ve done enough to earn your trust. Tell me more about the stuff {color=#f6d6bd}Asterion{/color} brought you.”' action [SetVariable("questionpreset", 0), SetVariable("can_rest", 0), Jump("foggylakeregularquestionsasterion03question06")] style "nvl_button" text_slow_cps True
                                if not foggy_about_shelter:
                                    textbutton '“Could I spend a night or two under your roof?”' action [SetVariable("questionpreset", 0), SetVariable("can_rest", 0), Jump("foggylakeregularquestionsshelter01")] style "nvl_button" text_slow_cps True
                                if description_foggy03 and not foggylake_alchemytable_firsttime and pc_class == "scholar":
                                    textbutton '“Can I take a look at your brewing set? I’m a bit of an alchemist.”' action [SetVariable("questionpreset", 0), SetVariable("can_rest", 0), Jump("foggylakeregularquestionsalchemyset01")] style "nvl_button" text_slow_cps True
                                if not foggy_about_job:
                                    textbutton '“I’m looking for work.”' action [SetVariable("questionpreset", 0), SetVariable("can_rest", 0), Jump("foggylakeregularquestionsjob101")] style "nvl_button" text_slow_cps True
                                elif quest_foggy1oldpagos == 1 and not oldpagos_plague_known:
                                    textbutton 'I still don’t know what happened with Old Págos.' action NullAction() style "nvl_button2" text_slow_cps True
                                elif quest_foggy1oldpagos == 1 and oldpagos_plague_known and not foggy_about_plague:
                                    textbutton '“I bring news from {color=#f6d6bd}Old Págos{/color}. They’re not good.”' action [SetVariable("questionpreset", 0), SetVariable("can_rest", 0), Jump("foggylakeregularquestionsjob102")] style "nvl_button" text_slow_cps True
                                elif quest_foggy1oldpagos > 1 and not quest_foggy2iason and foggy_about_job < 2:
                                    textbutton '“Want me to do anything else?”' action [SetVariable("questionpreset", 0), SetVariable("can_rest", 0), Jump("foggylakeregularquestionsjob201a")] style "nvl_button" text_slow_cps True
                                elif quest_foggy1oldpagos > 1 and not quest_foggy2iason and foggy_about_job >= 1 and (foggy_friendship+appearance_charisma) < 5:
                                    textbutton 'She doesn’t trust me enough to give me another job. Yet.' action NullAction() style "nvl_button2" text_slow_cps True
                                elif quest_foggy1oldpagos > 1 and not quest_foggy2iason and foggy_about_job >= 1 and (foggy_friendship+appearance_charisma) >= 5:
                                    textbutton '“So. The next job.”' action [SetVariable("questionpreset", 0), SetVariable("can_rest", 0), Jump("foggylakeregularquestionsjob201b")] style "nvl_button" text_slow_cps True
                                elif quest_foggy2iason == 1 and not quest_foggy2iason_description01:
                                    textbutton 'I still need to speak with Iason.' action NullAction() style "nvl_button2" text_slow_cps True
                                elif quest_foggy2iason == 1 and peltnorth_ban_perm and not quest_foggy2iason_description01:
                                    textbutton '“I won’t be able to deliver your message to {color=#f6d6bd}Pelt{/color}.”' action [SetVariable("questionpreset", 0), SetVariable("can_rest", 0), Jump("foggylakeregularquestionsjob203")] style "nvl_button" text_slow_cps True
                                elif quest_foggy2iason == 1 and quest_foggy2iason_description01:
                                    textbutton '“I had a talk with {color=#f6d6bd}Iason{/color}.”' action [SetVariable("questionpreset", 0), SetVariable("can_rest", 0), Jump("foggylakeregularquestionsjob202")] style "nvl_button" text_slow_cps True
                                elif quest_foggy2iason > 1 and not quest_foggy3whitemarshes and foggy_about_job < 3:
                                    textbutton '“Let me know if you have anything else for me to do.”' action [SetVariable("questionpreset", 0), SetVariable("can_rest", 0), Jump("foggylakeregularquestionsjob301a")] style "nvl_button" text_slow_cps True
                                elif quest_foggy2iason > 1 and not quest_foggy3whitemarshes and foggy_about_job >= 2 and (foggy_friendship+appearance_charisma) < 8:
                                    textbutton 'She doesn’t trust me enough to give me another job. Yet.' action NullAction() style "nvl_button2" text_slow_cps True
                                elif quest_foggy2iason > 1 and not quest_foggy3whitemarshes and foggy_about_job >= 2 and (foggy_friendship+appearance_charisma) >= 8 and not whitemarshes_attacked and not whitemarshes_destroyed:
                                    textbutton '“So, the next job.”' action [SetVariable("questionpreset", 0), SetVariable("can_rest", 0), Jump("foggylakeregularquestionsjob301b")] style "nvl_button" text_slow_cps True
                                elif (whitemarshes_attacked and quest_foggy2iason > 1 and not quest_foggy3whitemarshes and foggy_about_job >= 2 and not foggy_about_whitemarshes_cancelled) or (whitemarshes_destroyed and quest_foggy2iason > 1 and not quest_foggy3whitemarshes and foggy_about_job >= 2 and not foggy_about_whitemarshes_cancelled):
                                    textbutton '“So, the next job.”' action [SetVariable("questionpreset", 0), SetVariable("can_rest", 0), Jump("foggylakeregularquestionsjob301cancelled")] style "nvl_button" text_slow_cps True
                                elif quest_foggy3whitemarshes == 1:
                                    if orentius_convinced or orentius_banished or whitemarshes_destroyed:
                                        if foggy_about_nomoreundead and quest_foggy3whitemarshes_description01 and orentius_convinced:
                                            textbutton '“I took care of the cask with cider.”' action [SetVariable("questionpreset", 0), SetVariable("can_rest", 0), Jump("foggylakeregularquestionsjob302")] style "nvl_button" text_slow_cps True
                                        elif foggy_about_nomoreundead:
                                            textbutton '“About the cider...”' action [SetVariable("questionpreset", 0), SetVariable("can_rest", 0), Jump("foggylakeregularquestionsjob301cancelled02ALT")] style "nvl_button" text_slow_cps True
                                    else:
                                        if not quest_foggy3whitemarshes_description01:
                                            textbutton 'I still need to take the cask of cider to White Marshes.' action NullAction() style "nvl_button2" text_slow_cps True
                                        elif quest_foggy3whitemarshes_description01:
                                            textbutton '“I took care of the cask with cider.”' action [SetVariable("questionpreset", 0), SetVariable("can_rest", 0), Jump("foggylakeregularquestionsjob302")] style "nvl_button" text_slow_cps True
                                        elif quest_foggy3whitemarshes_description07 or whitemarshes_attacked:
                                            textbutton '(lie) “I took care of the cask with cider.”' action [SetVariable("questionpreset", 0), SetVariable("can_rest", 0), Jump("foggylakeregularquestionsjob302")] style "nvl_button" text_slow_cps True
                                if not foggy_about_rumors:
                                    textbutton '“What can you tell me about the peninsula?”' action [SetVariable("questionpreset", 0), SetVariable("can_rest", 0), Jump("foggylakeregularquestionsrumors00")] style "nvl_button" text_slow_cps True
                                if not foggy_about_rumors:
                                    textbutton '“Any interesting rumors?”' action [SetVariable("questionpreset", 0), SetVariable("can_rest", 0), Jump("foggylakeregularquestionsrumors00ALT")] style "nvl_button" text_slow_cps True
                                if foggy_about_rumors and foggy_friendship < 0 and not foggy_about_rumors_available: # (foggy_friendship+appearance_charisma) < 3
                                    textbutton 'She doesn’t trust me enough to share any rumors with me.' action NullAction() style "nvl_button2" text_slow_cps True
                                if (foggy_about_rumors_available and foggy_about_rumors) or (foggy_friendship >= 0 and foggy_about_rumors): # (foggy_friendship+appearance_charisma) >= 3
                                    textbutton '“I have some questions about the peninsula.”' action [SetVariable("questionpreset", 0), SetVariable("can_rest", 0), Jump("foggylakeregularquestionsrumors01")] style "nvl_button" text_slow_cps True
                                if (not foggy_about_bandits and quest_intelforpeltnorth == 1 and not foggy_about_bandits_available) or (not foggy_about_bandits and banditshideout_bandits_pchearedabout == 1 and not foggy_about_bandits_available):
                                    textbutton '“I’ve heard there are some bandits in the North.”' action [SetVariable("questionpreset", 0), SetVariable("can_rest", 0), Jump("foggylakeregularquestionsbandits01ALT")] style "nvl_button" text_slow_cps True
                                if not foggy_about_bandits and foggy_about_bandits_available:
                                    textbutton '“You’ve mentioned bandits?”' action [SetVariable("questionpreset", 0), SetVariable("can_rest", 0), Jump("foggylakeregularquestionsbandits01")] style "nvl_button" text_slow_cps True
                                if not orentius_met and not whitemarshes_attacked and not whitemarshes_nomoreundead:
                                    if not foggy_about_necromancers:
                                        textbutton '“Have you heard anything about necromancers here in the North?”' action [SetVariable("questionpreset", 0), SetVariable("can_rest", 0), Jump("foggylakeregularquestionsnecromancers01")] style "nvl_button" text_slow_cps True
                                elif whitemarshes_nomoreundead and not foggy_about_nomoreundead:
                                    if orentius_convinced:
                                        textbutton '“{color=#f6d6bd}White Marshes{/color} won’t be overtaken by its undead. {color=#f6d6bd}Orentius{/color} agreed to abandon dark magic.”' action [SetVariable("questionpreset", 0), SetVariable("can_rest", 0), Jump("foggylakeregularquesaboutnomoreundead01")] style "nvl_button" text_slow_cps True
                                    elif orentius_banished:
                                        textbutton '“{color=#f6d6bd}White Marshes{/color} won’t be overtaken by its undead, but the locals will most likely cut their ties to the other settlements.”' action [SetVariable("questionpreset", 0), SetVariable("can_rest", 0), Jump("foggylakeregularquesaboutnomoreundead02")] style "nvl_button" text_slow_cps True
                                    elif whitemarshes_destroyed:
                                        textbutton '“{color=#f6d6bd}White Marshes{/color} is no more, and its undead may soon come here. I don’t believe your wall and foragers will be enough to keep you safe.”' action [SetVariable("questionpreset", 0), SetVariable("can_rest", 0), Jump("foggylakeregularquesaboutnomoreundead03")] style "nvl_button" text_slow_cps True
                                if (foggy_about_personalquestions_amount < foggy_about_personalquestions_amount_max and (foggy_friendship+appearance_charisma) >= 5) or (foggy_about_personalquestions_amount < foggy_about_personalquestions_amount_max and not foggy_about_personalquestions):
                                    textbutton '“I’d like to learn more about your tavern.”' action [SetVariable("questionpreset", 0), SetVariable("can_rest", 0), Jump("foggylakeregularquestionspersonalquestions01")] style "nvl_button" text_slow_cps True
                                elif (foggy_about_personalquestions_amount < foggy_about_personalquestions_amount_max and foggy_about_personalquestions and (foggy_friendship+appearance_charisma) < 5):
                                    textbutton 'She doesn’t trust me enough to tell me more about herself.' action NullAction() style "nvl_button2" text_slow_cps True
                                if foggylake_alchemytable_firsttime:
                                    textbutton '“Time for me to go.”' action [SetVariable("questionpreset", 0), Jump("foggylakeafterfoggy01")] style "nvl_button" text_slow_cps True
                                else:
                                    textbutton '“Time for me to go.”' action [SetVariable("questionpreset", 0), Jump("foggylakeoutside01")] style "nvl_button" text_slow_cps True

                            elif questionpreset == "foggy2":
                                if not foggy_about_hertavern:
                                    textbutton '“What’s the story behind this place? It can’t be more than a few years old.”' action [SetVariable("questionpreset", 0), SetVariable("foggy_about_personalquestions_amount", foggy_about_personalquestions_amount+1), Jump("foggylakepersonalquestionsaboutthetavern01")] style "nvl_button" text_slow_cps True
                                if foggy_about_hertavern and not foggy_about_beastsaround:
                                    textbutton '“How do you stay safe from the beasts? You’re completely open from the lake.”' action [SetVariable("questionpreset", 0), SetVariable("foggy_about_personalquestions_amount", foggy_about_personalquestions_amount+1), Jump("foggylakepersonalquestionsaboutbeastsaround01")] style "nvl_button" text_slow_cps True
                                if foggy_about_beastsaround and not foggy_about_hunting:
                                    textbutton '“Any interesting beasts you hunt for?”' action [SetVariable("questionpreset", 0), SetVariable("foggy_about_personalquestions_amount", foggy_about_personalquestions_amount+1), Jump("foggylakepersonalquestionsabouthunting01")] style "nvl_button" text_slow_cps True
                                if not foggy_about_herself:
                                    textbutton '“What brought you North? You don’t look like someone who spends their life cleaning tables.”' action [SetVariable("questionpreset", 0), SetVariable("foggy_about_personalquestions_amount", foggy_about_personalquestions_amount+1), Jump("foggylakepersonalquestionsaboutherself01")] style "nvl_button" text_slow_cps True
                                if foggy_about_herself and foggy_about_hertavern and not foggy_about_thename:
                                    textbutton '“Your name’s {color=#f6d6bd}Foggy{/color}, and this is {color=#f6d6bd}Foggy Lake{/color}... Is the tavern named after you, or after the lake?”' action [SetVariable("questionpreset", 0), SetVariable("foggy_about_personalquestions_amount", foggy_about_personalquestions_amount+1), Jump("foggylakepersonalquestionsaboutthename01")] style "nvl_button" text_slow_cps True
                                if foggy_about_herself and not foggy_about_herarm:
                                    textbutton 'I nod toward the spot where her right arm should be. “Any story there?”' action [SetVariable("questionpreset", 0), SetVariable("foggy_about_personalquestions_amount", foggy_about_personalquestions_amount+1), Jump("foggylakepersonalquestionsaboutherarm01")] style "nvl_button" text_slow_cps True
                                if foggy_about_herself and not foggy_about_hermagic:
                                    textbutton '“So... You can move things with your thoughts.”' action [SetVariable("questionpreset", 0), SetVariable("foggy_about_personalquestions_amount", foggy_about_personalquestions_amount+1), Jump("foggylakepersonalquestionsabouthermagic01")] style "nvl_button" text_slow_cps True
                                if foggy_about_herself and not foggy_about_herplans:
                                    textbutton '“What’s going to happen next? Will you build a real wall?”' action [SetVariable("questionpreset", 0), SetVariable("foggy_about_personalquestions_amount", foggy_about_personalquestions_amount+1), Jump("foggylakepersonalquestionsaboutherplans01")] style "nvl_button" text_slow_cps True
                                if not foggy_about_alcohol:
                                    textbutton '“You seem to be into some expensive drinks.”' action [SetVariable("questionpreset", 0), SetVariable("foggy_about_personalquestions_amount", foggy_about_personalquestions_amount+1), Jump("foggylakepersonalquestionsaboutheralcohols01")] style "nvl_button" text_slow_cps True
                                textbutton '“Let’s change the topic.”' action [SetVariable("questionpreset", 0), Jump("foggylakefoggyafterinteraction01allpersonalquestions")] style "nvl_button" text_slow_cps True

                            elif questionpreset == "foragers1":
                                if quest_birdhunting == 1 and quest_birdhunting_description06:
                                    textbutton 'I was asked to take the news about the caught bird to Creeks.' action NullAction() style "nvl_button2" text_slow_cps True
                                if quest_asterion == 1 and quest_gatheracrew == 1 and not asterion_found and not foragers_about_gatherthecrew_tzvi_recruited and not foragers_about_gatherthecrew_rejected:
                                    if not foragers_about_gatherthecrew:
                                        $ options_foragers += 1
                                        textbutton '“I’m looking for a few souls willing to explore {color=#f6d6bd}High Island{/color} with me.”' action [SetVariable("questionpreset", 0), Jump("foggylakeforagersregularquestionsaboutgatherthecrew01")] style "nvl_button" text_slow_cps True
                                    else:
                                        $ options_foragers += 1
                                        textbutton '“Let’s discuss the price, {color=#f6d6bd}Tzvi{/color}.”' action [SetVariable("questionpreset", 0), Jump("foggylakeforagersregularquestionsaboutgatherthecrew02")] style "nvl_button" text_slow_cps True
                                if quest_missinghunters == 1 and not foragers_about_missinghunters:
                                    $ options_foragers += 1
                                    textbutton '“{color=#f6d6bd}Admon{/color}, {color=#f6d6bd}Dalia{/color}, and {color=#f6d6bd}Vaschel{/color} didn’t return from their hunting trip. Did they share any plans with you?”' action [SetVariable("questionpreset", 0), Jump("foggylakeforagersregularquestionsaboutmissinghunters01")] style "nvl_button" text_slow_cps True
                                if oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_knowledge and not foragers_about_traps:
                                    $ options_foragers += 1
                                    textbutton '“You know this and that about traps. Can you teach me how to build them?”' action [SetVariable("questionpreset", 0), Jump("foggylakeforagersregularquestionsabouttraps01")] style "nvl_button" text_slow_cps True
                                if not foragers_quest:
                                    $ options_foragers += 1
                                    textbutton '“What’s your plan? I could use some work.”' action [SetVariable("questionpreset", 0), Jump("foggylakeforagersregularquestionsaboutwork01")] style "nvl_button" text_slow_cps True
                                if quest_birdhunting > 0 and quest_birdhunting < 3 and efren_about_birdhunting == 2 and not foragers_quest_question_efren:
                                    $ options_foragers += 1
                                    textbutton '“A little wolf told me you didn’t ask any of the hunters to go with you.”' action [SetVariable("questionpreset", 0), Jump("foggylakeforagersregularquestionsaboutefrenandhunt01")] style "nvl_button" text_slow_cps True
                                if quest_birdhunting == 1 and not foragingground_bird_taken and quarters < (world_daylength-20) and pc_hp > 1 and day >= foragers_quest_daythreshold:
                                    $ options_foragers += 1
                                    textbutton '“I have everything I need. Let’s hunt while it’s still early.”' action [SetVariable("questionpreset", 0), Jump("foggylakeforagersregularquestionsaboutwork02")] style "nvl_button" text_slow_cps True
                                if quest_birdhunting == 1 and not foragingground_bird_taken and quarters >= (world_daylength-20) and day >= foragers_quest_daythreshold:
                                    textbutton 'The hour is too late for us to start our hunt.' action NullAction() style "nvl_button2" text_slow_cps True
                                if quest_birdhunting == 1 and not foragingground_bird_taken and day < foragers_quest_daythreshold:
                                    $ foragers_quest_daythreshold_display = (foragers_quest_daythreshold-day)
                                    textbutton 'They won’t be ready to start the hunt for [foragers_quest_daythreshold_display] more days.' action NullAction() style "nvl_button2" text_slow_cps True
                                if quest_birdhunting == 1 and not foragingground_bird_taken and pc_hp <= 1:
                                    textbutton 'I’m too tired to hunt.' action NullAction() style "nvl_button2" text_slow_cps True
                                if foragers_caius_heardabout and not foragers_caius_spokento:
                                    $ options_foragers += 1
                                    textbutton 'I turn toward the one without a hand. “Do you know {color=#f6d6bd}Tulia{/color}?”' action [SetVariable("questionpreset", 0), Jump("foggylakeforagersregularquestionsabouttulia01")] style "nvl_button" text_slow_cps True
                                if not foragers_caius_aboutvision_gray:
                                    if (foggy_about_militarycamp and not foragers_caius_heardabout and not foragers_caius_aboutvision) or (foragers_caius_heardabout and foragers_caius_spokento and not foragers_caius_aboutvision):
                                        if foragers_caius_spokento != day:
                                            $ options_foragers += 1
                                            textbutton '“So, {color=#f6d6bd}Caius{/color}. Your boss told me you have some sort of visions.”' action [SetVariable("questionpreset", 0), Jump("foggylakeforagersregularquestionsaboutvisions01")] style "nvl_button" text_slow_cps True
                                        else:
                                            textbutton 'Caius seems to be too on edge to speak any more. He won’t tell me about his visions.' action NullAction() style "nvl_button2" text_slow_cps True
                                else:
                                    if (foragers_caius_friendship+appearance_charisma) >= 2:
                                        if (foggy_about_militarycamp and not foragers_caius_heardabout and not foragers_caius_aboutvision) or (foragers_caius_heardabout and foragers_caius_spokento and not foragers_caius_aboutvision):
                                            if foragers_caius_spokento != day:
                                                $ options_foragers += 1
                                                textbutton '“So, {color=#f6d6bd}Caius{/color}. About these visions...”' action [SetVariable("questionpreset", 0), Jump("foggylakeforagersregularquestionsaboutvisions01")] style "nvl_button" text_slow_cps True
                                            else:
                                                textbutton 'Caius seems to be too on edge to speak any more. He won’t tell me about his visions.' action NullAction() style "nvl_button2" text_slow_cps True
                                    elif not foragers_caius_aboutvision:
                                        if (foggy_about_militarycamp and not foragers_caius_heardabout and not foragers_caius_aboutvision) or (foragers_caius_heardabout and foragers_caius_spokento and not foragers_caius_aboutvision):
                                            textbutton 'Caius doesn’t trust me enough to tell me about his visions.' action NullAction() style "nvl_button2" text_slow_cps True
                                if not quest_recruitahunter_spokento_foragers and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed:
                                    $ options_foragers += 1
                                    textbutton '“Have you ever met {color=#f6d6bd}Erastos{/color}, the trapper?”' action [SetVariable("questionpreset", 0), Jump("foragers_about_recruitahunter01")] style "nvl_button" text_slow_cps True
                                if not foragers_about_travelers:
                                    $ options_foragers += 1
                                    textbutton '“Do you often have travelers here?”' action [SetVariable("questionpreset", 0), Jump("foggylakeforagersregularquestionsabouttravelers01")] style "nvl_button" text_slow_cps True
                                if not foragers_about_rumors:
                                    $ options_foragers += 1
                                    textbutton '“What can you tell me about the peninsula?”' action [SetVariable("questionpreset", 0), Jump("foggylakeforagersregularquestionsaboutpeninsula01")] style "nvl_button" text_slow_cps True
                                if ruinedshelter_mushrooms and not foggy_about_mushroomsinruinedshelter and not foragers_about_mushrooms:
                                    $ options_foragers += 1
                                    textbutton '“I saw a lot of mushrooms at the ruined shelter in the west. A lot of bugs, too.”' action [SetVariable("questionpreset", 0), Jump("foggylakeforagersaboutmushrooms01")] style "nvl_button" text_slow_cps True
                                if not options_foragers:
                                    textbutton 'I have nothing more to say.' action NullAction() style "nvl_button2" text_slow_cps True
                                textbutton 'I walk away.' action [SetVariable("questionpreset", 0), Jump("foggylakeafterforagers01")] style "nvl_button" text_slow_cps True

                            elif questionpreset == "elah1":
                                if quest_missinghunters_description01 and not creeks_feast:
                                    $ options_elah += 1
                                    textbutton '“I was told to speak with you about the funeral rites. Let’s begin the preparations.”' action [SetVariable("questionpreset", 0), Jump("creekselahonfeast01")] style "nvl_button" text_slow_cps True
                                if not oldhava_known:
                                    $ options_elah += 1
                                    textbutton '“I’m looking for supplies.”' action [SetVariable("questionpreset", 0), Jump("creekselahonsupplies01")] style "nvl_button" text_slow_cps True
                                if oldhava_about_foggy >= 2 and creeks_mundanework and not creeks_mundanework_betterpay:
                                    $ options_elah += 1
                                    textbutton '“Let’s talk about the patrols you want to pay me for.”' action [SetVariable("questionpreset", 0), Jump("creekselahonmundaneworkbetterpay01")] style "nvl_button" text_slow_cps True
                                if not elah_about_plague1 and oldpagos_plague_known and oldpagos_cured:
                                    $ options_elah += 1
                                    textbutton '“There are many things occuring at {color=#f6d6bd}Old Págos{/color}... The village was suffering from a plague, but I helped to clear it. It now isolates itself from outsiders.”' action [SetVariable("questionpreset", 0), Jump("elah_about_plague2alt")] style "nvl_button" text_slow_cps True
                                elif elah_about_plague1 and not elah_about_plague2 and oldpagos_cured:
                                    $ options_elah += 1
                                    textbutton '“I’ve helped to clear the plague from {color=#f6d6bd}Old Págos{/color}. It may not be a safe place, but it will survive.”' action [SetVariable("questionpreset", 0), Jump("elah_about_plague2")] style "nvl_button" text_slow_cps True
                                elif not elah_about_plague1 and oldpagos_plague_known:
                                    $ options_elah += 1
                                    textbutton '“{color=#f6d6bd}Old Págos{/color} is suffering from a plague. The village is isolating itself from outsiders.”' action [SetVariable("questionpreset", 0), Jump("elah_about_plague1")] style "nvl_button" text_slow_cps True
                                if ruinedvillage_confront_can and not ruinedvillage_truth and not elah_about_steephouse and not elah_about_steephouse_canceled:
                                    if (elah_friendship+appearance_charisma) >= elah_about_steephouse_friendship and elah_about_steephouse_gray:
                                        $ options_elah += 1
                                        textbutton '“{color=#f6d6bd}Elah{/color}, I {i}need{/i} to know what happened ten years ago. Don’t you trust me?”' action [SetVariable("questionpreset", 0), Jump("elah_about_steephouse02")] style "nvl_button" text_slow_cps True
                                    elif quest_ruins_10yclue07 and elah_about_steephouse_gray and not elah_about_steephouse_friendship_thais:
                                        $ options_elah += 1
                                        textbutton '“I know that your tribe has witnessed nefarious deeds ten years ago. You must know more than what you said about the ruins.”' action [SetVariable("questionpreset", 0), Jump("elah_about_steephouse01reduction")] style "nvl_button" text_slow_cps True
                                    elif (elah_friendship+appearance_charisma) < elah_about_steephouse_friendship and elah_about_steephouse_gray:
                                        textbutton 'He gets upset even at the mention of the ruins.' action NullAction() style "nvl_button2" text_slow_cps True
                                    else:
                                        $ options_elah += 1
                                        textbutton '“What do you know about the ruins of the village in the south?”' action [SetVariable("questionpreset", 0), Jump("elah_about_steephouse01")] style "nvl_button" text_slow_cps True
                                if (quest_intelforpeltnorth and not quest_intelforpeltnorth_description04b) or (banditshideout_bandits_pchearedabout == 1 and not quest_intelforpeltnorth_description04b):
                                    if elah_about_bandits == 1:
                                        if (elah_friendship+appearance_charisma) < 4:
                                            textbutton 'He pretends that there are no bandits in the north. I need to gain his trust.' action NullAction() style "nvl_button2" text_slow_cps True
                                        else:
                                            $ options_elah += 1
                                            textbutton '“I’m worried about those bandits, {color=#f6d6bd}Elah{/color}.”' action [SetVariable("questionpreset", 0), Jump("creekselah_about_bandits02")] style "nvl_button" text_slow_cps True
                                        if banditshideout_firsttime:
                                            $ options_elah += 1
                                            textbutton 'I pressure him about the bandits. “I already met with {color=#f6d6bd}Glaucia{/color}, {i}friend{/i}. Don’t hide things from me.”' action [SetVariable("questionpreset", 0), Jump("creekselah_about_bandits02alt")] style "nvl_button" text_slow_cps True
                                        elif elah_about_asterion == 3:
                                            $ options_elah += 1
                                            textbutton 'I pressure him about the bandits. “You told me yourself about {color=#f6d6bd}Glaucia{/color}, {i}friend{/i}. Don’t hide things from me.”' action [SetVariable("questionpreset", 0), Jump("creekselah_about_bandits02alt2")] style "nvl_button" text_slow_cps True
                                    elif not elah_about_bandits:
                                        $ options_elah += 1
                                        textbutton '“I’ve heard about the bandits. Have they caused you any troubles?”' action [SetVariable("questionpreset", 0), Jump("creekselah_about_bandits01")] style "nvl_button" text_slow_cps True
                                if quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_creeks and not elah_about_bronzerod:
                                    $ options_elah += 1
                                    textbutton '“I’d like to place this rod somewhere high. It belongs to {color=#f6d6bd}Eudocia{/color}, the enchantress.”' action [SetVariable("questionpreset", 0), Jump("elah_about_bronzerod01")] style "nvl_button" text_slow_cps True
                                if quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_creeks and elah_about_bronzerod and (creeks_reputation+elah_friendship+appearance_charisma) < 10 and not creeks_feast:
                                    textbutton 'The village won’t accept the Eudocia’s rod anytime soon.' action NullAction() style "nvl_button2" text_slow_cps True
                                elif (quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_creeks and elah_about_bronzerod and (creeks_reputation+elah_friendship+appearance_charisma) >= 10) or (quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_creeks and elah_about_bronzerod and creeks_feast):
                                    $ options_elah += 1
                                    textbutton '“I want you to discuss the issue of the enchantress’ rod with the village. You should know by now I can be trusted.”' action [SetVariable("questionpreset", 0), Jump("elah_about_bronzerod02")] style "nvl_button" text_slow_cps True
                                if not orentius_met and not whitemarshes_attacked and not whitemarshes_nomoreundead:
                                    if quest_orentius == 1 and quest_orentius_thais_description00 and not quest_orentius_thais_description00betrayal and not thais_defeated and not quest_orentius_thais_description10 and quest_orentius_thais_description03 and not quest_orentius_thais_description03a05:
                                        $ options_elah += 1
                                        textbutton '“You know who {color=#f6d6bd}Thais{/color} is, right? She may need your help. It’s about {color=#f6d6bd}Orentius{/color}.”' action [SetVariable("questionpreset", 0), Jump("elahaboutorentius01")] style "nvl_button" text_slow_cps True
                                elif whitemarshes_nomoreundead and not elah_about_nomoreundead:
                                    if orentius_convinced:
                                        $ options_elah += 1
                                        textbutton '“The north will be a bit safer. The priest of {color=#f6d6bd}White Marshes{/color} has agreed to no longer use the undead.”' action [SetVariable("questionpreset", 0), Jump("elah_about_nomoreundead01")] style "nvl_button" text_slow_cps True
                                    elif orentius_banished:
                                        $ options_elah += 1
                                        textbutton '“The north will be a bit safer. {color=#f6d6bd}White Marshes{/color} no longer uses undead, though they had to be persuaded with force.”' action [SetVariable("questionpreset", 0), Jump("elah_about_nomoreundead02")] style "nvl_button" text_slow_cps True
                                    elif whitemarshes_destroyed:
                                        $ options_elah += 1
                                        textbutton '“Hard days may soon come. {color=#f6d6bd}White Marshes{/color} is destroyed, a large group of undead may strike after just a few fogs.”' action [SetVariable("questionpreset", 0), Jump("elah_about_nomoreundead03")] style "nvl_button" text_slow_cps True
                                if quest_asterion == 1 and not asterion_found and not elah_about_asterion:
                                    $ options_elah += 1
                                    textbutton '“Is {color=#f6d6bd}Asterion{/color} around?”' action [SetVariable("questionpreset", 0), Jump("creekselah_about_asterion01")] style "nvl_button" text_slow_cps True
                                if quest_asterion == 1 and not asterion_found and elah_about_asterion == 1 and elah_about_asterion_friendship >= 2:
                                    $ options_elah += 1
                                    textbutton '“People say that {color=#f6d6bd}Asterion{/color} has spent a lot of time in your village. You’re hiding something.”' action [SetVariable("questionpreset", 0), Jump("creekselah_about_asterion02")] style "nvl_button" text_slow_cps True
                                elif quest_asterion == 1 and not asterion_found and elah_about_asterion == 2 and elah_about_asterion_friendship >= 2 and (creeks_reputation+elah_friendship+appearance_charisma) >= 8:
                                    $ options_elah += 1
                                    textbutton '“Be serious now, {color=#f6d6bd}Elah{/color}. I need to know what happened to {color=#f6d6bd}Asterion{/color}.”' action [SetVariable("questionpreset", 0), Jump("creekselah_about_asterion03")] style "nvl_button" text_slow_cps True
                                elif quest_asterion == 1 and not asterion_found and elah_about_asterion == 2 and elah_about_asterion_friendship == 1:
                                    textbutton 'According to the rumors I’ve gathered, Elah hides what he knows about Asterion. I need more evidence before I accuse him of a lie.' action NullAction() style "nvl_button2" text_slow_cps True
                                if elah_about_asterion and asterion_found and not elah_about_asterion_found:
                                    $ options_elah += 1
                                    textbutton '“{color=#f6d6bd}Asterion{/color} is dead. I found his shell.”' action [SetVariable("questionpreset", 0), Jump("creekselahaboutfindingasterion01")] style "nvl_button" text_slow_cps True
                                if not elah_about_creeks:
                                    $ options_elah += 1
                                    textbutton '“This village isn’t much older than you are... What’s its story?”' action [SetVariable("questionpreset", 0), Jump("elah_about_creeks01")] style "nvl_button" text_slow_cps True
                                if not elah_about_peninsula:
                                    $ options_elah += 1
                                    textbutton '“I’d like to learn more about the peninsula.”' action [SetVariable("questionpreset", 0), Jump("elah_about_peninsula01")] style "nvl_button" text_slow_cps True
                                if quest_reachthepaganvillage and elah_about_peninsula and not elah_about_greenmountaintribe:
                                    $ options_elah += 1
                                    textbutton '“Have you ever met {color=#f6d6bd}The Tribe of The Green Mountain{/color}?”' action [SetVariable("questionpreset", 0), Jump("elah_about_greenmountaintribe01")] style "nvl_button" text_slow_cps True
                                if oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_knowledge and not elah_about_traps:
                                    $ options_elah += 1
                                    textbutton '“Let’s say you would need to place some traps in an old tunnel...”' action [SetVariable("questionpreset", 0), Jump("creekselahontraps01")] style "nvl_button" text_slow_cps True
                                if elah_efren_siblings and not elah_about_efren:
                                    $ options_elah += 1
                                    textbutton '“What do you think about {color=#f6d6bd}Efren{/color}?”' action [SetVariable("questionpreset", 0), Jump("creekselahonefren01")] style "nvl_button" text_slow_cps True
                                elif elah_efren_siblings and elah_about_efren == 1 and (elah_friendship+appearance_charisma) >= 4:
                                    $ options_elah += 1
                                    textbutton '“I was wondering about {color=#f6d6bd}Efren{/color}...”' action [SetVariable("questionpreset", 0), Jump("creekselahonefren02")] style "nvl_button" text_slow_cps True
                                elif elah_efren_siblings and elah_about_efren == 1 and (elah_friendship+appearance_charisma) < 4:
                                    textbutton 'He doesn’t trust me enough to tell me about his brother.' action NullAction() style "nvl_button2" text_slow_cps True
                                if (quest_easternpath_description00 and not quest_easternpath_description01) or (quest_easternpath_description_teaser and not quest_easternpath_description01):
                                    $ options_elah += 1
                                    textbutton '“I’ve heard you have some issues with the eastern path.”' action [SetVariable("questionpreset", 0), Jump("creekselahonquest_easternpath01alt")] style "nvl_button" text_slow_cps True
                                elif not quest_easternpath_description01:
                                    $ options_elah += 1
                                    textbutton '“Do you have any work for a roadwarden?”' action [SetVariable("questionpreset", 0), Jump("creekselahonquest_easternpath01")] style "nvl_button" text_slow_cps True
                                if quest_easternpath_description01 and quest_easternpath == 1:
                                    $ options_elah += 1
                                    textbutton '“About the eastern path...”' action [SetVariable("questionpreset", 0), Jump("creekselahonquest_easternpath02")] style "nvl_button" text_slow_cps True
                                elif (quest_easternpath == 2 and quest_easternpath_description03 and not quest_easternpath_description03a) or (quest_easternpath == 2 and quest_easternpath_description03alt and not quest_easternpath_description03aalt) or (quest_easternpath == 2 and quest_easternpath_description04 and not quest_easternpath_description04a) or (quest_easternpath == 2 and quest_easternpath_description05 and not quest_easternpath_description05a) or (quest_easternpath == 2 and quest_easternpath_description06 and not quest_easternpath_description06a) or (quest_easternpath == 2 and quest_easternpath_description06alt and not quest_easternpath_description06aalt) or (quest_easternpath == 2 and quest_easternpath_description07 and not quest_easternpath_description07a) or (quest_easternpath == 2 and quest_easternpath_description08 and not quest_easternpath_description08a) or (quest_easternpath == 2 and quest_easternpath_description08alt and not quest_easternpath_description08aalt) or (quest_easternpath == 2 and quest_easternpath_description09 and not quest_easternpath_description09a and not quest_easternpath_description09b) or (quest_easternpath == 2 and quest_easternpath_description09a and not quest_easternpath_description09aa) or (quest_easternpath == 2 and quest_easternpath_description10 and not quest_easternpath_description10a) or (eudocia_about_roadclearing_cleared and not quest_easternpath_description13) or (shortcut_westernentrance_firsttime and shortcut_ibex and shortcut_deepforest_firsttime and shortcut_deepforest_babydragon and shortcut_deepforest_treant and shortcut_deepforest_frightape and shortcut_deepforest_fruitgrove and shortcut_cairn_firsttime and shortcut_meadow_firsttime and shortcut_woodenroad_firsttime and shortcut_woodenroad_stoathunt and shortcut_woodenroad_fisheater and shortcut_woodenroad_horseaccident and shortcut_woodenroad_drinkingcat and shortcut_darkforest_firsttime and shortcut_darkforest_bandit and shortcut_darkforest_goblins and shortcut_darkforest_bagontree and shortcut_darkforest_birdfollower and shortcut_easternentrance_firsttime and shortcut_easternentrance_gnolls and not quest_easternpath_description11):
                                    $ options_elah += 1
                                    textbutton '“I have made some additional progress with the eastern path.”' action [SetVariable("questionpreset", 0), Jump("creekselahonquest_easternpath03")] style "nvl_button" text_slow_cps True
                                elif quest_easternpath == 2:
                                    textbutton 'I made no additional progress with the eastern path.' action NullAction() style "nvl_button2" text_slow_cps True
                                if not elah_about_himself:
                                    $ options_elah += 1
                                    textbutton '“I imagine being a carpenter in this part of the realm isn’t easy.”' action [SetVariable("questionpreset", 0), Jump("elah_about_himself01")] style "nvl_button" text_slow_cps True
                                if elah_about_himself and oldtunnel_inside_firsttime and not item_lantern and not elah_about_makingalantern_made:
                                    if not elah_about_makingalantern:
                                        $ options_elah += 1
                                        textbutton '“I need a wooden lantern, one useful for an adventurer.”' action [SetVariable("questionpreset", 0), Jump("elah_about_makingalantern01")] style "nvl_button" text_slow_cps True
                                    elif (elah_friendship+appearance_charisma) < elah_about_makingalantern_threshhold:
                                        textbutton 'He refuses to work on a lantern with me.' action NullAction() style "nvl_button2" text_slow_cps True
                                    elif quarters > (world_daylength-28):
                                        textbutton 'It’s too late to start working on a lantern.' action NullAction() style "nvl_button2" text_slow_cps True
                                    else:
                                        $ options_elah += 1
                                        textbutton '“I have time now. Want to help me build a lantern?”' action [SetVariable("questionpreset", 0), Jump("elah_about_makingalantern02")] style "nvl_button" text_slow_cps True
                                if not options_elah:
                                    textbutton 'I have nothing more to say.' action NullAction() style "nvl_button2" text_slow_cps True
                                textbutton '“I’ll see you later.”' action [SetVariable("questionpreset", 0), Jump("creeksleavingelah01")] style "nvl_button" text_slow_cps True

                            elif questionpreset == "efren1":
                                if not asterion_found and quest_asterion == 1 and quest_gatheracrew == 1 and quest_missinghunters_description02 and not efren_about_highisland_recruitment_done:
                                    $ options_efren += 1
                                    textbutton '“I need your help on {color=#f6d6bd}High Island{/color}. It will make us even.”' action [SetVariable("questionpreset", 0), Jump("creeksefren_about_highisland02")] style "nvl_button" text_slow_cps True
                                if asterion_highisland_knowsabout and not asterion_found and not efren_about_highisland:
                                    $ options_efren += 1
                                    textbutton '“Do you know of any creatures that live on {color=#f6d6bd}High Island{/color}?”' action [SetVariable("questionpreset", 0), Jump("creeksefren_about_highisland01")] style "nvl_button" text_slow_cps True
                                if elah_efren_siblings and not efren_about_elah:
                                    $ options_efren += 1
                                    textbutton '“What do you think about {color=#f6d6bd}Elah{/color}?”' action [SetVariable("questionpreset", 0), Jump("creeksefrenonelah01")] style "nvl_button" text_slow_cps True
                                elif elah_efren_siblings and efren_about_elah == 1 and (efren_friendship+appearance_charisma) >= 3:
                                    $ options_efren += 1
                                    textbutton '“I was wondering about {color=#f6d6bd}Elah{/color}...”' action [SetVariable("questionpreset", 0), Jump("creeksefrenonelah02")] style "nvl_button" text_slow_cps True
                                elif elah_efren_siblings and efren_about_elah == 1 and (efren_friendship+appearance_charisma) < 3:
                                    textbutton 'He doesn’t trust me enough to tell me about his brother.' action NullAction() style "nvl_button2" text_slow_cps True
                                if creek_woodenweapons and not efren_about_weapons:
                                    $ options_efren += 1
                                    textbutton '“I noticed that no soul in your tribe carries a weapon that would contain iron or copper.”' action [SetVariable("questionpreset", 0), Jump("creeksefrenaboutwoodenweapons01")] style "nvl_button" text_slow_cps True
                                if not efren_about_himself:
                                    $ options_efren += 1
                                    if day <= 20:
                                        textbutton '“Are you the only hunter around?”' action [SetVariable("questionpreset", 0), Jump("creeksefren_about_himself01")] style "nvl_button" text_slow_cps True
                                    else:
                                        textbutton '“Are you the only hunter around?”' action [SetVariable("questionpreset", 0), Jump("creeksefren_about_himself01alt")] style "nvl_button" text_slow_cps True
                                if efren_about_himself and not quest_missinghunters:
                                    $ options_efren += 1
                                    if day <= 5:
                                        textbutton '“Aren’t you worried about the other hunters?”' action [SetVariable("questionpreset", 0), Jump("creeksefrenaboutmissinghunters01v1")] style "nvl_button" text_slow_cps True
                                    elif day <= 10:
                                        textbutton '“Why do you think these other hunters aren’t back yet?”' action [SetVariable("questionpreset", 0), Jump("creeksefrenaboutmissinghunters01v3")] style "nvl_button" text_slow_cps True
                                    else:
                                        textbutton '“I’ll try to find these hunters. Tell me what you know.”' action [SetVariable("questionpreset", 0), Jump("creeksefrenaboutmissinghunters01v3")] style "nvl_button" text_slow_cps True
                                if quest_missinghunters == 1 and quest_missinghunters_reported < 3 and not quest_missinghunters_gaveup:
                                    $ options_efren += 1
                                    textbutton '“About the hunters...”' action [SetVariable("questionpreset", 0), Jump("creeksefrenaboutmissinghunters02")] style "nvl_button" text_slow_cps True
                                if efren_about_himself and not efren_about_peltnorthhunters:
                                    if description_bighunters01 or description_bighunters02 or description_bighunters03 or description_bighunters04 or description_bighunters05 or description_bighunters06:
                                        $ options_efren += 1
                                        textbutton '“Do the hunters from {color=#f6d6bd}Pelt of the North{/color} hinder your job?”' action [SetVariable("questionpreset", 0), Jump("creeksefren_about_peltnorthhunters01")] style "nvl_button" text_slow_cps True
                                if oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_knowledge:
                                    $ options_efren += 1
                                    textbutton '“What sort of traps would you put in an old tunnel?”' action [SetVariable("questionpreset", 0), Jump("creeksefrenontraps01")] style "nvl_button" text_slow_cps True
                                if quest_reachthepaganvillage and not efren_about_greenmountaintribe:
                                    $ options_efren += 1
                                    textbutton '“Have you ever met {color=#f6d6bd}The Tribe of The Green Mountain{/color}?”' action [SetVariable("questionpreset", 0), Jump("efren_about_greenmountaintribe01")] style "nvl_button" text_slow_cps True
                                if (efren_about_peltnorthhunters and not quest_recruitahunter_spokento_efren and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed) or (efren_about_peltnorthhunters and not quest_recruitahunter_spokento_efren and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed):
                                    $ options_efren += 1
                                    textbutton '“Have you ever had an opportunity to work with {color=#f6d6bd}Erastos{/color} from {color=#f6d6bd}Howler’s Dell{/color} and {color=#f6d6bd}Cassia{/color} from {color=#f6d6bd}Gale Rocks{/color}? Do they know their trade?”' action [SetVariable("questionpreset", 0), Jump("creeksefren_about_peltnorthhunters02")] style "nvl_button" text_slow_cps True
                                if shortcut_pcknowsabout and not efren_about_shortcut:
                                    $ options_efren += 1
                                    textbutton '“What do you know about the road running through the heart of the forest?”' action [SetVariable("questionpreset", 0), Jump("creeksefren_about_shortcut01")] style "nvl_button" text_slow_cps True
                                if quest_birdhunting == 1 and not foragingground_bird_taken and not efren_about_birdhunting:
                                    $ options_efren += 1
                                    textbutton '“I plan to help {color=#f6d6bd}the foragers{/color} with catching a big runner. Any tips on how to approach this?”' action [SetVariable("questionpreset", 0), Jump("creeksefren_about_birdhunting01")] style "nvl_button" text_slow_cps True
                                if not options_efren:
                                    textbutton 'I have nothing more to say.' action NullAction() style "nvl_button2" text_slow_cps True
                                textbutton 'I walk away. “Have a good hunting.”' action [SetVariable("questionpreset", 0), Jump("creeksleavingefren01")] style "nvl_button" text_slow_cps True

                            elif questionpreset == "creeksfeast1":
                                if creeks_reasonstojoin_beastattacks and druidcave_druid_about_peninsula and not creeks_reasonstojoin_feast_beastattacks:
                                    $ options_creeks += 1
                                    textbutton '“An old druid who lives on the opposite side of the peninsula told me about the recent migrations of beasts in the North. You’ve been struggling with monsters for decades now - it’s finally a time for you to seek allies.”' action [Jump("creeksefeastaboutbeastattacks01")] style "nvl_button" text_slow_cps True
                                elif creeks_reasonstojoin_beastattacks and quest_explorepeninsula_description04 and not creeks_reasonstojoin_feast_beastattacks:
                                    $ options_creeks += 1
                                    textbutton '“I’ve heard about the recent migrations of beasts in the North. You’ve been struggling with monsters for decades now - it’s finally a time for you to seek allies.”' action [Jump("creeksefeastaboutbeastattacks01alt")] style "nvl_button" text_slow_cps True
                                if creeks_reasonstojoin_lackofmetal and not creeks_reasonstojoin_feast_lackofmetal:
                                    $ options_creeks += 1
                                    textbutton '“I’ve seen your tools, weapons, houses. You {i}need{/i} iron, you {i}need{/i} copper. {color=#f6d6bd}Hovlavan{/color} will help you gain steel, bronze, and brass.”' action [Jump("creeksefeastaboutlackofmetal01")] style "nvl_button" text_slow_cps True
                                if creeks_reasonstojoin_creeksaboutlackingmeat and not creeks_reasonstojoin_feast_lackofmeat:
                                    $ options_creeks += 1
                                    textbutton '“I know you don’t have as many supplies as you need. Depending on animals you keep alive to butcher is not a safe way to deal with winters.”' action [SetVariable("questionpreset", 0), Jump("creeksefeastaboutmeat01")] style "nvl_button" text_slow_cps True
                                if creeks_reasonstojoin_creeksaboutlackingwall and not creeks_reasonstojoin_feast_lackingwall:
                                    $ options_creeks += 1
                                    textbutton '“You don’t really believe this wall will keep you safe, do you? Without a forest garden, you lack wood, and you can’t afford stone. You need proper guards to protect your homes and lumberjacks.”' action [Jump("creeksefeastaboutlackingwall01")] style "nvl_button" text_slow_cps True
                                if creeks_reasonstojoin_creeksaboutweakness and not creeks_reasonstojoin_feast_weakness:
                                    $ options_creeks += 1
                                    textbutton 'I look at {color=#f6d6bd}Elah{/color} and {color=#f6d6bd}Efren{/color}. “I know you don’t agree what it means to be {i}weak{/i}, but you don’t have to. With allies at your side, the days of weakness won’t be so punishing.”' action [Jump("creeksefeastaboutweakness01")] style "nvl_button" text_slow_cps True
                                if creeks_reasonstojoin_hpcknowstruthaboutinbreeding and not creeks_reasonstojoin_feast_inbreeding:
                                    $ options_creeks += 1
                                    textbutton '“Your blood is growing thick. You can seek new settlers among cityfolk, or use the safer roads to find willing people at other villages.”' action [Jump("creeksefeastaboutinbreeding1")] style "nvl_button" text_slow_cps True
                                if creeks_reasonstojoin_lackingseeds and not creeks_reasonstojoin_feast_lakingseeds:
                                    $ options_creeks += 1
                                    textbutton '“You want to grow crops, but you have no experience. With the city’s help, you may hire a specialist to teach you everything you need to know, and invest in the best seeds.”' action [Jump("creeksefeastaboutseeds01")] style "nvl_button" text_slow_cps True
                                if creeks_reasonstojoin_hruinedvillage_truth and ruinedvillage_name == "Steep House" and not creeks_reasonstojoin_feast_steephouse:
                                    $ options_creeks += 1
                                    textbutton 'I take a longer pause and scowl at the tribe. “You know well what happened to {color=#f6d6bd}Steep House{/color}. Are you truly willing to trust that none of your neighbors will look at your village with a greedy eye once you get prosperous?”' action [Jump("creeksefeastaboutsteephouse01")] style "nvl_button" text_slow_cps True
                                if quest_missinghunters_admonfound == 2 and quest_missinghunters_daliafound == 2 and quest_missinghunters_vaschelfound == 2 and not creeks_reasonstojoin_feast_missinghunters:
                                    $ options_creeks += 1
                                    textbutton '“You know how dangerous this land is. I brought you evidence that I found three of your finest hunters fallen by beasts. You can’t afford more losses, and you can see that {i}cityfolk{/i} can get things done.”' action [Jump("creeksefeastaboutmissinghunters01")] style "nvl_button" text_slow_cps True
                                if creeks_reasonstojoin_healedtheplague and elah_about_plague2 and not creeks_reasonstojoin_feast_plague:
                                    $ options_creeks += 1
                                    textbutton '“Sooner or later, a plague will reach your village. Living in isolation will postpone this day, but once it comes, how can you know help will ever come? Your best chance is to keep people like me around.”' action [Jump("creeksefeastaboutplague01")] style "nvl_button" text_slow_cps True
                                if quest_easternpath == 2 and not creeks_reasonstojoin_feast_easternpath:
                                    $ options_creeks += 1
                                    textbutton '“Just look how much work I was able to complete at the eastern path. You can’t keep it clear all by yourself, but with the city’s army and regular merchant trips it will endure winters and rains.”' action [Jump("creeksefeastabouteasternpath01")] style "nvl_button" text_slow_cps True
                                if not options_creeks:
                                    textbutton '“I have nothing more to add.”' action [SetVariable("questionpreset", 0), Jump("creeksefeastafterallreasons01")] style "nvl_button" text_slow_cps True
                                if not creeks_reasonstojoin_feast_reputation:
                                    textbutton '{image=d6} It’s risky, but... “You know me well, I have your trust. I wouldn’t try to trick you.”' action [Jump("creeksefeastaboutreputation01")] style "nvl_button" text_slow_cps True
                                if oldhava_about_foggy == 2 and not creeks_reasonstojoin_feast_foggy:
                                    textbutton '{image=d6} Maybe I shouldn’t try it, but... “{color=#f6d6bd}Foggy{/color}, won’t you vouch for me? You know I’m a valuable ally, and the tribe depends on your tavern. The city will bring many more people to help you.”' action [Jump("creeksefeastaboutfoggy01")] style "nvl_button" text_slow_cps True
                                if foragingground_foraging_vein and not foragingground_foraging_vein_sabotaged and not creeks_reasonstojoin_feast_copper:
                                    textbutton 'I should take it directly to the guild, but... “You want to be sure that your worth is going to be seen and respected? I’ll give you something you’ll use to gain an edge. I know where you can find copper.”' action [Jump("creeksefeastaboutcopper01")] style "nvl_button" text_slow_cps True

                            elif questionpreset == "photios1":
                                if asterion_highisland_knowsabout and not asterion_found and not galerocks_photios_about_highisland:
                                    textbutton '“Have you ever been to {color=#f6d6bd}High Island{/color}?”' action [SetVariable("questionpreset", 0), Jump("galerocks_photios_about_highisland01")] style "nvl_button" text_slow_cps True
                                if not galerocks_photios_about_mundanejob:
                                    textbutton '“Do you have any work for me?”' action [SetVariable("questionpreset", 0), Jump("galerocks_photios_about_mundanejob01")] style "nvl_button" text_slow_cps True
                                if galerocks_photios_about_mundanejob:
                                    if quarters < 48 and pc_hp >= 2:
                                        textbutton '{image=cointest} “Need help with fishing today?”' action [SetVariable("questionpreset", 0), Jump("galerocksphotiosofferingmundanejob01")] style "nvl_button" text_slow_cps True
                                    else:
                                        if quarters >= 48 and pc_hp < 2:
                                            textbutton '{image=coingray} It’s too late and I’m too exhausted to join the fishers in their work. (Required vitality: 2)' action NullAction() style "nvl_button2" text_slow_cps True
                                        elif quarters >= 48:
                                            textbutton '{image=coingray} It’s too late for me to join the fishers in their work.' action NullAction() style "nvl_button2" text_slow_cps True
                                        elif pc_hp < 2:
                                            textbutton '{image=coingray} I’m too exhausted to join the fishers in their work. (Required vitality: 2)' action NullAction() style "nvl_button2" text_slow_cps True
                                if galerocks_photios_about_mundanejob and not quest_spiritrock:
                                    textbutton '“Are you sure you don’t need help with something that would fit my... Skills? I spend many hours on the road.”' action [SetVariable("questionpreset", 0), Jump("galerocks_photios_quest_spiritrock01")] style "nvl_button" text_slow_cps True
                                if quest_spiritrock == 1:
                                    textbutton '“About the spirit rock...”' action [SetVariable("questionpreset", 0), Jump("galerocks_photios_quest_spiritrock02")] style "nvl_button" text_slow_cps True
                                if quest_empresscarp == 1 and not item_empresscarp and not galerocks_photios_about_empresscarp:
                                    textbutton '“I was sent here by an old druid from the South. He claims that you owe him a male empress carp.”' action [SetVariable("questionpreset", 0), Jump("galerocks_photios_about_empresscarp01")] style "nvl_button" text_slow_cps True
                                if galerocks_photios_about_empresscarp_ordered == day and not item_empresscarp:
                                    textbutton 'The empress carp should be here tomorrow.' action NullAction() style "nvl_button2" text_slow_cps True
                                if galerocks_photios_about_empresscarp_ordered and galerocks_photios_about_empresscarp_ordered < day and not item_empresscarp and not galerocks_photios_about_empresscarp_bought and not galerocks_photios_about_empresscarp_caught:
                                    textbutton '“Did you catch the empress carp?”' action [SetVariable("questionpreset", 0), Jump("galerocks_photios_about_empresscarp02")] style "nvl_button" text_slow_cps True
                                if galerocks_photios_about_empresscarp_ordered and galerocks_photios_about_empresscarp_ordered < day and not item_empresscarp and not galerocks_photios_about_empresscarp_bought and galerocks_photios_about_empresscarp_caught:
                                    textbutton '“I still need an empress carp.”' action [SetVariable("questionpreset", 0), Jump("galerocks_photios_about_empresscarp02alt")] style "nvl_button" text_slow_cps True
                                if quest_empresscarp == 1 and not item_empresscarp and galerocks_photios_about_empresscarp and galerocks_photios_about_empresscarp_bought:
                                    textbutton '“I need another empress carp.”' action [SetVariable("questionpreset", 0), Jump("galerocks_photios_about_empresscarp03")] style "nvl_button" text_slow_cps True
                                if not quest_recruitahunter_spokento_photios and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed:
                                    if not quest_recruitahunter_spokento_photios_gray:
                                        textbutton '“Is {color=#f6d6bd}Cassia{/color} working with you often?”' action [SetVariable("questionpreset", 0), Jump("photios_about_recruitahunter01")] style "nvl_button" text_slow_cps True
                                    elif (galerocks_photios_friendship+appearance_charisma+galerocks_reputation) < 6 and not quest_spiritrock == 2:
                                        textbutton 'He’s not willing to speak about Cassia with me.' action NullAction() style "nvl_button2" text_slow_cps True
                                    else:
                                        textbutton '“Why does {color=#f6d6bd}Cassia{/color} annoy you?”' action [SetVariable("questionpreset", 0), Jump("photios_about_recruitahunter01alt")] style "nvl_button" text_slow_cps True
                                if galerocks_photios_about_beingafisher:
                                    textbutton '“What’s it like, being a fisher?”' action [SetVariable("questionpreset", 0), Jump("galerocks_photios_about_beingafisher01")] style "nvl_button" text_slow_cps True
                                if (item_fishtrap and galerocks_photios_about_beingafisher and not galerocks_photios_about_fishtraps) or (achievement_fish and galerocks_photios_about_beingafisher and not galerocks_photios_about_fishtraps):
                                    textbutton '“Wouldn’t it be easier for you to use the fish traps? Like a basket?”' action [SetVariable("questionpreset", 0), Jump("galerocks_photios_about_fishtraps01")] style "nvl_button" text_slow_cps True
                                if galerocks_photios_quest_spiritrock_dayofcompleting and galerocks_photios_quest_spiritrock_dayofcompleting < day and not galerocks_photios_quest_spiritrock_about_phoibe_after:
                                    textbutton '“How’s {color=#f6d6bd}Phoibe{/color} doing?”' action [SetVariable("questionpreset", 0), Jump("galerocks_photios_quest_spiritrockaskingaboutphoibe01")] style "nvl_button" text_slow_cps True
                                if pc_area == "galerocks":
                                    textbutton '“See you later.”' action [SetVariable("questionpreset", 0), Jump("galerocksafterinteraction01")] style "nvl_button" text_slow_cps True
                                if pc_area == "beforebeach":
                                    textbutton '“See you later.”' action [SetVariable("questionpreset", 0), Jump("beforebeachafterinteraction01")] style "nvl_button" text_slow_cps True
                                if pc_area == "beach":
                                    textbutton '“See you later.”' action [SetVariable("questionpreset", 0), Jump("beachafterinteraction01")] style "nvl_button" text_slow_cps True

                            elif questionpreset == "severina1":
                                if banditshideout_galerocks_tiestobandits and quest_lostmerchants == 2 and not quest_galerockssupport:
                                    $ options_severina += 1
                                    textbutton '“You don’t just {i}speak{/i} with {color=#f6d6bd}Glaucia{/color}. You collaborate with her, and you got betrayed.”' action [SetVariable("questionpreset", 0), Jump("severina_about_bandits02")] style "nvl_button" text_slow_cps True
                                if quest_galerockssupport == 1:
                                    $ options_severina += 1
                                    textbutton '“I’m ready to present my case against {color=#f6d6bd}Glaucia{/color} to the council.”' action [SetVariable("questionpreset", 0), Jump("galerocksdebate01")] style "nvl_button" text_slow_cps True
                                elif severina_about_bandits and banditshideout_galerocks_tiestobandits and not quest_galerockssupport and quest_lostmerchants != 3:
                                    textbutton 'I need to have stronger evidence before I confront her about her collaboration with the bandits.' action NullAction() style "nvl_button2" text_slow_cps True
                                if galerocks_singlepeople_marina_notmatched and galerocks_singlepeople_paulus_matched and not severina_about_matchmaking_reward:
                                    $ options_severina += 1
                                    textbutton '“I believe {color=#f6d6bd}Paulus{/color} and {color=#f6d6bd}Marina{/color} already talked with you.”' action [SetVariable("questionpreset", 0), Jump("severina_about_matchmaking_reward01")] style "nvl_button" text_slow_cps True
                                if galerocks_watchtowerkey_knows and not watchtower_open and not severina_about_keytowatchtower:
                                    $ options_severina += 1
                                    textbutton '“I’d like to get inside the watchtower standing at the eastern road.”' action [SetVariable("questionpreset", 0), Jump("severina_about_keytowatchtower01")] style "nvl_button" text_slow_cps True
                                elif galerocks_watchtowerkey_knows and not watchtower_open and severina_about_keytowatchtower == 1 and (severina_friendship+galerocks_reputation+appearance_charisma) >= 6:
                                    $ options_severina += 1
                                    textbutton '“Can I borrow the key to the watchtower?”' action [SetVariable("questionpreset", 0), Jump("severina_about_keytowatchtower02")] style "nvl_button" text_slow_cps True
                                elif galerocks_watchtowerkey_knows and not watchtower_open and severina_about_keytowatchtower == 1 and (severina_friendship+galerocks_reputation+appearance_charisma) < 6:
                                    textbutton 'Before she gives me the key to the watchtower, I need to prove to her that I’m worth her trust.' action NullAction() style "nvl_button2" text_slow_cps True
                                if galerocks_pastrobbery and item_ironingot and severina_about_pastrobbery != 2:
                                    $ options_severina += 1
                                    textbutton '“I believe this ingot belongs to your people.”' action [SetVariable("questionpreset", 0), Jump("severina_receivesironingot01")] style "nvl_button" text_slow_cps True
                                if not severina_about_plague1 and oldpagos_plague_known and oldpagos_cured:
                                    $ options_severina += 1
                                    textbutton '“The village of {color=#f6d6bd}Old Págos{/color} has been struggling with a plague. I’ve helped them overcome it, but the seasons to come will be grim for them.”' action [SetVariable("questionpreset", 0), Jump("severina_about_plague02alt")] style "nvl_button" text_slow_cps True
                                elif not severina_about_plague2 and oldpagos_cured:
                                    $ options_severina += 1
                                    textbutton '“I’ve helped to cure the plague of {color=#f6d6bd}Old Págos{/color}, but the seasons to come will be grim for them.”' action [SetVariable("questionpreset", 0), Jump("severina_about_plague02")] style "nvl_button" text_slow_cps True
                                elif not severina_about_plague1 and oldpagos_plague_known:
                                    $ options_severina += 1
                                    textbutton '“The village of {color=#f6d6bd}Old Págos{/color} is struggling with a plague, and isolates itself from trade and travelers.”' action [SetVariable("questionpreset", 0), Jump("severina_about_plague1")] style "nvl_button" text_slow_cps True
                                if severina_about_plague1 and oldpagos_about_galerocks and not severina_about_galerockshelpingoldpagos1:
                                    $ options_severina += 1
                                    textbutton '“The people of {color=#f6d6bd}Old Págos{/color} could use an {i}old friend{/i} right now. Maybe some supplies for winter.”' action [SetVariable("questionpreset", 0), Jump("severina_about_galerockshelpingoldpagos01")] style "nvl_button" text_slow_cps True
                                elif severina_about_galerockshelpingoldpagos1 and quest_lostmerchants == 2 and banditshideout_galerocks_tiestobandits and not severina_about_galerockshelpingoldpagos2:
                                    $ options_severina += 1
                                    textbutton '“You say that the people of {color=#f6d6bd}Old Págos{/color} have accused you of thievery, but you do know already that {color=#f6d6bd}Glaucia{/color} lied to you about different events. You could heal the old wounds by helping the sick and weak.”' action [SetVariable("questionpreset", 0), Jump("severina_about_galerockshelpingoldpagos02")] style "nvl_button" text_slow_cps True
                                if not quest_recruitahunter_spokento_severina and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed:
                                    $ options_severina += 1
                                    textbutton '“What are your thoughts on {color=#f6d6bd}Cassia{/color}?”' action [SetVariable("questionpreset", 0), Jump("severina_about_recruitahunter01")] style "nvl_button" text_slow_cps True
                                if not severina_about_greenmountaintribe and quest_reachthepaganvillage == 1:
                                    $ options_severina += 1
                                    textbutton '“I’ve heard something about {color=#f6d6bd}The Tribe of The Green Mountain{/color}.”' action [SetVariable("questionpreset", 0), Jump("severina_aboutthegreenmountaintribe01")] style "nvl_button" text_slow_cps True
                                if not orentius_met and not whitemarshes_attacked and not whitemarshes_nomoreundead:
                                    if not severina_about_undead1 and not whitemarshes_firsttime:
                                        $ options_severina += 1
                                        textbutton '“I’ve heard about some necromancers in the North.”' action [SetVariable("questionpreset", 0), Jump("severina_about_undead01")] style "nvl_button" text_slow_cps True
                                    if not severina_about_undead1 and whitemarshes_firsttime:
                                        $ options_severina += 1
                                        textbutton '“What are your thoughts about the necromancers in {color=#f6d6bd}White Marshes{/color}?”' action [SetVariable("questionpreset", 0), Jump("severina_about_undead01alt")] style "nvl_button" text_slow_cps True
                                    if not severina_about_undead2 and severina_about_undead1 and galerocks_church_knowsabout >= 2 and not severina_about_orentius:
                                        $ options_severina += 1
                                        textbutton '“Considering that the people of your village follow The Wright, I’m surprised you’re not pressured into taking action against the undead of {color=#f6d6bd}White Marshes{/color}.”' action [SetVariable("questionpreset", 0), Jump("severina_about_undead02")] style "nvl_button" text_slow_cps True
                                    if quest_orentius == 1 and quest_orentius_thais_description00 and not quest_orentius_thais_description00betrayal and not thais_defeated and not quest_orentius_thais_description10 and quest_orentius_thais_description03 and not quest_orentius_thais_description03a06:
                                        $ options_severina += 1
                                        textbutton '“{color=#f6d6bd}Thais{/color} of {color=#f6d6bd}Howler’s Dell{/color} considers confronting {color=#f6d6bd}Orentius{/color}, the necromancer, directly. Will your people aid her in this task?”' action [SetVariable("questionpreset", 0), Jump("severina_about_orentius01")] style "nvl_button" text_slow_cps True
                                elif whitemarshes_nomoreundead and not severina_about_nomoreundead:
                                    if orentius_convinced:
                                        $ options_severina += 1
                                        textbutton '“I bring news about {color=#f6d6bd}White Marshes{/color}. The local necromancer has agreed to abandon his practice.”' action [SetVariable("questionpreset", 0), Jump("severina_about_nomoreundead01")] style "nvl_button" text_slow_cps True
                                    elif orentius_banished:
                                        $ options_severina += 1
                                        textbutton '“I bring news about {color=#f6d6bd}White Marshes{/color}. The local necromancer has been taken away from the village, but not before he turned his awoken into a pile of flesh.”' action [SetVariable("questionpreset", 0), Jump("severina_about_nomoreundead02")] style "nvl_button" text_slow_cps True
                                    elif whitemarshes_destroyed:
                                        $ options_severina += 1
                                        textbutton '“{color=#f6d6bd}White Marshes{/color} has fallen, but it’s undead are going to roam through the North. You may want to work on your defenses, and soon.”' action [SetVariable("questionpreset", 0), Jump("severina_about_nomoreundead03")] style "nvl_button" text_slow_cps True
                                if (not severina_about_bandits and quest_intelforpeltnorth and not banditshideout_galerocks_tiestobandits) or (not severina_about_bandits and banditshideout_bandits_pchearedabout == 1):
                                    $ options_severina += 1
                                    textbutton '“Did the village face any struggles with the bandits?”' action [SetVariable("questionpreset", 0), Jump("severina_about_bandits01")] style "nvl_button" text_slow_cps True
                                if asterion_highisland_knowsabout and not asterion_found and not severina_about_highisland:
                                    $ options_severina += 1
                                    textbutton '“I’m trying to learn more about {color=#f6d6bd}High Island{/color}.”' action [SetVariable("questionpreset", 0), Jump("severina_about_highisland01")] style "nvl_button" text_slow_cps True
                                if ruinedvillage_confront_can and not ruinedvillage_truth and not severina_about_steephouse:
                                    $ options_severina += 1
                                    textbutton '“I believe something awful happened to the village in the distant south, the one turned to ruins. Could you tell me anything about it?”' action [SetVariable("questionpreset", 0), Jump("severina_about_steephouse01")] style "nvl_button" text_slow_cps True
                                if not severina_quest_lostmerchants:
                                    $ options_severina += 1
                                    textbutton '“I spend a lot of time traveling between places. Do you have any work for me?”' action [SetVariable("questionpreset", 0), Jump("severina_quest_lostmerchants01")] style "nvl_button" text_slow_cps True
                                elif severina_quest_lostmerchants == 1 and (severina_friendship+galerocks_reputation+appearance_charisma) >= 7:
                                    $ options_severina += 1
                                    textbutton '“I could still do some work for you.”' action [SetVariable("questionpreset", 0), Jump("severina_quest_lostmerchants02")] style "nvl_button" text_slow_cps True
                                elif severina_quest_lostmerchants == 1 and (severina_friendship+galerocks_reputation+appearance_charisma) < 7:
                                    textbutton 'She doesn’t trust me enough to give me any work.' action NullAction() style "nvl_button2" text_slow_cps True
                                elif severina_quest_lostmerchants == 2 and quest_lostmerchants == 1:
                                    $ options_severina += 1
                                    textbutton '“About the lost merchants...”' action [SetVariable("questionpreset", 0), Jump("severina_quest_lostmerchants03")] style "nvl_button" text_slow_cps True
                                if not oldtunnel_inside_opened and not severina_about_oldtunnel:
                                    $ options_severina += 1
                                    textbutton '“What can you tell me about the tunnel, south from here?”' action [SetVariable("questionpreset", 0), Jump("severina_about_oldtunnel01")] style "nvl_button" text_slow_cps True
                                if oldtunnel_inside_opened and item_oldtunnelkey and not severina_about_clearedoldtunnel:
                                    $ options_severina += 1
                                    textbutton 'I put the gate key on her desk. “The undead from your tunnel are gone.”' action [SetVariable("questionpreset", 0), Jump("severina_about_clearedoldtunnel01")] style "nvl_button" text_slow_cps True
                                if quest_asterion == 1 and not asterion_found and not severina_about_asterion1:
                                    $ options_severina += 1
                                    textbutton '“Have you seen {color=#f6d6bd}Asterion{/color} recently? He’s also a roadwarden.”' action [SetVariable("questionpreset", 0), Jump("severina_about_asterion101")] style "nvl_button" text_slow_cps True
                                if asterion_found and severina_about_asterion1 and not severina_about_asterion2:
                                    $ options_severina += 1
                                    textbutton '“I found {color=#f6d6bd}Asterion{/color} on {color=#f6d6bd}High Island{/color}.”' action [SetVariable("questionpreset", 0), Jump("severina_about_asterion202")] style "nvl_button" text_slow_cps True
                                if not severina_about_galerocks and severina_friendship < 5:
                                    $ options_severina += 1
                                    textbutton '“Can you tell me a bit about {color=#f6d6bd}Gale Rocks{/color}?”' action [SetVariable("questionpreset", 0), Jump("severina_about_galerocks01")] style "nvl_button" text_slow_cps True
                                if not options_severina:
                                    textbutton 'I have nothing else to say.' action NullAction() style "nvl_button2" text_slow_cps True
                                textbutton '“Farewell.”' action [SetVariable("questionpreset", 0), Jump("galerocksleavingseverina01")] style "nvl_button" text_slow_cps True

                            elif questionpreset == "galerocksdebate":
                                if not galerocks_debate_argument_glauciaisallaboutrevenge and description_glaucia12 and description_glaucia06 and ruinedvillage_truth:
                                    $ options_galerocks += 1
                                    textbutton '“{color=#f6d6bd}Glaucia’s{/color} priority is to take revenge on those who mistreated her, not to build a better life for herself, and even less so for {color=#f6d6bd}Gale Rocks{/color}.”' action [Jump("galerocks_debate_argument_glauciaisallaboutrevenge01")] style "nvl_button" text_slow_cps True
                                if (not galerocks_debate_argument_oldtunnelgetsmoredangerous and severina_about_clearedoldtunnel) or (not galerocks_debate_argument_oldtunnelgetsmoredangerous and galerocks_iuno_about_oldtunnel_cleared) or (not galerocks_debate_argument_oldtunnelgetsmoredangerous and description_glaucia15):
                                    $ options_galerocks += 1
                                    textbutton '“Even though {color=#f6d6bd}Glaucia’s{/color} band knows only combat, they didn’t move a finger to secure the tunnel in the south. It’s no surprise to me that the wilds reclaim the roads with such ease.”' action [Jump("galerocks_debate_argument_oldtunnelgetsmoredangerous01")] style "nvl_button" text_slow_cps True
                                if (not galerocks_debate_argument_arrow and galerocks_florus_about_arrow and item_arrow):
                                    $ options_galerocks += 1
                                    textbutton '“I found this arrow at the place where {color=#f6d6bd}Glaucia{/color} attacked the merchants. You know it well - it was meant to kill humans, {i}especially{/i} humans. She’s ready to hurt others for her gain.”' action [Jump("galerocks_debate_argument_arrow01")] style "nvl_button" text_slow_cps True
                                if (not galerocks_debate_argument_stealingfromoldpagos and oldpagos_about_galerocks) or (not galerocks_debate_argument_stealingfromoldpagos and severina_about_galerockshelpingoldpagos2):
                                    $ options_galerocks += 1
                                    textbutton '“The people of {color=#f6d6bd}Old Págos{/color} no longer trust you. You’ve lost a valuable ally.”' action [Jump("galerocks_debate_argument_stealingfromoldpagos01")] style "nvl_button" text_slow_cps True
                                if not galerocks_debate_argument_glauciawenttoofarforexbandit and description_glaucia09:
                                    $ options_galerocks += 1
                                    textbutton '“{color=#f6d6bd}Glaucia’s{/color} own people already see that she’s going too far. I spoke with one of them, he left her band in secret.”' action [Jump("galerocks_debate_argument_glauciawenttoofarforexbandit01")] style "nvl_button" text_slow_cps True
                                if not galerocks_debate_argument_quintusthreatened and description_glaucia07:
                                    $ options_galerocks += 1
                                    textbutton '“{color=#f6d6bd}Glaucia{/color} is putting the lives of others into danger, out of fear of her.” I tell them about {color=#f6d6bd}Quintus{/color}.' action [Jump("galerocks_debate_argument_quintusthreatened01")] style "nvl_button" text_slow_cps True
                                if (not galerocks_debate_argument_peopleareafraidofher and description_bandits05 and quest_intelforpeltnorth and description_glaucia04) or (not galerocks_debate_argument_peopleareafraidofher and description_bandits05 and quest_intelforpeltnorth and eudocia_about_bandits_gray) or (not galerocks_debate_argument_peopleareafraidofher and quest_asterion_description15 and quest_intelforpeltnorth and description_glaucia04) or (not galerocks_debate_argument_peopleareafraidofher and quest_asterion_description15 and quest_intelforpeltnorth and eudocia_about_bandits_gray):
                                    $ options_galerocks += 1
                                    textbutton '“{color=#f6d6bd}Asterion{/color} is no longer around, but he also recognized the threat presented by {color=#f6d6bd}Glaucia{/color}. People are afraid of her. {color=#f6d6bd}Eudocia{/color}, {color=#f6d6bd}[iason_name]{/color}. Trade can’t go on like this.”' action [Jump("galerocks_debate_argument_peopleareafraidofher01")] style "nvl_button" text_slow_cps True
                                if (not galerocks_debate_argument_creekssupport and quest_creekssupport == 2) and (not galerocks_debate_argument_howlersdellsupport and quest_howlerssupport == 2):
                                    $ options_galerocks += 1
                                    textbutton '“Both {color=#f6d6bd}Creeks{/color} and {color=#f6d6bd}Howler’s Dell{/color} are already willing to negotiate with {color=#f6d6bd}Hovlavan{/color}. Don’t let yourself stay behind.”' action [Jump("galerocks_debate_argument_creeksandhowlersdellsupport01")] style "nvl_button" text_slow_cps True
                                elif (not galerocks_debate_argument_creekssupport and quest_creekssupport == 2):
                                    $ options_galerocks += 1
                                    textbutton '“{color=#f6d6bd}Creeks{/color} is already willing to negotiate with {color=#f6d6bd}Hovlavan{/color}. The endeavour to make the peninsula safer may be easier than you think.”' action [Jump("galerocks_debate_argument_creekssupport01")] style "nvl_button" text_slow_cps True
                                elif (not galerocks_debate_argument_howlersdellsupport and quest_howlerssupport == 2):
                                    $ options_galerocks += 1
                                    textbutton '“{color=#f6d6bd}Howler’s Dell{/color} is already willing to negotiate with {color=#f6d6bd}Hovlavan{/color}. The endeavour to make the peninsula safer may be easier than you think.”' action [Jump("galerocks_debate_argument_howlersdellsupport01")] style "nvl_button" text_slow_cps True
                                if not galerocks_debate_argument_hidingthingsfromthelocals and description_glaucia14:
                                    $ options_galerocks += 1
                                    textbutton '“If you’ve no doubt your support for the bandits is justified, why do most of your people have no right to know the truth about everything that {color=#f6d6bd}Glaucia{/color} has done? She’s far from being just a {i}treasure hunter{/i}.”' action [Jump("galerocks_debate_argument_hidingthingsfromthelocals01")] style "nvl_button" text_slow_cps True
                                if not galerocks_debate_argument_oldhavastory and description_glaucia10:
                                    $ options_galerocks += 1
                                    textbutton 'I think about {color=#f6d6bd}Old Hava{/color}. “Every bandit leader falls to their own desires, bringing only more suffering onto others.”' action [Jump("galerocks_debate_argument_oldhavastory01")] style "nvl_button" text_slow_cps True
                                if not options_galerocks or quest_glauciasupport:
                                    textbutton '“That’s all I have to say.”' action [SetVariable("questionpreset", 0), Jump("severina_debatediscussion01")] style "nvl_button" text_slow_cps True
                                if (not galerocks_debate_argument_livinginsin and severina_about_priest) or (not galerocks_debate_argument_livinginsin and galerocks_church_knowsabout >= 4 and galerocks_priest_firsttime):
                                    textbutton 'It’s risky, but... “Should followers of The Wright really provide support for a group of outlaws?”' action [Jump("galerocks_debate_argument_livinginsin01")] style "nvl_button" text_slow_cps True

                            elif questionpreset == "cephasgaiane1":
                                $ options_cephasgaiane_highisland = 0
                                if quest_asterion == 1 and asterion_highisland_knowsabout and not asterion_found and highisland_howtoreach_pcknows and not cephasgaiane_about_highisland_question1:
                                    $ options_cephasgaiane_highisland += 1
                                elif quest_asterion == 1 and asterion_highisland_knowsabout and not asterion_found and highisland_howtoreach_pcknows and cephasgaiane_about_highisland_question1 == 1 and (greenmountaintribe_reputation+(appearance_charisma/2)) >= greenmountaintribe_asterion_permission_threshold:
                                    $ options_cephasgaiane_highisland += 1
                                elif quest_asterion == 1 and asterion_highisland_knowsabout and not asterion_found and highisland_howtoreach_pcknows and cephasgaiane_about_highisland_question1 == 1 and (greenmountaintribe_reputation+(appearance_charisma/2)) < greenmountaintribe_asterion_permission_threshold:
                                    $ options_cephasgaiane_highisland += 1
                                if quest_asterion == 1 and asterion_highisland_knowsabout and not asterion_found and not highisland_howtoreach_pcknows and not cephasgaiane_about_highisland_question1:
                                    $ options_cephasgaiane_highisland += 1
                                elif quest_asterion == 1 and asterion_highisland_knowsabout and not asterion_found and not highisland_howtoreach_pcknows and cephasgaiane_about_highisland_question1 == 1 and (greenmountaintribe_reputation+(appearance_charisma/2)) >= greenmountaintribe_asterion_permission_threshold:
                                    $ options_cephasgaiane_highisland += 1
                                elif quest_asterion == 1 and asterion_highisland_knowsabout and not asterion_found and not highisland_howtoreach_pcknows and cephasgaiane_about_highisland_question1 == 1 and (greenmountaintribe_reputation+(appearance_charisma/2)) < greenmountaintribe_asterion_permission_threshold:
                                    $ options_cephasgaiane_highisland += 1
                                if cephasgaiane_about_highisland_question1 and not cephasgaiane_about_highisland_question2:
                                    $ options_cephasgaiane_highisland += 1
                                if not cephasgaiane_about_highisland_question3:
                                    $ options_cephasgaiane_highisland += 1
                                if cephasgaiane_about_highisland_question3 and not cephasgaiane_about_highisland_question4:
                                    $ options_cephasgaiane_highisland += 1
                                if not asterion_found and not cephasgaiane_about_highisland_question6:
                                    $ options_cephasgaiane_highisland += 1
                                if quest_asterion == 1 and cephasgaiane_about_highisland_question1 == 2 and not asterion_found and not cephasgaiane_about_highisland_question7:
                                    $ options_cephasgaiane_highisland += 1
                                if quest_asterion == 1 and quest_sleepinggiant < 2 and not asterion_found and not giantstatue_pray_map_learned and cephasgaiane_about_highisland_question7 and not cephasgaiane_about_highisland_question8:
                                    $ options_cephasgaiane_highisland += 1
                                if quest_asterion == 1 and quest_sleepinggiant < 2 and not asterion_found and giantstatue_pray_map_learned and cephasgaiane_about_highisland_question7 and not cephasgaiane_about_highisland_question8:
                                    $ options_cephasgaiane_highisland += 1
                                if (asterion_found and cephasgaiane_about_asterion1 and not cephasgaiane_about_asterion4) or (asterion_found and cephasgaiane_about_highisland and not cephasgaiane_about_asterion4):
                                    $ options_cephasgaiane += 1
                                    textbutton '“I bring you news of what I saw on {color=#f6d6bd}High Island{/color}.”' action [Jump("cephasgaiane_about_asterion401")] style "nvl_button" text_slow_cps True
                                if quest_asterion == 1 and not asterion_found and not cephasgaiane_about_asterion1:
                                    $ options_cephasgaiane += 1
                                    textbutton '“I’m trying to find {color=#f6d6bd}Asterion{/color}.”' action [Jump("cephasgaiane_about_asterion101")] style "nvl_button" text_slow_cps True
                                if quest_asterion == 1 and not asterion_found and cephasgaiane_about_asterion1 and not cephasgaiane_about_asterion1a:
                                    $ options_cephasgaiane += 1
                                    textbutton '“What kind of person is {color=#f6d6bd}Asterion{/color}?”' action [Jump("cephasgaiane_about_asterion101a")] style "nvl_button" text_slow_cps True
                                if (cephasgaiane_about_asterion1 and description_asterion08 and not cephasgaiane_about_asterion2) or (cephasgaiane_about_asterion1 and greenmountaintribe_firstattitude == "vulnerable" and not cephasgaiane_about_asterion2):
                                    $ options_cephasgaiane += 1
                                    textbutton '“That saurian I saw outside... It used to belong to {color=#f6d6bd}Asterion{/color}, am I right?”' action [Jump("cephasgaiane_about_asterion201")] style "nvl_button" text_slow_cps True
                                if quest_asterion == 1 and not asterion_found and cephasgaiane_about_asterion1 and not asterion_highisland_knowsabout and not cephasgaiane_about_asterion3:
                                    $ options_cephasgaiane += 1
                                    textbutton '“But where did {color=#f6d6bd}Asterion{/color} go?”' action [Jump("cephasgaiane_about_asterion301")] style "nvl_button" text_slow_cps True
                                elif quest_asterion == 1 and not asterion_found and cephasgaiane_about_asterion1 and not asterion_highisland_knowsabout and cephasgaiane_about_asterion3 == 1 and (greenmountaintribe_reputation+(appearance_charisma/2)) >= greenmountaintribe_asterion_permission_threshold-1:
                                    $ options_cephasgaiane += 1
                                    textbutton '“I {i}need{/i} to learn where did {color=#f6d6bd}Asterion{/color} go.”' action [SetVariable("questionpreset", 0), Jump("cephasgaiane_about_asterion302")] style "nvl_button" text_slow_cps True
                                elif quest_asterion == 1 and not asterion_found and cephasgaiane_about_asterion1 and not asterion_highisland_knowsabout and cephasgaiane_about_asterion3 == 1 and (greenmountaintribe_reputation+(appearance_charisma/2)) < greenmountaintribe_asterion_permission_threshold-1:
                                    textbutton 'He’s not willing to tell me about {color=#f6d6bd}Asterion’s{/color} journey.' action NullAction() style "nvl_button2" text_slow_cps True
                                    if (greenmountaintribe_reputation+(appearance_charisma/2)) >= (greenmountaintribe_asterion_permission_threshold-3) and cephasgaiane_shop:
                                        if item_axe02alt or item_axehead or item_axeset or item_axe03 or item_cidercask or item_ironingot or item_sealskin or item_spices or item_beholderroot:
                                            if cephasgaiane_shop_dragonhorn:
                                                textbutton '“I’d like to offer you a gift, as a sign of my good will.”' action [Jump("cephasgaiane_shop_freegift01")] style "nvl_button" text_slow_cps True
                                            else:
                                                textbutton 'Maybe I should earn their trust by starting with a simple barter.' action NullAction() style "nvl_button2" text_slow_cps True
                                        else:
                                            textbutton 'I could offer them a gift to show my good will, but I’ve nothing they’d be interested in.' action NullAction() style "nvl_button2" text_slow_cps True
                                    elif (greenmountaintribe_reputation+(appearance_charisma/2)) < (greenmountaintribe_asterion_permission_threshold-3) and cephasgaiane_shop:
                                        textbutton 'I could offer them a gift to show my good will, but I doubt they’ll accept it.' action NullAction() style "nvl_button2" text_slow_cps True
                                if not cephasgaiane_about_tribe:
                                    $ options_cephasgaiane += 1
                                    textbutton '“I’d like to learn more about your village.”' action [Jump("cephasgaiane_about_tribe01")] style "nvl_button" text_slow_cps True
                                if cephasgaiane_about_tribe and not cephasgaiane_about_chiefandshaman:
                                    $ options_cephasgaiane += 1
                                    textbutton '“Who’s the decision maker in the village? The chief, or the shaman?”' action [Jump("cephasgaiane_about_chiefandshaman01")] style "nvl_button" text_slow_cps True
                                if not cephasgaiane_about_work:
                                    $ options_cephasgaiane += 1
                                    textbutton '“Can I help you with anything, as a roadwarden?”' action [Jump("cephasgaiane_about_work01")] style "nvl_button" text_slow_cps True
                                if cephasgaiane_about_tribe and not cephasgaiane_about_city:
                                    $ options_cephasgaiane += 1
                                    textbutton '“What do you think about {color=#f6d6bd}Hovlavan{/color}?”' action [Jump("cephasgaiane_about_city01")] style "nvl_button" text_slow_cps True
                                if cephasgaiane_about_tribe and not cephasgaiane_about_mountain:
                                    $ options_cephasgaiane += 1
                                    textbutton '“I expected this mountain to be a bit more... {i}green{/i}.”' action [Jump("cephasgaiane_about_mountain01")] style "nvl_button" text_slow_cps True
                                if oldpagos_plague_known and not cephasgaiane_about_notcaring and not cephasgaiane_about_plague:
                                    $ options_cephasgaiane += 1
                                    textbutton '“{color=#f6d6bd}Old Págos{/color}, the village on the opposite side of the peninsula, was attacked by a plague.”' action [Jump("cephasgaiane_about_plague01")] style "nvl_button" text_slow_cps True
                                if whitemarshes_firsttime and not cephasgaiane_about_notcaring and not cephasgaiane_about_necromancers:
                                    $ options_cephasgaiane += 1
                                    textbutton '“Have you heard about the necromancers living in the far west?”' action [Jump("cephasgaiane_about_necromancers01")] style "nvl_button" text_slow_cps True
                                if (quest_intelforpeltnorth and not cephasgaiane_about_notcaring and not cephasgaiane_about_bandits) or (banditshideout_bandits_pchearedabout and not cephasgaiane_about_notcaring and not cephasgaiane_about_bandits):
                                    $ options_cephasgaiane += 1
                                    textbutton '“The roads in the west grow more dangerous as they struggle with bandits.”' action [Jump("cephasgaiane_about_bandits01")] style "nvl_button" text_slow_cps True
                                if not cephasgaiane_shop:
                                    $ options_cephasgaiane += 1
                                    textbutton '“The roads are dangerous. Do you have any useful equipment to sell?”' action [Jump("cephasgaiane_shop01")] style "nvl_button" text_slow_cps True
                                elif cephasgaiane_shop and not cephasgaiane_shop_dragonhorn:
                                    textbutton '{image=cointest} “Let’s barter.”' action [Jump("cephasgaiane_shop02")] style "nvl_button" text_slow_cps True
                                if quest_spiritrock == 1 and galerocks_photios_quest_spiritrock_question_doubt and not cephasgaiane_about_spiritrock:
                                    $ options_cephasgaiane += 1
                                    textbutton 'It will be difficult to explain this, but I try to learn from them what them think about {color=#f6d6bd}Phoibe’s{/color} situation.' action [Jump("cephasgaiane_about_spiritrock01")] style "nvl_button" text_slow_cps True
                                if galerocks_fulvia_about_shortcut2 and not cephasgaiane_about_orchard:
                                    $ options_cephasgaiane += 1
                                    textbutton '“I wonder... Is it true that you still maintain the old orchard at the heart of the woods?”' action [Jump("cephasgaiane_about_orchard01")] style "nvl_button" text_slow_cps True
                                if ruinedvillage_firsttime and not ruinedvillage_truth and not cephasgaiane_about_steephouse1:
                                    $ options_cephasgaiane += 1
                                    textbutton '“I’m trying to learn more about the ruins of the village at the southern road.”' action [Jump("cephasgaiane_about_steephouse01")] style "nvl_button" text_slow_cps True
                                if cephasgaiane_about_steephouse1 and not cephasgaiane_about_steephouse2 and quest_ruins_choice == "thais_defeated":
                                    $ options_cephasgaiane += 1
                                    textbutton '“I confronted {color=#f6d6bd}Thais{/color} about {color=#f6d6bd}Steep House{/color}. Her village will soon be under a new leadership.”' action [Jump("cephasgaiane_about_steephouse201")] style "nvl_button" text_slow_cps True
                                if (asterion_highisland_knowsabout and not cephasgaiane_about_highisland and options_cephasgaiane_highisland) or (asterion_highisland_knowsabout and not cephasgaiane_about_highisland and options_cephasgaiane_highisland):
                                    $ options_cephasgaiane += 1
                                    textbutton '“Can we talk about {color=#f6d6bd}High Island{/color}?”' action [Jump("cephasgaiane_about_highisland01")] style "nvl_button" text_slow_cps True
                                if cephasgaiane_about_highisland and options_cephasgaiane_highisland:
                                    $ options_cephasgaiane += 1
                                    textbutton '“I have more questions about {color=#f6d6bd}High Island{/color}.”' action [Jump("cephasgaiane_about_highisland02")] style "nvl_button" text_slow_cps True
                                if not options_cephasgaiane:
                                    textbutton 'I have no more questions.' action NullAction() style "nvl_button2" text_slow_cps True
                                textbutton 'I stand up. “Farewell.”' action [Jump("greenmountaintribeleavingthecave01")] style "nvl_button" text_slow_cps True

                            elif questionpreset == "cephasgaiane2":
                                if quest_asterion == 1 and asterion_highisland_knowsabout and not asterion_found and highisland_howtoreach_pcknows and not cephasgaiane_about_highisland_question1:
                                    textbutton '“Would it matter to you if I were to land there?”' action [SetVariable("questionpreset", 0), Jump("cephasgaiane_about_highisland_question101alt")] style "nvl_button" text_slow_cps True
                                elif quest_asterion == 1 and asterion_highisland_knowsabout and not asterion_found and highisland_howtoreach_pcknows and cephasgaiane_about_highisland_question1 == 1 and (greenmountaintribe_reputation+(appearance_charisma/2)) >= greenmountaintribe_asterion_permission_threshold:
                                    textbutton '“I would still appreciate your permission to search the island.”' action [SetVariable("questionpreset", 0), Jump("cephasgaiane_about_highisland_question102alt")] style "nvl_button" text_slow_cps True
                                elif quest_asterion == 1 and asterion_highisland_knowsabout and not asterion_found and highisland_howtoreach_pcknows and cephasgaiane_about_highisland_question1 == 1 and (greenmountaintribe_reputation+(appearance_charisma/2)) < greenmountaintribe_asterion_permission_threshold:
                                    textbutton 'He doesn’t trust me enough to tell me how to reach the island.' action NullAction() style "nvl_button2" text_slow_cps True
                                    if (greenmountaintribe_reputation+(appearance_charisma/2)) >= (greenmountaintribe_asterion_permission_threshold-3) and cephasgaiane_shop:
                                        if item_axe02alt or item_axehead or item_axeset or item_axe03 or item_cidercask or item_ironingot or item_sealskin or item_spices or item_beholderroot:
                                            if cephasgaiane_shop_dragonhorn:
                                                textbutton '“I’d like to offer you a gift, as a sign of my good will.”' action [Jump("cephasgaiane_shop_freegift01")] style "nvl_button" text_slow_cps True
                                            else:
                                                textbutton 'Maybe I should earn their trust by starting with a simple barter.' action NullAction() style "nvl_button2" text_slow_cps True
                                        else:
                                            textbutton 'I could offer them a gift to show my good will, but I’ve nothing they’d be interested in.' action NullAction() style "nvl_button2" text_slow_cps True
                                    elif (greenmountaintribe_reputation+(appearance_charisma/2)) < (greenmountaintribe_asterion_permission_threshold-3) and cephasgaiane_shop:
                                        textbutton 'I could offer them a gift to show my good will, but I doubt they’ll accept it.' action NullAction() style "nvl_button2" text_slow_cps True
                                if quest_asterion == 1 and asterion_highisland_knowsabout and not asterion_found and not highisland_howtoreach_pcknows and not cephasgaiane_about_highisland_question1:
                                    textbutton '“How can I get there?”' action [SetVariable("questionpreset", 0), Jump("cephasgaiane_about_highisland_question101")] style "nvl_button" text_slow_cps True
                                elif quest_asterion == 1 and asterion_highisland_knowsabout and not asterion_found and not highisland_howtoreach_pcknows and cephasgaiane_about_highisland_question1 == 1 and (greenmountaintribe_reputation+(appearance_charisma/2)) >= greenmountaintribe_asterion_permission_threshold:
                                    textbutton '“I {i}need{/i} to reach that place.”' action [SetVariable("questionpreset", 0), Jump("cephasgaiane_about_highisland_question102")] style "nvl_button" text_slow_cps True
                                elif quest_asterion == 1 and asterion_highisland_knowsabout and not asterion_found and not highisland_howtoreach_pcknows and cephasgaiane_about_highisland_question1 == 1 and (greenmountaintribe_reputation+(appearance_charisma/2)) < greenmountaintribe_asterion_permission_threshold:
                                    textbutton 'He doesn’t trust me enough to tell me how to reach the island.' action NullAction() style "nvl_button2" text_slow_cps True
                                    if (greenmountaintribe_reputation+(appearance_charisma/2)) >= (greenmountaintribe_asterion_permission_threshold-3) and cephasgaiane_shop:
                                        if item_axe02alt or item_axehead or item_axeset or item_axe03 or item_cidercask or item_ironingot or item_sealskin or item_spices or item_beholderroot:
                                            textbutton '“I’m willing to offer you a gift, as a sign of my good will.”' action [Jump("cephasgaiane_shop_freegift01")] style "nvl_button" text_slow_cps True
                                        else:
                                            textbutton 'I could offer them a gift to show my good will, but I’ve nothing they’d be interested in.' action NullAction() style "nvl_button2" text_slow_cps True
                                    elif (greenmountaintribe_reputation+(appearance_charisma/2)) < (greenmountaintribe_asterion_permission_threshold-3) and cephasgaiane_shop:
                                        textbutton 'I could offer them a gift to show my good will, but I doubt they’ll accept it.' action NullAction() style "nvl_button2" text_slow_cps True
                                if cephasgaiane_about_highisland_question1 and not cephasgaiane_about_highisland_question2:
                                    textbutton '“Why don’t you want anyone to land there?”' action [Jump("cephasgaiane_about_highisland_question201")] style "nvl_button" text_slow_cps True
                                if not cephasgaiane_about_highisland_question3:
                                    textbutton '“What’s the story of the island?”' action [Jump("cephasgaiane_about_highisland_question301")] style "nvl_button" text_slow_cps True
                                if cephasgaiane_about_highisland_question3 and not cephasgaiane_about_highisland_question4:
                                    textbutton '“Why won’t your tribe try to reclaim the island?”' action [Jump("cephasgaiane_about_highisland_question401")] style "nvl_button" text_slow_cps True
                                if not asterion_found and not cephasgaiane_about_highisland_question6:
                                    textbutton '“Is the island dangerous?”' action [Jump("cephasgaiane_about_highisland_question601")] style "nvl_button" text_slow_cps True
                                if quest_asterion == 1 and cephasgaiane_about_highisland_question1 == 2 and not asterion_found and not cephasgaiane_about_highisland_question7:
                                    textbutton '“Is there something that could help me explore the island?”' action [Jump("cephasgaiane_about_highisland_question701")] style "nvl_button" text_slow_cps True
                                if quest_asterion == 1 and quest_sleepinggiant < 2 and not asterion_found and not giantstatue_pray_map_learned and cephasgaiane_about_highisland_question7 and not cephasgaiane_about_highisland_question8:
                                    textbutton '“I’ve time now. Teach me what I need to know about this statue.”' action [Jump("cephasgaiane_about_highisland_question801")] style "nvl_button" text_slow_cps True
                                if quest_asterion == 1 and quest_sleepinggiant < 2 and not asterion_found and giantstatue_pray_map_learned and cephasgaiane_about_highisland_question7 and not cephasgaiane_about_highisland_question8:
                                    textbutton '“Actually, I was already able to awake the statue. But I’m not sure how to understand it.”' action [Jump("cephasgaiane_about_highisland_question801alt")] style "nvl_button" text_slow_cps True
                                textbutton '“That’s everything I wanted to ask about.”' action [Jump("greenmountaintribechiefafterinteraction01")] style "nvl_button" text_slow_cps True

                            elif questionpreset == "glaucia1":
                                if quest_galerockssupport == 1 and not glaucia_about_vote:
                                    $ options_glaucia += 1
                                    textbutton '“The council of {color=#f6d6bd}Gale Rocks{/color} is planning to hold a meeting about cutting ties with your band.”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_vote01")] style "nvl_button" text_slow_cps True
                                if quest_galerockssupport > 1 and glaucia_about_vote and not glaucia_about_galerocksdecision:
                                    $ options_glaucia += 1
                                    textbutton '“The council has come to a decision.”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_galerocksdecision01")] style "nvl_button" text_slow_cps True
                                if quest_galerockssupport > 1 and not glaucia_about_vote and not glaucia_about_galerocksdecision:
                                    $ options_glaucia += 1
                                    textbutton '“The council of {color=#f6d6bd}Gale Rocks{/color} held a meeting about cutting ties with your band.”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_galerocksdecision01alt")] style "nvl_button" text_slow_cps True
                                if (greenmountaintribe_firsttime and not cephasgaiane_shop_dragonhorn and not greenmountaintribe_banned) or (greenmountaintribe_firsttime and not cephasgaiane_about_highisland_permission and not greenmountaintribe_banned):
                                    if quest_lostmerchants and glaucia_about_lostmerchants_trail and not glaucia_spices_available and not item_spices:
                                        if greenmountaintribe_about_wanteditems or quest_reachthepaganvillage_description02:
                                            $ options_glaucia += 1
                                            textbutton '{image=cointest} “Do you still have the spices you {i}took{/i} from the merchants? I need some to get on the good side of {color=#f6d6bd}The Tribe of The Green Mountain{/color}.”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglauciaglaucia_spices_available01")] style "nvl_button" text_slow_cps True
                                    elif glaucia_spices_available and not glaucia_spices_bought:
                                        $ options_glaucia += 1
                                        textbutton '{image=cointest} “About those spices...”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglauciaglaucia_spices_available02")] style "nvl_button" text_slow_cps True
                                if quest_intelforpeltnorth and not glaucia_about_iason1:
                                    $ options_glaucia += 1
                                    textbutton '“You made {color=#f6d6bd}[iason_name]{/color} quite worried with your recent moves.”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_iason101")] style "nvl_button" text_slow_cps True
                                if glaucia_about_iason1 and description_glaucia01 and not glaucia_about_iason2:
                                    $ options_glaucia += 1
                                    textbutton '“You speak of {color=#f6d6bd}Iason{/color} as if you work together, but he didn’t agree to let your band move into {color=#f6d6bd}Pelt{/color}, am I wrong?”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_iason201")] style "nvl_button" text_slow_cps True
                                if not glaucia_about_herself:
                                    $ options_glaucia += 1
                                    textbutton '“I’d like to learn more about you.”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_herself01")] style "nvl_button" text_slow_cps True
                                elif glaucia_about_herself == 1 and (glaucia_friendship+appearance_charisma) >= 4:
                                    $ options_glaucia += 1
                                    textbutton '“Tell me about you.”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_herself02")] style "nvl_button" text_slow_cps True
                                elif glaucia_about_herself == 1 and (glaucia_friendship+appearance_charisma) < 4:
                                    textbutton 'She doesn’t trust me enough to tattle about herself.' action NullAction() style "nvl_button2" text_slow_cps True
                                if description_glaucia08 and glaucia_about_herself and not glaucia_about_pasttragedy:
                                    if not glaucia_about_steephouse2 and not glaucia_about_vendetta_whitemarshes:
                                        $ options_glaucia += 1
                                        textbutton '“{color=#f6d6bd}Foggy{/color} mentioned some dark days pushed you into becoming a bandit.”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_pasttragedy01")] style "nvl_button" text_slow_cps True
                                    else:
                                        $ options_glaucia += 1
                                        textbutton '“{color=#f6d6bd}Foggy{/color} mentioned that the other members of your group were also pushed into becoming bandit by some dark events.”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_pasttragedy01alt")] style "nvl_button" text_slow_cps True
                                if glaucia_about_herself == 2 and not glaucia_about_shortcut:
                                    $ options_glaucia += 1
                                    textbutton '“After spending a few days on these roads, I’m surprised your band didn’t get mauled to death yet.”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_shortcut01")] style "nvl_button" text_slow_cps True
                                if glaucia_about_herself == 2 and glaucia_about_shortcut and not glaucia_about_protectingthewoods:
                                    $ options_glaucia += 1
                                    textbutton '“Why don’t you try to secure these roads?”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_protectingthewoods01")] style "nvl_button" text_slow_cps True
                                if glaucia_about_herself == 2 and not glaucia_about_attackingpeople:
                                    $ options_glaucia += 1
                                    textbutton '“Who are you even robbing on these roads?”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_attackingpeople01")] style "nvl_button" text_slow_cps True
                                if glaucia_about_herself == 2 and tulia_about_hersquad and glaucia_about_attackingpeople and not glaucia_about_pastbandits:
                                    $ options_glaucia += 1
                                    textbutton '“You’re lucky that the soldiers from {color=#f6d6bd}Hovlavan{/color} took care of the band dwelling in {color=#f6d6bd}Hag Hills{/color}.”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_pastbandits01")] style "nvl_button" text_slow_cps True
                                if not glaucia_about_runaway:
                                    $ options_glaucia += 1
                                    textbutton '“Do you need any assistance?”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_runaway01")] style "nvl_button" text_slow_cps True
                                elif glaucia_about_runaway and quest_runaway == 1:
                                    $ options_glaucia += 1
                                    textbutton '“About the man you’re looking for...”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_runaway03")] style "nvl_button" text_slow_cps True
                                if quest_runaway == 2 and not glaucia_about_spyonnecromancers:
                                    $ options_glaucia += 1
                                    textbutton '“What else do you want me to do?”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_spyonnecromancers01")] style "nvl_button" text_slow_cps True
                                elif glaucia_about_spyonnecromancers and quest_spyonwhitemarshes == 1:
                                    $ options_glaucia += 1
                                    textbutton '“About the spying you wanted me to do...”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_spyonnecromancers02")] style "nvl_button" text_slow_cps True
                                if quest_orentius == 1 and quest_orentius_thais_description00 and not orentius_met and not whitemarshes_attacked and not quest_orentius_thais_description00betrayal and not thais_defeated and not quest_orentius_thais_description10:
                                    if (quest_spyonwhitemarshes and not quest_orentius_thais_description03a07 and quest_orentius_thais_description03 and not glaucia_about_orentius) or (glaucia_about_vendetta_whitemarshes and not quest_orentius_thais_description03a07 and quest_orentius_thais_description03 and not glaucia_about_orentius):
                                        $ options_glaucia += 1
                                        textbutton '“{color=#f6d6bd}Thais{/color} wants to deal with {color=#f6d6bd}Orentius{/color} and could use your band’s help.”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_orentius01")] style "nvl_button" text_slow_cps True
                                if oldpagos_plague_known and not glaucia_about_plague:
                                    $ options_glaucia += 1
                                    textbutton '“You may want to stay away from {color=#f6d6bd}Old Págos{/color}. It’s been struggling with a plague.”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_plague01")] style "nvl_button" text_slow_cps True
                                if not glaucia_about_vendetta_whitemarshes and not quest_orentius_thais_description03a07 and not glaucia_about_undead and not whitemarshes_nomoreundead:
                                    $ options_glaucia += 1
                                    textbutton '“Can you tell me anything about the undead in the North?”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_undead01")] style "nvl_button" text_slow_cps True
                                if not quest_recruitahunter_spokento_glaucia and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed:
                                    $ options_glaucia += 1
                                    textbutton '“Have you ever met {color=#f6d6bd}Cassia{/color} from {color=#f6d6bd}Gale Rocks{/color}?”' action [SetVariable("questionpreset", 0), Jump("glaucia_about_recruitahunter01")] style "nvl_button" text_slow_cps True
                                if fallentree_firsttime and not glaucia_about_lostmerchants_trail and not glaucia_about_arrow and not glaucia_about_abandonedwagon and not quest_lostmerchants_description01:
                                    $ options_glaucia += 1
                                    textbutton '“I found an abandoned cart on the eastern trail...”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_abandonedwagon01")] style "nvl_button" text_slow_cps True
                                if glaucia_about_abandonedwagon and shortcut_cairn_tracks and not glaucia_about_lostmerchants_trail and not quest_lostmerchants_description01:
                                    $ options_glaucia += 1
                                    textbutton '“I followed the trail leading from the abandoned cart. And here I am.”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_lostmerchants_trail01")] style "nvl_button" text_slow_cps True
                                if glaucia_about_abandonedwagon and fallentree_investigated_opinion02 == "was attacked by highwaymen" and galerocks_florus_about_arrow and item_arrow and not glaucia_about_arrow and not quest_lostmerchants_description01:
                                    $ options_glaucia += 1
                                    textbutton '“You dropped this arrow at the abandoned cart.”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_arrow01")] style "nvl_button" text_slow_cps True
                                if not glaucia_about_lostmerchants_trail and not glaucia_about_lostmerchants and not quest_lostmerchants_description01 and quest_lostmerchants:
                                    $ options_glaucia += 1
                                    textbutton '“I’ve heard in {color=#f6d6bd}Gale Rocks{/color} that the villagers are awaiting some spice merchants.”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_lostmerchants01")] style "nvl_button" text_slow_cps True
                                if galerocks_rufina_about_necklace and item_oceannecklace and not glaucia_about_necklace:
                                    $ options_glaucia += 1
                                    textbutton 'I reach for the pouch with a necklace. “I think this belongs to you.”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_necklace01")] style "nvl_button" text_slow_cps True
                                if quest_intelforpeltnorth_description04a or quest_orentius_thais_description03a07 or glaucia_about_spyonnecromancers or quest_intelforpeltnorth_description10 or shortcut_darkforest_bandit_confronted:
                                    if not whitemarshes_destroyed and not whitemarshes_attacked and whitemarshes_firsttime:
                                        if not glaucia_about_vendetta_whitemarshes and not whitemarshes_nomoreundead and not glaucia_about_vendetta_whitemarshes_gray:
                                            $ options_glaucia += 1
                                            textbutton '“Why do you target {color=#f6d6bd}White Marshes{/color}?”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_vendetta_whitemarshes01")] style "nvl_button" text_slow_cps True
                                        elif not glaucia_about_vendetta_whitemarshes and whitemarshes_nomoreundead and not glaucia_about_vendetta_whitemarshes_gray:
                                            $ options_glaucia += 1
                                            textbutton '“Why did you target {color=#f6d6bd}White Marshes{/color}?”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_vendetta_whitemarshes01alt")] style "nvl_button" text_slow_cps True
                                        elif glaucia_about_vendetta_whitemarshes_gray and not glaucia_about_vendetta_whitemarshes and (glaucia_friendship+appearance_charisma) >= glaucia_about_vendetta_whitemarshes_friendshiplevel:
                                            $ options_glaucia += 1
                                            textbutton '“What did {color=#f6d6bd}White Marshes{/color} do to you?”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_vendetta_whitemarshes02")] style "nvl_button" text_slow_cps True
                                        elif glaucia_about_vendetta_whitemarshes_gray and not glaucia_about_vendetta_whitemarshes and (glaucia_friendship+appearance_charisma) < glaucia_about_vendetta_whitemarshes_friendshiplevel:
                                            textbutton 'She’s not willing to talk to me about White Marshes yet.' action NullAction() style "nvl_button2" text_slow_cps True
                                if ruinedvillage_confront_can and not ruinedvillage_truth and not glaucia_about_steephouse2 and not glaucia_about_steephouse1 and not glaucia_about_vendetta_whitemarshes:
                                    $ options_glaucia += 1
                                    textbutton '“What can you tell me about the ruins at the southern road?”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_steephouse101")] style "nvl_button" text_slow_cps True
                                if (ruinedvillage_confront_can and description_glaucia12 and ruinedvillage_name == "Steep House") or (ruinedvillage_confront_can and quest_ruins_10yclue11 and ruinedvillage_name == "Steep House") or (ruinedvillage_confront_can and glaucia_about_vendetta_whitemarshes and ruinedvillage_name == "Steep House"):
                                    if not glaucia_about_steephouse2 and not glaucia_about_steephouse2_gray:
                                        $ options_glaucia += 1
                                        textbutton '“You were there when {color=#f6d6bd}Steep House{/color} fell, weren’t you?”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_steephouse201")] style "nvl_button" text_slow_cps True
                                    elif glaucia_about_steephouse2_gray and not glaucia_about_steephouse2 and (glaucia_friendship+appearance_charisma) >= glaucia_about_steephouse2_friendshiplevel:
                                        $ options_glaucia += 1
                                        textbutton '“Tell me, {color=#f6d6bd}Glaucia{/color}. What did you see in {color=#f6d6bd}Steep House{/color}?”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_steephouse202")] style "nvl_button" text_slow_cps True
                                    elif glaucia_about_steephouse2_gray and not glaucia_about_steephouse2 and (glaucia_friendship+appearance_charisma) < glaucia_about_steephouse2_friendshiplevel:
                                        textbutton 'She doesn’t want to talk with me about Steep House.' action NullAction() style "nvl_button2" text_slow_cps True
                                if glaucia_about_steephouse2 and glaucia_about_vendetta_whitemarshes and not glaucia_about_steephouse3:
                                    $ options_glaucia += 1
                                    textbutton '“So now you aim your rage at {color=#f6d6bd}White Marshes{/color}... Is {color=#f6d6bd}Howler’s Dell{/color} next?”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglauciaglaucia_about_steephouse301")] style "nvl_button" text_slow_cps True
                                if dolmen_underground_firsttime and not glaucia_about_dolmen_underground_firsttime and not glaucia_about_dolmen_underground_firsttime_refused and glaucia_about_herself:
                                    $ options_glaucia += 1
                                    textbutton 'I consider telling her about the secret trapdoor from the dolmen.' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_dolmen_underground_firsttime01")] style "nvl_button" text_slow_cps True
                                if quest_asterion == 1 and not asterion_found and not glaucia_about_asterion1 and not glaucia_about_asterion3:
                                    $ options_glaucia += 1
                                    textbutton '“I’m trying to find out what happened to {color=#f6d6bd}Asterion{/color}.”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_asterion101")] style "nvl_button" text_slow_cps True
                                if glaucia_about_asterion1 and quest_asterion == 1 and not asterion_found and description_glaucia11 and not glaucia_about_asterion2 and not glaucia_about_asterion3:
                                    $ options_glaucia += 1
                                    textbutton '“There are... {i}some{/i} who are convinced that you had something to do with {color=#f6d6bd}Asterion’s{/color} disappearance.”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_asterion201")] style "nvl_button" text_slow_cps True
                                if glaucia_about_asterion1 and not asterion_found and not glaucia_about_asterion3 and quest_runaway != 3 and quest_spyonwhitemarshes != 3 and quest_glauciasupport != 3:
                                    if quest_spyonwhitemarshes == 2 and quest_glauciasupport == 2:
                                        $ options_glaucia += 1
                                        textbutton '“I did enough for you already. Help me find {color=#f6d6bd}Asterion{/color}.”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_asterion301")] style "nvl_button" text_slow_cps True
                                    else:
                                        textbutton 'She wants me to do more for her before she helps me find Asterion.' action NullAction() style "nvl_button2" text_slow_cps True
                                if not asterion_found and glaucia_about_asterion3:
                                    if not glaucia_about_asterion3_bonusquestion1 or not glaucia_about_asterion3_bonusquestion2 or not highisland_howtoreach_pcknows or not glaucia_about_asterion3_bonusquestion4 or not glaucia_about_asterion3_bonusquestion5:
                                        $ options_glaucia += 1
                                        textbutton '“I have more questions about {color=#f6d6bd}Asterion’s{/color} journey.”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_asterion302")] style "nvl_button" text_slow_cps True
                                if glaucia_about_asterion2 and asterion_found and description_glaucia11 and not glaucia_about_asterion4:
                                    $ options_glaucia += 1
                                    textbutton '“{color=#f6d6bd}Asterion{/color} is dead.”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_asterion401")] style "nvl_button" text_slow_cps True
                                if (quest_asterion == 1 and asterion_highisland_knowsabout and not asterion_found and not glaucia_about_asterion3 and not glaucia_about_highhisland) or (quest_asterion == 1 and description_highisland00 and not asterion_found and not glaucia_about_asterion3 and not glaucia_about_highhisland):
                                    $ options_glaucia += 1
                                    textbutton '“Have you heard anything about {color=#f6d6bd}High Island{/color}?”' action [SetVariable("questionpreset", 0), Jump("banditshideoutglaucia_about_highhisland01")] style "nvl_button" text_slow_cps True
                                textbutton '“I should go.”' action [SetVariable("questionpreset", 0), Jump("banditshideoutaftertalkingtoglaucia01")] style "nvl_button" text_slow_cps True

                            elif questionpreset == "bogentrance":
                                if not bogentrance_dialogue_about_themselves:
                                    textbutton '“Are you from around here?”' action [SetVariable("questionpreset", 0), Jump("bogentrance_dialogue_about_themselves01")] style "nvl_button" text_slow_cps True
                                if bogentrance_dialogue_about_themselves and not bogentrance_dialogue_about_trade:
                                    textbutton '“I’m looking for a place to trade.”' action [SetVariable("questionpreset", 0), Jump("bogentrance_dialogue_about_trade01")] style "nvl_button" text_slow_cps True
                                if quest_missinghunters == 1 and not bogentrance_dialogue_about_missinghunters:
                                    textbutton '“I seek a few missing hunters from {color=#f6d6bd}Creeks{/color}. Have you seen any of them?”' action [SetVariable("questionpreset", 0), Jump("bogentrance_dialogue_about_missinghunters01")] style "nvl_button" text_slow_cps True
                                if bogentrance_dialogue_about_themselves and not bogentrance_dialogue_about_findingwhitemarshes:
                                    textbutton '“How can I reach {color=#f6d6bd}White Marshes{/color}?”' action [SetVariable("questionpreset", 0), Jump("bogentrance_dialogue_about_findingwhitemarshes01")] style "nvl_button" text_slow_cps True
                                if bogentrance_dialogue_about_area:
                                    textbutton '“What can you tell me about this area?”' action [SetVariable("questionpreset", 0), Jump("bogentrance_dialogue_about_area01")] style "nvl_button" text_slow_cps True
                                if bogentrance_dialogue_about_themselves and not bogentrance_dialogue_about_whitemarshes:
                                    textbutton '“Tell me about your village.”' action [SetVariable("questionpreset", 0), Jump("bogentrance_dialogue_about_whitemarshes01")] style "nvl_button" text_slow_cps True
                                if not bogentrance_dialogue_about_cart:
                                    textbutton '“Is this your cart?”' action [SetVariable("questionpreset", 0), Jump("bogentrance_dialogue_about_cart01")] style "nvl_button" text_slow_cps True
                                if not bogentrance_dialogue_about_hoodedperson:
                                    textbutton 'I look at the hooded person. “What’s up with this one?”' action [SetVariable("questionpreset", 0), Jump("bogentrance_dialogue_about_hoodedperson01")] style "nvl_button" text_slow_cps True
                                if (bogentrance_dialogue_friendship+appearance_charisma) >= 2 and bogentrance_dialogue_about_cart:
                                    textbutton '“Well, better to carry on. Good luck with the forest.”' action [SetVariable("questionpreset", 0), Jump("bogentranceleavingfriendly01")] style "nvl_button" text_slow_cps True
                                elif (bogentrance_dialogue_friendship+appearance_charisma) > 0:
                                    textbutton 'I nod to them. “Farewell, then.”' action [SetVariable("questionpreset", 0), Jump("bogentranceleavingneutral01")] style "nvl_button" text_slow_cps True
                                else:
                                    textbutton 'I gesture for them to clear the way. “I’m leaving.”' action [SetVariable("questionpreset", 0), Jump("bogentranceleavingangry01")] style "nvl_button" text_slow_cps True

                            elif questionpreset == "thyrsus1":
                                if thyrsus_about_himself1 and thyrsus_about_asterion_question5 and quest_asterion == 1 and not asterion_found and not quest_galerockssupport == 2 and not quest_galerockssupport == 3 and not whitemarshes_nomoreundead and not orentius_spared and not thyrsus_orentius_debt_option:
                                    $ options_thyrsus += 1
                                    textbutton '“Let’s say {i}I{/i} were to help your people with the bandits and got rid of the undead. Would you return the favor?”' action [SetVariable("questionpreset", 0), Jump("thyrsusabouttravelingwithpc01")] style "nvl_button" text_slow_cps True
                                elif thyrsus_about_himself1 and thyrsus_about_asterion_question5 and quest_asterion == 1 and not asterion_found and quest_galerockssupport == 2 and not whitemarshes_nomoreundead and not orentius_spared and not thyrsus_orentius_debt_option:
                                    $ options_thyrsus += 1
                                    textbutton '“I’ve already weakened {color=#f6d6bd}Glaucia{/color} quite a bit. Let’s say I were to get rid of the undead. Would you return the favor?”' action [SetVariable("questionpreset", 0), Jump("thyrsusabouttravelingwithpc01alt1")] style "nvl_button" text_slow_cps True
                                elif thyrsus_about_himself1 and thyrsus_about_asterion_question5 and quest_asterion == 1 and not asterion_found and not quest_galerockssupport == 2 and not quest_galerockssupport == 3 and whitemarshes_nomoreundead and not thyrsus_orentius_debt_option:
                                    $ options_thyrsus += 1
                                    textbutton '“I already helped you with the undead. Let’s say I were to help your people with the bandits - would you return the favor?”' action [SetVariable("questionpreset", 0), Jump("thyrsusabouttravelingwithpc01alt2")] style "nvl_button" text_slow_cps True
                                elif thyrsus_about_himself1 and thyrsus_about_asterion_question5 and quest_asterion == 1 and not asterion_found and quest_galerockssupport == 2 and whitemarshes_nomoreundead and not thyrsus_orentius_debt_option:
                                    $ options_thyrsus += 1
                                    textbutton '“I’ve already weakened {color=#f6d6bd}Glaucia{/color} quite a bit, and there are no more undead. Will you return the favor?”' action [SetVariable("questionpreset", 0), Jump("thyrsusabouttravelingwithpc02alt1")] style "nvl_button" text_slow_cps True
                                elif quest_asterion == 1 and not asterion_found and thyrsus_orentius_debt_option and not thyrsus_orentius_debt_achieved:
                                    if quest_galerockssupport == 2 and whitemarshes_nomoreundead:
                                        $ options_thyrsus += 1
                                        textbutton '“You owe me.”' action [SetVariable("questionpreset", 0), Jump("thyrsusabouttravelingwithpc02")] style "nvl_button" text_slow_cps True
                                    elif whitemarshes_nomoreundead and quest_thyrsusgift == 2:
                                        $ options_thyrsus += 1
                                        textbutton '“I helped you with the undead and I brought you your possessions. This should be enough to earn your help.”' action [SetVariable("questionpreset", 0), Jump("thyrsusabouttravelingwithpc02alt3")] style "nvl_button" text_slow_cps True
                                    elif not quest_galerockssupport == 2 and not whitemarshes_nomoreundead:
                                        textbutton 'He won’t be in my debt unless I weaken the bandits and get rid of the undead in the village.' action NullAction() style "nvl_button2" text_slow_cps True
                                    elif not quest_galerockssupport == 2:
                                        textbutton 'He won’t be in my debt unless I weaken the bandits.' action NullAction() style "nvl_button2" text_slow_cps True
                                    elif not whitemarshes_nomoreundead:
                                        textbutton 'He won’t be in my debt unless I get rid of the undead in the village.' action NullAction() style "nvl_button2" text_slow_cps True
                                if not asterion_found and quest_asterion == 1 and quest_gatheracrew == 1 and thyrsus_orentius_debt_achieved and not thyrsus_about_highisland_recruitment:
                                    $ options_thyrsus += 1
                                    textbutton '“I’m heading for {color=#f6d6bd}High Island{/color}. I want to take you with me, just for a single night.”' action [SetVariable("questionpreset", 0), Jump("thyrsus_about_highisland_recruitment01")] style "nvl_button" text_slow_cps True
                                if thyrsus_about_himself1 and vines_open_day != day and not vines_firsttime and not thyrsus_whitemarshes_entrance:
                                    $ options_thyrsus += 1
                                    textbutton '“Is this the way to {color=#f6d6bd}White Marshes{/color}?”' action [SetVariable("questionpreset", 0), Jump("thyrsusenteringwhitemarshes01")] style "nvl_button" text_slow_cps True
                                if vines_open_day != day and vines_firsttime and not thyrsus_whitemarshes_entrance:
                                    $ options_thyrsus += 1
                                    textbutton '“Some plants are blocking the way to {color=#f6d6bd}White Marshes{/color}. How about the road south from here?”' action [SetVariable("questionpreset", 0), Jump("thyrsusenteringwhitemarshes01alt")] style "nvl_button" text_slow_cps True
                                if vines_open_day != day and not vines_perma_open and not vines_perma_closed and thyrsus_whitemarshes_entrance:
                                    $ options_thyrsus += 1
                                    textbutton '“I need you to open the path to {color=#f6d6bd}White Marshes{/color}.”' action [SetVariable("questionpreset", 0), Jump("thyrsusenteringwhitemarshes02")] style "nvl_button" text_slow_cps True
                                if quest_readtheletter == 1 and item_letterwhitemarshes_read and not thyrsus_about_readtheletter:
                                    $ options_thyrsus += 1
                                    textbutton 'I tell him about {color=#f6d6bd}Valens’{/color} situation.' action [SetVariable("questionpreset", 0), Jump("thyrsus_about_readtheletter01")] style "nvl_button" text_slow_cps True
                                if not thyrsus_about_himself1:
                                    $ options_thyrsus += 1
                                    textbutton '“Do you live here all by yourself?”' action [SetVariable("questionpreset", 0), Jump("thyrsus_about_himself101")] style "nvl_button" text_slow_cps True
                                if thyrsus_about_himself1 and whitemarshes_opposition and not thyrsus_about_himself3:
                                    $ options_thyrsus += 1
                                    textbutton 'I raise my chin. “Did you {i}choose{/i} to move to this field, or were you forced to do so?”' action [SetVariable("questionpreset", 0), Jump("thyrsus_about_himself301")] style "nvl_button" text_slow_cps True
                                if not item_snakebait_truth and pc_class != "scholar":
                                    if item_snakebait or quest_eudociaflower == 1:
                                        if thyrsus_about_himself1 and not thyrsus_about_snakebait:
                                            $ options_thyrsus += 1
                                            textbutton '“What can you tell me about snake bait?”' action [SetVariable("questionpreset", 0), Jump("thyrsus_about_snakebait01")] style "nvl_button" text_slow_cps True
                                if thyrsus_about_himself1 and not thyrsus_shop:
                                    $ options_thyrsus += 1
                                    textbutton '{image=cointest} “Do you have anything to sell... {i}warlock{/i}?”' action [SetVariable("questionpreset", 0), Jump("thyrsus_shop01")] style "nvl_button" text_slow_cps True
                                $ thyrsus_estimate_wares = 0
                                if not thyrsus_shop_bonehook and not item_bonehook:
                                    $ thyrsus_estimate_wares += 1
                                if not thyrsus_shop_witheringdust and not item_witheringdust:
                                    $ thyrsus_estimate_wares += 1
                                if not thyrsus_shop_stingointment and not item_stingointment:
                                    $ thyrsus_estimate_wares += 1
                                if not thyrsus_shop_bugrepellent and not item_bugrepellent and not watchtower_tower_bugs_cleared:
                                    $ thyrsus_estimate_wares += 1
                                if thyrsus_shop and thyrsus_estimate_wares:
                                    textbutton '{image=cointest} “What can you sell me?”' action [SetVariable("questionpreset", 0), Jump("thyrsus_shop02")] style "nvl_button" text_slow_cps True
                                if thyrsus_shop == 1 and pc_class == "scholar":
                                    textbutton '{image=cointest} “Have you got any ingredients I could use?”' action [SetVariable("questionpreset", 0), Jump("thyrsus_shop03")] style "nvl_button" text_slow_cps True
                                elif thyrsus_shop == 2 and pc_class == "scholar":
                                    $ options_thyrsus += 1
                                    textbutton '{image=cointest} “Show me your alchemical ingredients.”' action [SetVariable("questionpreset", 0), Jump("thyrsus_shop04")] style "nvl_button" text_slow_cps True
                                if thyrsus_shop == 2 and pc_class == "scholar" and not thyrsus_shop_alchemytable_asked:
                                    $ options_thyrsus += 1
                                    textbutton '“Can I use your alchemy table?”' action [SetVariable("questionpreset", 0), Jump("thyrsus_alchemytable01")] style "nvl_button" text_slow_cps True
                                if thyrsus_about_himself1 and not thyrsus_about_himself2:
                                    $ options_thyrsus += 1
                                    textbutton '“But how do you avoid wild beasts?”' action [SetVariable("questionpreset", 0), Jump("thyrsus_about_himself201")] style "nvl_button" text_slow_cps True
                                if thyrsus_orentius_helped and whitemarshes_nomoreundead and not thyrsus_orentius_nomoreundead_react and not thyrsus_about_returninghome:
                                    $ options_thyrsus += 1
                                    textbutton '“Now that your tribe was shaken by the recent events, why don’t you return to the village?”' action [SetVariable("questionpreset", 0), Jump("thyrsus_about_returninghome01")] style "nvl_button" text_slow_cps True
                                if quest_spiritrock == 1 and galerocks_photios_quest_spiritrock_question_doubt and thyrsus_about_himself1 and not thyrsus_about_spiritrock:
                                    $ options_thyrsus += 1
                                    textbutton '“There’s a man living in {color=#f6d6bd}Gale Rocks{/color} who tries to {i}heal{/i} his spell-less daughter...”' action [SetVariable("questionpreset", 0), Jump("thyrsusaboutspiritrock01")] style "nvl_button" text_slow_cps True
                                if thyrsus_about_himself1 and description_thyrsus04 and not thyrsus_about_druids1:
                                    $ options_thyrsus += 1
                                    textbutton '“You were training with the druids?”' action [SetVariable("questionpreset", 0), Jump("thyrsus_about_druids101")] style "nvl_button" text_slow_cps True
                                if thyrsus_about_druids1 and not thyrsus_about_thyrsusgift:
                                    $ options_thyrsus += 1
                                    textbutton '“If you have any message for the druids, I {i}could{/i} do you a favor.”' action [SetVariable("questionpreset", 0), Jump("thyrsus_about_thyrsusgift101")] style "nvl_button" text_slow_cps True
                                elif quest_thyrsusgift == 1:
                                    if item_thyrsusgift:
                                        $ options_thyrsus += 1
                                        textbutton '“I brought you your {i}prized possessions{/i}.”' action [SetVariable("questionpreset", 0), Jump("thyrsus_about_thyrsusgift103")] style "nvl_button" text_slow_cps True
                                    elif not thyrsus_about_thyrsusgift_bonusquestion_1 or not thyrsus_about_thyrsusgift_bonusquestion_2 or not thyrsus_about_thyrsusgift_bonusquestion_3 or not thyrsus_about_thyrsusgift_bonusquestion_4 or not thyrsus_about_thyrsusgift_bonusquestion_5 or not thyrsus_about_thyrsusgift_bonusquestion_6: 
                                        $ options_thyrsus += 1
                                        textbutton '“I have a few more questions about the old wand”' action [SetVariable("questionpreset", 0), Jump("thyrsus_about_thyrsusgift101bonus")] style "nvl_button" text_slow_cps True
                                    else:
                                        textbutton 'He wants me to bring him a wand from Howler’s Dell.' action NullAction() style "nvl_button2" text_slow_cps True
                                elif quest_thyrsusgift == 2:
                                    if quest_thyrsusgift_dayofsuccess < day and not thyrsus_about_thyrsusgift_parentscomment:
                                        $ options_thyrsus += 1
                                        textbutton '“How did it go? With your parents?”' action [SetVariable("questionpreset", 0), Jump("thyrsus_about_thyrsusgift_parentscomment01")] style "nvl_button" text_slow_cps True
                                    elif thyrsus_about_thyrsusgift_parentscomment and druidcave_about_thyrsusgift_druidcomment and thyrsus_about_druids2 and not thyrsus_about_thyrsusgift_druidcomment:
                                        $ options_thyrsus += 1
                                        textbutton '“You may want to have a chat with the old druid.”' action [SetVariable("questionpreset", 0), Jump("thyrsus_about_thyrsusgift_druidcomment01")] style "nvl_button" text_slow_cps True
                                if thyrsus_about_druids1 and druidcave_druid_about_thyrsus and not thyrsus_about_druids2:
                                    $ options_thyrsus += 1
                                    textbutton '“I bring a message from your old teacher.”' action [SetVariable("questionpreset", 0), Jump("thyrsus_about_druids201")] style "nvl_button" text_slow_cps True
                                if thyrsus_about_himself1 and not thyrsus_about_peat:
                                    $ options_thyrsus += 1
                                    textbutton '“Is peat really worth constant overseeing?”' action [SetVariable("questionpreset", 0), Jump("thyrsus_about_peat01")] style "nvl_button" text_slow_cps True
                                if quest_foggy3whitemarshes == 1 and quest_foggy3whitemarshes_description01 and not quest_foggy3whitemarshes_description02 and item_cidercask and not thyrsus_about_cidercask:
                                    $ options_thyrsus += 1
                                    textbutton '“I was meant to deliver this cask of cider to {color=#f6d6bd}Helvius{/color}, but he’s afraid to accept it. Any advice?”' action [SetVariable("questionpreset", 0), Jump("thyrsus_about_cidercask01")] style "nvl_button" text_slow_cps True
                                if quest_foggy3whitemarshes == 1 and quest_foggy3whitemarshes_description01 and not quest_foggy3whitemarshes_description02 and item_cidercask and thyrsus_about_cidercask and not thyrsus_about_cidercask_delivered:
                                    $ options_thyrsus += 1
                                    textbutton '“You can take the cider, if you want.”' action [SetVariable("questionpreset", 0), Jump("thyrsus_about_cidercask02")] style "nvl_button" text_slow_cps True
                                if (thyrsus_about_asterion1 and quest_asterion == 1 and not asterion_found and not thyrsus_about_asterion2) or (helvius_about_asterion2 and quest_asterion == 1 and not asterion_found and not thyrsus_about_asterion2) or (whitemarshes_child_asterion and quest_asterion == 1 and not asterion_found and not thyrsus_about_asterion2) or (quest_asterion_description11a and quest_asterion == 1 and not asterion_found and not thyrsus_about_asterion2):
                                    $ options_thyrsus += 1
                                    textbutton '“Do you know anything about {color=#f6d6bd}Asterion’s{/color} whereabouts?”' action [SetVariable("questionpreset", 0), Jump("thyrsus_about_asterion201")] style "nvl_button" text_slow_cps True
                                elif quest_asterion == 1 and not asterion_found and thyrsus_about_asterion2:
                                    if (not thyrsus_about_asterion_question1 and not asterion_highisland_knowsabout) or not thyrsus_about_asterion_question2 or not thyrsus_about_asterion_question3 or (not thyrsus_about_asterion_question4 and not asterion_highisland_knowsabout) or (not thyrsus_about_asterion_question5 and description_asterion02b) or (not thyrsus_about_asterion_question5 and thyrsus_friendship >= 5):
                                        $ options_thyrsus += 1
                                        textbutton '“Let’s talk about {color=#f6d6bd}Asterion{/color}.”' action [SetVariable("questionpreset", 0), Jump("thyrsus_about_asterion202")] style "nvl_button" text_slow_cps True
                                if ruinedvillage_part_leftfield_EXPLORED == 1 and quest_ruins == 1 and not thyrsus_about_cursedsoil:
                                    $ options_thyrsus += 1
                                    textbutton '“I found a scrap of land that I think may be cursed, though I’m not sure how to examine it.”' action [SetVariable("questionpreset", 0), Jump("thyrsus_about_cursedsoil01")] style "nvl_button" text_slow_cps True
                                if not whitemarshes_nomoreundead and not orentius_spared and not whitemarshes_attacked and whitemarshes_firsttime:
                                    if thyrsus_about_himself1 and whitemarshes_opposition and description_thyrsus05 and not thyrsus_about_dissent1:
                                        $ options_thyrsus += 1
                                        textbutton 'I stare at him. “Something needs to be done about the undead.”' action [SetVariable("questionpreset", 0), Jump("thyrsus_about_dissent101")] style "nvl_button" text_slow_cps True
                                    elif thyrsus_about_himself3 and whitemarshes_opposition and not thyrsus_about_dissent1:
                                        $ options_thyrsus += 1
                                        textbutton '“Are you telling me you’re {i}wardening{/i} the bogs because you wanted to do so? You refused to accept the new order of things, these necromantic practices.”' action [SetVariable("questionpreset", 0), Jump("thyrsus_about_dissent101alt")] style "nvl_button" text_slow_cps True
                                    elif thyrsus_about_dissent1 and not thyrsus_about_dissent2:
                                        $ options_thyrsus += 1
                                        textbutton '“I need to meet with {color=#f6d6bd}Orentius{/color}.”' action [SetVariable("questionpreset", 0), Jump("thyrsus_about_dissent201")] style "nvl_button" text_slow_cps True
                                    elif (thyrsus_about_dissent2 and not thyrsus_about_dissent_question1) or (thyrsus_about_dissent2 and not thyrsus_about_dissent_question2) or (thyrsus_about_dissent2 and not thyrsus_about_dissent_question3) or (thyrsus_about_dissent2 and not thyrsus_about_dissent_question4) or (thyrsus_about_dissent2 and not thyrsus_about_dissent_question5) or (thyrsus_about_dissent2 and not thyrsus_orentius_canhelp):
                                        $ options_thyrsus += 1
                                        textbutton '“Let’s talk about {color=#f6d6bd}Orentius{/color}.”' action [SetVariable("questionpreset", 0), Jump("thyrsus_about_dissent204")] style "nvl_button" text_slow_cps True
                                if not options_thyrsus:
                                    textbutton 'I have nothing to say to him.' action NullAction() style "nvl_button2" text_slow_cps True

                            elif questionpreset == "helvius1":
                                if quest_foggy3whitemarshes == 1 and not quest_foggy3whitemarshes_description01 and item_cidercask and not helvius_about_cidercask:
                                    $ options_helvius += 1
                                    textbutton '“I have a delivery from {color=#f6d6bd}Foggy{/color}.” I pat the cask strapped to my bundles.' action [SetVariable("questionpreset", 0), Jump("whitemarsheshelviusaboutcidercask01")] style "nvl_button" text_slow_cps True
                                if not helvius_about_undead1:
                                    $ options_helvius += 1
                                    textbutton 'I look at the undead workers. “They don’t bother you?”' action [SetVariable("questionpreset", 0), Jump("whitemarsheshelviusaboutundead01")] style "nvl_button" text_slow_cps True
                                if (helvius_about_undead1 and not helvius_about_undead2 and description_whitemarshes05) or (helvius_about_undead1 and not helvius_about_undead2 and description_whitemarshes10):
                                    $ options_helvius += 1
                                    textbutton '“I hear what you say about the awoken, but your tribe used to be strong without them.”' action [SetVariable("questionpreset", 0), Jump("whitemarsheshelviusaboutundead02")] style "nvl_button" text_slow_cps True
                                if description_orentius00 and not helvius_about_orentius1 and not orentius_spared:
                                    $ options_helvius += 1
                                    textbutton '“I’d like to speak with {color=#f6d6bd}Orentius{/color}.”' action [SetVariable("questionpreset", 0), Jump("helvius_about_orentius101")] style "nvl_button" text_slow_cps True
                                elif helvius_about_orentius1 and not helvius_about_orentius2 and not orentius_spared and (whitemarshes_reputation+appearance_charisma) >= helvius_orentius_threshold:
                                    $ options_helvius += 1
                                    textbutton '“Do you really think I’m not trustworthy enough to speak with {color=#f6d6bd}Orentius{/color}?”' action [SetVariable("questionpreset", 0), Jump("whitemarsheshelviusaboutaboutorentius201")] style "nvl_button" text_slow_cps True
                                elif helvius_about_orentius1 and not helvius_about_orentius2 and not orentius_spared and (whitemarshes_reputation+appearance_charisma) < helvius_orentius_threshold:
                                    textbutton 'He doesn’t trust me enough to let me see Orentius.' action NullAction() style "nvl_button2" text_slow_cps True
                                elif helvius_about_orentius1 and helvius_about_orentius2 and not orentius_spared and quarters >= (world_daylength-4):
                                    $ options_helvius += 1
                                    textbutton '“I’m ready to meet with him now.”' action [SetVariable("questionpreset", 0), Jump("helvius_about_orentius202")] style "nvl_button" text_slow_cps True
                                elif helvius_about_orentius1 and helvius_about_orentius2 and not orentius_spared and quarters < (world_daylength-4):
                                    $ options_helvius += 1
                                    textbutton 'He won’t let me meet with Orentius before evening.' action NullAction() style "nvl_button2" text_slow_cps True
                                    textbutton 'I sit down by the well and wait until I can see {color=#f6d6bd}Orentius{/color}.' action [SetVariable("quarters", world_daylength-4)] style "nvl_button" text_slow_cps True
                                if not helvius_about_whitemarshes:
                                    $ options_helvius += 1
                                    textbutton '“I’d like to learn more about {color=#f6d6bd}White Marshes{/color}.”' action [SetVariable("questionpreset", 0), Jump("whitemarsheshelviusaboutwhitemarshes01")] style "nvl_button" text_slow_cps True
                                if helvius_about_whitemarshes and not helvius_about_independence:
                                    $ options_helvius += 1
                                    textbutton '“So you want to separate yourself from the other settlements.”' action [SetVariable("questionpreset", 0), Jump("whitemarsheshelviusaboutgrowingindependent01")] style "nvl_button" text_slow_cps True
                                if helvius_about_whitemarshes and description_whitemarshes05 and not helvius_about_wood:
                                    $ options_helvius += 1
                                    textbutton '“You used to sell wood, correct?”' action [SetVariable("questionpreset", 0), Jump("helvius_about_wood01")] style "nvl_button" text_slow_cps True
                                if ruinedvillage_confront_can and not ruinedvillage_truth and helvius_about_independence and helvius_about_wood and helvius_about_undead2 and not helvius_about_steephouse:
                                    $ options_helvius += 1
                                    textbutton '“The changes and struggles of recent years... Are they related to what happened to the village in the south?”' action [SetVariable("questionpreset", 0), Jump("whitemarsheshelviusaboutsteephouse01")] style "nvl_button" text_slow_cps True
                                if quest_asterion == 1 and not asterion_found and not helvius_about_asterion1:
                                    $ options_helvius += 1
                                    textbutton '“Is {color=#f6d6bd}Asterion{/color} around?”' action [SetVariable("questionpreset", 0), Jump("whitemarsheshelviusaboutasterion01")] style "nvl_button" text_slow_cps True
                                elif (quest_asterion == 1 and not asterion_found and helvius_about_asterion1 == 1 and not helvius_about_asterion2 and (whitemarshes_reputation+appearance_charisma) >= 3):
                                    $ options_helvius += 1
                                    textbutton '“Are you {i}sure{/i} you have nothing to tell me about {color=#f6d6bd}Asterion{/color}?”' action [SetVariable("questionpreset", 0), Jump("whitemarsheshelviusaboutasterion02v01")] style "nvl_button" text_slow_cps True
                                elif (quest_asterion == 1 and not asterion_found and helvius_about_asterion1 == 1 and not helvius_about_asterion2 and quest_asterion_description02) or (quest_asterion == 1 and not asterion_found and helvius_about_asterion1 == 1 and not helvius_about_asterion2 and quest_asterion_description11a):
                                    $ options_helvius += 1
                                    textbutton '“You say you know nothing about {color=#f6d6bd}Asterion{/color}, but people claim he had strong ties with your tribe.”' action [SetVariable("questionpreset", 0), Jump("whitemarsheshelviusaboutasterion02v02")] style "nvl_button" text_slow_cps True
                                elif quest_asterion == 1 and not asterion_found and helvius_about_asterion1 == 1 and not helvius_about_asterion2 and (whitemarshes_reputation+appearance_charisma) < 3:
                                    textbutton 'He gets upset whenever I mention Asterion.' action NullAction() style "nvl_button2" text_slow_cps True
                                if not quest_recruitahunter_spokento_helvius and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_cassia_completed:
                                    textbutton '“Have you ever met {color=#f6d6bd}Cassia{/color}? She’s a warrior from {color=#f6d6bd}Gale Rocks{/color}.”' action [SetVariable("questionpreset", 0), Jump("helvius_about_recruitahunter01")] style "nvl_button" text_slow_cps True
                                if not helvius_about_plague1 and oldpagos_plague_known and oldpagos_cured:
                                    $ options_helvius += 1
                                    textbutton '“The people of {color=#f6d6bd}Old Págos{/color} were suffering from a plague, but I helped them overcome it.”' action [SetVariable("questionpreset", 0), Jump("whitemarsheshelviusaboutplague02alt")] style "nvl_button" text_slow_cps True
                                elif helvius_about_plague1 and not helvius_about_plague2 and oldpagos_cured:
                                    $ options_helvius += 1
                                    textbutton '“I’ve helped to purge the plague in {color=#f6d6bd}Old Págos{/color}. Maybe with time the things will return to normal.”' action [SetVariable("questionpreset", 0), Jump("whitemarsheshelviusaboutplague02")] style "nvl_button" text_slow_cps True
                                elif not helvius_about_plague1 and oldpagos_plague_known:
                                    $ options_helvius += 1
                                    textbutton '“The people of {color=#f6d6bd}Old Págos{/color} are fighting a plague.”' action [SetVariable("questionpreset", 0), Jump("whitemarsheshelviusaboutplague01")] style "nvl_button" text_slow_cps True
                                if not thyrsus_about_asterion_question5:
                                    if (quest_intelforpeltnorth == 1 and not helvius_about_bandits1 and not helvius_about_bandits2) or (banditshideout_bandits_pchearedabout and not helvius_about_bandits1 and not helvius_about_bandits2):
                                        $ options_helvius += 1
                                        textbutton '“Were you recently bothered by any highwaymen?”' action [SetVariable("questionpreset", 0), Jump("whitemarsheshelviusaboutbandits01")] style "nvl_button" text_slow_cps True
                                    elif (quest_intelforpeltnorth == 1 and helvius_about_bandits1 and not helvius_about_bandits2 and druidcave_druid_about_bandits1) or (quest_intelforpeltnorth == 1 and helvius_about_bandits1 and not helvius_about_bandits2 and druidcave_druid_about_bandits1):
                                        $ options_helvius += 1
                                        textbutton '“According to what an old druid told me, the highwaymen bother you much more severely than you lead me to believe.”' action [SetVariable("questionpreset", 0), Jump("whitemarsheshelviusaboutbandits02alt")] style "nvl_button" text_slow_cps True
                                    elif (quest_intelforpeltnorth == 1 and helvius_about_bandits1 and not helvius_about_bandits2 and (whitemarshes_reputation+appearance_charisma) >= helvius_about_bandits_reputation) or (quest_intelforpeltnorth == 1 and helvius_about_bandits1 and not helvius_about_bandits2 and (whitemarshes_reputation+appearance_charisma) >= helvius_about_bandits_reputation):
                                        $ options_helvius += 1
                                        textbutton '“We were talking about the highwaymen...”' action [SetVariable("questionpreset", 0), Jump("whitemarsheshelviusaboutbandits02")] style "nvl_button" text_slow_cps True
                                    elif (quest_intelforpeltnorth == 1 and helvius_about_bandits1 and not helvius_about_bandits2 and (whitemarshes_reputation+appearance_charisma) < helvius_about_bandits_reputation) or (quest_intelforpeltnorth == 1 and helvius_about_bandits1 and not helvius_about_bandits2 and (whitemarshes_reputation+appearance_charisma) < helvius_about_bandits_reputation):
                                        textbutton 'He doesn’t trust me enough to speak with me about the highwaymen.' action NullAction() style "nvl_button2" text_slow_cps True
                                if (quest_missinghunters == 1 and not bogentrance_dialogue_about_missinghunters and not helvius_about_missinghunters) or (quest_missinghunters == 1 and bogentrance_dialogue_about_missinghunters and not helvius_about_missinghunters and not northernroad_rawhide_owner):
                                    $ options_helvius += 1
                                    textbutton '“I seek a few missing hunters from {color=#f6d6bd}Creeks{/color}. Are they here, maybe?”' action [SetVariable("questionpreset", 0), Jump("whitemarsheshelviusaboutmissinghunters01")] style "nvl_button" text_slow_cps True
                                elif quest_missinghunters == 1 and helvius_about_missinghunters and item_rawhide and not northernroad_rawhide_owner:
                                    $ options_helvius += 1
                                    textbutton '“You mentioned {color=#f6d6bd}Dalia{/color}. Does this rawhide belong to her?”' action [SetVariable("questionpreset", 0), Jump("whitemarsheshelviusaboutmissinghunters02")] style "nvl_button" text_slow_cps True
                                if helvius_about_cidercask and thyrsus_about_cidercask_delivered and not helvius_about_cidercask_thyrsus:
                                    $ options_helvius += 1
                                    textbutton 'I lower my voice. “You may want to speak with {color=#f6d6bd}Thyrsus{/color}. I heard he has some {i}hard apples{/i} for you.”' action [SetVariable("questionpreset", 0), Jump("whitemarsheshelviusaboutcidercask03")] style "nvl_button" text_slow_cps True
                                if quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_whitemarshes and not helvius_about_bronzerod:
                                    $ options_helvius += 1
                                    textbutton '“{color=#f6d6bd}Eudocia{/color}, the enchantress, would like to place this rod in your village, somewhere high. Would that be a problem?”' action [SetVariable("questionpreset", 0), Jump("whitemarsheshelviusaboutbronzerod01")] style "nvl_button" text_slow_cps True
                                elif quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_whitemarshes and helvius_about_bronzerod:
                                    $ options_helvius += 1
                                    textbutton '“About {color=#f6d6bd}Eudocia’s{/color} rod...”' action [SetVariable("questionpreset", 0), Jump("whitemarsheshelviusaboutbronzerod02")] style "nvl_button" text_slow_cps True
                                if helvius_about_undead1 and oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated and not helvius_about_oldtunnel1:
                                    $ options_helvius += 1
                                    textbutton '“I could use your tribe’s assistance.” I tell him about the undead roaming in the old tunnel in the north.' action [SetVariable("questionpreset", 0), Jump("whitemarsheshelviusaboutoldtunnel01")] style "nvl_button" text_slow_cps True
                                elif helvius_about_undead1 and oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated and helvius_about_oldtunnel1 and not helvius_about_oldtunnel2 and item_pileofbones_sold and (whitemarshes_reputation+appearance_charisma) >= (helvius_about_oldtunnel_reputation/2):
                                    $ options_helvius += 1
                                    textbutton '“...Be serious. I sold you a pile of bones. It should be enough to prove my intentions are clear.”' action [SetVariable("questionpreset", 0), Jump("whitemarsheshelviusaboutoldtunnel02alt")] style "nvl_button" text_slow_cps True
                                elif helvius_about_undead1 and oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated and helvius_about_oldtunnel1 and not helvius_about_oldtunnel2 and (whitemarshes_reputation+appearance_charisma) >= helvius_about_oldtunnel_reputation:
                                    $ options_helvius += 1
                                    textbutton '“You know me well enough to realize I don’t try to lure you into a trap. Help me with the old tunnel.”' action [SetVariable("questionpreset", 0), Jump("whitemarsheshelviusaboutoldtunnel02")] style "nvl_button" text_slow_cps True
                                elif helvius_about_undead1 and oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated and helvius_about_oldtunnel1 and not helvius_about_oldtunnel2 and (whitemarshes_reputation+appearance_charisma) < helvius_about_oldtunnel_reputation:
                                    textbutton 'He refuses to help me with the undead roaming in the old tunnel.' action NullAction() style "nvl_button2" text_slow_cps True
                                elif helvius_about_undead1 and oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated and helvius_about_oldtunnel2 and not helvius_about_oldtunnel_paid:
                                    $ options_helvius += 1
                                    textbutton '“Let’s talk the price for clearing the tunnel.”' action [SetVariable("questionpreset", 0), Jump("whitemarsheshelviusaboutoldtunnel04")] style "nvl_button" text_slow_cps True
                                if quest_orentius_thais_description03 and not orentius_met and not helvius_about_thaisattack and (whitemarshes_reputation+appearance_charisma) < helvius_orentius_threshold:
                                    $ options_helvius += 1
                                    textbutton 'It will sabotage {color=#f6d6bd}Thais’{/color} plans, but may help me earn his trust. “You need to strengthen your guards...”' action [SetVariable("questionpreset", 0), Jump("whitemarsheshelviusaboutthaisconspiracy01")] style "nvl_button" text_slow_cps True
                                if (banditshideout_firsttime and thyrsus_about_asterion_question5 and not helvius_about_bandits3 and (whitemarshes_reputation+appearance_charisma) < helvius_orentius_threshold) or (banditshideout_firsttime and helvius_about_bandits2 and thyrsus_about_asterion_question5 and not helvius_about_bandits3 and (whitemarshes_reputation+appearance_charisma) < helvius_orentius_threshold):
                                    $ options_helvius += 1
                                    textbutton 'It would anger {color=#f6d6bd}Glaucia{/color}, but may help me earn his trust. “I know where’s the highwaymen’s hideout.”' action [SetVariable("questionpreset", 0), Jump("whitemarsheshelviusaboutbandits04")] style "nvl_button" text_slow_cps True
                                if whitemarshes_pursewoman_talkedto and not helvius_about_womanwithpurse_denied and not helvius_about_womanwithpurse1 and not helvius_about_womanwithpurse2 and not helvius_about_womanwithpurse3 and (whitemarshes_reputation+appearance_charisma) < helvius_orentius_threshold:
                                    $ options_helvius += 1
                                    textbutton 'I could tell him about the woman that asked me to find her savings...' action [SetVariable("questionpreset", 0), Jump("whitemarsheshelviusaboutwomanwithpurse01")] style "nvl_button" text_slow_cps True
                                if not helvius_about_buying:
                                    $ options_helvius += 1
                                    textbutton '{image=cointest} “Shall we trade?”' action [SetVariable("questionpreset", 0), Jump("helvius_about_buying01")] style "nvl_button" text_slow_cps True
                                if helvius_about_buying:
                                    $ options_helvius += 1
                                    textbutton '{image=cointest} “I have some wares to sell.”' action [SetVariable("questionpreset", 0), Jump("helvius_about_buying02")] style "nvl_button" text_slow_cps True
                                textbutton '“Farewell.”' action [SetVariable("questionpreset", 0), Jump("whitemarshesafterinteraction01")] style "nvl_button" text_slow_cps True
                                if not options_helvius:
                                    textbutton 'I have nothing to say to him.' action NullAction() style "nvl_button2" text_slow_cps True

                            elif questionpreset == "orentius1":
                                if not orentius_argument_undeadaredangerous:
                                    $ options_orentius += 1
                                    textbutton '“You must be aware that undead are dangerous.”' action [SetVariable("questionpreset", 0), Jump("whitemarshesorentiusaboutundeadaredangerous01")] style "nvl_button" text_slow_cps True
                                if not orentius_argument_orthodoxy:
                                    $ options_orentius += 1
                                    textbutton '“Should a priest of The Wright really involve themselves with forbidden rituals?”' action [SetVariable("questionpreset", 0), Jump("whitemarshesorentiusaboutorthodoxy01")] style "nvl_button" text_slow_cps True
                                if not orentius_argument_locals:
                                    $ options_orentius += 1
                                    textbutton '“Do you truly believe your people are grateful for your leadership?”' action [SetVariable("questionpreset", 0), Jump("whitemarshesorentiusaboutlocals01")] style "nvl_button" text_slow_cps True
                                if not orentius_argument_empathy:
                                    $ options_orentius += 1
                                    textbutton '“You may have good reasons to do what you’re doing...”' action [SetVariable("questionpreset", 0), Jump("whitemarshesorentiusaboutempathy01")] style "nvl_button" text_slow_cps True
                                if foragers_caius_aboutvision and not orentius_argument_caius:
                                    $ options_orentius += 1
                                    textbutton '“I met this {i}prophet{/i} at {color=#f6d6bd}Foggy’s{/color}...”' action [SetVariable("questionpreset", 0), Jump("whitemarshesorentiusaboutcaius01")] style "nvl_button" text_slow_cps True
                                if not options_orentius and orentius_argument_empathy and not orentius_argument_trust:
                                    textbutton 'I may be pushing this too far... “Can’t you see I’m trustworthy? I don’t wish you harm.”' action [SetVariable("questionpreset", 0), Jump("whitemarshesorentiusabouttrust01")] style "nvl_button" text_slow_cps True
                                if not options_orentius:
                                    textbutton '“I guess we’re done here.”' action [SetVariable("questionpreset", 0), Jump("whitemarshesorentiusafterdispute01")] style "nvl_button" text_slow_cps True

                            elif i.action and not questionpreset:
                                if "{image=d6}" in i.caption:
                                    if persistent.textstyle == "pixel":
                                        textbutton i.caption.replace("{image=d6}", "{image=d62}"):
                                            action [i.action, SetVariable("autosave_counter", autosave_counter+1)]
                                            style "nvl_button" text_slow_cps True
                                    else:
                                        textbutton i.caption:
                                            action [i.action, SetVariable("autosave_counter", autosave_counter+1)]
                                            style "nvl_button" text_slow_cps True
                                elif "(disabled)" in i.caption:
                                    textbutton i.caption.replace("(disabled)", "") style "nvl_button2" text_slow_cps True
                                else:
                                    textbutton i.caption:
                                        action [i.action, SetVariable("autosave_counter", autosave_counter+1)]
                                        style "nvl_button" text_slow_cps True
                            elif not questionpreset:
                                textbutton i.caption:
                                    action [i.action, SetVariable("autosave_counter", autosave_counter+1)]
                                    style "nvl_button" text_slow_cps True

                        # for n, i in enumerate(items, 1): # n would be the number starting from 1
                        #     if n<10:
                        #         key str(n) action i.action
                        #     textbutton str(n) + ") " + i.caption action i.action

    if showdialoguebar:
        vbar value YScrollValue ("dialogue"):
            unscrollable "hide"
            xpos 1526
            ypos 48
            ysize 984
            xsize 5

screen nvl_dialogue(dialogue):
    for d in dialogue:
        window:
            id d.window_id
            fixed:
                yfit gui.nvl_height is None
                if d.who is not None:
                    text d.who:
                        id d.who_id
                text d.what:
                    id d.what_id
                    if persistent.textstyle == "basic":
                        line_spacing 8
                    if persistent.textstyle == "pixel":
                        line_spacing 10

## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length
style nvl_window is default
style nvl_entry is default
style nvl_label is say_label
style nvl_dialogue is say_dialogue
style nvl_button is button:
    xmaximum 800
style nvl_button_text is button_text:
    size 26
style nvl_button2 is button:
    xmaximum 800
style nvl_button2_text is button_text:
    size 26
style nvl_window:
    xfill True
    yfill True
    #background "gui/nvl.png"
    padding gui.nvl_borders.padding
style nvl_entry:
    xfill True
    ysize gui.nvl_height
style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign
style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")
style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")
style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign
style nvl_button2:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign
style nvl_button_text:
    properties gui.button_text_properties("nvl_button")
    hover_color '#fff1e5'#'#f6d6bd'
    size 28
style nvl_button2_text:
    properties gui.button_text_properties("nvl_button")
    #hover_color '#f6d6bd'
    size 28
    color "#6a6a6a"

init python:
    config.empty_window = nvl_show_core
    config.window_hide_transition = dissolve
    config.window_show_transition = dissolve
