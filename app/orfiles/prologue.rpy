###################### Prologue
default militarycamp_gate1 = 0
default militarycamp_gate2 = 0
default militarycamp_gate3 = 0
default militarycamp_firstwatch = 0
default militarycamp_firstwatch_finished = 0
default militarycamp_sleep_tent = 0

default tulia_friendship = 0

default tulia_about_tired = 0
default tulia_questions_main = 0
default tulia_about_peninsula = 0
default tulia_about_peninsula_bonusquestion1 = 0
default tulia_about_peninsula_bonusquestion2 = 0
default tulia_about_peninsula_bonusquestion3 = 0
default tulia_about_peninsula_bonusquestion4 = 0
default tulia_about_asterion1 = 0
default tulia_questions_side = 0
default tulia_about_hersquad = 0
default tulia_about_herself = 0
default tulia_about_hermission = 0
default tulia_about_camp = 0
default tulia_about_advice = 0
default tulia_attitude = 0

###################### Tutorials
default persistent.tutorial_display = True
default tutorial_finished = 0
default tutorial_attitudes = 0
default tutorial_inventory = 0
default tutorial_journal = 0
default tutorial_archive = 0
default tutorial_hp = 0
default tutorial_armor = 0
default tutorial_appearance = 0
default tutorial_sleep = 0
default tutorial_restatinn = 0
default tutorial_map = 0
default tutorial_abilities = 0
default tutorial_random = 0
default tutorial_attitudes_gray = 0
default tutorial_achievements = 0
default tutorial_endgame = 1
default tutorial_input = 0
default tutorial_input_roots = 0
default tutorial_twopictures = 0
default tutorial_5hp = 0
default tutorial_selling = 0
default tutorial_selling2 = 0
default tutorial_daylength = 0
default tutorial_bogdaylength = 0
default tutorial_lateevening = 0
default tutorial_eating = 0
default tutorial_sheet = 0
default tutorial_sheet_display = 0
default tutorial_using_items = 0

default world_higher_night_damage = 0
default difficultypick_advanced_questseasier = 0

