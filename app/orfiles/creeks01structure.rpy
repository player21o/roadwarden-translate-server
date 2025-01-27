###################### CREEKS
default creeks_firsttime = 0
default creeks_reputation = 0
default creeks_feast = 0
default creeks_feast_known = 0

default creeks_sleep_available = 0
default creeks_sleep = 0
default creeks_traveling = 0
default creeks_offeredtojoin = 0
default creek_woodenweapons = 0

default creeks_youth_lookedat = 0
default creeks_youth_gambling = 0
default creeks_youth_gambling_invited = 0
default creeks_youth_gambling_wager = 0 # "wilplants" / "coin" / "rations" / "none"
default creeks_youth_sex = 0

default creeks_fluff = ""
default creeks_fluff_old = ""
default creeks_horsename_fluff = ""
default creeks_horsename_fluff_old = ""

default shoshi_namebig = "The dark-haired woodcutter"
default shoshi_namesmall = "the dark-haired woodcutter"
default shoshi_single = 0 # Shoshi
default shoshi_marina = 0
default shoshi_religion = 0
default shoshi_notmatched = 0

default creeks_mundanework = 0
default creeks_mundanework_counter = 0
default creeks_mundanework_betterpay = 0
default creeks_mundanework_payment = 2
default creeks_mundanework_numberoftimes = 0

# https://www.babynamesdirect.com/baby-names/hebrew/girl/meaning/flower
# https://www.babynamesdirect.com/baby-names/hebrew/boy/meaning/tree
# https://www.kveller.com/article/jewish-flower-names-for-spring/
# https://ulpan.com/trees-and-childrens-names-2/
# https://babynames.net/boy/hebrew?page=13

# BRONIE PROSTE
# drewniane, skomplikowane pałki (cudgels?) - https://www.youtube.com/watch?v=2C6_pSEPbO8 - samoan war club, fighting staff, tewhatewha , maori pounamu / patu onewa

# ARGUMENTS TO CONVINVCE THE VILLAGE TO JOIN HOVLAVAN
default creeks_reasonstojoin_missinghunters = 0
default creeks_reasonstojoin_beastattacks = 0
default creeks_reasonstojoin_lackofmetal = 0
default creeks_reasonstojoin_creeksaboutlackingwall = 0
default creeks_reasonstojoin_creeksaboutlackingmeat = 0
default creeks_reasonstojoin_creeksaboutweakness = 0
default creeks_reasonstojoin_reputation = 0
default creeks_reasonstojoin_foggy_friendship = 0
default creeks_reasonstojoin_healedtheplague = 0
default creeks_reasonstojoin_hruinedvillage_truth = 0
default creeks_reasonstojoin_hpcknowstruthaboutinbreeding = 0
default creeks_reasonstojoin_lackingseeds = 0
default creeks_reasonstojoin_problemsknown = 0
default creeks_reasonstojoin_points = 0

default creeks_reasonstojoin_feast_beastattacks = 0
default creeks_reasonstojoin_feast_lackofmetal = 0
default creeks_reasonstojoin_feast_lackofmeat = 0
default creeks_reasonstojoin_feast_lackingwall = 0
default creeks_reasonstojoin_feast_weakness = 0
default creeks_reasonstojoin_feast_inbreeding = 0
default creeks_reasonstojoin_feast_steephouse = 0
default creeks_reasonstojoin_feast_lakingseeds = 0
default creeks_reasonstojoin_feast_foggy = 0
default creeks_reasonstojoin_feast_missinghunters = 0
default creeks_reasonstojoin_feast_reputation = 0
default creeks_reasonstojoin_feast_copper = 0
default creeks_reasonstojoin_feast_plague = 0
default creeks_reasonstojoin_feast_easternpath = 0