label startALL:
    label start:
        $ difficultypick_advanced_questseasier = 0
        if persistent.difficulty == 1:
            $ game_mode = 1
            # $ foragingground_quest_timer += 10
            $ difficultypick_advanced_questseasier = 1
            $ akakios_quest_healingpotion_deadline += 10
            $ pyrrhos_deathcounter_unmet += 10
            $ world_deadline = 1000
            $ coins += 5
            $ orentius_arguments_needed -= 1
            $ eudocia_invitation_argument_points_threshold -= 3
            $ galerocks_debate_argument_needed -= 1
            $ creeks_reasonstojoin_points += 1
            $ howlersdell_steephouseconfrontation_elpis_points_required -= 2
            $ howlersdell_steephouseconfrontation_thais_points_required -= 2
            $ beholder_altar_awakened_threshold -= 4
        if persistent.difficulty == 2:
            $ game_mode = 2
            $ world_deadline = 40
        if persistent.difficulty == 3:
            $ world_higher_night_damage = 1
            $ game_mode = 3
            $ world_deadline = 30
        if persistent.difficulty == 0:
            $ game_mode = 0
            if persistent.difficultypick_advanced_world_deadline == 45:
                $ world_deadline = 45
            elif persistent.difficultypick_advanced_world_deadline == 40:
                $ world_deadline = 40
            elif persistent.difficultypick_advanced_world_deadline == 30:
                $ world_deadline = 30
            else:
                $ world_deadline = 1000
            if persistent.difficultypick_advanced_questseasier == 1:
                $ difficultypick_advanced_questseasier = 1
                $ akakios_quest_healingpotion_deadline += 10
                $ pyrrhos_deathcounter_unmet += 10
                $ orentius_arguments_needed -= 1
                $ eudocia_invitation_argument_points_threshold -= 3
                $ galerocks_debate_argument_needed -= 1
                $ creeks_reasonstojoin_points += 1
                $ howlersdell_steephouseconfrontation_elpis_points_required -= 2
                $ howlersdell_steephouseconfrontation_thais_points_required -= 2
                $ beholder_altar_awakened_threshold -= 4
            if persistent.difficultypick_advanced_bonusdamage == 1:
                $ world_higher_night_damage = 1
            else:
                $ world_higher_night_damage = 0
            if persistent.difficultypick_advanced_potion == 1:
                $ item_smallhealingpotion += 1
            if persistent.difficultypick_advanced_coins == 10:
                $ coins += 5
            # elif persistent.difficultypick_advanced_coins == 5:
            #     $ coins += 5
            elif persistent.difficultypick_advanced_coins == 0:
                $ coins = 0
        $ persistent.difficultypick_advanced_world_deadline = 40
        $ persistent.difficultypick_advanced_questseasier = 0
        $ persistent.difficultypick_advanced_bonusdamage = 0
        $ persistent.difficultypick_advanced_coins = 5
        $ persistent.difficultypick_advanced_potion = 0
        scene layoutfull
        if persistent.difficultypick_advanced_skip_prologue:
            $ persistent.difficultypick_advanced_skip_prologue = 0
            $ quarters = 95
            show areapicture nightsky01 at basicfade
            $ pc_area = "militarycamp"
            $ tomilitarycamp = 0
            $ quick_menu = True
            $ persistent.tutorial_display = 0
            $ pc_hp = limit_pc_hp(3)
            $ hpscreen = 1
            $ isinventory = 1
            $ armorscreen = 1
            $ foodscreen = 1
            $ isjournal = 1
            $ appearancescreen = 1
            $ restunlocked = 1
            $ classabilityscreen = 1
            $ mapunlocked = 1
            $ tosoutherncrossroads = 0
            $ travel_firsttime = 1
            $ item_rope = 1
            show screen achievements()
            show screen doubleimage()
            show screen doubleimage2()
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            $ showdialoguebar = 1
            $ interface_showline = True
            $ quest_explorepeninsula = 1
            $ quest_explorepeninsula_description01 = "I need to explore the peninsula as thoroughly as I can. I have to get to know the locals and find out how much of a profit can be made here, then bring the news to {color=#f6d6bd}Hovlavan{/color}."
            $ quest_explorepeninsula_description01a = "To add worth to my work here, I could secure the roads by getting rid of any major threats, and convince the tribes to negotiate with the officials."
            $ quest_explorepeninsula_description02a = "Soldiers told me about a large village that repeatedly uses necromancy, even though it’s forbidden by law and can be extremely dangerous. I should take a look and judge for myself. The village is somewhere among the bogs, by the northwestern road."
            $ world_deadline_display = (world_deadline)
            $ description_asterion01 = "According to {color=#f6d6bd}Tulia{/color}, he was a bit of a recluse, constantly on the move, looking for work. Since he disappeared before summer, he may already be dead. His kids live near {color=#f6d6bd}Hovlavan{/color}."
            $ tulia_about_asterion1 += 1
            $ description_tulia01 = "She plans to return to {color=#f6d6bd}Hovlavan{/color} in the near future."
            $ quest_asterion = 1
            $ quest_asterion_description01 = "Before I became the roadwarden of this peninsula, a man known as {color=#f6d6bd}Asterion{/color} used to patrol these roads. If I manage to find out what happened to him and bring the news to {color=#f6d6bd}Tulia{/color} from the southern camp, I’ll receive his abandoned belongings."
            $ tulia_about_peninsula += 1
            $ tulia_questions_main = 2
            python:
                pcname = renpy.input("Folks call you by...", default="Leto", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                pcname = pcname.strip()
                pcname_reduced = pcname.strip().lower().replace(" ", "")
                if not pcname:
                    pcname = "Leto"
            menu:
                'You follow...
                '
                'The United Church.':
                    $ pc_religion = "theunitedchurch"
                    $ item_wingedhourglass = 1
                'An Order of Truth.':
                    $ pc_religion = "ordersoftruth"
                    $ item_wingedhourglass = 1
                'My fellowship.':
                    $ pc_religion = "fellowship"
                    $ item_wingedhourglass = 1
                'My ancestors.':
                    $ pc_religion = "pagan"
                'My own judgment.':
                    $ pc_religion = "none"
            menu:
                'You used to be...
                '
                'A fighter.':
                    $ item_crossbow = 1
                    $ item_crossbowquarrels += 3
                    $ armor = limit_armor(armor+3)
                    $ item_axe02 = 1
                    $ pc_class = "warrior"
                'A mage.':
                    $ pc_class = "mage"
                    $ armor = limit_armor(armor+2)
                    $ item_axe01 = 1
                    $ item_mageamulets = 1
                    $ mana = 3
                'A scholar.':
                    $ pc_class = "scholar"
                    $ armor = limit_armor(armor+2)
                    $ item_axe01 = 1
                    $ item_smallhealingpotion += 1
                    $ item_scholaringredients = 1
                    $ item_writinginstruments = 1
            menu:
                'You left to...
                '
                'Gather coins so I can help save my sibling from debt collectors.':
                    $ pc_goal = "ineedmoney"
                    $ quest_pc_goal_name = "Gather Wealth"
                'Get rich!':
                    $ pc_goal = "iwantmoney"
                    $ quest_pc_goal_name = "Become Rich"
                'Gain influence in the merchant guild.':
                    $ pc_goal = "iwantstatus"
                    $ quest_pc_goal_name = "Gain Influence"
                'Become a hero.':
                    $ pc_goal = "iwanttoberemembered"
                    $ quest_pc_goal_name = "Become a Hero"
                'Help people. Make this place safer.':
                    $ pc_goal = "iwanttohelp"
                    $ quest_pc_goal_name = "Help Others"
                'Find a new life for myself.':
                    $ pc_goal = "iwanttostartanewlife"
                    $ quest_pc_goal_name = "A New Life"
            $ quest_pc_goal = 1
            python:
                horsename = renpy.input("Your horse is called...", default="Sodal", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                horsename = horsename.strip()
                horsename_reduced = horsename.strip().lower().replace(" ", "")
                if not horsename:
                    horsename = "Sodal"
            menu:
                'And you...
                '
                'Care about them deeply.':
                    $ pc_likeshorsename = 1
                'Just use it for travel.':
                    $ pc_likeshorsename = 0
            show areapicture prologuemilitarycampscrap04 at basicfade
            $ day = 1
            $ quarters = 32
            menu:
                'While talking to Tulia...
                '
                'We helped each other, and I asked her about everything I could.':
                    $ quarters -= 2
                    $ tulia_friendship = 3
                    $ pc_food_gruel +=1
                    $ item_rations = limit_item_rations(item_rations-1)
                    $ tulia_about_peninsula_bonusquestion1 = 1
                    $ tulia_about_peninsula_bonusquestion2 = 1
                    $ tulia_about_peninsula_bonusquestion3 = 1
                    $ pc_food = limit_pc_food(pc_food-1)
                    $ foragers_caius_heardabout += 1
                    $ tulia_about_hersquad += 1
                    $ tulia_about_herself += 1
                    $ tulia_about_hermission += 1
                    $ description_tulia04 = "Her squad was meant to find a fitting place for a new outpost."
                    $ tulia_about_advice += 1
                    $ description_iason01 = "According to {color=#f6d6bd}Tulia{/color}, he prefers to stick to trade, doesn’t like to waste time on jokes and empty gestures."
                    $ tulia_about_camp += 1
                    $ militarycamp_firstwatch = 1
                'I could still learn more from her, but she offered me some help.':
                    $ tulia_friendship = 1
                    $ pc_food_gruel +=1
                    $ tulia_about_peninsula_bonusquestion1 = 1
                    $ tulia_about_peninsula_bonusquestion2 = 1
                    $ tulia_about_peninsula_bonusquestion3 = 1
                    $ pc_hp = limit_pc_hp(pc_hp-1)
                    $ pc_food = limit_pc_food(pc_food-1)
                    $ foragers_caius_heardabout += 1
                    $ tulia_about_hersquad += 1
                    $ description_tulia02 = "She didn’t expect to become a lieutenant. Most members of her squad are already dead."
                    $ tulia_about_herself += 1
                    $ tulia_about_advice += 1
                    $ description_iason01 = "According to {color=#f6d6bd}Tulia{/color}, he prefers to stick to trade, doesn’t like to waste time on jokes and empty gestures."
                    $ tulia_about_camp += 1
                'She was relieved to see me gone.':
                    $ tulia_friendship = -1
                    $ pc_hp = limit_pc_hp(pc_hp-1)
                    $ pc_food = limit_pc_food(pc_food-2)
                    $ cleanliness = limit_cleanliness(cleanliness-1)
                    $ mana = limit_mana(mana+2)
                    $ description_tulia02 = "She didn’t expect to become a lieutenant. Most members of her squad are already dead."
            show areapicture militarycamptosoutherncrossroads at basicfade    
            menu:
                'Once you faced the griffons, you...
                '
                '{image=d6} Risked combat.':
                    $ d100roll = renpy.random.randint(1, 8)
                    if not pc_food:
                        $ d100roll += 1
                    if pc_food == 3:
                        $ d100roll -= 1
                    if pc_food == 4:
                        $ d100roll -= 2
                    if d100roll != 1:
                        $ pc_hp = limit_pc_hp(pc_hp-1)
                '{image=d6} Waited.':
                    $ achievement_animalssavedpoints += 1
                    $ d100roll = 0
                    $ d100roll = renpy.random.randint(1, 4)
                    $ quarters += (4+d100roll)
                'Got through them with ease, thanks to my training.' if pc_class == "warrior":
                    $ tutorial_random = 0
                'Shot one with my crossbow.' if item_crossbow:
                    $ encounter_scavenger_griffon_hurt_quarrel = 1
                    $ item_crossbowquarrels -= 1
                'I casted a light spell at them. [[Cost: {color=#f6d6bd}1{/color} pneuma]' if pc_class == "mage":
                    $ mana = limit_mana(mana-1)
                'Mixed black powder with herbs to scare them away.' if pc_class == "scholar":
                    $ quarters += 1
            $ travel_destination = "southerncrossroads"
            $ world_skippingprologue = 1
            $ tutorial_sheet = 1
            stop music fadeout 4.0
            jump finaldestinationafterevent


        show areapicture prologuemilitarycampscrap01 at basicfade
        show screen characterstatus()
        show screen achievements()
        show screen doubleimage()
        show screen doubleimage2()
        $ quarters = 82
        $ pc_area = "militarycamp"
        $ tomilitarycamp = 0
        $ quick_menu = True
        nvl clear
        show screen tutorialtooltips()
        play nature "audio/ambient/prologuebirds01.ogg" fadeout 6.0 fadein 7.0 volume 1.0
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        $ showdialoguebar = 1
        $ interface_showline = True
        menu:
            'The wall is still standing. There are no wolves around, no stench of blood. Good signs.
            \n\nThis {i}should{/i} be the place you’re looking for. You were supposed to meet with a group of soldiers, but you hear no voices, no sounds of labor.
            \n\nThe gate is ajar, but the camp isn’t safe. It may keep away the goblins and pebblers, but not beastfolk, nor trolls. And the night is near.
            \n\nYour palfrey breathes heavily. It had a long day.
            '
            'I could just look for another shelter.' if not militarycamp_gate1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could just look for another shelter.')
                # $ item_rations = 2
                # $ item_chicken = 1
                # $ item_wildplants = 1
                # $ item_spiritrock = 1
                # $ item_generichealingpotion = 1
                # $ item_magicfruit = 1
                # $ item_magicfruit_lost = 1
                # $ item_potiondolmen = 1
                # $ item_potiondolmen_known = 1
                # $ item_smallhealingpotion = 1
                # $ item_sharpeningpotion = 1
                # $ item_sharpeningpotion_used = 1
                # $ item_gambeson01 = 1
                # $ item_gambeson02 = 1
                # $ item_asterionspear = 1
                # $ item_axe01 = 1
                # $ item_axe02 = 1
                # $ item_axe02alt = 1
                # $ item_axehead = 1
                # $ item_axeset = 1
                # $ item_axe03 = 1
                # $ item_crossbow = 1
                # $ item_crossbowquarrels = 1
                # $ item_mountainroadspear = 1
                # $ item_shield = 1
                # $ item_golemglove = 1
                # $ item_trollurine = 1
                # $ item_blindingpowder = 1
                # $ item_bonehook = 1
                # $ item_dragonhorn = 1
                # $ item_lantern = 1
                # $ item_magicchisel = 1
                # $ item_travelequipment = 1
                # $ item_witheringdust = 1
                # $ item_machete = 1
                # $ item_gambesonrepairset = 1
                # $ item_sewingkit = 1
                # $ item_arrow = 1
                # $ item_boxfromdolmen = 1
                # $ item_peltnorthberries = 1
                # $ item_empresscarp = 1
                # $ item_empresscarp_timelimit = 1
                # $ item_snakebait = 1
                # $ item_oceannecklace = 1
                # $ item_bronzerod = 1
                # $ item_magicpens = 1
                # $ item_asterionkey = 1
                # $ item_oldtunnelkey = 1
                # $ item_trapdoorkeydolmen = 1
                # $ item_watchtowerkey = 1
                # $ item_piershedkey = 1
                # $ item_oldtunnesmallkey = 1
                # $ item_bonebuckle = 1
                # $ item_bonebuckle_returned = 1
                # $ item_boneearring = 1
                # $ item_brokenknife = 1
                # $ item_rawhide = 1
                # $ item_pileofbones = 1
                # $ item_pileofbones_returned = 1
                # $ item_pileofbones_destroyed = 1
                # $ item_pileofbones_sold = 1
                # $ item_signpost = 1
                # $ item_casket = 1
                # $ item_casket_tested = 1
                # $ coins = 5
                # $ item_peltnorthberryclaw = 1
                # $ item_peltnorthberrytools = 1
                # $ item_elkfur = 1
                # $ item_harepelt = 1
                # $ item_sealskin = 1
                # $ item_asterionwine = 1
                # $ item_asterionwine_pcknows_1 = 1
                # $ item_asterionwine_pcknows_2 = 1
                # $ item_antlers = 1
                # $ item_asterionbow = 1
                # $ item_boartusks = 1
                # $ item_bonering = 1
                # $ item_cidercask = 1
                # $ item_furlesswolftrophy = 1
                # $ item_furlesswolftrophy_day = 1
                # $ item_griffonegg = 1
                # $ item_ironscraps = 1
                # $ item_linen = 1
                # $ item_dragonlingpaw = 1
                # $ item_dragonlingclaws = 1
                # $ item_spidersilk = 1
                # $ item_stoat = 1
                # $ item_stoat_day = 1
                # $ item_wingedhourglass = 1
                # $ item_wingedhourglass_worn = 1
                # $ item_wingedhourglass_taboo_broken = 1
                # $ item_cloak01 = 1
                # $ item_horse = 1
                # $ item_mageamulets = 1
                # $ item_scholaringredients = 1
                # $ item_writinginstruments = 1
                # $ item_rope = 1
                # $ item_bogfriend = 1
                # $ item_blackwoundwort = 1
                # $ item_ghoulblood = 1
                # $ item_marshbules = 1
                # $ item_powderedrock = 1
                # $ item_rocktobepowdered = 1
                # $ item_shortcutherbs = 1
                # $ item_spidervenom = 1
                # $ item_driftwood = 1
                # $ item_cursedsoil = 1
                # $ item_cavemushroom = 1
                # $ item_stingointment = 1
                # $ item_asterioncloak = 1
                # $ item_asterionpurse = 1
                # $ item_asteriontablet = 1
                # $ item_asteriontablet_read = 1
                # $ item_beholderroot = 1
                # $ item_bugrepellent = 1
                # $ item_earplugs = 1
                # $ item_goblinspear = 1
                # $ item_howlersdelltoken = 1
                # $ item_magicalsapling = 1
                # $ item_thaisletter = 1
                # $ item_thaisletter_opened = 1
                # $ item_thaisletter_read = 1
                # $ item_thaisletter_readingblocked = 1
                # $ item_teethset = 1
                # $ item_teethset_type = "hazelnut"
                # $ item_soap = 1
                # $ item_perfume = 1
                # $ item_perfume_type = "Cherry"
                # $ item_fancyclothes = 1
                # $ item_rawfish_gaining = 1
                # $ item_rawfish_losing = 1
                # $ item_rawfishtotalnumber = 1
                # $ item_rawfish01 = 1
                # $ item_rawfish02 = 1
                # $ item_rawfish03 = 1
                # $ item_rawfish04 = 1
                # $ item_rawfish05 = 1
                # $ item_rawfish06 = 1
                # $ item_rawfish07 = 1
                # $ item_rawfish08 = 1
                # $ item_rawfish09 = 1
                # $ item_rawfish10 = 1
                # $ item_fishtrap = 1
                # $ item_cookedfish = 1
                # $ item_ironingot = 1
                # $ item_spices = 1
                # # jump peltnorth_selling01
                # # jump howlersdelltradersellingitems01
                # # jump foggylakeregularquestionsselling01
                # # jump thyrsusselling01
                # # jump helvius_about_buying02after
                # # jump greenmountaintribeentrancebarter01
                # # jump greenmountaintribechiefbarteringfordragonhorn01
                jump prolcamp01choice01
            'I need to look around. Cautiously.' if not militarycamp_gate2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I need to look around. Cautiously.')
                jump prolcamp01choice02
            'I dismount and sneak to the gate. Let’s peek inside.' if not militarycamp_gate3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I dismount and sneak to the gate. Let’s peek inside.')
                jump prolcamp01choice03
            'I get off the horse and enter the camp briskly.' if not militarycamp_gate3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I get off the horse and enter the camp briskly.')
                jump prolcamp01entering01
            'It doesn’t look like much of a threat. I can enter.' if militarycamp_gate3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It doesn’t look like much of a threat. I can enter.')
                jump prolcamp01entering02

    label prolcamp01choice01: # I could just look for another shelter.
        $ militarycamp_gate1 = 1
        menu:
            'Doing so right before nightfall would only invite death. The monsters will soon start their hunt, and your horse won’t pull off another gallop.
            \n\nYou rub your eyes and hold back the yawn.
            '
            'I could just look for another shelter.' if not militarycamp_gate1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could just look for another shelter.')
                jump prolcamp01choice01
            'I need to look around. Cautiously.' if not militarycamp_gate2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I need to look around. Cautiously.')
                jump prolcamp01choice02
            'I dismount and sneak to the gate. Let’s peek inside.' if not militarycamp_gate3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I dismount and sneak to the gate. Let’s peek inside.')
                jump prolcamp01choice03
            'I get off the horse and enter the camp briskly.' if not militarycamp_gate3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I get off the horse and enter the camp briskly.')
                jump prolcamp01entering01
            'It doesn’t look like much of a threat. I can enter.' if militarycamp_gate3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It doesn’t look like much of a threat. I can enter.')
                jump prolcamp01entering02

    label prolcamp01choice02: # I need to look around. Cautiously.
        $ militarycamp_gate2 = 1
        if persistent.deafmode:
            $ deafcustom1 = "The birds, insects, and furry beasts are as loud as usual. "
        else:
            $ deafcustom1 = ""
        if not militarycamp_gate3:
            $ custom1 = "Considering the noise, you doubt that anyone noticed the clatter of hooves."
        else:
            $ custom1 = "The people inside the camp didn’t even notice the clatter of hooves."
        menu:
            '[deafcustom1][custom1]
            \n\nThe short, dry grasses barely cover the arid soil of this valley, but you’re maybe a minute away from the edge of the sparse woods, which get denser as they climb up the hills.
            \n\nAt best, this trail has a few more years before getting overgrown for good. Hard to believe it’s the only route north.
            '
            'I could just look for another shelter.' if not militarycamp_gate1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could just look for another shelter.')
                jump prolcamp01choice01
            'I need to look around. Cautiously.' if not militarycamp_gate2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I need to look around. Cautiously.')
                jump prolcamp01choice02
            'I dismount and sneak to the gate. Let’s peek inside.' if not militarycamp_gate3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I dismount and sneak to the gate. Let’s peek inside.')
                jump prolcamp01choice03
            'I get off the horse and enter the camp briskly.' if not militarycamp_gate3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I get off the horse and enter the camp briskly.')
                jump prolcamp01entering01
            'It doesn’t look like much of a threat. I can enter.' if militarycamp_gate3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It doesn’t look like much of a threat. I can enter.')
                jump prolcamp01entering02

    label prolcamp01choice03: # I dismount and sneak to the gate. Let’s peek inside.
        $ militarycamp_gate3 = 1
        if not tutorial_hp:
            $ tutorial_hp = 1
            $ pc_hp = limit_pc_hp(3)
            $ hpscreen = 1
        menu:
            'Your heavy boots hit the ground and the pain of the long ride finally catches up with you. You stretch out, bringing your back and legs comfort. All you want now is a table, a decent chair, a nice mug of beer, and some warm stew.
            \n\nWith any luck, your axe won’t be needed here.
            '
            'I approach the gate slowly.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the gate slowly.')
                $ tutorial_hp = 2
                show areapicture prologuemilitarycampscrap02withsack at basicfade
                menu:
                    'If it’s a military camp, it doesn’t look the part. Plenty of wasted space, the firepit is cold.
                    \n\n{color=#f6d6bd}Two people{/color} are sitting at the table, tired and disheartened. They’re looking in different directions, paying no attention to one another. One of them is holding a cup.
                    \n\nAfter a moment, you notice the quiet humming. You recognize the melody of a light-hearted drinking song from the city harbor.
                    '
                    'I could just look for another shelter.' if not militarycamp_gate1:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could just look for another shelter.')
                        jump prolcamp01choice01
                    'I need to look around. Cautiously.' if not militarycamp_gate2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I need to look around. Cautiously.')
                        jump prolcamp01choice02
                    'I dismount and sneak to the gate. Let’s peek inside.' if not militarycamp_gate3:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I dismount and sneak to the gate. Let’s peek inside.')
                        jump prolcamp01choice03
                    'I get off the horse and enter the camp briskly.' if not militarycamp_gate3:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I get off the horse and enter the camp briskly.')
                        jump prolcamp01entering01
                    'They don’t look like much of a threat. I can enter.' if militarycamp_gate3:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- They don’t look like much of a threat. I can enter.')
                        jump prolcamp01entering02

    label prolcamp01entering01: # I get off the horse and enter the camp briskly.
        if not tutorial_hp:
            $ tutorial_hp = 1
            $ pc_hp = limit_pc_hp(3)
            $ hpscreen = 1
        menu:
            'Your heavy boots hit the ground and the pain of the long ride finally catches up with you. You stretch out, bringing your back and legs comfort. All you want now is a table, a decent chair, a nice mug of beer, and some warm stew.
            \n\nWith any luck, your axe won’t be needed here.
            '
            'I approach the gate, ready to walk in.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the gate, ready to walk in.')
                $ tutorial_hp = 2
                show areapicture prologuemilitarycampscrap02withsack at basicfade
                menu:
                    'If it’s a military camp, it doesn’t look the part. Plenty of wasted space, the firepit is cold.
                    \n\n{color=#f6d6bd}Two people{/color} are sitting at the table, tired and disheartened. They’re looking in different directions, paying no attention to one another. One of them is holding a cup.
                    '
                    'I walk toward them.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk toward them.')
                        jump prolcamp01entering02

    label prolcamp01entering02:
        stop nature fadeout 6.0
        menu:
            'It takes them a few breaths to glance in your direction. The first person greets you with a wave of his hand. There are bags under his eyes, his beard is messy. Despite his simple shirt, he’s wearing durable, decent boots.
            \n\nA mace, with a head covered in iron, hangs at his side, but he doesn’t reach for it.
            '
            'I take a look at the second soul.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a look at the second soul.')
                menu:
                    'Just like you, she’s wearing a gambeson, but hers is a bit loose, as if she took it off a corpse. Her head is shaven, as if she’s protecting herself from flesh-eating bugs. Her eyes are weary, yet kind. She smiles.
                    \n\nConsidering the squad was sent here half a year ago, these two surely look the part. Though there should be more of them. Eight, you believe.
                    '
                    'I let them speak first.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I let them speak first.')
                        menu:
                            '“It’s nice to see an unharmed traveler in this godforsaken shithole, makes me just a tiny bit hopeful.” {color=#f6d6bd}The bearded man’s{/color} voice is strong, yet timid. “You’ll be staying the night with us, I guess.”
                            \n\n“We’re soldiers, he and I,” adds {color=#f6d6bd}the armored woman{/color}. Her voice switches from half-asleep to relaxed. “We’ll do our best to keep the camp safe, but if you were to take the first watch, it would be a huge help. Travelers ought to help each other, wouldn’t you say?”
                            \n\nYou think for a moment. To fully rest, you’d need a good sleep.
                            '
                            '“Sure, leave it to me.”':
                                $ tulia_friendship += 1
                                $ militarycamp_firstwatch = 1
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Sure, leave it to me.”')
                                menu:
                                    '“Fantastic,” she rubs her hands together. “I don’t remember the last time I had more than half a night of sleep. The hours before midnight should be the calmest, just wake us up if anything happens.”
                                    \n\n{color=#f6d6bd}The man{/color} flashes you a wide smile. “It’s easy to wake us up. Just yell,” he drinks from his mug.
                                    '
                                    'I ask them about their lieutenant.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask them about their lieutenant.')
                                        jump prolcamp01enteringaskingforlieutenant
                            '“I’m exhausted.”':
                                $ militarycamp_firstwatch -= 1
                                $ tulia_friendship -= 1
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m exhausted.”')
                                menu:
                                    '{color=#f6d6bd}The man{/color} looks away. “If you say so. Though better keep your axe nearby. The nights here can get spooky.”
                                    \n\n“I’d say {i}sinister{/i},” the other soldier snorts.
                                    '
                                    'I ask them about their lieutenant.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask them about their lieutenant.')
                                        jump prolcamp01enteringaskingforlieutenant
                    'I ask them about their lieutenant.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask them about their lieutenant.')
                        jump prolcamp01enteringaskingforlieutenant

###########################################
label prolcamp01enteringaskingforlieutenantALL:
    label prolcamp01enteringaskingforlieutenant:
        $ attitudes = 1
        $ at_activate = 1
        $ at = 0
        $ tutorial_attitudes = 1
        menu:
            'You wonder how to phrase your question.
            '
            ' (disabled)' ( condition="at == 0" ):
                pass
            '“I was hoping to meet with your lieutenant. Could we talk for a bit?”' ( condition="at == 'friendly'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='(friendly) - “I was hoping to meet with your lieutenant. Could we talk for a bit?”')
                $ at_activate = 0
                $ at = 0
                $ tutorial_attitudes = 0
                $ tulia_attitude = "friendly"
                jump prolcamp01lookingfora
            '“I’m sure you’re busy, so if you could just introduce me to your lieutenant...”' ( condition="at == 'playful'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='(playful) - “I’m sure you’re busy, so if you could just introduce me to your lieutenant...”')
                $ at_activate = 0
                $ at = 0
                $ tutorial_attitudes = 0
                $ tulia_attitude = "playful"
                jump prolcamp01lookingforb
            '“I’m looking for your lieutenant.”' ( condition="at == 'distanced'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='(distanced) - “I’m looking for your lieutenant.”')
                $ at_activate = 0
                $ at = 0
                $ tutorial_attitudes = 0
                $ tulia_attitude = "distanced"
                jump prolcamp01lookingforc
            '“I’d rather speak with someone who’s not going to waste my time.”' ( condition="at == 'intimidating'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='(intimidating) - “I’d rather speak with someone who’s not going to waste my time.”')
                $ at_activate = 0
                $ at = 0
                $ tutorial_attitudes = 0
                $ tulia_attitude = "intimidating"
                jump prolcamp01lookingford
            '“I had a long journey. I need to have a word with your lieutenant.”' ( condition="at == 'vulnerable'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='(vulnerable) - “I had a long journey. I need to have a word with your lieutenant.”')
                $ at_activate = 0
                $ at = 0
                $ tutorial_attitudes = 0
                $ tulia_attitude = "vulnerable"
                jump prolcamp01lookingfore

    label prolcamp01lookingfora: #“I was hoping to meet with your lieutenant. Could we talk for a bit?”
        $ at_activate = 0
        $ tulia_friendship += 1
        $ tutorial_attitudes_gray = 1
        menu:
            '{color=#f6d6bd}The woman{/color} lets out a loud sigh, dusts off her gambeson, and steps toward you. She pays little attention to the sword at her side.
            \n\n“We most definitely can, you and I, though holding this rank is still somewhat new to me. Are you a messenger? Did you lose your mount?” She observes you with curiosity. “Or are you looking for help?”
            '
            '“I’m your new roadwarden. My horse is waiting outside.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m your new roadwarden. My horse is waiting outside.”')
                jump prolcamp01lookingforb02

    label prolcamp01lookingforb: #“I’m sure you’re busy, so if you could just introduce me to your lieutenant...”
        $ at_activate = 0
        $ tulia_friendship += 1
        $ tutorial_attitudes_gray = 1
        menu:
            '{color=#f6d6bd}The armored soldier{/color} spares you a polite smile. “Next time better schedule a meeting. This place gets really crowded these days,” she stands up. She pays little attention to the sword at her side.
            \n\n“I figured you aren’t here on a walk. Let’s say it’s me you need to speak with. Are you a messenger? Did you lose your mount? Or are you looking for help?”
            '
            '“I’m your new roadwarden. My horse is waiting outside.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m your new roadwarden. My horse is waiting outside.”')
                label prolcamp01lookingforb02:
                    $ tutorial_attitudes_gray = 0
                    menu:
                        '“Really!” {color=#f6d6bd}The soldier in the shirt{/color} leans forward. “That explains how you got here in one piece, all by yourself!”
                        \n\n“Better bring your beast here,” adds {i}the lieutenant{/i}. “We have no hay, but I bet it dreams of dropping its saddle.” A long pause. “I’m {color=#f6d6bd}Tulia{/color}, by the way.”
                        \n\nShe reaches out her hand.
                        '
                        'I shake her hand. “I’m...”':
                            python:
                                pcname = renpy.input("How do you want people to call you?", default="Leto", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                                pcname = pcname.strip()
                                pcname_reduced = pcname.strip().lower().replace(" ", "")
                                if not pcname:
                                    pcname = "Leto"
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shake her hand. “I’m %s.”' %pcname)
                            jump prolcamp01greetingwithhandshake
                        'It may be a trap. I gesture for her to stop, pretending to be embarrassed. “I should wash myself first. But you can call me...”':
                            python:
                                pcname = renpy.input("How do you want people to call you?", default="Leto", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                                pcname = pcname.strip()
                                pcname_reduced = pcname.strip().lower().replace(" ", "")
                                if not pcname:
                                    pcname = "Leto"
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It may be a trap. I gesture for her to stop, pretending to be embarrassed. “I should wash myself first. But you can call me %s.”' %pcname)
                            jump prolcamp01greetingnohandshakefriendly

    label prolcamp01lookingforc: #“I’m looking for your lieutenant.”
        $ at_activate = 0
        $ tutorial_attitudes_gray = 1
        menu:
            '{color=#f6d6bd}The woman{/color} stands up, dusts off her gambeson, adjusts the sword at her side, and rests her hand on the hilt. Her shoulders are straight, her eyes attentive.
            \n\n“It’d be me, traveler. Are you in trouble?”
            '
            '“I’m fine. I’m your new roadwarden.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m fine. I’m your new roadwarden.”')
                $ tutorial_attitudes_gray = 0
                menu:
                    '“I took you for a wayfarer, to be honest.” When you mention that your mount is waiting outside, she raises an eyebrow. “Shouldn’t you unsaddle it? I bet it’s tired.”
                    \n\nShe glances at the gate, then at her companion. Her voice drops the slightest sign of weariness. “I expect you’re looking for directions. I’ll help you as much as I can.” She reaches out to you. “{color=#f6d6bd}Lieutenant Tulia{/color}.”
                    '
                    'I shake her hand. “I’m...”':
                        python:
                            pcname = renpy.input("How do you want people to call you?", default="Leto", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                            pcname = pcname.strip()
                            pcname_reduced = pcname.strip().lower().replace(" ", "")
                            if not pcname:
                                pcname = "Leto"
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shake her hand. “I’m %s.”' %pcname)
                        jump prolcamp01greetingwithhandshake
                    'It may be a trap. I gesture for her to stop, pretending to be embarrassed. “I should wash myself first. But you can call me...”':
                        python:
                            pcname = renpy.input("How do you want people to call you?", default="Leto", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                            pcname = pcname.strip()
                            pcname_reduced = pcname.strip().lower().replace(" ", "")
                            if not pcname:
                                pcname = "Leto"
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- It may be a trap. I gesture for her to stop, pretending to be embarrassed. “I should wash myself first. But you can call me %s.”' %pcname)
                        jump prolcamp01greetingnohandshakefriendly
                    'I don’t shake her hand. “I’m...”':
                        python:
                            pcname = renpy.input("How do you want people to call you?", default="Leto", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                            pcname = pcname.strip()
                            pcname_reduced = pcname.strip().lower().replace(" ", "")
                            if not pcname:
                                pcname = "Leto"
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t shake her hand. “I’m %s.”' %pcname)
                        jump prolcamp01greetingnohandshake

    label prolcamp01lookingford:#“I’d rather speak with someone who’s not going to waste my time.”
        $ at_activate = 0
        $ tulia_friendship -= 1
        $ tutorial_attitudes_gray = 1
        menu:
            '“What’s up with the tone?” {color=#f6d6bd}The man{/color} scowls at you, though he doesn’t reach for his mace. “We’ve nothing against you.”
            \n\n“Just ignore it,” adds {color=#f6d6bd}the second soldier{/color}, turning toward you. “it’s me you need to speak with. Are you a mercenary?”
            '
            '“I’m your new roadwarden.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m your new roadwarden.”')
                $ tutorial_attitudes_gray = 0
                menu:
                    '“Are you now? That explains {i}a bit{/i}. As long as you keep the roads safe from goblins and wolves, it doesn’t matter that you’re an apeass.”
                    \n\nShe stands up, resting her hand on the hilt of her sword. “Where’s your mount, roadwarden?”
                    '
                    '“Waiting outside.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Waiting outside.”')
                        if tulia_friendship <= 0:
                            menu:
                                '“So unsaddle it before it falls asleep,” she glances at the gate, then at her companion. Her voice is strong, her shoulders straight.
                                \n\n“I expect you’re looking for directions. I’m lieutenant {color=#f6d6bd}Tulia{/color}.”
                                '
                                '“I’m...”':
                                    python:
                                        pcname = renpy.input("How do you want people to call you?", default="Leto", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                                        pcname = pcname.strip()
                                        pcname_reduced = pcname.strip().lower().replace(" ", "")
                                        if not pcname:
                                            pcname = "Leto"
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m...”')
                                    jump prolcamp01greetingnohandshakenogiven
                        else:
                            menu:
                                '“So unsaddle it before it falls asleep,” she glances at the gate, then at her companion. Her voice is strong, her shoulders straight.
                                \n\n“I expect you’re looking for directions. I’ll help you as much as I can.” She reaches out to you. “Lieutenant {color=#f6d6bd}Tulia{/color}.”
                                '
                                'I shake her hand. “I’m...”':
                                    python:
                                        pcname = renpy.input("How do you want people to call you?", default="Leto", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                                        pcname = pcname.strip()
                                        pcname_reduced = pcname.strip().lower().replace(" ", "")
                                        if not pcname:
                                            pcname = "Leto"
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shake her hand. “I’m %s.”' %pcname)
                                    jump prolcamp01greetingwithhandshake
                                'I don’t shake her hand. “I’m...”':
                                    python:
                                        pcname = renpy.input("How do you want people to call you?", default="Leto", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                                        pcname = pcname.strip()
                                        pcname_reduced = pcname.strip().lower().replace(" ", "")
                                        if not pcname:
                                            pcname = "Leto"
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t shake her hand. “I’m %s.”' %pcname)
                                    jump prolcamp01greetingnohandshake

    label prolcamp01lookingfore: #“I had a long journey. I need to have a word with your lieutenant.”
        $ at_activate = 0
        $ tutorial_attitudes_gray = 1
        $ tulia_about_tired += 1
        menu:
            '{color=#f6d6bd}The woman{/color} stands up and approaches you. She pays little attention to the sword at her side. Her shoulders are straight, eyes worried.
            \n\n“It’d be me, traveler. Are you in trouble? There’s only the two of us here, but if you’re lost, we’ll take you to the nearby inn, right after sunrise.”
            '
            '“Actually, I’m your new roadwarden.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Actually, I’m your new roadwarden.”')
                $ tutorial_attitudes_gray = 0
                menu:
                    '“Really!” {color=#f6d6bd}The soldier in the shirt{/color} leans forward. “That explains how you got here in one piece, all by yourself!”
                    \n\n“Though you look exhausted,” adds {color=#f6d6bd}the other soul{/color}. “Don’t you have a mount?”
                    '
                    '“I’ve a horse. It’s waiting outside.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve a horse. It’s waiting outside.”')
                        menu:
                            '“Shouldn’t you unsaddle it? I bet it’s tired.” A long pause. “I assume you’re here not to meet our lieutenant, but rather to get some directions. I’m {color=#f6d6bd}Tulia{/color}, and I’ll be happy to help.”
                            \n\nShe reaches out to you.
                            '
                            'I shake her hand. “I’m...”':
                                python:
                                    pcname = renpy.input("How do you want people to call you?", default="Leto", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                                    pcname = pcname.strip()
                                    pcname_reduced = pcname.strip().lower().replace(" ", "")
                                    if not pcname:
                                        pcname = "Leto"
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shake her hand. “I’m %s.”' %pcname)
                                jump prolcamp01greetingwithhandshake
                            'It may be a trap. I step back. “I’m...”':
                                python:
                                    pcname = renpy.input("How do you want people to call you?", default="Leto", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                                    pcname = pcname.strip()
                                    pcname_reduced = pcname.strip().lower().replace(" ", "")
                                    if not pcname:
                                        pcname = "Leto"
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It may be a trap. I step back. “I’m %s.”' %pcname)
                                jump prolcamp01greetingnohandshake

################################## HANDSHAKE + HORSE (CLASS SELECTION)
label prolcamp01greetinghandshakeALL:
    label prolcamp01greetingwithhandshake:
        $ tulia_friendship += 1
        menu:
            'Her grasp is confident, the shake is slight. “Just keep your horse away from the tents,” she steps away. “We don’t need to smell its dung.”
            \n\n“Ah, there’s this one issue,” {color=#f6d6bd}the soldier in the shirt{/color} also rises to his feet. “We’ve no tent to spare. You’ll have to use a blanket or something.”
            '
            '“No problem, I enjoy observing the stars.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “No problem, I enjoy observing the stars.”')
                jump prolcamp01goingforhorse
            '“I should get used to sleeping on the ground anyway.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I should get used to sleeping on the ground anyway.”')
                jump prolcamp01goingforhorse

    label prolcamp01greetingnohandshakefriendly:
        menu:
            '{color=#f6d6bd}The lieutenant{/color} stands with her hand out, but then raises her arms with an awkward smile. “Of course, of course. Just keep your horse away from the tents,” she steps away. “We don’t need to smell its dung.”
            \n\n“We should also prepare for the night,” {color=#f6d6bd}the soldier in the shirt{/color} also rises to his feet. “We’ve no tent to spare. You’ll have to use a blanket or something.”
            '
            '“That’s fine.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s fine.”')
                jump prolcamp01goingforhorse
            '“I should get used to sleeping on the ground anyway.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I should get used to sleeping on the ground anyway.”')
                jump prolcamp01goingforhorse

    label prolcamp01greetingnohandshake:
        $ tulia_friendship -= 1
        menu:
            '{color=#f6d6bd}The lieutenant{/color} stands with her hand awkwardly reached out. After a few breaths she crosses her arms, and the air gets a bit colder. “You better bring your horse now. We’ll talk later.”
            \n\n{color=#f6d6bd}The soldier{/color} gives you a sullen glance. “You’ll have to sleep on the ground, under the stars. No tents.”
            '
            '“I need to get used to it anyway.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to get used to it anyway.”')
                jump prolcamp01goingforhorse
            'I walk away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk away.')
                jump prolcamp01goingforhorse

    label prolcamp01greetingnohandshakenogiven:
        menu:
            '{color=#f6d6bd}The lieutenant{/color} nods and crosses her arms. “Well. Let’s talk after you bring your beast.”
            \n\n“We should also prepare for the night,” {color=#f6d6bd}the soldier in the shirt{/color} also rises to his feet. “You’ll have to sleep on the ground, under the stars.”
            '
            '“That’s fine with me.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s fine with me.”')
                jump prolcamp01goingforhorse
            '“I need to get used to it anyway.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to get used to it anyway.”')
                jump prolcamp01goingforhorse
            'I walk away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk away.')
                jump prolcamp01goingforhorse

##############################################
label prolcamp01goingforhorseALL:
    label prolcamp01goingforhorse:
        menu:
            'You walk through the gate. Your mount looks around, and snorts anxiously.
            \n\nNot many humans could ride a horse. It’s not only taller than you, but also bulky, as heavy as it is strong. You can get in the saddle within a single breath, but most people wouldn’t know where to even begin. From every side, it’s a wall of flesh.
            \n\nHorses were brought to The Dragonwoods from the conquests in the South. They can trot for a long time, but won’t outrun some of the local monsters. Your palfrey needs you to survive - but without it, you too would be lost.
            '
            'It’s my only companion here. I want it to feel at ease.':
                $ pc_likeshorsename = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s my only companion here. I want it to feel at ease.')
                menu:
                    'It takes a few steps toward you, scolding you with another snort. You scratch the bottom of its neck, with strength and confidence, just the way it likes it.
                    \n\nHumans see useful animals, and even pets, as monsters in disguise. Getting emotionally attached to them is believed to lead humans to their doom.
                    \n\nBut {i}you{/i} know that horses {i}need{/i} companionship.
                    '
                    'I speak to it gently and lead it to the camp.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I speak to it gently and lead it to the camp.')
                        jump prolcamp01goingforhorse03
            'I don’t care how it feels, but I need it to be strong if I want to travel. And I can’t afford another one.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t care how it feels, but I need it to be strong if I want to travel. And I can’t afford another one.')
                menu:
                    'It keeps watching its surroundings, ignoring your approach. You clear your throat and reach out for the reins, and only then the beast responds with a stomp of its leg.
                    \n\nHumans see useful animals, and even pets, as monsters in disguise. Getting emotionally attached to them is believed to lead humans to their doom.
                    '
                    'I lead it to the camp.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lead it to the camp.')
                        jump prolcamp01goingforhorse03

    label prolcamp01goingforhorse03:
        menu:
            'You end up next to the firepit. Removing the saddle makes the horse nicker with relief. You take a couple of minutes to examine its back, just in case. While the riding equipment is not that heavy for such a strong animal, with enough time it starts to chafe.
            \n\nYou wish it had something better to eat than this shabby grass. You should look for an inn.
            '
            'I need to unpack.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I need to unpack.')
                jump prolcamp01goingforhorse04

    label prolcamp01goingforhorse04:
        menu:
            'You haven’t brought that many things, and you lost one of the sacks while fleeing the crimson corpse eaters. Worst of all, you have no rope left, but maybe the soldiers could share one. Shouldn’t cost more than a dragon bone.
            \n\nAside from the travel set, you own a few valuable possessions, essential for your trade.
            '
            '[[{color=#f6d6bd}Fighter{/color}] I spent my savings on decent combat equipment. I have a fine gambeson, an axe made of steel, and a reliable crossbow with quarrels.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- [[{color=#f6d6bd}Fighter{/color}] I spent my savings on decent combat equipment. I have a fine gambeson, an axe made of steel, and a reliable crossbow with quarrels.')
                $ item_crossbow = 1
                $ item_crossbowquarrels += 3
                $ armor = limit_armor(armor+3)
                $ item_axe02 = 1
                $ pc_class = "warrior"
                jump prolcamp01goingforhorse04b
            '[[{color=#f6d6bd}Mage{/color}] I have talismans that help me use my powers, as well as an iron axe and a worn gambeson.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- [[{color=#f6d6bd}Mage{/color}] I have talismans that help me use my powers, as well as an iron axe and a worn gambeson.')
                $ pc_class = "mage"
                $ armor = limit_armor(armor+2)
                $ item_axe01 = 1
                $ item_mageamulets = 1
                $ mana = 3
                jump prolcamp01goingforhorse04b
            # '[[{color=#f6d6bd}Scholar{/color}] I carry writing instruments and alchemical ingredients, as well as an iron axe and a worn gambeson.':
            #     $ narrator.add_history(kind='nvl', who=narrator.name, what='- [[{color=#f6d6bd}Scholar{/color}] I carry writing instruments and alchemical ingredients, as well as an iron axe and a worn gambeson.')
            #     $ pc_class = "scholar"
            #     $ armor = limit_armor(armor+2)
            #     $ item_axe01 = 1
            #     $ item_scholaringredients = 1
            #     $ item_writinginstruments = 1
            #     jump prolcamp01goingforhorse04b
            '[[{color=#f6d6bd}Scholar{/color}] I carry writing instruments and alchemical ingredients, as well as an iron axe, a worn gambeson, and a small healing potion.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- [[{color=#f6d6bd}Scholar{/color}] I carry writing instruments and alchemical ingredients, as well as an iron axe, a worn gambeson, and a healing potion.')
                $ pc_class = "scholar"
                $ armor = limit_armor(armor+2)
                $ item_axe01 = 1
                $ item_smallhealingpotion += 1
                $ item_scholaringredients = 1
                $ item_writinginstruments = 1
                jump prolcamp01goingforhorse04b
            'I want to learn more about the three classes.' ( condition="persistent.tutorial_display" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='-I want to learn more about the three classes.')
                menu:
                    'As {color=#f6d6bd}a fighter{/color}, you’ll have an easier time in physical challenges, thanks to your superior equipment and hidden bonuses during dice rolls. You’ll be physically more capable than the other classes, what opens unique opportunities during some social interactions. It’s the best class for RPG beginners.
                    \n{color=#f6d6bd}The fighter’s{/color} weakness is their reliance on physical strength. Your special abilities won’t be available to you if your vitality points drop to 0.
                    \n\n{color=#f6d6bd}The mage{/color} uses {i}pneuma{/i}, a versatile, but limited pool of energy points that can be spent to cast a few humble spells. Magic won’t protect you better than a sharp axe, but as a mage, you’ll be able to heal faster while resting; detect magic in a mysterious area; distract a beast with a simple trick; and find a common tongue with other magic users.
                    \nUsing {color=#f6d6bd}the mage’s{/color} powers too freely will result in having no {i}pneuma{/i} left when you need it the most.
                    \n\n{color=#f6d6bd}The scholar{/color} will know more about the world’s mysteries than you, helping you take advantage of some unusual situations. Your character will impress the locals with its knowledge, and you’ll be able to read the sparse, written clues without anyone’s assistance.
                    \n{color=#f6d6bd}Scholars{/color} struggle with combat more than the other classes, but with enough carefulness and exploration, you’ll gain access to alchemical mixtures that will help you escape from many dangerous situations.
                    '
                    'I’ll be {color=#f6d6bd}a fighter{/color}.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll be {color=#f6d6bd}a fighter{/color}.')
                        $ item_crossbow = 1
                        $ item_crossbowquarrels += 3
                        $ armor = limit_armor(armor+3)
                        $ item_axe02 = 1
                        $ pc_class = "warrior"
                        jump prolcamp01goingforhorse04b
                    'I pick {color=#f6d6bd}the mage{/color}.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pick {color=#f6d6bd}the mage{/color}.')
                        $ pc_class = "mage"
                        $ armor = limit_armor(armor+2)
                        $ item_axe01 = 1
                        $ item_mageamulets = 1
                        $ mana = 3
                        jump prolcamp01goingforhorse04b
                    'I’d like to play as {color=#f6d6bd}a scholar{/color}.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’d like to play as {color=#f6d6bd}a scholar{/color}.')
                        $ pc_class = "scholar"
                        $ armor = limit_armor(armor+2)
                        $ item_axe01 = 1
                        $ item_smallhealingpotion += 1
                        $ item_scholaringredients = 1
                        $ item_writinginstruments = 1
                        jump prolcamp01goingforhorse04b
                    # 'I’d like to play as {color=#f6d6bd}a scholar{/color}.':
                    #     $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’d like to play as {color=#f6d6bd}a scholar{/color}.')
                    #     $ pc_class = "scholar"
                    #     $ armor = limit_armor(armor+2)
                    #     $ item_axe01 = 1
                    #     $ item_scholaringredients = 1
                    #     $ item_writinginstruments = 1
                    #     jump prolcamp01goingforhorse04b

    label prolcamp01goingforhorse04b:
        $ tutorial_inventory = 1
        $ isinventory = 1
        $ tutorial_armor = 1
        $ armorscreen = 1
        $ quarters += 1
        menu:
            'You unpack and inspect your belongings. Your water skin isn’t pierced, the spare clothes are still here. Just in case, you take a look at your wooden bowl and mug, your cape, tinder box, bandages, food rations, knife... Nothing special or too cumbersome.
            \n\nFrom time to time your routine helps you avoid mistakes, but this doesn’t make it any more exciting.
            '
            'I return to the soldiers.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the soldiers.')
                $ tutorial_inventory = 0
                $ tutorial_armor = 0
                if tulia_friendship > 0:
                    jump prolcamp01goingforhorse05
                else:
                    jump prolcamp01goingforhorse05b

    label prolcamp01goingforhorse05:
        menu:
            'They’re at the table again, observing your beast and chatting between themselves. Your stomach growls at the sight of them eating out of wooden bowls.
            \n\nOne more bowl was put at a previously unused end of the table. You can sit down on a tree log.
            '
            'I join them and take a look at the meal.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I join them and take a look at the meal.')
                jump prolcamp01goingforhorse06
            'I thank them for the meal, but I don’t want to eat with them. I sit down and ask {color=#f6d6bd}Tulia{/color} what she can tell me about this area.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I thank them for the meal, but I don’t want to eat with them. I sit down and ask {color=#f6d6bd}Tulia{/color} what she can tell me about this area.')
                jump prolcamp01atthetable
            'I completely ignore the meal. I sit down and speak to {color=#f6d6bd}Tulia{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I completely ignore the meal. I sit down and speak to {color=#f6d6bd}Tulia{/color}.')
                $ tulia_friendship -= 1
                jump prolcamp01atthetable

    label prolcamp01goingforhorse05b:
        menu:
            'They’re at the table again, observing your beast and chatting between themselves. Your stomach growls at the sight of them eating out of wooden bowls.
            \n\nThere’s no meal for you, but you can sit down on a tree log.
            '
            'I take some of my own rations.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take some of my own rations.')
                jump prolcamp01goingforhorse06b
            'I don’t want to eat with them. I sit down and ask {color=#f6d6bd}Tulia{/color} what she can tell me about this area.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t want to eat with them. I sit down and ask {color=#f6d6bd}Tulia{/color} what she can tell me about this area.')
                jump prolcamp01atthetable

    label prolcamp01goingforhorse06:
        $ tutorial_eating = 1
        $ foodscreen = 1
        $ pc_food_gruel +=1
        menu:
            'It’s cold gruel, the meal eaten in times of hardship. This specific bowl is filled with water, hog millet, some strange-looking cereals, and blueberries.
            \n\nWelcoming you with a meal, even a humble one, is beyond their duty. Soldiers live with and for their companions, constantly on the move from one part of the realm to another, making sacrifices to protect their group as they face dozens of hideous creatures. Their lives are filled with discipline, hardship, and camaraderie.
            \n\nRoadwardens, on the other hand, learn how to work by themselves. They seldom engage in open combat, patrolling the same roads for years. They help the settlements stay in touch, but also maintain commerce, settle down, forge friendships. When there are no laws to follow, they use their own judgment.
            \n\nDifferent responsibilities. Different lifestyles.
            '
            'I eat quickly, not focusing on the taste, then speak with {color=#f6d6bd}Tulia{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='I eat quickly, not focusing on the taste, then speak with {color=#f6d6bd}Tulia{/color}.')
                $ tutorial_eating = 2
                $ pc_food = limit_pc_food(pc_food+1)
                show plus1food at foodchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 nourishment point.{/i}')
                jump prolcamp01atthetable

    label prolcamp01goingforhorse06b:
        $ tutorial_eating = 1
        $ foodscreen = 1
        menu:
            'In the last inn you got a smelling loaf of dark bread, decorated with sunflower seeds. It tastes great, even by itself.
            \n\nWhen on the road, most people have to think about themselves. Soldiers live with and for their companions, constantly on the move from one part of the realm to another, making sacrifices to protect their group as they face dozens of hideous creatures. Their lives are filled with discipline, hardship, and camaraderie.
            \n\nRoadwardens, on the other hand, learn how to work by themselves. They seldom engage in open combat, patrolling the same roads for years. They help the settlements stay in touch, but also maintain commerce, settle down, forge friendships. When there are no laws to follow, they use their own judgment.
            \n\nDifferent responsibilities. Different lifestyles.
            '
            'I eat slowly, enjoying myself. In the meantime, I speak with {color=#f6d6bd}Tulia{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I eat slowly, enjoying myself. I speak with {color=#f6d6bd}Tulia{/color}.')
                $ pc_food = limit_pc_food(pc_food+2)
                show plus2food at foodchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 nourishment points.{/i}')
                $ item_rations = limit_item_rations(item_rations-1)
                jump prolcamp01atthetable