label creeks01:
    nvl clear
    $ pc_area = "creeks"
    if not creeks_offeredtojoin:
        if not renpy.music.get_playing(channel='music') == "<loop 18.6>audio/track_11creeks01loop.ogg":
            play music "<loop 18.6>audio/track_11creeks01loop.ogg" fadeout 1.0 fadein 1.0
    else:
        if not renpy.music.get_playing(channel='music') == "audio/track_11creeks02.ogg":
            $ renpy.music.play("audio/track_11creeks02.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    stop nature fadeout 4.0
    $ creeks_youth_gambling_invited = 0
    label creeks_fluffloop:
        $ creeks_fluff = ""
        $ creeks_fluff = renpy.random.choice(['A group of woodcutters wave to you from the copse growing by the river. Both the path and the yard behind the gate bears fresh blood stains, as well as claw marks.', 'A guard leaning from the watchtower warmly welcomes you with a shout, though the wind distorts the words.', 'A few souls, carrying wooden and stone weapons and tools, are just leaving the village. Once you reach the yard, you hear the cozy rustling of shrubs growing on the other side of the palisade.', 'A gust of wind catches some of the falling water and showers you with the cool droplets. You hear the chopping of wood, and it takes a while before the locals open the gate.', 'A few scantily clad people are standing on the bridge, greeting you as you ride by. On your way to the gate, a flock of sparrows takes off from the road, landing either on the watchtower, or on the tree to your right.'])
        if creeks_fluff_old == creeks_fluff:
            jump creeks_fluffloop
        else:
            $ creeks_fluff_old = creeks_fluff
    if not creeks_firsttime:
        $ world_known_npcs += 1
        $ world_known_areas += 1
        $ creeks_firsttime = 1
        $ foggylake_unlocked = 1
        if not pc_firstvillage:
            $ pc_firstvillage = "creeks"
        show areapicture creeks00a at basicfade
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ elah_lastseen = day
        $ efren_lastseen = day
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        jump creeksfirsttime01
    else:
        if quarters < (world_daylength-6):
            if not creeks_feast:
                show areapicture creeks01 at basicfade
            else:
                show areapicture creeks01alt1 at basicfade
        else:
            if not creeks_feast:
                show areapicture creeks01open at basicfade
            else:
                show areapicture creeks01openalt1 at basicfade
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        if elah_quest_easternpath_lumberjacks == 2:
            jump creekselahaboutquesteasternroadfallentree11
        elif quest_birdhunting_description06 and not quest_birdhunting_description07 and not quest_birdhunting_description08 and foragingground_bird_taken == 1:
            jump creeksbringingthebirdnews
        elif not creeks_offeredtojoin and quest_easternpath_points >= 5 and quest_missinghunters == 2 and (appearance_charisma+creeks_reputation+(oldhava_friendship/2)+(efren_friendship/2)+(elah_friendship/2)) >= 20 and elah_about_nomoreundead != 3 and not elah_locked == day:
            $ custom1 = "Before you cross the bridge, a person on the watchtower announces your arrival, and soon after {color=#f6d6bd}Elah{/color} welcomes you from the gate. “I’m glad to see you again, friend!"
            jump creeksinvitingpctojointhetribe01
        jump creeksregular01

label creeksregular01:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    if creeks_feast and not creeks_sleep_available and (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) >= 25 and not oldhava_about_sleep_available:
        $ oldhava_known = 1
        $ oldhava_about_sleep_available = 1
        $ custom4 = "\n\nA young man carrying a few empty buckets welcomes you with a smile. “Here you are, friend! Better speak with {color=#f6d6bd}Old Hava{/color} soon, she has something to tell you about one of the sleeping spots.”"
    elif creeks_reputation >= 6 and appearance_charisma >= 1 and not creeks_youth_gambling and creeks_youth_lookedat:
        $ creeks_youth_gambling_invited = 1
        $ creeks_fluff = "While you cross the bridge, you pass the same group that you saw on the first day you arrived at this place, once again gathered at the creek and scantily clad. Their smiles are inviting, and after you look at them, one of the women invites you with a handwave."
        $ custom4 = ""
    else:
        $ custom4 = ""
    menu:
        '[creeks_fluff][custom4]
        '
        'I look for {color=#f6d6bd}Elah{/color}, the carpenter.' if elah_lastseen < day and elah_locked != day:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for {color=#f6d6bd}Elah{/color}, the carpenter.')
            jump creekselah01
        'I return to {color=#f6d6bd}Elah{/color}, the carpenter.' if elah_lastseen >= day and elah_locked != day:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Elah{/color}, the carpenter.')
            jump creekselah01
        'Elah won’t speak with me today. (disabled)' if elah_locked == day:
            pass
        'I look for {color=#f6d6bd}Efren{/color}, the hunter.' if efren_lastseen < day:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for {color=#f6d6bd}Efren{/color}, the hunter.')
            jump creeksefren01
        'I return to {color=#f6d6bd}Efren{/color}, the hunter.' if efren_lastseen >= day:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Efren{/color}, the hunter.')
            jump creeksefren01
        'I go to {color=#f6d6bd}Old Hava{/color}, the farmer.' if oldhava_known:
            jump creeksoldhava01
        'I approach the shallow creek.' if not creeks_youth_gambling_invited or (creeks_youth_gambling_invited and creeks_youth_gambling):
            jump creekscreek0201
        'I accept the invitation and head to the creek.' if creeks_youth_gambling_invited and not creeks_youth_gambling:
            jump creekscreek0201
        'Maybe there are some locals looking for a match in other villages.' ( condition="not shoshi_single and quest_matchmaking == 1" ):
            jump creekssinglepeople01firsttime
        'I return to {color=#f6d6bd}Shoshi{/color}.' ( condition="(shoshi_single and quest_matchmaking == 1 and not shoshi_notmatched and galerocks_singlepeople_firsttime and not shoshi_marina) or (shoshi_single and quest_matchmaking == 1 and not shoshi_notmatched and shoshi_marina and galerocks_singlepeople_marina_religion1 and not shoshi_religion) or (quest_recruitahunter_noonerecruited and shoshi_notmatched and not quest_recruitahunter_spokento_shoshi)" ):
            jump creekssinglepeople01
        'I still need to find a match for Shoshi. (disabled)' ( condition="shoshi_single and quest_matchmaking == 1 and not galerocks_singlepeople_firsttime" ):
            pass
        'Shoshi is waiting for a message from Marina. (disabled)' ( condition="shoshi_single and quest_matchmaking == 1 and shoshi_marina and not galerocks_singlepeople_marina_religion1" ):
            pass
        '{image=cointest} I have a day to spare. I ask around to see if any locals need protection on the roads.' ( condition="creeks_mundanework and quarters <= 40 and (creeks_mundanework_counter < day)" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Elah{/color}, the carpenter.')
            jump creeksmundanework01
        '{image=coingray} The locals won’t need my services before day [creeks_mundanework_counter]. (disabled)' ( condition="creeks_mundanework and (creeks_mundanework_counter >= day)" ):
            pass
        '{image=coingray} At such a late hour the locals won’t be interested in my services. (disabled)' ( condition="creeks_mundanework and quarters > 40" ):
            pass

label creeksafterinteraction01:
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    label creeks_horsename_fluffloop:
        $ creeks_horsename_fluff = ""
        $ creeks_horsename_fluff = renpy.random.choice(['snorts at a group of kids that are trying to pull its tail. You tell them to run to their grandpa.', 'is napping in the shadow of a tree.', 'is enjoying the cold stream and green grass to graze on, and welcomes you with a nicker.', 'is lazily looking around as it rests on the dusty path.', 'is observing the monkeys moving on the surface of the rock face, swinging its tail.', 'is pawing the ground, and welcomes your arrival with a snort.', 'is walking around the tree, as far away from it as its cord allows.'])
        if creeks_horsename_fluff_old == creeks_horsename_fluff:
            jump creeks_horsename_fluffloop
        else:
            $ creeks_horsename_fluff_old = creeks_horsename_fluff
    menu:
        '{color=#f6d6bd}[horsename]{/color} [creeks_horsename_fluff]
        '
        'I look for {color=#f6d6bd}Elah{/color}, the carpenter.' if elah_lastseen < day and elah_locked != day:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for {color=#f6d6bd}Elah{/color}, the carpenter.')
            jump creekselah01
        'I return to {color=#f6d6bd}Elah{/color}, the carpenter.' if elah_lastseen >= day and elah_locked != day:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Elah{/color}, the carpenter.')
            jump creekselah01
        'Elah won’t speak with me today. (disabled)' if elah_locked == day:
            pass
        'I look for {color=#f6d6bd}Efren{/color}, the hunter.' if efren_lastseen < day:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for {color=#f6d6bd}Efren{/color}, the hunter.')
            jump creeksefren01
        'I return to {color=#f6d6bd}Efren{/color}, the hunter.' if efren_lastseen >= day:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Efren{/color}, the hunter.')
            jump creeksefren01
        'I go to {color=#f6d6bd}Old Hava{/color}, the farmer.' if oldhava_known:
            jump creeksoldhava01
        'I approach the shallow creek.' if not creeks_youth_gambling_invited or (creeks_youth_gambling_invited and creeks_youth_gambling):
            jump creekscreek0201
        'I accept the invitation and head to the creek.' if creeks_youth_gambling_invited and not creeks_youth_gambling:
            jump creekscreek0201
        'Maybe there are some locals looking for a match in other villages.' ( condition="not shoshi_single and quest_matchmaking == 1" ):
            jump creekssinglepeople01firsttime
        'I return to {color=#f6d6bd}Shoshi{/color}.' ( condition="(shoshi_single and quest_matchmaking == 1 and not shoshi_notmatched and galerocks_singlepeople_firsttime and not shoshi_marina) or (shoshi_single and quest_matchmaking == 1 and not shoshi_notmatched and shoshi_marina and galerocks_singlepeople_marina_religion1 and not shoshi_religion) or (quest_recruitahunter_noonerecruited and shoshi_notmatched and not quest_recruitahunter_spokento_shoshi)" ):
            jump creekssinglepeople01
        'I still need to find a match for Shoshi. (disabled)' ( condition="shoshi_single and quest_matchmaking == 1 and not galerocks_singlepeople_firsttime" ):
            pass
        'Shoshi is waiting for a message from Marina. (disabled)' ( condition="shoshi_single and quest_matchmaking == 1 and shoshi_marina and not galerocks_singlepeople_marina_religion1" ):
            pass
        '{image=cointest} I have a day to spare. I ask around to see if any locals need protection on the roads.' ( condition="creeks_mundanework and quarters <= 40 and (creeks_mundanework_counter < day)" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Elah{/color}, the carpenter.')
            jump creeksmundanework01
        '{image=coingray} The locals won’t need my services before day [creeks_mundanework_counter]. (disabled)' ( condition="creeks_mundanework and (creeks_mundanework_counter >= day)" ):
            pass
        '{image=coingray} At such a late hour the locals won’t be interested in my services. (disabled)' ( condition="creeks_mundanework and quarters > 40" ):
            pass

label creeksbringingthebirdnews:
    $ elah_lastseen = day
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    menu:
        '{color=#f6d6bd}Elah{/color} and {color=#f6d6bd}Efren{/color} are on the bridge, discussing something as they look at the flowing, clear stream. They welcome you politely and ask you about your day.
        '
        '“I have some good news for you. I helped {color=#f6d6bd}the boys from Foggy’s{/color} catch a large bird that will soon be brought here.”' if quest_birdhunting_description06 and not quest_birdhunting_description07 and foragingground_bird_taken == 1:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have some good news for you. I helped {color=#f6d6bd}the boys from Foggy’s{/color} catch a large bird that will soon be brought here.”')
            $ creeks_reputation += 1
            $ foragers_friendship += 1
            $ minutes += 5
            menu:
                'While you try to stay to the point, {color=#f6d6bd}Efren{/color} is full of energy. He asks about every detail, from the animal’s size to the way it acted in combat. Your brief answers are met with shouts, echoed by the silent bounces of the wolf’s head.
                \n\n“It was a brave venture, I’m glad they didn’t try it without you.” {color=#f6d6bd}Elah{/color} gestures for {color=#f6d6bd}the hunter{/color} to drop it. “Thank you for giving us time to prepare.”
                '
                '“I was also told to ask for one dragon bone.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I was also told to ask for one dragon bone.”')
                    show screen notifyimage( "Quest completed: Bird Hunt.\n+1", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Bird Hunt. +1 {image=cointest}{/i}')
                    $ quest_birdhunting_description08 = "I received my reward for delivering the message."
                    $ quest_birdhunting = 2
                    $ coins += 1
                    $ minutes += 5
                    $ efren_friendship += 1
                    $ elah_efren_siblings = 1
                    $ questionpreset = "elah1"
                    menu:
                        '“Aye, of course.” {color=#f6d6bd}The carpenter{/color} looks around. “Pay for the messenger... Just give me a minute.” He scurries away, as quickly as his thick legs allow him. “We don’t carry dragons with us,” {color=#f6d6bd}the hunter{/color} explains. “So, how large is the beak? Something like this?” He demonstrates the size with his hands, and for another few minutes showers you with questions.
                        \n\nFinally, the dragon bone finds its place in your hand. “I... I’ll get to preparations soon,” concludes {color=#f6d6bd}Elah{/color}, gasping for air and leaning against the railing, while {color=#f6d6bd}Efren{/color} lopes away, apparently to “prepare the animal pen” as “there’s no time to waste.” {color=#f6d6bd}The carpenter{/color} invites you to follow him to his working station.
                        '
                        '(elah1 set)':
                            pass
                'I smile. “Yep. We did good.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Yep. We did good.”')
                    $ renpy.notify("Quest completed: Bird Hunting")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Bird Hunting{/i}')
                    $ quest_birdhunting_description08 = "I delivered the message."
                    $ quest_birdhunting = 2
                    $ elah_friendship += 1
                    $ questionpreset = "elah1"
                    menu:
                        '{color=#f6d6bd}Efren{/color} praises your bravery and lopes away, apparently to “prepare the animal pen.” {color=#f6d6bd}Elah{/color} watches him with a smile, and chuckles after the wolf’s head bounces so much that it lands on his back. He then invites you to follow him to his working station.
                        '
                        '(elah1 set)':
                            pass

label creeksaftersleep01:
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    if not creeks_offeredtojoin:
        if not renpy.music.get_playing(channel='music') == "<loop 18.6>audio/track_11creeks01loop.ogg":
            play music "<loop 18.6>audio/track_11creeks01loop.ogg" fadeout 1.0 fadein 1.0
    else:
        $ renpy.music.play("audio/track_11creeks02.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    stop nature fadeout 4.0
    if not creeks_feast:
        show areapicture creeks01 at basicfade
    else:
        show areapicture creeks01alt1 at basicfade
    nvl clear
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    if day == 6 or day == 12 or day == 18 or day == 24 or day == 30 or day == 36 or day == 42:
        $ renpy.notify("The days are getting shorter.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}The days are getting shorter.{/i}')
    menu:
        'Some people are preparing to leave, others are in a deep sleep. There are loud conversations coming from the main square, where people are sitting with plates of cold meat and bowls of gruel, chatting about the plans for the day.
        \n\n{color=#f6d6bd}[horsename]{/color} is well-rested and satisfied with grass.
        '
        'I look for {color=#f6d6bd}Elah{/color}, the carpenter.' if elah_lastseen < day and elah_locked != day:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for {color=#f6d6bd}Elah{/color}, the carpenter.')
            jump creekselah01
        'I return to {color=#f6d6bd}Elah{/color}, the carpenter.' if elah_lastseen >= day and elah_locked != day:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Elah{/color}, the carpenter.')
            jump creekselah01
        'Elah won’t speak with me today. (disabled)' if elah_locked == day:
            pass
        'I look for {color=#f6d6bd}Efren{/color}, the hunter.' if efren_lastseen < day:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for {color=#f6d6bd}Efren{/color}, the hunter.')
            jump creeksefren01
        'I return to {color=#f6d6bd}Efren{/color}, the hunter.' if efren_lastseen >= day:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Efren{/color}, the hunter.')
            jump creeksefren01
        'I go to {color=#f6d6bd}Old Hava{/color}, the farmer.' if oldhava_known:
            jump creeksoldhava01
        'I approach the shallow creek.' if not creeks_youth_gambling_invited or (creeks_youth_gambling_invited and creeks_youth_gambling):
            jump creekscreek0201
        'I accept the invitation and head to the creek.' if creeks_youth_gambling_invited and not creeks_youth_gambling:
            jump creekscreek0201
        'Maybe there are some locals looking for a match in other villages.' ( condition="not shoshi_single and quest_matchmaking == 1" ):
            jump creekssinglepeople01firsttime
        'I return to {color=#f6d6bd}Shoshi{/color}.' ( condition="(shoshi_single and quest_matchmaking == 1 and not shoshi_notmatched and galerocks_singlepeople_firsttime and not shoshi_marina) or (shoshi_single and quest_matchmaking == 1 and not shoshi_notmatched and shoshi_marina and galerocks_singlepeople_marina_religion1 and not shoshi_religion) or (quest_recruitahunter_noonerecruited and shoshi_notmatched and not quest_recruitahunter_spokento_shoshi)" ):
            jump creekssinglepeople01
        'I still need to find a match for Shoshi. (disabled)' ( condition="shoshi_single and quest_matchmaking == 1 and not galerocks_singlepeople_firsttime" ):
            pass
        'Shoshi is waiting for a message from Marina. (disabled)' ( condition="shoshi_single and quest_matchmaking == 1 and shoshi_marina and not galerocks_singlepeople_marina_religion1" ):
            pass
        '{image=cointest} I have a day to spare. I ask around to see if any locals need protection on the roads.' ( condition="creeks_mundanework and quarters <= 40 and (creeks_mundanework_counter < day)" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Elah{/color}, the carpenter.')
            jump creeksmundanework01
        '{image=coingray} The locals won’t need my services before day [creeks_mundanework_counter]. (disabled)' ( condition="creeks_mundanework and (creeks_mundanework_counter >= day)" ):
            pass
        '{image=coingray} At such a late hour the locals won’t be interested in my services. (disabled)' ( condition="creeks_mundanework and quarters > 40" ):
            pass

label creeksaftersleep2resting:
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    if not creeks_offeredtojoin:
        if not renpy.music.get_playing(channel='music') == "<loop 18.6>audio/track_11creeks01loop.ogg":
            play music "<loop 18.6>audio/track_11creeks01loop.ogg" fadeout 1.0 fadein 1.0
    else:
        $ renpy.music.play("audio/track_11creeks02.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    stop nature fadeout 4.0
    if not creeks_feast:
        show areapicture creeks01 at basicfade
    else:
        show areapicture creeks01alt1 at basicfade
    nvl clear
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    if day == 6 or day == 12 or day == 18 or day == 24 or day == 30 or day == 36 or day == 42:
        $ renpy.notify("The days are getting shorter.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}The days are getting shorter.{/i}')
    menu:
        '[custom6] {color=#f6d6bd}[horsename]{/color} is well-rested and satisfied with grass.
        '
        'I look for {color=#f6d6bd}Elah{/color}, the carpenter.' if elah_lastseen < day and elah_locked != day:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for {color=#f6d6bd}Elah{/color}, the carpenter.')
            jump creekselah01
        'I return to {color=#f6d6bd}Elah{/color}, the carpenter.' if elah_lastseen >= day and elah_locked != day:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Elah{/color}, the carpenter.')
            jump creekselah01
        'Elah won’t speak with me today. (disabled)' if elah_locked == day:
            pass
        'I look for {color=#f6d6bd}Efren{/color}, the hunter.' if efren_lastseen < day:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for {color=#f6d6bd}Efren{/color}, the hunter.')
            jump creeksefren01
        'I return to {color=#f6d6bd}Efren{/color}, the hunter.' if efren_lastseen >= day:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Efren{/color}, the hunter.')
            jump creeksefren01
        'I go to {color=#f6d6bd}Old Hava{/color}, the farmer.' if oldhava_known:
            jump creeksoldhava01
        'I approach the shallow creek.' if not creeks_youth_gambling_invited or (creeks_youth_gambling_invited and creeks_youth_gambling):
            jump creekscreek0201
        'I accept the invitation and head to the creek.' if creeks_youth_gambling_invited and not creeks_youth_gambling:
            jump creekscreek0201
        'Maybe there are some locals looking for a match in other villages.' ( condition="not shoshi_single and quest_matchmaking == 1" ):
            jump creekssinglepeople01firsttime
        'I return to {color=#f6d6bd}Shoshi{/color}.' ( condition="(shoshi_single and quest_matchmaking == 1 and not shoshi_notmatched and galerocks_singlepeople_firsttime and not shoshi_marina) or (shoshi_single and quest_matchmaking == 1 and not shoshi_notmatched and shoshi_marina and galerocks_singlepeople_marina_religion1 and not shoshi_religion) or (quest_recruitahunter_noonerecruited and shoshi_notmatched and not quest_recruitahunter_spokento_shoshi)" ):
            jump creekssinglepeople01
        'I still need to find a match for Shoshi. (disabled)' ( condition="shoshi_single and quest_matchmaking == 1 and not galerocks_singlepeople_firsttime" ):
            pass
        'Shoshi is waiting for a message from Marina. (disabled)' ( condition="shoshi_single and quest_matchmaking == 1 and shoshi_marina and not galerocks_singlepeople_marina_religion1" ):
            pass
        '{image=cointest} I have a day to spare. I ask around to see if any locals need protection on the roads.' ( condition="creeks_mundanework and quarters <= 40 and (creeks_mundanework_counter < day)" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Elah{/color}, the carpenter.')
            jump creeksmundanework01
        '{image=coingray} The locals won’t need my services before day [creeks_mundanework_counter]. (disabled)' ( condition="creeks_mundanework and (creeks_mundanework_counter >= day)" ):
            pass
        '{image=coingray} At such a late hour the locals won’t be interested in my services. (disabled)' ( condition="creeks_mundanework and quarters > 40" ):
            pass

label creeksaftersleep02food:
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    if not creeks_offeredtojoin:
        if not renpy.music.get_playing(channel='music') == "<loop 18.6>audio/track_11creeks01loop.ogg":
            play music "<loop 18.6>audio/track_11creeks01loop.ogg" fadeout 1.0 fadein 1.0
    else:
        $ renpy.music.play("audio/track_11creeks02.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    stop nature fadeout 4.0
    if not creeks_feast:
        show areapicture creeks01 at basicfade
    else:
        show areapicture creeks01alt1 at basicfade
    nvl clear
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    if day == 6 or day == 12 or day == 18 or day == 24 or day == 30 or day == 36 or day == 42:
        $ renpy.notify("The days are getting shorter.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}The days are getting shorter.{/i}')
    menu:
        '[custom6] {color=#f6d6bd}[horsename]{/color} is well-rested and satisfied with grass.
        '
        'I look for {color=#f6d6bd}Elah{/color}, the carpenter.' if elah_lastseen < day and elah_locked != day:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for {color=#f6d6bd}Elah{/color}, the carpenter.')
            jump creekselah01
        'I return to {color=#f6d6bd}Elah{/color}, the carpenter.' if elah_lastseen >= day and elah_locked != day:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Elah{/color}, the carpenter.')
            jump creekselah01
        'Elah won’t speak with me today. (disabled)' if elah_locked == day:
            pass
        'I look for {color=#f6d6bd}Efren{/color}, the hunter.' if efren_lastseen < day:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for {color=#f6d6bd}Efren{/color}, the hunter.')
            jump creeksefren01
        'I return to {color=#f6d6bd}Efren{/color}, the hunter.' if efren_lastseen >= day:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Efren{/color}, the hunter.')
            jump creeksefren01
        'I go to {color=#f6d6bd}Old Hava{/color}, the farmer.' if oldhava_known:
            jump creeksoldhava01
        'I approach the shallow creek.' if not creeks_youth_gambling_invited or (creeks_youth_gambling_invited and creeks_youth_gambling):
            jump creekscreek0201
        'I accept the invitation and head to the creek.' if creeks_youth_gambling_invited and not creeks_youth_gambling:
            jump creekscreek0201
        'Maybe there are some locals looking for a match in other villages.' ( condition="not shoshi_single and quest_matchmaking == 1" ):
            jump creekssinglepeople01firsttime
        'I return to {color=#f6d6bd}Shoshi{/color}.' ( condition="(shoshi_single and quest_matchmaking == 1 and not shoshi_notmatched and galerocks_singlepeople_firsttime and not shoshi_marina) or (shoshi_single and quest_matchmaking == 1 and not shoshi_notmatched and shoshi_marina and galerocks_singlepeople_marina_religion1 and not shoshi_religion) or (quest_recruitahunter_noonerecruited and shoshi_notmatched and not quest_recruitahunter_spokento_shoshi)" ):
            jump creekssinglepeople01
        'I still need to find a match for Shoshi. (disabled)' ( condition="shoshi_single and quest_matchmaking == 1 and not galerocks_singlepeople_firsttime" ):
            pass
        'Shoshi is waiting for a message from Marina. (disabled)' ( condition="shoshi_single and quest_matchmaking == 1 and shoshi_marina and not galerocks_singlepeople_marina_religion1" ):
            pass
        '{image=cointest} I have a day to spare. I ask around to see if any locals need protection on the roads.' ( condition="creeks_mundanework and quarters <= 40 and (creeks_mundanework_counter < day)" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Elah{/color}, the carpenter.')
            jump creeksmundanework01
        '{image=coingray} The locals won’t need my services before day [creeks_mundanework_counter]. (disabled)' ( condition="creeks_mundanework and (creeks_mundanework_counter >= day)" ):
            pass
        '{image=coingray} At such a late hour the locals won’t be interested in my services. (disabled)' ( condition="creeks_mundanework and quarters > 40" ):
            pass

label creeksaftersleep2chatting:
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    if not creeks_offeredtojoin:
        if not renpy.music.get_playing(channel='music') == "<loop 18.6>audio/track_11creeks01loop.ogg":
            play music "<loop 18.6>audio/track_11creeks01loop.ogg" fadeout 1.0 fadein 1.0
    else:
        $ renpy.music.play("audio/track_11creeks02.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    stop nature fadeout 4.0
    if not creeks_feast:
        show areapicture creeks01 at basicfade
    else:
        show areapicture creeks01alt1 at basicfade
    nvl clear
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    if day == 6 or day == 12 or day == 18 or day == 24 or day == 30 or day == 36 or day == 42:
        $ renpy.notify("The days are getting shorter.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}The days are getting shorter.{/i}')
    menu:
        '[custom6] {color=#f6d6bd}[horsename]{/color} is well-rested and satisfied with grass.
        '
        'I look for {color=#f6d6bd}Elah{/color}, the carpenter.' if elah_lastseen < day and elah_locked != day:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for {color=#f6d6bd}Elah{/color}, the carpenter.')
            jump creekselah01
        'I return to {color=#f6d6bd}Elah{/color}, the carpenter.' if elah_lastseen >= day and elah_locked != day:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Elah{/color}, the carpenter.')
            jump creekselah01
        'Elah won’t speak with me today. (disabled)' if elah_locked == day:
            pass
        'I look for {color=#f6d6bd}Efren{/color}, the hunter.' if efren_lastseen < day:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for {color=#f6d6bd}Efren{/color}, the hunter.')
            jump creeksefren01
        'I return to {color=#f6d6bd}Efren{/color}, the hunter.' if efren_lastseen >= day:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Efren{/color}, the hunter.')
            jump creeksefren01
        'I go to {color=#f6d6bd}Old Hava{/color}, the farmer.' if oldhava_known:
            jump creeksoldhava01
        'I approach the shallow creek.' if not creeks_youth_gambling_invited or (creeks_youth_gambling_invited and creeks_youth_gambling):
            jump creekscreek0201
        'I accept the invitation and head to the creek.' if creeks_youth_gambling_invited and not creeks_youth_gambling:
            jump creekscreek0201
        'Maybe there are some locals looking for a match in other villages.' ( condition="not shoshi_single and quest_matchmaking == 1" ):
            jump creekssinglepeople01firsttime
        'I return to {color=#f6d6bd}Shoshi{/color}.' ( condition="(shoshi_single and quest_matchmaking == 1 and not shoshi_notmatched and galerocks_singlepeople_firsttime and not shoshi_marina) or (shoshi_single and quest_matchmaking == 1 and not shoshi_notmatched and shoshi_marina and galerocks_singlepeople_marina_religion1 and not shoshi_religion) or (quest_recruitahunter_noonerecruited and shoshi_notmatched and not quest_recruitahunter_spokento_shoshi)" ):
            jump creekssinglepeople01
        'I still need to find a match for Shoshi. (disabled)' ( condition="shoshi_single and quest_matchmaking == 1 and not galerocks_singlepeople_firsttime" ):
            pass
        'Shoshi is waiting for a message from Marina. (disabled)' ( condition="shoshi_single and quest_matchmaking == 1 and shoshi_marina and not galerocks_singlepeople_marina_religion1" ):
            pass
        '{image=cointest} I have a day to spare. I ask around to see if any locals need protection on the roads.' ( condition="creeks_mundanework and quarters <= 40 and (creeks_mundanework_counter < day)" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Elah{/color}, the carpenter.')
            jump creeksmundanework01
        '{image=coingray} The locals won’t need my services before day [creeks_mundanework_counter]. (disabled)' ( condition="creeks_mundanework and (creeks_mundanework_counter >= day)" ):
            pass
        '{image=coingray} At such a late hour the locals won’t be interested in my services. (disabled)' ( condition="creeks_mundanework and quarters > 40" ):
            pass

label creeksaftersleep2sex:
    if not creeks_offeredtojoin:
        if not renpy.music.get_playing(channel='music') == "<loop 18.6>audio/track_11creeks01loop.ogg":
            play music "<loop 18.6>audio/track_11creeks01loop.ogg" fadeout 1.0 fadein 1.0
    else:
        $ renpy.music.play("audio/track_11creeks02.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    stop nature fadeout 4.0
    if not creeks_feast:
        show areapicture creeks01 at basicfade
    else:
        show areapicture creeks01alt1 at basicfade
    nvl clear
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    if day == 6 or day == 12 or day == 18 or day == 24 or day == 30 or day == 36 or day == 42:
        $ renpy.notify("The days are getting shorter.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}The days are getting shorter.{/i}')
    menu:
        'After a few hours spent on a pile of furs...
        '
        '...I’m woken up by my companion, who is getting dressed in the early morning light.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- ...I’m woken up by my companion, who is getting dressed in the early morning light.')
            $ creeks_youth_gambling = 4
            $ creeks_youth_sex = 1
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            menu:
                'You watch through eyes half-lidded with sleep as the skin you’d only recently caressed gets covered with leathers and furs, growing more distant with each piece of clothing. Most of the people resting in the large room have already left, but, as if to let you sleep, your erstwhile companion holds their boots in their hand, slipping out the exit.
                \n\nAs you gather your senses, you think about the last words you heard before you fell asleep. “Come to me in spring.”
                \n\nWhen you leave the building, the square is filled with loud conversations. The locals are sitting with plates of cold meat and bowls of gruel, chatting about the plans for the day. Many of them wish you a great day. {color=#f6d6bd}[horsename]{/color} is well-rested and satisfied with grass.
                '
                'I look for {color=#f6d6bd}Elah{/color}, the carpenter.' if elah_lastseen < day and elah_locked != day:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for {color=#f6d6bd}Elah{/color}, the carpenter.')
                    jump creekselah01
                'I return to {color=#f6d6bd}Elah{/color}, the carpenter.' if elah_lastseen >= day and elah_locked != day:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Elah{/color}, the carpenter.')
                    jump creekselah01
                'Elah won’t speak with me today. (disabled)' if elah_locked == day:
                    pass
                'I look for {color=#f6d6bd}Efren{/color}, the hunter.' if efren_lastseen < day:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for {color=#f6d6bd}Efren{/color}, the hunter.')
                    jump creeksefren01
                'I return to {color=#f6d6bd}Efren{/color}, the hunter.' if efren_lastseen >= day:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Efren{/color}, the hunter.')
                    jump creeksefren01
                'I go to {color=#f6d6bd}Old Hava{/color}, the farmer.' if oldhava_known:
                    jump creeksoldhava01
                'I approach the shallow creek.' if not creeks_youth_gambling_invited or (creeks_youth_gambling_invited and creeks_youth_gambling):
                    jump creekscreek0201
                'I accept the invitation and head to the creek.' if creeks_youth_gambling_invited and not creeks_youth_gambling:
                    jump creekscreek0201
                'Maybe there are some locals looking for a match in other villages.' ( condition="not shoshi_single and quest_matchmaking == 1" ):
                    jump creekssinglepeople01firsttime
                'I return to {color=#f6d6bd}Shoshi{/color}.' ( condition="(shoshi_single and quest_matchmaking == 1 and not shoshi_notmatched and galerocks_singlepeople_firsttime and not shoshi_marina) or (shoshi_single and quest_matchmaking == 1 and not shoshi_notmatched and shoshi_marina and galerocks_singlepeople_marina_religion1 and not shoshi_religion) or (quest_recruitahunter_noonerecruited and shoshi_notmatched and not quest_recruitahunter_spokento_shoshi)" ):
                    jump creekssinglepeople01
                'I still need to find a match for Shoshi. (disabled)' ( condition="shoshi_single and quest_matchmaking == 1 and not galerocks_singlepeople_firsttime" ):
                    pass
                'Shoshi is waiting for a message from Marina. (disabled)' ( condition="shoshi_single and quest_matchmaking == 1 and shoshi_marina and not galerocks_singlepeople_marina_religion1" ):
                    pass
                '{image=cointest} I have a day to spare. I ask around to see if any locals need protection on the roads.' ( condition="creeks_mundanework and quarters <= 40 and (creeks_mundanework_counter < day)" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Elah{/color}, the carpenter.')
                    jump creeksmundanework01
                '{image=coingray} The locals won’t need my services before day [creeks_mundanework_counter]. (disabled)' ( condition="creeks_mundanework and (creeks_mundanework_counter >= day)" ):
                    pass
                '{image=coingray} At such a late hour the locals won’t be interested in my services. (disabled)' ( condition="creeks_mundanework and quarters > 40" ):
                    pass
        '...I’m by myself, thinking about the feast and the time I spent with the group of young people.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- ...I’m by myself, thinking about the feast and the time I spent with the group of young people.')
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            menu:
                'You told them about the many places and creatures that you have seen, about the inns and their food in the South, what living in {color=#f6d6bd}Hovlavan{/color} is like, and when there was nothing else to say, you noticed your aching throat. In return, you received tales of hunts and memories of petty squabbles that, after seasons, cause mostly laughter and embarrassment. The warm arms of your companions see you through the cold night in comfort.
                \n\nWhen you leave the building, the square is filled with loud conversations. The locals are sitting with plates of cold meat and bowls of gruel, chatting about the plans for the day. Many of them wish you a great day. {color=#f6d6bd}[horsename]{/color} is well-rested and satisfied with grass.
                '
                'I look for {color=#f6d6bd}Elah{/color}, the carpenter.' if elah_lastseen < day and elah_locked != day:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for {color=#f6d6bd}Elah{/color}, the carpenter.')
                    jump creekselah01
                'I return to {color=#f6d6bd}Elah{/color}, the carpenter.' if elah_lastseen >= day and elah_locked != day:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Elah{/color}, the carpenter.')
                    jump creekselah01
                'Elah won’t speak with me today. (disabled)' if elah_locked == day:
                    pass
                'I look for {color=#f6d6bd}Efren{/color}, the hunter.' if efren_lastseen < day:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for {color=#f6d6bd}Efren{/color}, the hunter.')
                    jump creeksefren01
                'I return to {color=#f6d6bd}Efren{/color}, the hunter.' if efren_lastseen >= day:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Efren{/color}, the hunter.')
                    jump creeksefren01
                'I go to {color=#f6d6bd}Old Hava{/color}, the farmer.' if oldhava_known:
                    jump creeksoldhava01
                'I approach the shallow creek.' if not creeks_youth_gambling_invited or (creeks_youth_gambling_invited and creeks_youth_gambling):
                    jump creekscreek0201
                'I accept the invitation and head to the creek.' if creeks_youth_gambling_invited and not creeks_youth_gambling:
                    jump creekscreek0201
                'Maybe there are some locals looking for a match in other villages.' ( condition="not shoshi_single and quest_matchmaking == 1" ):
                    jump creekssinglepeople01firsttime
                'I return to {color=#f6d6bd}Shoshi{/color}.' ( condition="(shoshi_single and quest_matchmaking == 1 and not shoshi_notmatched and galerocks_singlepeople_firsttime and not shoshi_marina) or (shoshi_single and quest_matchmaking == 1 and not shoshi_notmatched and shoshi_marina and galerocks_singlepeople_marina_religion1 and not shoshi_religion) or (quest_recruitahunter_noonerecruited and shoshi_notmatched and not quest_recruitahunter_spokento_shoshi)" ):
                    jump creekssinglepeople01
                'I still need to find a match for Shoshi. (disabled)' ( condition="shoshi_single and quest_matchmaking == 1 and not galerocks_singlepeople_firsttime" ):
                    pass
                'Shoshi is waiting for a message from Marina. (disabled)' ( condition="shoshi_single and quest_matchmaking == 1 and shoshi_marina and not galerocks_singlepeople_marina_religion1" ):
                    pass
                '{image=cointest} I have a day to spare. I ask around to see if any locals need protection on the roads.' ( condition="creeks_mundanework and quarters <= 40 and (creeks_mundanework_counter < day)" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Elah{/color}, the carpenter.')
                    jump creeksmundanework01
                '{image=coingray} The locals won’t need my services before day [creeks_mundanework_counter]. (disabled)' ( condition="creeks_mundanework and (creeks_mundanework_counter >= day)" ):
                    pass
                '{image=coingray} At such a late hour the locals won’t be interested in my services. (disabled)' ( condition="creeks_mundanework and quarters > 40" ):
                    pass

label creeksmundanework01:
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    show screen mundanejob() with dissolve
    menu:
        'You ask if anyone needs your help.
        '
        'I look for {color=#f6d6bd}Elah{/color}, the carpenter.' if elah_lastseen < day and elah_locked != day:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for {color=#f6d6bd}Elah{/color}, the carpenter.')
            jump creekselah01
        'I return to {color=#f6d6bd}Elah{/color}, the carpenter.' if elah_lastseen >= day and elah_locked != day:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Elah{/color}, the carpenter.')
            jump creekselah01
        'Elah won’t speak with me today. (disabled)' if elah_locked == day:
            pass
        'I look for {color=#f6d6bd}Efren{/color}, the hunter.' if efren_lastseen < day:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for {color=#f6d6bd}Efren{/color}, the hunter.')
            jump creeksefren01
        'I return to {color=#f6d6bd}Efren{/color}, the hunter.' if efren_lastseen >= day:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Efren{/color}, the hunter.')
            jump creeksefren01
        'I go to {color=#f6d6bd}Old Hava{/color}, the farmer.' if oldhava_known:
            jump creeksoldhava01
        'I approach the shallow creek.' if not creeks_youth_gambling_invited or (creeks_youth_gambling_invited and creeks_youth_gambling):
            jump creekscreek0201
        'I accept the invitation and head to the creek.' if creeks_youth_gambling_invited and not creeks_youth_gambling:
            jump creekscreek0201
        'Maybe there are some locals looking for a match in other villages.' ( condition="not shoshi_single and quest_matchmaking == 1" ):
            jump creekssinglepeople01firsttime
        'I return to {color=#f6d6bd}Shoshi{/color}.' ( condition="(shoshi_single and quest_matchmaking == 1 and not shoshi_notmatched and galerocks_singlepeople_firsttime and not shoshi_marina) or (shoshi_single and quest_matchmaking == 1 and not shoshi_notmatched and shoshi_marina and galerocks_singlepeople_marina_religion1 and not shoshi_religion) or (quest_recruitahunter_noonerecruited and shoshi_notmatched and not quest_recruitahunter_spokento_shoshi)" ):
            jump creekssinglepeople01
        'I still need to find a match for Shoshi. (disabled)' ( condition="shoshi_single and quest_matchmaking == 1 and not galerocks_singlepeople_firsttime" ):
            pass
        'Shoshi is waiting for a message from Marina. (disabled)' ( condition="shoshi_single and quest_matchmaking == 1 and shoshi_marina and not galerocks_singlepeople_marina_religion1" ):
            pass
        '{image=cointest} I have a day to spare. I ask around to see if any locals need protection on the roads.' ( condition="creeks_mundanework and quarters <= 40 and (creeks_mundanework_counter < day)" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Elah{/color}, the carpenter.')
            jump creeksmundanework01
        '{image=coingray} The locals won’t need my services before day [creeks_mundanework_counter]. (disabled)' ( condition="creeks_mundanework and (creeks_mundanework_counter >= day)" ):
            pass
        '{image=coingray} At such a late hour the locals won’t be interested in my services. (disabled)' ( condition="creeks_mundanework and quarters > 40" ):
            pass

    label creeksaftermundanejob:
        $ creeks_mundanework_counter = (day+2)
        $ creeks_mundanework_numberoftimes += 1
        $ creeks_reputation += 1
        $ quest_easternpath_points += 1
        $ d100roll = 0
        $ d100roll = renpy.random.randint(1, 100)
        $ d100roll += (50-(quest_easternpath_points*10))
        if pc_class == "warrior":
            $ d100roll -= (pc_battlecounter)
        else:
            $ d100roll -= (pc_battlecounter/2)
        nvl clear
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        if d100roll > 90:
            $ custom1 = "A tragic encounter puts your life in danger, but you manage to get away to safety. Your clothes are in terrible shape."
            $ pc_battlecounter += 1
            if armor >= 3:
                $ armor = limit_armor(armor-2)
                show minus2armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 armor points.{/i}')
            elif armor >= 2:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            else:
                $ pc_hp = limit_pc_hp(pc_hp-2)
                show minus2hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
            $ cleanliness_clothes_torn = 1
            $ cleanliness_clothes_blood = 1
            $ cleanliness = limit_cleanliness(cleanliness-2)
            show minus4appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-4 appearance points.{/i}')
            $ quarters = (world_daylength-12)
        elif d100roll > 60:
            $ custom1 = "At one point you have to flee desperately toward safety. You’re tired, and your clothes get torn in the process."
            if armor >= 2:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
            else:
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            $ cleanliness_clothes_torn = 1
            $ cleanliness = limit_cleanliness(cleanliness-2)
            show minus3appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 appearance points.{/i}')
            $ quarters = (world_daylength-16)
        elif d100roll > 40:
            if armor < 2:
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ custom1 = "For most of the time you stay safe, but at one point you find yourself evading a pack of predators, and your clothes are now soaked in sweat."
            else:
                $ custom1 = "For most of the time you stay safe, but at one point you find yourself evading a pack of predators, and your clothes are now soaked in sweat. Thankfully, your armor was able to keep you in one piece."
            $ cleanliness = limit_cleanliness(cleanliness-2)
            show minus2appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
            $ quarters = (world_daylength-18)
        elif d100roll > 20:
            $ custom1 = "For most of the time you stay safe, but at one point you find yourself evading a pack of predators, and your clothes are now soaked in sweat."
            $ cleanliness = limit_cleanliness(cleanliness-2)
            show minus2appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
            $ quarters = (world_daylength-18)
        else:
            $ custom1 = "It turns out you don’t have much to do. You get your job done quickly and with little difficulty."
            $ cleanliness = limit_cleanliness(cleanliness-1)
            show minus1appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            $ quarters = (world_daylength-12)
        $ pc_food = limit_pc_food(pc_food+2)
        show plus2food at foodchange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 nourishment points.{/i}')
        $ coins += creeks_mundanework_payment
        show screen notifyimage( "+%s" %creeks_mundanework_payment, "gui/coin2.png" )
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+%s {image=cointest}{/i}' %howlersdell_mundanework_payment_total)
        menu:
            '[custom1]
            '
            'I look for {color=#f6d6bd}Elah{/color}, the carpenter.' if elah_lastseen < day and elah_locked != day:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for {color=#f6d6bd}Elah{/color}, the carpenter.')
                jump creekselah01
            'I return to {color=#f6d6bd}Elah{/color}, the carpenter.' if elah_lastseen >= day and elah_locked != day:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Elah{/color}, the carpenter.')
                jump creekselah01
            'Elah won’t speak with me today. (disabled)' if elah_locked == day:
                pass
            'I look for {color=#f6d6bd}Efren{/color}, the hunter.' if efren_lastseen < day:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for {color=#f6d6bd}Efren{/color}, the hunter.')
                jump creeksefren01
            'I return to {color=#f6d6bd}Efren{/color}, the hunter.' if efren_lastseen >= day:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Efren{/color}, the hunter.')
                jump creeksefren01
            'I go to {color=#f6d6bd}Old Hava{/color}, the farmer.' if oldhava_known:
                jump creeksoldhava01
            'I approach the shallow creek.' if not creeks_youth_gambling_invited or (creeks_youth_gambling_invited and creeks_youth_gambling):
                jump creekscreek0201
            'I accept the invitation and head to the creek.' if creeks_youth_gambling_invited and not creeks_youth_gambling:
                jump creekscreek0201
            'Maybe there are some locals looking for a match in other villages.' ( condition="not shoshi_single and quest_matchmaking == 1" ):
                jump creekssinglepeople01firsttime
            'I return to {color=#f6d6bd}Shoshi{/color}.' ( condition="(shoshi_single and quest_matchmaking == 1 and not shoshi_notmatched and galerocks_singlepeople_firsttime and not shoshi_marina) or (shoshi_single and quest_matchmaking == 1 and not shoshi_notmatched and shoshi_marina and galerocks_singlepeople_marina_religion1 and not shoshi_religion) or (quest_recruitahunter_noonerecruited and shoshi_notmatched and not quest_recruitahunter_spokento_shoshi)" ):
                jump creekssinglepeople01
            'I still need to find a match for Shoshi. (disabled)' ( condition="shoshi_single and quest_matchmaking == 1 and not galerocks_singlepeople_firsttime" ):
                pass
            'Shoshi is waiting for a message from Marina. (disabled)' ( condition="shoshi_single and quest_matchmaking == 1 and shoshi_marina and not galerocks_singlepeople_marina_religion1" ):
                pass
            '{image=cointest} I have a day to spare. I ask around to see if any locals need protection on the roads.' ( condition="creeks_mundanework and quarters <= 40 and (creeks_mundanework_counter < day)" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Elah{/color}, the carpenter.')
                jump creeksmundanework01
            '{image=coingray} The locals won’t need my services before day [creeks_mundanework_counter]. (disabled)' ( condition="creeks_mundanework and (creeks_mundanework_counter >= day)" ):
                pass
            '{image=coingray} At such a late hour the locals won’t be interested in my services. (disabled)' ( condition="creeks_mundanework and quarters > 40" ):
                pass

label creekscreek0201:
    if not creeks_youth_gambling_invited or (creeks_youth_gambling_invited and creeks_youth_gambling):
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the shallow creek.')
    else:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I accept the invitation and head to the creek.')
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the shallow creek.')
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ creeks_youth_gambling_invited = 0
    if creeks_reputation >= 6 and appearance_charisma >= 1 and not creeks_youth_gambling and creeks_youth_lookedat:
        jump creekscreek0202
    if cleanliness_equipment <= 0:
        $ custom1 = "{color=#6a6a6a}You need at least 2 pieces of bathing equipment to get more out of this place.{/color}"
        $ custom2 = ""
    elif cleanliness_equipment == 1:
        if item_soap:
            $ custom1 = "The oak-ash soap you own is not enough to help you get cleaner."
        elif item_teethset:
            $ custom1 = "The teeth set you own is not enough to help you get cleaner."
        elif item_perfume:
            $ custom1 = "The perfume you own is not enough to help you get cleaner."
        $ custom2 = "\n\n{color=#6a6a6a}You need at least 2 pieces of bathing equipment to get more out of this place.{/color}"
    elif cleanliness_equipment == 2:
        if item_soap and item_teethset:
            $ custom1 = "The oak-ash soap and the teeth set you own can help you get cleaner."
        elif item_soap and item_perfume:
            $ custom1 = "The oak-ash soap and the perfume you own can help you get cleaner."
        elif item_teethset and item_perfume:
            $ custom1 = "The teeth set and the perfume you own can help you get cleaner."
        $ custom2 = ""
    elif cleanliness_equipment >= 3:
        $ custom1 = "The oak-ash soap, the teeth set, and the perfume you own can help you get cleaner."
        $ custom2 = ""
    menu:
        'With the calming sounds of the waterfall around you, you observe the stream, as clean as a spring.
        \n\n[custom1][custom2]
        '
        'I jump into the stream.' if (cleanliness < 2 and cleanliness_equipment < 2) or (cleanliness < 3 and cleanliness_equipment >= 2):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I jump into the stream.')
            jump creekscreek02washing01
        'I won’t get any cleaner here. (disabled)' if cleanliness < 3 and cleanliness_equipment < 2:
            pass
        'I’m as clean as I can get. (disabled)' if cleanliness == 3:
            pass
        'In an hour I’ll remove blood stains from my clothes.' if cleanliness_clothes_blood:
            jump creekscreek02laundry01
        'My clothes need no washing. (disabled)' if not cleanliness_clothes_blood:
            pass
        'I step away.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
            jump creeksafterinteraction01
    label creekscreek02washing01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I undress and jump in the creek.')
        if not cleanliness:
            if cleanliness_equipment >= 2:
                $ minutes += 20
                $ cleanliness = limit_cleanliness(cleanliness+3)
                show plus3appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 appearance points.{/i}')
            else:
                $ quarters += 1
                $ cleanliness = limit_cleanliness(cleanliness+2)
                show plus2appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 appearance points.{/i}')
        elif cleanliness == 1:
            if cleanliness_equipment >= 2:
                $ quarters += 1
                $ cleanliness = limit_cleanliness(cleanliness+2)
                show plus2appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 appearance points.{/i}')
            else:
                $ minutes += 10
                $ cleanliness = limit_cleanliness(cleanliness+1)
                show plus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 appearance point.{/i}')
        elif cleanliness == 2:
            $ minutes += 10
            $ cleanliness = limit_cleanliness(cleanliness+1)
            show plus1appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 appearance point.{/i}')
        menu:
            'There are no fish or plants to bother with and your feet find mud among the not-always-smooth pebbles. The water reaches above your waist, allowing you to have some fun and wash every spot of your shell. Thanks to the gentle flow, you are able to remove the mud stains from your clothes and boots.
            '
            'I jump into the stream.' if (cleanliness < 2 and cleanliness_equipment < 2) or (cleanliness < 3 and cleanliness_equipment >= 2):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I jump into the stream.')
                jump creekscreek02washing01
            'I won’t get any cleaner here. (disabled)' if cleanliness < 3 and cleanliness_equipment < 2:
                pass
            'I’m as clean as I can get. (disabled)' if cleanliness == 3:
                pass
            'In an hour I’ll remove blood stains from my clothes.' if cleanliness_clothes_blood:
                jump creekscreek02laundry01
            'My clothes need no washing. (disabled)' if not cleanliness_clothes_blood:
                pass
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump creeksafterinteraction01
    label creekscreek02laundry01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- In an hour I’ll remove blood stains from my clothes.')
        $ cleanliness_clothes_blood = 0
        $ quarters += 4
        show plus1appearance at appearancechange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 appearance point.{/i}')
        menu:
            'Thanks to the bridge, soaking, pounding, and rubbing the fabric goes smoothly.
            '
            'I jump into the stream.' if (cleanliness < 2 and cleanliness_equipment < 2) or (cleanliness < 3 and cleanliness_equipment >= 2):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I jump into the stream.')
                jump creekscreek02washing01
            'I won’t get any cleaner here. (disabled)' if cleanliness < 3 and cleanliness_equipment < 2:
                pass
            'I’m as clean as I can get. (disabled)' if cleanliness == 3:
                pass
            'In an hour I’ll remove blood stains from my clothes.' if cleanliness_clothes_blood:
                jump creekscreek02laundry01
            'My clothes need no washing. (disabled)' if not cleanliness_clothes_blood:
                pass
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump creeksafterinteraction01

label creekscreek0202:
    $ creek_woodenweapons = 1
    $ creeks_youth_gambling = 1
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    if shoshi_namebig == "The dark-haired woodcutter":
        $ custom6 = "The dark-haired, large woman who plays with her massive axe speaks first"
    else:
        $ custom6 = "{color=#f6d6bd}Shoshi{/color}, who plays with her massive axe, speaks first"
    menu:
        'The group of young people at the bridge are still preparing to enter the creek, and are currently whispering to each other and giving you looks. Some of them are naked, others keep half-clothed with pants or a shirt, more to avoid the gusts of wind than anyone’s eyes.
        \n\n[custom6]. “How ‘bout a li’l help? It’s not easy to scratch one’s own back.”
        '
        '“I’d love some company.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d love some company.”')
            $ creeks_reputation += 1
            jump creekscreek0202b
        '“You have enough hands already. I want to wash myself and hit the road.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You have enough hands already. I want to wash myself and hit the road.”')
            $ creeks_reputation -= 1
            if cleanliness_equipment:
                $ custom1 = "\n\nYou could also "
                if item_teethset and item_soap and not item_perfume:
                    $ custom2 = "wash your teeth "
                elif item_teethset:
                    $ custom2 = "wash your teeth, "
                else:
                    $ custom2 = ""
                if item_teethset and item_soap and item_perfume:
                    $ custom3 = "use the oak-ash soap, "
                elif item_soap and item_teethset:
                    $ custom3 = "and use the oak-ash soap, "
                elif item_soap and item_perfume:
                    $ custom3 = "use the oak-ash soap "
                elif item_soap:
                    $ custom3 = "use the oak-ash soap, "
                else:
                    $ custom3 = ""
                if (item_perfume and item_soap) or (item_perfume and item_teethset):
                    $ custom4 = "and sprinkle your hair with perfume, "
                elif item_perfume:
                    $ custom4 = "sprinkle your hair with perfume, "
                else:
                    $ custom4 = ""
                if cleanliness_equipment >= 2:
                    $ custom5 = "which will make you much cleaner."
                else:
                    $ custom5 = "but in this place it’s not enough to make much of a difference."
            else:
                $ custom1 = "\n\nYou have no additional equipment that could help you here."
                $ custom2 = ""
                $ custom3 = ""
                $ custom4 = ""
                $ custom5 = ""
            menu:
                'They give you awkward looks and, after spending a few minutes pretending that it wasn’t a serious offer and they’d rather bathe at a later hour, they leave you to yourself.
                \n\nWith the calming sounds of the waterfall around you, you observe the stream, as clean as a spring. [custom1][custom2][custom3][custom4][custom5]
                '
                'I jump into the stream.' if (cleanliness < 2 and cleanliness_equipment < 2) or (cleanliness < 3 and cleanliness_equipment >= 2):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I jump into the stream.')
                    jump creekscreek02washing01
                'I won’t get any cleaner here. (disabled)' if cleanliness < 3 and cleanliness_equipment < 2:
                    pass
                'I’m as clean as I can get. (disabled)' if cleanliness == 3:
                    pass
                'In an hour I’ll remove blood stains from my clothes.' if cleanliness_clothes_blood:
                    jump creekscreek02laundry01
                'My clothes need no washing. (disabled)' if not cleanliness_clothes_blood:
                    pass
                'I step away.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                    jump creeksafterinteraction01

    label creekscreek0202b:
        $ quarters += 1
        menu:
            'The seven souls encourage you to strip, but don’t wait for you. The splashes are followed both by chuckling and grumbling about the cold water, and once you join the others, you’re neither ignored, nor at the center of attention. Playful nudges and submerging are indeed accompanied by helping each other with washing hard-to-reach spots, and you find that the locals have surprisingly strong arms, proving they have many days of hard labor behind them.
            \n\nAfter a few active minutes, two male lovers compete against one another by swimming with and against the flow, comparing their speed. The others spread along the banks, chatting about this and that. In a moment of silence, you decide to direct the topic slightly.
            '
            '“So how do you feel about {color=#f6d6bd}Creeks{/color}? Do you enjoy living here?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So how do you feel about {color=#f6d6bd}Creeks{/color}? Do you enjoy living here?”')
                $ creeks_reasonstojoin_hpcknowstruthaboutinbreeding = 1
                if shoshi_namebig == "The dark-haired woodcutter":
                    $ custom1 = "The answers vary. The dark-haired woodcutter plans to move to a different settlement, another one hopes to see the lands beyond the peninsula. Two would like to start families here since they feel free and loved in their tribe, while the last two hope to still change some things about this place before they decide for sure."
                else:
                    $ custom1 = "The answers vary. {color=#f6d6bd}Shoshi{/color} plans to move to a different settlement, another one hopes to see the lands beyond the peninsula. Two would like to start families here since they feel free and loved in their tribe, while the last two hope to still change some things about this place before they decide for sure."
                jump creekscreek0202c
            '“The water here is so lovely.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The water here is so lovely.”')
                if shoshi_namebig == "The dark-haired woodcutter":
                    $ custom1 = "The laziness of your observation instantly fills the air. A short woman with wavy hair, which she keeps dry like an ornament, closes her eyes and tilts her head back, resting it on the grass. “Aye, and the weather is never too harsh, though once the snows fall, even {color=#f6d6bd}Foggy{/color} has to move back in. We spend winters in our house of gatherings, burning wood and killing time.” A few more good moments go by like this. “It’s a good land, even if a small one,” concludes the dark-haired woman."
                else:
                    $ custom1 = "The laziness of your observation instantly fills the air. A short woman with wavy hair, which she keeps dry like an ornament, closes her eyes and tilts her head back, resting it on the grass. “Aye, and the weather is never too harsh, though once the snows fall, even {color=#f6d6bd}Foggy{/color} has to move back in. We spend winters in our house of gatherings, burning wood and killing time.” A few more good moments go by like this. “It’s a good land, even if a small one,” concludes {color=#f6d6bd}Shoshi{/color}."
                jump creekscreek0202c
            '“How are your days? Any news?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How are your days? Any news?”')
                $ custom1 = "“Life isn’t bad,” says a short woman with wavy hair, which she keeps dry like an ornament. “Even if it’s slow.” You pay attention to their brief stories, but none of them are especially absorbing. The skinny man with long limbs tried to catch a muflon, but it ran away. The dark-skinned woman just made a little wooden cart for her nephew. There are hopes to restore one of the roofs, or maybe replace it with thatch. The lazy minutes go by."
                jump creekscreek0202c
            '“What do you do around here when you have a free day?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you do around here when you have a free day?”')
                $ custom1 = "“Well, you’re looking at it right now,” says a skinny man with long limbs. “We hang around the water, or play games in the square. Bards don’t come here, and if we had a juggler or an acrobat, we would get tired of them in a year.”\n\nA dark-skinned woman disappears beneath the surface for a few moments, as if trying to sink the boredom before it finds her. “Not that there are many days without work,” adds a short woman with wavy hair, which she keeps dry like an ornament. “We drudge from spring to fall, and in the middle of winter die of boredom.”"
                jump creekscreek0202c

    label creekscreek0202c:
        $ quarters += 1
        if not cleanliness:
            $ quarters += 1
            $ cleanliness = limit_cleanliness(cleanliness+2)
            show plus2appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 appearance points.{/i}')
        elif cleanliness == 1:
            $ quarters += 1
            $ cleanliness = limit_cleanliness(cleanliness+1)
            show plus1appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 appearance point.{/i}')
        menu:
            '[custom1]
            \n\nAfter a quiet moment, a short blonde male speaks to you gently. “We weren’t sure you’d be willing to spend time with such {i}ribald{/i} folk...” He’s instantly interrupted by the others, who start to argue which one of them is more indecent. He then carries on. “Aren’t the cityfolk taught to be {i}of humble gaze and silent breath{/i}, like that missionary told us?”
            '
            '“Oh, the cityfolk are prudes. People go to small bathhouses and pay for their privacy. It’s impolite to glance at a naked stranger.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Oh, the cityfolk are prudes. People go to small bathhouses and pay for their privacy. It’s impolite to glance at a naked stranger.”')
                $ hovlavan_nakedness = "prudeness"
                if shoshi_namebig == "The dark-haired woodcutter":
                    $ custom1 = "“You’ve found a place to loosen up the {i}chains{/i},” the dark-haired woman, who you now recognize as a woodcutter, comments melodiously. During the next few minutes, the young people have no issue hugging or grabbing one another in ways that would be scandalous in the city, but here are so casual that they feel more playful than sexual, even though there are no clothes at hand."
                else:
                    $ custom1 = "“You’ve found a place to loosen up the {i}chains{/i},” {color=#f6d6bd}Shoshi{/color} comments melodiously. During the next few minutes, the young people have no issue hugging or grabbing one another in ways that would be scandalous in the city, but here are so casual that they feel more playful than sexual, even though there are no clothes at hand."
                jump creekscreek0202d
            '“After the invasion, people had to share their space, and are now used to bathing in large numbers in the river, or at the common bathhouse. There isn’t much touching, though.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “After the invasion, people had to share their space, and are now used to bathing in large numbers in the river, or at the common bathhouse. There isn’t much touching, though.”')
                $ hovlavan_nakedness = "justbaths"
                if shoshi_namebig == "The dark-haired woodcutter":
                    $ custom1 = "“Poor thing,” says the dark-haired woman, who you now recognize as a woodcutter. “Touching is the {i}best{/i} part!” During the next few minutes, the young people have no issue hugging or grabbing one another in ways that would be scandalous in the city, but here are so casual that they feel more playful than sexual, even though there are no clothes at hand."
                else:
                    $ custom1 = "“Poor thing,” says {color=#f6d6bd}Shoshi{/color}. “Touching is the {i}best{/i} part!” During the next few minutes, the young people have no issue hugging or grabbing one another in ways that would be scandalous in the city, but here are so casual that they feel more playful than sexual, even though there are no clothes at hand."
                jump creekscreek0202d
            'I smile. “You’d be surprised how many naked shells one may see in the city. And touch.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “You’d be surprised how many naked shells one may see in the city. And touch.”')
                $ hovlavan_nakedness = "ribald"
                $ custom1 = "One of the male lovers bursts into laughter. “I {i}knew{/i} the priest was lying about the bathhouses!” A wavy-haired woman also chuckles. “So we may not be that strange in the city after all. Hwere there’s will to live,” her voice gets solemn, “there’s shagging.” To demonstrate her words, she kisses one of her friends, luring the eyes of the rest of the group."
                jump creekscreek0202d
            '“It’s tied to one’s status, like everything in the city. The rich folk bathe in luxurious rooms and invite or pay for many lovers, while most people have rather humble experiences.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s tied to one’s status, like everything in the city. The rich folk bathe in luxurious rooms and invite or pay for many lovers, while most people have rather humble experiences.”')
                $ hovlavan_nakedness = "status"
                $ foragers_tzvi_darksecret_unknown = 1
                $ custom1 = "The group exchanges telling looks. “That’s the saddest thing I’ve ever heard,” says the woman with wavy hair, but one of the male lovers tells her to think about it. “We may not judge each other for our trade or dragon bones, but there’s reputation and memories. Wouldn’t you say {color=#f6d6bd}Tzvi{/color} has a poor {i}status{/i}?” Her eyes suddenly turn cold, and a surprisingly serious conversation sparks right away, in the center of which lies the difference between being “unwanted” because of one’s deeds, or because of one’s background."
                jump creekscreek0202d

    label creekscreek0202d:
        $ quarters += 1
        if cleanliness == 2:
            $ quarters += 1
            $ cleanliness = limit_cleanliness(cleanliness+1)
            show plus1appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 appearance point.{/i}')
        if dalit_dice_never:
            $ custom2 = "You feel tightness in your throat as you think about {color=#f6d6bd}Pelt of the North{/color}, where you mentioned you don’t really gamble."
        else:
            $ custom2 = ""
        menu:
            '[custom1]
            \n\nOnce the discussion slows down again, the group looks at each other, and the skinny man with long limbs is the first one to speak. “A round of dice?” He gets out without waiting for an answer, and others follow suit. “But hwat do we wager,” asks a brown-skinned woman with short hair. “Apples?” You follow them to the grass and it seems like the others aren’t even thinking of gathering their clothes.
            \n\nSeeing how quickly the dice find their way from a bag to the wide, short tree stump, you realize it’s not as much a spontaneous invitation, as it is a part of an old ritual. [custom2]
            '
            '“I do have some fruits and veggies. Let’s play!”' if item_wildplants:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I do have some fruits and veggies. Let’s play!”')
                $ creeks_youth_gambling_wager = "wilplants"
                $ custom1 = "“Yes!” The skinny man adds your share to the prize pool. “But the greens count as half.” In his bag, you indeed see mostly pears, plums, and other fruits."
                jump creekscreek0202e
            '“I’ll add some dried meat to the pile.”' if item_rations:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll add some dried meat to the pile.”')
                $ creeks_youth_gambling_wager = "rations"
                $ custom1 = "“Well well, hwat a fancy share! Too bad it’s the {i}wrong{/i} currency, and you won’t get a fair exchange!” The skinny man adds your entire package to the prize pool, even though one of his friends asks him to calm down."
                jump creekscreek0202e
            'I take a confident posture. “Apples are fine, but if you can win, I’ll give you a dragon bone.”' if coins:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a confident posture. “Apples are fine, but if you can win, I’ll give you a dragon bone.”')
                $ creeks_youth_gambling_wager = "coin"
                $ custom1 = "The skinny man playfully reaches to you with an open palm, solemnly waiting for your coin. He then adds it to the bag of apples, pears, and plums. “Very well! Now the true game begins!”"
                jump creekscreek0202e
            '“No need for a wager. Let’s play for fun.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “No need for a wager. Let’s play for fun.”')
                $ creeks_youth_gambling_wager = "none"
                $ custom1 = "The skinny man lets out a short wail. “But apples are nothing big, it {i}is{/i} just for fun!” Even though his tone is exaggerated, the serious look he gets from the brown-skinned woman makes it clear he wasn’t entirely joking."
                jump creekscreek0202e

    label creekscreek0202e:
        if not dalit_dice:
            $ custom2 = "The rules are new to you, but in no way baffling. Four people can play at once. The dice are bone-made cubes with six dotted faces. Every time someone wins a round, they get a point, and the person with the most points at the end of the game wins all the coins. As you play, you don’t feel like you have much control over the results."
        else:
            $ custom2 = "The rules are similar to the those of the game you played in {color=#f6d6bd}Pelt of the North{/color}, but this time six people can play at once, and the bone dice are cubes, with six dotted faces instead of four. Every time someone wins a round, they get a point, and the person with the most points at the end of the game wins all the coins."
        menu:
            '[custom1]
            \n\nYou look at the light dancing on everyone’s skin, but also their hair, now shaken by the wind. The way the grass touches your own backside is a bit distracting. The group is mostly glancing at each other or gossiping, without paying much attention to the game. [shoshi_namebig] once again holds her axe, and looks at all of you while humming a peaceful tune.
            \n\n[custom2]
            '
            'I stay focused, doing my best to win.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stay focused, doing my best to win.')
                $ quarters += 1
                $ creeks_youth_gambling = 2
                $ pc_gamblingxp += 5
                $ creeks_reputation -= 1
                if quarters < (world_daylength-44):
                    $ custom2 = "day"
                elif quarters < (world_daylength-52):
                    $ custom2 = "afternoon"
                elif quarters < (world_daylength-12):
                    $ custom2 = "evening"
                else:
                    $ custom2 = "night"
                if creeks_youth_gambling_wager == "wilplants":
                    $ item_wildplants += 2
                    $ renpy.notify("You won 2 bunches of wild plants.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You won 2 bunches of wild plants.{/i}')
                    $ custom1 = "All that’s left for you is to grab the bag and stand up."
                else:
                    $ custom1 = "All that’s left for you is to stand up."
                menu:
                    'The skinny coordinator realizes that you aren’t holding back and also starts to ignore his surroundings, trying to take you down. The two of you sometimes comment on your plays, while the other players at first fall silent, feeling the tension in the air, and then surrender their spots, one by one, allowing the two of you to play over the reward.
                    \n\nAfter the last person walks away, chatting with the others as they collect their clothes, the skinny man also gives you an awkward look. “Know hwat, let’s just say you won,” he growls and grabs the dice. [custom1] “Have a good [custom2], roadwarden,” says the woman with an axe on her shoulder, now covered with a leather shirt.
                    '
                    '“Well, thanks for playing.” I get dressed and leave the bridge.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Well, thanks for playing.” I get dressed and leave the bridge.')
                        jump creeksafterinteraction01
            'I try to learn as much about the game as I can.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to learn as much about the game as I can.')
                $ quarters += 1
                $ creeks_youth_gambling = 2
                $ pc_gamblingxp += 10
                if creeks_youth_gambling_wager == "wilplants":
                    $ item_wildplants -= 1
                    $ renpy.notify("You lost a bunch of wild plants.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a bunch of wild plants.{/i}')
                if creeks_youth_gambling_wager == "rations":
                    $ item_rations -= 1
                    $ renpy.notify("You lost a food ration.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a food ration.{/i}')
                if creeks_youth_gambling_wager == "coin":
                    $ coins -= 1
                    show screen notifyimage( "-1", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 {image=cointest}{/i}')
                menu:
                    'The skinny coordinator is more than eager to discuss your moves, though you feel like he may be giving you less-than-optimal advice, especially once he finishes with the highest score. Still, the things he tells you, even those you can’t completely agree with, are insightful, and you feel like they may be of use even in slightly different games.
                    \n\nThe conversation between you and the man is intense, while the others participate only so far as it takes for them to cast the dice. Once it’s over, the youths decide to get back to their tasks, and the skinny man throws you your clothes. “Thanks for helping us get clean,” says the woman with an axe on her naked shoulder, and the group chuckles amiably.
                    '
                    'I wish them a good day and get dressed.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wish them a good day and get dressed.')
                        jump creeksafterinteraction01
            'I try to get to know them better, flirt a bit.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to get to know them better, flirt a bit.')
                $ quarters += 2
                $ creeks_youth_gambling = 3
                $ pc_gamblingxp += 2
                $ creeks_reputation += 1
                if creeks_youth_gambling_wager == "wilplants":
                    $ item_wildplants -= 1
                    $ renpy.notify("You lost a bunch of wild plants.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a bunch of wild plants.{/i}')
                if creeks_youth_gambling_wager == "rations":
                    $ item_rations -= 1
                    $ renpy.notify("You lost a food ration.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a food ration.{/i}')
                if creeks_youth_gambling_wager == "coin":
                    $ coins -= 1
                    show screen notifyimage( "-1", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 {image=cointest}{/i}')
                menu:
                    'Aside from the skinny coordinator of the game, who finally wins it, no one else tries to keep track of points or discuss the strategy. Hands throw dice, push the cups, and return to either resting on the grass, or holding a nearby person, including you.
                    \n\nYou hear their names, but you’d need some time to memorize all of them at once. The skinny man tries to learn more about the trees, hoping to be a forest gardener; [shoshi_namesmall] claims to be the fastest axe thrower in the village, and announces this with a quiet song; the short one with wavy hair used to study herbs in {color=#f6d6bd}Howler’s Dell{/color}, but came here to move away from the druids’ strict looks; the male couple both help {color=#f6d6bd}Old Hava{/color} on the farm, and hope to learn enough to supervise the fields on their own; the dark-skinned woman with short hair plans to fix the houses and the palisade; and the last person, a blonde man of a tiny stature who had said almost nothing during the last hour, is proud to announce himself as the only cave explorer in {color=#f6d6bd}Creeks{/color}, though once asked about any interesting findings, he instantly refuses to share. You catch a soul-crushing terror in his eyes.
                    \n\nFinally, the youths decide to get back to their tasks, and the skinny man throws you your clothes. “It was nice,” says the woman with an axe on her naked shoulder, as she invites you to approach with her spread arm.
                    '
                    'I hug them all and prepare myself to leave.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I hug them all and prepare myself to leave.')
                        menu:
                            'While your nose catches only the freshness of the creek and a few hints of trampled grass, there’s a comforting warmth in the skin and lips that touch you, a shelter from the winds.
                            \n\nYou get dressed and cross the bridge.
                            '
                            'I look for {color=#f6d6bd}Elah{/color}, the carpenter.' if elah_lastseen < day and elah_locked != day:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for {color=#f6d6bd}Elah{/color}, the carpenter.')
                                jump creekselah01
                            'I return to {color=#f6d6bd}Elah{/color}, the carpenter.' if elah_lastseen >= day and elah_locked != day:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Elah{/color}, the carpenter.')
                                jump creekselah01
                            'Elah won’t speak with me today. (disabled)' if elah_locked == day:
                                pass
                            'I look for {color=#f6d6bd}Efren{/color}, the hunter.' if efren_lastseen < day:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for {color=#f6d6bd}Efren{/color}, the hunter.')
                                jump creeksefren01
                            'I return to {color=#f6d6bd}Efren{/color}, the hunter.' if efren_lastseen >= day:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Efren{/color}, the hunter.')
                                jump creeksefren01
                            'I go to {color=#f6d6bd}Old Hava{/color}, the farmer.' if oldhava_known:
                                jump creeksoldhava01
                            'I approach the shallow creek.' if not creeks_youth_gambling_invited or (creeks_youth_gambling_invited and creeks_youth_gambling):
                                jump creekscreek0201
                            'I accept the invitation and head to the creek.' if creeks_youth_gambling_invited and not creeks_youth_gambling:
                                jump creekscreek0201
                            'Maybe there are some locals looking for a match in other villages.' ( condition="not shoshi_single and quest_matchmaking == 1" ):
                                jump creekssinglepeople01firsttime
                            'I return to {color=#f6d6bd}Shoshi{/color}.' ( condition="(shoshi_single and quest_matchmaking == 1 and not shoshi_notmatched and galerocks_singlepeople_firsttime and not shoshi_marina) or (shoshi_single and quest_matchmaking == 1 and not shoshi_notmatched and shoshi_marina and galerocks_singlepeople_marina_religion1 and not shoshi_religion) or (quest_recruitahunter_noonerecruited and shoshi_notmatched and not quest_recruitahunter_spokento_shoshi)" ):
                                jump creekssinglepeople01
                            'I still need to find a match for Shoshi. (disabled)' ( condition="shoshi_single and quest_matchmaking == 1 and not galerocks_singlepeople_firsttime" ):
                                pass
                            'Shoshi is waiting for a message from Marina. (disabled)' ( condition="shoshi_single and quest_matchmaking == 1 and shoshi_marina and not galerocks_singlepeople_marina_religion1" ):
                                pass
                            '{image=cointest} I have a day to spare. I ask around to see if any locals need protection on the roads.' ( condition="creeks_mundanework and quarters <= 40 and (creeks_mundanework_counter < day)" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Elah{/color}, the carpenter.')
                                jump creeksmundanework01
                            '{image=coingray} The locals won’t need my services before day [creeks_mundanework_counter]. (disabled)' ( condition="creeks_mundanework and (creeks_mundanework_counter >= day)" ):
                                pass
                            '{image=coingray} At such a late hour the locals won’t be interested in my services. (disabled)' ( condition="creeks_mundanework and quarters > 40" ):
                                pass
                    'It’s getting a bit {i}too{/i} intimate. I smile at them and grab my clothes.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s getting a bit {i}too{/i} intimate. I smile at them and grab my clothes.')
                        menu:
                            'There’s no judgment in the amicable words of farewell. You nod and cross the bridge.
                            '
                            'I look for {color=#f6d6bd}Elah{/color}, the carpenter.' if elah_lastseen < day and elah_locked != day:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for {color=#f6d6bd}Elah{/color}, the carpenter.')
                                jump creekselah01
                            'I return to {color=#f6d6bd}Elah{/color}, the carpenter.' if elah_lastseen >= day and elah_locked != day:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Elah{/color}, the carpenter.')
                                jump creekselah01
                            'Elah won’t speak with me today. (disabled)' if elah_locked == day:
                                pass
                            'I look for {color=#f6d6bd}Efren{/color}, the hunter.' if efren_lastseen < day:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for {color=#f6d6bd}Efren{/color}, the hunter.')
                                jump creeksefren01
                            'I return to {color=#f6d6bd}Efren{/color}, the hunter.' if efren_lastseen >= day:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Efren{/color}, the hunter.')
                                jump creeksefren01
                            'I go to {color=#f6d6bd}Old Hava{/color}, the farmer.' if oldhava_known:
                                jump creeksoldhava01
                            'I approach the shallow creek.' if not creeks_youth_gambling_invited or (creeks_youth_gambling_invited and creeks_youth_gambling):
                                jump creekscreek0201
                            'I accept the invitation and head to the creek.' if creeks_youth_gambling_invited and not creeks_youth_gambling:
                                jump creekscreek0201
                            'Maybe there are some locals looking for a match in other villages.' ( condition="not shoshi_single and quest_matchmaking == 1" ):
                                jump creekssinglepeople01firsttime
                            'I return to {color=#f6d6bd}Shoshi{/color}.' ( condition="(shoshi_single and quest_matchmaking == 1 and not shoshi_notmatched and galerocks_singlepeople_firsttime and not shoshi_marina) or (shoshi_single and quest_matchmaking == 1 and not shoshi_notmatched and shoshi_marina and galerocks_singlepeople_marina_religion1 and not shoshi_religion) or (quest_recruitahunter_noonerecruited and shoshi_notmatched and not quest_recruitahunter_spokento_shoshi)" ):
                                jump creekssinglepeople01
                            'I still need to find a match for Shoshi. (disabled)' ( condition="shoshi_single and quest_matchmaking == 1 and not galerocks_singlepeople_firsttime" ):
                                pass
                            'Shoshi is waiting for a message from Marina. (disabled)' ( condition="shoshi_single and quest_matchmaking == 1 and shoshi_marina and not galerocks_singlepeople_marina_religion1" ):
                                pass
                            '{image=cointest} I have a day to spare. I ask around to see if any locals need protection on the roads.' ( condition="creeks_mundanework and quarters <= 40 and (creeks_mundanework_counter < day)" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Elah{/color}, the carpenter.')
                                jump creeksmundanework01
                            '{image=coingray} The locals won’t need my services before day [creeks_mundanework_counter]. (disabled)' ( condition="creeks_mundanework and (creeks_mundanework_counter >= day)" ):
                                pass
                            '{image=coingray} At such a late hour the locals won’t be interested in my services. (disabled)' ( condition="creeks_mundanework and quarters > 40" ):
                                pass

label creekssinglepeople01firsttime:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe there are some locals looking for a match in other villages.')
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ shoshi_single = 1
    $ renpy.notify("Journal updated: Matchmaking")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Matchmaking{/i}')
    $ shoshi_namebig = "{color=#f6d6bd}Shoshi{/color}"
    $ shoshi_namesmall = "{color=#f6d6bd}Shoshi{/color}"
    $ minutes += 10
    menu:
        'After a few minutes you find yourself sitting at a table with {color=#f6d6bd}Shoshi{/color}, a dark-haired twenty-year-old who some call a woodcutter, others - a singer. In both of these roles, her massive stature must be of help. When she walks, she either carries a large axe on her shoulders, or swings it around, towering over her tribesfolk like a chieftain from the tales of war.
        \n\nShe admits she enjoys “a friendly shag” from time to time, but can’t see a future for her in {color=#f6d6bd}Creeks{/color}. “Enough of these {i}friends{/i} lose their lives in the wilderness, I start seeing cats and gargoyles in every shadow. I’d rather have a few calm, {i}safe{/i} years at the side of a pretty li’l woman whom I’ll see in my bed in the evenings. Though you know, friend. Not just her,” she lets out sonorous laughter. You mention that you don’t know if she’ll be able to keep her trade after moving away, and she strokes her axe with affection. “Aye, I’d miss the woods, but who knows. My tribe can’t be the only one that cuts trees around here, aye?”
        \n\nYou try to ask her about her worldview, but she gets bored by the topic. “We here,” she looks around, “have no temples and priests. And I don’t aim to become one.”
        '
        '“I wonder... {color=#f6d6bd}Dalit{/color} from {color=#f6d6bd}Pelt of the North{/color} is looking for hunters. Are you up to the task?”' if quest_recruitahunter_noonerecruited and shoshi_notmatched and not quest_recruitahunter_spokento_shoshi:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I wonder... {color=#f6d6bd}Dalit{/color} from {color=#f6d6bd}Pelt of the North{/color} is looking for hunters. Are you up to the task?”')
            jump shoshi_recruitahunter01
        'I tell her about {color=#f6d6bd}Marina{/color} from {color=#f6d6bd}Gale Rocks{/color}.' if galerocks_singlepeople_firsttime and not shoshi_marina:
            jump shoshi_marina01
        'I try to recall {color=#f6d6bd}Marina’s{/color} message.' if shoshi_marina and galerocks_singlepeople_marina_religion1 and not shoshi_religion:
            jump shoshi_religion01
        '“Farewell.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell.”')
            jump creeksafterinteraction01

    label creekssinglepeople01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Shoshi{/color}.')
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            'She’s preparing for work, but is ready to give you a few moments.
            '
            '“I wonder... {color=#f6d6bd}Dalit{/color} from {color=#f6d6bd}Pelt of the North{/color} is looking for hunters. Are you up to the task?”' if quest_recruitahunter_noonerecruited and shoshi_notmatched and not quest_recruitahunter_spokento_shoshi:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I wonder... {color=#f6d6bd}Dalit{/color} from {color=#f6d6bd}Pelt of the North{/color} is looking for hunters. Are you up to the task?”')
                jump shoshi_recruitahunter01
            'I tell her about {color=#f6d6bd}Marina{/color} from {color=#f6d6bd}Gale Rocks{/color}.' if galerocks_singlepeople_firsttime and not shoshi_marina:
                jump shoshi_marina01
            'I try to recall {color=#f6d6bd}Marina’s{/color} message.' if shoshi_marina and galerocks_singlepeople_marina_religion1 and not shoshi_religion:
                jump shoshi_religion01
            '“Farewell.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell.”')
                jump creeksafterinteraction01

    label shoshi_marina01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell her about {color=#f6d6bd}Marina{/color} from {color=#f6d6bd}Gale Rocks{/color}.')
        $ shoshi_marina = 1
        menu:
            '“Well, well, you found quite the someone, friend, and I’ve heard a lot of good things ‘bout her home. But this Wright talk makes me worried, are you sure she’d be ready to keep our {i}bonds{/i} loose?” Seeing your shrug, she sighs. “Tell her about me, don’t hide my plans. Just speak of me kindly,” she laughs. “If she wants to have fun with me, I’ll make her life warmer. And I love kids.” For the first time, her smile becomes humble and kind, instead of playful.
            '
            '“I wonder... {color=#f6d6bd}Dalit{/color} from {color=#f6d6bd}Pelt of the North{/color} is looking for hunters. Are you up to the task?”' if quest_recruitahunter_noonerecruited and shoshi_notmatched and not quest_recruitahunter_spokento_shoshi:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I wonder... {color=#f6d6bd}Dalit{/color} from {color=#f6d6bd}Pelt of the North{/color} is looking for hunters. Are you up to the task?”')
                jump shoshi_recruitahunter01
            'I tell her about {color=#f6d6bd}Marina{/color} from {color=#f6d6bd}Gale Rocks{/color}.' if galerocks_singlepeople_firsttime and not shoshi_marina:
                jump shoshi_marina01
            'I try to recall {color=#f6d6bd}Marina’s{/color} message.' if shoshi_marina and galerocks_singlepeople_marina_religion1 and not shoshi_religion:
                jump shoshi_religion01
            '“Farewell.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell.”')
                jump creeksafterinteraction01

    label shoshi_religion01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to recall {color=#f6d6bd}Marina’s{/color} message.')
        $ shoshi_religion = 1
        $ shoshi_notmatched = 1
        $ creeks_reputation += 1
        $ quest_matchmaking_points += 1
        if quest_matchmaking_points >= quest_matchmaking_points_max:
            $ quest_matchmaking = 2
            $ pc_goal_iwanttohelppoints += 1
            $ renpy.notify("Quest completed: Matchmaking")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Matchmaking{/i}')
        else:
            $ renpy.notify("Journal updated: Matchmaking")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Matchmaking{/i}')
        menu:
            '“Then I guess it’s not meant to be,” she shakes her head with disappointment. “I’m glad you opened this chance for me, friend, but there are parts of me I’m not willing to change. Still, I’ll make sure the tribe hears about your help,” she suddenly raises her axe and shouts. “Hey, you!” She addresses no one in particular, but her powerful voice makes everyone stop. “[pcname] did me a big favor, aye? Be nice!” A few people smile or scoff, and life goes on.
            \n\n“And if you want to bring {color=#f6d6bd}Marina{/color} my answer,” she rests her chin on the top of her blade. “Tell her {i}think it over, for I can make every day of yours sweet and light, if you’re ready to breathe fully.{/i}”
            '
            '“I wonder... {color=#f6d6bd}Dalit{/color} from {color=#f6d6bd}Pelt of the North{/color} is looking for hunters. Are you up to the task?”' if quest_recruitahunter_noonerecruited and shoshi_notmatched and not quest_recruitahunter_spokento_shoshi:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I wonder... {color=#f6d6bd}Dalit{/color} from {color=#f6d6bd}Pelt of the North{/color} is looking for hunters. Are you up to the task?”')
                jump shoshi_recruitahunter01
            'I tell her about {color=#f6d6bd}Marina{/color} from {color=#f6d6bd}Gale Rocks{/color}.' if galerocks_singlepeople_firsttime and not shoshi_marina:
                jump shoshi_marina01
            'I try to recall {color=#f6d6bd}Marina’s{/color} message.' if shoshi_marina and galerocks_singlepeople_marina_religion1 and not shoshi_religion:
                jump shoshi_religion01
            '“Farewell.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell.”')
                jump creeksafterinteraction01

    label shoshi_recruitahunter01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I wonder... {color=#f6d6bd}Dalit{/color} from {color=#f6d6bd}Pelt of the North{/color} is looking for hunters. Are you up to the task?”')
        $ quest_recruitahunter_spokento_shoshi = 1
        menu:
            'She rests her axe on her shoulder and makes a wide grin. “Now that I’ve nothing better waiting for me here, friend? If she’s looking for a folk who can take a swing, take a hit, and take a few steps into the woods without getting mauled to death, she’ll find no better soul in this boring-ass land.”
            '
            '“Great. I’ll mention this to her once I see her.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Great. I’ll mention this to her once I see her.”')
                jump creeksafterinteraction01