##################################
label prolcamp01atthetable:
    $ quarters += 1
    if not tutorial_eating:
        $ tutorial_eating = 1
        $ foodscreen = 1
    if tulia_friendship > 0:
        $ custom1 = "“I’m afraid I can tell you less than I would like to and less than I should.”"
    else:
        $ custom1 = "“I can only say as much as I know, and that’s not much.”"
    menu:
        'She’s focused and chooses her words carefully. She looks away only when she gathers her thoughts.
        \n\n[custom1] She nods toward the other soldier. “As you can see, there’s not a lot of us left. At the beginning of summer there were eight of us, including our previous lieutenant. Five are dead, one has run away in tears.”
        \n\n“We’re also strangers in this land,” adds {color=#f6d6bd}her companion{/color}.
        '
        '“Any piece of information may help me do my job.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any piece of information may help me do my job.”')
            $ tutorial_eating = 2
            menu:
                '{color=#f6d6bd}The man{/color} leans forward, his legs shake nervously. He sounds like a kid asking a bard to sing one more story, tell a joke, or do a magic trick. Whatever it takes to escape from boredom. His untrimmed beard hides a much younger face than you originally thought.
                \n\n“What did the officials tell you? I expect not that much, no soul governs these lands.”
                '
                'I share what I consider to be relevant.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I share what I consider to be relevant.')
                    menu:
                        'You tell the soldiers how little guidance you’ve received. Since this area is too far away from {color=#f6d6bd}Hovlavan{/color} to keep it under control, you were warned that it’s untamed and unknown.
                        \n\nWho knows how many villages, bandits, or monsters may be found in these unmapped hills and forests. From time to time, new people come here to look for boundless opportunities. Most of them never return. Do they turn into walking corpses, or find what they’re looking for?
                        '
                        '“No soul could tell me, so I was looking for your guidance.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “No soul could tell me, so I was looking for your guidance.”')
                            jump prolcamp01questions01
                '“What I’ve discussed with the officials should stay between me and them.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What I’ve discussed with the officials should stay between me and them.”')
                    menu:
                        'You think how unprepared you are for this task. Since this area is too far away from {color=#f6d6bd}Hovlavan{/color} to keep it under control, you were warned that it’s untamed and unknown.
                        \n\nWho knows how many villages, bandits, or monsters may be found in these unmapped hills and forests. It’s a place of both danger and opportunity.
                        '
                        'A great realm to spend the rest of summer.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- A great realm to spend the rest of summer.')
                            menu:
                                '“Actually, I’d prefer to keep it that way,” says {color=#f6d6bd}Tulia{/color}. “The less you tell us, the smaller the chance that the commanders will send us here again,” there’s bitterness in her brief laughter. “I’m fine with a soldier’s life, you know. I just hope to find an outpost where I won’t have to bid farewell to most people I know.”
                                '
                                '“It’s understandable.”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s understandable.”')
                                    jump prolcamp01questions01
                                'I don’t say anything.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t say anything.')
                                    jump prolcamp01questions01

################################## QUESTIONS
label prolcamp01questions01:
    $ questionpreset = "tulia1"
    menu:
        '{color=#f6d6bd}The lieutenant{/color} drinks from her cup and crosses her legs, ankle-on-knee. Seeing her chair makes you doubt she’ll ever find a comfortable position.
        \n\n“Where should we start?”
        '
        '(tulia1 set)':
            pass

label tulia_about_peninsulaALL:
    label tulia_about_peninsula:
        $ tulia_about_peninsula += 1
        $ tulia_questions_main += 1
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What should I know about the peninsula?”')
        if tutorial_journal == 1:
            $ tutorial_journal = 2
        menu:
            '“I’ll tell you what {i}I{/i} know, and you’ll be the judge,” says {color=#f6d6bd}the lieutenant{/color}. “How long did it take you to get here from the city? On a decent palfrey, I’d guess it would be... three, four days?” When you confirm, she continues. “From here, you can reach the coast in about a day, as long as you don’t make any stops. Do you know the situation? Why no ships can get here?”
            \n\nYou nod. The sea route allows {color=#f6d6bd}Hovlavan{/color} officials to keep in touch with the coastal villages - collect taxes, move the soldiers, collect lumber, deliver tools... But maintaining order on a wild coast, such as this one, is like filling the ocean depths with coins.
            '
            '“Because of the rocks. You can hardly stop a ship five miles from the shore, and boats can’t get much closer.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Because of the rocks. You can hardly stop a ship five miles from the shore, and boats can’t get much closer.”')
                menu:
                    'She nods. “I don’t know much about fishing, but there’s not that many people living by the shore. And they don’t crave to stay in touch with the cityfolk.”
                    \n\nAs she pauses, {color=#f6d6bd}her companion{/color} carries on. “No soul from the North ever came to the camp, but when we travel to the roadside inn, {color=#f6d6bd}Pelt of the North{/color}, they’re happy to trade. And to play dice.”
                    '
                    '“Why not just stay at one of the settlements?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why not just stay at one of the settlements?”')
                        menu:
                            '{color=#f6d6bd}The man{/color} clears his throat. “I mean, you know. We’re to guard this road, this camp is our post. And, well,” he turns toward {color=#f6d6bd}Tulia{/color}. She lowers her voice.
                            \n\n“Don’t take it the wrong way, [pcname], but... Are you a devout soul?”
                            '
                            'Like most cityfolk, I believe that people should unite their strength to overcome the threats of nature and dark magic. Everyone will be judged for both good and evil deeds. “I’m a part of {color=#f6d6bd}The United Church{/color}.”':
                                $ pc_religion = "theunitedchurch"
                                $ item_wingedhourglass = 1
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Like most cityfolk, I believe that people should unite their strength to overcome the threat of nature and dark magic. Everyone will be judged for both good and evil deeds. “I’m a part of {color=#f6d6bd}The United Church{/color}.”')
                                $ tulia_friendship += 1
                                menu:
                                    '“A fellow Unite!” {color=#f6d6bd}The man{/color} smiles. “Though in this land it won’t bring you much good.”
                                    \n\n“At least we can discuss the topic freely,” adds {color=#f6d6bd}the lieutenant{/color} with a barely visible smile.
                                    '
                                    '“Let’s get into it.”':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s get into it.”')
                                        jump tulia_about_peninsulap04
                            'For many years I’ve supported a monastery that does its best to advance mankind’s spiritual growth, artistry, herbalism, and magical research. “I follow the teachings of {color=#f6d6bd}an Order of Truth{/color}.”':
                                $ pc_religion = "ordersoftruth"
                                $ item_wingedhourglass = 1
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- For many years I’ve supported a monastery that does its best to advance mankind’s spiritual growth, artistry, herbalism, and magical research. “I follow the teachings of {color=#f6d6bd}an Order of Truth{/color}.”')
                                jump tulia_about_peninsulap03b
                            'I’m from a small village. For me, the freedom of shell, pneuma, and soul are the main virtues of life. My community is unique and independent, and so are its members. “I have a place in {color=#f6d6bd}my fellowship{/color}.”':
                                $ pc_religion = "fellowship"
                                $ item_wingedhourglass = 1
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m from a small village. For me, the freedom of shell, pneuma, and soul are the main virtues of life. My community is unique and independent, and so are its members. “I have a place in {color=#f6d6bd}my fellowship{/color}.”')
                                label tulia_about_peninsulap03b:
                                    menu:
                                        '“Oh, I see,” she hesitantly looks away. “I don’t know much about that River of Faith, but I’m sure we’re not that different. I’m a Unite myself,” she says with a sort of pride in her voice. So she follows The United Church.
                                        '
                                        '“M-hm.”':
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “M-hm.”')
                                            jump tulia_about_peninsulap04
                                        '“Maybe just explain what you were thinking of.”':
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe just explain what you were thinking of.”')
                                            jump tulia_about_peninsulap04
                            'I have a strong connection to nature and spirits, and follow the path of my ancestors. Some of my beliefs may be considered sinister and treacherous by the cityfolk. “You’d probably call me {color=#f6d6bd}a pagan{/color}.”':
                                $ pc_religion = "pagan"
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I have a strong connection to nature and spirits, and follow the path of my ancestors. Some of my beliefs may be considered sinister and treacherous by the cityfolk. “You’d probably call me a {color=#f6d6bd}a pagan{/color}.”')
                                menu:
                                    '“A pagan roadwarden?” {color=#f6d6bd}The man{/color} scratches his head without the slightest subtlety.
                                    \n\n“Now, I... I’m sure we can have a conversation, we’re civilized people,” {color=#f6d6bd}the lieutenant{/color} clears her throat. “I’m from The United Church, but I’m not a priest or anything. And definitely not a zealot.”
                                    \n\nAn awkward pause. The United Church has spilled the blood of countless pagan tribes, making it clear that who’s not with them, is against them. Your family shared gruesome stories about the atrocities committed by the priests against your ancestors.
                                    '
                                    '“Sure. I’m not looking for squabbles.”':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Sure. I’m not looking for squabbles.”')
                                        jump tulia_about_peninsulap04
                                    'I frown in silence.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I frown in silence.')
                                        jump tulia_about_peninsulap04
                            'There’s no evidence of The Wright’s existence and all the {i}mystical{/i} tales are explained by magic. “No. I’m not.”':
                                $ pc_religion = "none"
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- There’s no evidence of The Wright’s existence and all the {i}mystical{/i} tales are explained by magic. “No. I’m not.”')
                                menu:
                                    '{color=#f6d6bd}The man{/color} nods. “I heard that most roadwardens drift away from the churches.”
                                    \n\n“It doesn’t matter to me, to neither of us, I think,” adds {color=#f6d6bd}the lieutenant{/color}, peeping at her companion. “I just wanted to make sure I won’t step on any... touchy subject.”
                                    '
                                    '“You won’t. Go ahead.”':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You won’t. Go ahead.”')
                                        jump tulia_about_peninsulap04
                            # '“You don’t need to know that.”':
                            #     $ pc_religion = "unknown"
                            #     $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t need to know that.”')
                            #     menu:
                            #         '“No, of course you don’t, it’s just,” she takes a moment to think. “I don’t want you to assume... I’m not one of those zealots who want everyone to think how they think, see how they see,” she grunts. “I may not agree with the choices that others make, but I’m not looking for holy wars against them, and I don’t hate anyone, or anything...” She keeps speaking faster.
                            #         '
                            #         '“What was it that led you to this question?”':
                            #             $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What was it that led you to this question?”')
                            #             jump tulia_about_peninsulap04

    label tulia_about_peninsulap04:
        if pc_religion == "fellowship":
            $ custom1 = ", like yourself.”"
        else:
            $ custom1 = ".” You nod. She means a fellowship."
        menu:
            '“The people here are... Disquieting.” Every few words, she taps the table with her finger. “Their traditions won’t help them negotiate with the officials. Here,” she starts to draw lines with her index finger, as if she’s pointing at an invisible map. “The peninsula is connected with roads, like a big circle. In the northwest, you’ll find a weird village at a bog. It’s not exactly pagan, I don’t think, it even has a priest who claims to be an Eremite[custom1]
            \n\n“They do crazy shit,” {color=#f6d6bd}her companion{/color} chips in. “They use the dead to cut down trees and dig in soil. Once I saw it, I begged to never return there.”
            '
            '“I see.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I see.”')
                $ quest_explorepeninsula_description02a = "Soldiers told me about a large village that repeatedly uses necromancy, even though it’s forbidden by law and can be extremely dangerous. I should take a look and judge for myself. The village is somewhere among the bogs, by the northwestern road."
                menu:
                    'You’ve heard tales such as this one since you were a child. If an isolated settlement manages to survive without a city’s influence, its customs and traditions grow more and more alien. Every generation learns how to adapt to the dangerous conditions they have to deal with, and the rustic, pagan traditions muddy their River of Faith.
                    \n\nThe United Church often warns its members about {i}the crazy druids{/i}, necromancers, and blood mages. {i}The bringers of doom, the traitors to humankind.{/i}
                    '
                    '“Were you able to speak with these necromancers?”' if not tulia_about_peninsula_bonusquestion1:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Were you able to speak with these necromancers?”')
                        jump tulia_about_peninsula_bonusquestion1
                    '“And how about the East?”' if not tulia_about_peninsula_bonusquestion2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And how about the East?”')
                        jump tulia_about_peninsula_bonusquestion2
                    '“Any monster worth mentioning? Anything that could catch my mount?”' if not tulia_about_peninsula_bonusquestion3:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any monster worth mentioning? Anything that could catch my mount?”')
                        jump tulia_about_peninsula_bonusquestion3
                    '“That’s all I need to know.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need to know.”')
                        jump militarycamp01afteressentialquestion01

    label tulia_about_peninsula_bonusquestion1: #“Were you able to speak with these necromancers?”
        $ tulia_about_peninsula_bonusquestion1 = 1
        menu:
            '“You can see why we were not eager to go there if we could avoid it,” {color=#f6d6bd}the lieutenant{/color} chuckles. “Maybe they’ll be more welcoming to a roadwarden. The roads are dangerous, with little to no shelters. People need your help.”
            \n\n{color=#f6d6bd}The man in the shirt{/color} turns a bit and points a finger to the northwest. “If you’re heading to the undead village, you’ll get to an inn first, and soon.”
            \n\n{color=#f6d6bd}Tulia{/color} nods. “{color=#f6d6bd}Pelt of the North{/color} is a safe place. You can talk with the innkeep or the guards, ask them about the road.”
            '
            '“Were you able to speak with these necromancers?”' if not tulia_about_peninsula_bonusquestion1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Were you able to speak with these necromancers?”')
                jump tulia_about_peninsula_bonusquestion1
            '“And how about the East?”' if not tulia_about_peninsula_bonusquestion2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And how about the East?”')
                jump tulia_about_peninsula_bonusquestion2
            '“Any monster worth mentioning? Anything that could catch my mount?”' if not tulia_about_peninsula_bonusquestion3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any monster worth mentioning? Anything that could catch my mount?”')
                jump tulia_about_peninsula_bonusquestion3
            '“That’s all I need to know.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need to know.”')
                jump militarycamp01afteressentialquestion01

    label tulia_about_peninsula_bonusquestion2: # “And how about the East?”
        $ tulia_about_peninsula_bonusquestion2 = 1
        menu:
            'She stares off across the camp. “Hard to tell, we went there only once. There are hills, forests, rivers. We saw a {i}tunnel{/i} sculpted in leaves and branches, but we didn’t enter it. Wilderness, all around.”
            '
            '“Were you able to speak with these necromancers?”' if not tulia_about_peninsula_bonusquestion1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Were you able to speak with these necromancers?”')
                jump tulia_about_peninsula_bonusquestion1
            '“And how about the East?”' if not tulia_about_peninsula_bonusquestion2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And how about the East?”')
                jump tulia_about_peninsula_bonusquestion2
            '“Any monster worth mentioning? Anything that could catch my mount?”' if not tulia_about_peninsula_bonusquestion3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any monster worth mentioning? Anything that could catch my mount?”')
                jump tulia_about_peninsula_bonusquestion3
            '“That’s all I need to know.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need to know.”')
                jump militarycamp01afteressentialquestion01

    label tulia_about_peninsula_bonusquestion3: # “Any monster worth mentioning? Anything that could catch my mount?”
        $ tulia_about_peninsula_bonusquestion3 = 1
        menu:
            '“We saw all sorts of beasts,” {color=#f6d6bd}the man{/color} starts to count on his fingers. “Goblins, treants, cats large and small, runners, howlers, wolves, spiked boars, mouflon eaters, griffons... But we managed to stay away.”
            \n\n“Some could catch up with most mounts.” {color=#f6d6bd}Tulia{/color} glances at her companion. “Though a palfrey {i}should{/i} be fine. The trees are so tall that the flying creatures keep to the coast and mountains. There’s not that many humans around, and the animals are busy fighting among themselves. They fight more for food than territory.”
            \n\n{color=#f6d6bd}The soldier{/color} cracks his knuckles. “Don’t provoke them and ride fast, just count on luck.”
            '
            '“Were you able to speak with these necromancers?”' if not tulia_about_peninsula_bonusquestion1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Were you able to speak with these necromancers?”')
                jump tulia_about_peninsula_bonusquestion1
            '“And how about the East?”' if not tulia_about_peninsula_bonusquestion2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And how about the East?”')
                jump tulia_about_peninsula_bonusquestion2
            '“Any monster worth mentioning? Anything that could catch my mount?”' if not tulia_about_peninsula_bonusquestion3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any monster worth mentioning? Anything that could catch my mount?”')
                jump tulia_about_peninsula_bonusquestion3
            '“That’s all I need to know.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I need to know.”')
                jump militarycamp01afteressentialquestion01

    label militarycamp01afteressentialquestion01:
        $ minutes += 6
        $ questionpreset = "tulia1"
        menu:
            'She nods. “I’m afraid we can’t do more for you.”
            '
            '(tulia1 set)':
                pass

label tulia_about_asterion1:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any ideas what happened to the previous roadwarden?”')
    $ description_asterion01 = "According to {color=#f6d6bd}Tulia{/color}, he was a bit of a recluse, constantly on the move, looking for work. Since he disappeared before summer, he may already be dead. His kids live near {color=#f6d6bd}Hovlavan{/color}."
    $ tulia_about_asterion1 += 1
    $ tulia_questions_main += 1
    if tutorial_journal == 1:
        $ tutorial_journal = 2
    menu:
        '{color=#f6d6bd}Tulia{/color} takes a deep breath. “Aren’t you a bit late for a rescue mission? We haven’t heard from him for almost half a year.” The soldiers speak for a bit between themselves, trying to get their story straight. They confirm that he had stopped by their camp a few times, but stopped showing up at all in early summer.
        \n\n{color=#f6d6bd}The bearded soldier{/color} starts to scratch the table with the tip of his knife, without looking at you. “I don’t remember his voice. Always busy, drowning in things to take care of. He would sit somewhere, sharpen his sword, fix his loud mail, clean clothes, write notes on that wax tablet of his.”
        \n\n“Yep, and leave at dawn. Unlike us, {color=#f6d6bd}Asterion{/color} never gets bored,” {color=#f6d6bd}Tulia{/color} lets out a joyless chuckle. “He’s secretive, but some of the locals speak about him warmly. Maybe he just doesn’t like us.”
        '
        '“Sounds like you’re not sure if he’s dead or not.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Sounds like you’re not sure if he’s dead or not.”')
            if not pc_likeshorsename:
                $ custom1 = "On the other hand, they enjoy attacking nearby targets a bit too much. "
            else:
                $ custom1 = "At least your palfrey is fast and reliable, and won’t suddenly sink its teeth into an innocent passerby."
            menu:
                '“If anyone knows, they won’t tell us. Maybe someone is keeping him in a basement,” {color=#f6d6bd}the man{/color} carves with passion. “We haven’t seen him, or his saurian. Something ate them, I bet. The officials have hired {i}you{/i}, right? They don’t expect him to return.”
                \n\nRicher roadwardens often use four-legged, meat-eating saurians as their mounts. They have to be tamed and trained since their hatching, but, unlike horses, can easily defend themselves from many monsters. [custom1]
                '
                '“Do you know what he was looking for? Maybe he left you a message?”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you know what he was looking for? Maybe he left you a message?”')
                    menu:
                        '“Neither one of us had any insight into his dealings,” says {color=#f6d6bd}Tulia{/color}. “My predecessor left me no clues. We also took a look at {color=#f6d6bd}Asterion’s{/color} stuff... Wait!” She raises her open palm. “I almost forgot.”
                        \n\nShe stands up and heads to a nearby tent. “He has kids, in a village near {color=#f6d6bd}Hovlavan{/color}. I was planning to take all his things there. A pouch, a second spear, a decent bow, some potions. Quite a treasure.” She glances at you. “But I would {i}much{/i} prefer to bring them the truth about their father.”
                        '
                        '“So you want me to find out what happened to him in exchange for his stuff?”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So you want me to find out what happened to him in exchange for his stuff?”')
                            $ description_tulia01 = "She plans to return to {color=#f6d6bd}Hovlavan{/color} in the near future."
                            menu:
                                '“Here’s the catch.” She dusts off the hilt of her sword. “We’ve hired a messenger to ask the commanders for further orders. Since she hasn’t returned and you know nothing about her, she either ran away or something happened to her,” she sighs with resignation. “We are meant to stay here until fall. What do you think? Come see us, tell us what you’ve learned about the man, and we’ll get back to {color=#f6d6bd}Hovlavan{/color} together?”
                                \n\nYou think about your {i}real{/i} mission. You were planning to return to {color=#f6d6bd}Hovlavan{/color} in the early fall anyway.
                                '
                                '“If he’s alive, I don’t think he’s going to be happy about me taking away all of his possessions.”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If he’s alive, I don’t think he’s going to be happy about me taking away all of his possessions.”')
                                    $ isjournal = 1
                                    $ quest_asterion = 1
                                    $ quest_asterion_description01 = "Before I became the roadwarden of this peninsula, a man known as {color=#f6d6bd}Asterion{/color} used to patrol these roads. If I manage to find out what happened to him and bring the news to {color=#f6d6bd}Tulia{/color} from the southern camp, I’ll receive his abandoned belongings." # {b}I have to return to her before the end of summer.{/b}
                                    $ tutorial_journal += 1
                                    $ renpy.notify("New journal entry: Find the Roadwarden")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New journal entry: Find the Roadwarden{/i}')
                                    $ minutes += 6
                                    $ questionpreset = "tulia1"
                                    menu:
                                        '“True, but he’s considered dead, I doubt he’d begrudge you anything. And who knows, you may just find his shell lying on the roadside tomorrow. He wears mail, uses a spear, mostly. Maybe five feet tall, but stout. Long, red beard, short hair. Pale face. Rarely smiles.”
                                        \n\nShe glances at her companion, but after he adds nothing, she sits down and stretches out her legs. “So find out what happened to him. Dead, alive, left - just let me know.”
                                        '
                                        '(tulia1 set)':
                                            pass

label militarycamp01askingabouttheropeALL:
    label militarycamp01askingabouttherope:
        show areapicture prologuemilitarycampscrap02 at basicfade
        $ shop = "tutorial"
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve lost my rope. Could you spare one?”')
        if tutorial_journal == 1:
            $ tutorial_journal = 2
        menu:
            '“You’re in luck,” she heads toward one of the crates and moves aside a large, linen sack, revealing a rope. She brings it back and nonchalantly sits down on her chair. “Take it. I was planning to leave it behind.”
            '
            'I take a closer look.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look.')
                show screen shopscreen() with dissolve
                $ questionpreset = "tulia1"
                menu:
                    'It’s an ordinary rope made of hemp, durable enough.
                    '
                    '(tulia1 set)':
                        pass

    label militarycamp01askingabouttherope03:
        $ questionpreset = "tulia1"
        $ minutes += 6
        menu:
            '{color=#f6d6bd}Tulia{/color} nods. For now, you leave the rope on the table.
            '
            '(tulia1 set)':
                pass

    label militarycamp01askingabouttherope03a:
        $ tulia_friendship += 1
        $ item_rations = limit_item_rations(item_rations-1)
        $ questionpreset = "tulia1"
        $ minutes += 6
        menu:
            '{color=#f6d6bd}Tulia{/color} leans forward and rests her forearms on her thighs, looking down with clasped hands, then meets your eyes. “I’d normally refuse, but we need some decent food. Every day I’m searching through our groats, looking for worms and putridity. We forage, but it’s not a great spot. Some food rations will brighten up a foggy day.”
            \n\nFor now, you leave the rope on the table.
            '
            '(tulia1 set)':
                pass

label tulia_about_hersquad:
    $ foragers_caius_heardabout += 1
    $ tulia_questions_side += 1
    $ tulia_about_hersquad += 1
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What happened to your squad?”')
    if tutorial_journal == 1:
        $ tutorial_journal = 2
    menu:
        '{color=#f6d6bd}The man{/color} shrugs. “Bandits happened. And monsters.”
        \n\n“A {i}strong{/i} band, though,” {color=#f6d6bd}his companion{/color} chips in. “When we got to the peninsula in spring, we saw some people living in this camp. The lieutenant decided to avoid it, and look for an inn. We had to travel through the night for a bit,” {color=#f6d6bd}the bearded soldier{/color} scoffs and crosses his arms, but she carries on. “If he had decided otherwise, we would all have died that day. {color=#f6d6bd}The innkeeper{/color} explained that the camp is a trap, that the armed ones pretend to be soldiers. Stay there at night, lose everything you have.”
        '
        '“Sounds like slave hunters.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Sounds like slave hunters.”')
            menu:
                '{color=#f6d6bd}Tulia{/color} sighs. “Very much so. They killed some, and took others away, who knows where. They were letting the northerners go, hoping to avoid their wrath.”
                \n\n“It kind of worked,” adds {color=#f6d6bd}the soldier{/color}. “We asked them for help, but they refused. We had to clear the entire camp on our own, and that’s why three of our people died.”
                \n\n“Don’t exaggerate, it’s not like the lieutenant didn’t make a mistake. He wanted to get rid of them and take over their camp, but we didn’t know our enemy well enough. We were outnumbered, and they had an ice mage among them.” She looks at you. “At least we cleared the road. Saved lives.”
                '
                '“You mentioned monsters as well?”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You mentioned monsters as well?”')
                    $ description_tulia02 = "She didn’t expect to become a lieutenant. Most members of her squad are already dead."
                    menu:
                        '“Nothing that would surprise you. Those of us who survived the skirmish were young. Too inexperienced to spend a summer in this place without a good leader, and they didn’t trust me. One of them got caught by a treant. Another one ignored my orders to perform some sort of a ritual hunt, so a werebear tore her to pieces. The last one tried to act tough, didn’t tell us that he had cut his hand while cleaning his gambeson,” she lets out a ghastly chuckle. “We had to cut it off and he was so ashamed that he decided to walk north, find a new life, disappear. Idiot.”
                        \n\n“What a colorful journey.” {color=#f6d6bd}The man{/color} tries to drink from his mug, but it’s empty.
                        '
                        '“You’ve made this place safer.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’ve made this place safer.”')
                            $ questionpreset = "tulia1"
                            menu:
                                '“Barely.” {color=#f6d6bd}Tulia{/color} seems tired. “And who knows if it was worth the lives and effort.”
                                '
                                '(tulia1 set)':
                                    pass
                        'I stay silent.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stay silent.')
                            $ questionpreset = "tulia1"
                            menu:
                                '{color=#f6d6bd}Tulia{/color} seems defeated.
                                '
                                '(tulia1 set)':
                                    pass

label tulia_about_herselfALL:
    label tulia_about_herself:
        $ tulia_questions_side += 1
        $ tulia_about_herself += 1
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Tulia{/color}, how did you become a lieutenant?”')
        if tutorial_journal == 1:
            $ tutorial_journal = 2
        menu:
            '“That’s not much of a story, honestly,” she looks at her hand, which is currently rolling a mug over the table. “In the city there’s a strict order of, what should I call it?” She exchanges looks with her companion, but he can’t help her. “Well, {i}leadership succession{/i}, I guess. {color=#f6d6bd}Hovlavan{/color} chief selects commanders, those select lieutenants, and those put their soldiers in order of priority. If a lieutenant dies, they get replaced by the next soldier in line.”
            '
            '“So you were his successor?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So you were his successor?”')
                menu:
                    '“Nah, not exactly. When we fought the bandits, our lieutenant was hit by a slingshot. His boyfriend jumped to help him, but failed to protect either of them from a spell. It was like a ball of ice that hung above them and exploded, piercing their heads, completely avoiding their shield. Really unpleasant.”
                    \n\nShe pauses.
                    '
                    '“And you were the third one in line, is that right?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And you were the third one in line, is that right?”')
                        jump tulia_about_herselfp03
                    '“Jumping like that to save a man in the middle of an attack... Doesn’t sound like a wise decision.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Jumping like that to save a man in the middle of an attack... Doesn’t sound like a wise decision.”')
                        menu:
                            '“I agree, but so what? He’s dead, I doubt he’s going to learn much from scolding.”
                            '
                            '“And you were the third one in line, is that right?”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And you were the third one in line, is that right?”')
                                jump tulia_about_herselfp03

    label tulia_about_herselfp03:
        $ description_tulia02 = "She didn’t expect to become a lieutenant and most members of her squad are already dead."
        $ questionpreset = "tulia1"
        menu:
            '“Basically, yeah,” she says without enthusiasm. “I didn’t plan to become a leader, though. I’ll get demoted once we return to the city. I prefer to follow anyway.”
            '
            '(tulia1 set)':
                pass

label tulia_about_hermission:
    $ tulia_questions_side += 1
    $ tulia_about_hermission += 1
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What was your squad’s mission?”')
    if tutorial_journal == 1:
        $ tutorial_journal = 2
    menu:
        '{color=#f6d6bd}The lieutenant{/color} looks into your eyes. “You know. The usual. Making the roads safe. Keeping people alive.”
        '
        'I explain that it may be important for me to know what they have tried to accomplish.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I explain that it may be important for me to know what have they tried to accomplish.')
            label tulia_about_hermissionp02b:
                $ questionpreset = "tulia1"
                if tulia_friendship >= 3:
                    $ description_tulia04 = "Her squad was meant to find a fitting place for a new outpost."
                    menu:
                        '“I can’t really tell you... Let’s just say it would be nice to have a {i}reliable{/i} outpost somewhere nearby. A place where you can always find a group of fighters willing to protect you in the name of the law,” she tilts her head back. “Now, if you have any other questions...”
                        '
                        '(tulia1 set)':
                            pass
                else:
                    $ questionpreset = "tulia1"
                    menu:
                        '“I can’t really tell you,” you sense no hesitation. “Do you have any other questions?”
                        '
                        '(tulia1 set)':
                            pass

    label tulia_about_hermissionp02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About your squad’s mission...”')
        jump tulia_about_hermissionp02b

label tulia_about_camp:
    $ tulia_questions_side += 1
    $ tulia_about_camp += 1
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Anything I should know about this camp?”')
    if tutorial_journal == 1:
        $ tutorial_journal = 2
    $ questionpreset = "tulia1"
    menu:
        'The story is brief. Some merchants built the camp to have an extra stop for mules and donkeys, just between the inn and the southern villages. There’s plenty of grass here, and a pond nearby.
        \n\nWhen the peninsula grew more dangerous, the camp stood abandoned, from time to time serving as a shelter for travelers. The bandits came here in spring, further paralyzing the exchange of information between the northern and southern settlements.
        \n\nSince these highwaymen are no more, the situation may reverse. Time will tell.
        \n\n“You can sleep here wherever you want,” {color=#f6d6bd}the man{/color} concludes their tale. “Though don’t expect to wake up without pain in your back.
        '
        '(tulia1 set)':
            pass

label tulia_about_advice:
    $ tulia_questions_side += 1
    $ tulia_about_advice += 1
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If you were me, where would you go next?”')
    if tutorial_journal == 1:
        $ tutorial_journal = 2
    menu:
        '{color=#f6d6bd}The soldier{/color} answers quickly. “To the inn, of course,” he grabs his empty mug. “The one northwest from here. If you can’t afford the room, the main hall is free of charge.”
        \n\n“The locals rarely gather there. The northern road is much more traveled,” mentions {color=#f6d6bd}Tulia{/color}, “but the hunters will tell you about this and that, and you’ll have a chance to introduce yourself. {color=#f6d6bd}The innkeeper{/color} can listen, and knows many souls.”
        '
        '“Any tips on how can I make a good first impression on him?”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any tips on how can I make a good first impression on him?”')
            $ description_iason01 = "According to {color=#f6d6bd}Tulia{/color}, he prefers to stick to trade, doesn’t like to waste time on jokes and empty gestures."
            $ questionpreset = "tulia1"
            menu:
                'She smirks. “Avoid cheap jokes, stick to trade, don’t waste his time. Show him that you can be relied on.”
                '
                '(tulia1 set)':
                    pass

label prolcamp01imdonewithquestionsALL:
    label prolcamp01imdonewithquestions01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I know everything I need.”')
        if tutorial_journal == 1:
            $ tutorial_journal = 2
        menu:
            '“Are you sure?” says {color=#f6d6bd}the bearded man{/color}. “We may not be around the next time you come here.”
            '
            '“There was something else I meant to discuss.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There was something else I meant to discuss.”')
                $ questionpreset = "tulia1"
                menu:
                    '{color=#f6d6bd}Tulia{/color} nods. “What is it?”
                    '
                    '(tulia1 set)':
                        pass
            '“We should prepare for the night anyway.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We should prepare for the night anyway.”')
                jump prolcamp01afterquestions01

    label prolcamp01afterquestions01:
        $ tutorial_archive = 1
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s getting late. We should prepare for the night.”')
        if tutorial_journal == 1:
            $ tutorial_journal = 2
        if tulia_friendship > 0:
            menu:
                '“I agree,” {color=#f6d6bd}Tulia{/color} sighs with relief. “And may you do better than {color=#f6d6bd}Asterion{/color} did. Stay vigilant,” she winks at you, shattering the mask of a soldier.
                '
                '“Thank you for your help.”':
                    $ tutorial_archive = 0
                    if militarycamp_firstwatch == 0:
                        jump prolcamp01firstwatchsecondinvite
                    else:
                        jump prolcamp01afterquestions02
        else:
            menu:
                '“We very much should,” {color=#f6d6bd}Tulia{/color} sighs with relief. “And you’ll need a lot of sleep on your journey.”
                '
                'I stand up and prepare for the night.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stand up and prepare for the night')
                    $ tutorial_archive = 0
                    if militarycamp_firstwatch == 0:
                        jump prolcamp01firstwatchsecondinvite
                    else:
                        jump prolcamp01afterquestions02

################################## BEING ON A WATCH / SLEEPING

label prolcamp01firstwatchALL:
    label prolcamp01firstwatchsecondinvite:
        menu:
            '“One more thing, if I can,” {color=#f6d6bd}the bearded man{/color} approaches you. “Can you take the first watch? Splitting time between three people makes a great difference.”
            \n\nYou think for a moment. To fully rest, you’d need a good sleep.
            '
            '“Sure, leave it to me.”':
                $ tulia_friendship += 1
                $ militarycamp_firstwatch = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Sure, leave it to me.”')
                menu:
                    '“Fabulous,” he pats your shoulder. “It should be calm, at least before midnight. Wake me up in a few hours, or even earlier, if anything happens.”
                    '
                    'I nod.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod.')
                        jump prolcamp01afterquestions02
                    'I smile. “I’m happy to do my part.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “I’m happy to do my part.”')
                        jump prolcamp01afterquestions02
            '“I’m exhausted.”':
                $ tulia_friendship -= 1
                $ militarycamp_firstwatch = -1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m exhausted.”')
                menu:
                    'He nods, but the spark in his eyes wears off. “I better put on my armor.” He walks past you, heading to his tent by the southern gate.
                    '
                    'I go to my mount.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to my mount.')
                        jump prolcamp01afterquestions02

    label prolcamp01afterquestions02:
        $ quarters += 1
        $ tutorial_appearance = 1
        $ appearancescreen = 1
        menu:
            'You go to the barrel and splash water on your face, which makes you even more aware of how much you need a bath. After the night, it will only get worse.
            \n\nYour horse is already napping, still too anxious to lay down.
            '
            'I prepare for my watch.' if militarycamp_firstwatch == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I prepare for my watch.')
                $ tutorial_appearance = 2
                jump prolcamp01nightwatch01
            'I look for a place protected from wind. I use my bag as a pillow, put my blanket on the ground, and cover myself with my cloak.' if militarycamp_firstwatch != 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for a place protected from wind. I use my bag as a pillow, put my blanket on the ground, and cover myself with my cloak.')
                $ tutorial_appearance = 2
                jump prolcamp01firstnight01

    label prolcamp01nightwatch01:
        menu:
            '{color=#f6d6bd}The soldier in the shirt{/color} is eager to guide you. “Just observe the area. There’s plenty of griffons around, though they won’t try to jump over the palisade. Probably. Better watch out for the apes, they climb up and carry out any food they can find. And there’s this one really loud wereelk that keeps smelling the wall, though it has never tried to get in.”
            \n\nHe points at a gate. “The lieutenant and I will block the entrances. They’re quite heavy, so if anyone comes here looking for shelter, better call us to help you out. And if this someone is being chased by wolves or anything, better throw them the rope instead.”
            \n\nHe scratches his head. “If it gets cold, feel free to make a fire. And the best place is on the watchtower, you may want to put a blanket there or something.”
            '
            '“The watchtower?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The watchtower?”')
                if tulia_friendship >= 2 or tulia_about_tired:
                    menu:
                        'He gives you a long, puzzled look.
                        \n\n“Oh, here!” He points at the pile of crates. “Just climb up to the tallest one. You’ll have a great view at the northern side. The more {i}dangerous{/i} side. And also... I know you’re tired, after all that riding,” he points at the tent on the other side of the camp. “I can handle a couple of hours sleeping on the ground. If you wish, go there after me and rest, just this once. At least I have a pallet inside.”
                        '
                        'I smile. “Thanks a lot.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Thanks a lot.”')
                            $ militarycamp_sleep_tent = 1
                            jump prolcamp01nightwatch03
                        'I walk away. “I’m fine, don’t worry about me.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk away. “I’m fine, don’t worry about me.”')
                            $ militarycamp_sleep_tent = 0
                            jump prolcamp01nightwatch03
                else:
                    menu:
                        'He gives you a long, puzzled look.
                        \n\n“Oh, here!” He points at the pile of crates. “Just climb up to the tallest one. You’ll have a great view,” he snickers, but you know you won’t be able to spot any movement under the southern part of the palisade.
                        '
                        'Maybe the real danger comes from the north.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe the real danger comes from the north.')
                            jump prolcamp01nightwatch03

    label prolcamp01nightwatch03:
        show areapicture prologuemilitarycampscrap05dark at basicfade
        $ quarters += 1
        stop music fadeout 4.0
        play nature "audio/ambient/night01.ogg" fadeout 1.0 fadein 5.0 volume 1.0
        menu:
            'You put your blanket on the tallest crate and sit down. The night is warm, but the sporadic summer breeze brings gentle refreshment. From time to time your back aches, and you have to force yourself to keep your eyes open. The light of the moon helps you focus on the tall grasses.
            \n\nFor most of the time, you spot smaller critters and birds, but there are exceptions. At one point, you see three-horned deer, trying to challenge one another. Before they clash their antlers, a two-legged dragonling appears, leading its much smaller offspring. The furry beasts try to intimidate the predators with roars and aggressive head movements. After a few moments, both sides walk away slowly, not willing to risk the fight, nor to admit their defeat.
            '
            'I don’t let it distract me. I keep looking around.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t let it distract me. I keep looking around.')
                $ militarycamp_firstwatch_finished = 1
                $ quarters += 9
                menu:
                    'You hear the death screams of distant prey and the mating calls of monkeys. Runners are chasing a gray hare. A group of muskoxen lazily chew the grass, preparing themselves to sleep. A dusk fox is running together with a lynx, making playful screeches.
                    \n\nThankfully, you never have to intervene. You just sit there, watching the not-so-distant forest, trying to outlast your sleepiness.
                    \n\nYou can only guess how much time has passed. Once you feel you’ve had enough, you climb down and go to a tent, waking up {color=#f6d6bd}the bearded man{/color} with just a couple of words. You confirm that nothing important has happened.
                    '
                    'I look for a place protected from wind. I use my bag as a pillow, put my blanket on the ground, and cover myself with my cloak.' if not militarycamp_sleep_tent:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for a place protected from wind. I use my bag as a pillow, put my blanket on the ground, and cover myself with my cloak.')
                        jump prolcamp01firstnight01
                    'I gather my things and squeeze into the tent. I use my bag as a pillow, put my blanket on the pallet, and cover myself with my cloak.' if militarycamp_sleep_tent == 1:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I gather my things and squeeze into the tent. I use my bag as a pillow, put my blanket on the pallet, and cover myself with my cloak.')
                        jump prolcamp01firstnight01inatent

label prolcamp01firstnight01:
    menu:
        'You aren’t used to sleeping in such harsh conditions, but it’s better than nothing. The weather is gentle, maybe you won’t catch a cold.
        \n\nThe stars instantly inspire your dreams, both with their splendor and by making you look for patterns and shapes among them.
        \n\nYour job starts tomorrow.
        '
        'I focus on the real goal of my journey.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I focus on the real goal of my journey.')
            jump prolcamp01firstnight02

label prolcamp01firstnight01inatent:
    menu:
        'Sleeping in a tent is not the stuff of dreams, but it’s a much welcomed rest. The pallet keeps the cold soil away. The moonlight saves the outside world from the eerie gloom. You listen to your own breath and find a comfortable position.
        \n\nYour job starts tomorrow.
        '
        'I focus on the real goal of my journey.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I focus on the real goal of my journey.')
            jump prolcamp01firstnight02

label prolcamp01firstnightALL:
    label prolcamp01firstnight02:
        $ quest_explorepeninsula = 1
        $ quest_explorepeninsula_description01 = "I need to explore the peninsula as thoroughly as I can. I have to get to know the locals and find out how much of a profit can be made here, then bring the news to {color=#f6d6bd}Hovlavan{/color}."
        $ quest_explorepeninsula_description01a = "To add worth to my work here, I could secure the roads by getting rid of any major threats, and convince the tribes to negotiate with the officials."
        $ renpy.notify("New journal entry: Explore the Peninsula")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New journal entry: Explore the Peninsula{/i}')
        $ world_deadline_display = (world_deadline)
        menu:
            'The merchant guild wants to take control of this realm. Your wardening duties are secondary - first and foremost, you need to explore the peninsula. Learn about the territory, resources, and threats. Get to know the locals - and if you can, convince them to consider negotiations with {color=#f6d6bd}Hovlavan{/color} officials and traders. Could the tribes resist the soldiers, or be a threat to the priests of The United Church? Are there any forbidden practices that need to be eradicated - such as blood magic, necromancy, robbery, or slavery?
            '
            'At least I have time. I need to be as thorough as I can.' if game_mode == 1 or world_deadline == 1000:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- At least I have time. I need to be as thorough as I can.')
                jump prolcamp01firstnight02a
            'At least I have time. [world_deadline_display] days, to be exact. I need to be as thorough as I can.' if game_mode != 1 and world_deadline != 1000:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- At least I have time. %s, to be exact. I need to be as thorough as I can.' %world_deadline_display)
                label prolcamp01firstnight02a:
                    menu:
                        'Once you finish your reconnaissance, you should speak with {color=#f6d6bd}Tulia{/color} and return to {color=#f6d6bd}Hovlavan{/color}. There, you’ll report back to your employers and get your reward. In the meantime, you have your own goal to pursue.
                        '
                        'I need to gather some extra coins so I can save my sibling from debt collectors.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I need to gather some extra coins so I can save my sibling from debt collectors.')
                            $ pc_goal = "ineedmoney"
                            $ quest_pc_goal_name = "Gather Wealth"
                            jump prolcamp01firstnight04
                        ############################
                        'I need to gather some extra coins so I can retire early and live in prosperity and safety.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I need to gather some extra coins so I can retire early and live in prosperity and safety.')
                            $ pc_goal = "iwantmoney"
                            $ quest_pc_goal_name = "Become Rich"
                            jump prolcamp01firstnight04
                        ############################
                        'If I gather enough connections among the local leaders, I’ll use them to become a major player in the merchant guild.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- If I gather enough connections among the local leaders, I’ll use them to become a major player in the merchant guild.')
                            $ pc_goal = "iwantstatus"
                            $ quest_pc_goal_name = "Gain Influence"
                            jump prolcamp01firstnight04
                        ############################
                        'I want to be remembered as the soul who brought peace and order to this realm. A hero.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to be remembered as the soul who brought peace and order to this realm. A hero.')
                            $ pc_goal = "iwanttoberemembered"
                            $ quest_pc_goal_name = "Become a Hero"
                            jump prolcamp01firstnight04
                        ############################
                        'I just want to help people. Make this region safer for the locals and the newcomers alike.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I just want to help people. Make this region safer for the locals and the newcomers alike.')
                            $ pc_goal = "iwanttohelp"
                            $ quest_pc_goal_name = "Help Others"
                            jump prolcamp01firstnight04
                        ############################
                        'I need to find a new life for myself. I have a difficult past, and I want it to be forgotten.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I need to find a new life for myself. I have a difficult past, and I want it to be forgotten.')
                            $ pc_goal = "iwanttostartanewlife"
                            $ quest_pc_goal_name = "A New Life"
                            jump prolcamp01firstnight04

    label prolcamp01firstnight04:
        $ restunlocked = 1
        $ can_rest = 1
        $ tutorial_sleep = 1
        $ can_items = 1
        if pc_class == "mage":
            $ classabilityscreen = 1
        $ quarters += 1
        $ renpy.notify("New shelter unlocked.\nNew entry: %s" %quest_pc_goal_name)
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New shelter unlocked.\nNew entry: %s{/i}' %quest_pc_goal_name)
        $ quest_pc_goal = 1
        if persistent.deafmode:
            $ deafcustom1 = "All the roars, whimpers, howls, and singing... "
        else:
            $ deafcustom1 = ""
        menu:
            'Your half-asleep senses are catching the sounds of the wild forest. [deafcustom1]Your instincts keep you alert and anxious, though the pleasant, humid, late-summer air evens it out slowly.
            \n\nYou’re thinking about your goal, but you need to gather your strength.
            '
            'All I can do now is rest. (disabled)':
                pass

################################## NEXT DAY
label prolcamp01newdayALL:
    label prolcamp01newday:
        show areapicture prologuemilitarycampscrap08 at basicfade
        stop nature fadeout 4.0
        stop music fadeout 4.0
        $ tutorial_sleep = 0
        nvl clear
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        play nature "audio/ambient/pyre01.ogg" fadeout 1.0 fadein 5.0 volume 1.0
        menu:
            'You’re surrounded by sunlight, your back begs you to stand up.
            \n\nBefore you fully wake up, you smell a roast. No, burning meat. Burning, rotten meat. Disgust crawls toward your consciousness.
            \n\nYou stand up. Normally you would dust off your cape and blanket, but your instincts are stronger than your routine.
            \n\nYour horse is looking around nervously. Your bags are where you had left them. You see an open gate.
            '
            'I go outside to see what’s happening.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside to see what’s happening.')
                $ renpy.force_autosave(take_screenshot=False, block=True)
                jump prolcamp01newday02

    label prolcamp01newdaytent:
        show areapicture prologuemilitarycampscrap08 at basicfade
        stop nature fadeout 4.0
        stop music fadeout 4.0
        $ tutorial_sleep = 0
        nvl clear
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        play nature "audio/ambient/pyre01.ogg" fadeout 1.0 fadein 5.0 volume 1.0
        menu:
            'You’re woken up by sunlight, well-rested and ready. Without haste, you gather your things. After only a couple of breaths you notice a weird smell, like a roast. No, burning meat. Burning, rotten meat. Disgust crawls into your consciousness. You exit the tent.
            \n\nYour horse is looking around nervously. Your bags are where you had left them. You see an open gate.
            '
            'I go outside to see what’s happening.':
                $ renpy.force_autosave(take_screenshot=False, block=True)
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside to see what’s happening.')
                jump prolcamp01newday02

    label prolcamp01newday02:
        show areapicture prologuemilitarycampscrap04 at basicfade
        menu:
            'Both soldiers are standing near a humble pyre. {color=#f6d6bd}The man in the shirt{/color} looks at it contemplatively. {color=#f6d6bd}Tulia{/color} is the first one to address you.
            \n\n“[pcname],” she greets you with a nod. “We used the horse’s manure for the flames, so don’t worry about cleaning it up.”
            \n\nYou see a corpse among the flames. It’s impossible to tell if it belongs to a male or a female, but it was an adult.
            \n\nThe burning process won’t be over for a couple more hours.
            '
            '“A traveler, or an undead?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “A traveler, or an undead?”')
                menu:
                    '“The latter. A young one, she lacked the pneuma to understand that she couldn’t get inside the camp without climbing. I stabbed her with a spear, from a safe distance,” she shifts her weight. “One more fog and she’d be a real threat. Even now it took a couple of hits to knock her down.”
                    \n\nSooner or later, every human shell wakes up, gaining more strength with each soul it devours and each moment it spends in the fogs. Burning the dead is not just a religious practice, it’s a necessity. Soldiers, priests, village mayors, even roadwardens... Making a large pyre takes a lot of time, but it saves lives.
                    \n\n{color=#f6d6bd}Tulia{/color} calls this undead a {i}she{/i}. Most Unites hesitate to do so.
                    '
                    '“Time for me to leave.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Time for me to leave.”')
                        jump prolcamp01newday04

    label prolcamp01newday04:
        if tulia_friendship >= 2:
            menu:
                '“Running away from the reek, huh? I don’t blame you,” she walks with you for a few steps. “Find us here if you need us, or if you learn what happened to {color=#f6d6bd}Asterion{/color}. There’s enough ground here for you to rest. Safe travels.”
                \n\nThese words make you stop. An old farewell, mocked in a number of songs and tales, but yet you hear no scorn in {color=#f6d6bd}Tulia’s{/color} voice. You wonder how many acts of kindness like this one you’re going to experience in the days to follow.
                \n\nShe returns to the pyre.
                '
                'I prepare myself for the journey.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I prepare myself for the journey.')
                    jump prolcamp01newday05
        else:
            menu:
                '“Running away from the reek, huh? I don’t blame you.” She looks again at the fire. “Find us here if you learn what happened to {color=#f6d6bd}Asterion{/color}. We leave once the fall comes, if not sooner. Safe travels.”
                \n\nThese words make you stop. An old farewell, mocked in a number of songs and tales, but yet you hear no scorn in {color=#f6d6bd}Tulia’s{/color} voice. She observes the fire with one hand on her hip, the other one on her chin.
                '
                'I prepare myself for the journey.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I prepare myself for the journey.')
                    jump prolcamp01newday05

    label prolcamp01newday05:
        if militarycamp_firstwatch == 1:
            $ mapunlocked = 1
            $ tutorial_map = 1
            $ horsename = 0
            $ can_leave = 1
            $ tosoutherncrossroads = 1
            if not pc_likeshorsename:
                $ custom1 = ""
            else:
                $ custom1 = "The palfrey nickers, ready to leave. "
            menu:
                'You somehow missed the fact that your mount is already saddled and warmed up. You double-check the equipment, but you don’t need to fix anything - the soldiers were diligent. Normally, preparing any palfrey for a long journey takes a lot of time.
                \n\nYou put on your gambeson and make sure that your axe is tightly attached to your belt, then get in the saddle. [custom1]It’s time for you to get to the crossroads, north from here.
                '
                'I need to ride north. (disabled)':
                    pass
        else:
            $ quarters += 2
            $ mapunlocked = 1
            $ tutorial_map = 1
            $ can_leave = 1
            $ horsename = 0
            $ tosoutherncrossroads = 1
            if not pc_likeshorsename:
                $ custom1 = ""
            else:
                $ custom1 = "The palfrey nickers, ready to leave. "
            menu:
                'You gather your equipment and spend half an hour warming up and preparing your mount, double-checking the buckled straps. You put on your gambeson and make sure that your axe is tightly attached to your belt, then get in the saddle. [custom1]
                \n\nIt’s time for you to get to the crossroads, north from here.
                '
                'I need to ride north. (disabled)':
                    pass

################################## GRIFFONS
label griffonsroadALL:
    label griffonsroad01:
        show areapicture militarycamptosoutherncrossroads at basicfade
        if not renpy.music.get_playing(channel='music') == "<loop 20.0>audio/track_16travelingandprologuedayone.ogg":
            play music "<loop 20.0>audio/track_16travelingandprologuedayone.ogg" fadeout 1.0 fadein 1.0
        stop nature fadeout 2.0
        $ travel_firsttime = 1
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ tutorial_map = 0
        $ tutorial_endgame = 0
        $ pc_area = "griffonsroad01"
        nvl clear
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        menu:
            'Even at a later hour you wouldn’t expect to meet any travelers in the valley. The warm summer breeze lures your mount forward, but the serene chirping of birds is quickly replaced by the distracting screeches and gurgles, coming from further down the path.
            \n\nYou soon find the pack of four-legged griffons. They’re larger than foxes, and merge the features of birds and furred beasts. Each one is of a different size, coat, and colors, and their temperaments are just as varied. Their fronts are covered with vivid feathers, while their rears have darker fur. Their wings are massive, making them impressive jumpers, but they’re too heavy to fly.
            \n\nAbout two dozen beasts are yelling, brawling, and chasing each other around, blocking your path.
            '
            'I consider my options.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I consider my options.')
                $ tutorial_abilities = 1
                $ tutorial_random = 1
                $ classabilityscreen = 1
                $ at = 0
                if pc_class == "warrior":
                    $ at_unlock_force = 1
                if pc_class == "mage":
                    $ at_unlock_spell = 1
                    $ manacost = 1
                if pc_class == "scholar":
                    $ at_unlock_knowledge = 1
                menu:
                    'You can’t enter the forest blindly. If these or other creatures were to chase after you, the thicket would be disastrous for your horse. There are reasons why travelers stay as close to the main roads as possible, and why adventurers move in groups.
                    \n\nUsually, the safest approach would be to stay where you are and just wait for the pack to get hungry. It may, however, take up to a couple of hours. You’re thinking about your conversation with {color=#f6d6bd}Tulia{/color}. You’ve got a lot to do, and time may be of the essence.
                    '
                    '{image=d6} I take my axe and hurry the horse. If we ride fast enough, we should be fine.' ( condition="at != 'force' and at != 'spell' and at != 'knowledge'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I take my axe and hurry the horse. If we ride fast enough, we should be fine.')
                        $ at_unlock_force = 0
                        $ at_unlock_spell = 0
                        $ at_unlock_knowledge = 0
                        $ tutorial_abilities = 0
                        $ d100roll = 0
                        $ d100roll = renpy.random.randint(1, 10)
                        if not pc_food:
                            $ d100roll += 1
                        if pc_food == 3:
                            $ d100roll -= 1
                        if pc_food == 4:
                            $ d100roll -= 2
                        $ tutorial_random = 0
                        jump griffonsroad03charge
                    '{image=d6} I should stay here. Better safe than sorry.' ( condition="at != 'force' and at != 'spell' and at != 'knowledge'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I should stay here. Better safe than sorry.')
                        $ achievement_animalssavedpoints += 1
                        $ at_unlock_force = 0
                        $ at_unlock_spell = 0
                        $ at_unlock_knowledge = 0
                        $ tutorial_abilities = 0
                        $ d100roll = 0
                        $ d100roll = renpy.random.randint(1, 4)
                        $ quarters += (4+d100roll)
                        $ tutorial_random = 0
                        jump griffonsroad03wait
                    'Getting through them should be easy enough.' ( condition="at == 'force'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Getting through them should be easy enough.')
                        $ at_unlock_force = 0
                        $ at_unlock_spell = 0
                        $ at_unlock_knowledge = 0
                        $ tutorial_abilities = 0
                        $ tutorial_random = 0
                        jump griffonsroad03force
                    'I grab my crossbow. A light hit should be enough to make them scatter.' ( condition="at != 'force' and item_crossbow and item_crossbowquarrels" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab my crossbow. A light hit should be enough to make them scatter.')
                        $ encounter_scavenger_griffon_hurt_quarrel = 1
                        $ at_unlock_force = 0
                        $ at_unlock_spell = 0
                        $ at_unlock_knowledge = 0
                        $ tutorial_abilities = 0
                        $ tutorial_random = 0
                        jump griffonsroad03crossbow
                    'I grab an amulet and shape a missile of light. A harmless flare will frighten them off. [[Cost: {color=#f6d6bd}[manacost]{/color} pneuma]' ( condition="at == 'spell'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab an amulet and shape a missile of light. A harmless flare will frighten them off.')
                        $ at_unlock_force = 0
                        $ at_unlock_spell = 0
                        $ at_unlock_knowledge = 0
                        $ tutorial_abilities = 0
                        $ tutorial_random = 0
                        $ mana = limit_mana(mana-manacost)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
                        jump griffonsroad03spell
                    'I mix black powder with gladdon that grows nearby and the dried skunk sorrel from my bag. Once I ignite it and throw it at the griffons, they’ll scatter.' ( condition="at == 'knowledge'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I mix black powder with gladdon that grows nearby and the dried skunk sorrel from my bag. Once I ignite it and throw it at the griffons, they’ll scatter.')
                        $ at_unlock_force = 0
                        $ at_unlock_spell = 0
                        $ at_unlock_knowledge = 0
                        $ tutorial_abilities = 0
                        $ tutorial_random = 0
                        $ quarters += 1
                        jump griffonsroad03knowledge

    label griffonsroad03wait:
        $ tutorial_sheet = 1
        $ tutorial_sheet_display = 1
        if d100roll == 1 or d100roll == 2:
            $ custom1 = "more than an hour"
        elif d100roll == 3:
            $ custom1 = "almost two hours"
        else:
            $ custom1 = "about maybe two hours"
        menu:
            'While you’re observing the griffons from a safe distance, you allow your horse to graze for a bit. Occasionally you see other, smaller animals, but you spend your time undisturbed.
            \n\nAfter [custom1] of waiting, two of the larger beasts engage in what looks to you like savage combat, but results in merely knocking one of them on its side. The defeated griffon stands up completely unharmed, preening its feathers bashfully, while the champion walks away proudly, followed by the other members of its pack. They disappear among the trees.
            '
            'I’m ready to move forward.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m ready to move forward.')
                $ tutorial_sheet_display = 0
                jump finaldestinationafterevent

    label griffonsroad03charge:
        $ tutorial_sheet = 1
        $ tutorial_sheet_display = 1
        if d100roll == 1:
            label griffonsroad03force:
                $ pc_battlecounter += 1
                $ tutorial_sheet = 1
                $ tutorial_sheet_display = 1
                menu:
                    'Initially, your horse completely trusts your guidance, though after a few more steps it snorts. You prepare your axe and get ready to push away any griffon willing to jump on you. Once you get in the middle of the surprised herd, your mount squeals and gallops forward.
                    \n\nThe creatures in front of you flee, but others try to jump at you from both sides. You kick two of them away, and while the third one gets close, its beak lands only on your boot. The hard leather keeps you safe.
                    \n\nYou ride away, and the griffons can’t keep up. You still hear their screeches when your mount slows down.
                    '
                    'I don’t give them an opportunity to catch up with me.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t give them an opportunity to catch up with me.')
                        $ tutorial_sheet_display = 0
                        jump finaldestinationafterevent
        else:
            $ pc_battlecounter += 1
            $ pc_hp = limit_pc_hp(pc_hp-1)
            show minus1hp at hpchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            menu:
                'Initially, your horse completely trusts your guidance, though after a few more steps it snorts. You prepare your axe and get ready to push away any griffon willing to jump on you. Once you get in the middle of the surprised herd, your mount squeals and gallops forward.
                \n\nThe creatures in front of you flee, but others try to jump at you from both sides. You kick two of them away, but the third one scratches your leg. It hurts, though only a bit.
                \n\nYou ride away, and the griffons can’t keep up. You still hear their screeches when your mount slows down.
                '
                'Once I get to a safer spot, I stop to clean and bandage my wound.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Once I get to a safer spot, I stop to clean and bandage my wound.')
                    $ tutorial_sheet_display = 0
                    jump finaldestinationafterevent

    label griffonsroad03crossbow:
        $ tutorial_sheet = 1
        $ tutorial_sheet_display = 1
        $ item_crossbowquarrels -= 1
        $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
        menu:
            'Crossbows are an easy weapon to use and you’ve got plenty of time to aim. The creature falls on its side and screams, alerting its companions. Confused, they look around, and after a while, they run away, one of them limping, with your quarrel in its thigh.
            '
            'I ride forward.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ride forward.')
                $ tutorial_sheet_display = 0
                jump finaldestinationafterevent

    label griffonsroad03spell:
        $ tutorial_sheet = 1
        $ tutorial_sheet_display = 1
        menu:
            'You grab one of your oldest amulets, a pendant made of leather and a single dim pearl. The little sphere is covered by cryptic engravings, but if there’s any special meaning behind them, you were never able to find out what it could be.
            \n\nHolding the pearl between your fingers, you feel the pleasant, familiar warmth. The spell you are about to cast is not much more than a mere illusion, but you take a couple of breaths, trying to minimize any risk of failure.
            \n\nThe pneuma leaves your shell, formed into a white ball that you barely comprehend. When it falls next to the griffons, for a couple of blinks it emits dazzling light. The animals squeak and snarl, fleeing in multiple directions at once. The road is now clear.
            '
            'I ride forward and enjoy the touch of my pendant. It cools down slowly.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ride forward and enjoy the touch of my pendant. It cools down slowly.')
                $ tutorial_sheet_display = 0
                jump finaldestinationafterevent

    label griffonsroad03knowledge:
        $ tutorial_sheet = 1
        $ tutorial_sheet_display = 1
        menu:
            'Most cityfolk feel aversion toward black powder, and you touch it with great care. The odor of the plants makes you feel dizzy, but what’s more important is that the griffons have wolf-like sensitivity to smells and noises.
            \n\nA few of the beasts turn their heads toward you as you approach the pack with a bag in your hand. You ignite your missile and throw it forward. At first, the creatures surround the source of smoke, but then growl in disgust, even putting their beaks to the ground. They flee, allowing you to continue your journey.
            '
            'I climb on the horse and cover my nose. I really need to find a proper alchemy set.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I climb on the horse and cover my nose. I really need to find a proper alchemy set.')
                $ tutorial_sheet_display = 0
                jump finaldestinationafterevent
