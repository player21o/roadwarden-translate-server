################################################################################
## Initialization
################################################################################

init offset = -1


default persistent.journal_notes = []
default journal_notes_currently_entering = None
default journal_notes_currently_entering_value = ""
default tutorial_notes = 0

init python:
    def confirm_editing():
        global journal_notes_currently_entering_value
        global journal_notes_currently_entering

        # if (journal_notes_currently_entering_value == ""):
        #     persistent.journal_notes.pop(journal_notes_currently_entering)
        # else:
        persistent.journal_notes[journal_notes_currently_entering] = journal_notes_currently_entering_value


        journal_notes_currently_entering = None

    def cancel_editing():
        global journal_notes_currently_entering_value
        global journal_notes_currently_entering

        if (journal_notes_currently_entering and persistent.journal_notes[journal_notes_currently_entering] == ""):
            persistent.journal_notes.pop(journal_notes_currently_entering)

        journal_notes_currently_entering = None

    def start_editing_journal_note(i):
        global journal_notes_currently_entering_value
        global journal_notes_currently_entering

        cancel_editing()

        journal_notes_currently_entering_value = persistent.journal_notes[i]
        journal_notes_currently_entering = i
        # persistent.journal_notes_copy = persistent.journal_notes.copy()
        # persistent.journal_notes = persistent.journal_notes_copy        
        # renpy.notify("asjhdkasjhdksaj")
        # renpy.restart_interaction()

    def delete_journal_note(i):
        global journal_notes_currently_entering

        persistent.journal_notes.pop(i)

        if (journal_notes_currently_entering > 0):
            journal_notes_currently_entering = journal_notes_currently_entering - 1


    def add_new_journal_note():
        persistent.journal_notes.append("")
        start_editing_journal_note(len(persistent.journal_notes) - 1)


###################### Quests (quest 0 = not discovered, 1 = discovered but not completed, 2 = completed)
default journal_quest = 0
default journal_people = 0
default journal_group = 0
default journal_beast = 0
default journal_glossary = 0

default quest_explorepeninsula_points = 0
default quest_explorepeninsula_points_threshold_1 = 14 # the city hesitates
default quest_explorepeninsula_points_threshold_2 = 25 # the city is careful
default quest_explorepeninsula_points_threshold_3 = 32 # the city goes all-in
default quest_explorepeninsula_result = 0
default quest_explorepeninsula_mainvillage = 0
default quest_explorepeninsula = 0 #Explore the Peninsula
default quest_explorepeninsula_description00 = 0 #""
default quest_explorepeninsula_description01 = 0 #"I need to explore the peninsula as thoroughly as I can. I have to get to know the locals and find out how much of a profit can be made here, then bring the news to {color=#f6d6bd}Hovlavan{/color}."
default quest_explorepeninsula_description01a = 0 # "To add worth to my work here, I could secure the roads by getting rid of any major threats, and convince the tribes to negotiate with the officials."
default quest_explorepeninsula_description02a = 0 #"Soldiers told me about a large village that repeatedly uses necromancy, even though it’s forbidden by law and can be extremely dangerous. I should take a look and judge for myself. The village is somewhere among the bogs, by the northwestern road."
default quest_explorepeninsula_description02b = 0 #"I heard that the undead from the village of {color=#f6d6bd}White Marshes{/color} are related to the local priest. Since they’ve appeared, some of the villagers have decided to leave their homes." / "I heard that these practices are related to the local priest, and since they’ve started, some of the villagers have decided to leave their homes."
default quest_explorepeninsula_description02prec = 0 #"The few travellers I met at the edge of the bog got upset when I mentioned the undead."
default quest_explorepeninsula_description02c = 0 #"I’ve been to {color=#f6d6bd}White Marshes{/color} and confirmed the rumors about their wide-spread necromantic practices."
default quest_explorepeninsula_description02d = 0 #"I heard that these practices are related to the local priest, and since they’ve started, some of the villagers have decided to leave their homes."
default quest_explorepeninsula_description03 = 0 #"I heard that some of the locals know ways to move safely through the rocky coasts, so it may be possible to maintain access to the sea after all."
default quest_explorepeninsula_description03b = 0#"According to {color=#f6d6bd}Thais’{/color} letter, the people of {color=#f6d6bd}Gale Rocks{/color} use their knowledge of the shore to trade with pirates."
default quest_explorepeninsula_description04 = 0 #"I heard that many creatures have recently left the northern forests, which results in much more tension among the predators. Some claim that the wilderness has become unusually dangerous."
default quest_explorepeninsula_description05 = 0 #"I found an abandoned watchtower set near the eastern road. It needs some renovations, but could easily be turned into a military post."
default quest_explorepeninsula_description06 = 0 #"I took a good look at the ruins placed at the northern road. It would be easy to turn it into a small daytime shelter."
default quest_explorepeninsula_description07 = 0 #
default quest_explorepeninsula_description08 = 0 #"The eastern path may be dangerous, but the people of {color=#f6d6bd}Creeks{/color} plan to take better care of it."
default quest_explorepeninsula_description09 = 0 #"The abandoned village in the South may be a useful spot for future settlers. I should figure out why it was ruined."
default quest_explorepeninsula_description10 = 0 #"The villagers from {color=#f6d6bd}Howler’s Dell{/color} are willing to sell linen and sturdy clothing in exchange for a squad of soldiers, as well as some iron. They are already well-off and as long as they won’t be forced to follow The United Church, they’re open to trading negotiations."
default quest_explorepeninsula_description10b = 0 #"The druids from {color=#f6d6bd}Howler’s Dell{/color} are far from enthusiastic about contacting the guild. Their alienation can introduce some difficulties down the road."
default quest_explorepeninsula_description10c = 0 # "The old mine set in {color=#f6d6bd}Hag Hills{/color} is flooded. There’s no point in trying to restore it."
default quest_explorepeninsula_description11 = 0 #
default quest_explorepeninsula_description12 = 0 #"The stone workers who live in {color=#f6d6bd}Old Págos{/color} suffer from a lethal plague. If the situation doesn’t improve, the village may have no value to the merchants."
default quest_explorepeninsula_description12a = 0 #"I’ve managed to take care of the plague that had fallen upon {color=#f6d6bd}Old Págos{/color}. The peninsula should be safer now."
default quest_explorepeninsula_description13 = 0 #"{color=#f6d6bd}The monastery{/color} hides a tremendous cave with walls covered by copies of Wright’s Tablets. It may be of huge importance to the religious leaders in {color=#f6d6bd}Hovlavan{/color}."
default quest_explorepeninsula_description13b = 0 #"I’ve read a part of the texts myself, so I’m sure the monks weren’t lying to me."
default quest_explorepeninsula_description14 = 0 #
default quest_explorepeninsula_description15 = 0 #"I met {color=#f6d6bd}Eudocia{/color}, a skilled enchantress who lives near the western road. The guild could benefit from her powerful golems."
default quest_explorepeninsula_description15a = 0 #"{color=#f6d6bd}Eudocia{/color} has agreed to talk with the merchants. I need to take her Golem Glove to the city."
default quest_explorepeninsula_description15b = 0 #"I sacrificed The Golem Glove. The officials will have to trust my word."
default quest_explorepeninsula_description15c = 0 #"{color=#f6d6bd}Eudocia{/color} refused to start talks with the merchants."
default quest_explorepeninsula_description16 = 0 #"I found a spot at the eastern road that may be a part of a larger copper vein. It should be investigated by an experienced team, and {color=#f6d6bd}Hovlavan{/color} will surely appreciate it if they can be the first ones to get to it."
default quest_explorepeninsula_description17 = 0 #The western bogs are a good spot for peat harvesting - as long as the locals are friendly to the outsiders, they may be willing to trade for it.
default quest_explorepeninsula_description17a = 0 #In spring, {color=#f6d6bd}White Marshes{/color} will most likely completely separate itself from the rest of the peninsula. The city merchants will have fewer reasons to invest in a new route.
default quest_explorepeninsula_description17b = 0 #The people of {color=#f6d6bd}White Marshes{/color} feel threatened and may attempt to completely seperate themselves from the rest of the peninsula. If that happens, the city merchants will have fewer reasons to invest in a new route.
default quest_explorepeninsula_description18 = 0 #"I’ve gained a deeper understanding of the trade related to {color=#f6d6bd}Gale Rocks{/color}. With a decent deal, they could provide the city with many barrels of salt and salted fish, and for little more than some coins, seeds, and timber."
default quest_explorepeninsula_description19 = 0 #
default quest_explorepeninsula_description20 = 0 #"From what I’ve learned in The Tribe of The Green Mountain, they will never be open to negotiate with the city."

default quest_asterion = 0 #Find the Roadwarden
default quest_asterion_description00asterion_highisland_knowsabout = 0 #"I discovered that {color=#f6d6bd}Asterion{/color} has died during his lonely journey to an isolated island."
default quest_asterion_description00badresult = 0 #"I wasn’t able to find {color=#f6d6bd}Asterion{/color} on time."
default quest_asterion_description00lies = 0 #"I wasn’t able to find {color=#f6d6bd}Asterion{/color} on time, but I lied to {color=#f6d6bd}Tulia{/color} to get my reward."
default quest_asterion_description00goodresult = 0 #"I collected my reward from {color=#f6d6bd}Tulia{/color}."
default quest_asterion_description00gaveup = 0 #"I’ve decided to give up on my search."
default quest_asterion_description01 = 0 #"Before I became the roadwarden of this peninsula, a man known as {color=#f6d6bd}Asterion{/color} used to patrol these roads. If I manage to find out what happened to him and bring the news to {color=#f6d6bd}Tulia{/color} from the southern camp, I’ll receive his abandoned belongings." # {b}I have to return to her before the end of summer.{/b}
default quest_asterion_description01b = 0 #"I heard that he might have disappeared in the wilderness."
default quest_asterion_description01c = 0 #"I could look for him near the heart of the woods, in the center of the peninsula."
default quest_asterion_description01d = 0 #"It looks like there are some isolated territories in the far east, though it’s hard to reach them."
default quest_asterion_description01e = 0 #"In the northwest, near the coast, there's an {i}uninhabited{/i} island. One needs a boat to reach this place, though."
##########if item_asteriontablet_read : "I found a wax tablet that could have belonged to Asterion. It’s filled with small pictures and chaotic notes focused on the construction of boats and oars. One word seems to be a name: {i}Navica{/i}."
default quest_asterion_description02 = 0 #"I’ve heard in {color=#f6d6bd}Pelt{/color} that right before Asterion’s disappearance, the innkeeper gave him 50 dragons for some sort of investment. Asterion was seen in White Marshes, a village set northwest from the inn."
default quest_asterion_description03 = 0 #"According to {color=#f6d6bd}the druid from the cave{/color} in the southwest, Asterion was last seen in one of the villages in the North."
default quest_asterion_description04 = 0 #"According to {color=#f6d6bd}the scavenger{/color} I met in a ruined village in the South, people in the northern villages were asking him about {color=#f6d6bd}Asterion{/color}, but after a couple of weeks they dropped the topic."
default quest_asterion_description04b = 0 # "According to {color=#f6d6bd}Eudocia{/color}, Asterion was preparing for “a great journey.”"
default quest_asterion_description04c = 0 # "According to {color=#f6d6bd}Eudocia{/color}, Asterion was looking for a way to “borrow” one of her golems."
default quest_asterion_description05 = 0 #"According to {color=#f6d6bd}Thais{/color}, {color=#f6d6bd}Howler’s Dell{/color} has banished Asterion as a result of his failed mission."
default quest_asterion_description05b = "" #"She believes I should look for him in the northern villages."
default quest_asterion_description06 = 0 #"According to {color=#f6d6bd}Akakios{/color}, Asterion bought from him a sickle sword. Pathfinders use them to cut through thickets."
default quest_asterion_description07 = 0 # "I’ve heard a more detailed description of Asterion’s {color=#f6d6bd}saurian{/color}. It’s larger than a horse, dark green, though the edges of its limbs, tail, and eyebrows are red-and-orange."
default quest_asterion_description08 = 0 # "In {color=#f6d6bd}Old Págos{/color} I heard that he was planning to restore the watchtower that stands at the eastern crossroads."
default quest_asterion_description09 = 0 # "According to {color=#f6d6bd}Aeli{/color}, {color=#f6d6bd}Asterion{/color} was tasked with finding iron and steel for the monastery. It’s possible that he purchased them in either {color=#f6d6bd}Gale Rocks{/color} or {color=#f6d6bd}Creeks{/color}."
default quest_asterion_description10 = 0 # "According to {color=#f6d6bd}Foggy{/color}, Asterion had been seen purchasing a boat in {color=#f6d6bd}Gale Rocks{/color}."
default quest_asterion_description11a = 0 # "I heard that the villagers from {color=#f6d6bd}White Marshes{/color} are also looking for him."
default quest_asterion_description12 = 0 # "{color=#f6d6bd}Elah{/color} told me that {color=#f6d6bd}Asterion{/color} was seeking something of great value, and {color=#f6d6bd}Glaucia{/color}, the leader of bandits, was aiming to help him."
default quest_asterion_description13 = 0 #"{color=#f6d6bd}Cephas and Gaiane{/color} told me that {color=#f6d6bd}Asterion{/color} was meant to examine the state of the ruins and the caves that can be found on the island’s volcano, and to bring news about them to the Tribe."
default quest_asterion_description14 = 0 #"{color=#f6d6bd}Glaucia{/color} told me that {color=#f6d6bd}Asterion{/color} was meant to find a treasure left behind in a cave by {color=#f6d6bd}The Tribe of The Green Mountain{/color} on {color=#f6d6bd}High Island{/color}, at the feet of the volcano."
default quest_asterion_description15 = 0 #"According to {color=#f6d6bd}Thyrsus{/color}, {color=#f6d6bd}Asterion{/color} promised him to “take care of” the conflict between {color=#f6d6bd}White Marshes{/color} and {color=#f6d6bd}Glaucia{/color}, the bandit, as well as of the undead kept by his own tribe."
default quest_asterion_description16 = 0 # "According to {color=#f6d6bd}Thyrsus{/color}, {color=#f6d6bd}Asterion{/color} bought out his supplies of various poisons and “bogey balms” meant for beasts, including ones that live on the sea, such as harpies. He “was heading for {i}a’journey{/i}.”"
default quest_asterion_description17 = 0 # "{color=#f6d6bd}Helvius{/color} from {color=#f6d6bd}White Marshes{/color} told me to speak with {color=#f6d6bd}Thyrsus{/color}, the warlock."

default quest_pc_goal = 0 # [quest_pc_goal_name]
default quest_pc_goal_name = "" #ineedmoney ("Gather Wealth") / iwantmoney ("Become Rich") / iwanttoberemembered ("Become a Hero") / iwanttohelp ("Help Others") / iwanttostartanewlife ("A New Life") / iwantstatus ("Gain Influence")
default quest_pc_goal_description_completed_ineedmoney = 0 #"I have a bottle of {color=#f6d6bd}Night’s Bane{/color}, a wine left by {color=#f6d6bd}Asterion{/color}. If it’s the real deal, it will surely help me support the people I care about."
default quest_pc_goal_description_completed_iwantmoney = 0 #"I have a bottle of {color=#f6d6bd}Night’s Bane{/color}, a wine left by {color=#f6d6bd}Asterion{/color}. If it’s the real deal, it will make me incredibly rich in {color=#f6d6bd}Hovlavan{/color}."
default quest_pc_goal_description_completed_ineedmoney100 = 0 #"I’ve gathered at least one hundred dragon coins. They will surely help me support the people I care about."
default quest_pc_goal_description_completed_iwantmoney100 = 0 #"I’ve gathered at least one hundred dragon coins. It’s a good start to help me get rich in {color=#f6d6bd}Hovlavan{/color}."
default quest_pc_goal_description_completed_iwantstatus = 0 #""
default quest_pc_goal_description_completed_iwanttoberemembered = 0 #""
default quest_pc_goal_description_completed_iwanttohelp = 0 #""
default quest_pc_goal_description_completed_iwanttostartanewlife = 0 #""
default quest_pc_goal_description01 = 0 #"I heard that the people of {color=#f6d6bd}Creeks{/color} may be willing to invite me to live with them."
default achievement_pc_goal_description = 0

default quest_birdhunting = 0 # "Bird Hunting"
default quest_birdhunting_description00 = "{color=#f6d6bd}Ilan{/color} and {color=#f6d6bd}Tzvi{/color}, two foragers working in {color=#f6d6bd}Foggy’s tavern{/color}, have invited me to join them on their hunt for a runner. They wish to capture it alive."
default quest_birdhunting_description01 = 0 # works
default quest_birdhunting_description02 = 0 #"The bird is nowhere to be found."
default quest_birdhunting_description03 = 0 #"The trip was a failure. The bird managed to run away."
default quest_birdhunting_description04 = 0 #"The trip has been a partial success. The bird died in the process, but at least we’ve got its meat."
default quest_birdhunting_description05 = 0 #"The trip has been a success. I received my reward."
default quest_birdhunting_description06 = 0 #"I was asked to bring the news about the creature to {color=#f6d6bd}Creeks{/color} in a day or so."
default quest_birdhunting_description07 = 0 #"The bird is already in {color=#f6d6bd}Creeks{/color}. It’s too late for me to deliver the message."
default quest_birdhunting_description08 = 0 #"I received my reward for delivering the message."

default quest_closedtunnel = 0 # "(The) Closed Tunnel"
default quest_closedtunnel_description00 = 0 #"The tunnel leading through the northern mountains is closed. Opening the gate would make this route safer."
default quest_closedtunnel_description01 = 0 #"The tunnel hides a group of undead. To have a better chance at fighting them, I could ask someone to teach me how to construct simple traps."
default quest_closedtunnel_description01a = 0 #"The tunnel hides a group of undead. To have a better chance at fighting them, I could construct some simple traps."
default quest_closedtunnel_description02 = 0 #"The undead are going to stay at the entrance. Before I face them, I should prepare myself for combat."
default quest_closedtunnel_description03 = 0 #"The undead are destroyed, but I still need to open the gate." #"The undead are destroyed, but I still need to make sure the tunnel can be crossed."
default quest_closedtunnel_description04 = 0 #"The gate is now open. The locals could be interested in this."

default quest_cursedcoins = 0 # "(The) Cursed Coins"
default quest_cursedcoins_dayofreceived = 0 # day
#00 - "{color=#f6d6bd}Navica{/color} from {color=#f6d6bd}Gale Rocks{/color} asked me to get rid of the coins she received for reaching {color=#f6d6bd}High Island{/color}. To do so, I need to ride to {color=#f6d6bd}Beholder{/color}, the tree south of {color=#f6d6bd}Howler’s Dell{/color}, and place the pouch on the altar."
default quest_cursedcoins_description01 = 0 #1 - "I decided to keep the coins to myself, but I can still lie to their owner."
default quest_cursedcoins_description02 = 0 #1 - "I decided to keep the coins to myself, and to forget about the whole thing."
default quest_cursedcoins_description03 = 0 #1 - "I did as she asked, but the coins seem fine. I kept them to myself, and should now return to {color=#f6d6bd}Navica{/color}."
default quest_cursedcoins_description04 = 0 #1 - "I got rid of the coins for good. I should return to {color=#f6d6bd}Navica{/color}."
default quest_cursedcoins_description05 = 0 #1 - "{color=#f6d6bd}Navica{/color} agreed to join my crew."

default quest_bronzerod = 0 # "Bronze Rods"
default quest_bronzerod_description00 = "I’m meant to place the bronze rods in high points all across the peninsula, which will allow Eudocia’s sentinels to reach new parts of the land and collect valuable resources."
default quest_bronzerod_description00b = "It’s crucial that one of the rods will be placed in {color=#f6d6bd}White Marshes{/color}."
default quest_bronzerod_description00c = "I can get the first share of my reward after placing at least four rods."
default quest_bronzerod_description02 = "I still have to place a rod in {color=#f6d6bd}White Marshes{/color}."
default quest_bronzerod_description03 = 0 #"I’ve placed the rods, but not in {color=#f6d6bd}White Marshes{/color}. Let’s hope {color=#f6d6bd}Eudocia{/color} is going to pay anyway."
default quest_bronzerod_description04 = 0 #"I’ve placed some of the rods, but I don’t have any of them left."
default quest_bronzerod_description05 = 0 #"I’ve placed all of the rods."
default quest_bronzerod_description06 = 0 #"I collected my reward."
default quest_bronzerod_description07 = 0 #"I’ve placed fewer than four rods, but don’t have any of them left. I should inform Eudocia."
default quest_bronzerod_description08 = 0 #"I’ve informed Eudocia about my failure. She wasn’t happy."

default quest_easternpath_points = 0
default quest_easternpath_points_max = 8
default quest_easternpath = 0 # "Eastern Path"
default quest_easternpath_description_teaser = 0 #"{color=#f6d6bd}Thais{/color}, the mayor of {color=#f6d6bd}Howler’s Dell{/color}, claims that the people from {color=#f6d6bd}Creeks{/color}, a hunting village in the far north, have some issues with maintaining their roads."
default quest_easternpath_description00 = 0 #"People from {color=#f6d6bd}Creeks{/color} are interested in reclaiming the neglected road that connects their village with the southern crossroads."
default quest_easternpath_description01 = 0 #"{color=#f6d6bd}Elah{/color} wants me to get to know the roads that connect {color=#f6d6bd}Foggy Lake{/color} with both {color=#f6d6bd}western crossroads{/color} and {color=#f6d6bd}southern crossroads{/color} and do as much as I can to make them more secure, or at least bring to him news about what can be done to make them so."
default quest_easternpath_description02 = 0 #"I’ll receive dragon bones depending on what I’ll accomplish."
default quest_easternpath_description03 = 0 #"I got rid of a small pack that lived in the ruined shelter in the west and took a look at the building." - 2 points
default quest_easternpath_description03a = 0 #"I received my reward for getting rid of the dusk foxes."
default quest_easternpath_description03alt = 0 #"I don’t think humans should disturb the dusk foxes at the shelter in the west." - 1 point # ruinedshelter_lefttobeasts
default quest_easternpath_description03aalt = 0 #"I received my reward for bringing news about the dusk foxes."
default quest_easternpath_description04 = 0 #"I’ve restored the stream ford that connects the eastern road with the heart of the forest." - 1 point
default quest_easternpath_description04a = 0 #"I received my reward for fixing the brook ford leading to the heart of the forest."
default quest_easternpath_description05 = 0 #"The spider from the cabin is gone." - 1 point
default quest_easternpath_description05a = 0 #"I received my reward for removing the spider from the hunter’s cabin."
default quest_easternpath_description06 = 0 #"I cleared the bushes leading east of the old stone bridge." - 1 point
default quest_easternpath_description06a = 0 #"I was asked to place a new sign at the path leading east of the old stone bridge."
default quest_easternpath_description06alt = 0 #"I placed the sign at the path leading east of the old stone bridge." - 1 point
default quest_easternpath_description06aalt = 0 #"I received my reward for placing the sign."
default quest_easternpath_description07 = 0 #"I cleared the statue south of {color=#f6d6bd}Foggy’s{/color} place." - 0 point?
default quest_easternpath_description07a = 0 #"I received my reward for clearing the statue."
default quest_easternpath_description08 = 0 #"The watchtower is clear and ready for new guards." - 2 points
default quest_easternpath_description08a = 0 #"I received my reward for bringing the news about the watchtower."
default quest_easternpath_description08alt = 0 #"The watchtower is clear, though its door is broken." - 1 point
default quest_easternpath_description08aalt = 0 #"I received my reward for bringing the news about the watchtower."
default quest_easternpath_description09 = 0 #"I encountered a fallen tree in the south of the peninsula."
default quest_easternpath_description09a = 0 #"I was asked to assist the villagers in their travel to the fallen tree. I should meet with them some day before noon, but only if I know the entire route and it’s safe enough to travel in a large group. To make the road safer, I should improve it further."
default quest_easternpath_description09aa = 0 #"I received my reward for assisting the villagers in removing the fallen tree." + 3 points
default quest_easternpath_description09b = 0 #"I received my reward for informing the villagers about the fallen tree." + 1 points
default quest_easternpath_description10 = 0 # "I took a look at the dolmen in the south. It’s safe." + 1
default quest_easternpath_description10a = 0 #"I received my reward for bringing the news about the dolmen."
default quest_easternpath_description11 = 0 #"I received my reward for sharing the detailed description of the shortcut."
default quest_easternpath_description13 = 0 #"I received my reward for making a deal with {color=#f6d6bd}Eudocia{/color}."
default quest_easternpath_description12 = 0

default quest_easternpath_description_final = 0 #"My job at the eastern path is done. Without regular patrols, it won’t get safer anytime soon."

default quest_empresscarp = 0 #"Empress Carp"
default quest_empresscarp_description00 = "{color=#f6d6bd}The druid from the cave{/color} has asked me to travel to {color=#f6d6bd}Gale Rocks{/color} and look for a fisher named {color=#f6d6bd}Photios{/color}, a young father. I’m meant to collect his debt - a male empress carp - and bring it in one piece back to the cave."
default quest_empresscarp_description00b = "My reward is going to be one-time access to the man’s healing powers."
default quest_empresscarp_description01 = 0 # "I can collect my reward whenever I want to."

default quest_escortpyrrhos = 0 #"Escort The Scavenger"
default quest_escortpyrrhos_description01 = 0 # więcej w dzienniku
default quest_escortpyrrhos_description02 = 0 # "I can also take him to {color=#f6d6bd}Pelt of the North{/color}."
default quest_escortpyrrhos_description03 = 0 # "For my help, he offers me either dragon bones, or a mixture that “scares apemen away.” (# "For my help, he’s offering me information about the peninsula and either coins, or a mixture that “scares apemen away.”")
default quest_escortpyrrhos_description04 = 0 # "The man is currently in Howler’s Dell. He told me to return after the night to get my reward." / "The man is currently at Pelt of the North. He told me to return after the night to get my reward."
default quest_escortpyrrhos_description05 = 0 # "I’ve got my coin." / "I took a... potion."
default quest_escortpyrrhos_description06 = 0 # "He’s no longer in the ruins, even though he left behind some of his stuff. He was probably finished off by the nearby goblin camp."

default quest_fallentree = 0 #"Fallen Tree"
default quest_fallentree_description00 = "The road in the East is blocked by a fallen tree. Clearing this path would support future trade routes."
default quest_fallentree_description01 = 0 # ""
default quest_fallentree_description02 = 0 # "Whoever was present at the wagon, was then passing by the abandoned watchtower, and even reached the heart of the forest. I can follow them from the cairn."
default quest_fallentree_description03 = 0 # "When I mentioned the abandoned wagon to a group of travelers, they said the bandits are the most likely culprits."
default quest_fallentree_description04 = 0 # "I’ve no doubt it was {color=#f6d6bd}Glaucia{/color} and her band who took the people from the wagon at the fallen tree."
default quest_fallentree_description05 = 0 # ""
default quest_fallentree_description06 = 0 # "The road is now passable."

default quest_fetchingfood = 0 #Fetching Food
default quest_fetchingfood_description01 = 0 # "I delivered the food."

default quest_fisherhamlet_gray = 0
default quest_fisherhamlet = 0 # "The Old Hamlet"
default quest_fisherhamlet_description00 = "{color=#f6d6bd}Thais{/color}, the mayor of {color=#f6d6bd}Howler’s Dell{/color}, has told me about an old fishing hamlet set northwest from her village. She wants to restore it, but the mountain pass leading to it was buried by a rockslide."
default quest_fisherhamlet_description00b = "My first task is to check if that spot is currently safe."
default quest_fisherhamlet_description01 = 0 #"It looks like something might have been buried beneath the rocks. I should report this to Thais."
default quest_fisherhamlet_description02 = 0 #"Once I’m ready, I should get to {color=#f6d6bd}Howler’s{/color} during the early morning hours. We’re going to organize workers and clear the rockslide, though it may take up to an entire day"
default quest_fisherhamlet_description03 = 0 #"We’ve removed the rocks and gotten rid of an undead that was buried beneath them. I should report this to Thais."
default quest_fisherhamlet_description04 = 0 #"I was asked to cross the mountain pass and to reach the hamlet itself. I need to inspect the buildings and look for unusual creatures."
default quest_fisherhamlet_description04cd = 0 #"I met {color=#f6d6bd}Aegidia{/color}, the not-so-dead daughter of {color=#f6d6bd}Thais{/color}. She’s asked me to lie in her name and to talk her mother out of regaining the hamlet."
default quest_fisherhamlet_description05 = 0 #"I’ve been to the hamlet. I should return to {color=#f6d6bd}Thais{/color}."
default quest_fisherhamlet_description05proto = "I don’t yet know enough about the hamlet to return to {color=#f6d6bd}Thais{/color}."
default quest_fisherhamlet_description06 = 0 #"I talked to {color=#f6d6bd}the druids{/color} that live in {color=#f6d6bd}Howler’s Dell{/color}. They want the hamlet to stay abandoned."
default quest_fisherhamlet_description06a = 0
default quest_fisherhamlet_description06b = "" #"They believe that {color=#f6d6bd}Thais{/color} pushes the village in a dangerous direction."
default quest_fisherhamlet_description07 = 0 #"I talked with {color=#f6d6bd}Thais{/color}. I encouraged her to send workers to the hamlet and I’ve told her about her daughter."
default quest_fisherhamlet_description08 = 0 #"I talked with {color=#f6d6bd}Thais{/color}. I encouraged her to send workers to the hamlet, but I’ve kept the truth about her daughter to myself."
default quest_fisherhamlet_description09 = 0 #"I talked with {color=#f6d6bd}Thais{/color}. I told her to stay away from the hamlet and about her daughter."
default quest_fisherhamlet_description10 = 0 #"I talked with {color=#f6d6bd}Thais{/color}. I told her to stay away from the hamlet, but I’ve kept the truth about her daughter to myself."
default quest_fisherhamlet_description11 = 0 #"{color=#f6d6bd}Thais{/color} has walked away without handing me the letter that she promised. I should speak with her tomorrow."
default quest_fisherhamlet_description12 = 0 #"I received my reward."

default quest_eudociaflower = 0 # "Flowers for Eudocia"
default quest_eudociaflower_description00 = "{color=#f6d6bd}Eudocia{/color} wants me to pick a few “orange tulips” for her."
default quest_eudociaflower_description01 = 0 #"According to {color=#f6d6bd}Eudocia{/color}, the flowers can be found in shadowy meadows that grow in deep forests."
default quest_eudociaflower_description03 = 0 #"I received my reward."
default quest_eudociaflower_description04 = 0 #"I called off our deal."

default quest_intelforpeltnorth = 0 #Glaucia’s Band
default quest_intelforpeltnorth_rewardvalue = 0
default quest_intelforpeltnorth_description01 = 0 #"According to {color=#f6d6bd}Pelt’s innkeep{/color}, {color=#f6d6bd}Glaucia{/color} and her band have broken the truce with the local villages. He’s going to pay me three dragons if I get in touch with {color=#f6d6bd}Thais{/color}, the mayor of {color=#f6d6bd}Howler’s Dell{/color}, and bring him her response."
default quest_intelforpeltnorth_description02 = 0 #"{color=#f6d6bd}The druid from the cave{/color} in the southwest has warned me that {color=#f6d6bd}Glaucia{/color} won’t be happy if she finds out that I’ve been trying to mess with her."
default quest_intelforpeltnorth_description02b = 0 #"I need to find out where the bandits have been active in the recent past."
default quest_intelforpeltnorth_description03 = 0 #"It looks like the bandits have been especially harsh toward {color=#f6d6bd}White Marshes{/color} village."
default quest_intelforpeltnorth_description04 = 0 #"{color=#f6d6bd}Thais{/color} won’t answer my question until I learn more about the “raids” from the northern villages - {color=#f6d6bd}White Marshes{/color}, {color=#f6d6bd}Gale Rocks{/color}, and {color=#f6d6bd}Creeks{/color}."
default quest_intelforpeltnorth_description04a = 0 # {color=#f6d6bd}White Marshes{/color} has suffered from bandit attacks quite severely.
default quest_intelforpeltnorth_description04b = 0 #"{color=#f6d6bd}Creeks{/color} has had no issues with the bandits."
default quest_intelforpeltnorth_description04c = 0 #"The people of {color=#f6d6bd}Gale Rocks{/color} claim that bandits are not a big issue."
default quest_intelforpeltnorth_description05 = 0 #"{color=#f6d6bd}Thais{/color} has decided to reject the collaboration. I should return to the innkeeper."
default quest_intelforpeltnorth_description06 = 0 #"I brought the news to {color=#f6d6bd}Thais{/color}, but she has decided to reject the invitation. I should bring the news to the innkeeper."
default quest_intelforpeltnorth_description07 = 0 #"I received my payment."
default quest_intelforpeltnorth_description08 = 0 #"The keeper wants me to find the bandit’s camp and speak with {color=#f6d6bd}Glaucia{/color} herself."
default quest_intelforpeltnorth_description10 = 0 #"I’ve learned that {color=#f6d6bd}Glaucia{/color} tries to destroy the necromancers of {color=#f6d6bd}White Marshes{/color}. I should bring the news to the keeper."
default quest_intelforpeltnorth_description11 = 0 #"I received my last payment for the job."

default quest_healingtheplague = 0 # "Healing the Plague"
default quest_healingtheplague_description_pre = 0 #"{color=#f6d6bd}Aeli{/color} believes that the plague can only be healed by time, or by “a mage more powerful than anyone in the order.”"
default quest_healingtheplague_description00 = 0 #"{color=#f6d6bd}The druids from Howler’s Dell{/color} have told me that if I care about healing the plague that has stricken {color=#f6d6bd}Old Págos{/color}, I should speak with a man who lives in a cave in the South."
default quest_healingtheplague_description01 = 0 # "{color=#f6d6bd}The old druid from the cave{/color} has told me that to help the sick people from {color=#f6d6bd}Old Págos{/color} he’d need to use the Holy Seed born from {color=#f6d6bd}Beholder{/color}, the large tree growing near the altar."
default quest_healingtheplague_description02 = 0 # "The tree “eats magic,” which can also be found in human blood."
default quest_healingtheplague_description03 = "I’ve got the Seed. I should report to the druid."
default quest_healingtheplague_description04 = "I’ve eaten the Seed. I should report to the druid."
default quest_healingtheplague_description04alt = "I’ve lost the Seed. I should report to the druid."
default quest_healingtheplague_description05 = 0 # "I gave away the Seed. Whenever I’m ready, I should return to the druid no later than six hours before nightfall, so we can travel together to {color=#f6d6bd}Old Págos{/color} and back."
default quest_healingtheplague_description05alt = 0 # "I gave away the seed. I now need to visit the village of {color=#f6d6bd}Howler’s Dell{/color}, so we can safely pass through it. Whenever I’m ready, I should return to the druid no later than six hours before nightfall, so we can travel together to {color=#f6d6bd}Old Págos{/color} and back."
default quest_healingtheplague_description07 = 0 # "The village will have to take care of itself without my help."
default quest_healingtheplague_description08 = 0 # "The village is still under quarantine, but it should regain its strength before winter."

default quest_hiddenpurse = 0 # "A Hidden Pouch"
default quest_hiddenpurse_description00 = "{color=#f6d6bd}A woman from White Marshes{/color} has asked me to look for her pouch, which was hidden under the bridge on the eastern road."
default quest_hiddenpurse_description00a = 0 #"It seems like it would be better for her to not mention it to {color=#f6d6bd}Helvius{/color}."
default quest_hiddenpurse_description01 = 0 #"I found the pouch. It contained a single dragon bone."
default quest_hiddenpurse_description02 = 0 #"I brought her the news."
default quest_hiddenpurse_description03 = 0 #"I decided to lie to her and keep the coin to myself."
default quest_hiddenpurse_description04 = 0 #"I told {color=#f6d6bd}Helvius{/color} about her request. She’ll now face consequences."

default quest_readtheletter = 0 # "Read the Letter"
default quest_readtheletter_description00 = "{color=#f6d6bd}A man from White Marshes{/color} has handed me a wax tablet. He wants me to find someone who could read its contents."
default quest_readtheletter_description00a = 0 #"He told me I could find help among followers of The Wright."
# default quest_readtheletter_description01 = 0 #"According to the letter, {color=#f6d6bd}Valens’{/color} husband left him for another person." # item_letterwhitemarshes_read
default quest_readtheletter_description00b = 0 #"According to {color=#f6d6bd}Thyrsus{/color}, it’d be better to spare {color=#f6d6bd}Valens{/color} unnecessary suffering."
default quest_readtheletter_description01 = 0 #"I brought him the news and received my reward."
default quest_readtheletter_description01alt = 0 #"I lied to him about the contents and received my reward."
default quest_readtheletter_description02 = 0 #"I sold the tablet before I read its contents."
default quest_readtheletter_description03 = 0 #"I sold the tablet before I spoke with its owner."
default quest_readtheletter_description04 = 0 # best ending

default quest_healingpotion = 0 # "The Merchant’s Medicament" Akakios
default quest_healingpotion_description00b = 0 #"I could look for the potion in a “secret chamber” of a dolmen, somewhere along the southern road. The merchant gave me a key to it.
default quest_healingpotion_description00c = 0 #"Maybe I could buy a flask or two from {color=#f6d6bd}the monks{/color} who live near {color=#f6d6bd}Old Págos{/color}?"
default quest_healingpotion_description00d = 0 #"It looks like I won’t be able to get the potion from the monks."
default quest_healingpotion_description00d_alt = 0 #"{color=#f6d6bd}Aeli{/color} told me to ask {color=#f6d6bd}Foggy{/color} about the dolmen."
default quest_healingpotion_description00d_alt2 = 0 #"{color=#f6d6bd}Foggy{/color} told me to dig, and mentioned the dolmen’s walls may be covered in soot."
default quest_healingpotion_description01 = 0 #"I found the box."
default quest_healingpotion_description02 = 0 #"It turns out that the box was containing a bottle, probably a magical potion."
default quest_healingpotion_description03 = 0 #"I have brought back “the medicament” and received my reward."
default quest_healingpotion_description04 = 0 #"I have lost the potion. I should speak with the merchant."
default quest_healingpotion_description05 = 0 #"He was far from happy."

default quest_gatheracrew = 0 # "Gather a Crew"
default quest_gatheracrew_description00 = "{color=#f6d6bd}Asterion{/color} has been seen heading to {color=#f6d6bd}High Island{/color}, northwest from the peninsula. Traveling there all by myself is going to be dangerous - it would be safer to gather a crew willing to explore this place with me. Maybe some of the people I’ve helped in the past would be interested in helping me."
default quest_gatheracrew_description00a = "If no one agrees to join me, I can also attempt a lone journey."
default quest_gatheracrew_description00b = "Once I’m ready, I need to go to my boat in the early morning hours. From there, I’ll gather my crew and we’ll leave in the evening."
default quest_gatheracrew_description00boatgalerockssteal = 0 #""
default quest_gatheracrew_description00boatfishinghamlet = 0 #""
default quest_gatheracrew_description00boatgalerocksrent = 0 #""
default quest_gatheracrew_description01 = 0 #"I could put some time into learning more about the statue of a giant, and learn the “map” it hides."
# default quest_gatheracrew_description02a = 0"{color=#f6d6bd}The monks{/color} are not willing to join me. Maybe I’ll convince them if I can show them that it’s worthwhile to have me on their good side."

default quest_spiritrock = 0 # "(A) Spirit Rock"
default quest_spiritrock_description00 = "{color=#f6d6bd}Photios{/color}, a fisher from {color=#f6d6bd}Gale Rocks{/color}, has asked me to travel to {color=#f6d6bd}an enchantress{/color} who lives in the East and ask her for a “spirit rock” to help {color=#f6d6bd}Phoibe{/color}, his spell-less daughter."
default quest_spiritrock_description02 = "According to {color=#f6d6bd}Eudocia{/color}, her spirit rocks won’t help in this scenario."
default quest_spiritrock_description03 = "I have a spirit rock."
default quest_spiritrock_description04 = 0 # "I collected my reward."

default quest_spyonwhitemarshes = 0 # "Spy on White Marshes"
default quest_spyonwhitemarshes_description01 = 0 # "I was asked by {color=#f6d6bd}Glaucia{/color} to gather as much information as I can about the defenses of the village of {color=#f6d6bd}White Marshes{/color}."
default quest_spyonwhitemarshes_description01a = 0 # "The locals won’t let me wander around their village. Maybe I could take a closer look at this when there’s fewer curious eyes."
default quest_spyonwhitemarshes_description02 = 0 # "I received my reward."
default quest_spyonwhitemarshes_description03 = 0 # "I rejected her offer... Though she wasn’t happy about it."
default quest_spyonwhitemarshes_description04 = 0 # "I couldn’t finish the job."

default quest_matchmaking_points = 0
default quest_matchmaking_points_max = 4
default quest_matchmaking = 0 # "Matchmaking"
default quest_matchmaking_description00 = "The youth of the peninsula could use help with starting families at other settlements. I can ask around, learn if anyone seeks a match for the approaching spring."
default quest_matchmaking_description00b = "I don’t think there’s anyone else who’s looking for a match."

# default quest_messageseverina_dayofreceiving = 0 # day
# default quest_messageseverina = 0 # "Message To Akakios"
# default quest_messageseverina_description_akakios00 = "{color=#f6d6bd}Severina{/color}, the headwoman of {color=#f6d6bd}Gale Rocks{/color}, will pay me one dragon bone for delivering her message to {color=#f6d6bd}Akakios{/color} from {color=#f6d6bd}Howler’s Dell{/color}."
# default quest_messageseverina_description_akakios01 = 0 #"I’ve spoken to {color=#f6d6bd}Akakios{/color}."
# default quest_messageseverina_description_akakios02 = 0 #"I received my payment."
# default quest_messageseverina_description_akakios03 = 0 #"I’ve decided to lie to {color=#f6d6bd}Severina{/color} instead."
# # quest Message To Akakios przerobić na "weź się dowiedz kto nam może sprzedać najtaniej mąkę w tym roku", ale akakios i white marshes chcą wiedzieć, czemu PC pyta, można kłamać, wtedy są gorsze ceny.

default quest_foggy1oldpagos = 0 # "Check on Old Págos"
default quest_foggy1oldpagos_description00 = "{color=#f6d6bd}Foggy{/color}, the tavern keeper from the northern crossroads, is wondering why the people of {color=#f6d6bd}Old Págos{/color} stopped visiting her place to trade. I can find the village riding west of the western crossroads, among the mountains."
default quest_foggy1oldpagos_description01 = 0 # "I collected my reward."

default quest_foggy2iason = 0 # "Check on Iason"
default quest_foggy2iason_description00 = "{color=#f6d6bd}Foggy{/color}, the tavern keeper from the northern crossroads, wants me to ask {color=#f6d6bd}Iason{/color} of {color=#f6d6bd}Pelt of the North{/color} if he’s still interested in their deal. She’s “displeased” about his recent silence."
default quest_foggy2iason_description01 = 0 # {color=#f6d6bd}Iason{/color} is unable to keep his side of the bargain, but wants me to lie to in his name. It seems to me like he made a decision a long time ago.
default quest_foggy2iason_description02 = 0 # "I told {color=#f6d6bd}Iason{/color} I’ll fulfill his wish."
default quest_foggy2iason_description02a = 0 # "I lied to {color=#f6d6bd}Iason{/color} that I’d fulfill his wish."
default quest_foggy2iason_description03 = 0 # "I lied to {color=#f6d6bd}Foggy{/color}. I collected my reward."
default quest_foggy2iason_description04 = 0 # "I told {color=#f6d6bd}Foggy{/color} the truth. I collected my reward."

default quest_foggy3whitemarshes = 0 # "Cask of Cider"
default quest_foggy3whitemarshes_description00 = "{color=#f6d6bd}Foggy{/color}, the tavern keeper from the northern crossroads, wants me to deliver a cask of apple cider to the people of {color=#f6d6bd}White Marshes{/color}, who paid for it a long time ago."
default quest_foggy3whitemarshes_description01 = 0 # "For whatever reason, {color=#f6d6bd}mayor Helvius{/color} refuses to accept it. Maybe someone else would do so, or I could just bring it back to {color=#f6d6bd}Foggy{/color}."
default quest_foggy3whitemarshes_description02 = 0 # "I convinced {color=#f6d6bd}Thyrsus{/color} to take and hide the cask."
default quest_foggy3whitemarshes_description03 = 0 # "I collected my reward."
default quest_foggy3whitemarshes_description04 = 0 # "I’ve brought the cask back to {color=#f6d6bd}Foggy{/color}. I collected my reward."
default quest_foggy3whitemarshes_description05 = 0 # "I’ve decided to keep the cask to myself. I lied to {color=#f6d6bd}Foggy{/color} about it and received my reward."
default quest_foggy3whitemarshes_description06 = 0 # "I’ve decided to keep the cask to myself. I told the truth about it to {color=#f6d6bd}Foggy{/color} and she’s decided to break our deal."
default quest_foggy3whitemarshes_description07 = 0 # "I sold the cask outside of {color=#f6d6bd}White Marshes{/color}. Let’s hope {color=#f6d6bd}Foggy{/color} won’t learn about it."

default quest_lostmerchants = 0 # "(The) Lost Merchants"
default quest_lostmerchants_description00 = "{color=#f6d6bd}Severina{/color}, the headwoman of {color=#f6d6bd}Gale Rocks{/color}, will pay me five dragon bones for learning what happened to a group of merchants who were supposed to show up a few days ago. I was asked to not mention them to anyone."
default quest_lostmerchants_description01 = 0 #"I’ve learned that {color=#f6d6bd}Glaucia{/color} and her band attacked the traders. I should report this to {color=#f6d6bd}Severina{/color}."
default quest_lostmerchants_description02 = 0 #"I received my payment."
default quest_lostmerchants_description03 = 0 #"I decided to tell her that they are nowhere around."

default quest_missinghunters_gaveup = 0
default quest_missinghunters = 0 # "(The) Missing Hunters"
default quest_missinghunters_admonfound = 0 # the one from the ghoulcave. 1 - found, 2 - reported with evidence, 3 - reported WITHOUT evidence
default quest_missinghunters_admonknown = 0
default quest_missinghunters_daliafound = 0 # from howlers lair
default quest_missinghunters_daliaknown = 0
default quest_missinghunters_vaschelfound = 0 # from shortcut
default quest_missinghunters_vaschelknown = 0
default quest_missinghunters_reported = 0
default quest_missinghunters_description00 = "The people of {color=#f6d6bd}Creeks{/color} are afraid of what happened to the three hunters who were trying to outdo each other in the wilderness. {color=#f6d6bd}Efren{/color} wants me to find them, and ideally bring him evidence to back up my words."
default quest_missinghunters_description01 = 0#"When possible, I should speak with {color=#f6d6bd}Elah{/color} during evening hours and participate in the parting rites."
default quest_missinghunters_description02 = 0#"{color=#f6d6bd}Efren{/color} will help me in time of need."
default quest_missinghunters_description03 = 0#"This task wasn’t worth the effort."

default quest_orentius = 0 #Orentius, the Necromancer
default quest_orentius_thyrsus_description01 = 0 #"{color=#f6d6bd}Thyrsus{/color} will help me meet with {color=#f6d6bd}Orentius{/color} if I make it worth his time and trust."
default quest_orentius_thyrsus_description02 = 0 #"{color=#f6d6bd}Thyrsus{/color} can wait until I spend the night in {color=#f6d6bd}White Marshes{/color}. I should return to him only once I’m ready to speak with {color=#f6d6bd}Orentius{/color} - it’s the only chance I’ll get. # "{color=#f6d6bd}Thyrsus{/color} will wait for me to fall asleep in {color=#f6d6bd}White Marshes{/color}. He’ll then take me to {color=#f6d6bd}Orentius{/color}."
default quest_orentius_thyrsus_description03 = 0 # "Thanks to me, {color=#f6d6bd}White Marshes{/color} abandoned their necromantic practices."
default quest_orentius_thyrsus_description04 = 0 # "Not only I failed at getting rid of the necromancers, the villagers won’t put any trust in me anymore. This matter is now out of my hands."
default quest_orentius_thyrsus_description05 = 0 # "I stopped the necromancers... And destroyed the entire village at the same time."

default quest_orentius_helvius_description01 = 0 #"{color=#f6d6bd}Helvius{/color} will agree to introduce me to {color=#f6d6bd}Orentius{/color} if he decides I proved to be a trustworthy ally of his tribe."
default quest_orentius_helvius_description02 = 0 #"Once I’m ready, I should tell {color=#f6d6bd}Helvius{/color} to introduce me to {color=#f6d6bd}Orentius{/color}. It’s going to be my only opportunity to speak with him, so I should be sure I know what I’m doing."
default quest_orentius_helvius_description03 = 0 # "Thanks to me, {color=#f6d6bd}White Marshes{/color} abandoned their necromantic practices."
default quest_orentius_helvius_description04 = 0 # "Not only I failed at getting rid of the necromancers, the villagers won’t put any trust in me anymore. This matter is now out of my hands."
default quest_orentius_helvius_description05 = 0 # "I stopped the necromancers... And destroyed the entire village at the same time."

default quest_orentius_thais_description00betrayal = 0#"I warned the village about {color=#f6d6bd}Thais’{/color} plans. She won’t be able to get in by surprise."
default quest_orentius_thais_description00 = 0#{color=#f6d6bd}Thais{/color} wants to get rid of the undead that serve {color=#f6d6bd}Orentius{/color}, the priest of {color=#f6d6bd}White Marshes{/color}.
default quest_orentius_thais_description01 = 0 #"My first task is to reach {color=#f6d6bd}White Marshes{/color} and see the scale of the problem with my own eyes."
default quest_orentius_thais_description02 = 0 #"I spoke with {color=#f6d6bd}Helvius{/color} about meeting with {color=#f6d6bd}Orentius{/color}. I should report back to Thais."
default quest_orentius_thais_description03 = 0 #"I was asked to speak with the {i}leaders{/i} of other settlements and find some allies willing to join our efforts."

default quest_orentius_thais_description03a01 = 0 #"The hunters from {color=#f6d6bd}Pelt of the North{/color} are going to support {color=#f6d6bd}Thais’{/color} cause."
default quest_orentius_thais_description03a02 = 0 #"{color=#f6d6bd}Old Págos{/color} doesn’t trust {color=#f6d6bd}Thais’{/color} judgment, but will also not support the people of {color=#f6d6bd}White Marshes{/color}."
default quest_orentius_thais_description03a03 = 0 #"{color=#f6d6bd}The monks{/color} have refused to share their thoughts on the matter." OR "While {color=#f6d6bd}the monks{/color} have officially refused to share their thoughts on the matter, {color=#f6d6bd}Aeli{/color} offered me a gift to help me in my pursuit."
default quest_orentius_thais_description03a05 = 0 #"{color=#f6d6bd}Creeks{/color} isn’t going to plot with {color=#f6d6bd}Thais{/color}. {color=#f6d6bd}Elah{/color} told me it would be wiser to handle the necromancer by myself, without bounding myself to any specific leader."
default quest_orentius_thais_description03a06 = 0 #"{color=#f6d6bd}Severina{/color} of {color=#f6d6bd}Gale Rocks{/color} is not fully convinced, but is willing to send a group to discuss it."
default quest_orentius_thais_description03a07 = 0 #"{color=#f6d6bd}Glaucia{/color} and her band are going to join {color=#f6d6bd}Thais{/color} in her efforts."

default quest_orentius_thais_description03b = 0 #"{color=#f6d6bd}Thais{/color} is ready to organize our raid, though I can still look for more people willing to join us."
default quest_orentius_thais_description03c = 0 #"{color=#f6d6bd}Thais{/color} doubts there’s anyone else who’ll be willing to join us."

default quest_orentius_thais_description04a = "Once I’m ready, I can speak with {color=#f6d6bd}Thais{/color} sometime in the morning. We will start organizing our raid."

default quest_orentius_thais_description06 = 0 #"I’ve taken care of {color=#f6d6bd}Orentius{/color}."
default quest_orentius_thais_description09 = 0 #"I failed - {color=#f6d6bd}Orentius{/color} has kept his position, and I doubt the villagers are going to accept me among them ever again."
default quest_orentius_thais_description10 = 0 #"I decided to refuse to collaborate with {color=#f6d6bd}Thais{/color}."

# quest można wykonać zbierając punkty - jeśli zbierze się odpowiednio dużo punktów, Dalit odrzuca kandydata. Najlepsze rozwiązanie to odrzucić dwóch kandydatów, a potem zaprosić Shoshi po Matchmaking.
# pytanie niektórych NPCów wymaga reputacji, pytanie samych kandydatów zabiera czas

default quest_recruitahunter_possible = 1
default quest_recruitahunter_dalit_started = 0
default quest_recruitahunter_dalit_about_quintus = 0
default quest_recruitahunter_dalit_about_tips = 0
default quest_recruitahunter_dalit_about_reward = 0
default quest_recruitahunter_dalit_about_reward_granted = 0

default quest_recruitahunter_dalit_about_erastos = 0
default quest_recruitahunter_dalit_about_cassia = 0
default quest_recruitahunter_dalit_about_erastos_completed = 0
default quest_recruitahunter_dalit_about_cassia_completed = 0

default quest_recruitahunter_spokento_iason = 0 # nikt - porada, by pogadać z ludźmi spoza wioski
default quest_recruitahunter_spokento_efren = 0 # oba

default quest_recruitahunter_erastos_points = 0 # howlers - chce porzucić życie tam, bo jest nieszczęśliwie zakochany w córce Thais. można o to spytać innych mieszkańców - najwięcej powie Eryx. ogólnie trochę słaby, niezbyt doświadczony.
default quest_recruitahunter_erastos_threshold = 3
default quest_recruitahunter_erastos_threshold2 = 7
default quest_recruitahunter_spokento_erastos = 0
default quest_recruitahunter_erastos_points_notify1 = 0
default quest_recruitahunter_erastos_points_notify2 = 0
default quest_recruitahunter_spokento_erastos_questions1 = 0
default quest_recruitahunter_spokento_erastos_questions2 = 0
default quest_recruitahunter_spokento_erastos_questions3 = 0
default quest_recruitahunter_spokento_erastos_questions4 = 0
default quest_recruitahunter_spokento_erastos_questions5 = 0

default quest_recruitahunter_spokento_bion = 0
default quest_recruitahunter_spokento_bion_gray = 0
default quest_recruitahunter_spokento_thais = 0
default quest_recruitahunter_spokento_thais_gray = 0
default quest_recruitahunter_spokento_eryx = 0
default quest_recruitahunter_spokento_eryx_gray = 0
default quest_recruitahunter_spokento_elpis = 0
default quest_recruitahunter_spokento_elpis_gray = 0
default quest_recruitahunter_spokento_akakios = 0
default quest_recruitahunter_spokento_akakios_gray = 0

default quest_recruitahunter_spokento_quintus = 0
default quest_recruitahunter_spokento_tertia = 0
default quest_recruitahunter_spokento_aeli = 0
default quest_recruitahunter_spokento_foragers = 0
default quest_recruitahunter_spokento_aegidia = 0 # erastos
default quest_recruitahunter_spokento_druid = 0 # erastos, a może odsyła do kogoś w wiosce, kto normalnie nie chce powiedzieć?

default quest_recruitahunter_cassia_points = 0 # w Gale Rocks - jest całkiem spoko wojowniczką, ale nie wie nic o zwierzętach, jest bardzo krzykliwa i pewna siebie, leniwa.
default quest_recruitahunter_cassia_threshold = 3
default quest_recruitahunter_cassia_threshold2 = 6
default quest_recruitahunter_spokento_cassia = 0
default quest_recruitahunter_cassia_points_notify1 = 0
default quest_recruitahunter_cassia_points_notify2 = 0
default quest_recruitahunter_spokento_cassia_questions1 = 0
default quest_recruitahunter_spokento_cassia_questions2 = 0
default quest_recruitahunter_spokento_cassia_questions3 = 0
default quest_recruitahunter_spokento_cassia_questions4 = 0
default quest_recruitahunter_spokento_cassia_questions5 = 0

default quest_recruitahunter_spokento_guard = 0
default quest_recruitahunter_spokento_tatius = 0
default quest_recruitahunter_spokento_tatius_gray = 0
default quest_recruitahunter_spokento_fulvia = 0
default quest_recruitahunter_spokento_rufina = 0
default quest_recruitahunter_spokento_rufina_gray = 0
default quest_recruitahunter_spokento_photios = 0
default quest_recruitahunter_spokento_photios_gray = 0
default quest_recruitahunter_spokento_florus = 0
default quest_recruitahunter_spokento_aquila = 0
default quest_recruitahunter_spokento_aquila_gray = 0
default quest_recruitahunter_spokento_porcia = 0
default quest_recruitahunter_spokento_porcia_gray = 0
default quest_recruitahunter_spokento_severina = 0 # odsyła do petroniusa
default quest_recruitahunter_spokento_petronius = 0 # dwa punkty do cassia
default quest_recruitahunter_spokento_iuno = 0

default quest_recruitahunter_spokento_glaucia = 0 # cassia
default quest_recruitahunter_spokento_helvius = 0 # cassia

default quest_recruitahunter_spokento_shoshi = 0 # shoshi_notmatched
default quest_recruitahunter_spokento_shoshi_recruited = 0

default quest_recruitahunter = 0 # "Recruit a Hunter"
default quest_recruitahunter_noonerecruited = 0 #
default quest_recruitahunter_erastosrecruited = 0 #
default quest_recruitahunter_cassiarecruited = 0 #
default quest_recruitahunter_description00 = "{color=#f6d6bd}Dalit{/color} from {color=#f6d6bd}Pelt{/color} will pay me 5 dragon bones for learning more about two questionable candidates who wish to be hunters - {color=#f6d6bd}Erastos{/color} from {color=#f6d6bd}Howler’s Dell{/color} and {color=#f6d6bd}Cassia{/color} from {color=#f6d6bd}Gale Rocks{/color}."
default quest_recruitahunter_description01 = 0 # "I received my reward."
default quest_recruitahunter_description02 = 0 # "{color=#f6d6bd}Dalit{/color} rejected both hunters. I received my reward, but she would like to know if I meet a trustworthy candidate."
default quest_recruitahunter_description03 = 0 # "I told {color=#f6d6bd}Dalit{/color} what I learned about {color=#f6d6bd}Shoshi{/color}."

default quest_runaway = 0 # "The Runaway"
default quest_runaway00 = "A man has left {color=#f6d6bd}Glaucia’s{/color} band. If I were to help her find him, she could punish him for betraying her trust."
default quest_runaway_description01 = 0 # "I received my reward."
default quest_runaway_description02 = 0 # "I decided to lie to her, sacrificing my reward."

default quest_reachthepaganvillage = 0 # "The Hidden Village"
default quest_reachthepaganvillage_description00 = "Apparently there’s another group of people somewhere in the North, though rarely mentioned by anyone - {color=#f6d6bd}The Tribe of The Green Mountain{/color}. Maybe they have a settlement somewhere away from the main roads."
default quest_reachthepaganvillage_description00b = 0 #"I’ve heard a rumor that {color=#f6d6bd}Asterion{/color} has kept in touch with them."
default quest_reachthepaganvillage_description01 = 0 #"To reach the village, I have to follow the eastern road until I reach the stone bridge, then turn east and move alongside the northern shore of the brook."
default quest_reachthepaganvillage_description02 = 0 #"According to the old sailor, I should bring them some sort of a gift - maybe a decent blade, or a sack of spices."
default quest_reachthepaganvillage_description08 = 0 #"If I want to see the leaders of the tribe, I need to bring them a worthy gift."
default quest_reachthepaganvillage_description09 = "" # "According to the guard, it could be “something of great value, and what’s difficult to find. A sharp blade. A cask full of golden liquid. Spices from another land.”" OR "According to the guard, it could be “rare t’ing to us. A good blade. Good drink. Spices.”"
default quest_reachthepaganvillage10 = 0 #"I’ve reached The Tribe."

default quest_pensformonastery_forgiven = 0
default quest_pensformonastery = 0 # "Quills for The Monastery"
default quest_pensformonastery_description00 = "{color=#f6d6bd}Aeli{/color}, the monk from {color=#f6d6bd}the monastery{/color}, has asked me to travel far to the east, to the enchantress known as {color=#f6d6bd}Eudocia{/color}, then ask her for a set of magical pens that she was working on for his order. Once I get them, I need to bring them back."
default quest_pensformonastery_description01 = 0 # "Eudocia gave me the quills."
default quest_pensformonastery_description02 = 0 # "I used the quills on the altar, feeding the mysterious tree with them. While it worked, they were completely destroyed in the process."
default quest_pensformonastery_description03 = 0 # "I’ve saved my skin with a lie."
default quest_pensformonastery_description04 = 0 # "I’ve delivered the pens to the monastery and collected my reward."
default quest_pensformonastery_description05 = 0 # "I’ve brought the news about the destroyed pens to the monastery."

default quest_ruins = 0 # "Ruined Village" #Thais chciała dać im nauczkę by wioski się zjednoczyły, zrobiła wypad / rajd na ich ziemię. Wioskowcy spróbowali podjąć szybkie kroki, by zreperować szkody, co sprowokowało the wrath of the herds. wioska upadła. CZYLI: najpierw mały rajd, potem inwazja, ale duże osłabienie.
default quest_ruins_description00 = "I’ve arrived at the ruins of a village that used to be set at the southern road. It may be important to figure out what happened here, and if it can ever be reinhabited."
default quest_ruins_insideclues01 = 0 # "The southern gate was destroyed by a massive force, most likely a troll or a powerful mage."
default quest_ruins_insideclues02 = 0 # "The nearby clearing was massive, large enough to provoke the wrath of the herds."
default quest_ruins_insideclues03 = 0 # "I found many marks left by large animal claws on various building entrances."
default quest_ruins_insideclues04 = 0 # "I found human bones gathered and chewed on by a pack of goblins. Now I know where the shells have disappeared to."
default quest_ruins_insideclues05 = 0 # "While the village used to be small, it was also unusually wealthy."
default quest_ruins_insideclues07 = 0 # "A wooden wagon and a set of tools were thrown into a river, all right next to each other."
default quest_ruins_insideclues08 = 0 # "I found a quince tree that was partially burnt by a torch."
default quest_ruins_insideclues09 = 0 # "Some humans chopped through the fence that surrounds the large pasture. Maybe to save a herd, maybe to steal it."

default quest_ruins_description01 = 0 # "I heard that the village was destroyed almost ten years ago."
default quest_ruins_calculateclues = 0
default quest_ruins_10yclue01 = 0 # "I heard that {color=#f6d6bd}Thais{/color} tried to start a pact that was meant to unite the local tribes, but it turned out to be a failure."
default quest_ruins_10yclue02 = 0 # "Newcomers arrived at {color=#f6d6bd}Pelt of the North{/color}."
default quest_ruins_10yclue03 = 0 # "{color=#f6d6bd}Elpis{/color} became the leader of the druids in {color=#f6d6bd}Howler’s Dell{/color}."
default quest_ruins_10yclue04 = 0 # "{color=#f6d6bd}Elpis{/color} told me to speak with her predecessor - the older druid who lives in the cave, south of {color=#f6d6bd}Howler’s Dell{/color}."
default quest_ruins_10yclue04p2 = 0 # "{color=#f6d6bd}The druid from the cave{/color} has confirmed that the village was pillaged by humans, then destroyed by monsters."
default quest_ruins_10yclue05 = 0 # "I heard that the trade between the villages has slowed down."
default quest_ruins_10yclue05p2 = 0 # "That’s also when the locals stopped caring about the shelter at the northern road."
default quest_ruins_10yclue06 = 0 # "{color=#f6d6bd}The Tribe of The Green Mountain{/color} cut off contact with other villages."
default quest_ruins_10yclue07 = 0 # "The people of {color=#f6d6bd}Creeks{/color} decided to refuse any sort of collaboration with {color=#f6d6bd}Thais{/color} because of {i}the things she did ten years ago{/i}."
default quest_ruins_10yclue08 = 0 # "{color=#f6d6bd}Eudocia{/color} left {color=#f6d6bd}Old Págos{/color}."
default quest_ruins_10yclue09 = 0 # "People stopped using the road leading through the heart of the forest."
default quest_ruins_10yclue10 = 0 # "The people of {color=#f6d6bd}Gale Rocks{/color} started neglecting their tunnel in the south."
default quest_ruins_10yclue11 = 0 # "{color=#f6d6bd}Glaucia{/color} became a bandit."
default quest_ruins_10yclue12 = 0 # "{color=#f6d6bd}Thyrsus{/color} left his teachers at {color=#f6d6bd}Howler’s Dell{/color}."
default quest_ruins_10yclue13 = 0 # "The people of {color=#f6d6bd}White Marshes{/color} started to isolate themselves."

default quest_ruins_treepicture = 0 # ""
default quest_ruins_insideclues10 = 0 # "I experienced mysterious symptoms of an illness while exploring the village, and the scavenger felt the same thing."
default quest_ruins_insideclues06 = 0 # "I’ve proven that the local fields have been turned barren by a curse."
default quest_ruins_description_truestory = 0 # "{color=#f6d6bd}SOMEONE{/color} blames the people of {color=#f6d6bd}Howler’s Dell{/color} for destroying {color=#f6d6bd}Steep House{/color}. According to their story, {color=#f6d6bd}Thais{/color}tried to make an example out of these villagers when they refused to join her covenant."
default quest_ruins_description_creeksparticipated = 0 # "{color=#f6d6bd}Elah{/color} admitted that the people of {color=#f6d6bd}Creeks{/color} were helping {color=#f6d6bd}Thais{/color} during the raid."
default quest_ruins_description_peltparticipated = 0 # "{color=#f6d6bd}Pelt’s{/color} innkeep admitted that his crew was helping {color=#f6d6bd}Thais{/color} during the raid."
default quest_ruins_description_origins = 0 # "The village was located by the people of {color=#f6d6bd}Howler’s Dell{/color}, and was a part of their tribe."
default quest_ruins_description_glauciasperspective = 0 # "{color=#f6d6bd}Glaucia{/color} claims that {color=#f6d6bd}Steep House{/color} was getting very rich because of its location, causing great anger of {color=#f6d6bd}Howler’s{/color}, which demanded a share of the village’s income - even though they were a part of the same tribe."
default quest_ruinsconflictopen = 0
default quest_ruins_choice = 0 # "lefttocity" "forgotten" "thais_defeated" "thais_won" "thais_alliance" "thais_alliance_fail"

default quest_sleepinggiant = 0 # "Sleeping Giant"
default quest_sleepinggiant_description00 = 0 #"I have reasons to believe that the huge statue at the foot of the mountain is tied to a ritual of sorts."
default quest_sleepinggiant_description00a = 0 #"Apparently, the statue hides a “map” of {color=#f6d6bd}High Island{/color}."
default quest_sleepinggiant_description01 = 0 #"My amulets have found magic in the area."
default quest_sleepinggiant_description02 = 0 #"I won’t be able to get anywhere without a proper prayer, or a spell."
default quest_sleepinggiant_description03 = 0 #"I’ve managed to awaken the statue, but I still need to spend time at it to memorize its secrets."
default quest_sleepinggiant_description04 = 0 #"I’ve recorded the pattern of “stars” that I found at the statue."
default quest_sleepinggiant_description05 = 0 #"I’ve decided to stay truthtfull to my faith. I won’t pray at the statue."

default quest_studyingthegolems = 0 # "Studying the Golems"
default quest_studyingthegolems_description00 = "{color=#f6d6bd}Aeli{/color} from {color=#f6d6bd}the monastery{/color} has asked me to look into the rumors of “dangerous golems” that were spotted in the possession of {color=#f6d6bd}Eudocia{/color}. She’s an enchantress who lives near the eastern road. The more details I learn, the higher my reward will be."
default quest_studyingthegolems_description01 = 0 #"I asked {color=#f6d6bd}Eudocia{/color} a few things about the golems. Maybe I could learn more if I take a closer look at the sentinels on my own."
default quest_studyingthegolems_description02 = 0 #"The monk has advised me to look for guidance about fighting off the golems. Maybe an experienced fighter could share their knowledge with me."
default quest_studyingthegolems_description03 = 0 #"I had a chance to take a closer look at one of the golems."
default quest_studyingthegolems_description03b = 0 #"I’ve learned that at least some of the golems are covered with inscriptions, possibly enhancing their powers."
default quest_studyingthegolems_description04 = 0 #"According to"# [dalit_name],
default quest_studyingthegolems_description04b = 0 #"golems get confused when they move away from their owners. Trying to crush their shells won’t do much good, but if properly trapped, their limbs can be pulled apart, weakening the magic that keeps them in one piece."
default quest_studyingthegolems_description06 = 0 #"I can return to the monastery and ask for a {i}secret{/i} whenever I want."
default quest_studyingthegolems_description07 = 0 #"I collected my reward."

default quest_creekssupport = 0 #"Support of Creeks"
default quest_creekssupport_description00 = "When possible, I should speak with {color=#f6d6bd}Elah{/color} during evening hours and participate in the parting rites. It’s an opportunity to make my case for the village to collaborate with {color=#f6d6bd}Hovlavan{/color}, so I should make sure the locals have good reasons to trust me."
default quest_creekssupport_description01 = 0 # "I gained the support of the tribe."
default quest_creekssupport_description04 = 0 # "The tribe is not going to collaborate with the city anytime soon."
default quest_creekssupport_description05 = 0 # "I don’t think the tribe will ever agree to collaborate with the city."

default quest_galerockssupport = 0 # "The Support of Gale Rocks"
default quest_galerockssupport_description00 = "I will be allowed to speak with the council of {color=#f6d6bd}Gale Rocks{/color} and state my case why they should cut their ties with {color=#f6d6bd}Glaucia{/color}. Considering that many of the bandits share blood with the villagers and I will have only one chance to convince them, I need to be sure I have good arguments on my side."
default quest_galerockssupport_description00a = "Once I’m prepared, I should speak with {color=#f6d6bd}Severina{/color} some time before nightfall. The session may take even a few hours."
default quest_galerockssupport_description01 = 0 #"The villagers agreed to cut their ties with the bandits. The merchants and officials now have an open way to negotiate the terms of the new treaty."
default quest_galerockssupport_description02 = 0 #"The villagers are now convinced to take an even stronger stance on the side of the bandits. It’s going to be bad news for the city merchants."

default quest_glauciasupport = 0 # "The Support of Bandits"
default quest_glauciasupport_description00 = 0 # "I could sabotage my meeting with {color=#f6d6bd}Gale Rocks’{/color} council. Securing {color=#f6d6bd}Glaucia’s{/color} future may hinder the city’s efforts, but will help me learn more about the peninsula."
default quest_glauciasupport_description00alt = 0 #"I could sabotage my meeting with {color=#f6d6bd}Gale Rocks’{/color} council. Securing {color=#f6d6bd}Glaucia’s{/color} future may hinder the city’s efforts, but would keep me safer in the future seasons... If I care for it."
default quest_glauciasupport_description00a = "Doing obviously bad job during the meeting would make the council less convinced in their judgment, so I should at least try to tell them something worth listening to."
default quest_glauciasupport_description01 = 0 # "I told her about my success, and she was grateful - in her own way."
default quest_glauciasupport_description02 = 0 # "I lied to her. Let’s hope she won’t learn the truth while I’m around."
default quest_glauciasupport_description03 = 0 # "I told her the truth, and she was far from happy."

default quest_howlerssupport = 0 #"Support of Howler’s Dell"
default quest_howlerssupport_description00 = "{color=#f6d6bd}Thais{/color}, the mayor of {color=#f6d6bd}Howler’s Dell{/color}, is willing to discuss trade and tax deals with {color=#f6d6bd}Hovlavan{/color}. In exchange for helping her neighbors, I’ll receive a letter with her offer."
default quest_howlerssupport_description01 = 0 # "{color=#f6d6bd}Thais{/color} wants me to spy for her."
default quest_howlerssupport_description05 = 0 # "I received my reward."
default quest_howlerssupport_description06 = 0 # "{color=#f6d6bd}Thais{/color} distrusts me. I won’t be able to negotiate with her."

default quest_greenmountainsupport_reward = 0 #"horn"/"support"/"friendship"
default quest_greenmountainsupport = 0 #"Support of The Tribe of The Green Mountain"
default quest_greenmountainsupport_description00 = "The leaders of the Tribe agreed to speak with the city’s messengers, even if only to set up clear boundaries around their region."

default quest_monasterysupport = 0 #"Support of Monks"
default quest_monasterysupport_description00 = "If I manage to convince the monks to trust me, they’ll agree to introduce me to their {color=#f6d6bd}prelate{/color}. It’s an opportunity to talk with them about tightening their ties to {color=#f6d6bd}Hovlavan{/color}."
default quest_monasterysupport_description01 = 0 # "I spoke with {color=#f6d6bd}the prelate{/color} and promised them to portray the monastery’s goals and zeal in front of the officials."
default quest_monasterysupport_description01lie = 0 # "I spoke with {color=#f6d6bd}the prelate{/color} and lied to them about portraying the monastery’s goals and zeal in front of the officials."
default quest_monasterysupport_description02 = 0 # "I refused to help the monks, possibly separating them from the city officials for good."
default quest_monasterysupport_description03 = 0 # "{color=#f6d6bd}The prelate{/color} has seen through my lies. It’s possible I separated the monastery from the city for good."

default quest_oldpagossupport = 0 #"Support of Old Págos"
default quest_oldpagossupport_description00 = "I’ve managed to take care of the plague that had fallen upon the villagers, in exchange asking them to consider joining {color=#f6d6bd}Hovlavan{/color}. The merchant guild has an open gate to begin its negotiations."

default quest_swampaltar = 0 # "Swamp Altar"
default quest_swampaltar_description00 = "I found an {color=#f6d6bd}altar in the swamps{/color} which seems to be somehow connected to the tree roots that surround it. There may be a way to get some sort of response from it."
default quest_swampaltar_description01 = 0 #The tree reacts when I “feed” it with human blood.
default quest_swampaltar_description02 = 0 #"The altar is responding to magical powers. I can use it as a sacrifice, but it will temporarily make me unable to use any more spells."
default quest_swampaltar_description03 = 0 #"The tree can “drain” magical power from various items, which results in their destruction."
default quest_swampaltar_description04 = 0 #"The tree has answered to all this sacrifice with a strange, bone-like fruit. I think it won’t grow anymore in the near future."

default quest_thyrsusgift = 0 # "Thyrsus’ Wand"
default quest_thyrsusgift_description00 = "{color=#f6d6bd}Thyrsus{/color} from {color=#f6d6bd}the peat field{/color} wants me to bring him back his old wand. Maybe {color=#f6d6bd}Akakios{/color} in {color=#f6d6bd}Howler’s Dell{/color} will know how to get it."
define quest_thyrsusgift_description_faildescription = "{color=#f6d6bd}Thyrsus{/color} no longer needs my assistance."
define quest_thyrsusgift_description_successdescription = "I received my payment."
default quest_thyrsusgift_dayofsuccess = 0
# default quest_thyrsusgift_dayof = 0
default quest_thyrsusgift_description01 = 0 #"{color=#f6d6bd}Akakios{/color} told me I should speak with {color=#f6d6bd}Elpis{/color}, the druidess."
default quest_thyrsusgift_description02 = 0 #"{color=#f6d6bd}Elpis{/color} wants me to ask for “a mundane work” at {color=#f6d6bd}Howler’s{/color} sometime in the morning. {i}Someone{/i} is going to take me to the forest garden, so I should be of a healthy shell."
default quest_thyrsusgift_description03 = 0 #"I received {i}the gift{/i}."
default quest_thyrsusgift_description04 = 0 #""
default quest_thyrsusgift_description05 = 0 #""

###################### People for the journal
default description_aegidia00 = "An archeress from {color=#f6d6bd}Howler’s Dell{/color} who lives by herself in {color=#f6d6bd}the old fishing hamlet{/color}."
default description_aegidia01 = 0 # "An adopted daughter of {color=#f6d6bd}Thais{/color} and {color=#f6d6bd}Eryx{/color}. She despises her mother."
default description_aegidia02 = 0 # "According to {color=#f6d6bd}Thais{/color}, she died during an accident that involved {color=#f6d6bd}Asterion{/color}."
default description_aegidia03 = 0 # "Her mother disowned her once she had learned of Aegidia’s deception."
default description_aegidia04 = 0 # "According to {color=#f6d6bd}Thais{/color}, she “listened to people, was ready to help them and to cry with them.”"
default description_aegidia05 = 0 # "She owes me a favor."
default description_aegidia06 = 0 # "She tries to learn how to catch the small fish from the stream."

default description_akakios00 = "A trader living in {color=#f6d6bd}Howler’s Dell{/color}."
default description_akakios01 = 0 # "He’s the treasurer of the village, responsible for distributing the supplies among the denizens, and for exchanging what’s left with outsiders."
default description_akakios02 = 0 # "According to"
default description_akakios02a = ", he won’t give much to strangers for furs and animal trophies."
default description_akakios03 = 0 # "The rules of his village forced him to tell me that he “was” a wife beater. His daughter has a new father now."
default description_akakios04 = 0 # "According to {color=#f6d6bd}Ilan{/color}, he doesn’t care about chit-chat and gets straight to the point."
default description_akakios05 = 0 # "According to {color=#f6d6bd}Ilan{/color}, he’s “all about trade, not much for idle talk.”"
default description_akakios06 = 0 # ""

default description_asterion00 = "The previous roadwarden. He disappeared a couple of months ago under unknown circumstances. The merchants would like to find out what happened to him. Short, but broad-shouldered. Red hair and beard. Pale. Wears mail. Rides on a four-legged lizard."
default description_asterion01 = 0 #According to {color=#f6d6bd}Tulia{/color}, he was a bit of a recluse, constantly on the move, looking for work. Since he disappeared before the summer, he may already be dead. His kids live near {color=#f6d6bd}Hovlavan{/color}.
default description_asterion02 = 0 #According to #[iason_name]
default description_asterion02b = 0 #, {color=#f6d6bd}Asterion{/color} was meant to do something for the people of {color=#f6d6bd}White Marshes{/color} and disappeared soon after that. He and the innkeep have made some sort of deal, in which the latter invested - and lost - fifty dragons. He doesn’t think {color=#f6d6bd}Asterion{/color} has stolen them.
default description_asterion03 = 0 #According to#[iason_name]
default description_asterion03b = 0 #", {color=#f6d6bd}Asterion{/color} tried to stay impartial and didn’t tie himself to any village, so there’s a good chance that he’s already dead. It’s possible that someone knows exactly what happened to him, or even has set him up."
default description_asterion04 = 0 #"According to the scavenger I met in a ruined village in the South, people in the northern villages were asking him if he saw Asterion, but after a couple of weeks they dropped the topic completely."
default description_asterion05 = 0 #"According to the druid from the cave in the southwest, Asterion was planning to settle down in the peninsula and was hoping to make it a better place first."
default description_asterion06 = 0 #"According to {color=#f6d6bd}Eudocia{/color}, Asterion owns a green cloak, embroidered with black patterns representing a variety of leaves."
default description_asterion07 = 0 # "If {color=#f6d6bd}Thais{/color} is telling the truth, {color=#f6d6bd}Asterion{/color} was ready to face consequences of his wrongdoings."
default description_asterion08 = 0 # "I’ve heard a more detailed description of Asterion’s {color=#f6d6bd}saurian{/color}. It’s larger than a horse, dark green, though the edges of its limbs, tail, and eyebrows are red-and-orange."
default description_asterion09 = 0 # "According to monk {color=#f6d6bd}Aeli{/color}, {color=#f6d6bd}Asterion’s{/color} thigh was severely hurt by a hundred-legged worm."
default description_asterion10 = 0 # ""
default description_asterion11 = 0 # "{color=#f6d6bd}Foggy{/color} knows more about Asterion than she wants to admit, though if I want her to talk with me, I need to earn her trust first."
default description_asterion12 = 0 # "According to {color=#f6d6bd}Foggy{/color}, Asterion sold her a unique, magical cloak to purchase a boat."
default description_asterion13 = 0 # "According to {color=#f6d6bd}Elah{/color}, Asterion was a very confident and self-reliant person."
default description_asterion14 = 0 # "According to {color=#f6d6bd}Photios{/color}, Asterion was “useless”, for he refused to give a spirit rock to his daughter."
default description_asterion15 = 0 # "According to {color=#f6d6bd}Gaiane{/color}, Asterion is “a shell lost on its pat’ to nowhere, a soul torn by its dreams, a word spoken to no one.”"
default description_asterion16 = 0 # "As far as I understand, he was obsessed with some sort of treasure."

default description_dalit00 = "A huntress living in {color=#f6d6bd}Pelt of the North{/color}."
# default description_dalit00a = "Has red curly hair, wears a yellow gambeson."
default description_dalit01 = 0 #It looks like she could teach me quite a bit about the monsters that live in this peninsula.
default description_dalit02 = 0 #According to# [iason_name], she’s a master of the crossbow. He’s known her since she was a child.
default description_dalit02b = 0 #, she’s a master of the crossbow. He’s known her since she was a child.
default description_dalit03 = 0 #"According to {color=#f6d6bd}Ilan{/color}, she’s a playful girl who always looks for entertainment."
default description_dalit04 = 0 #"According to {color=#f6d6bd}Ilan{/color}, she loves to tell stories about the monsters she’s faced."
default description_dalit05 = 0 #"According to {color=#f6d6bd}Thyrsus{/color}, she’s an expert when it comes to fighting dangerous beasts."

default description_elah_efren00 = 0 #"The two brothers from {color=#f6d6bd}Creeks{/color} who speak with me the most. {color=#f6d6bd}Elah{/color} is a carpenter, {color=#f6d6bd}Efren{/color} is a hunter."
default description_elah_efren00alt = "The two men from {color=#f6d6bd}Creeks{/color}. {color=#f6d6bd}Elah{/color} is a carpenter, {color=#f6d6bd}Efren{/color} is a hunter."
default description_elah_efren01 = 0 # "According to [iason_name], #{color=#f6d6bd}Elah{/color} tries to carry a big burden, being one of the very few people in his tribe willing to plan for the future."
default description_elah_efren05 = 0 # "{color=#f6d6bd}Elah{/color} admitted to participating in the raid on {color=#f6d6bd}Steep House{/color}."
default description_elah_efren06 = 0 # "According to [iason_name], #{color=#f6d6bd}Efren{/color} is more of a pathfinder than a fighter, and was invited to stay at {color=#f6d6bd}Pelt of the North{/color} as a ranger."

default description_eudocia00 = "An enchantress living in a lonely house near {color=#f6d6bd}the eastern road{/color}."
default description_eudocia01 = 0 #According to# [iason_name], she’s insane and lives alone, {i}skinny and dirty{/i}, protected by her golems.
default description_eudocia01b = 0 #, she’s insane and lives alone, {i}skinny and dirty{/i}, protected by her golems. She “never cries and never smiles”.
default description_eudocia02 = 0 #Eudocia doesn’t allow anyone in her house while she works. I should ask her to meet me in the early morning, or a few hours before dusk.
default description_eudocia03 = 0 #"{color=#f6d6bd}The monks{/color} distrust her and are convinced she may try to harm their order."
default description_eudocia04 = 0 #"According to {color=#f6d6bd}Aeli{/color}, “her talent knows no equal, yet she’s a spider queen in the center of the web. She’s the only shell she cares about, and uses those who reach out to her. Keep your guard up.”"
default description_eudocia05 = 0 #"According to {color=#f6d6bd}Foggy{/color}, she doesn’t look for friendships, and may already be crazy."
default description_eudocia06 = 0 #"Her golems are unusual, as if she’s designed them without relying on any inventions from previous generations."
default description_eudocia07 = 0 #"According to {color=#f6d6bd}Photios{/color}, she’s “tall, with cold eyes. For the few days she was around, she kept to herself. People say she’s a witch, and a mad one at that.”"
default description_eudocia08 = 0 #"According to herself, her magical talents manifested when she was a child, and she doesn’t understand them."
default description_eudocia09 = 0 #"According to {color=#f6d6bd}Quintus{/color}, “she was a quiet kid, but a smart one. Never tried to steal my milk.”"

default description_foggy00 = "She’s the owner of {color=#f6d6bd}Foggy Lake{/color}, a tavern set on the northern road."
default description_foggy01 = 0 #"According to"# [iason_name], she often organizes large feasts and likes to drink a lot."
default description_foggy01b = 0 #", she often organizes large feasts and likes to drink a lot. She appreciates those who are promising allies in trade."
default description_foggy02 = 0 #"According to {color=#f6d6bd}Eudocia{/color}, her place is cheerful and “not as boring as {color=#f6d6bd}Pelt of the North{/color}.”
default description_foggy03 = 0 #"She has her own set of alchemical tools, necessary to brew ciders and distill hard drinks."
default description_foggy04 = 0 #"Apparently she has a great interest in animal trophies, especially those gathered from dangerous creatures."
default description_foggy05 = 0 #"She has a great interest in animal trophies, especially those gathered from dangerous creatures, weapons, and hard drinks."
default description_foggy06 = 0 #"According to {color=#f6d6bd}Old Hava{/color}, {color=#f6d6bd}Foggy{/color} is essential to sustain the trade between {color=#f6d6bd}Creeks{/color} and other settlements."
default description_foggy07 = 0 #"According to {color=#f6d6bd}Aeli{/color}, {color=#f6d6bd}Foggy{/color} cares about the northern paths."

default description_glaucia00 = "The leader of the local band of highwaymen."
default description_glaucia01 = 0 #According to# [iason_name]
default description_glaucia01b = 0 #, she’s tanned, wrinkled by age. Charismatic, {i}strong{/i}, {i}scary{/i}. He heard that she was born in one of the northern villages. He claims that she wanted to move into Pelt of the North.
default description_glaucia01c = 0 # works
default description_glaucia02 = 0 #"I heard that she was raised by her family in the {color=#f6d6bd}Gale Rocks{/color} village."
default description_glaucia03 = 0 #"According to {color=#f6d6bd}the druid from the cave{/color}, Glaucia listens only to force and looks for ways to display her own superiority."
default description_glaucia04 = 0 #"{color=#f6d6bd}Eudocia{/color} is afraid of her. “She can’t be reasoned with - if she doesn’t feel threatened, one can only ask her for mercy.”" # eudocia_about_bandits_gray ALSO WORKS
default description_glaucia05 = 0 #"According TO PELT OF THE NORTH’s {color=#f6d6bd}innkeep{/color}, Glaucia is more favorable toward those who don’t show her their fear."
default description_glaucia06 = 0 #"I’ve learned that she plans to take down the necromancers from {color=#f6d6bd}White Marshes{/color}, who have turned the deceased members of her family into undead."
default description_glaucia07 = 0 #"{color=#f6d6bd}Quintus{/color}, the gatekeeper, claims that she’s the one who forced him to stay on his post."
default description_glaucia08 = 0 #"According to {color=#f6d6bd}Foggy{/color}, she became the leader of the local bandits after they’ve faced some sort of a tragedy."
default description_glaucia09 = 0 #"According to the bandit I met in the heart of the woods, she’s “pushing things too far, too much.” He left her “before we turn into murderers.”"
default description_glaucia10 = 0 #"According to {color=#f6d6bd}Old Hava{/color}, every bandit leader will fall to their own desires, bringing only more suffering onto others."
default description_glaucia11 = 0 #"According to {color=#f6d6bd}Elah{/color}, she was involved with {color=#f6d6bd}Asterion’s{/color} disappearance."
default description_glaucia12 = 0 #"I’ve learned that many years ago she found a husband in the south - in the village of {color=#f6d6bd}Steep House{/color}."
default description_glaucia13 = 0 #"Her parents are losing her wits, as well as memories."
default description_glaucia14 = 0 #"The gate guard from {color=#f6d6bd}Gale Rocks{/color} seemed surprised when I mentioned the bandits. He claimed that {color=#f6d6bd}Glaucia{/color} and her band are but a group of treasure hunters and traders."
default description_glaucia15 = 0 #"She seems to be fine with the local roads growing more dangerous."
default description_glaucia16 = 0 #"She feels deep hatred toward the undead of {color=#f6d6bd}White Marshes{/color}."
default description_glaucia17 = 0 #"Once the undead are gone, she will likely use her band to wound the people of {color=#f6d6bd}Howler’s Dell{/color}."
default description_glaucia18 = 0 #"She’s a survivor of the massacre in {color=#f6d6bd}Steep House{/color}."
default description_glaucia19 = 0 #"According to {color=#f6d6bd}the runaway bandit{/color}, “for as long as she’s backed by the council of {color=#f6d6bd}Gale Rocks{/color}, she has a full stomach and warm togs. She won’t hesitate to kill you if she feels threatened by you.”"
default description_glaucia20 = 0 #"According to {color=#f6d6bd}the runaway bandit{/color}, “her gratitude goes only as far as it takes to spare one’s life. She thinks she’s saving the innocent and punishing the monsters, so in her view it’s {i}us{/i} who should be grateful to {i}her{/i}.”"
default description_glaucia21 = 0 #"According to {color=#f6d6bd}Thyrsus{/color}, she’s a bandit leader who puts obedience above all else."

default description_iason00 = "A man in charge of {color=#f6d6bd}Pelt of the North{/color}."
default description_iason01 = 0 #According to {color=#f6d6bd}Tulia{/color}, he prefers to stick to trade, doesn’t like to waste time on jokes and empty gestures.
default description_iason02 = 0 #The leader of a team of big-game hunters.
default description_iason02a = 0 #"He arrived here more than ten years ago."
default description_iason03 = 0 #His purple skin combined with the clean, city accent implies that he might have been born into slavery.
default description_iason04 = 0 #According to# [dalit_name]
default description_iason04b = 0 #, he likes to give strangers small tasks to find out if they’re useful. And hates thieves.
default description_iason05 = 0 #"According to {color=#f6d6bd}Eudocia{/color}, he’s “stiff like a broom.”"
default description_iason06 = 0 #"He was planning to purchase the {color=#f6d6bd}Foggy Lake{/color} tavern."
default description_iason07 = 0 #"According to {color=#f6d6bd}Ilan{/color}, he was in need of hard drinks and healing potions."
default description_iason08 = 0 #"He was willing to keep me in a long lie for his own gain."
default description_iason10 = 0 #"He admitted that his crew was helping {color=#f6d6bd}Thais{/color} during the raid on {color=#f6d6bd}Steep House{/color}."

default description_orentius00 = 0 #"The priest living in {color=#f6d6bd}White Marshes{/color}, the leader of the local fellowship of The Wright. Known for his necromantic practices."
default description_orentius01 = 0 #"I heard that he won’t meet with people who are not trusted in his fellowship."
default description_orentius02 = 0 #"According to {color=#f6d6bd}Thais{/color}, he used to have no interest in being a leader."
default description_orentius03 = 0 #"he’s “greater in thought than he is in heart.”"
default description_orentius04 = 0 #"According to {color=#f6d6bd}Tertia{/color}, he’s {i}a pagan blinded by his wicked wits, rotten to the core{/i}."
default description_orentius05 = 0 #"I heard that he never leaves his house."
default description_orentius06 = 0 #"According to {color=#f6d6bd}Foggy{/color}: “A quiet man, but preaches like a zealot. Always looks like he’s on the verge of crying.”"
default description_orentius07 = 0 #"According to {color=#f6d6bd}Thyrsus{/color}, he used to eagerly oppose pagan magic, seeing it as disgusting in Wright’s eyes."
default description_orentius08 = 0 #"According to {color=#f6d6bd}Thyrsus{/color}: “I was never close with him. When I left the village to learn spells, many years ago, he was ba a priest of ours. Once I returned, he came forward like a prophet, shouting with zeal, warning the tribe needs to {i}prepare{/i} itself, for whatever. When his followers brough first dead shells to the village, they were still in minority, ba were ready to fight for him. We could either throw them all outside f’our walls, or... Empty disputes, empty threats. You can tell how it all ended.”"
default description_orentius09 = 0 #"According to {color=#f6d6bd}Thyrsus{/color}, he may be more eager to listen to me if I have {color=#f6d6bd}Helvius’{/color} trust on my side."
default description_orentius10 = 0 #"According to {color=#f6d6bd}Aeli{/color}, he’s the real leader of {color=#f6d6bd}White Marshes{/color}, and it’s possible that he kidnaps people from the woods. He’s responsible for raising the undead."
default description_orentius11 = 0 #"According to {color=#f6d6bd}Valens{/color}, he “always asks to be heard”."

default description_quintus00 = "The gatekeeper born and raised in {color=#f6d6bd}Old Págos{/color}."
default description_quintus01 = 0 #"He now takes care of the western gate that leads to the heart of the forest."
default description_quintus02 = 0 # # According to #[iason_name]
default description_quintus02b = ", he drinks quite a lot and has been training with the inn’s team of hunters."
default description_quintus03 = 0 #"According to {color=#f6d6bd}Aeli{/color}: “He’s a brute and an idiot, can’t understand jokes, can’t stand {i}weaklings{/i}. If thou ever meet him, just smile and let him speak as much as he needs to shut up.”"
default description_quintus04 = 0 #"He has a crossbow, but claims to be bad at using it."
default description_quintus05 = 0 #"For now, he hides at {color=#f6d6bd}Pelt of the North{/color}."
default description_quintus06 = 0 #"According to {color=#f6d6bd}Tertia{/color}, “he may be not of the sharpest wits, but he’s loyal to his duty and returns kindness with kindness, like we all should.”"
default description_quintus07 = 0 #"According to {color=#f6d6bd}Dalit{/color}, he’s a bit dumb."

default description_pyrrhos00 = "I met him {color=#f6d6bd}in the ruined village{/color} at the southern road."
default description_pyrrhos01 = 0 #"He calls himself a drifter and a trader, and isn’t afraid of some more dangerous tasks. He claims that he came here by ship, looking for dragon bones."
default description_pyrrhos02 = 0 #"He claims that he was healed by powerful magic in the local monastery."
default description_pyrrhos03 = 0 #"I’ve helped him get to {color=#f6d6bd}Howler’s Dell{/color}." / "I’ve helped him get to {color=#f6d6bd}Pelt{/color}."
default description_pyrrhos04 = 0 #"According to {color=#f6d6bd}Thais{/color}, she doesn’t like his company. “The farther away he stays from here, the better.”"
default description_pyrrhos06 = 0 #"He’s no longer in the ruins, even though he left behind some of his stuff. He was probably finished off by the nearby goblin camp."

default description_thais_pcopinion = 0
default description_thais00 = "{color=#f6d6bd}The mayor of Howler’s Dell{/color}. A rich woman that represents her village when it comes to trade and negotiations."
default description_thais01 = 0 #"{color=#f6d6bd}Foggy{/color} seems to be afraid of her, and encouraged me to “laugh at her jokes”."
default description_thais02 = 0 #"According to {color=#f6d6bd}Aegidia{/color}, {color=#f6d6bd}Elpis{/color} describes {color=#f6d6bd}Thais{/color} as a soul who hates to be seen as a weakling."
default description_thais02a = 0 # "According to {color=#f6d6bd}Aegidia{/color}, she’s getting weaker with every year, struggling with a mysterious illness."
default description_thais03 = 0 #"According to {color=#f6d6bd}the scavenger{/color}, she’s a lively soul who enjoys games and jokes. “She’s short, and her blond hair is straight and long. She wears dresses and rouges her cheeks like a merchant.”"
default description_thais03b = "" #She hates being asked about the origins of her wealth."
default description_thais04 = 0 #" doesn’t like her and admits that “she may be frivolous, but she isn’t stupid.” According to him, she was born into wealth."
default description_thais05 = 0 #"I heard that she has tried to start a pact that was meant to unite the villages of the North, but was unable to make her neighbors a tempting enough offer."
default description_thais06 = 0 #"{color=#f6d6bd}The monks{/color} blame her for destroying the southern village."
default description_thais07 = 0 #"I met people in the west who called her a “fake, smiling rat.”"
default description_thais08 = 0 #"{color=#f6d6bd}Elah{/color} calls her a “tyrant.”"
default description_thais09 = 0 #"I was advised to have the druids on my side if I were to confront her."
default description_thais10 = 0 #"According to {color=#f6d6bd}Elpis{/color}: “Her parents were adventurers, they stood with us after a few grand journeys, carrying many treasures en sacks of dragon rings. They hoped to give her a life of comfort, without bloodshed. When others dug in soil or trained with spears, they taught her to count en read, then sent her to {color=#f6d6bd}Hovlavan{/color}, used their ties to let her into the guild. But the war disturbed her learning, she had to return, but told us she was to help us push against the Southerners, if we trust her. En she did. With poison en betrayal, aye. But saved all of us.”"
default description_thais11 = 0 # "According to {color=#f6d6bd}Tertia{/color}, “her laughter is as hollow as her soul.”"

default description_tertia00 = 0 #"Whenever I’m there, I speak with {color=#f6d6bd}Tertia{/color}, a fighter who, despite her age, represents the council."
default description_tertia01 = 0 #"According to"
default description_tertia01a = ", {color=#f6d6bd}Tertia{/color} is especially talented when it comes to spears and was planning to become an armed monk."
default description_tertia02 = 0 #"REMOVED? According to {color=#f6d6bd}Tertia{/color}, they used to be friends, but {color=#f6d6bd}Tertia{/color} kept getting more strict the closer she got to the monks, while {color=#f6d6bd}the enchantress{/color} was unwilling to trust them."
default description_tertia03 = 0 #"According to {color=#f6d6bd}Eudocia{/color}, it’s easier to convince {color=#f6d6bd}Tertia{/color} with a winged hourglass on one’s neck."

default description_thyrsus00 = "A warlock and the caretaker of the peat fields."
default description_thyrsus00a = "" #" A capable mage specialized in controlling plants."
default description_thyrsus00b = "" #" A herbalist willing to sell useful balms and powders."
default description_thyrsus01 = 0 #"According to the patrol I encountered at the old forest garden, I shouldn’t “bother him long. He’s of a cold soul.”"
default description_thyrsus02 = 0 #"According to the people of {color=#f6d6bd}Gale Rocks{/color}: “He just listens to what we need, tells his price, and makes us go, he does.”"
default description_thyrsus03 = 0 #"According to {color=#f6d6bd}Glaucia{/color}, he has “a soul as firm as a shield. No threat nor begging will move him an inch.”"
default description_thyrsus04 = 0 #"He was taught his unusual magic by the druids of {color=#f6d6bd}Howler’s Dell{/color}."
default description_thyrsus04a = 0 #"He left the village when he realized that he was seen by everyone as an outsider."
default description_thyrsus05 = 0 #"He seems to be bothered by the undead of {color=#f6d6bd}White Marshes{/color}."
default description_thyrsus06 = 0 #"He got into an argument with his tribe over the security of his family."

default description_tulia00 = "One of the last soldiers left in the peninsula. She is stationed at the military camp in the South."
default description_tulia01 = 0 #She plans to return to {color=#f6d6bd}Hovlavan{/color} in the near future.
default description_tulia02 = 0 #She didn’t expect to become a lieutenant and most members of her squad are already dead.
default description_tulia03 = 0 #According to#[iason_name], she’s more efficient when she has someone to order her around.
default description_tulia03b = 0 #, she’s more efficient when she has someone to order her around.
default description_tulia04 = 0 #"Her squad was meant to find a fitting place for a new outpost."
default description_tulia05 = 0 #"It seems like {color=#f6d6bd}Glaucia{/color} has been collaborating with {color=#f6d6bd}Tulia{/color} in the past."

######### GROUPS from the journal

default description_bandits00 = "A group responsible for robbing travelers and settlements in the peninsula."
default description_bandits01 = 0 # "According to {color=#f6d6bd}Foggy{/color}, the highwaymen sometimes eat at her place, but they don’t bother them. Seems like they’ve made a pact."
default description_bandits02 = 0 # "According to {color=#f6d6bd}Elah{/color}, all of them were born in the local villages."
default description_bandits03 = 0 # "According to {color=#f6d6bd}Eudocia{/color}, they may stay at an old lumberjack camp, though she doesn’t know where it is."
default description_bandits04 = 0 # "The gate guard from {color=#f6d6bd}Gale Rocks{/color} seemed surprised when I mentioned the bandits. He claimed that {color=#f6d6bd}Glaucia{/color} and her band are but a group of treasure hunters and traders."
default description_bandits05 = 0 # "According to {color=#f6d6bd}the druid from the cave{/color}, {color=#f6d6bd}Asterion{/color} was planning to get rid of the bandits."
default description_bandits06 = 0 # "According to {color=#f6d6bd}Glaucia{/color}, every member of her band has been {i}wronged by this land{/i}."
default description_bandits07 = 0 # "According to {color=#f6d6bd}Thyrsus{/color}, they don’t bother his hut, but in recent years pillaged {color=#f6d6bd}White Marshes{/color} a few times."
default description_bandits08 = 0 # ""

# default description_greenmountaintribe00 = "Apparently there’s another group of people somewhere in the North, though rarely mentioned by anyone - {color=#f6d6bd}The Tribe of The Green Mountain{/color}. Maybe they have a settlement somewhere away from the main roads."
default description_greenmountaintribe01 = 0 # "To reach the village, I have to follow the eastern road until I reach the stone bridge, then turn east and move alongside the northern shore of the brook."
default description_greenmountaintribe02 = 0 # "I heard that the brook leading to this village is dangerous, filled with flesh-eating fish."
default description_greenmountaintribe03 = 0 # "The druid from the cave has told me that once I find this place, I should introduce myself as “a freedom seeker, a friend of the speakers of the forest,” and that I need to present myself with humbleness."
default description_greenmountaintribe04 = 0 # "This tribe doesn’t trust people who follow Wright’s teachings."
default description_greenmountaintribe05 = 0 # "According to {color=#f6d6bd}Thais’s{/color} deceased sister, they were “wearing animal faces.”"
default description_greenmountaintribe06 = 0 # "According to {color=#f6d6bd}Foggy{/color}, they cut their contacts with other villages almost ten years ago."
default description_greenmountaintribe07 = 0 # "Apparently they try to stay away from the cityfolk, afraid of persecutions from the hands of The United Church."
default description_greenmountaintribe08 = 0 # "The locals have made a pact with other villages that’s meant to keep The Tribe’s presence a secret."
default description_greenmountaintribe09 = 0 # "Apparently they forbade other villages to enter {color=#f6d6bd}High Island{/color}."
default description_greenmountaintribe10 = 0 # "According to what you’ve heard, The Tribe used to thrive on {color=#f6d6bd}High Island{/color}, but was thrown out from the original {color=#f6d6bd}Green Mountain{/color} - the volcano - by the corsairs of {color=#f6d6bd}Hovlavan{/color} when it refused to join the city."
default description_greenmountaintribe11 = 0 # "According to {color=#f6d6bd}Efren{/color}, The Tribe uses the Old Speech, and has a custom of giving gifts to whom it visits, as well as of receiving ones from those who visit them."
default description_greenmountaintribe12 = 0 # "According to {color=#f6d6bd}Severina{/color}, her village refuses to talk about them out of respect."
default description_greenmountaintribe13 = 0 # "According to {color=#f6d6bd}Aeli{/color}, “they will soon become little more than a rumor, then a legend. But not against their will - The Tribe has been torn away from its soul centuries ago, and now aims to be lost to the world.”"

default description_creeks01 = 0 # "A village of fishers, hunters, and woodcutters in the far North."
default description_creeks01a = 0 # "They plan to focus more on woodcutting and carpentry."
default description_creeks01b = 0 # "I’ve heard I may make a good first impression there by being “nice and clean.”"
default description_creeks02 = 0 # "I heard that the locals are lighthearted and eager to have fun, and appreciate those who approach them with a smile."
default description_creeks03 = 0 # "According to {color=#f6d6bd}Eudocia{/color}: “They plan to reclaim the road to the far south of the peninsula. Just smile a lot and they’ll let ye in.”"
default description_creeks04 = 0 # "According to [iason_name]:" "Simple, but honest people... They drink a fair bit, but you wouldn’t believe how much they eat. And not just groats, but meats. They have no druids around, but none would want to live with them. They are like a well without a bottom.”"
default description_creeks05 = 0 # "According to {color=#f6d6bd}Foggy{/color}, the village is still very young, and almost the entire generation of its original settlers was lost to the fogs."
default description_creeks06 = 0 # "I heard that {color=#f6d6bd}Old Hava{/color}, the farmer, doesn’t like being bothered and should be spoken to only when she allows it."
default description_creeks07 = 0 # "{color=#f6d6bd}Old Hava{/color} claims that her tribe lacks ability when it comes to trade, and is completely dependent on {color=#f6d6bd}Foggy{/color} and the safety of the road leading to her."
default description_creeks08 = 0 # "{color=#f6d6bd}Old Hava{/color} used to be an infamous highwaywoman. Some of the {i}mysterious{/i} disappearances that brought a bad name on the peninsula were tied to bounty hunters who were chasing after her."
default description_creeks09 = 0 # "{color=#f6d6bd}Elah{/color} admitted that the people of {color=#f6d6bd}Creeks{/color} were helping {color=#f6d6bd}Thais{/color} during the raid."
default description_creeks10 = 0 # "According to {color=#f6d6bd}Tertia{/color}, “they wouldn’t be great neighbors or friends. They drink a lot, hunt for sport, die often and give birth to many children. I wouldn’t rely on them.”"

default description_druids00 = "Each group of druids is different, but most of them are pagan mages who specialize in taming the wilderness."
default description_druids01 = 0 #I can find the local druids in their cave, near the large tree in the south-west corner of the peninsula, on the edge of the swamp.
default description_druids02 = 0 #"I can find the local druids in the village of {color=#f6d6bd}Howler’s Dell{/color}, on the western road."
default description_druids03 = 0 #According to# [iason_name], one of the hunters who lives in his inn shares a {i}past{/i} with the local druids.
default description_druids03b = 0 #, one of the hunters who lives in his inn shares a {i}past{/i} with the local druids.
default description_druids04a = 0 #"According to {color=#f6d6bd}Foggy{/color}: “It’s the same as it is with the priests of Unites, dear. You keep your eyes low, nod without a word, then let them go and do your own thing.”"
default description_druids04 = 0 #To show them due respect, one should be humble and penitent, respect their efforts and address them as {i}forest speakers{/i}.
default description_druids05 = 0 #According to one of the hunters from {color=#f6d6bd}Pelt{/color}, the local druids are not as interested in faith and rituals, as they are in protecting the villagers. They teach them how to respect the {i}laws of the forests{/i} and are ready to turn down anyone who dares to break their strict code.
default description_druids06 = 0 #"I heard that an elderly druid who lives in the cave in the southwest corner of the peninsula is a selfless man who considers the well-being of others to be his top priority."
default description_druids07 = 0 #"The leader of the druids from {color=#f6d6bd}Howler’s Dell{/color} is known as {color=#f6d6bd}Elpis{/color}, though she rarely uses this name."
default description_druids08 = 0 #"According to {color=#f6d6bd}Foggy{/color}, the large tree from the swamps is kept under their protection. It’s older than their ring, and it “eats their souls”."
default description_druids09 = 0 #According to {color=#f6d6bd}an old druid from the cave{/color}: “The forest guides us, en we share its wisdom with the tribes. We and they ought to stay humble, take from the land what is needed instead of what’s wanted. Ne because ‘tis something we {i}believe{/i} in, but because it protects us from the wrath of the herds. To stay safe, one {i}needs{/i} to know how to be patient, take restraint into their hearts. En to make the beasts listen to us, we keep the animals healthy, teaching them to ne approach our homes en travelers.”
default description_druids10 = 0 #"I told {color=#f6d6bd}Elpis{/color} about {color=#f6d6bd}Thais’{/color} betrayal."
default description_druids11 = 0 #"According to {color=#f6d6bd}Thyrsus{/color}, the locals are weak in pneuma."
default description_druids12 = 0 #"According to {color=#f6d6bd}the tall druid{/color}, his gathering doesn’t know that many spells useful for combat."

default description_galerocks01 = 0 # "A large fishing village near the northern shore."
default description_galerocks02 = 0 # "During sunny days, the locals go to the shores to hunt the fish and birds that live there. When it gets dark, they hide behind the walls, boiling water for salt."
default description_galerocks03 = 0 # "According to {color=#f6d6bd}the scavenger{/color}, the locals are unfriendly, but got more talkative once he helped them with a few tasks."
default description_galerocks04 = 0 # "I heard that the fishers from {color=#f6d6bd}Gale Rocks{/color} know how to move between the coastal rocks."
default description_galerocks05 = 0 # "According to {color=#f6d6bd}Foggy{/color}, harsh lives turned them into harsh people."
default description_galerocks06 = 0 # "According to {color=#f6d6bd}Aeli{/color}: “They are weak and angry, like a wolf beaten and kicked from a pup. Loud, ready to bite, but all it takes is for someone to raise their hand, then it jumps away, in whimpers.”"
default description_galerocks07 = 0 # "I heard that they trade more than any other village in the North, paying well for crops, wood, and meat."
default description_galerocks08 = 0 # "According to {color=#f6d6bd}Foggy{/color}, they lose many folks during their trading trips."
default description_galerocks09 = 0 # "I heard that it was the people of {color=#f6d6bd}Gale Rocks{/color} who helped establish {color=#f6d6bd}Creeks{/color}, and they used to be of a much more welcoming nature."
default description_galerocks10 = 0 # "According to the locals, “There’s no coin worth losing a neighbor.”"
default description_galerocks11 = 0 # "I heard that in the past they’ve been mistreated and robbed by outsiders."
default description_galerocks12 = 0 # "{color=#f6d6bd}Severina{/color} seems to be convinced that the villagers are close to being defenseless without their walls."
default description_galerocks13 = 0 # "According to {color=#f6d6bd}Petronius{/color}, {color=#f6d6bd}Severina{/color} has a short patience. “When I speak with her, I’d rather say less, but quickly. And it’s better to tell her only one, two things at once, bring her other news after she gets a good sleep.”"
default description_galerocks14 = 0 # "According to {color=#f6d6bd}Tertia{/color}, “they follow Wright’s teachings, work hard and live humbly. We used to trade with them and take our clothes to {color=#f6d6bd}Rufina{/color} for fixing, but they betrayed our trust and if it weren’t for the plague, we’d be sharpening our blades.”"
default description_galerocks15 = 0 # "According to {color=#f6d6bd}Aeli{/color}, the village has a small temple dedicated to The Wright."

default description_highisland00 = 0 # "The largest island in the North. Unreachable without a boat."
default description_highisland01 = 0 # "The island’s surface is high above the water, and it’s covered with a lush forest. In its center stands a large volcano."
default description_highisland02 = 0 # "I’ve heard rumors of “treasures and huge monsters” that can be found there."
default description_highisland03 = 0 # "The only way to get to the surface of the island is to reach it during nighttime, through a waterfall."
default description_highisland04 = 0 # "According to {color=#f6d6bd}Foggy{/color}, the people of {color=#f6d6bd}Gale Rocks{/color} and {color=#f6d6bd}Howler’s Dell{/color} may know more about the place."
default description_highisland05 = 0 # "In distant times, it used to be a home to {color=#f6d6bd}The Tribe of The Green Mountain{/color}, who were then pushed away by {color=#f6d6bd}Hovlavan’s{/color} army."
default description_highisland06 = 0 # "It’s possible that the island still hides ruins of an old village."
default description_highisland07 = 0 # "Since there are many harpies between the island and the coast, it may be better to have a proper ranged weapon, or a shooting expert."
default description_highisland08 = 0 # "According to {color=#f6d6bd}Navica{/color}, I need to reach the “closer” waterfall."
default description_highisland08a = 0 # "According to {color=#f6d6bd}Gaiane{/color}, I need to reach the “northern” waterfall."
default description_highisland09 = 0 # "I’ve heard about a group of cityfolk who landed on this during wartime, and never returned."
default description_highisland10 = 0 # "The story of this place reaches centuries back. According to what you’ve heard, {color=#f6d6bd}The Tribe of The Green Mountain{/color} used to thrive on this island, but was thrown out by the corsairs of {color=#f6d6bd}Hovlavan{/color} when it refused to join the city."
default description_highisland11 = 0 # "According to {color=#f6d6bd}Photios{/color}, the direct route from his village to the island is crowded with harpies, but having an inexperienced crew would make taking the longer path quite tiring."
default description_highisland12 = 0 # "According to {color=#f6d6bd}Severina{/color}, the locals are forbidden to sail to this island."
default description_highisland13 = 0 # "According to {color=#f6d6bd}the old sailor{/color}, I need to take a strong source of light with me - the island is so overgrown it’s covered with darkness."
default description_highisland15 = 0 # "{color=#f6d6bd}Cephas{/color} described the meaning of the map of The Sleeping Giant as follows: “T’ great green light in t’ center is {color=#f6d6bd}T’ Green Mountain{/color}, and t’ great blue one next to it - t’ home of T’ Tribe. T’ others mark buildings. T’ dim ones were lost even before t’ days of t’ corsairs. We abandoned t’ brighter ones only eight generations ago. Blue lights stand for hamlets. White - camps and dolmens. Yellow - watchtowers. T’ orange... Are different, as ‘ey mean the lairs of t’ greatest beasts.”"

default hovlavan_humaninteraction = 0
default hovlavan_music = 0
default hovlavan_nakedness = 0
# {color=#f6d6bd}Hovlavan{/color} - in reality, theres much more to find in the journal, just based on different variables
default description_hovlavan00 = "One of the greatest harbors in The Dragonwoods, and the heart of the north-western province of The Ten Cities. I was hired by its officials and merchants."
default description_hovlavan01 = 0 # ""
default description_hovlavan02 = 0 # ""
default description_hovlavan03 = 0 # ""
default description_hovlavan04 = 0 # "nooldstatues" "oldstatuesnoattention" "oldstatuesofheroes" "oldstatuesofthemselves" "oldstatuesofimportantplaces"
default description_hovlavan05 = 0 # ""
default description_hovlavan06 = 0 # ""
default description_hovlavan07 = 0 # ""
default description_hovlavan08 = 0 # "The priests of The United Church live more comfortable lives than most cityfolk, and therefore look much healthier than the others."
default description_hovlavan09 = 0 # "During The Southern Invasion, the city kept many asylum seekers outside the walls, unable to provide shelter to the great number of people who reached this place from the southern provinces. The way these refugees disturbed the forests has provoked a dragon attack, and brought doom on many of them."
default description_hovlavan10 = 0 # ""
default description_hovlavan11 = 0 # ""
default description_hovlavan12 = 0 # ""
default description_hovlavan13 = 0 # ""
default description_hovlavan14 = 0 # ""
default description_hovlavan15 = 0 # ""
default description_hovlavan16 = 0 # ""
default description_hovlavan17 = 0 # ""
default description_hovlavan18 = 0 # ""
default description_hovlavan19 = 0 # "During my time there, I’ve learned how to ignore drunken crowds while sleeping."
default description_hovlavan20 = 0 # ""

default description_howlersdell01 = 0 # "A prosperous village of farmers and animal breeders set on the western road."
default description_howlersdell02 = 0 # "It’s customary for the village mayor to look after the village orphans."
default description_howlersdell03 = 0 # "According to {color=#f6d6bd}Tertia{/color}, “they have food, riches, mead, and pretty houses. But all of those carry poison, and this poison is what leads them.”"
default description_howlersdell04 = 0 # "According to {color=#f6d6bd}Elah{/color}, the locals are unwilling to help others, and are led by a tyrant."
default description_howlersdell05 = 0 # "The locals are following the teachings of a group of druids."
default description_howlersdell06 = 0 # "It was set {i}centuries ago{/i} at the wide, but shallow Howler’s Creek."
default description_howlersdell06a = 0 # "The locals are proud of their wealth and the goods they have to sell."
default description_howlersdell06b = "" # "{color=#f6d6bd}Thais{/color} calls it the “greatest village in the far North.”"
default description_howlersdell07 = 0 # "It used to have an access to the fishing hamlet set at the western coast."
default description_howlersdell08 = 0 # "The inn placed at the village square is named {color=#f6d6bd}Ape Ale{/color}."
default description_howlersdell08a = "" # " I’ve heard in {color=#f6d6bd}Pelt{/color} that their prices are “absurd”."
default description_howlersdell09 = 0 # "According to {color=#f6d6bd}Thyrsus{/color}: “Cadn’t handle their looks. Their tone. They thought they’re betta than us here. An’ didn’t let me forget that.”"
default description_howlersdell10 = 0 # ""

default description_bighunters01 = 0 #They are led by #[iason_name].
default description_bighunters02 = 0 #According to #[iason_name], they are cautious and value teamwork above all else.
default description_bighunters02b = 0 #, they are cautious and value teamwork above all else.
default description_bighunters03 = 0 #"Most of them came here from the South, but some were born in the peninsula."
default description_bighunters04 = 0 #"They arrived here about ten years ago."
default description_bighunters05 = 0 #"According to {color=#f6d6bd}Foggy{/color}, “they can be a lot of fun if he’s not around.”"
default description_bighunters06 = 0 #"According to {color=#f6d6bd}Efren{/color}, “at least they smile, unlike the others in the peninsula.”"
default description_bighunters10 = 0 #"{color=#f6d6bd}Pelt’s{/color} innkeep admitted that his crew was helping {color=#f6d6bd}Thais{/color} during the raid on {color=#f6d6bd}Steep House{/color}."

default description_monastery00 = "The monastery devoted to the teachings of an Order of Truth is set near {color=#f6d6bd}the Old Págos village{/color}, near the western road."
default description_monastery01 = 0 #According to [iason_name]", the monastery has unusual teachings, and the monks are experienced alchemists."
default description_monastery02 = 0 #"According to {color=#f6d6bd}Foggy{/color}, her old friend used to say that sleeping in the monastery helps him with casting spells."
default description_monastery03 = 0 #"The monks may welcome some “delicacies.”"
default description_monastery04 = 0 #"According to Eudocia, the prelate is used to being surrounded by obedient, apologetic people."
default description_monastery05 = 0 #"I heard that I can ask the monks to read any piece of writing I struggle with."
default description_monastery06 = 0 #"I’ve heard they may be able to give me a better understanding of necromancy."
default description_monastery07 = 0 #"{color=#f6d6bd}The old druid{/color} told me to “speak with them with nae anger, but also nae foolery.”"
default description_aeli00 = 0 # "The monk who speaks in the name of the local monastery introduced himself as {color=#f6d6bd}Aeli{/color}."
default description_aeli01 = 0 # "According to" #iason_name
default description_aeli01a = ", {color=#f6d6bd}Aeli{/color} used to be a bandit in his youth, but is now one of the more important alchemists."

default description_oldpagos00 = 0 # "According to {color=#f6d6bd}Quintus{/color}, {i}Págos{/i} means {i}Hill{/i}. He seems to be proud of his home."
default description_oldpagos01 = 0 # "A western village settled on barren soil. The locals exchange the stones from their quarries for supplies."
default description_oldpagos02 = 0 # "It’s connected strongly with the nearby Order of Truth."
default description_oldpagos03 = 0 # "I heard that the nearby grounds are somewhat peaceful."
default description_oldpagos03a = 0 # "In {color=#f6d6bd}Gale Rocks{/color}, I heard that the locals are willing to welcome the outsiders."
default description_oldpagos04 = 0 # "According to {color=#f6d6bd}the scavenger{/color}, the locals “are cold, they spend days praying and talking on and on about their {i}duty{/i}, and are gray like an ashworm.”"
default description_oldpagos04a = 0 # "According to {color=#f6d6bd}Elah{/color}, the locals value those who fulfil their “duty.”"
default description_oldpagos05 = 0 # “as long as you don’t mock their Order and act nice, they’ll also be kind. My boss says they’re too serious for him to stand them, but at least they don’t bite without a reason.”
default description_oldpagos06 = 0 # "It may be one of the oldest settlements in the North."
default description_oldpagos07 = 0 # "According to {color=#f6d6bd}Glaucia{/color}, they have a strong squad of guards who see their job as a way to fulfill their sacred duty."
default description_oldpagos08 = 0 # "According to {color=#f6d6bd}Foggy{/color}, “they don’t look kindly at those who don’t follow the Orders of Truth”, but “are true believers” and “good people”."
default description_oldpagos09 = 0 # "According to the wayfarers I met, the locals “are a warm bunch”."
default description_oldpagos10 = 0 # "According to {color=#f6d6bd}Orentius{/color}, the locals “have nuff zeal to spread doubt about us, yet lacked faith to help us when we needed them the most.”"

default description_shortcut00 = 0 # "A shortcut leading through the center of the peninsula."
default description_shortcut01 = 0 # "I heard that it connects the western villages to the watchtower in the east."
default description_shortcut02 = 0 # "I heard that to get to the bandit camp, one needs to own a grappling hook."
default description_shortcut03 = 0 # "The locals claim that this place is abandoned, neglected, and unusually dangerous."
default description_shortcut04 = 0 # "I was advised to use it only when healthy, ideally with a fine equipment at hand."
default description_shortcut05 = 0 # "According to {color=#f6d6bd}Foggy{/color}: “Stay as close to the road as you can. You may find parts that seem safe, but nothing ‘bout the woods is. Sooner or later, something flesh-chasing will show up. Don’t get yourself killed for a couple of sour apples. The cairn in the middle of the road may seem safer, but there are some nasty beasts living in the grass. You won’t return with a twisted ankle.”"
default description_shortcut06 = 0 # "According to {color=#f6d6bd}Ilan{/color}, it’s a bad idea to enter the woods without a crossbow."
default description_shortcut07 = 0 # "According to {color=#f6d6bd}Efren{/color}, I may encounter gnolls and frightapes. He told me a bit more about them."
default description_shortcut08 = 0 # "According to {color=#f6d6bd}Eudocia{/color}, the best way to deal with the monkeys in the far west is to ignore them, so that they get used to one’s sight."
default description_shortcut09 = 0 # "According to {color=#f6d6bd}[dalit_name]{/color}: #“There are treants there, and wolves, even the furless ones. And if you have to go through the tall grasses, watch out for what’s on the ground. There ain’t many archers on the trees, but there are all too many worms, even larger than a water leech.”"
default description_shortcut10 = 0 # "According to {color=#f6d6bd}Glaucia{/color}: “There ain’t anything free in the woods. A lost bone, rotten apple, shiny pebble, a cave. Everything will be eaten or taken away, and if it’s laying there all by itself, you better wonder why.”"

default description_ruinedvillage00 = 0 # ""
default description_ruinedvillage01 = 0 # "According to""
default description_ruinedvillage01a = ", “it was destroyed by beasts almost a decade ago.”"
# default quest_ruins_description01 = 0 # "I heard that the village was destroyed almost ten years ago."
default description_ruinedvillage02 = 0 # "{color=#f6d6bd}The monks{/color} blame the people of {color=#f6d6bd}Howler’s Dell{/color} for destroying {color=#f6d6bd}Steep House{/color}. According to their story, {color=#f6d6bd}Thais{/color} tried to make an example out of these villagers when they refused to join her covenant."
default description_ruinedvillage03 = 0 # ""
default description_ruinedvillage04 = 0 # ""
default description_ruinedvillage05 = 0 # ""
default description_ruinedvillage06 = 0 # ""
default description_ruinedvillage07 = 0 # ""
default description_ruinedvillage08 = 0 # ""
default description_ruinedvillage09 = 0 # ""
default description_ruinedvillage10 = 0 # ""

default description_whitemarshes00 = 0 # "To enter it, I need to pay a toll to {color=#f6d6bd}Thyrsus{/color}, the mage living among the peat fields."
default description_whitemarshes01 = 0 # "A village set among the western bogs." # "A village of foragers and peat gatherers set among the western bogs."
default description_whitemarshes01a = 0 # "In {color=#f6d6bd}Gale Rocks{/color}, I was told by a pious elder that the locals are “dark wizards who build their army to crush us all. Show them your strength, and never hide your axe!”"
default description_whitemarshes_helvius01 = 0 # "The mayor of the village is known as {color=#f6d6bd}Helvius{/color}."
default description_whitemarshes_helvius02 = 0 # "“like all brutes, he understands only strength, and hates those who challenge him.”"
default description_whitemarshes02 = 0 # "The locals use the awoken undead to do their bidding."
default description_whitemarshes02a = "" # " Quite a few people can give them orders."
default description_whitemarshes03 = 0 # "Some of the locals decided to leave their homes once the village had started to awaken the dead."
default description_whitemarshes04 = 0 # "The locals have recently started to raise a lot of structures."
default description_whitemarshes05 = 0 # "I heard that the locals had to stop selling their lumber because {color=#f6d6bd}Howler’s Dell{/color} started offering their own supplies for much better prices. Because of that, the village fell into poverty."
default description_whitemarshes06 = 0 # "The locals are especially interested in purchasing iron."
default description_whitemarshes07 = 0 # "It’s possible that the only paths connecting the deeper bogs with the rest of the peninsula were built from scratch by the locals."
default description_whitemarshes08 = 0 # "{color=#f6d6bd}Efren{/color}, the hunter, believes the local seeds should not be trusted."
default description_whitemarshes09 = 0 # "I’ve heard in {color=#f6d6bd}Pelt{/color} that “their priest doesn’t look kindly on hard drinks, imagine that. He say it {i}clouds one’s judgment{/i}.”"
default description_whitemarshes10 = 0 # "According to {color=#f6d6bd}Aeli{/color}, the village “has been struggling for years. With food, children, the beasts of the bogs, the traders. They were strangers to us, even in the old days, when they used to join {color=#f6d6bd}Old Págos{/color} in their pagan feasts. But then, the monks arrived, and that bridge went down with flames. When the missionaries reached the bogs during the years of war, there were already some wounds that could never be sealed, not even by a shared prayer.”"
default description_whitemarshes11 = 0 # "According to {color=#f6d6bd}Severina{/color}, the village has gone through terrifying hunger."
default description_whitemarshes12 = 0 # "According to {color=#f6d6bd}Glaucia{/color}, the villagers are using more than just their own dead - they are willing to seek corpses in the wilderness."
default description_whitemarshes13 = 0 # "According to {color=#f6d6bd}Glaucia{/color}, they are a harsh tribe that “will listen only to the strong and the gritty.”"
default description_whitemarshes14 = 0 # "The locals’ necromantic “talents” are at least partially substituted by blood magic."
default description_whitemarshes15 = 0 #"According to {color=#f6d6bd}Thyrsus{/color}, the locals are weak in pneuma."
default description_whitemarshes17 = 0 #The locals feel threatened and may attempt to completely seperate themselves from the rest of the peninsula.

default bestiary = 0
default bestiary_ghouls_legend = 0
default bestiary_goblins_mourn = 0
default bestiary_seamonsters_city = 0
default bestiary_griffon_parenting = 0

######### JOURNAL - lista questów
screen journal():
    tag menu
    on "show" action SetVariable("game_menu_screen", "journal")
    on "replace" action SetVariable("game_menu_screen", "journal")
    use game_menu(_("Journal")):
        vbox:
            spacing 20
            hbox:
                style_prefix "journalmode"
                xalign 0.0
                yalign 0.0
                xpos -20
                xmaximum 900
                ypos 0
                spacing 60
                textbutton "Quests" action [SetVariable("journalmode", "quests")]
                textbutton "Humans" action [SetVariable("journalmode", "people")]
                textbutton "Groups & Places" action [SetVariable("journalmode", "groups")]
                textbutton "Bestiary" action [SetVariable("journalmode", "bestiary")]
                textbutton "Glossary" action [SetVariable("journalmode", "glossary")]
                textbutton "Notes" action [SetVariable("journalmode", "notes")]
            hbox:
                box_wrap True
                xpos -30
                ypos 10
                if journalmode == "quests":
                    hbox:
                        xmaximum 380
                        viewport id "listquests":
                            draggable True
                            xmaximum 350
                            mousewheel True
                            xpos 10
                            vbox:
                                style_prefix "journal"
                                xalign 0.0
                                yalign 0.0
                                xmaximum 350
                                xpos 10
                                ypos 6
                                spacing 20
                                if quest_explorepeninsula == 1:
                                    textbutton "Explore the Peninsula" action [SetVariable("journal_quest", "quest_explorepeninsula")]
                                if quest_pc_goal == 1:
                                    textbutton "[quest_pc_goal_name]" action [SetVariable("journal_quest", "quest_pc_goal")]
                                if quest_asterion == 1:
                                    textbutton "Find the Roadwarden" action [SetVariable("journal_quest", "quest_asterion")]
                                if quest_gatheracrew == 1:
                                    textbutton "Gather a Crew" action [SetVariable("journal_quest", "quest_gatheracrew")]
                                if quest_birdhunting == 1:
                                    textbutton "Bird Hunting" action [SetVariable("journal_quest", "quest_birdhunting")]
                                if quest_bronzerod == 1:
                                    textbutton "Bronze Rods" action [SetVariable("journal_quest", "quest_bronzerod")]
                                if quest_foggy3whitemarshes == 1:
                                    textbutton "Cask of Cider" action [SetVariable("journal_quest", "quest_foggy3whitemarshes")]
                                if quest_foggy2iason == 1:
                                    textbutton "Check on Iason" action [SetVariable("journal_quest", "quest_foggy2iason")]
                                if quest_foggy1oldpagos == 1:
                                    textbutton "Check on Old Págos" action [SetVariable("journal_quest", "quest_foggy1oldpagos")]
                                if quest_closedtunnel == 1:
                                    textbutton "Closed Tunnel" action [SetVariable("journal_quest", "quest_closedtunnel")]
                                if quest_cursedcoins == 1:
                                    textbutton "Cursed Coins" action [SetVariable("journal_quest", "quest_cursedcoins")]
                                if quest_easternpath == 1:
                                    textbutton "Eastern Path" action [SetVariable("journal_quest", "quest_easternpath")]
                                if quest_empresscarp == 1:
                                    textbutton "Empress Carp" action [SetVariable("journal_quest", "quest_empresscarp")]
                                if quest_escortpyrrhos == 1:
                                    textbutton "Escort The Scavenger" action [SetVariable("journal_quest", "quest_escortpyrrhos")]
                                if quest_fallentree == 1:
                                    textbutton "Fallen Tree" action [SetVariable("journal_quest", "quest_fallentree")]
                                if quest_fetchingfood == 1:
                                    textbutton "Fetching Food" action [SetVariable("journal_quest", "quest_fetchingfood")]
                                if quest_eudociaflower == 1:
                                    textbutton "Flowers for Eudocia" action [SetVariable("journal_quest", "quest_eudociaflower")]
                                if quest_thyrsusgift == 1:
                                    textbutton "Thyrsus’ Wand" action [SetVariable("journal_quest", "quest_thyrsusgift")]
                                if quest_intelforpeltnorth == 1:
                                    textbutton "Glaucia’s Band" action [SetVariable("journal_quest", "quest_intelforpeltnorth")]
                                if quest_healingtheplague == 1:
                                    textbutton "Healing the Plague" action [SetVariable("journal_quest", "quest_healingtheplague")]
                                if quest_hiddenpurse == 1:
                                    textbutton "Hidden Pouch" action [SetVariable("journal_quest", "quest_hiddenpurse")]
                                if quest_reachthepaganvillage == 1:
                                    textbutton "Hidden Village" action [SetVariable("journal_quest", "quest_reachthepaganvillage")]
                                if quest_lostmerchants == 1:
                                    textbutton "Lost Merchants" action [SetVariable("journal_quest", "quest_lostmerchants")]
                                if quest_matchmaking == 1:
                                    textbutton "Matchmaking" action [SetVariable("journal_quest", "quest_matchmaking")]
                                if quest_healingpotion == 1:
                                    textbutton "Merchant’s Medicament" action [SetVariable("journal_quest", "quest_healingpotion")]
                                # if quest_messageseverina == 1:
                                #     textbutton "Message To Akakios" action [SetVariable("journal_quest", "quest_messageseverina_description_akakios")]
                                if quest_missinghunters == 1:
                                    textbutton "Missing Hunters" action [SetVariable("journal_quest", "quest_missinghunters")]
                                if quest_fisherhamlet == 1:
                                    textbutton "Old Hamlet" action [SetVariable("journal_quest", "quest_fisherhamlet")]
                                if quest_orentius == 1:
                                    textbutton "Orentius, the Necromancer" action [SetVariable("journal_quest", "journal_quest_orentius")]
                                if quest_pensformonastery == 1:
                                    textbutton "Quills for The Monastery" action [SetVariable("journal_quest", "quest_pensformonastery")]
                                if quest_readtheletter == 1:
                                    textbutton "Read the Letter" action [SetVariable("journal_quest", "quest_readtheletter")]
                                if quest_recruitahunter == 1:
                                    textbutton "Recruit a Hunter" action [SetVariable("journal_quest", "quest_recruitahunter")]
                                if quest_ruins == 1:
                                    textbutton "Ruined Village" action [SetVariable("journal_quest", "quest_ruins")]
                                if quest_runaway == 1:
                                    textbutton "Runaway" action [SetVariable("journal_quest", "quest_runaway")]
                                if quest_sleepinggiant == 1:
                                    textbutton "Sleeping Giant" action [SetVariable("journal_quest", "quest_sleepinggiant")]
                                if quest_spiritrock == 1:
                                    textbutton "Spirit Rock" action [SetVariable("journal_quest", "quest_spiritrock")]
                                if quest_spyonwhitemarshes == 1 and quest_spyonwhitemarshes_description01:
                                    textbutton "Spy on White Marshes" action [SetVariable("journal_quest", "quest_spyonwhitemarshes")]
                                if quest_studyingthegolems == 1:
                                    textbutton "Studying the Golems" action [SetVariable("journal_quest", "quest_studyingthegolems")]
                                if quest_glauciasupport == 1:
                                    textbutton "Support of Bandits" action [SetVariable("journal_quest", "quest_glauciasupport")]
                                if quest_creekssupport == 1:
                                    textbutton "Support of Creeks" action [SetVariable("journal_quest", "quest_creekssupport")]
                                if quest_galerockssupport == 1:
                                    textbutton "Support of Gale Rocks" action [SetVariable("journal_quest", "quest_galerockssupport")]
                                if quest_howlerssupport == 1:
                                    textbutton "Support of Howler’s Dell" action [SetVariable("journal_quest", "quest_howlerssupport")]
                                if quest_monasterysupport == 1:
                                    textbutton "Support of Monks" action [SetVariable("journal_quest", "quest_monasterysupport")]
                                if quest_oldpagossupport == 1:
                                    textbutton "Support of Old Págos" action [SetVariable("journal_quest", "quest_oldpagossupport")]
                                if quest_greenmountainsupport == 1:
                                    textbutton "Support of The Tribe of The Green Mountain" action [SetVariable("journal_quest", "quest_greenmountainsupport")]
                                if quest_swampaltar == 1:
                                    textbutton "Swamp Altar" action [SetVariable("journal_quest", "quest_swampaltar")]

                                text "{size=10}\n{/size}{color=#6a6a6a}Completed Quests:{/color}"
                                if quest_explorepeninsula > 1:
                                    textbutton "Explore the Peninsula" action [SetVariable("journal_quest", "quest_explorepeninsula")]
                                if quest_pc_goal > 1:
                                    textbutton "[quest_pc_goal_name]" action [SetVariable("journal_quest", "quest_pc_goal")]
                                if quest_asterion > 1:
                                    textbutton "Find the Roadwarden" action [SetVariable("journal_quest", "quest_asterion")]
                                if quest_gatheracrew > 1:
                                    textbutton "Gather a Crew" action [SetVariable("journal_quest", "quest_gatheracrew")]
                                if quest_bronzerod == 2 or quest_bronzerod == 3:
                                    textbutton "Bronze Rods" action [SetVariable("journal_quest", "quest_bronzerod")]
                                if quest_birdhunting > 1:
                                    textbutton "Bird Hunting" action [SetVariable("journal_quest", "quest_birdhunting")]
                                if quest_foggy3whitemarshes == 2 or quest_foggy3whitemarshes == 3:
                                    textbutton "Cask of Cider" action [SetVariable("journal_quest", "quest_foggy3whitemarshes")]
                                if quest_foggy2iason > 1:
                                    textbutton "Check on Iason" action [SetVariable("journal_quest", "quest_foggy2iason")]
                                if quest_foggy1oldpagos > 1:
                                    textbutton "Check on Old Págos" action [SetVariable("journal_quest", "quest_foggy1oldpagos")]
                                if quest_closedtunnel > 1:
                                    textbutton "Closed Tunnel" action [SetVariable("journal_quest", "quest_closedtunnel")]
                                if quest_cursedcoins > 1:
                                    textbutton "Cursed Coins" action [SetVariable("journal_quest", "quest_cursedcoins")]
                                if quest_easternpath > 1:
                                    textbutton "Eastern Path" action [SetVariable("journal_quest", "quest_easternpath")]
                                if quest_empresscarp > 1:
                                    textbutton "Empress Carp" action [SetVariable("journal_quest", "quest_empresscarp")]
                                if quest_escortpyrrhos > 1:
                                    textbutton "Escort the Scavenger" action [SetVariable("journal_quest", "quest_escortpyrrhos")]
                                if quest_fallentree > 1:
                                    textbutton "Fallen Tree" action [SetVariable("journal_quest", "quest_fallentree")]
                                if quest_fetchingfood > 1:
                                    textbutton "Fetching Food" action [SetVariable("journal_quest", "quest_fetchingfood")]
                                if quest_thyrsusgift > 1:
                                    textbutton "Thyrsus’ Wand" action [SetVariable("journal_quest", "quest_thyrsusgift")]
                                if quest_eudociaflower > 1:
                                    textbutton "Flowers for Eudocia" action [SetVariable("journal_quest", "quest_eudociaflower")]
                                if quest_intelforpeltnorth > 1:
                                    textbutton "Glaucia’s Band" action [SetVariable("journal_quest", "quest_intelforpeltnorth")]
                                if quest_healingtheplague > 1:
                                    textbutton "Healing the Plague" action [SetVariable("journal_quest", "quest_healingtheplague")]
                                if quest_reachthepaganvillage > 1:
                                    textbutton "Hidden Village" action [SetVariable("journal_quest", "quest_reachthepaganvillage")]
                                if quest_lostmerchants > 1:
                                    textbutton "Lost Merchants" action [SetVariable("journal_quest", "quest_lostmerchants")]
                                if quest_matchmaking > 1:
                                    textbutton "Matchmaking" action [SetVariable("journal_quest", "quest_matchmaking")]
                                if quest_hiddenpurse > 1:
                                    textbutton "Hidden Pouch" action [SetVariable("journal_quest", "quest_hiddenpurse")]
                                if quest_healingpotion > 1:
                                    textbutton "Merchant’s Medicament" action [SetVariable("journal_quest", "quest_healingpotion")]
                                # if quest_messageseverina > 1:
                                #     textbutton "Message To Akakios" action [SetVariable("journal_quest", "quest_messageseverina_description_akakios")]
                                if quest_missinghunters == 2: # not 3 - 3 means that the quest appeared too late for it to start up
                                    textbutton "Missing Hunters" action [SetVariable("journal_quest", "quest_missinghunters")]
                                if quest_fisherhamlet > 1:
                                    textbutton "Old Hamlet" action [SetVariable("journal_quest", "quest_fisherhamlet")]
                                if quest_orentius > 1:
                                    textbutton "Orentius, the Necromancer" action [SetVariable("journal_quest", "journal_quest_orentius")]
                                if quest_pensformonastery > 1:
                                    textbutton "Quills for The Monastery" action [SetVariable("journal_quest", "quest_pensformonastery")]
                                if quest_readtheletter > 1:
                                    textbutton "Read the Letter" action [SetVariable("journal_quest", "quest_readtheletter")]
                                if quest_recruitahunter > 1:
                                    textbutton "Recruit a Hunter" action [SetVariable("journal_quest", "quest_recruitahunter")]
                                if quest_ruins > 1:
                                    textbutton "Ruined Village" action [SetVariable("journal_quest", "quest_ruins")]
                                if quest_runaway > 1:
                                    textbutton "Runaway" action [SetVariable("journal_quest", "quest_runaway")]
                                if quest_sleepinggiant > 1:
                                    textbutton "Sleeping Giant" action [SetVariable("journal_quest", "quest_sleepinggiant")]
                                if quest_spiritrock > 1:
                                    textbutton "Spirit Rock" action [SetVariable("journal_quest", "quest_spiritrock")]
                                if quest_spyonwhitemarshes > 1 and quest_spyonwhitemarshes_description01:
                                    textbutton "Spy on White Marshes" action [SetVariable("journal_quest", "quest_spyonwhitemarshes")]
                                if quest_studyingthegolems > 1:
                                    textbutton "Studying the Golems" action [SetVariable("journal_quest", "quest_studyingthegolems")]
                                if quest_glauciasupport == 2 or quest_glauciasupport == 3: # 4 means quest wasn't accepted
                                    textbutton "Support of Bandits" action [SetVariable("journal_quest", "quest_glauciasupport")]
                                if quest_creekssupport > 1:
                                    textbutton "Support of Creeks" action [SetVariable("journal_quest", "quest_creekssupport")]
                                if quest_galerockssupport > 1:
                                    textbutton "Support of Gale Rocks" action [SetVariable("journal_quest", "quest_galerockssupport")]
                                if quest_howlerssupport > 1:
                                    textbutton "Support of Howler’s Dell" action [SetVariable("journal_quest", "quest_howlerssupport")]
                                if quest_monasterysupport > 1:
                                    textbutton "Support of Monks" action [SetVariable("journal_quest", "quest_monasterysupport")]
                                if quest_oldpagossupport == 2: # 3 doesn't show up
                                    textbutton "Support of Old Págos" action [SetVariable("journal_quest", "quest_oldpagossupport")]
                                if quest_greenmountainsupport == 2: # 3 doesn't show up
                                    textbutton "Support of The Tribe of The Green Mountain" action [SetVariable("journal_quest", "quest_greenmountainsupport")]
                                if quest_swampaltar > 1:
                                    textbutton "Swamp Altar" action [SetVariable("journal_quest", "quest_swampaltar")]
                        vbar value YScrollValue ("listquests"):
                            xpos 30
                            unscrollable "hide"

                    hbox:
                        xmaximum 1100
                        viewport id "journalquests":
                            draggable True
                            xmaximum 1008
                            mousewheel True
                            xpos 66
                            vbox:
                                style_prefix "journal"
                                xalign 0.0
                                yalign 0.0
                                xpos 80
                                xmaximum 968
                                ypos 10
                                spacing 20
                                #######
                                if journal_quest == "quest_explorepeninsula":
                                    label _("{color=#f6d6bd}Explore the Peninsula{/color}"):
                                        style "journal_prompt"
                                    if quest_explorepeninsula_description01 and difficultypick_advanced_questseasier:
                                        text "[quest_explorepeninsula_description01]"
                                    elif quest_explorepeninsula_description01 and not difficultypick_advanced_questseasier:
                                        text "[quest_explorepeninsula_description01] {b}I have to leave the peninsula on the [world_deadline_display]th day of my journey, or sooner.{/b}"
                                    if quest_explorepeninsula_description01a:
                                        text "[quest_explorepeninsula_description01a]"
                                    if quest_explorepeninsula_description02prec and not quest_explorepeninsula_description02c:
                                        text "[quest_explorepeninsula_description02prec]"
                                    if quest_explorepeninsula_description02c:
                                        text "[quest_explorepeninsula_description02c]"
                                        if quest_explorepeninsula_description02d:
                                            text "[quest_explorepeninsula_description02d]"
                                    elif quest_explorepeninsula_description02a:
                                        text "[quest_explorepeninsula_description02a]"
                                        if quest_explorepeninsula_description02b:
                                            text "[quest_explorepeninsula_description02b]"
                                    if quest_explorepeninsula_description03:
                                        text "[quest_explorepeninsula_description03]"
                                    if quest_explorepeninsula_description03b:
                                        text "[quest_explorepeninsula_description03b]"
                                    if quest_explorepeninsula_description04:
                                        text "[quest_explorepeninsula_description04]"
                                    if quest_explorepeninsula_description05:
                                        text "[quest_explorepeninsula_description05]"
                                    if quest_explorepeninsula_description06:
                                        text "[quest_explorepeninsula_description06]"
                                    if quest_explorepeninsula_description07:
                                        text "[quest_explorepeninsula_description07]"
                                    if quest_explorepeninsula_description08:
                                        text "[quest_explorepeninsula_description08]"
                                    if quest_explorepeninsula_description09:
                                        text "[quest_explorepeninsula_description09]"
                                    if quest_explorepeninsula_description10:
                                        text "[quest_explorepeninsula_description10]"
                                    if quest_explorepeninsula_description10b:
                                        text "[quest_explorepeninsula_description10b]"
                                    if quest_explorepeninsula_description10c:
                                        text "[quest_explorepeninsula_description10c]"
                                    if quest_explorepeninsula_description11:
                                        text "[quest_explorepeninsula_description11]"
                                    if quest_explorepeninsula_description12 and not quest_explorepeninsula_description12a:
                                        text "[quest_explorepeninsula_description12]"
                                    if quest_explorepeninsula_description12a:
                                        text "[quest_explorepeninsula_description12a]"
                                    if quest_explorepeninsula_description13 and quest_explorepeninsula_description13b:
                                        text "[quest_explorepeninsula_description13] [quest_explorepeninsula_description13b]"
                                    elif quest_explorepeninsula_description13:
                                        text "[quest_explorepeninsula_description13]"
                                    if quest_explorepeninsula_description14:
                                        text "[quest_explorepeninsula_description14]"
                                    if quest_explorepeninsula_description15c:
                                        text "[quest_explorepeninsula_description15c]"
                                    elif quest_explorepeninsula_description15b:
                                        text "[quest_explorepeninsula_description15b]"
                                    elif quest_explorepeninsula_description15a:
                                        text "[quest_explorepeninsula_description15a]"
                                    elif quest_explorepeninsula_description15:
                                        text "[quest_explorepeninsula_description15]"
                                    if foragingground_foraging_vein_sabotaged and quest_explorepeninsula_description16:
                                        text "I shared the news about the ore with the locals. They’ll surely start to investigate it soon."
                                        text "{color=#6a6a6a}[quest_explorepeninsula_description16]{/color}"
                                    elif quest_explorepeninsula_description16:
                                        text "[quest_explorepeninsula_description16]"
                                    if quest_explorepeninsula_description17a:
                                        text "[quest_explorepeninsula_description17a]"
                                    elif quest_explorepeninsula_description17b:
                                        text "[quest_explorepeninsula_description17b]"
                                    if quest_explorepeninsula_description17 and not quest_explorepeninsula_description17a:
                                        text "[quest_explorepeninsula_description17]"
                                    elif quest_explorepeninsula_description17 and quest_explorepeninsula_description17a:
                                        text "{color=#6a6a6a}[quest_explorepeninsula_description17]{/color}"
                                    if quest_explorepeninsula_description18:
                                        text "[quest_explorepeninsula_description18]"
                                    elif galerocks_resource_barrels or galerocks_resource_fish or galerocks_resource_salt:
                                        if not galerocks_resource_barrels:
                                            $ galerocks_resource_barrels_display = ""
                                        else:
                                            $ galerocks_resource_barrels_display = galerocks_resource_barrels
                                        if not galerocks_resource_fish:
                                            $ galerocks_resource_fish_display = ""
                                        else:
                                            $ galerocks_resource_fish_display = galerocks_resource_fish
                                        if not galerocks_resource_salt:
                                            $ galerocks_resource_salt_display = ""
                                        else:
                                            $ galerocks_resource_salt_display = galerocks_resource_salt
                                        text "In {color=#f6d6bd}Gale Rocks{/color}, traders could [galerocks_resource_fish_display][galerocks_resource_barrels_display][galerocks_resource_salt_display]. However, I feel I can still learn more about the local trade."
                                    if quest_explorepeninsula_description19:
                                        text "[quest_explorepeninsula_description19]"
                                    if quest_explorepeninsula_description20:
                                        text "[quest_explorepeninsula_description20]"
                                #######
                                elif journal_quest == "quest_pc_goal":
                                    label _("{color=#f6d6bd}[quest_pc_goal_name]{/color}"):
                                        style "journal_prompt"
                                    if quest_pc_goal_description_completed_ineedmoney:
                                        text "[quest_pc_goal_description_completed_ineedmoney]"
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    if quest_pc_goal_description_completed_iwantmoney:
                                        text "[quest_pc_goal_description_completed_iwantmoney]"
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    if quest_pc_goal_description_completed_ineedmoney100:
                                        text "[quest_pc_goal_description_completed_ineedmoney100]"
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    if quest_pc_goal_description_completed_iwantmoney100:
                                        text "[quest_pc_goal_description_completed_iwantmoney100]"
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    if quest_pc_goal_description_completed_iwantstatus:
                                        text "[quest_pc_goal_description_completed_iwantstatus]"
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    if quest_pc_goal_description_completed_iwanttoberemembered:
                                        text "[quest_pc_goal_description_completed_iwanttoberemembered]"
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    if quest_pc_goal_description_completed_iwanttohelp:
                                        text "[quest_pc_goal_description_completed_iwanttohelp]"
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    if quest_pc_goal_description_completed_iwanttostartanewlife:
                                        text "[quest_pc_goal_description_completed_iwanttostartanewlife]"
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    if pc_goal == "ineedmoney":
                                        text "I need to gather enough dragon bones to save my sibling from debt collectors. A hundred coins would be a good start. I could also look for an expensive treasure, something that’s going to sell well in {color=#f6d6bd}Hovlavan{/color}."
                                    if pc_goal == "iwantmoney":
                                        text "I want to gather enough dragon bones to retire early and live in prosperity and safety. A hundred coins would be a good start. I could also look for an expensive treasure, something that’s going to sell well in {color=#f6d6bd}Hovlavan{/color}."
                                    if pc_goal == "iwanttoberemembered":
                                        text "I want to be remembered as the soul who brought peace and order to this realm. A hero."
                                        if oldpagos_cured:
                                            text "The people of {color=#f6d6bd}Old Págos{/color} will remember me as their savior."
                                        if quest_ruins_choice == "thais_defeated":
                                            text "Because of me, {color=#f6d6bd}Thais{/color} will face justice for the destruction of {color=#f6d6bd}Steep House{/color}."
                                        if orentius_convinced:
                                            text "Without using force, I helped the people of {color=#f6d6bd}White Marshes{/color} abandon their necromantic practices."
                                        elif whitemarshes_nomoreundead:
                                            text "I freed this land from the threat of the undead of {color=#f6d6bd}White Marshes{/color}, even though it took a great sacrifice."
                                        if highisland_returned:
                                            text "I will be remembered as one of the few people who returned from their journey to {color=#f6d6bd}High Island{/color}."
                                        if (quest_missinghunters_admonfound == 2 and quest_missinghunters_daliafound == 2) or (quest_missinghunters_admonfound == 2 and quest_missinghunters_vaschelfound == 2) or (quest_missinghunters_vaschelfound == 2 and quest_missinghunters_daliafound == 2):
                                            text "I helped the people of {color=#f6d6bd}Creeks{/color} learn the truth about their missing tribesfolk."
                                        if quest_easternpath == 2:
                                            text "I secured the eastern path for the people of {color=#f6d6bd}Creeks{/color}."
                                        if quest_galerockssupport == 2:
                                            text "By convicing the people of {color=#f6d6bd}Gale Rocks{/color} to do the right thing, I made a crucial step in getting rid of the highwaymen from the peninsula."
                                        if oldpagos_plague_helpfromgalerocks == 2:
                                            text "I layed the groundwork for restoring the friendship between {color=#f6d6bd}Gale Rocks{/color} and {color=#f6d6bd}Old Págos{/color}."
                                        if quest_closedtunnel == 2 and oldtunnel_inside_undead_defeated_bypc:
                                            text "I opened {color=#f6d6bd}the old tunnel{/color} in the north and eliminated its undead."
                                    if pc_goal == "iwanttohelp":
                                        text "While I’m here, I want to help people. Make this region safer for the locals and newcomers alike."
                                        if oldpagos_cured:
                                            text "I saved {color=#f6d6bd}Old Págos{/color} from the plague, getting hardly anything in return."
                                        if quest_easternpath == 2:
                                            text "I helped the people of {color=#f6d6bd}Creeks{/color} secure the eastern path."
                                        if quest_missinghunters == 2:
                                            text "I helped the people of {color=#f6d6bd}Creeks{/color} learn the truth about the missing hunters."
                                        if bogroad_triedtohelp:
                                            text "I risked my life trying to save someone in the bogs. An empty effort, but I did my best."
                                        if shortcut_darkforest_bandit_promisedtocoverforhim:
                                            text "I decided to protect {color=#f6d6bd}the runaway bandit{/color} from his chief’s wrath."
                                        if quest_closedtunnel == 2:
                                            text "I opened {color=#f6d6bd}the old tunnel{/color} in the north and eliminated its undead."
                                        if ruinedvillage_goblinlair_EXPLORED:
                                            text "I destroyed the goblin lair at the ruined village."
                                        if description_pyrrhos03 and pyrrhos_quest_potion:
                                            text "I helped {color=#f6d6bd}the scavenger{/color} get to a safe spot and gave him a healing potion."
                                        elif description_pyrrhos03:
                                            text "I helped {color=#f6d6bd}the scavenger{/color} get to a safe spot."
                                        if quest_matchmaking == 2:
                                            text "I helped a few people with finding - or rejecting - their match."
                                        if quest_bronzerod_description05:
                                            text "I helped {color=#f6d6bd}Eudocia{/color} spread her rods across the peninsula."
                                        if eudocia_about_parents:
                                            text "I helped {color=#f6d6bd}Eudocia{/color} learn more about her parents."
                                        if aegidia_favor == "iwill" or aegidia_favor == "iwillforatime":
                                            text "I’ve kept {color=#f6d6bd}Aegidia’s{/color} secret to myself."
                                        if galerocks_photios_quest_spiritrock_about_phoibe_after and galerocks_photios_quest_spiritrock_doubts_phoibe and not galerocks_phoibe_coma:
                                            text "I helped {color=#f6d6bd}Photios{/color} to accept {color=#f6d6bd}Phoibe{/color} as she is."
                                        if glaucia_willreturntogalerocks:
                                            text "I did my best to convince {color=#f6d6bd}Glaucia{/color} to consider returning home and giving up on her band."
                                        if item_ironingot_sold_galerocks:
                                            text "I returned the stolen ingot back to {color=#f6d6bd}Gale Rocks{/color}."
                                        if quest_fetchingfood_description01:
                                            text "I delivered food to {color=#f6d6bd}Quintus{/color}."
                                        if quintus_left_gate:
                                            text "I convinced {color=#f6d6bd}Quintus{/color} to seek shelter."
                                        if quest_healingpotion_description03:
                                            text "I delivered “the medicament” to {color=#f6d6bd}Akakios{/color}."
                                        if quest_pensformonastery == 2:
                                            text "I delivered the quills to the monastery."
                                        if quest_empresscarp == 2:
                                            text "I delivered the empress fish to the druid."
                                        if eudocia_about_flower_refusal:
                                            text "I decided not to deliver snake bait to {color=#f6d6bd}Eudocia{/color} - for her own sake."
                                        if quest_cursedcoins == 2 and quest_cursedcoins_description04:
                                            text "I helped {color=#f6d6bd}Navica{/color} free herself from a curse."
                                        if whitemarshes_pursewoman_coins == 10 and helvius_about_womanwithpurse_denied:
                                            text "I gave {color=#f6d6bd}the woman from White Marshes{/color} more dragon bones than I was obliged to, and kept it a secret from {color=#f6d6bd}Helvius{/color}."
                                        if quest_readtheletter == 2 and quest_readtheletter_description04:
                                            text "I helped {color=#f6d6bd}Valens{/color} learn the truth about his husband."
                                        elif quest_readtheletter == 2 and quest_readtheletter_description01:
                                            text "I helped {color=#f6d6bd}Valens{/color} learn the contents of the letter from his husband."
                                        elif quest_readtheletter == 2 and quest_readtheletter_description01alt:
                                            text "I lied to {color=#f6d6bd}Valens{/color} to save him from pain."
                                    if pc_goal == "iwantstatus":
                                        text "While I’m in the North, I should build connections among the local leaders so I can become a major player in the merchant guild."
                                        if quest_ruins_choice == "thais_alliance":
                                            text "I used my knowledge about {color=#f6d6bd}Steep House{/color} to coerce {color=#f6d6bd}Thais{/color} into working for me."
                                        if quest_ruins_choice == "forgotten" and item_howlersdelltoken and item_thaisletter:
                                            text "I left {color=#f6d6bd}Steep House{/color} to the past, securing my “friendship” with {color=#f6d6bd}Howler’s Dell{/color}."
                                        if quest_galerockssupport == 2:
                                            text "I proved my value to the council of {color=#f6d6bd}Gale Rocks{/color}. Any negotiator with me on their side will have a strong advantage."
                                        if quest_glauciasupport == 2 and not glaucia_about_galerocksdecision_liedto:
                                            text "{color=#f6d6bd}Glaucia’s{/color} band may stay around for long, but {i}I{/i} am the only person who can tame her destructiveness for the guild’s sake."
                                        if quest_creekssupport == 2:
                                            text "I was able to defend my position in front of the tribe of {color=#f6d6bd}Creeks{/color}. They will surely listen to any negotiator who has my support."
                                        if quest_oldpagossupport == 2:
                                            text "I layed the groundwork for the future negotiations with {color=#f6d6bd}Old Págos{/color}, and as the {i}savior{/i} of this place, I may gain something extra from it."
                                        if monastery_promise:
                                            text "I made a pact with {color=#f6d6bd}the prelate{/color}. I’ll be the main link between the monastery and the officials."
                                        if iason_alliance and quest_foggy2iason_description02:
                                            text "I’m seen as “a valuable ally” in {color=#f6d6bd}Pelt of the North{/color}."
                                        if quest_greenmountainsupport == 2:
                                            text "Dealing with {color=#f6d6bd}The Tribe of The Green Mountain{/color} may be problematic, but since I got on their good side - it’s not impossible."
                                    if pc_goal == "iwanttostartanewlife":
                                        text "I want to escape my difficult past. I could make a place for myself by staying loyal to the merchant guild, or maybe pursue another opportunity while I’m here."
                                        if pc_goal_iwantnewlife_creeks:
                                            text "{color=#f6d6bd}Elah{/color} invited me to start a new life in {color=#f6d6bd}Creeks{/color}."
                                        if pc_goal_iwantnewlife_galerocks:
                                            text "{color=#f6d6bd}Severina{/color} invited me to become a rider for {color=#f6d6bd}Gale Rocks{/color}."
                                        if pc_goal_iwantnewlife_bandits:
                                            text "{color=#f6d6bd}Glaucia{/color} invited me to join her band."
                                        if pc_goal_iwantnewlife_howlersdell:
                                            text "{color=#f6d6bd}Thais{/color} invited me to join forces with her in {color=#f6d6bd}Howler’s Dell{/color}."
                                        if pc_goal_iwantnewlife_monastery:
                                            text "{color=#f6d6bd}The monks{/color} accepted my request to join their order."
                                #######
                                elif journal_quest == "quest_asterion":
                                    label _("{color=#f6d6bd}Find the Roadwarden{/color}"):
                                        style "journal_prompt"
                                    if quest_asterion_description00asterion_highisland_knowsabout:
                                        text "[quest_asterion_description00asterion_highisland_knowsabout]"
                                    if quest_asterion_description00badresult:
                                        text "[quest_asterion_description00badresult]"
                                    if quest_asterion_description00lies:
                                        text "[quest_asterion_description00lies]"
                                    if quest_asterion_description00goodresult:
                                        text "[quest_asterion_description00goodresult]"
                                    if quest_asterion_description00gaveup:
                                        text "[quest_asterion_description00gaveup]"
                                    if quest_asterion_description00asterion_highisland_knowsabout or quest_asterion_description00badresult or quest_asterion_description00lies or quest_asterion_description00goodresult or quest_asterion_description00gaveup:
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    if quest_asterion_description01:
                                        text "[quest_asterion_description01]"
                                    if quest_asterion_description01b:
                                        text "[quest_asterion_description01b]"
                                    if quest_asterion_description01c:
                                        text "[quest_asterion_description01c]"
                                    if quest_asterion_description01d:
                                        text "[quest_asterion_description01d]"
                                    if quest_asterion_description01e:
                                        text "[quest_asterion_description01e]"
                                    if world_popupnarration_highisland1:
                                        text "There’s a good chance that {color=#f6d6bd}Asterion{/color} is at {color=#f6d6bd}High Island{/color}. I need to learn how to reach this place."
                                    elif world_popupnarration_highisland0:
                                        text "There’s a good chance that {color=#f6d6bd}Asterion{/color} has disappeared on some island. I should speak with someone who knows a lot about these lands."
                                    if item_asteriontablet_read and not tulia_about_tablet:
                                        text "I found a wax tablet that could have belonged to Asterion. It’s filled with small pictures and chaotic notes focused on the construction of boats and oars. One word seems to be a name: {i}Navica{/i}."
                                    elif item_asteriontablet_read and tulia_about_tablet:
                                        text "I found a wax tablet that belonged to Asterion. It’s filled with small pictures and chaotic notes focused on the construction of boats and oars. One word seems to be a name: {i}Navica{/i}."
                                    elif galerocks_rumor_asterion:
                                        text "I heard that {color=#f6d6bd}Navica{/color} from {color=#f6d6bd}Gale Rocks{/color} used to speak {color=#f6d6bd}Asterion{/color} quite often."
                                    if asterion_highisland_clues >= 3 and highisland_howtoreach_pcknows:
                                        text "I found enough clues to believe that {color=#f6d6bd}Asterion{/color} has traveled to an island north-west of the peninsula. I should find a crew that could help me get there."
                                    if quest_asterion_description02:
                                        text "[quest_asterion_description02]"
                                    if quest_asterion_description17:
                                        text "[quest_asterion_description17]"
                                    if quest_asterion_description03:
                                        text "[quest_asterion_description03]"
                                    if quest_asterion_description04:
                                        text "[quest_asterion_description04]"
                                    if quest_asterion_description04b:
                                        text "[quest_asterion_description04b]"
                                    if quest_asterion_description04c:
                                        text "[quest_asterion_description04c]"
                                    if quest_asterion_description05:
                                        text "[quest_asterion_description05] [quest_asterion_description05b]"
                                    if quest_asterion_description06:
                                        text "[quest_asterion_description06]"
                                    if quest_asterion_description07:
                                        text "[quest_asterion_description07]"
                                    if quest_asterion_description08:
                                        text "[quest_asterion_description08]"
                                    if quest_asterion_description09:
                                        text "[quest_asterion_description09]"
                                    if quest_asterion_description16:
                                        text "[quest_asterion_description16]"
                                    if quest_asterion_description15:
                                        text "[quest_asterion_description15]"
                                    if quest_asterion_description10:
                                        text "[quest_asterion_description10]"
                                    if quest_asterion_description11a:
                                        text "[quest_asterion_description11a]"
                                    if quest_asterion_description12:
                                        text "[quest_asterion_description12]"
                                    if quest_asterion_description13:
                                        text "[quest_asterion_description13]"
                                    if quest_asterion_description14:
                                        text "[quest_asterion_description14]"
                                ########
                                elif journal_quest == "quest_gatheracrew":
                                    label _("{color=#f6d6bd}Gather a Crew{/color}"):
                                        style "journal_prompt"
                                    if quest_gatheracrew == 2:
                                        text "With the help of my crew, I was ready to start the journey."
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    elif quest_gatheracrew == 3:
                                        text "I decided to reach the island on my own."
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    text "[quest_gatheracrew_description00]"
                                    text "[quest_gatheracrew_description00a]"
                                    text "[quest_gatheracrew_description00b]"
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    if not quest_gatheracrew_description00boatgalerockssteal and not quest_gatheracrew_description00boatfishinghamlet and not quest_gatheracrew_description00boatgalerocksrent and not galerocks_navica_boat_bought:
                                        text "I also need to find a boat I could use."
                                    if quest_gatheracrew_description00boatgalerockssteal and not galerocks_navica_boat_bought:
                                        text "I could steal the boat from the shed at the northern beach."
                                    if quest_gatheracrew_description00boatfishinghamlet:
                                        text "Aegidia from the fishing hamlet is willing to lend me her boat."
                                    if quest_gatheracrew_description00boatgalerocksrent and not galerocks_navica_boat_bought:
                                        text "The villagers of Gale Rocks may sell me a boat, but it won’t be cheap."
                                    if galerocks_navica_boat_bought:
                                        text "I can use my boat that’s at the pier behind Gale Rocks."
                                    if quest_gatheracrew_description01:
                                        text "[quest_gatheracrew_description01]"
                                    if giantstatue_pray_map_learned:
                                        text "With the help of the “map” I took from the giant statue, it may be easier for me to cross the island."
                                    if aegidia_favor or aegidia_about_highisland_recruitment_done or dalit_about_highisland_recruitment_done or galerocks_navica_about_highisland_recruitment_done or thyrsus_orentius_debt_achieved or (pyrrhos_debt == 1 and not pyrrhos_dead) or (shortcut_darkforest_bandit_promisedtocoverforhim and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_fled) or thais_about_highisland_recruitment_done or tulia_about_highisland_recruited or foragers_about_gatherthecrew_tzvi_recruited or (quintus_alive == 1 and quintus_left_gate < day):
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    if aegidia_favor:
                                        text "{color=#f6d6bd}Aegidia{/color} owes me a favor."
                                    elif aegidia_about_highisland_recruitment_done:
                                        text "I recruited {color=#f6d6bd}Aegidia{/color}."
                                    if dalit_about_highisland_recruitment_done:
                                        text "I hired {color=#f6d6bd}Dalit{/color}."
                                    if galerocks_navica_about_highisland_recruitment_done:
                                        text "I recruited {color=#f6d6bd}Navica{/color}."
                                    if thyrsus_orentius_debt_achieved:
                                        text "{color=#f6d6bd}Orentius{/color} owes me a favor."
                                    if pyrrhos_debt == 1 and not pyrrhos_dead:
                                        text "{color=#f6d6bd}Pyrrhos{/color} owes me a favor."
                                    if shortcut_darkforest_bandit_promisedtocoverforhim and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_fled:
                                        text "{color=#f6d6bd}The runaway bandit{/color} owes me a favor."
                                    if thais_about_highisland_recruitment_done:
                                        text "{color=#f6d6bd}Thais{/color} agreed to send with me a few guards, though I can either take an entire group, or none of them."
                                    # if tulia_about_bandits_indebt:
                                    #     text "I recruited {color=#f6d6bd}Tulia{/color}."
                                    if tulia_about_highisland_recruited and asterion_lie:
                                        text "{color=#6a6a6a}I can’t take Tulia with me now that I’ve lied to her.{/color}"
                                    elif tulia_about_highisland_recruited:
                                        text "I recruited {color=#f6d6bd}Tulia{/color}."
                                    if foragers_about_gatherthecrew_tzvi_recruited:
                                        text "I hired {color=#f6d6bd}Tzvi{/color}."
                                    if quintus_alive == 1 and quintus_left_gate and quintus_left_gate < day:
                                        text "{color=#f6d6bd}Quintus{/color} owes me a favor."
                                ########
                                elif journal_quest == "quest_birdhunting":
                                    label _("{color=#f6d6bd}The Bird Hunting{/color}"):
                                        style "journal_prompt"
                                    text "[quest_birdhunting_description00]"
                                    if quest_birdhunting_description01:
                                        text "They want to leave no sooner than on day [foragers_quest_daythreshold], but I should leave with them as early as I can, some day before afternoon, while the bird is still around."
                                    else:
                                        text "If I’m interested, I should get in touch with them rather sooner than later, some day before afternoon, while the bird is still around."
                                    if quest_birdhunting_description02:
                                        text "[quest_birdhunting_description02]"
                                    if quest_birdhunting_description03:
                                        text "[quest_birdhunting_description03]"
                                    if quest_birdhunting_description04:
                                        text "[quest_birdhunting_description04]"
                                    if quest_birdhunting_description05:
                                        text "[quest_birdhunting_description05]"
                                    if quest_birdhunting_description06:
                                        text "[quest_birdhunting_description06]"
                                    if quest_birdhunting_description07:
                                        text "[quest_birdhunting_description07]"
                                    if quest_birdhunting_description08:
                                        text "[quest_birdhunting_description08]"
                                ########
                                elif journal_quest == "quest_foggy1oldpagos":
                                    label _("{color=#f6d6bd}Check on Old Págos{/color}"):
                                        style "journal_prompt"
                                    text "[quest_foggy1oldpagos_description00]"
                                    if oldpagos_plague_known:
                                        text "I’ve learned that the villagers are isolating themselves because of the plague that has smitten them. I should bring the news to {color=#f6d6bd}Foggy{/color}."
                                    if quest_foggy1oldpagos_description01:
                                        text "[quest_foggy1oldpagos_description01]"
                                ########
                                elif journal_quest == "quest_foggy2iason":
                                    label _("{color=#f6d6bd}Check on Iason{/color}"):
                                        style "journal_prompt"
                                    text "[quest_foggy2iason_description00]"
                                    if quest_foggy2iason_description01:
                                        text "[quest_foggy2iason_description01]"
                                    if quest_foggy2iason_description02:
                                        text "[quest_foggy2iason_description02]"
                                    if quest_foggy2iason_description02a:
                                        text "[quest_foggy2iason_description02a]"
                                    if quest_foggy2iason_description03:
                                        text "[quest_foggy2iason_description03]"
                                    if quest_foggy2iason_description04:
                                        text "[quest_foggy2iason_description04]"
                                    if not quest_foggy2iason_description01 and peltnorth_ban_perm:
                                        text "I won’t be able to deliver the message. I should speak report back to Foggy."
                                ########
                                elif journal_quest == "quest_foggy3whitemarshes":
                                    label _("{color=#f6d6bd}The Cask of Cider{/color}"):
                                        style "journal_prompt"
                                    text "[quest_foggy3whitemarshes_description00]"
                                    if quest_foggy3whitemarshes_description01:
                                        text "[quest_foggy3whitemarshes_description01]"
                                    if quest_foggy3whitemarshes_description02:
                                        text "[quest_foggy3whitemarshes_description02]"
                                    if quest_foggy3whitemarshes_description03:
                                        text "[quest_foggy3whitemarshes_description03]"
                                    if quest_foggy3whitemarshes_description04:
                                        text "[quest_foggy3whitemarshes_description04]"
                                    if quest_foggy3whitemarshes_description05:
                                        text "[quest_foggy3whitemarshes_description05]"
                                    if quest_foggy3whitemarshes_description06:
                                        text "[quest_foggy3whitemarshes_description06]"
                                    if quest_foggy3whitemarshes_description07:
                                        text "[quest_foggy3whitemarshes_description07]"
                                ########
                                elif journal_quest == "quest_closedtunnel":
                                    label _("{color=#f6d6bd}The Closed Tunnel{/color}"):
                                        style "journal_prompt"
                                    if quest_closedtunnel_description00:
                                        text "[quest_closedtunnel_description00]"
                                    if quest_closedtunnel_description01a:
                                        text "[quest_closedtunnel_description01a]"
                                    if quest_closedtunnel_description02:
                                        text "[quest_closedtunnel_description02]"
                                    if quest_closedtunnel_description03:
                                        text "[quest_closedtunnel_description03]"
                                    if quest_closedtunnel_description04:
                                        text "[quest_closedtunnel_description04]"
                                    if quest_closedtunnel_description01:
                                        if quest_closedtunnel_description01a or quest_closedtunnel_description02 or quest_closedtunnel_description03:
                                            text "{color=#6a6a6a}[quest_closedtunnel_description01]{/color}"
                                        elif quest_closedtunnel_description01:
                                            text "[quest_closedtunnel_description01]"
                                ########
                                elif journal_quest == "quest_cursedcoins":
                                    label _("{color=#f6d6bd}The Cursed Coins{/color}"):
                                        style "journal_prompt"
                                    text "{color=#f6d6bd}Navica{/color} from {color=#f6d6bd}Gale Rocks{/color} asked me to get rid of the coins she received for reaching {color=#f6d6bd}High Island{/color}. To do so, I need to ride to {color=#f6d6bd}Beholder{/color}, the tree south of {color=#f6d6bd}Howler’s Dell{/color}, and place the pouch on the altar."
                                    if quest_cursedcoins_description01:
                                        text "I decided to keep the coins to myself, but I can still lie to their owner."
                                    if quest_cursedcoins_description02:
                                        text "I decided to keep the coins to myself, and to forget about the whole thing."
                                    if quest_cursedcoins_description03:
                                        text "I did as she asked, but the coins seem fine. I kept them to myself, and should now return to {color=#f6d6bd}Navica{/color}."
                                    if quest_cursedcoins_description04:
                                        text "I got rid of the coins for good. I should return to {color=#f6d6bd}Navica{/color}."
                                    if quest_cursedcoins_description05:
                                        text "{color=#f6d6bd}Navica{/color} agreed to join my crew."
                                ########
                                elif journal_quest == "quest_easternpath":
                                    label _("{color=#f6d6bd}The Eastern Path{/color}"):
                                        style "journal_prompt"
                                    if quest_easternpath_description_final:
                                        text "[quest_easternpath_description_final]"
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    if quest_easternpath_description00:
                                        text "[quest_easternpath_description00]"
                                    if quest_easternpath_description01:
                                        text "[quest_easternpath_description01]"
                                    if quest_easternpath_description02:
                                        text "[quest_easternpath_description02]"
                                    if quest_easternpath_description03 and not quest_easternpath_description03a:
                                        text "[quest_easternpath_description03]"
                                    elif quest_easternpath_description03a:
                                        text "{color=#6a6a6a}[quest_easternpath_description03a]{/color}"
                                    if quest_easternpath_description03alt and not quest_easternpath_description03aalt:
                                        text "[quest_easternpath_description03alt]"
                                    elif quest_easternpath_description03aalt:
                                        text "{color=#6a6a6a}[quest_easternpath_description03aalt]{/color}"
                                    if quest_easternpath_description05 and not quest_easternpath_description05a:
                                        text "[quest_easternpath_description05]"
                                    elif quest_easternpath_description05a:
                                        text "{color=#6a6a6a}[quest_easternpath_description05a]{/color}"
                                    if quest_easternpath_description06 and not quest_easternpath_description06a:
                                        text "[quest_easternpath_description06]"
                                    elif quest_easternpath_description06a and not quest_easternpath_description06alt:
                                        text "[quest_easternpath_description06a]"
                                    elif quest_easternpath_description06alt and not quest_easternpath_description06aalt:
                                        text "[quest_easternpath_description06alt]"
                                    elif quest_easternpath_description06aalt:
                                        text "{color=#6a6a6a}[quest_easternpath_description06aalt]{/color}"
                                    if quest_easternpath_description07 and not quest_easternpath_description07a:
                                        text "[quest_easternpath_description07]"
                                    elif quest_easternpath_description07a:
                                        text "{color=#6a6a6a}[quest_easternpath_description07a]{/color}"
                                    if quest_easternpath_description08 and not quest_easternpath_description08a:
                                        text "[quest_easternpath_description08]"
                                    elif quest_easternpath_description08a:
                                        text "{color=#6a6a6a}[quest_easternpath_description08a]{/color}"
                                    if quest_easternpath_description09 and not quest_easternpath_description09a:
                                        text "[quest_easternpath_description09]"
                                    elif quest_easternpath_description09a and not quest_easternpath_description09aa and creeks_mundanework:
                                        text "{color=#6a6a6a}[quest_easternpath_description09a] I could also complete a few mundane patrols for the village.{/color}"
                                    elif quest_easternpath_description09a and not quest_easternpath_description09aa:
                                        text "{color=#6a6a6a}[quest_easternpath_description09a]{/color}"
                                    elif quest_easternpath_description09aa:
                                        text "{color=#6a6a6a}[quest_easternpath_description09aa]{/color}"
                                    if quest_easternpath_description11:
                                        text "[quest_easternpath_description11]"
                                    if quest_easternpath_description13:
                                        text "[quest_easternpath_description13]"
                                    if quest_easternpath_description10 and not quest_easternpath_description10a:
                                        text "[quest_easternpath_description10]"
                                    elif quest_easternpath_description10a:
                                        text "{color=#6a6a6a}[quest_easternpath_description10a]{/color}"
                                    if quest_easternpath_description04 and not quest_easternpath_description04a:
                                        text "[quest_easternpath_description04]"
                                    elif quest_easternpath_description04a:
                                        text "{color=#6a6a6a}[quest_easternpath_description04a]{/color}"
                                    if quest_easternpath_description_teaser and not quest_easternpath_description10 and not quest_easternpath_description01:
                                        text "[quest_easternpath_description_teaser]"
                                    elif quest_easternpath_description_teaser:
                                        text "{color=#6a6a6a}[quest_easternpath_description_teaser]{/color}"
                                    if quest_easternpath_description00 and not quest_easternpath_description01:
                                        text "[quest_easternpath_description00]"
                                    elif quest_easternpath_description00:
                                        text "{color=#6a6a6a}[quest_easternpath_description00]{/color}"
                                ########
                                elif journal_quest == "quest_empresscarp":
                                    label _("{color=#f6d6bd}An Empress Carp{/color}"):
                                        style "journal_prompt"
                                    text "[quest_empresscarp_description00]"
                                    text "[quest_empresscarp_description00b]"
                                    if item_empresscarp:
                                        text "I have the fish."
                                    if quest_empresscarp_description01:
                                        text "[quest_empresscarp_description01]"
                                ########
                                elif journal_quest == "quest_escortpyrrhos":
                                    label _("{color=#f6d6bd}Escort The Scavenger{/color}"):
                                        style "journal_prompt"
                                    if quest_escortpyrrhos_description01:
                                        text "On day [pyrrhos_quest_counter], I met {color=#f6d6bd}a scavenger{/color} in {color=#f6d6bd}the ruined village{/color} at the southern road. He wants me to escort him to the village of {color=#f6d6bd}Howler’s Dell{/color}."
                                        text "He needs another day to gather his things and prepare the iron he’s gathered. He asked me to return tomorrow, at least three hours before the dusk, but before I do, I need to make sure that the route leading to {color=#f6d6bd}Howler’s Dell{/color} isn’t blocked by obstacles."
                                    if ruinedvillage_firsttime and beholder_firsttime and howlersdell_firsttime:
                                        text "I know the road from the ruined village to Howler's Dell. It’s safe."
                                    if quest_escortpyrrhos_description02:
                                        text "[quest_escortpyrrhos_description02]"
                                    if quest_escortpyrrhos_description03:
                                        text "[quest_escortpyrrhos_description03]"
                                    if quest_escortpyrrhos_description04:
                                        text "[quest_escortpyrrhos_description04]"
                                    if quest_escortpyrrhos_description05:
                                        text "[quest_escortpyrrhos_description05]"
                                    if quest_escortpyrrhos_description06:
                                        text "[quest_escortpyrrhos_description06]"
                                ########
                                elif journal_quest == "quest_fallentree":
                                    label _("{color=#f6d6bd}The Fallen Tree{/color}"):
                                        style "journal_prompt"
                                    text "[quest_fallentree_description00]"
                                    if quest_fallentree_description01:
                                        text "I think that the tree [fallentree_investigated_opinion01]. The cart, [fallentree_investigated_opinion03], [fallentree_investigated_opinion02]. Its owners [fallentree_investigated_opinion04]."
                                    if quest_fallentree_description02:
                                        text "[quest_fallentree_description02]"
                                    if quest_fallentree_description03:
                                        text "[quest_fallentree_description03]"
                                    if quest_fallentree_description04:
                                        text "[quest_fallentree_description04]"
                                    if quest_fallentree_description05:
                                        text "[quest_fallentree_description05]"
                                    if quest_fallentree_description06:
                                        text "[quest_fallentree_description06]"
                                ########
                                elif journal_quest == "quest_fetchingfood":
                                    label _("{color=#f6d6bd}Fetching Food{/color}"):
                                        style "journal_prompt"
                                    text "{color=#f6d6bd}Quintus{/color} won’t let me use the gate he keeps unless I bring him [quintus_food_gate_amount] food rations first."
                                    if quest_fetchingfood_description01:
                                        text "[quest_fetchingfood_description01]"
                                ########
                                elif journal_quest == "quest_eudociaflower":
                                    label _("{color=#f6d6bd}Flowers for Eudocia{/color}"):
                                        style "journal_prompt"
                                    text "[quest_eudociaflower_description00]"
                                    if quest_eudociaflower_description01:
                                        text "[quest_eudociaflower_description01]"
                                    if item_snakebait:
                                        text "I found the flowers."
                                    if quest_eudociaflower_description03:
                                        text "[quest_eudociaflower_description03]"
                                    if quest_eudociaflower_description04:
                                        text "[quest_eudociaflower_description04]"
                                ########
                                elif journal_quest == "quest_thyrsusgift":
                                    label _("{color=#f6d6bd}Thyrsus’ Wand{/color}"):
                                        style "journal_prompt"
                                    text "[quest_thyrsusgift_description00]"
                                    if quest_thyrsusgift == 2:
                                        text "[quest_thyrsusgift_description_successdescription]"
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    if quest_thyrsusgift >= 3:
                                        text "[quest_thyrsusgift_description_faildescription]"
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    if quest_thyrsusgift_description05:
                                        text "[quest_thyrsusgift_description05]"
                                    if quest_thyrsusgift_description04:
                                        text "[quest_thyrsusgift_description04]"
                                    if quest_thyrsusgift_description03:
                                        text "[quest_thyrsusgift_description03]"
                                    if quest_thyrsusgift_description02:
                                        text "[quest_thyrsusgift_description02]"
                                    if quest_thyrsusgift_description01:
                                        text "[quest_thyrsusgift_description01]"
                                ########
                                elif journal_quest == "quest_intelforpeltnorth":
                                    label _("{color=#f6d6bd}Glaucia’s Band{/color}"):
                                        style "journal_prompt"
                                    if quest_intelforpeltnorth_description08:
                                        text "[quest_intelforpeltnorth_description08]"
                                    if quest_intelforpeltnorth_description08 and quest_intelforpeltnorth_description10:
                                        text "[quest_intelforpeltnorth_description10]"
                                    if quest_intelforpeltnorth == 3 and peltnorth_ban_perm:
                                        text "I won’t be able to speak with the innkeeper anymore."
                                    if quest_intelforpeltnorth_description08 or quest_intelforpeltnorth_description10:
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    elif quest_intelforpeltnorth == 3 and peltnorth_ban_perm:
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    if quest_intelforpeltnorth_description01:
                                        text "[quest_intelforpeltnorth_description01]"
                                    if quest_intelforpeltnorth_description02:
                                        text "[quest_intelforpeltnorth_description02]"
                                    if quest_intelforpeltnorth_description02b:
                                        text "[quest_intelforpeltnorth_description02b]"
                                    if quest_intelforpeltnorth_description03:
                                        text "[quest_intelforpeltnorth_description03]"
                                    if quest_intelforpeltnorth_description04:
                                        text "[quest_intelforpeltnorth_description04]"
                                    if quest_intelforpeltnorth_description04a:
                                        text "[quest_intelforpeltnorth_description04a]"
                                    if quest_intelforpeltnorth_description04b:
                                        text "[quest_intelforpeltnorth_description04b]"
                                    if quest_intelforpeltnorth_description04c:
                                        text "[quest_intelforpeltnorth_description04c]"
                                    if quest_intelforpeltnorth_description05:
                                        text "[quest_intelforpeltnorth_description05]"
                                    if quest_intelforpeltnorth_description06:
                                        text "[quest_intelforpeltnorth_description06]"
                                    if quest_intelforpeltnorth_description07:
                                        text "[quest_intelforpeltnorth_description07]"
                                ########
                                elif journal_quest == "quest_bronzerod":
                                    label _("{color=#f6d6bd}Bronze Rods{/color}"):
                                        style "journal_prompt"
                                    if quest_bronzerod_description03:
                                        text "[quest_bronzerod_description03]"
                                    if quest_bronzerod_description04:
                                        text "[quest_bronzerod_description04]"
                                    if quest_bronzerod_description05:
                                        text "[quest_bronzerod_description05]"
                                    if quest_bronzerod_description06:
                                        text "[quest_bronzerod_description06]"
                                    if quest_bronzerod_description07:
                                        text "[quest_bronzerod_description07]"
                                    if quest_bronzerod_description08:
                                        text "[quest_bronzerod_description08]"
                                    if quest_bronzerod_description03 or quest_bronzerod_description04 or quest_bronzerod_description05 or quest_bronzerod_description06 or quest_bronzerod_description07 or quest_bronzerod_description08:
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    text "[quest_bronzerod_description00]"
                                    text "[quest_bronzerod_description00b]"
                                    if quest_bronzerod_description02 and not eudocia_bronzerod_rodin_whitemarshes:
                                        text "[quest_bronzerod_description02]"
                                    if eudocia_bronzerod_rodin_whitemarshes:
                                        text "I’ve placed a rod in {color=#f6d6bd}White Marshes{/color}."
                                    elif whitemarshes_attacked or whitemarshes_destroyed:
                                        text "I won’t have a chance to place a rod in {color=#f6d6bd}White Marshes{/color}."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    text "[quest_bronzerod_description00c] I’ve already placed [eudocia_bronzerod_installed]. I currently have [item_bronzerod]."
                                    if eudocia_bronzerod_rodin_watchtower:
                                        text "I’ve placed a rod on the abandoned {color=#f6d6bd}watchtower{/color}."
                                    if eudocia_bronzerod_rodin_southerncrossroads:
                                        text "I’ve placed a rod at {color=#f6d6bd}the southern crossroads{/color}."
                                    if eudocia_bronzerod_rodin_shortcut:
                                        text "I’ve placed a rod in {color=#f6d6bd}the heart of the woods{/color}."
                                    if eudocia_bronzerod_rodin_peltnorth:
                                        text "I’ve placed a rod in {color=#f6d6bd}Pelt of the North{/color}."
                                    if eudocia_bronzerod_rodin_druidcave:
                                        text "I’ve placed a rod in the hills above {color=#f6d6bd}the druids’ cave{/color}."
                                    if eudocia_bronzerod_rodin_creeks:
                                        text "I’ve placed a rod in the village of {color=#f6d6bd}Creeks{/color}."
                                    if eudocia_bronzerod_rodin_mountainroad:
                                        text "I’ve placed a rod {color=#f6d6bd}in the eastern mountains{/color}."
                                    if eudocia_bronzerod_rodin_oldtunnel:
                                        text "I’ve placed a rod at {color=#f6d6bd}the entrance to an old tunnel{/color} in the north."
                                    if eudocia_bronzerod_rodin_howlersdell:
                                        text "I’ve placed a rod in {color=#f6d6bd}Howler’s Dell{/color}."
                                    if eudocia_bronzerod_rodin_westgate:
                                        text "I’ve placed a rod at {color=#f6d6bd}the gate on the western road{/color}."
                                    if aeli_about_bronzerod and aeli_about_bronzerod_ignored:
                                        text "I’ve placed a rod in the mountains close to {color=#f6d6bd}the monastery{/color}."
                                    if thais_about_bronzerod_allowed < 0:
                                        text "{color=#6a6a6a}I was forbidden to place a rod in Howler’s Dell.{/color}"
                                    if aeli_about_bronzerod and not aeli_about_bronzerod_ignored:
                                        text "{color=#6a6a6a}I was forbidden to place a rod in the monastery.{/color}"
                                ########
                                elif journal_quest == "quest_healingtheplague":
                                    label _("{color=#f6d6bd}Healing the Plague{/color}"):
                                        style "journal_prompt"
                                    if quest_healingtheplague_description07:
                                        text "[quest_healingtheplague_description07]"
                                    if quest_healingtheplague_description08:
                                        text "[quest_healingtheplague_description08]"
                                    if quest_healingtheplague_description07 or quest_healingtheplague_description08:
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    if quest_healingtheplague_description03 and item_magicfruit:
                                        text "[quest_healingtheplague_description03]"
                                    if quest_healingtheplague_description04 and pc_foodmagicfruit:
                                        text "[quest_healingtheplague_description04]"
                                    if quest_healingtheplague_description04alt and item_magicfruit_lost:
                                        text "[quest_healingtheplague_description04alt]"
                                    if quest_healingtheplague_description05:
                                        text "[quest_healingtheplague_description05]"
                                    if (quest_healingtheplague_description03 and item_magicfruit) or (quest_healingtheplague_description04 and pc_foodmagicfruit) or (quest_healingtheplague_description04alt and item_magicfruit_lost) or quest_healingtheplague_description05:
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    if quest_healingtheplague_description01:
                                        text "[quest_healingtheplague_description01]"
                                    if quest_healingtheplague_description02:
                                        text "[quest_healingtheplague_description02]"
                                    if quest_healingtheplague_description_pre or quest_healingtheplague_description00:
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    if quest_healingtheplague_description_pre:
                                        text "[quest_healingtheplague_description_pre]"
                                    if quest_healingtheplague_description00 and not quest_healingtheplague_description01:
                                        text "[quest_healingtheplague_description00]"
                                    elif quest_healingtheplague_description00 and quest_healingtheplague_description01:
                                        text "{color=#6a6a6a}[quest_healingtheplague_description00]{/color}"
                                ########
                                elif journal_quest == "quest_matchmaking":
                                    label _("{color=#f6d6bd}Matchmaking{/color}"):
                                        style "journal_prompt"
                                    text "[quest_matchmaking_description00]"
                                    if howlersdell_timo_firsttime and not howlersdell_timo_matched:
                                        text "{color=#f6d6bd}Timo{/color} from {color=#f6d6bd}Howler’s Dell{/color} looks for a hard-working man who’d like to marry her according to the traditions of her ancestors, then either move in with her, or take her to a new home."
                                    elif howlersdell_timo_firsttime and howlersdell_timo_matched:
                                        text "{color=#6a6a6a}I’ve helped Timo from Howler’s Dell find her match.{/color}"
                                    if galerocks_singlepeople_firsttime and not galerocks_singlepeople_paulus_matched:
                                        text "{color=#f6d6bd}Paulus{/color} from {color=#f6d6bd}Gale Rocks{/color} seeks a new home, and is willing to work hard to help his future wife take care of their children."
                                    elif galerocks_singlepeople_firsttime and galerocks_singlepeople_paulus_matched:
                                        text "{color=#6a6a6a}I’ve helped Paulus from Gale Rocks find his match.{/color}"
                                    if galerocks_singlepeople_firsttime and not galerocks_singlepeople_marina_notmatched:
                                        text "{color=#f6d6bd}Marina{/color} from {color=#f6d6bd}Gale Rocks{/color} seeks someone willing to move in with her and her son, but is only interested in Wright’s followers."
                                    elif galerocks_singlepeople_firsttime and galerocks_singlepeople_marina_notmatched:
                                        text "{color=#6a6a6a}Marina from Gale Rocks is no longer looking for a match.{/color}"
                                    if shoshi_single and not shoshi_notmatched:
                                        text "{color=#f6d6bd}Shoshi{/color} from {color=#f6d6bd}Creeks{/color} looks for a safe, slow life with a woman who lives in another village and is interested in keeping their relationship open."
                                    elif shoshi_single and shoshi_notmatched:
                                        text "{color=#6a6a6a}Shoshi from Creeks would rather wait for another year or two.{/color}"
                                    if whitemarshes_about_matchmaking:
                                        text "{color=#6a6a6a}The tribe of White Marshes seeks no spouses.{/color}"
                                    if oldpagos_about_matchmaking:
                                        text "{color=#6a6a6a}The tribe of Old Págos seeks no spouses.{/color}"
                                    if quest_matchmaking == 2:
                                        text "[quest_matchmaking_description00b]"
                                ########
                                elif journal_quest == "quest_hiddenpurse":
                                    label _("{color=#f6d6bd}A Hidden Pouch{/color}"):
                                        style "journal_prompt"
                                    text "[quest_hiddenpurse_description00]"
                                    if quest_hiddenpurse_description00a:
                                        text "[quest_hiddenpurse_description00a]"
                                    if quest_hiddenpurse_description01:
                                        text "[quest_hiddenpurse_description01]"
                                    if quest_hiddenpurse_description02:
                                        text "[quest_hiddenpurse_description02]"
                                    if quest_hiddenpurse_description03:
                                        text "[quest_hiddenpurse_description03]"
                                    if quest_hiddenpurse_description04:
                                        text "[quest_hiddenpurse_description04]"
                                ########
                                elif journal_quest == "quest_lostmerchants":
                                    label _("{color=#f6d6bd}The Lost Merchants{/color}"):
                                        style "journal_prompt"
                                    if quest_lostmerchants_description00:
                                        text "[quest_lostmerchants_description00]"
                                    if quest_lostmerchants_description01:
                                        text "[quest_lostmerchants_description01]"
                                    if quest_lostmerchants_description02:
                                        text "[quest_lostmerchants_description02]"
                                    if quest_lostmerchants_description03:
                                        text "[quest_lostmerchants_description03]"
                                ########
                                elif journal_quest == "quest_healingpotion":
                                    label _("{color=#f6d6bd}Merchant’s Medicament{/color}"):
                                        style "journal_prompt"
                                    if quest_healingpotion_description03:
                                        text "[quest_healingpotion_description03]"
                                    if quest_healingpotion_description04:
                                        text "[quest_healingpotion_description04]"
                                    if akakios_quest_healingpotion_deadline < day:
                                        text "I’m out of time. I should return to the merchant."
                                    if quest_healingpotion_description05:
                                        text "[quest_healingpotion_description05]"
                                    if quest_healingpotion_description03 or quest_healingpotion_description04 or akakios_quest_healingpotion_deadline < day or quest_healingpotion_description05:
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    if quest_healingpotion_description01:
                                        text "[quest_healingpotion_description01]"
                                    if quest_healingpotion_description02:
                                        text "[quest_healingpotion_description02]"
                                    if quest_healingpotion_description01 or quest_healingpotion_description02:
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    text "{color=#f6d6bd}Akakios{/color}, a merchant from {color=#f6d6bd}Howler’s Dell{/color}, is looking for a healing potion. I need to deliver it to him on day [akakios_quest_healingpotion_deadline], or earlier."
                                    if quest_healingpotion_description00b:
                                        text "[quest_healingpotion_description00b]"
                                    if quest_healingpotion_description00c:
                                        text "[quest_healingpotion_description00c]"
                                    if quest_healingpotion_description00d:
                                        text "[quest_healingpotion_description00d]"
                                    if quest_healingpotion_description00d_alt:
                                        text "[quest_healingpotion_description00d_alt]"

                                    if quest_healingpotion_description00d_alt2:
                                        text "[quest_healingpotion_description00d_alt2]"


                                # ########
                                # elif journal_quest == "quest_messageseverina_description_akakios":
                                #     label _("{color=#f6d6bd}Message To Akakios{/color}"):
                                #         style "journal_prompt"
                                #     if quest_messageseverina_description_akakios00:
                                #         text "[quest_messageseverina_description_akakios00]"
                                #     if quest_messageseverina_description_akakios01:
                                #         text "[quest_messageseverina_description_akakios01]"
                                #     if quest_messageseverina_description_akakios02:
                                #         text "[quest_messageseverina_description_akakios02]"
                                #     if quest_messageseverina_description_akakios03:
                                #         text "[quest_messageseverina_description_akakios03]"
                                ########
                                elif journal_quest == "quest_missinghunters":
                                    label _("{color=#f6d6bd}The Missing Hunters{/color}"):
                                        style "journal_prompt"
                                    if quest_missinghunters_description01:
                                        text "[quest_missinghunters_description01]"
                                    if quest_missinghunters_description02:
                                        text "[quest_missinghunters_description02]"
                                    if quest_missinghunters_description03:
                                        text "[quest_missinghunters_description03]"
                                    if quest_missinghunters_description01 or quest_missinghunters_description02 or quest_missinghunters_description03:
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    text "[quest_missinghunters_description00]"
                                    if not quest_missinghunters_reported:
                                        text "I still have to find all three of the hunters."
                                    elif quest_missinghunters_reported == 1:
                                        text "I brought back the news about one of the hunters."
                                    elif quest_missinghunters_reported == 2:
                                        text "I brought back the news about two of the hunters."
                                    if quest_missinghunters_admonfound or quest_missinghunters_daliafound or quest_missinghunters_vaschelfound:
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    if quest_missinghunters_admonfound == 1 and quest_missinghunters_admonknown:
                                        text "I found the hunter known as {color=#f6d6bd}Admon{/color}. I should share the news with {color=#f6d6bd}Efren{/color}."
                                    elif quest_missinghunters_admonfound == 3:
                                        text "I delivered the news about the hunter named {color=#f6d6bd}Admon{/color}, though I had no evidence with me to show."
                                    elif quest_missinghunters_admonfound == 2:
                                        text "I delivered the news about the hunter named {color=#f6d6bd}Admon{/color} and had evidence to back up my words."
                                    elif quest_missinghunters_admonfound == 4:
                                        text "I shared what I know about the hunter named {color=#f6d6bd}Admon{/color}, but I’m not sure I know the truth."
                                    if quest_missinghunters_daliafound == 1 and quest_missinghunters_daliaknown:
                                        text "I found the huntress known as {color=#f6d6bd}Dalia{/color}. I should share the news with {color=#f6d6bd}Efren{/color}."
                                    elif quest_missinghunters_daliafound == 3:
                                        text "I delivered the news about the huntress named {color=#f6d6bd}Dalia{/color}, though I had no evidence with me to show."
                                    elif quest_missinghunters_daliafound == 2:
                                        text "I delivered the news about the huntress named {color=#f6d6bd}Dalia{/color} and had evidence to back up my words."
                                    elif quest_missinghunters_daliafound == 4:
                                        text "I shared what I know about the huntress named {color=#f6d6bd}Dalia{/color}, but I’m not sure I know the truth."
                                    if quest_missinghunters_vaschelfound == 1 and quest_missinghunters_vaschelknown:
                                        text "I found the hunt person known as {color=#f6d6bd}Vaschel{/color}. I should share the news with {color=#f6d6bd}Efren{/color}."
                                    elif quest_missinghunters_vaschelfound == 3:
                                        text "I delivered the news about the hunt person named {color=#f6d6bd}Vaschel{/color}, though I had no evidence with me to show."
                                    elif quest_missinghunters_vaschelfound == 2:
                                        text "I delivered the news about the hunt person named {color=#f6d6bd}Vaschel{/color} and had evidence to back up my words."
                                    elif quest_missinghunters_vaschelfound == 4:
                                        text "I shared what I know about the hunt person named {color=#f6d6bd}Vaschel{/color}, but I’m not sure I know the truth."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    text "{color=#f6d6bd}Efren{/color} on {color=#f6d6bd}Admon{/color}: “He’s a man who seeks paths and challenges.” He believes that seeking knowledge of the peninsula will bring the tribe ways to survive hardships. “He was, {i}is{/i} smaller than the others, and knows more ‘bout dressing the wild game than any of us. His arms are small, so he often places traps. His hair is a bit darker than {color=#f6d6bd}Dalia’s{/color}, but short, just like his beard.”"
                                    text "{color=#f6d6bd}Efren{/color} on {color=#f6d6bd}Dalia{/color}: “She’ the bravest of them, with strong legs. She has simple ways and looks for beasts in the open, by the roads. Her hair is light, always tied in a single braid.”"
                                    text "{color=#f6d6bd}Efren{/color} on {color=#f6d6bd}Vaschel{/color}: “Isn’t a man, though they were born with a prick,” and “wears browns and greens to blend in with the trees. They hunt like a gargoyle, hiding among leaves, jumping at a creature when it gets close.” Because of that, they have often roamed in the woods, even those that are far away from the village."
                                ########
                                elif journal_quest == "quest_runaway":
                                    label _("{color=#f6d6bd}The Runaway{/color}"):
                                        style "journal_prompt"
                                    if not shortcut_darkforest_bandit:
                                        text "According to {color=#f6d6bd}Glaucia{/color}, he’s “a young, strong lad, with the pretty face and blue eyes of a beaten puppy. The last togs he had on his back was our black gambeson, matching his short hair, but if he has any wits, he sold it somewhere already. Shaves often.”"
                                    elif shortcut_darkforest_bandit:
                                        text "According to {color=#f6d6bd}Glaucia{/color}, he’s “a young, strong lad, with the pretty face and blue eyes of a beaten puppy. The last togs he had on his back was our black gambeson, matching his short hair, but if he has any wits, he sold it somewhere already. Shaves often.”"
                                        text "I saw a man who matches this description. I should speak with {color=#f6d6bd}Glaucia{/color} about it."
                                    if quest_runaway_description01:
                                        text "[quest_runaway_description01]"
                                    if quest_runaway_description02:
                                        text "[quest_runaway_description02]"
                                    if quest_runaway == 3 and not banditshideout_banned:
                                        text "I refused to accept her request."
                                    if quest_runaway == 3 and banditshideout_banned:
                                        text "I won’t be able to return to her camp."
                                ########
                                elif journal_quest == "quest_spiritrock":
                                    label _("{color=#f6d6bd}A Spirit Rock{/color}"):
                                        style "journal_prompt"
                                    text "[quest_spiritrock_description00]"
                                    if eudocia_about_spiritrock_problem:
                                        text "[quest_spiritrock_description02]"
                                    if item_spiritrock:
                                        text "[quest_spiritrock_description03]"
                                    if quest_spiritrock_description04:
                                        text "[quest_spiritrock_description04]"
                                    if (galerocks_photios_quest_spiritrock_about_phoibe_after and galerocks_phoibe_coma) or galerocks_phoibe_coma_knowsabout:
                                        text "It seems like the stone not only didn’t help {color=#f6d6bd}Phoibe{/color}, but also put her into coma."
                                ########
                                elif journal_quest == "quest_spyonwhitemarshes":
                                    label _("{color=#f6d6bd}Spy on White Marshes{/color}"):
                                        style "journal_prompt"
                                    if quest_spyonwhitemarshes_description01:
                                        text "[quest_spyonwhitemarshes_description01]"
                                    if whitemarshes_nomoreundead:
                                        text "Since the undead are no longer, I should report back to {color=#f6d6bd}Glaucia{/color}."
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    if quest_spyonwhitemarshes_description01a:
                                        text "[quest_spyonwhitemarshes_description01a]"
                                    if whitemarshes_spying_completed:
                                        text "I’ve learned quite a bit. I can report back to her."
                                    if quest_spyonwhitemarshes_description02:
                                        text "[quest_spyonwhitemarshes_description02]"
                                    if quest_spyonwhitemarshes_description03:
                                        text "[quest_spyonwhitemarshes_description03]"
                                    if quest_spyonwhitemarshes_description04:
                                        text "[quest_spyonwhitemarshes_description04]"
                                ########
                                elif journal_quest == "quest_fisherhamlet":
                                    label _("{color=#f6d6bd}The Old Hamlet{/color}"):
                                        style "journal_prompt"
                                    if quest_fisherhamlet_description07:
                                        text "[quest_fisherhamlet_description07]"
                                    if quest_fisherhamlet_description08:
                                        text "[quest_fisherhamlet_description08]"
                                    if quest_fisherhamlet_description09:
                                        text "[quest_fisherhamlet_description09]"
                                    if quest_fisherhamlet_description10:
                                        text "[quest_fisherhamlet_description10]"
                                    if quest_fisherhamlet_description11:
                                        text "[quest_fisherhamlet_description11]"
                                    if quest_fisherhamlet_description12:
                                        text "[quest_fisherhamlet_description12]"
                                    if quest_fisherhamlet_description07 or quest_fisherhamlet_description08 or quest_fisherhamlet_description09 or quest_fisherhamlet_description10 or quest_fisherhamlet_description11 or quest_fisherhamlet_description12:
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    text "[quest_fisherhamlet_description00]"
                                    if not quest_fisherhamlet_description01 and quest_fisherhamlet_description00b:
                                        text "[quest_fisherhamlet_description00b]"
                                    elif quest_fisherhamlet_description00b:
                                        text "{color=#6a6a6a}[quest_fisherhamlet_description00b]{/color}"
                                    if quest_fisherhamlet_description04 or quest_fisherhamlet_description04cd or quest_fisherhamlet_description05 or quest_fisherhamlet_description05proto:
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    if not quest_fisherhamlet_description05 and quest_fisherhamlet_description04:
                                        text "[quest_fisherhamlet_description04]"
                                    elif quest_fisherhamlet_description04:
                                        text "{color=#6a6a6a}[quest_fisherhamlet_description04]{/color}"
                                    if quest_fisherhamlet_description04cd:
                                        text [quest_fisherhamlet_description04cd]
                                    if quest_fisherhamlet_description05:
                                        text "[quest_fisherhamlet_description05]"
                                    if quest_fisherhamlet_description05proto and quest_fisherhamlet_description04 and not quest_fisherhamlet_description05:
                                        text "[quest_fisherhamlet_description05proto]"
                                    if quest_fisherhamlet_description06:
                                        text "[quest_fisherhamlet_description06] [quest_fisherhamlet_description06b]"
                                    if quest_fisherhamlet_description01 or quest_fisherhamlet_description02 or quest_fisherhamlet_description03 or quest_fisherhamlet_description06:
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    if not quest_fisherhamlet_description02 and quest_fisherhamlet_description01:
                                        text "[quest_fisherhamlet_description01]"
                                    elif quest_fisherhamlet_description01:
                                        text "{color=#6a6a6a}[quest_fisherhamlet_description01]{/color}"
                                    if not quest_fisherhamlet_description03 and quest_fisherhamlet_description02:
                                        text "[quest_fisherhamlet_description02]"
                                    elif quest_fisherhamlet_description02:
                                        text "{color=#6a6a6a}[quest_fisherhamlet_description02]{/color}"
                                    if not quest_fisherhamlet_description04 and quest_fisherhamlet_description03:
                                        text "[quest_fisherhamlet_description03]"
                                    elif quest_fisherhamlet_description03:
                                        text "{color=#6a6a6a}[quest_fisherhamlet_description03]{/color}"
                                ########
                                elif journal_quest == "journal_quest_orentius":
                                    label _("{color=#f6d6bd}Orentius, the Necromancer{/color}"):
                                        style "journal_prompt"
                                    if quest_orentius_thyrsus_description02:
                                        text "[quest_orentius_thyrsus_description02]"
                                        text "{color=#6a6a6a}[quest_orentius_thyrsus_description01]{/color}"
                                    if quest_orentius_thyrsus_description03:
                                        text "[quest_orentius_thyrsus_description03]"
                                    if quest_orentius_thyrsus_description04:
                                        text "[quest_orentius_thyrsus_description04]"
                                    if (quest_orentius_thyrsus_description01 and quest_orentius_thais_description00 and not quest_orentius_thyrsus_description02) or (quest_orentius_thyrsus_description01 and quest_orentius_helvius_description01 and not quest_orentius_thyrsus_description02):
                                        text "[quest_orentius_thyrsus_description01]"
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    elif quest_orentius_thyrsus_description01:
                                        text "[quest_orentius_thyrsus_description01]"
                                    ####
                                    if quest_orentius_helvius_description02:
                                        text "[quest_orentius_helvius_description02]"
                                        text "{color=#6a6a6a}[quest_orentius_helvius_description01]{/color}"
                                    if quest_orentius_helvius_description03:
                                        text "[quest_orentius_helvius_description03]"
                                    if quest_orentius_helvius_description04:
                                        text "[quest_orentius_helvius_description04]"
                                    if (quest_orentius_helvius_description01 and quest_orentius_thais_description00):
                                        text "[quest_orentius_helvius_description01]"
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    elif quest_orentius_helvius_description01:
                                        text "[quest_orentius_helvius_description01]"
                                    ####
                                    if quest_orentius_thais_description00betrayal:
                                        text "[quest_orentius_thais_description00betrayal]"
                                    elif thais_defeated:
                                        text "Without {color=#f6d6bd}Thais{/color}, the raid won’t succeed."
                                    elif quest_orentius_thais_description10:
                                        text "[quest_orentius_thais_description10]"
                                    else:
                                        if quest_orentius_thais_description09:
                                            text "[quest_orentius_thais_description09]"
                                        if quest_orentius_thais_description00:
                                            text "{color=#6a6a6a}[quest_orentius_thais_description00]{/color}"
                                        if not quest_orentius_thais_description02 and quest_orentius_thais_description01:
                                            text "[quest_orentius_thais_description01]"
                                        elif quest_orentius_thais_description01:
                                            text "{color=#6a6a6a}[quest_orentius_thais_description01]{/color}"
                                        if not quest_orentius_thais_description03 and quest_orentius_thais_description02:
                                            text "[quest_orentius_thais_description02]"
                                        elif quest_orentius_thais_description02:
                                            text "{color=#6a6a6a}[quest_orentius_thais_description02]{/color}"
                                        if not quest_orentius_thais_description03b and quest_orentius_thais_description03:
                                            text "[quest_orentius_thais_description03]"
                                        elif quest_orentius_thais_description03:
                                            text "{color=#6a6a6a}[quest_orentius_thais_description03]{/color}"
                                        if quest_orentius_thais_description03a01 or quest_orentius_thais_description03a06 or quest_orentius_thais_description03a07:
                                            text "I should speak with {color=#f6d6bd}Thais{/color} about the allies I found."
                                        if not quest_orentius_thais_description03b and quest_orentius_thais_description03a01:
                                            text "[quest_orentius_thais_description03a01]"
                                        elif quest_orentius_thais_description03a01:
                                            text "{color=#6a6a6a}[quest_orentius_thais_description03a01]{/color}"
                                        if not quest_orentius_thais_description03b and quest_orentius_thais_description03a02:
                                            text "[quest_orentius_thais_description03a02]"
                                        elif quest_orentius_thais_description03a02:
                                            text "{color=#6a6a6a}[quest_orentius_thais_description03a02]{/color}"
                                        if not quest_orentius_thais_description03b and quest_orentius_thais_description03a03:
                                            text "[quest_orentius_thais_description03a03]"
                                        elif quest_orentius_thais_description03a03:
                                            text "{color=#6a6a6a}[quest_orentius_thais_description03a03]{/color}"
                                        if not quest_orentius_thais_description03b and quest_orentius_thais_description03a05:
                                            text "[quest_orentius_thais_description03a05]"
                                        elif quest_orentius_thais_description03a05:
                                            text "{color=#6a6a6a}[quest_orentius_thais_description03a05]{/color}"
                                        if not quest_orentius_thais_description03b and quest_orentius_thais_description03a06:
                                            text "[quest_orentius_thais_description03a06]"
                                        elif quest_orentius_thais_description03a06:
                                            text "{color=#6a6a6a}[quest_orentius_thais_description03a06]{/color}"
                                        if not quest_orentius_thais_description03b and quest_orentius_thais_description03a07:
                                            text "[quest_orentius_thais_description03a07]"
                                        elif quest_orentius_thais_description03a07:
                                            text "{color=#6a6a6a}[quest_orentius_thais_description03a07]{/color}"
                                        if quest_orentius_thais_description03b and not orentius_met and not whitemarshes_attacked:
                                            text "[quest_orentius_thais_description03b]"
                                        elif quest_orentius_thais_description03b:
                                            text "{color=#6a6a6a}[quest_orentius_thais_description03b]{/color}"
                                        if not whitemarshes_attacked and not orentius_met:
                                            if quest_orentius_thais_description03a01 or quest_orentius_thais_description03a06 or quest_orentius_thais_description03a07:
                                                text "[quest_orentius_thais_description04a]"
                                        if quest_orentius_thais_description06:
                                            text "[quest_orentius_thais_description06]"
                                ########
                                elif journal_quest == "quest_recruitahunter":
                                    label _("{color=#f6d6bd}Recruit a Hunter{/color}"):
                                        style "journal_prompt"
                                    if quest_recruitahunter_description01:
                                        text "[quest_recruitahunter_description01]"
                                    if quest_recruitahunter_description03:
                                        text "[quest_recruitahunter_description03]"
                                    elif quest_recruitahunter_description02:
                                        text "[quest_recruitahunter_description02]"
                                    if quest_recruitahunter_description01 or quest_recruitahunter_description02 or quest_recruitahunter_description03:
                                        add "gui/horizontalline.png":
                                            xalign 0.5

                                    text "[quest_recruitahunter_description00]"
                                    if quest_recruitahunter_spokento_iason or quest_recruitahunter_spokento_quintus:
                                        text "I was advised that it may be easier to learn more about them if I were to ask people outside of their tribes."
                                    add "gui/horizontalline.png":
                                        xalign 0.5

                                    if quest_recruitahunter_dalit_about_erastos_completed:
                                        text "{color=#6a6a6a}I told Dalit what I learned about Erastos.{/color}"
                                    else:
                                        if not quest_recruitahunter_spokento_erastos:
                                            text "I need to speak with {color=#f6d6bd}Erastos{/color}."
                                        if quest_recruitahunter_spokento_erastos:
                                            text "{color=#6a6a6a}I spoke with Erastos.{/color}"
                                        if quest_recruitahunter_erastos_points < quest_recruitahunter_erastos_threshold:
                                            text "I need to learn more about {color=#f6d6bd}Erastos{/color}."
                                        elif quest_recruitahunter_erastos_points < quest_recruitahunter_erastos_threshold2:
                                            text "I learned quite a bit about {color=#f6d6bd}Erastos{/color}, but I could ask a few more people about him before I report back to {color=#f6d6bd}Dalit{/color}."
                                        else:
                                            text "{color=#6a6a6a}I’m convinced Erastos is a bad candidate for the job.{/color}"
                                    add "gui/horizontalline.png":
                                        xalign 0.5

                                    if quest_recruitahunter_dalit_about_cassia_completed:
                                        text "{color=#6a6a6a}I told Dalit what I learned about Cassia.{/color}"
                                    else:
                                        if not quest_recruitahunter_spokento_cassia:
                                            text "I need to speak with {color=#f6d6bd}Cassia{/color}."
                                        if quest_recruitahunter_spokento_cassia:
                                            text "{color=#6a6a6a}I spoke with Cassia.{/color}"
                                        if quest_recruitahunter_cassia_points < quest_recruitahunter_cassia_threshold:
                                            text "I need to learn more about {color=#f6d6bd}Cassia{/color}."
                                        elif quest_recruitahunter_cassia_points < quest_recruitahunter_cassia_threshold2:
                                            text "I learned quite a bit about {color=#f6d6bd}Cassia{/color}, but I could ask a few more people about her before I report back to {color=#f6d6bd}Dalit{/color}."
                                        else:
                                            text "{color=#6a6a6a}I’m convinced Cassia is a bad candidate for the job.{/color}"

                                    if quest_recruitahunter_dalit_about_cassia == 1 or quest_recruitahunter_dalit_about_erastos == 1:
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    if quest_recruitahunter_dalit_about_erastos == 1:
                                        text "According to {color=#f6d6bd}Dalit{/color}, “{color=#f6d6bd}Erastos{/color} is a trapper. A few months ago, he told a passing-by caravan he wanted to leave his home, and asked them to bring us his message. One of his past neighbors told me he remembers {color=#f6d6bd}Erastos{/color} as a weak, quiet boy. I’m not sure he knows how to fight, but we’d rather use traps anyway.”"
                                    if quest_recruitahunter_dalit_about_cassia == 1:
                                        text "According to {color=#f6d6bd}Dalit{/color}, “{color=#f6d6bd}Cassia{/color} mentioned to {color=#f6d6bd}Asterion{/color} she’d like to come here. She’s a guard, but I’ve heard she’s more of a talker than a fighter. {color=#f6d6bd}Gale Rocks{/color} is so far away I’d really prefer to not travel there, but if she’s the {i}better{/i} choice, I may have no other option.”"
                                ########
                                elif journal_quest == "quest_reachthepaganvillage":
                                    label _("{color=#f6d6bd}The Hidden Village{/color}"):
                                        style "journal_prompt"
                                    text "[quest_reachthepaganvillage_description00]"
                                    if quest_reachthepaganvillage_description00b:
                                        text "[quest_reachthepaganvillage_description00b]"
                                    if quest_reachthepaganvillage_description01:
                                        text "[quest_reachthepaganvillage_description01]"
                                    if quest_reachthepaganvillage_description02:
                                        text "[quest_reachthepaganvillage_description02]"
                                    if quest_reachthepaganvillage_description08:
                                        text "[quest_reachthepaganvillage_description08][quest_reachthepaganvillage_description09]"
                                    if quest_reachthepaganvillage10:
                                        text "[quest_reachthepaganvillage10]"
                                ########
                                elif journal_quest == "quest_pensformonastery":
                                    label _("{color=#f6d6bd}Quills for The Monastery{/color}"):
                                        style "journal_prompt"
                                    text "[quest_pensformonastery_description00]"
                                    if aeli_quest_pens_reward == "reputation":
                                        text "For my service, the monks will spread a few good words about my deeds."
                                    if aeli_quest_pens_reward == "dragons":
                                        text "For my service, I’ll receive five dragon bones."
                                    if aeli_quest_pens_reward == "healingpotion":
                                        text "For my service, I’ll receive a healing potion."
                                    if aeli_quest_pens_reward == "shelter":
                                        text "For my service, I’ll be able to rest in the monastery after dusk."
                                    if quest_pensformonastery_description01:
                                        text "[quest_pensformonastery_description01]"
                                    if quest_pensformonastery_description02:
                                        text "[quest_pensformonastery_description02]"
                                    if quest_pensformonastery_description03:
                                        text "[quest_pensformonastery_description03]"
                                    if quest_pensformonastery_description04:
                                        text "[quest_pensformonastery_description04]"
                                    if quest_pensformonastery_description05:
                                        text "[quest_pensformonastery_description05]"
                                ########
                                elif journal_quest == "quest_readtheletter":
                                    label _("{color=#f6d6bd}Read the Letter{/color}"):
                                        style "journal_prompt"
                                    text "[quest_readtheletter_description00]"
                                    if quest_readtheletter_description00a:
                                        text "[quest_readtheletter_description00a]"
                                    if quest_readtheletter_description00b:
                                        text "[quest_readtheletter_description00b]"
                                    if item_letterwhitemarshes_read and iason_about_valens:
                                        text "According to the letter, {color=#f6d6bd}Valens’{/color} husband left him for another person, though I heard a different story in {color=#f6d6bd}Pelt of the North{/color}."
                                    elif item_letterwhitemarshes_read:
                                        text "According to the letter, {color=#f6d6bd}Valens’{/color} husband left him for another person."
                                    if quest_readtheletter_description01:
                                        text "[quest_readtheletter_description01]"
                                    if quest_readtheletter_description01alt:
                                        text "[quest_readtheletter_description01alt]"
                                    if quest_readtheletter_description02:
                                        text "[quest_readtheletter_description02]"
                                    if quest_readtheletter_description03:
                                        text "[quest_readtheletter_description03]"
                                ########
                                elif journal_quest == "quest_ruins":
                                    label _("{color=#f6d6bd}The Ruined Village{/color}"):
                                        style "journal_prompt"
                                    if quest_ruins_choice == "lefttocity":
                                        text "I decided to leave this matter to the city officials."
                                    elif quest_ruins_choice == "forgotten":
                                        text "I decided to let these events stay in the past. Nothing good would come out of opening such old wounds."
                                    elif quest_ruins_choice == "thais_defeated":
                                        text "{color=#f6d6bd}The druids{/color} helped me convince the village to question {color=#f6d6bd}Thais’{/color} leadership. Hopefully, she will soon stop being a mayor."
                                    elif quest_ruins_choice == "thais_won":
                                        text "I tried to undercut {color=#f6d6bd}Thais’{/color} position, but I gathered close to no support. She won."
                                    elif quest_ruins_choice == "thais_alliance":
                                        text "I offered {color=#f6d6bd}Thais{/color} an alliance. As long as I have ties with the merchant guild, I can expect a secure and {i}profitable{/i} position for myself in the North."
                                    elif quest_ruins_choice == "thais_alliance_fail":
                                        text "I offered {color=#f6d6bd}Thais{/color} an alliance, but she doesn’t trust me. I gained nothing from it."
                                    if quest_ruins_choice:
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    if quest_ruinsconflictopen == 1:
                                        text "I should use what I’ve learned to confront the people of {color=#f6d6bd}Howler’s Dell{/color} - but only if I’m sure I can use my knowledge and the trust I’ve gained to my advantage."
                                    elif ruinedvillage_confront_can == 1:
                                        text "I should use what I’ve learned to confront the locals and learn from them the truth about the ruins in the south."
                                    if quest_ruins_description_glauciasperspective:
                                        text "[quest_ruins_description_glauciasperspective]"
                                    if quest_ruins_description_creeksparticipated:
                                        text "[quest_ruins_description_creeksparticipated]"
                                    if quest_ruins_description_peltparticipated:
                                        text "[quest_ruins_description_peltparticipated]"
                                    if quest_ruins_description_truestory:
                                        text "[quest_ruins_description_truestory]"
                                    if quest_ruinsconflictopen == 1 or ruinedvillage_confront_can == 1 or quest_ruins_description_truestory:
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    text "[quest_ruins_description00]"
                                    if quest_ruins_description01:
                                        text "[quest_ruins_description01]"
                                        if (quest_ruins_10yclue05 and quest_ruins_10yclue05p2) or quest_ruins_10yclue05 or quest_ruins_10yclue06 or quest_ruins_10yclue01 or quest_ruins_10yclue02 or quest_ruins_10yclue03 or (quest_ruins_10yclue04 and quest_ruins_10yclue04p2) or quest_ruins_10yclue04 or quest_ruins_10yclue07 or quest_ruins_10yclue08 or quest_ruins_10yclue09 or quest_ruins_10yclue10 or quest_ruins_10yclue11 or quest_ruins_10yclue12 or quest_ruins_10yclue13:
                                            text "This event ocurred at the same time as a few others:"
                                        if quest_ruins_10yclue05 and quest_ruins_10yclue05p2:
                                            text "[quest_ruins_10yclue05] [quest_ruins_10yclue05p2]"
                                        elif quest_ruins_10yclue05:
                                            text "[quest_ruins_10yclue05]"
                                        if quest_ruins_10yclue06:
                                            text "[quest_ruins_10yclue06]"
                                        if quest_ruins_10yclue01:
                                            text "[quest_ruins_10yclue01]"
                                        if quest_ruins_10yclue02:
                                            text "[quest_ruins_10yclue02]"
                                        if quest_ruins_10yclue03:
                                            text "[quest_ruins_10yclue03]"
                                        if quest_ruins_10yclue04 and quest_ruins_10yclue04p2:
                                            text "[quest_ruins_10yclue04p2]"
                                        elif quest_ruins_10yclue04:
                                            text "[quest_ruins_10yclue04]"
                                        if quest_ruins_10yclue07:
                                            text "[quest_ruins_10yclue07]"
                                        if quest_ruins_10yclue08:
                                            text "[quest_ruins_10yclue08]"
                                        if quest_ruins_10yclue09:
                                            text "[quest_ruins_10yclue09]"
                                        if quest_ruins_10yclue10:
                                            text "[quest_ruins_10yclue10]"
                                        if quest_ruins_10yclue11:
                                            text "[quest_ruins_10yclue11]"
                                        if quest_ruins_10yclue12:
                                            text "[quest_ruins_10yclue12]"
                                        if quest_ruins_10yclue13:
                                            text "[quest_ruins_10yclue13]"
                                        if (quest_ruins_10yclue05 and quest_ruins_10yclue05p2) or quest_ruins_10yclue05 or quest_ruins_10yclue06 or quest_ruins_10yclue01 or quest_ruins_10yclue02 or quest_ruins_10yclue03 or (quest_ruins_10yclue04 and quest_ruins_10yclue04p2) or quest_ruins_10yclue04 or quest_ruins_10yclue07 or quest_ruins_10yclue08 or quest_ruins_10yclue09 or quest_ruins_10yclue10 or quest_ruins_10yclue11 or quest_ruins_10yclue12 or quest_ruins_10yclue13:
                                            add "gui/horizontalline.png":
                                                xalign 0.5
                                    if quest_ruins_treepicture:
                                        if pc_class == "scholar":
                                            if item_howlersdelltoken:
                                                text "In the ruins, I found a weird, threatening image of a dead tree growing from a human skull. It’s very similar to the picture on the {i}Token of Gratitude{/i} that I received in Howler’s Dell. Above it, there was a single large word: {i}TRAITORS.{/i}"
                                            elif howlersdell_firsttime:
                                                text "In the ruins, I found a weird, threatening image of a dead tree growing from a human skull. I’ve seen a similar plant in the main square of {color=#f6d6bd}Howler’s Dell{/color}. Above it, there was see a single large word: {i}TRAITORS.{/i}"
                                            else:
                                                text "In the ruins, I found a weird, threatening image of a dead tree growing from a human skull. I’re not sure what exactly it could be. Above it, there was see a single large word: {i}TRAITORS.{/i}"
                                        else:
                                            if item_howlersdelltoken:
                                                text "In the ruins, I found a weird, threatening image of a dead tree growing from a human skull. It’s very similar to the picture on the {i}Token of Gratitude{/i} that I received in Howler’s Dell."
                                            elif howlersdell_firsttime:
                                                text "In the ruins, I found a weird, threatening image of a dead tree growing from a human skull. I’ve seen a similar plant in the main square of {color=#f6d6bd}Howler’s Dell{/color}. "
                                            else:
                                                text "In the ruins, I found a weird, threatening image of a dead tree growing from a human skull. I’re not sure what exactly it could be."
                                    if quest_ruins_insideclues10:
                                        text "[quest_ruins_insideclues10]"
                                    if quest_ruins_insideclues01:
                                        text "[quest_ruins_insideclues01]"
                                    if quest_ruins_insideclues02:
                                        text "[quest_ruins_insideclues02]"
                                    if quest_ruins_insideclues03:
                                        text "[quest_ruins_insideclues03]"
                                    if quest_ruins_insideclues04:
                                        text "[quest_ruins_insideclues04]"
                                    if quest_ruins_insideclues05:
                                        text "[quest_ruins_insideclues05]"
                                    if quest_ruins_insideclues06:
                                        text "[quest_ruins_insideclues06]"
                                    if quest_ruins_insideclues07:
                                        text "[quest_ruins_insideclues07]"
                                    if quest_ruins_insideclues08:
                                        text "[quest_ruins_insideclues08]"
                                    if quest_ruins_insideclues09:
                                        text "[quest_ruins_insideclues09]"
                                ########
                                elif journal_quest == "quest_sleepinggiant":
                                    label _("{color=#f6d6bd}The Sleeping Giant{/color}"):
                                        style "journal_prompt"
                                    if quest_sleepinggiant_description04:
                                        text "[quest_sleepinggiant_description04]"
                                    if quest_sleepinggiant_description05:
                                        text "[quest_sleepinggiant_description05]"
                                    if quest_sleepinggiant_description04 or quest_sleepinggiant_description05:
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    if quest_sleepinggiant_description00:
                                        text "[quest_sleepinggiant_description00]"
                                    if quest_sleepinggiant_description00a:
                                        text "[quest_sleepinggiant_description00a]"
                                    if quest_sleepinggiant_description01:
                                        text "[quest_sleepinggiant_description01]"
                                    if foggy_about_giantstatue:
                                        text "{color=#f6d6bd}Foggy{/color} told me about people kneeling in front of the statue."
                                    if quest_sleepinggiant_description02:
                                        text "[quest_sleepinggiant_description02]"
                                    if giantstatue_pray_knows:
                                        text "I’ve learned how to “pray” in front of the statue. I should start with kneeling down in front of it."
                                    if quest_sleepinggiant_description03:
                                        text "[quest_sleepinggiant_description03]"
                                ########
                                elif journal_quest == "quest_studyingthegolems":
                                    label _("{color=#f6d6bd}Studying the Golems{/color}"):
                                        style "journal_prompt"
                                    if quest_studyingthegolems_description06:
                                        text "[quest_studyingthegolems_description06]"
                                    if quest_studyingthegolems_description07:
                                        text "[quest_studyingthegolems_description07]"
                                    if quest_studyingthegolems_description06 or quest_studyingthegolems_description07:
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    text "[quest_studyingthegolems_description00]"
                                    if quest_studyingthegolems_description02:
                                        text "[quest_studyingthegolems_description02]"
                                    if quest_studyingthegolems_description01 or quest_studyingthegolems_description03 or quest_studyingthegolems_description03b or quest_studyingthegolems_description04:
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    if quest_studyingthegolems_description01:
                                        if aeli_golems_learned01:
                                            text "{color=#6a6a6a}[quest_studyingthegolems_description01]{/color}"
                                        else:
                                            text "[quest_studyingthegolems_description01]"
                                    if quest_studyingthegolems_description03:
                                        if aeli_golems_learned03:
                                            text "{color=#6a6a6a}[quest_studyingthegolems_description03]{/color}"
                                        else:
                                            text "[quest_studyingthegolems_description03]"
                                    if quest_studyingthegolems_description03b:
                                        if aeli_golems_learned03b:
                                            text "{color=#6a6a6a}[quest_studyingthegolems_description03b]{/color}"
                                        else:
                                            text "[quest_studyingthegolems_description03b]"
                                    if quest_studyingthegolems_description04:
                                        if aeli_golems_learned04b:
                                            text "{color=#6a6a6a}[quest_studyingthegolems_description04] {color=#f6d6bd}[dalit_name]{/color}, [quest_studyingthegolems_description04b].{/color}"
                                        else:
                                            text "[quest_studyingthegolems_description04] {color=#f6d6bd}[dalit_name]{/color}, [quest_studyingthegolems_description04b]."
                                ########
                                elif journal_quest == "quest_creekssupport":
                                    label _("{color=#f6d6bd}The Support of Creeks{/color}"):
                                        style "journal_prompt"
                                    text "[quest_creekssupport_description00]"
                                    if quest_creekssupport_description01:
                                        text "[quest_creekssupport_description01]"
                                    if quest_creekssupport_description04:
                                        text "[quest_creekssupport_description04]"
                                    if quest_creekssupport_description05:
                                        text "[quest_creekssupport_description05]"
                                ########
                                elif journal_quest == "quest_glauciasupport":
                                    label _("{color=#f6d6bd}The Support of Bandits{/color}"):
                                        style "journal_prompt"
                                    if quest_glauciasupport_description00:
                                        text "[quest_glauciasupport_description00]"
                                    if quest_glauciasupport_description00alt:
                                        text "[quest_glauciasupport_description00alt]"
                                    if quest_glauciasupport_description00a:
                                        text "[quest_glauciasupport_description00a]"
                                    if quest_glauciasupport_description01:
                                        text "[quest_glauciasupport_description01]"
                                    if quest_glauciasupport_description02:
                                        text "[quest_glauciasupport_description02]"
                                    if quest_glauciasupport_description03:
                                        text "[quest_glauciasupport_description03]"
                                ########
                                elif journal_quest == "quest_galerockssupport":
                                    label _("{color=#f6d6bd}The Support of Gale Rocks{/color}"):
                                        style "journal_prompt"
                                    text "[quest_galerockssupport_description00]"
                                    text "[quest_galerockssupport_description00a]"
                                    if quest_galerockssupport_description01:
                                        text "[quest_galerockssupport_description01]"
                                    if quest_galerockssupport_description02:
                                        text "[quest_galerockssupport_description02]"
                                ########
                                elif journal_quest == "quest_howlerssupport":
                                    label _("{color=#f6d6bd}The Support of Howler’s Dell{/color}"):
                                        style "journal_prompt"
                                    text "[quest_howlerssupport_description00]"
                                    if quest_howlerssupport_description01:
                                        text "[quest_howlerssupport_description01]"
                                    if quest_howlerssupport_description05:
                                        text "[quest_howlerssupport_description05]"
                                    if quest_howlerssupport_description06:
                                        text "[quest_howlerssupport_description06]"
                                ########
                                elif journal_quest == "quest_greenmountainsupport":
                                    label _("{color=#f6d6bd}The Support of The Green Mountain Tribe{/color}"):
                                        style "journal_prompt"
                                    text "[quest_greenmountainsupport_description00]"
                                ########
                                elif journal_quest == "quest_monasterysupport":
                                    label _("{color=#f6d6bd}The Support of Monks{/color}"):
                                        style "journal_prompt"
                                    text "[quest_monasterysupport_description00]"
                                    if quest_monasterysupport_description01:
                                        text "[quest_monasterysupport_description01]"
                                    if quest_monasterysupport_description01lie:
                                        text "[quest_monasterysupport_description01lie]"
                                    if quest_monasterysupport_description02:
                                        text "[quest_monasterysupport_description02]"
                                    if quest_monasterysupport_description03:
                                        text "[quest_monasterysupport_description03]"
                                ########
                                elif journal_quest == "quest_oldpagossupport":
                                    label _("{color=#f6d6bd}The Support of Old Págos{/color}"):
                                        style "journal_prompt"
                                    text "[quest_oldpagossupport_description00]"
                                ########
                                elif journal_quest == "quest_swampaltar":
                                    label _("{color=#f6d6bd}The Swamp Altar{/color}"):
                                        style "journal_prompt"
                                    text "[quest_swampaltar_description00]"
                                    if quest_swampaltar_description01:
                                        text "[quest_swampaltar_description01]"
                                    if quest_swampaltar_description02:
                                        text "[quest_swampaltar_description02]"
                                    if quest_swampaltar_description03:
                                        text "[quest_swampaltar_description03]"
                                    if quest_swampaltar_description04:
                                        text "[quest_swampaltar_description04]"
                                #######
                                else:
                                    text "No quest selected."
                        vbar value YScrollValue ("journalquests"):
                            xpos 60
                            unscrollable "hide"

                elif journalmode == "people":
                    hbox:
                        xmaximum 380
                        viewport id "listpeople":
                            draggable True
                            xmaximum 350
                            mousewheel True
                            xpos 10
                            vbox:
                                style_prefix "journal"
                                xalign 0.0
                                yalign 0.0
                                xmaximum 350
                                xpos 10
                                ypos 6
                                spacing 20
                                if description_aegidia01:
                                    textbutton "Aegidia" action [SetVariable("journal_people", "persondescription_aegidia")]
                                if description_akakios01 or description_akakios02 or description_akakios03 or description_akakios04 or description_akakios05:
                                    textbutton "Akakios" action [SetVariable("journal_people", "persondescription_akakios")]
                                if description_asterion01 or description_asterion02 or description_asterion03 or description_asterion04 or description_asterion05:
                                    textbutton "Asterion" action [SetVariable("journal_people", "persondescription_asterion")]
                                if iason_name == "Pelt’s innkeep":
                                    if description_iason01 or description_iason02 or description_iason03 or description_iason04 or description_iason05 or description_iason07:
                                        textbutton "Pelt’s Innkeep" action [SetVariable("journal_people", "persondescription_iason")]
                                if eudocia_name == "crafter":
                                    if description_eudocia01 or description_eudocia02 or description_eudocia03 or description_eudocia04 or description_eudocia05 or description_eudocia06 or description_eudocia07 or description_eudocia08 or description_eudocia09:
                                        textbutton "Enchantress" action [SetVariable("journal_people", "persondescription_eudocia")]
                                if dalit_name == "Dalit":
                                    if description_dalit01 or description_dalit02 or description_dalit03 or description_dalit04 or description_dalit05:
                                        textbutton "Dalit" action [SetVariable("journal_people", "persondescription_dalit")]
                                if description_elah_efren00 or description_elah_efren01 or description_elah_efren05 or description_elah_efren06:
                                    textbutton "Efren & Elah" action [SetVariable("journal_people", "persondescription_elah_efren")]
                                if eudocia_name == "Eudocia":
                                    if description_eudocia01 or description_eudocia02 or description_eudocia03 or description_eudocia04 or description_eudocia05 or description_eudocia06 or description_eudocia07 or description_eudocia08 or description_eudocia09:
                                        textbutton "[eudocia_name]" action [SetVariable("journal_people", "persondescription_eudocia")]
                                if description_foggy01 or description_foggy02 or description_foggy03 or description_foggy04 or description_foggy05 or description_foggy06 or description_foggy07:
                                    textbutton "Foggy" action [SetVariable("journal_people", "persondescription_foggy")]
                                if description_glaucia01 or description_glaucia02 or description_glaucia03 or description_glaucia04 or description_glaucia05 or description_glaucia08 or description_glaucia11 or description_glaucia12 or description_glaucia13 or description_glaucia14 or description_glaucia21:
                                    textbutton "Glaucia" action [SetVariable("journal_people", "persondescription_glaucia")]
                                if iason_name == "Iason":
                                    if description_iason01 or description_iason02 or description_iason03 or description_iason04 or description_iason05 or description_iason07:
                                        textbutton "[iason_name]" action [SetVariable("journal_people", "persondescription_iason")]
                                # if nalia_met:
                                #     if description_nalia01 or description_nalia02 or description_nalia03 or description_nalia04 or description_nalia05:
                                #         textbutton "Nalia" action [SetVariable("journal_people", "persondescription_nalia")]
                                if description_orentius00 or description_orentius01 or description_orentius02 or description_orentius03 or description_orentius05 or description_orentius06 or description_orentius07 or description_orentius08 or description_orentius09 or description_orentius10 or description_orentius11:
                                    textbutton "Orentius" action [SetVariable("journal_people", "persondescription_orentius")]
                                if description_pyrrhos01:
                                    textbutton "Pyrrhos" action [SetVariable("journal_people", "persondescription_pyrrhos")]
                                if description_quintus01 or description_quintus02 or description_quintus03 or description_quintus07 or description_quintus04 or description_quintus05 or description_quintus06:
                                    textbutton "Quintus" action [SetVariable("journal_people", "persondescription_quintus")]
                                if description_thais01 or description_thais02 or description_thais03 or description_thais03b or description_thais04 or description_thais05 or description_thais06 or description_thais07 or description_thais08 or description_thais09 or description_thais10 or description_thais11:
                                    textbutton "Thais" action [SetVariable("journal_people", "persondescription_thais")]
                                if description_thyrsus00a != "" or description_thyrsus00b != "" or description_thyrsus01 or description_thyrsus02 or description_thyrsus03 or description_thyrsus05:
                                    textbutton "Thyrsus" action [SetVariable("journal_people", "persondescription_thyrsus")]
                                if description_tulia01 or description_tulia02 or description_tulia03 or description_tulia04 or description_tulia05:
                                    textbutton "Tulia" action [SetVariable("journal_people", "persondescription_tulia")]
                        vbar value YScrollValue ("listpeople"):
                            xpos 30
                            unscrollable "hide"

                    hbox:
                        xmaximum 1100
                        viewport id "journalpeople":
                            draggable True
                            xmaximum 1008
                            mousewheel True
                            xpos 66
                            vbox:
                                style_prefix "journal"
                                xalign 0.0
                                yalign 0.0
                                xpos 80
                                xmaximum 968
                                ypos 10
                                spacing 20
                                #######
                                if journal_people == "persondescription_aegidia":
                                    label _("{color=#f6d6bd}Aegidia{/color}"):
                                        style "journal_prompt"
                                    text "[description_aegidia00]"
                                    if description_aegidia01:
                                        text "[description_aegidia01]"
                                    if description_aegidia02:
                                        text "[description_aegidia02]"
                                    if description_aegidia03:
                                        text "[description_aegidia03]"
                                    if description_aegidia04:
                                        text "[description_aegidia04]"
                                    if description_aegidia06:
                                        text "[description_aegidia06]"
                                    if description_aegidia05:
                                        text "[description_aegidia05]"
                                elif journal_people == "persondescription_akakios":
                                    label _("{color=#f6d6bd}Akakios{/color}"):
                                        style "journal_prompt"
                                    text "[description_akakios00]"
                                    if description_akakios01:
                                        text "[description_akakios01]"
                                    if description_akakios02:
                                        text "[description_akakios02] {color=#f6d6bd}[iason_name]{/color}[description_akakios02a]"
                                    if description_akakios03:
                                        text "[description_akakios03]"
                                    if description_akakios04:
                                        text "[description_akakios04]"
                                    if description_akakios05:
                                        text "[description_akakios05]"
                                    if description_akakios06:
                                        text "[description_akakios06]"
                                elif journal_people == "persondescription_asterion":
                                    label _("{color=#f6d6bd}Asterion{/color}"):
                                        style "journal_prompt"
                                    text "[description_asterion00]"
                                    if description_asterion01:
                                        text "[description_asterion01]"
                                    if description_asterion02:
                                        text "[description_asterion02]{color=#f6d6bd}[iason_name]{/color}[description_asterion02b]"
                                    if description_asterion03:
                                        text "[description_asterion03] {color=#f6d6bd}[iason_name]{/color}[description_asterion03b]"
                                    if description_asterion04:
                                        text "[description_asterion04]"
                                    if description_asterion05:
                                        text "[description_asterion05]"
                                    if description_asterion06:
                                        text "[description_asterion06]"
                                    if description_asterion07:
                                        text "[description_asterion07]"
                                    if description_asterion08:
                                        text "[description_asterion08]"
                                    if description_asterion09:
                                        text "[description_asterion09]"
                                    if description_asterion10:
                                        text "[description_asterion10]"
                                    if description_asterion11 and not description_asterion12:
                                        text "[description_asterion11]"
                                    if description_asterion12:
                                        text "[description_asterion12]"
                                    if description_asterion13:
                                        text "[description_asterion13]"
                                    if description_asterion14:
                                        text "[description_asterion14]"
                                    if description_asterion15:
                                        text "[description_asterion15]"
                                    if description_asterion16:
                                        text "[description_asterion16]"
                                elif journal_people == "persondescription_dalit":
                                    label _("{color=#f6d6bd}Dalit{/color}"):
                                        style "journal_prompt"
                                    text "[description_dalit00]"
                                    if description_dalit01:
                                        text "[description_dalit01]"
                                    if description_dalit02:
                                        text "[description_dalit02] {color=#f6d6bd}[iason_name]{/color}[description_dalit02b]"
                                    if description_dalit03:
                                        text "[description_dalit03]"
                                    if description_dalit04:
                                        text "[description_dalit04]"
                                    if description_dalit05:
                                        text "[description_dalit05]"
                                elif journal_people == "persondescription_elah_efren":
                                    label _("{color=#f6d6bd}Efren & Elah{/color}"):
                                        style "journal_prompt"
                                    if elah_efren_siblings:
                                        text "[description_elah_efren00]"
                                    else:
                                        text "[description_elah_efren00alt]"
                                    if description_elah_efren06:
                                        text "According to {color=#f6d6bd}[iason_name]{/color}, [description_elah_efren06]"
                                    if description_elah_efren01:
                                        text "According to {color=#f6d6bd}[iason_name]{/color}, [description_elah_efren01]"
                                    if description_elah_efren05:
                                        text "[description_elah_efren05]"



                                elif journal_people == "persondescription_eudocia":
                                    label _("{color=#f6d6bd}Eudocia{/color}"):
                                        style "journal_prompt"
                                    if description_eudocia00:
                                        text "[description_eudocia00]"
                                    if description_eudocia01:
                                        text "[description_eudocia01] {color=#f6d6bd}[iason_name]{/color}[description_eudocia01b]"
                                    if description_eudocia08:
                                        text "[description_eudocia08]"
                                    if description_eudocia07:
                                        text "[description_eudocia07]"
                                    if description_eudocia02:
                                        text "[description_eudocia02]"
                                    if description_eudocia03:
                                        text "[description_eudocia03]"
                                    if description_eudocia04:
                                        text "[description_eudocia04]"
                                    if description_eudocia05:
                                        text "[description_eudocia05]"
                                    if description_eudocia06:
                                        text "[description_eudocia06]"
                                    if description_eudocia09:
                                        text "[description_eudocia09]"
                                    if quest_explorepeninsula_description15c:
                                        text "[quest_explorepeninsula_description15c]"
                                    elif quest_explorepeninsula_description15b:
                                        text "[quest_explorepeninsula_description15b]"
                                    elif quest_explorepeninsula_description15a:
                                        text "[quest_explorepeninsula_description15a]"
                                    elif quest_explorepeninsula_description15:
                                        text "[quest_explorepeninsula_description15]"
                                elif journal_people == "persondescription_foggy":
                                    label _("{color=#f6d6bd}Foggy{/color}"):
                                        style "journal_prompt"
                                    text "[description_foggy00]"
                                    if description_foggy01:
                                        text "[description_foggy01] {color=#f6d6bd}[iason_name]{/color}[description_foggy01b]"
                                    if description_foggy03:
                                        text "[description_foggy03]"
                                    if description_foggy02:
                                        text "[description_foggy02]"
                                    if description_foggy04 and not description_foggy05:
                                        text "[description_foggy04]"
                                    if description_foggy05:
                                        text "[description_foggy05]"
                                    if description_foggy06:
                                        text "[description_foggy06]"
                                    if description_foggy07:
                                        text "[description_foggy07]"
                                elif journal_people == "persondescription_glaucia":
                                    label _("{color=#f6d6bd}Glaucia{/color}"):
                                        style "journal_prompt"
                                    # text "[description_glaucia00]"
                                    if description_glaucia18:
                                        text "[description_glaucia18]"
                                    if description_glaucia01 and not description_glaucia01c:
                                        text "[description_glaucia01] {color=#f6d6bd}[iason_name]{/color}[description_glaucia01b]"
                                    elif description_glaucia01 and description_glaucia01c:
                                        text "[description_glaucia01] {color=#f6d6bd}[iason_name]{/color}[description_glaucia01b][description_glaucia01c]"
                                    if description_glaucia21:
                                        text "[description_glaucia21]"
                                    if description_glaucia12:
                                        text "[description_glaucia12]"
                                    if description_glaucia11:
                                        text "[description_glaucia11]"
                                    if galerocks_rumor_glaucia and not description_glaucia02:
                                        text "Everyone in {color=#f6d6bd}Gale Rocks{/color} seems to recognize her name."
                                    elif description_glaucia02:
                                        text "[description_glaucia02]"
                                    if description_glaucia14:
                                        text "[description_glaucia14]"
                                    if description_glaucia03:
                                        text "[description_glaucia03]"
                                    if description_glaucia04:
                                        text "[description_glaucia04]"
                                    if description_glaucia16:
                                        text "[description_glaucia16]"
                                    if description_glaucia17:
                                        text "[description_glaucia17]"
                                    if description_glaucia05:
                                        text "[description_glaucia05]"
                                    if description_glaucia06:
                                        text "[description_glaucia06]"
                                    if description_glaucia07:
                                        text "[description_glaucia07]"
                                    if description_glaucia08:
                                        text "[description_glaucia08]"
                                    if description_glaucia09:
                                        text "[description_glaucia09]"
                                    if description_glaucia10:
                                        text "[description_glaucia10]"
                                    if description_glaucia15:
                                        text "[description_glaucia15]"
                                    if description_glaucia19:
                                        text "[description_glaucia19]"
                                    if description_glaucia20:
                                        text "[description_glaucia20]"
                                elif journal_people == "persondescription_iason":
                                    if iason_name == "Pelt’s innkeep":
                                        label _("{color=#f6d6bd}Pelt's Innkeep{/color}"):
                                            style "journal_prompt"
                                    if iason_name == "Iason":
                                        label _("{color=#f6d6bd}Iason{/color}"):
                                            style "journal_prompt"
                                    text "[description_iason00]"
                                    if description_iason01:
                                        text "[description_iason01]"
                                    if description_iason08:
                                        text "[description_iason08]"
                                    if description_iason10:
                                        text "[description_iason10]"
                                    if description_iason02:
                                        text "[description_iason02]"
                                    if description_iason02a:
                                        text "[description_iason02a]"
                                    if description_iason03:
                                        text "[description_iason03]"
                                    if description_iason04:
                                        text "[description_iason04] {color=#f6d6bd}[dalit_name]{/color}[description_iason04b]"
                                    if description_iason05:
                                        text "[description_iason05]"
                                    if description_iason06:
                                        text "[description_iason06]"
                                    if description_iason07:
                                        text "[description_iason07]"
                                # elif journal_people == "persondescription_nalia":
                                #     label _("{color=#f6d6bd}Nalia{/color}"):
                                #         style "journal_prompt"
                                #     text "[description_nalia00]"
                                #     if description_nalia01:
                                #         text "[description_nalia01]"
                                #     if description_nalia02:
                                #         text "[description_nalia02]"
                                #     if description_nalia03:
                                #         text "[description_nalia03]"
                                #     if description_nalia04:
                                #         text "[description_nalia04]"
                                #     if description_nalia05:
                                #         text "[description_nalia05]"
                                elif journal_people == "persondescription_orentius":
                                    label _("{color=#f6d6bd}Orentius{/color}"):
                                        style "journal_prompt"
                                    if description_orentius00:
                                        text "[description_orentius00]"
                                    if description_orentius10:
                                        text "[description_orentius10]"
                                    if description_orentius11:
                                        text "[description_orentius11]"
                                    if description_orentius01:
                                        text "[description_orentius01]"
                                    if description_orentius02:
                                        text "[description_orentius02]"
                                    if description_orentius03:
                                        text "According to {color=#f6d6bd}[iason_name]{/color}, [description_orentius03]"
                                    if description_orentius04:
                                        text "[description_orentius04]"
                                    if description_orentius05:
                                        text "[description_orentius05]"
                                    if description_orentius06:
                                        text "[description_orentius06]"
                                    if description_orentius08:
                                        text "[description_orentius08]"
                                    if description_orentius09:
                                        text "[description_orentius09]"
                                    if description_orentius07:
                                        text "[description_orentius07]"
                                elif journal_people == "persondescription_quintus":
                                    label _("{color=#f6d6bd}Quintus{/color}"):
                                        style "journal_prompt"
                                    text "[description_quintus00]"
                                    if description_quintus05:
                                        text "[description_quintus05]"
                                    if quintus_friendswithdalit:
                                        text "You’ve heard that he used to spend quite a bit of time with the hunters at {color=#f6d6bd}Pelt{/color}."
                                    if description_quintus03:
                                        text "[description_quintus03]"
                                    if description_quintus07:
                                        text "[description_quintus07]"
                                    if description_quintus01 and description_quintus05:
                                        text "{color=#6a6a6a}[description_quintus01]{/color}"
                                    elif description_quintus01:
                                        text "[description_quintus01]"
                                    elif description_quintus06:
                                        text "[description_quintus06]"
                                    if description_quintus02:
                                        text "[description_quintus02] {color=#f6d6bd}[iason_name]{/color}[description_quintus02b]"
                                    if quintus_friendswithdalit:
                                        text "I heard that he used to be a good friend with the hunters at {color=#f6d6bd}Pelt of The North{/color}."
                                    if description_quintus04:
                                        text "[description_quintus04]"
                                elif journal_people == "persondescription_pyrrhos":
                                    label _("{color=#f6d6bd}Pyrrhos{/color}"):
                                        style "journal_prompt"
                                    text "[description_pyrrhos00]"
                                    if description_pyrrhos01:
                                        text "[description_pyrrhos01]"
                                    if galerocks_petronius_about_pastrobbery:
                                        text "I heard that he stole an iron ingot in {color=#f6d6bd}Gale Rocks{/color}."
                                    if description_pyrrhos02:
                                        text "[description_pyrrhos02]"
                                    if description_pyrrhos03:
                                        text "[description_pyrrhos03]"
                                    if description_pyrrhos04:
                                        text "[description_pyrrhos04]"
                                elif journal_people == "persondescription_thais":
                                    label _("{color=#f6d6bd}Thais{/color}"):
                                        style "journal_prompt"
                                    text "[description_thais00]"
                                    if description_thais_pcopinion == "strongleader":
                                        text "I believe she’s a strong leader."
                                    elif description_thais_pcopinion == "trustworthy":
                                        text "I think she’s worthy of my trust."
                                    elif description_thais_pcopinion == "wicked":
                                        text "Sometimes I think there’s an evil spirit in her."
                                    elif description_thais_pcopinion == "dishonest":
                                        text "I think she’s dishonest and should be kept at a distance."
                                    elif description_thais_pcopinion == "useful":
                                        text "She has her flaws, but she’s useful to me."
                                    elif description_thais_pcopinion == "friend":
                                        text "I enjoy her company."
                                    elif description_thais_pcopinion == "lie":
                                        text "When I had to say what I think of her, I kept the truth to myself."
                                    elif description_thais_pcopinion == "notsure":
                                        text "When I had to say what I think of her, I wasn’t sure."
                                    if description_thais09:
                                        text "[description_thais09]"
                                    if description_thais01:
                                        text "[description_thais01]"
                                    if description_thais02:
                                        text "[description_thais02]"
                                    if description_thais02a:
                                        text "[description_thais02a]"
                                    if description_thais04:
                                        if iason_name == "Iason":
                                            text "{color=#f6d6bd}[iason_name]{/color}[description_thais04]"
                                        else:
                                            text "{color=#f6d6bd}Pelt’s Innkeep{/color}[description_thais04]"
                                    if description_thais03:
                                        text "[description_thais03] [description_thais03b]"
                                    if description_thais07:
                                        text "[description_thais07]"
                                    if description_thais08:
                                        text "[description_thais08]"
                                    if description_thais11:
                                        text "[description_thais11]"
                                    if description_thais05:
                                        text "[description_thais05]"
                                    if description_thais06:
                                        text "[description_thais06]"
                                    if description_thais10:
                                        text "[description_thais10]"
                                elif journal_people == "persondescription_thyrsus":
                                    label _("{color=#f6d6bd}Thyrsus{/color}"):
                                        style "journal_prompt"
                                    if description_thyrsus00:
                                        text "[description_thyrsus00][description_thyrsus00a][description_thyrsus00b]"
                                    if description_thyrsus01:
                                        text "[description_thyrsus01]"
                                    if description_thyrsus04:
                                        text "[description_thyrsus04]"
                                    if description_thyrsus04a:
                                        text "[description_thyrsus04a]"
                                    if description_thyrsus02:
                                        text "[description_thyrsus02]"
                                    if description_thyrsus03:
                                        text "[description_thyrsus03]"
                                    if description_thyrsus05:
                                        text "[description_thyrsus05]"
                                    if description_thyrsus06:
                                        text "[description_thyrsus06]"
                                elif journal_people == "persondescription_tulia":
                                    label _("{color=#f6d6bd}Tulia{/color}"):
                                        style "journal_prompt"
                                    text "[description_tulia00]"
                                    if description_tulia01:
                                        text "[description_tulia01]"
                                    if description_tulia02:
                                        text "[description_tulia02]"
                                    if description_tulia04:
                                        text "[description_tulia04]"
                                    if description_tulia03:
                                        text "[description_tulia03] {color=#f6d6bd}[iason_name]{/color}[description_tulia03b]"
                                    if description_tulia05:
                                        text "[description_tulia05]"
                                #######
                                else:
                                    text "No soul selected."
                        vbar value YScrollValue ("journalpeople"):
                            xpos 60
                            unscrollable "hide"

                elif journalmode == "groups":
                    hbox:
                        xmaximum 380
                        viewport id "listgroups":
                            draggable True
                            xmaximum 350
                            mousewheel True
                            xpos 10
                            vbox:
                                style_prefix "journal"
                                xalign 0.0
                                yalign 0.0
                                xmaximum 350
                                xpos 10
                                ypos 6
                                spacing 20
                                # if NAMEdescription01 or NAMEdescription02 or NAMEdescription03 or NAMEdescription04 or NAMEdescription05:
                                #     textbutton "NAME" action [SetVariable("journal_group", "groupsNAMEdescription")]
                                if quest_intelforpeltnorth or banditshideout_galerocks_tiestobandits or banditshideout_pcknowswhere or description_bandits01 or description_bandits02 or description_bandits03 or description_bandits04 or description_bandits05 or description_bandits06:
                                    textbutton "Bandits’ Camp" action [SetVariable("journal_group", "journal_group_bandits")]
                                if description_greenmountaintribe01 or description_greenmountaintribe03 or description_greenmountaintribe04 or description_greenmountaintribe05 or description_greenmountaintribe06 or description_greenmountaintribe07 or description_greenmountaintribe08 or description_greenmountaintribe09 or description_greenmountaintribe10:
                                    textbutton "The Tribe of The Green Mountain" action [SetVariable("journal_group", "journal_group_greenmountaintribe")]
                                if description_creeks01 or description_creeks01a or description_creeks01b or description_creeks02 or description_creeks03 or description_creeks04 or description_creeks05:
                                    textbutton "Creeks" action [SetVariable("journal_group", "journal_group_creeks")]
                                if description_druids01 or description_druids02 or description_druids03 or description_druids04 or description_druids04a or description_druids05 or description_druids07 or description_druids08 :
                                    textbutton "Druids" action [SetVariable("journal_group", "journal_group_druids")]
                                if description_galerocks01 or description_galerocks02 or description_galerocks03 or description_galerocks04 or description_galerocks05 or description_galerocks14:
                                    textbutton "Gale Rocks" action [SetVariable("journal_group", "journal_group_galerocks")]
                                if description_shortcut01 or description_shortcut02 or description_shortcut03 or description_shortcut04 or description_shortcut05 or description_shortcut06 or description_shortcut07 or description_shortcut08 or description_shortcut09:
                                    textbutton "Heart of the Forest" action [SetVariable("journal_group", "journal_group_shortcut")]
                                if description_highisland00 or description_highisland01 or description_highisland02 or description_highisland03 or description_highisland04 or description_highisland05:
                                    textbutton "High Island" action [SetVariable("journal_group", "journal_group_highisland")]
                                if description_bighunters01 or description_bighunters02 or description_bighunters03 or description_bighunters04 or description_bighunters05 or description_bighunters06:
                                    textbutton "Hunters from Pelt" action [SetVariable("journal_group", "journal_group_bighunters")]
                                if description_hovlavan00:
                                    textbutton "Hovlavan" action [SetVariable("journal_group", "journal_group_hovlavan")]
                                if description_howlersdell01 or description_howlersdell02 or description_howlersdell03 or description_howlersdell04 or description_howlersdell05:
                                    textbutton "Howler’s Dell" action [SetVariable("journal_group", "journal_group_howlersdell")]
                                if description_monastery01 or description_monastery02 or description_monastery03 or description_monastery04 or description_monastery05 or description_monastery06 or description_monastery07:
                                    textbutton "Monks" action [SetVariable("journal_group", "journal_group_monastery")]
                                if description_oldpagos00 or description_oldpagos01 or description_oldpagos02 or description_oldpagos03 or description_oldpagos03a or description_oldpagos04 or description_oldpagos05:
                                    textbutton "Old Págos" action [SetVariable("journal_group", "journal_group_oldpagos")]
                                # if description_ruinedvillage01 or description_ruinedvillage02 or description_ruinedvillage03 or description_ruinedvillage04 or description_ruinedvillage05:
                                #     textbutton "[ruinedvillage_name]" action [SetVariable("journal_group", "journal_group_ruinedvillage")]
                                if description_whitemarshes01 or description_whitemarshes01a or description_whitemarshes02 or description_whitemarshes03 or description_whitemarshes04 or description_whitemarshes05 or description_whitemarshes11 or description_whitemarshes12 or description_whitemarshes13:
                                    textbutton "White Marshes" action [SetVariable("journal_group", "journal_group_whitemarshes")]

                    hbox:
                        xmaximum 1100
                        viewport id "journalgroups":
                            draggable True
                            xmaximum 1008
                            mousewheel True
                            xpos 66
                            vbox:
                                style_prefix "journal"
                                xalign 0.0
                                yalign 0.0
                                xpos 80
                                xmaximum 968
                                ypos 10
                                spacing 20
                                #######
                                if journal_group == "journal_group_bandits":
                                    label _("{color=#f6d6bd}Bandits’ Camp{/color}"):
                                        style "journal_prompt"
                                    text "[description_bandits00]"
                                    if quest_intelforpeltnorth or description_glaucia01 or description_glaucia03 or description_glaucia04 or description_glaucia05 or description_glaucia07 or description_glaucia08 or description_glaucia09:
                                        text "They are led by a woman named {color=#f6d6bd}Glaucia{/color}."
                                    if banditshideout_pcknowswhere:
                                        text "I heard that to find {color=#f6d6bd}the hideout{/color} I need to enter the shortcut that leads through the heart of the forest, reach the cairn, then turn north and enter the wilderness."
                                        if banditshideout_knowsaboutlumberjackcamp_knowsbanditsareinlumberjackcamp:
                                            text "They are occupying an old woodcutter camp."
                                    if quest_intelforpeltnorth_description03:
                                        text "It looks like the bandits have been especially harsh toward the village of {color=#f6d6bd}White Marshes{/color}."
                                    if banditshideout_galerocks_tiestobandits:
                                        text "I heard they have strong ties to {color=#f6d6bd}Gale Rocks{/color}"
                                    if pyrrhos_about_bandits:
                                        text "According to {color=#f6d6bd}the scavenger{/color}, “they are somewhere in the North, in some sort of hideout. I stuck to the western road and no soul bothered me.”"
                                    if description_bandits06:
                                        text "[description_bandits06]"
                                    if description_glaucia07:
                                        text "{color=#f6d6bd}Quintus{/color}, the gatekeeper, claims that the bandits have forced him to stay at his post."
                                    if description_bandits01:
                                        text "[description_bandits01]"
                                    if description_bandits02:
                                        text "[description_bandits02]"
                                    if description_bandits03:
                                        text "[description_bandits03]"
                                    if description_bandits04:
                                        text "[description_bandits04]"
                                    if description_bandits05:
                                        text "[description_bandits05]"
                                    if description_bandits07:
                                        text "[description_bandits07]"
                                    if description_bandits08:
                                        text "[description_bandits08]"

                                elif journal_group == "journal_group_creeks":
                                    label _("{color=#f6d6bd}Creeks{/color}"):
                                        style "journal_prompt"
                                    if creeks_firsttime or oldhava_firsttime:
                                        hbox:
                                            # style_prefix "journal"
                                            xalign 0.0
                                            yalign 0.0
                                            # xpos 80
                                            xmaximum 968
                                            ypos 0
                                            box_wrap True
                                            box_wrap_spacing 8
                                            text "Notable dwellers: "
                                            if creeks_firsttime:
                                                text "Carpenter {color=#f6d6bd}Elah{/color}. "
                                            if creeks_firsttime:
                                                text "Hunter {color=#f6d6bd}Efren{/color}. "
                                            if oldhava_firsttime:
                                                text "Farmer {color=#f6d6bd}Old Hava{/color}. "
                                    if description_creeks01:
                                        text "[description_creeks01]"
                                    if description_creeks01a:
                                        text "[description_creeks01a]"
                                    if description_creeks01b:
                                        text "[description_creeks01b]"
                                    if description_creeks02:
                                        text "[description_creeks02]"
                                    if description_creeks03:
                                        text "[description_creeks03]"
                                    if description_creeks04:
                                        text "According to {color=#f6d6bd}[iason_name]{/color}: [description_creeks04]"
                                    if description_creeks05:
                                        text "[description_creeks05]"
                                    if oldpagos_about_creeks:
                                        text "According to {color=#f6d6bd}Tertia{/color}, it was settled briefly after the war: “I’ve heard they came here from the far South, running away from some shady deeds of theirs. Who knows what their children are up to? They drink a lot, even hunt for play, for things they don’t need.”"
                                    if description_creeks06:
                                        text "[description_creeks06]"
                                    if description_creeks07:
                                        text "[description_creeks07]"
                                    if description_creeks08:
                                        text "[description_creeks08]"
                                    if description_creeks09:
                                        text "[description_creeks09]"
                                    if description_creeks10:
                                        text "[description_creeks10]"
                                    if elah_about_creeks:
                                        text "The gist of the story that the people of {color=#f6d6bd}Creeks{/color} are willing to tell goes like this: The settlers arrived here twenty five years ago, soon after one of The Ten Cities had fallen to The Southern Invasion. Most of them came from the very capital, while some joined them along the way. They soon came to realize that none of the villages had enough space or will to host a few dozen refugees. The folks of {color=#f6d6bd}Gale Rocks{/color} used to have a much kinder attitude toward strangers than they do now, and they offered the newcomers to stay at the beach behind their village.\nYet there was nothing for them to eat other than what they caught in the salt waters. They soon started their search for a land remote enough to not compete with the locals, and with the help of kind folks from “{color=#f6d6bd}Gale Rocks{/color}, {color=#f6d6bd}Hwite Marshes{/color}, {color=#f6d6bd}Old Págos{/color}... and others,” they received enough wood and tools to turn a scrap of this plateau into a clearing, then a camp, a hamlet, and finally - a village."
                                elif journal_group == "journal_group_druids":
                                    label _("{color=#f6d6bd}Druids{/color}"):
                                        style "journal_prompt"
                                    text "[description_druids00]"
                                    if description_druids01:
                                        text "[description_druids01]"
                                    if description_druids02:
                                        text "[description_druids02]"
                                    if description_druids11:
                                        text "[description_druids11]"
                                    if description_druids12:
                                        text "[description_druids12]"
                                    if description_druids03:
                                        text "[description_druids03] {color=#f6d6bd}[iason_name]{/color}[description_druids03b]"
                                    if description_druids04a:
                                        text "[description_druids04a]"
                                    if description_druids04:
                                        text "[description_druids04]"
                                    if description_druids05:
                                        text "[description_druids05]"
                                    if description_druids06:
                                        text "[description_druids06]"
                                    if description_druids07:
                                        text "[description_druids07]"
                                    if description_druids08:
                                        text "[description_druids08]"
                                    if description_druids09:
                                        text "[description_druids09]"
                                    if description_druids10:
                                        text "[description_druids10]"

                                elif journal_group == "journal_group_greenmountaintribe":
                                    label _("{color=#f6d6bd}The Tribe of The Green Mountain{/color}"):
                                        style "journal_prompt"
                                    # text "[description_greenmountaintribe00]"
                                    if description_greenmountaintribe01:
                                        text "[description_greenmountaintribe01]"
                                    if description_greenmountaintribe02:
                                        text "[description_greenmountaintribe02]"
                                    if description_greenmountaintribe03:
                                        text "[description_greenmountaintribe03]"
                                    if description_greenmountaintribe08:
                                        text "[description_greenmountaintribe08]"
                                    if description_greenmountaintribe09:
                                        text "[description_greenmountaintribe09]"
                                    if description_greenmountaintribe11:
                                        text "[description_greenmountaintribe11]"
                                    if description_greenmountaintribe04:
                                        text "[description_greenmountaintribe04]"
                                    if description_greenmountaintribe05:
                                        text "[description_greenmountaintribe05]"
                                    if oldpagos_about_creeks:
                                        text "According to {color=#f6d6bd}Tertia{/color}, “they were always known for their blood magic.”"
                                    if description_greenmountaintribe06:
                                        text "[description_greenmountaintribe06]"
                                    if description_greenmountaintribe07:
                                        text "[description_greenmountaintribe07]"
                                    if description_greenmountaintribe10:
                                        text "[description_greenmountaintribe10]"
                                    if description_greenmountaintribe12:
                                        text "[description_greenmountaintribe12]"
                                    if description_greenmountaintribe13:
                                        text "[description_greenmountaintribe13]"
                                    if cephasgaiane_about_highisland_question3:
                                        text "{color=#f6d6bd}Gaiane’s{/color} story about The Tribe went like this:"
                                        text "The Green Mountain, the life-giving volcano in the center of the island, has been home to the Tribe for longer than anyone can remember, “as we’re older ‘tan any of T’ Ten Cities” - though you doubt there are any ways to verify such a claim. {color=#f6d6bd}The shaman{/color} spends a good few minutes describing the filling years of her ancestors - through hardship, they’ve managed to tame enough land to grow vegetables, and made a great chunk of the island their forest garden. After finding the iron and copper veins, they had enough tools and weapons to save their offspring from back-breaking labor. She’s also eager to describe the deeds of many families and heroes, and the unique herbs with their “beautiful names”, but {color=#f6d6bd}the chief{/color} asks her to move on."
                                        text "For most of its existence, {color=#f6d6bd}Hovlavan{/color} avoided the island, finding hardship in getting close to it, and since “the pagans” were reluctant to accept dragon bones, the merchants saw little value in their wares. However, once the tribes of the peninsula noticed the growing supplies of alloys used by the islandfolk and their fishers, the news reached the city."
                                        text "A little more than two hundred years ago, the officials tried to negotiate the new trade deal with the locals, but to no avail. Finally, they allowed the corsairs to start their usual efforts, putting to use the growing height of their ships. At first, they were bothering the fishers, then landing on the island itself. The Tribe was ready to fight over their possession, but the cruelty they faced outmatched them. The kidnappings made the locals afraid to leave their walls, and then the raids enslaved whole hamlets, or burned many crucial structures."
                                        text "Using traps and knowledge of the terrain, The Tribe managed to kill more than they lost, but the corsair ships kept coming, always led by new, yet even more experienced captains. After a few bloody battles, the forest fires started, and the locals understood they had little time before the wrath of the herds would trample them to death."
                                        text "“We are t’ eight’ generation of T’ Tribe living here, so close to t’ coast, yet so far from it,” she ends her tale. “Taming t’ new grounds was harsh, and once t’ first children born in ‘tese tunnels started breat’ing, only a fift’ of T’ Tribe was still here to welcome ‘em.”"

                                elif journal_group == "journal_group_galerocks":
                                    label _("{color=#f6d6bd}Gale Rocks{/color}"):
                                        style "journal_prompt"
                                    if galerocks_firsttime and galerocks_npcsmet:
                                        hbox:
                                            # style_prefix "journal"
                                            xalign 0.0
                                            yalign 0.0
                                            # xpos 80
                                            xmaximum 968
                                            ypos 0
                                            box_wrap True
                                            box_wrap_spacing 8
                                            text "Notable dwellers: "
                                            # if galerocks_albus_firsttime:
                                            #     text "Salter {color=#f6d6bd}Albus{/color}. "
                                            if galerocks_aquila_firsttime:
                                                text "Bath man {color=#f6d6bd}Aquila{/color}. "
                                            # if galerocks_domitia_firsttime:
                                            #     text "Cooper {color=#f6d6bd}Domitia{/color}. "
                                            if galerocks_fulvia_firsttime:
                                                text "Shelter keeper {color=#f6d6bd}Fulvia{/color}. "
                                            # if galerocks_florus_firsttime:
                                            #     text "Fletcher {color=#f6d6bd}Florus{/color}. "
                                            if galerocks_iuno_firsttime:
                                                text "Digger {color=#f6d6bd}Iuno{/color}. "
                                            if galerocks_navica_firsttime:
                                                text "Boatmaker {color=#f6d6bd}Navica{/color}. "
                                            if galerocks_petronius_firsttime:
                                                text "Gossiper {color=#f6d6bd}Petronius{/color}. "
                                            if galerocks_photios_firsttime:
                                                text "Fisher {color=#f6d6bd}Photios{/color}. "
                                            if galerocks_porcia_firsttime:
                                                text "Cook {color=#f6d6bd}Porcia{/color}. "
                                            if galerocks_rufina_firsttime:
                                                text "Tailor {color=#f6d6bd}Rufina{/color}. "
                                            if severina_firsttime:
                                                text "Headwoman {color=#f6d6bd}Severina{/color}. "
                                            if galerocks_tatius_firsttime:
                                                text "Armorer {color=#f6d6bd}Tatius{/color}. "
                                    if description_galerocks01:
                                        text "[description_galerocks01]"
                                    if description_galerocks02:
                                        text "[description_galerocks02]"
                                    if description_galerocks03:
                                        text "[description_galerocks03]"
                                    if description_galerocks04:
                                        text "[description_galerocks04]"
                                    if description_galerocks14:
                                        text "[description_galerocks14]"
                                    if description_galerocks15:
                                        text "[description_galerocks15]"
                                    if description_galerocks05:
                                        text "[description_galerocks05]"
                                    if description_galerocks12:
                                        text "[description_galerocks12]"
                                    if description_galerocks13:
                                        text "[description_galerocks13]"
                                    if description_galerocks08:
                                        text "[description_galerocks08]"
                                    if iason_about_severina:
                                        text "According to {color=#f6d6bd}[iason_name]{/color}, I should always call {color=#f6d6bd}Severina{/color} a {i}headwoman{/i}, instead of mayor or a chief. He also told me to visit her only when I’m clean, so I can show her proper respect, and to “treat her as if she’s a city official. Be brief, don’t ask for favors, don’t threaten. Say what you have to, don’t argue for long.”"
                                    if iason_about_navica:
                                        text "According to {color=#f6d6bd}[iason_name]{/color}, {color=#f6d6bd}Navica{/color}, the boatmaker, is “all about work, and gets shaky if anyone raises their voice around her, or even laughs too loudly.”"
                                    if oldpagos_about_galerocks:
                                        text "According to {color=#f6d6bd}Tertia{/color}, they follow Wright’s teachings, but have betrayed the trust of the people of {color=#f6d6bd}Old Págos{/color} by stealing their belongings."
                                    if description_galerocks06:
                                        text "[description_galerocks06]"
                                    if description_galerocks07:
                                        text "[description_galerocks07]"
                                    if aegidia_about_arrow:
                                        text "They produce arrows that match the one I found near the destroyed wagon."
                                    if description_galerocks09:
                                        text "[description_galerocks09]"
                                    if description_galerocks10:
                                        text "[description_galerocks10]"
                                    if description_galerocks11:
                                        text "[description_galerocks11]"

                                elif journal_group == "journal_group_highisland":
                                    label _("{color=#f6d6bd}High Island{/color}"):
                                        style "journal_prompt"
                                    if description_highisland00:
                                        text "[description_highisland00]"
                                    if description_highisland01:
                                        text "[description_highisland01]"
                                    if description_highisland02:
                                        text "[description_highisland02]"
                                    if description_highisland03:
                                        text "[description_highisland03]"
                                    if description_highisland04:
                                        text "[description_highisland04]"
                                    if description_highisland05:
                                        text "[description_highisland05]"
                                    if description_highisland12:
                                        text "[description_highisland12]"
                                    if description_highisland13:
                                        text "[description_highisland13]"
                                    if description_highisland06:
                                        text "[description_highisland06]"
                                    if description_highisland07:
                                        text "[description_highisland07]"
                                    if description_highisland08:
                                        text "[description_highisland08]"
                                    if description_highisland09:
                                        text "[description_highisland09]"
                                    if description_highisland10:
                                        text "[description_highisland10]"
                                    if description_highisland11:
                                        text "[description_highisland11]"
                                    if description_highisland15:
                                        text "[description_highisland15]"

                                elif journal_group == "journal_group_howlersdell":
                                    label _("{color=#f6d6bd}Howler’s Dell{/color}"):
                                        style "journal_prompt"
                                    if howlersdell_eryx_firsttime or howlersdell_bion_firsttime or howlersdell_akakios_firsttime or howlersdell_elpis_firsttime:
                                        hbox:
                                            # style_prefix "journal"
                                            xalign 0.0
                                            yalign 0.0
                                            # xpos 80
                                            xmaximum 968
                                            ypos 0
                                            box_wrap True
                                            box_wrap_spacing 8
                                            text "Notable dwellers: "
                                            if howlersdell_akakios_firsttime:
                                                text "Trader {color=#f6d6bd}Akakios{/color}. "
                                            if howlersdell_bion_firsttime:
                                                text "Tailor {color=#f6d6bd}Bion{/color}. "
                                            if howlersdell_elpis_firsttime and description_druids07:
                                                text "Druidess {color=#f6d6bd}Elpis{/color}. "
                                            elif howlersdell_elpis_firsttime:
                                                text "{color=#f6d6bd}Druids{/color}. "
                                            if howlersdell_eryx_firsttime:
                                                text "Innkeeper {color=#f6d6bd}Eryx{/color}. "
                                            if pyrrhos_howlersdell and description_pyrrhos01:
                                                text "Scavenger {color=#f6d6bd}Pyrrhos{/color}. "
                                            elif pyrrhos_howlersdell:
                                                text "{color=#f6d6bd}The scavenger{/color}. "
                                            if thaisfirstconversation:
                                                text "Mayor {color=#f6d6bd}Thais{/color}. "
                                    if description_howlersdell01:
                                        text "[description_howlersdell01]"
                                    if description_howlersdell03:
                                        text "[description_howlersdell03]"
                                    if description_howlersdell04:
                                        text "[description_howlersdell04]"
                                    if oldpagos_about_howlersdell:
                                        text "According to {color=#f6d6bd}Tertia{/color}: “Don’t let them cloud your eyes. They have plenty of food, riches, mead, pretty houses. But there’s poison in all of it. The poison of those who lead them.”"
                                    if description_howlersdell05:
                                        text "[description_howlersdell05]"
                                    if description_howlersdell06:
                                        text "[description_howlersdell06]"
                                    if description_howlersdell06a:
                                        text "[description_howlersdell06a][description_howlersdell06b]"
                                    if description_howlersdell07:
                                        text "[description_howlersdell07]"
                                    if description_howlersdell08:
                                        text "[description_howlersdell08][description_howlersdell08a]"
                                    if description_howlersdell09:
                                        text "[description_howlersdell09]"
                                    if description_howlersdell10:
                                        text "[description_howlersdell10]"
                                    if description_howlersdell02:
                                        text "[description_howlersdell02]"

                                elif journal_group == "journal_group_hovlavan":
                                    label _("{color=#f6d6bd}The City of Hovlavan{/color}"):
                                        style "journal_prompt"
                                    text "[description_hovlavan00]"
                                    #### PC's relationship with the city
                                    if thais_hovlavan04: # is player from the city
                                        text "[thais_hovlavan04]"
                                    if pc_home_druid == "notfromthecity":
                                        text "I wasn’t born in the city, and that’s the reason why I know this and that about herbs."
                                    elif pc_home_druid == "cityhasroofgardens":
                                        text "You’ll find a garden on every scrap of free space in the city - on the roofs, outside of the city wall wall, and in small patches."
                                    elif pc_home_druid == "cityneighbors":
                                        text "I used to have neighbors there who used to be farmers before they lost their home in the war. They taught me a lot about herbs."
                                    elif pc_home_druid == "citymonasterygarden":
                                        text "The local monastery has a great garden with all sorts of valuable plants. The caretakers were willing to share their knowledge about herbs with me."
                                    elif pc_home_druid == "citybooks":
                                        text "While I was there, I had an access to many valuable books, such as the herbaria, which were crucial to me."
                                    if description_hovlavan19: # ignoring the drunk people
                                        text "[description_hovlavan19]"
                                    if hovlavan_humaninteraction == "trueloneliness": # loneliness and friendships
                                        text "There are many people in the city, but all of them are too busy with their duties to share their lives with others. I hate the loneliness it brings."
                                    elif hovlavan_humaninteraction == "okloneliness":
                                        text "There are many people in the city, but all of them are too busy with their duties to share their lives with others. It brings loneliness, but I can deal with it."
                                    elif hovlavan_humaninteraction == "onlyfamilies":
                                        text "Cityfolk spend time with their families and close friends, usually people they work with. They are close to each other, but no soul knows what happens behind doors. In the evenings, the streets feel empty."
                                    elif hovlavan_humaninteraction == "closefriendships":
                                        text "It’s hard to get to know new people when everyone’s so busy, but kids spend a lot of time together, and build long-time friendships."
                                    elif hovlavan_humaninteraction == "thinfriendships":
                                        text "In there, one can easily find groups to hang out with. People shop together, work, take baths, pray, and when one has nothing to do in the evening, they just go outside and seek company. It’s not easy to build a strong friendship, though."
                                    elif hovlavan_humaninteraction == "okdistrust":
                                        text "In there, the merchants are getting richer, the priests have their games, craft guilds decide who goes in and out, and the workers have to compete. There are no monsters on the streets, at least not every day, but there is distrust in many souls. It’s a place darker than the heart of the woods... Unless you are at the top."
                                    elif hovlavan_humaninteraction == "truedistrust":
                                        text "In there, the merchants are getting richer, the priests have their games, craft guilds decide who goes in and out, and the workers have to compete. There are no monsters on the streets, at least not every day, but there is distrust in many souls. It’s a place darker than the heart of the woods."
                                    #### the city's geography, areas, and such
                                    if thais_hovlavan01 == 1: # the general state of the city
                                        text "It has managed to heal from the wounds it took during The Southern Invasion. It prospers and grows comfortable."
                                    elif thais_hovlavan01 == 2:
                                        text "It’s been healing slowly ever since The Southern Invasion, but the new generation is ready to start their own fight."
                                    elif thais_hovlavan01 == 3:
                                        text "It’s been struggling ever since The Southern Invasion. Children who lost their parents during the war have no trade in hand and there’s not enough settlements to send them away."
                                    if pc_sea_fluff:
                                        text "The port and the sea are full of ships, warehouses, traders, dockers. There’s also the Sickle, the barrier island that provides the city with its lagoon, but also serves as a home to dozens of species of birds, monkeys, and rodents. For most people, the sea is never silent."
                                    if bestiary_seamonsters_city == "creaturesstayaway":
                                        text "The nearby waters are rather safe. The monsters are used to avoiding areas crowded with the guards and sailors."
                                    elif bestiary_seamonsters_city == "creaturesattackdrunkards":
                                        text "There are many creatures living close to the harbor. They wait for trash or drunkards to fall off of a bridge."
                                    elif bestiary_seamonsters_city == "creaturesgetontheland":
                                        text "It struggles with severe attacks of creatures from the seas that show up between the boats, or even enter the streets. People learn to run away and leave it to the soldiers, but from time to time there are casualties."
                                    elif bestiary_seamonsters_city == "flyingmonsters":
                                        text "It struggles with constant issues caused by the harpies and other flying creatures. Most of the regular folks carry spears, and the children are rarely allowed to play on the streets without supervision."
                                    if thais_hovlavan02 == 1: # the Backwood Corner
                                        text "The Backwood Corner used to be a poor area, but the war turned it into a home of thugs."
                                    elif thais_hovlavan02 == 2:
                                        text "The Backwood Corner used to be a poor area, but it’s now a respectable place, and hides one of the fanciest inns in the city - The Apple And The Boar."
                                    elif thais_hovlavan02 == 3:
                                        text "I know The Backwood Corner well, the {i}bad{/i} part of the city. It’s dark and dirty, but cheap, especially The Boarhead Inn."
                                    elif thais_hovlavan02 == 4:
                                        text "The Backwood Corner used to be a poor area, but it all turned to ashes many years back."
                                    if westerncrossroads_firsttime and description_hovlavan04 == "nooldstatues":
                                        text "The roads closer to the city are often patrolled, and much wider and more convenient than they are in the countryside. Still, the people treat them as not a place {i}for{/i} them."
                                    elif westerncrossroads_firsttime and description_hovlavan04 == "oldstatuesnoattention":
                                        text "The roads closer to the city are often patrolled, and much wider and more convenient than they are in the countryside. There are even some old statues placed near them, but I never paid much attention to them."
                                    elif westerncrossroads_firsttime and description_hovlavan04 == "oldstatuesofheroes":
                                        text "The roads closer to the city are often patrolled, and much wider and more convenient than they are in the countryside. There are various old statues placed near them, portraying heroes of Wright’s Tablets, local champions, famous adventurers, and such."
                                    elif westerncrossroads_firsttime and description_hovlavan04 == "oldstatuesofthemselves":
                                        text "The roads closer to the city are often patrolled, and much wider and more convenient than they are in the countryside. There are various statues placed near them, most of which are of rich merchants and artisans who want to be remembered after their souls leave them."
                                    elif westerncrossroads_firsttime and description_hovlavan04 == "oldstatuesofimportantplaces":
                                        text "The roads closer to the city are often patrolled, and much wider and more convenient than they are in the countryside. There are various old statues placed near them, and they mark places of importance, or spots where an important event has happened."
                                    elif westerncrossroads_firsttime:
                                        text "The roads closer to the city are often patrolled, and much wider and more convenient than they are in the countryside."
                                    #### the city's culture and people
                                    if thais_hovlavan06 == 1: # the influence of the church
                                        text "The United Church stands strong in the city, and so do its laws. {color=#f6d6bd}Hovlavan{/color} is still loyal to the Empress, even if she’s not around."
                                    elif thais_hovlavan06 == 2:
                                        text "The United Church stands strong in the city, and so do its laws. {color=#f6d6bd}Hovlavan{/color} is still loyal to the Empress, even if she’s not around."
                                    elif thais_hovlavan06 == 3:
                                        text "The local Unites are matched by the new order of Seekers, but nothing is set in stone yet."
                                    elif thais_hovlavan06 == 4:
                                        text "The United Church isn’t as influential as it used to be. Soon after the war, the army had to take over, and never let go of its power."
                                    elif thais_hovlavan06 == 5:
                                        text "The United Church isn’t as influential as it used to be. The maritime trade keeps the city alive. The merchants took the lead in the game."
                                    elif thais_hovlavan06 == 6:
                                        text "I don’t follow the city politics too keenly."
                                    if tulia_about_herself:
                                        text "According to {color=#f6d6bd}Tulia{/color}: “{color=#f6d6bd}Hovlavan{/color} chief selects commanders, the commanders select lieutenants, and every lieutenant puts all of their soldiers in order of priority. If a lieutenant dies, they get replaced by the next soldier in line.”"
                                    if thais_hovlavan03 == 1: # clothes
                                        text "People there dress the same way they always did. There’s always a shortage of fabric."
                                    elif thais_hovlavan03 == 2:
                                        text "For years there was not enough hemp and wool at hand, so people have started to wear furs again."
                                    elif thais_hovlavan03 == 3:
                                        text "A lot of the cityfolk wear impractical headgear."
                                    elif thais_hovlavan03 == 4:
                                        text "People there dress the same way they always did, nothing special."
                                    if thais_hovlavan05 == 1: # common animals
                                        text "The ibexes are especially common in the nearby villages. They do well on the hills."
                                    elif thais_hovlavan05 == 2:
                                        text "The mouflons are especially common in the nearby villages. The monks need their parchment."
                                    elif thais_hovlavan05 == 3:
                                        text "The nearby villages mostly breed fowl and hunt for fish, but some of them raise boars."
                                    elif thais_hovlavan05 == 4:
                                        text "The locals are a bit desperate for meat. They mostly eat crickets and rats."
                                    if hovlavan_music == "shanties":
                                        text "The cityfolk often sing the sea shanties during long hours of labor."
                                    elif hovlavan_music == "oldtunes":
                                        text "The cityfolk find great strength while they sing the patriotic tunes from the old days."
                                    elif hovlavan_music == "tame":
                                        text "The songs in the city are rather tame - some themes don’t sound so good when the priests are around."
                                    elif hovlavan_music == "no":
                                        text "The cityfolk rarely sing during work, as they treat their trade very seriously."
                                    if hovlavan_nakedness == "prudeness":
                                        text "When it comes to sex and nudity, the cityfolk are prude. They go to small bathhouses and pay for their privacy. It’s impolite to glance at a naked stranger."
                                    elif hovlavan_nakedness == "justbaths":
                                        text "When it comes to nudity, the cityfolk don’t feel ashamed of bathing with others, though they manage to keep a bit of a distance."
                                    elif hovlavan_nakedness == "ribald":
                                        text "When it comes to sex and nudity, the cityfolk are far from being prude."
                                    elif hovlavan_nakedness == "status":
                                        text "Like everything in the city, the relationship with sex and nudity is tied to one’s status. The rich folk bathe in luxurious rooms and invite or pay for many lovers, while most people have rather humble experiences."
                                    ##### UNUSED
                                    if description_hovlavan01:
                                        text "[description_hovlavan01]"
                                    if description_hovlavan02:
                                        text "[description_hovlavan02]"
                                    if description_hovlavan03:
                                        text "[description_hovlavan03]"
                                    if description_hovlavan05:
                                        text "[description_hovlavan05]"
                                    if description_hovlavan06:
                                        text "[description_hovlavan06]"
                                    if description_hovlavan07:
                                        text "[description_hovlavan07]"
                                    if description_hovlavan08:
                                        text "[description_hovlavan08]"
                                    if description_hovlavan09:
                                        text "[description_hovlavan09]"
                                    if description_hovlavan10:
                                        text "[description_hovlavan10]"
                                    if description_hovlavan11:
                                        text "[description_hovlavan11]"
                                    if description_hovlavan12:
                                        text "[description_hovlavan12]"
                                    if description_hovlavan13:
                                        text "[description_hovlavan13]"
                                    if description_hovlavan14:
                                        text "[description_hovlavan14]"
                                    if description_hovlavan15:
                                        text "[description_hovlavan15]"
                                    if description_hovlavan16:
                                        text "[description_hovlavan16]"
                                    if description_hovlavan17:
                                        text "[description_hovlavan17]"
                                    if description_hovlavan18:
                                        text "[description_hovlavan18]"
                                    if description_hovlavan20:
                                        text "[description_hovlavan20]"

                                elif journal_group == "journal_group_bighunters":
                                    label _("{color=#f6d6bd}Hunters From Pelt{/color}"):
                                        style "journal_prompt"
                                    #text "[description_bighunters00]"
                                    if description_bighunters01:
                                        text "[description_bighunters01] [iason_name]."
                                    if description_bighunters02:
                                        text "[description_bighunters02] {color=#f6d6bd}[iason_name]{/color}[description_bighunters02b]"
                                    if description_bighunters03:
                                        text "[description_bighunters03]"
                                    if description_bighunters04:
                                        text "[description_bighunters04]"
                                    if description_bighunters05:
                                        text "[description_bighunters05]"
                                    if description_bighunters06:
                                        text "[description_bighunters06]"
                                    if description_bighunters10:
                                        text "[description_bighunters10]"

                                elif journal_group == "journal_group_monastery":
                                    label _("{color=#f6d6bd}Monks from Old Págos{/color}"):
                                        style "journal_prompt"
                                    text "[description_monastery00]"
                                    if description_monastery01:
                                        text "According to {color=#f6d6bd}[iason_name]{/color}, [description_monastery01]"
                                    if description_monastery02:
                                        text "[description_monastery02]"
                                    if description_monastery07:
                                        text "[description_monastery07]"
                                    if description_monastery03:
                                        text "[description_monastery03]"
                                    if description_monastery04:
                                        text "[description_monastery04]"
                                    if description_monastery05:
                                        text "[description_monastery05]"
                                    if description_monastery06:
                                        text "[description_monastery06]"
                                    if description_aeli00:
                                        text "[description_aeli00]"
                                    if description_aeli01:
                                        text "[description_aeli01] {color=#f6d6bd}[iason_name]{/color}[description_aeli01a]"

                                elif journal_group == "journal_group_oldpagos":
                                    label _("{color=#f6d6bd}Old Págos{/color}"):
                                        style "journal_prompt"
                                    if description_oldpagos00:
                                        text "[description_oldpagos00]"

                                    if description_tertia00:
                                        text "[description_tertia00]"
                                    if description_tertia01:
                                        text "[description_tertia01] {color=#f6d6bd}[iason_name]{/color}[description_tertia01a]"
                                    if description_tertia02:
                                        text "[description_tertia02]"
                                    if description_tertia03:
                                        text "[description_tertia03]"


                                    if description_oldpagos01:
                                        text "[description_oldpagos01]"
                                    if oldpagos_plague_known:
                                        text "It’s been struggling with a mysterious plague."
                                    if description_oldpagos02:
                                        text "[description_oldpagos02]"
                                    if description_oldpagos03:
                                        text "[description_oldpagos03]"
                                    if description_oldpagos03a:
                                        text "[description_oldpagos03a]"
                                    if description_oldpagos04:
                                        text "[description_oldpagos04]"
                                    if description_oldpagos04a:
                                        text "[description_oldpagos04a]"
                                    if description_oldpagos05:
                                        text "According to {color=#f6d6bd}[dalit_name]{/color}, [description_oldpagos05]"
                                    if quintus_about_leaving:
                                        text "According to {color=#f6d6bd}Quintus{/color}, {color=#f6d6bd}Old Págos{/color} has no allies."
                                    if description_oldpagos06:
                                        text "[description_oldpagos06]"
                                    if description_oldpagos07:
                                        text "[description_oldpagos07]"
                                    if description_oldpagos08:
                                        text "[description_oldpagos08]"
                                    if description_oldpagos09:
                                        text "[description_oldpagos09]"
                                    if description_oldpagos10:
                                        text "[description_oldpagos10]"

                                elif journal_group == "journal_group_shortcut":
                                    label _("{color=#f6d6bd}The Heart of the Forest{/color}"):
                                        style "journal_prompt"
                                    if description_shortcut00:
                                        text "[description_shortcut00]"
                                    if description_shortcut01:
                                        text "[description_shortcut01]"
                                    if quest_ruins_10yclue09:
                                        text "People stopped using it about ten years ago."
                                    if description_shortcut03:
                                        text "[description_shortcut03]"
                                    if banditshideout_pcknowswhere:
                                        text "It looks like the bandits have their {color=#f6d6bd}hideout{/color} down this road. To reach it, one needs to reach the cairn in the middle of the road, then turn north and enter the wilderness."
                                    if description_shortcut02:
                                        text "[description_shortcut02]"
                                    if description_shortcut04:
                                        text "[description_shortcut04]"
                                    if description_shortcut05:
                                        text "[description_shortcut05]"
                                    if description_shortcut06:
                                        text "[description_shortcut06]"
                                    if galerocks_fulvia_about_shortcut2:
                                        text "According to {color=#f6d6bd}Fulvia{/color}, it’s possible that the old orchard is still looked after by “{color=#f6d6bd}The Green Mountain Tribe{/color}”."
                                    elif galerocks_fulvia_about_shortcut:
                                        text "According to {color=#f6d6bd}Fulvia{/color}, there used to be an old orchard in this part of the woods, with many beasts threatening those who tried to take too much at once. According to her, it’s better to focus on picking up the hazelnuts."
                                    if description_shortcut07:
                                        text "[description_shortcut07]"
                                    if description_shortcut08:
                                        text "[description_shortcut08]"
                                    if description_shortcut09:
                                        text "According to {color=#f6d6bd}[dalit_name]{/color}: [description_shortcut09]"
                                    if description_shortcut10:
                                        text "[description_shortcut10]"
                                    if shortcut_cairn_interacted == 2:
                                        text "The cairn built in the middle of the road has been touched with magic in the past, though it’s unclear if it has any powers left."

                                elif journal_group == "journal_group_ruinedvillage":
                                    label _("{color=#f6d6bd}[ruinedvillage_name]{/color}"):
                                        style "journal_prompt"
                                    # text "[description_ruinedvillage00]"
                                    if quest_ruins_description_origins:
                                        text "[quest_ruins_description_origins]"
                                    if quest_ruins_description_glauciasperspective:
                                        text "[quest_ruins_description_glauciasperspective]"
                                    if description_ruinedvillage01:
                                        text "[description_ruinedvillage01] {color=#f6d6bd}[iason_name]{/color}[description_ruinedvillage01a]"
                                    elif quest_ruins_description01:
                                        text "[quest_ruins_description01]"
                                    if description_ruinedvillage02:
                                        text "[description_ruinedvillage02]"
                                    if description_ruinedvillage03:
                                        text "[description_ruinedvillage03]"
                                    if description_ruinedvillage04:
                                        text "[description_ruinedvillage04]"
                                    if description_ruinedvillage05:
                                        text "[description_ruinedvillage05]"
                                    if description_ruinedvillage06:
                                        text "[description_ruinedvillage06]"
                                    if description_ruinedvillage07:
                                        text "[description_ruinedvillage07]"
                                    if description_ruinedvillage08:
                                        text "[description_ruinedvillage08]"
                                    if description_ruinedvillage09:
                                        text "[description_ruinedvillage09]"
                                    if description_ruinedvillage10:
                                        text "[description_ruinedvillage10]"

                                elif journal_group == "journal_group_whitemarshes":
                                    label _("{color=#f6d6bd}White Marshes{/color}"):
                                        style "journal_prompt"
                                    if whitemarshes_destroyed:
                                        text "The haunted ruins spread across the western bogs."
                                    else:
                                        if description_whitemarshes01:
                                            text "[description_whitemarshes01]"
                                        if description_whitemarshes00:
                                            text "[description_whitemarshes00]"
                                        if whitemarshes_valens_shop_firsttime:
                                            text "{color=#f6d6bd}Valens{/color} is willing to purchase all sorts of food."
                                        if description_whitemarshes01a:
                                            text "[description_whitemarshes01a]"
                                        if description_whitemarshes_helvius01:
                                            text "[description_whitemarshes_helvius01]"
                                        if description_whitemarshes_helvius02:
                                            text "According to {color=#f6d6bd}[iason_name]{/color}, [description_whitemarshes_helvius02]"
                                        if description_whitemarshes15:
                                            text "[description_whitemarshes15]"
                                        if description_whitemarshes17:
                                            text "[description_whitemarshes17]"
                                        if description_whitemarshes14:
                                            text "[description_whitemarshes14]"
                                        if description_whitemarshes13:
                                            text "[description_whitemarshes13]"
                                        if description_whitemarshes11:
                                            text "[description_whitemarshes11]"
                                        if description_whitemarshes02:
                                            text "[description_whitemarshes02][description_whitemarshes02a]"
                                        if description_whitemarshes03:
                                            text "[description_whitemarshes03]"
                                        if description_whitemarshes04:
                                            text "[description_whitemarshes04]"
                                        if description_whitemarshes05:
                                            text "[description_whitemarshes05]"
                                        if oldpagos_about_whitemarshes:
                                            text "According to {color=#f6d6bd}Tertia{/color}: “The road to them is dangerous. Weird creatures live in the swamps, yelling with human-like voices, luring travelers to leave the path. When ya knees are in water, they, these beasts, jump from a tree onto ya back, biting ya skin off. That’s just what {color=#f6d6bd}White Marshes{/color} are. Ye may think it’s a part of the realm of humans, but not any more than a bear trap set in the woods.”"
                                        if description_whitemarshes06:
                                            text "[description_whitemarshes06]"
                                        if description_whitemarshes07:
                                            text "[description_whitemarshes07]"
                                        if description_whitemarshes08:
                                            text "[description_whitemarshes08]"
                                        if description_whitemarshes09:
                                            text "[description_whitemarshes09]"
                                        if description_whitemarshes10:
                                            text "[description_whitemarshes10]"
                                        if description_whitemarshes12:
                                            text "[description_whitemarshes12]"

                                #######
                                else:
                                    text "No group selected."
                        vbar value YScrollValue ("journalgroups"):
                            xpos 60
                            unscrollable "hide"

                elif journalmode == "bestiary":
                    hbox:
                        xmaximum 330
                        viewport id "listbeasts":
                            draggable True
                            xmaximum 320
                            mousewheel True
                            xpos 10
                            vbox:
                                style_prefix "journal"
                                xalign 0.0
                                yalign 0.0
                                xmaximum 320
                                xpos 10
                                ypos 6
                                spacing 20
                                textbutton "Apes and monkeys" action [SetVariable("journal_beast", "beastapesdescription")]
                                textbutton "Beastfolk" action [SetVariable("journal_beast", "beastfolkdescription")]
                                textbutton "Corpse eaters" action [SetVariable("journal_beast", "beastcorpseeatersdescription")]
                                textbutton "Dragonlings" action [SetVariable("journal_beast", "beastdragonlingsdescription")]
                                textbutton "Dragons" action [SetVariable("journal_beast", "beastdragonsdescription")]
                                textbutton "Foxes and such" action [SetVariable("journal_beast", "beastmediumcrittersdescription")]
                                textbutton "Gargoyles" action [SetVariable("journal_beast", "beastgargoylesdescription")]
                                textbutton "Goblins" action [SetVariable("journal_beast", "beastgoblinsdescription")]
                                textbutton "Golems" action [SetVariable("journal_beast", "beastgolemsdescription")]
                                textbutton "Griffons" action [SetVariable("journal_beast", "beastgriffonsdescription")]
                                textbutton "Harpies" action [SetVariable("journal_beast", "beastharpiesdescription")]
                                textbutton "Howlers" action [SetVariable("journal_beast", "beasthowlersdescription")]
                                textbutton "Huntlords" action [SetVariable("journal_beast", "beasthuntlordsdescription")]
                                textbutton "Large cats" action [SetVariable("journal_beast", "beastlargecatsdescription")]
                                textbutton "Pebblers" action [SetVariable("journal_beast", "beastpebblersdescription")]
                                textbutton "Runners" action [SetVariable("journal_beast", "beastrunningbirdsdescription")]
                                textbutton "Saurians" action [SetVariable("journal_beast", "beastsauriansdescription")]
                                textbutton "Spiders" action [SetVariable("journal_beast", "beastspidersdescription")]
                                textbutton "Treants" action [SetVariable("journal_beast", "beasttreantsdescription")]
                                textbutton "Trolls" action [SetVariable("journal_beast", "beasttrollsdescription")]
                                textbutton "Undead" action [SetVariable("journal_beast", "beastundeaddescription")]
                                textbutton "Unicorns" action [SetVariable("journal_beast", "beastunicornsdescription")]
                                textbutton "Wolves" action [SetVariable("journal_beast", "beastwolvesdescription")]
                        vbar value YScrollValue ("listbeasts"):
                            xpos 30
                            unscrollable "hide"
                    hbox:
                        xmaximum 1100
                        viewport id "journalbeasts":
                            draggable True
                            xmaximum 1008
                            mousewheel True
                            xpos 80
                            vbox:
                                style_prefix "journal"
                                xalign 0.0
                                yalign 0.0
                                xpos 80
                                xmaximum 968
                                ypos 10
                                spacing 20
                                #######
                                if journal_beast == "beastapesdescription":
                                    label _("{color=#f6d6bd}Apes and Monkeys{/color}"):
                                        style "journal_prompt"
                                    text "The limbs and tails of these furry critters have an uncanny strength, a result of the time they spend swinging from branches and climbing, doing their best to avoid the terrestrial predators. Unlike goblins, they rarely attack humans and don’t use weapons, but can savagely defend their territories, to the point of participating in lasting wars with other packs, and even with human settlements. Some tribes hunt for their meat, but these beasts are still hardly understood, and many tales ascribe to them unusual powers and abilities."
                                    text "The communities that distinct {i}apes{/i} from {i}monkeys{/i} usually describe the former as the larger ones, with broader chests, and the latter as the smaller creatures with tails, but these labels don’t always match the reality."
                                    if dalit_beastiary_unlocked:
                                        text "According to {color=#f6d6bd}[dalit_name]{/color}: “The monkeys ain’t much of a threat if you stay away from their land, but they throw things at whatever they’re afraid of. Once they get used to you, they’ll leave you alone, at least one of the many families that live in these forests. There’s a couple of dangerous apes, though. They ain’t to be ignored. We’ve seen at least one frightape, you know what it is? The gray one, with large muscles. If it attacks you, it knows it can easily squeeze you to death. You can’t fight it. All you can do is run away.”"
                                    if efren_about_shortcut:
                                        text "According to {color=#f6d6bd}Efren{/color}: “It’s the frightapes that scare me the most, and there’s an entire family of them. Trust me, if you ever hear a terrible scream of a human somewhere in the tree crowns, run as fast as you can, don’t seek it, and certainly don’t {i}fight{/i} it. Just ride as fast as you can.”"
                                    if not dalit_beastiary_unlocked or not efren_about_shortcut:
                                        text "{color=#6a6a6a}There’s still more to learn about them.{/color}"
                                elif journal_beast == "beastfolkdescription":
                                    label _("{color=#f6d6bd}Beastfolk{/color}"):
                                        style "journal_prompt"
                                    text "Many believe that talking about beastfolk brings bad luck. It’s difficult to even judge if there’s such a thing as a {i}pure{/i} specimen - each one of them partially resembles another animal: a boar, wildcat, bear, owl, lizard... Yet no matter if they have long tails, fangs, tusks, claws, or antlers, they’re always bipedal and seemingly capable of working together. “Packs,” some people say. Others call them “tribes.”"
                                    text "These mysterious creatures show up all across the realm, hunting for animals as well as travelers, but it’s not clear how smart they actually are. They don’t use weapons, nor speak, yet seem to partially understand human behavior. Even Wright’s Tablets describe a woman who used to trade with beastfolk, before they ate her."
                                    text "The smallest beastfolks, usually with wolf-like heads, are known as gnolls. While threatening in large numbers, in small groups they don’t present a problem for a skilled, confident fighter."
                                    if dalit_beastiary_unlocked:
                                        text "According to {color=#f6d6bd}[dalit_name]{/color}: “Two of them, one deerhead and one bearfolk, tried to steal a rabbit from our trap. We outnumbered them, so they just grunted for a bit and withdrew. But you know the old tales. Bring the offerings, meat and whatnot, and {i}maybe{/i} they’ll be {i}kind{/i} to you. Something they won’t find in the woods. Or food touched with pneuma. And if you were asking just about the gnolls... Who cares about them, they could barely bite your hand. You see a dozen of them? Run before they knock you down. You see two? Just chop their heads off. They ain’t magical, that I can tell you for sure. And they’re dumber than wolves.”"
                                    if oldpagos_about_bogroadcat:
                                        text "According to {color=#f6d6bd}an elder from Old Págos{/color}, one can tell if a beastfolk is a threat danger if it moves on all fours. Those standing on two hind legs are more eager to let one go."
                                    if efren_about_shortcut:
                                        text "According to {color=#f6d6bd}Efren{/color}: “Gnolls will threaten you until you give them some meat, and that’s all they eat. No fruits, no, I don’t know, bones.”"
                                    if not oldpagos_about_bogroadcat or not dalit_beastiary_unlocked or not efren_about_shortcut:
                                        text "{color=#6a6a6a}There’s still more to learn about them.{/color}"
                                elif journal_beast == "beastcorpseeatersdescription":
                                    label _("{color=#f6d6bd}Corpse eaters{/color}"):
                                        style "journal_prompt"
                                    text "These hairless, scaleless creatures resemble constantly stooped apes, but their limbs and torsos are extremely thin, as if there are barely any muscles on them. While they’re nimble, their limited strength turned them into scavengers. They rarely move in packs."
                                    text "Wright’s followers preach that {i}corpse eaters{/i} should be purged from The Dragonwoods, no matter the cost. A famous tale from The Tablets describes the ancient home of these beasts - The Shadow Vale. They hunted and devoured any human they could find, and woke up their undead shells right away, even without a fog. Countless expeditions, even from days before The Ten Cities, were meant to wipe them out in the woods."
                                    if dalit_beastiary_unlocked:
                                        text "According to {color=#f6d6bd}[dalit_name]{/color}: “They’re somewhere for sure, but not around. There ain’t many travelers and settlements here, so they can’t feast on humans alone. Last time I saw their claw marks, when was it? A year ago or so, when we placed traps in the northeast, near the old watchtower. I bet they stay away from the heart of the forest, so all that remains is the far east. You can handle at least one of them, with that axe of yours. Just remember to give it all, right away. Hurt the beast even slightly, just cut its arm or something, and it’s going to run in panic. They may be deadly, but they’re cowards.”"
                                    if bestiary_ghouls_legend:
                                        text "According to some, a shell eaten by a ghoul will much sooner wake up as an undead."
                                    if not dalit_beastiary_unlocked or not bestiary_ghouls_legend:
                                        text "{color=#6a6a6a}There’s still more to learn about them.{/color}"
                                elif journal_beast == "beastdragonlingsdescription":
                                    label _("{color=#f6d6bd}Dragonlings{/color}"):
                                        style "journal_prompt"
                                    text "Dragonlings are fast and bipedal, often as tall as a human. Travelers encounter their packs near the roads - they’re used to chasing their prey, with an extra advantage in an empty field than in the forests. They have a thick, dragon-like skin, powerful jaws, short hands, and some of them are partially covered with furs."
                                    if dalit_beastiary_unlocked:
                                        text "According to {color=#f6d6bd}[dalit_name]{/color}: “Why not just run? You have your horse, put it to use! Most of them are west from here, but we usually walk in a large group, so they stay away. But oh, do they lurk around! If you {i}really{/i} have to fight them... They attack all at once, so you won’t make it when outnumbered, and you won’t outrun them on foot. Hide on a tree if you’re alone, and if not, be sure that everyone in your group has a decent weapon. Getting through their skin is tough. Unless you find kobolds, you know. Those that are knee-high. They’re not too dangerous, they won’t try to hunt down a human. Though who knows, maybe if they’re starving.”"
                                    if not dalit_beastiary_unlocked:
                                        text "{color=#6a6a6a}There’s still more to learn about them.{/color}"
                                elif journal_beast == "beastdragonsdescription":
                                    label _("{color=#f6d6bd}Dragons{/color}"):
                                        style "journal_prompt"
                                    text "Dragons’ size and the danger they present is beyond the understanding of humans. Some of them move on four limbs and devour leaves all day long; some are bipedal and walk in the wilderness hunting for other monstrosities; others fly on their massive wings, or have other, even magical powers."
                                    text "Dragon hides and trophies are one of the most rare and valued crafting resources on The Land, and their bones are either cut into small, disk-like coins, or turned into weapons, armors, or tools."
                                    if dalit_beastiary_unlocked:
                                        text "According to {color=#f6d6bd}[dalit_name]{/color}: “They don’t even care about humans all that much. We’re too small for their jaws, and it’s not easy for them to get through our clothes, or whatever it is that we carry around. But they do destroy villages if they feel like it. I wish I could have a voice like they do. Whenever they roar, birds take off, and the wild game either flees or plays dead. Could be a handy little trick.”"
                                    if not dalit_beastiary_unlocked:
                                        text "{color=#6a6a6a}There’s still more to learn about them.{/color}"
                                elif journal_beast == "beastmediumcrittersdescription":
                                    label _("{color=#f6d6bd}Foxes and such{/color}"):
                                        style "journal_prompt"
                                    text "The woods are full of medium-size critters. Badgers, foxes, wolverines, beavers... Most of them avoid humans, and in some cases are even seen as valuable allies when it comes to taming the wilderness. Still, the villagers tend to admire their beautiful furs, and since they can’t really threaten a group of armed hunters, they are not seen as a threat."
                                    if dalit_beastiary_unlocked:
                                        text "According to {color=#f6d6bd}[dalit_name]{/color}: “They stay in their burrows, or in the ruins if there are no goblins around. You don’t hunt for furs, I expect? If you have no reason to fight them, just bother them from time to time. Scare them off, you see? Show them their home ain’t safe anymore, and they’ll look for another one. Much safer than a fight with a whole pack at once, and less bloody.”"
                                    if elpis_about_thyrsusgift1_bonus2:
                                        text "According to {color=#f6d6bd}Elpis{/color}: “‘Tis better to keep your distance, but be worried, for such beasts rarely roam on their own, en are much smarter than most people expect.”"
                                    if not dalit_beastiary_unlocked or not elpis_about_thyrsusgift1_bonus2:
                                        text "{color=#6a6a6a}There’s still more to learn about them.{/color}"
                                elif journal_beast == "beastgargoylesdescription":
                                    label _("{color=#f6d6bd}Gargoyles{/color}"):
                                        style "journal_prompt"
                                    text "While capable of flying, these large predators spend most of the time on the ground, using their dexterous paws to set up spots where they stand still, even for days. Such camouflaged ambushes are seldom noticed by distracted, running prey. Like many other monsters, they hope to avoid combat, aiming to feast quickly, then look for a new hunting spot, ready to starve for weeks at a time."
                                    if dalit_beastiary_unlocked:
                                        text "According to {color=#f6d6bd}[dalit_name]{/color}: “They stay where the trees and shrubs are the thickest. In the heart of the forest, most likely. Waiting for something to get close, then they jump, ready to bite off their prey’s heads. What you need to do is keep an eye on the tree crowns, or maybe the really lush bushes growing next to the road. When a gargoyle prepares to strike, their eyes get red, almost shiny. That’s when you need to take a damn crossbow and shoot right into it. Don’t use spells, though. They won’t do any good.”"
                                    if efren_about_missinghunters_questions05:
                                        text "According to {color=#f6d6bd}Efren{/color}, they “hide among leaves, jumping at a creature when it gets close.”"
                                    if eudocia_about_gargoyle:
                                        text "According to {color=#f6d6bd}Eudocia{/color}: “A dead gargoyle on the road, or by a village gate, was meant to scare off evil spirits. I don’t know about that, but its sight sure taught the local beasts who they’re dealing with.”"
                                    if not dalit_beastiary_unlocked or not eudocia_about_gargoyle:
                                        text "{color=#6a6a6a}There’s still more to learn about them.{/color}"
                                elif journal_beast == "beastgoblinsdescription":
                                    label _("{color=#f6d6bd}Goblins{/color}"):
                                        style "journal_prompt"
                                    text "These furry critters can move both on two legs and on all fours, and while they resemble apes, they spend most of their time on the ground, capable of hunting for their prey and seeking new, temporal shelters. Many people, both in the monasteries of the Orders of Truth and at the marketplaces, argue how smart a goblin can really get. It’s clear that they can fight with a pointed stick or pick up an abandoned sword, but it looks like they can’t even start their own fire, nor speak. Nevertheless, some people call their lairs {i}camps{/i}."
                                    if dalit_beastiary_unlocked:
                                        text "According to {color=#f6d6bd}[dalit_name]{/color}: “They travel all around and move their camps every now and then. Still, what are the chances you’ll find just a single creature? If you see it, turn back, its family is just nearby. And if you really want to hurt them, take care of their home. Sink it, ruin it, burn it. Whatever you do with it, they’ll move away. They need to hide from monsters, just like we do, so they won’t stay around.”"
                                    if item_trollurine:
                                        text "You’ve heard that spreading troll urine could keep goblins away from an area, at least for some time."
                                    if foggy_about_goblins:
                                        text "According to {color=#f6d6bd}Foggy{/color}: “They’re getting too clever. They surround you from two sides, one gets loud, others sneaks by you... And bam, they get you from the back.”"
                                    if quintus_about_fatsmoke:
                                        text "According to {color=#f6d6bd}Quintus{/color}, they follow the smell of the burning fat."
                                    if shortcut_darkforest_goblins_observed:
                                        text "In the heart of the woods, you noticed that goblins are willing to fight each other over found possessions."
                                    if bestiary_goblins_mourn:
                                        text "Goblins are capable of mourning their dead in a very human-like ways."
                                    if not dalit_beastiary_unlocked or not item_trollurine or not bestiary_goblins_mourn or not shortcut_darkforest_goblins_observed or not quintus_about_fatsmoke:
                                        text "{color=#6a6a6a}There’s still more to learn about them.{/color}"
                                elif journal_beast == "beastgolemsdescription":
                                    label _("{color=#f6d6bd}Golems{/color}"):
                                        style "journal_prompt"
                                    text "Magical sentinels are not a single shell, but rather a group of levitating “limbs,” flexibly changing their position when necessary. They can be made of stone, clay, timber, but even weirder materials, such as animal bones, straw, or iron. Their shells have no heart, no real eyes, voice, muscles. While you’ve seen some of them in {color=#f6d6bd}Hovlavan{/color}, you have no clue how they work."
                                    if dalit_beastiary_unlocked:
                                        text "According to {color=#f6d6bd}[dalit_name]{/color}: “They are not a single whole. That’s one of their weak spots. I don’t understand it fully, but I think it’s a bit like with the undead. The more parts of the shell you remove, even for a time, the more magic gets to waste, as if... It returns to the air? Make a trap, try to hold it, then pull, maybe with a rope? It may work. Just don’t try to stab it or smash it with a hammer. You can’t {i}harm{/i} them. Or maybe... You could just kill their owner. Or move them far away. It’s impossible to order golems around from a large distance. It confuses them.”"
                                    if quest_studyingthegolems_description03b:
                                        text "[quest_studyingthegolems_description03b]"
                                    if not dalit_beastiary_unlocked or not quest_studyingthegolems_description03b:
                                        text "{color=#6a6a6a}There’s still more to learn about them.{/color}"
                                elif journal_beast == "beastgriffonsdescription":
                                    label _("{color=#f6d6bd}Griffons{/color}"):
                                        style "journal_prompt"
                                    text "The scrub griffons are four-legged omnivores, larger than a fox, that merge features of furry critters and birds. The front parts of their shells are covered with vivid feathers, while their rears have darker furs. Their wings seem fairly massive, making them impressive jumpers, but they’re too heavy to fly."
                                    text "The noble ones are rare and especially valued in villages across The Dragonwoods. They can be as large as a horse and taught to protect homes, as long as they’re well-fed."
                                    if dalit_beastiary_unlocked:
                                        text "According to {color=#f6d6bd}[dalit_name]{/color}: “The noble griffins? But they don’t live here, it’s too close to the ocean. They can’t compete with the flying beasts, so they keep their distance, hunting only at dawn. Oh, or do you mean the scrubs? Those are everywhere. Just try to scare them off, like from a large distance, or by wounding them before they get in the position. In a place like this one they won’t starve, there’s a lot of game around. I wouldn’t expect them to hunt for human flesh.”"
                                    if bestiary_griffon_parenting:
                                        text "From what you’ve seen, even the large noble griffons are afraid of the nights, vigilantly observing their surroundings."
                                    if not dalit_beastiary_unlocked or not bestiary_griffon_parenting:
                                        text "{color=#6a6a6a}There’s still more to learn about them.{/color}"
                                elif journal_beast == "beastharpiesdescription":
                                    label _("{color=#f6d6bd}Harpies{/color}"):
                                        style "journal_prompt"
                                    text "They look like a hybrid of a goblin and a bat. While they’re much stronger than the common birds of prey, they’re infamous for their cowardice - they only attack in great numbers, selecting targets that seem to be alone, or weakened, often trying to scare away other predators from their prey."
                                    if dalit_beastiary_unlocked:
                                        text "According to {color=#f6d6bd}[dalit_name]{/color}: “Are you even going to find them? There should be none in these woods, the thicket is much too dense. And, you know, they’re cowards, how much of a threat can they be? If you have to travel where they live, just be sure to have a few guards with you. They won’t attack a group of humans. Or take a crossbow. Or spells.”"
                                    if efren_about_highisland:
                                        text "According to {color=#f6d6bd}Efren{/color}: “They’re common on the coast, and on open waters, I saw them from {color=#f6d6bd}Gale Rocks’{/color} beach. Rocks and sticks don’t fly well when thrown upward, a bow would be a safer bet, howlers are herbivores.”"
                                    if galerocks_about_harpies:
                                        text "According to the people of {color=#f6d6bd}Gale Rocks{/color}: “They take no bait, no food. All them beasts do nothing but fly and seek weaklings to catch. We tried to tame them with fish, but they never learn, dumb little bats.”"
                                    if not dalit_beastiary_unlocked or not efren_about_highisland or not galerocks_about_harpies:
                                        text "{color=#6a6a6a}There’s still more to learn about them.{/color}"
                                elif journal_beast == "beasthowlersdescription":
                                    label _("{color=#f6d6bd}Howlers{/color}"):
                                        style "journal_prompt"
                                    text "Howlers are monkeys of strong limbs and tails, though still not as dangerous as apes. Instead of using weapons, they fill their territories with otherworldly calls that are harmful to most creatures, including humans. While their furs are often seen as beautiful, they don’t have impressive claws or teeth, and their meat is seen as unsavory. Still, the books of Wright’s churches mention a few grand battles over land between howlers and humans."
                                    if dalit_beastiary_unlocked:
                                        text "According to {color=#f6d6bd}[dalit_name]{/color}: “Their shouts are like spells, and will make you sick. All it takes is what, a minute or so. Maybe a single one won’t be a threat, but they’re never alone. You’ll see packs of them in the north, and you better stay away from them, or be sure to have as many ways to keep them scared of you as you can. If they ain’t afraid, they ain’t going to let you live, and will devour you right after they deafen you.”"
                                    if howlerslair_corpse_predator:
                                        text "According to your experience, howlers are herbivores."
                                    if not dalit_beastiary_unlocked or not howlerslair_corpse_predator:
                                        text "{color=#6a6a6a}There’s still more to learn about them.{/color}"
                                elif journal_beast == "beasthuntlordsdescription":
                                    label _("{color=#f6d6bd}Huntlords{/color}"):
                                        style "journal_prompt"
                                    text "Huntlords and huntqueens spend their lives trying to take over the land of their opponents or looking for a promising mate, though only for the time it takes to copulate. They can quickly run, climb, and jump on four paws, but are also more than confident fighting on their hind limbs. Larger and stronger than a bear, they’re known to be the perfect killers. Their deafening roar, which cuts through the air whenever they finish their hunt, can be heard every night."
                                    if dalit_beastiary_unlocked:
                                        text "According to {color=#f6d6bd}[dalit_name]{/color}: “Yeah, they don’t fight anymore. The latest queen rules for maybe five years now. Our watchmen saw it a couple of times, it’s tall and has red and silver fur. I’d recognize its howling anywhere. But please don’t tell me you plan to look for it. No human can harm such a being. If it decides it wants you, the best you can do is abandon your palfrey and hope it looks tasty. But huntlords rarely strike before dusk, so who cares? Stay in the sunlight, like the rest of us.”"
                                    if not dalit_beastiary_unlocked:
                                        text "{color=#6a6a6a}There’s still more to learn about them.{/color}"
                                elif journal_beast == "beastlargecatsdescription":
                                    label _("{color=#f6d6bd}Large cats{/color}"):
                                        style "journal_prompt"
                                    text "While the smaller wild cats are too afraid of humans to attack them, the larger species are among the strongest and most successful hunters living in the North. Strong and heavy enough to kill a boar with a single strike, but also able to remain so silent and patient that most people won’t even spot them in the taller meadows."
                                    text "Their skins are usually turned into expensive pelts. They are not valued for their meat, nor their bones, but some people value the jewelry and clothing made of their claws and tusks, yet believe they bring bad luck on those who live close to the wilderness. Because of that, they are usually worn by the richest of merchants."
                                    if dalit_beastiary_unlocked:
                                        text "According to {color=#f6d6bd}[dalit_name]{/color}: “Cats won’t let you see them. They stalk their prey, and jump when you least expect it. Like, slash, and its claws are in your neck. And have you seen how big they can get? A venemus gets twice as long as your horse! You could do something if it’s right in front of you. Like, if it ain’t hunting right now. If you were smart, you’d stay away, wait for the cat to move. But if you have to... I don’t know. Be calm? Scare it away? Pretend you’re large?”"
                                    if druidcave_druid_about_shortcut:
                                        text "According to {color=#f6d6bd}the old druid{/color}: “Death may take many paths to us, stranger, but cats are the one enemy that’s both as dangerous in its stealth, as in combat. No human can fight it alone. If you see one of them en it’s ne too late... Do ne provoke it, make it wary, but ne scared. Look big, talk a lot, seek its action in its eyes.”"
                                    if bogroad_triedtohelp and oldpagos_about_bogroadcat_introduction:
                                        text "According to your own experience, the black cats from the wetlands may get along with speech-imitating birds, luring humans into a trap. {color=#f6d6bd}Tertia’s{/color} story about the mysterious creatures on the road to {color=#f6d6bd}White Marshes{/color} had a grain of truth to it."
                                    elif bogroad_triedtohelp:
                                        text "According to your own experience, the black cats from the wetlands may get along with speech-imitating birds, luring humans into a trap."
                                    if not dalit_beastiary_unlocked or not bogroad_triedtohelp or not druidcave_druid_about_shortcut:
                                        text "{color=#6a6a6a}There’s still more to learn about them.{/color}"
                                elif journal_beast == "beastpebblersdescription":
                                    label _("{color=#f6d6bd}Pebblers{/color}"):
                                        style "journal_prompt"
                                    text "Like most people, you know quite a bit about pebblers - maybe the most infamous sources of nuisance for farmers across The Dragonwoods. They can get as big as a house, and maybe just as heavy. From time to time, pebblers look for some unusual tastes, like meat or honey, which can encourage them to bother human settlements. Once they get used to a specific spot, like an unfenced farm or a forest garden, getting rid of them may be a huge endeavour. There are but a few blades able to cut through their thick skin and durable bones, and a single mistake may put them into a furious charge, and then encourage them to look for human dwellings to tear them down in revenge."
                                    if item_trollurine:
                                        text "You’ve heard that spreading troll urine could keep pebblers away from an area, at least for some time."
                                    if dalit_beastiary_unlocked:
                                        text "According to {color=#f6d6bd}[dalit_name]{/color}: “There are not that many forest gardens here, in the North, so they sometimes show up west. The druids get rid of them, and the people of {color=#f6d6bd}Old Págos{/color} have a pile of mails and iron spearheads, so they know how to fight them off. I’d say there ain’t much point in hunting them. You can’t eat them, or get a good pelt. And their bones are so hard you ain’t going to sharpen one after even a day. Dragging their corpse away will take you hours and dozens of hands, so it’s all a big waste of time. Better to just discourage them, or scare them away.”"
                                    if not dalit_beastiary_unlocked or not item_trollurine:
                                        text "{color=#6a6a6a}There’s still more to learn about them.{/color}"
                                elif journal_beast == "beastrunningbirdsdescription":
                                    label _("{color=#f6d6bd}Runners{/color}"):
                                        style "journal_prompt"
                                    text "These birds are usually larger and taller than humans, but there’s not many of them left. Like all birds, they move on two legs, but their wings are very short and it’s anyone’s guess what their actual purpose is."
                                    text "Travelers often encounter these creatures near the roads, but they also do well in the woods. Their beaks are as large as a human head and their strong necks allow them to easily get through their prey’s skin. An unarmed soul would never be able to hurt one of them, but blades, especially those made of steel, pierce them easily."
                                    if dalit_beastiary_unlocked:
                                        text "According to {color=#f6d6bd}[dalit_name]{/color}: “Well, they ain’t as bad as dragonlings, you know? At least you can make a roast out of them. You’ll outrun them on a palfrey, but if you’re on foot, don’t even try. Don’t hide up a tree, they jump way too high. Wings, you know. And remember, they strike with their beaks. If they miss, it takes time for them to try again. Be fast, be decisive. Or you can try to buy you time by throwing it some meat. But only if there’s one of them, no more. Otherwise, they’ll just move past it.”"
                                    if efren_about_birdhunting:
                                        text "According to {color=#f6d6bd}Efren{/color}: “Don’t fight hungry, have a decent jacket, be sure to have something to block a bird’s charge. Oh, and a spear! The longer you keep it at a distance, the better.”"
                                    if not dalit_beastiary_unlocked or not efren_about_birdhunting:
                                        text "{color=#6a6a6a}There’s still more to learn about them.{/color}"
                                elif journal_beast == "beastsauriansdescription":
                                    label _("{color=#f6d6bd}Saurians{/color}"):
                                        style "journal_prompt"
                                    text "{i}Saurian{/i} is a term as vague as {i}monkey{/i}, and covers a vast range of four legged creatures that resemble small dragons. Some of them are hunted for meat, especially the smaller ones, while the larger ones often attack humans, though prefer heavier animals that can satiate them for longer. There are many tales about the unique abilities that some of their groups may possess, but they are among the lesser-understood creatures."
                                    if dalit_beastiary_unlocked:
                                        text "According to {color=#f6d6bd}[dalit_name]{/color}: “At least not all of them eat all meat! That’s why you keep away from the ponds and lakes. They stay just at the bank, jump at whatever gets close. You try to wash your hands, whoosh! Snapped. Even worse with a horse, it will grab it by a leg... And you know how fragile they are, as good as gone. Those all-gray are the worst, pretty much all of them eat humans. And look at their tails. If they are thin and swing left and right a lot, they can break your ribs.”"
                                    if highisland_yellowdotsaurian_knowsabout:
                                        text "You’ve heard that the large saurians with yellow dots on them are fruit eaters that eat meat only when they’re desperate."
                                    if not dalit_beastiary_unlocked or not highisland_yellowdotsaurian_knowsabout:
                                        text "{color=#6a6a6a}There’s still more to learn about them.{/color}"
                                elif journal_beast == "beastspidersdescription":
                                    label _("{color=#f6d6bd}Spiders{/color}"):
                                        style "journal_prompt"
                                    text "The most dangerous types inhabit ruins, or very lush and dark parts of the forest. They sit, all by themselves, in their webs, waiting for critters that have lost their way. Some are large like cattle, strong enough to cut through a human shell with their legs. Others use a poison-like substance that destroys their prey’s flesh. It’s impossible to list all the unique tricks they use either to strike first, or to defend themselves."
                                    if dalit_beastiary_unlocked:
                                        text "According to {color=#f6d6bd}[dalit_name]{/color}: “How to fight them? Like a really large one? Without a crossbow? A bow should do fine as well, but aim at the abdomen. A spear would be a good choice and when it gets too close, switch to an axe, or a mace. Or do you mean the smaller ones, like head-size big? Because they often, I don’t know, spit at their targets, or something. You do not want to get hit with it, this {i}web{/i}. Dodge it, or get blinded. Maybe jump away. Then you can smash it with whatever you have at hand.”"
                                    if not dalit_beastiary_unlocked:
                                        text "{color=#6a6a6a}There’s still more to learn about them.{/color}"
                                elif journal_beast == "beasttreantsdescription":
                                    label _("{color=#f6d6bd}Treants{/color}"):
                                        style "journal_prompt"
                                    text "They are tall creatures with thick, hard skin and exceptional patience. They’re slow, but thanks to their camouflage, every now and then they hit and knock out smaller creatures, then devour them whole. Since they don’t have leaves, they usually grow among wetlands or hills, where they resemble plants that struggle with those harsh conditions, though it’s not a rule."
                                    if dalit_beastiary_unlocked:
                                        text "According to {color=#f6d6bd}[dalit_name]{/color}: they may use their food to bait other creatures to get near: “They use their food to bait other creatures, can you believe that? If one of them catches you after all, play dead. Don’t try to free yourself, just wait, or it’s going to choke you, or tear off your limbs. I know it sounds bad, but stay calm. It’ll put you into its mouth, only then should you strike. Its inside is smooth, hit it with a blade, it may panic, then drop you. May. That’s your moment to run.”"
                                    if thyrsus_about_treant:
                                        text "According to {color=#f6d6bd}Thyrsus{/color}, the more one moves in the treant’s “branches”, the tighter it squeezes its prey."
                                    if not dalit_beastiary_unlocked or not thyrsus_about_treant:
                                        text "{color=#6a6a6a}There’s still more to learn about them.{/color}"
                                elif journal_beast == "beasttrollsdescription":
                                    label _("{color=#f6d6bd}Trolls{/color}"):
                                        style "journal_prompt"
                                    text "Trolls are merciless predators that move through the forests in small groups and devour as many creatures as they can catch, trying to satiate their seemingly endless hunger. Whenever they arrive in a new area, the majority of local wild game run for their lives, which also causes the migration of predators. Only the largest monsters, such as dragons, pebblers, or unicorns, don’t feel threatened by a troll family. The rest instinctively avoid any signs of their presence."
                                    text "They’re massive, heavy creatures with powerful, long arms. Fighting them requires a team of experienced fighters, and is considered to be a righteous effort. Letting them be can put a heavy burden on the local wilderness."
                                    if pc_religion == "theunitedchurch":
                                        text "Witnesses claim that trolls can also be attacked by the wrath of the herds. The priests of The United Church, however, deny the validity of such rumors."
                                    else:
                                        text "Witnesses claim that trolls can also be attacked by the wrath of the herds."
                                    if dalit_beastiary_unlocked:
                                        text "According to {color=#f6d6bd}[dalit_name]{/color}: “There should be none of them left. These fatheads were causing utter chaos across the entire peninsula, especially near the coast. Once they started to eat foragers from the east, we were hired to get rid of them. And so we did. It may happen that a new family will cross the southern gorge, but I bet the soldiers are going to spot them. Or die.”"
                                    if quintus_about_fatsmoke:
                                        text "According to {color=#f6d6bd}Quintus{/color}, they follow the smell of the burning fat."
                                    if not dalit_beastiary_unlocked or not quintus_about_fatsmoke:
                                        text "{color=#6a6a6a}There’s still more to learn about them.{/color}"
                                elif journal_beast == "beastundeaddescription":
                                    label _("{color=#f6d6bd}Undead{/color}"):
                                        style "journal_prompt"
                                    text "Any breathless human shell touched by a fog, or by a spell of a necromancer, wakes up as a bloodthirsty beast. They seek pneuma to grow stronger, may it be waiting for other foggy days, or by collecting it from the dead. The more magic fills their new form, the greater their intellect and capabilities. They start using weapons, mechanisms, tools, even magic, and start to use a human-like speech."
                                    if dalit_beastiary_unlocked:
                                        text "According to {color=#f6d6bd}[dalit_name]{/color}: “You’ll find them in {color=#f6d6bd}White Marshes{/color}, but also in the deep woods, surely looking to form a new band. I don’t have any tricks for you. All the priests and soldiers are right. Just chop them as many times as you can. Crush their bones, cut off their limbs. Surround them, outnumber them. Only the dumbest ones, those barely touched by the fogs, can fall into a simple trap. But if you {i}hurt{/i} them enough, the magic disperses. Don’t ask me how it works, I don’t drink with necromancers.”"
                                    if aeli_about_necromancers_question03:
                                        text "According to {color=#f6d6bd}Aeli{/color}: “Thou needest to learn how shrewd the enemy is. Can it sense thy presence? Can it use a bow, or spells? As long as thou are, {i}art{/i}, alone, it’s always better to run. The older undead, even more so those that weren’t awoken by the fogs, get cunning, human-like, but with cruelty thou hast never seen.”"
                                    if helvius_about_undead1:
                                        text "I’ve heard in {color=#f6d6bd}White Marshes{/color} that the undead pose no threat to animals."
                                    if galerocks_about_undead:
                                        text "The people of {color=#f6d6bd}Gale Rocks{/color} claim that it would be difficult to hurt a fleshless undead with an arrow, unless one would hit it directly in the head."
                                    if oldtunnel_inside_undead_seen and dalit_bestiary_undead_light:
                                        text "From what I’ve seen, some of the undead use light sources in the darkness, but I don’t think they need them. It may be a behavior similar to wearing clothes, or using other human tools without an obvious need."
                                    elif oldtunnel_inside_undead_seen:
                                        text "From what I’ve seen, some of the undead use light sources in the darkness - though I’m not sure they need them."
                                    if not dalit_beastiary_unlocked or not aeli_about_necromancers_question03 or not helvius_about_undead1 or not galerocks_about_undead or not oldtunnel_inside_undead_seen:
                                        text "{color=#6a6a6a}There’s still more to learn about them.{/color}"
                                elif journal_beast == "beastunicornsdescription":
                                    label _("{color=#f6d6bd}Unicorns{/color}"):
                                        style "journal_prompt"
                                    text "These massive beasts, covered with thick brown fur, are named after the horns sticking out of their skulls, often larger than a human shell. They move on four legs in dense forests and open meadows, but since they avoid settlements or even commonly used roads, they are shrouded in mystery, with legends and rumors that often contradict one another."
                                    text "Yet unicorns are among the most feared creatures of The Dragonwoods, infamous for holding a crucial role in the wrath of the herds - they charge in the front, able to get through wooden and most stone walls with a single crash, ignoring the wounds they receive in the process. Their part is then done - other beasts can get inside, not bothering with the defenders."
                                    if dalit_beastiary_unlocked:
                                        text "According to {color=#f6d6bd}[dalit_name]{/color}, they are solitary creatures. “You know what people say. The unicorns crave flesh filled with pneuma, but rarely hunt humans, and are only afraid of the largest beasts.”"
                                    if cephasgaiane_about_unicorns:
                                        text "According to {color=#f6d6bd}Gaiane{/color}: “You’d like to cut t’ skin of a spirit of havoc? Cityfolk ‘tink t’ unicorns are but a battery ram, yet ‘ey are ‘eir own soulcarriers, led by judgment, not anger. Eat grass and shoots, not flesh, and when not wit’ calves, listen to friendly voices, t’ kind tales and prayers.”"
                                    if not dalit_beastiary_unlocked or not cephasgaiane_about_unicorns:
                                        text "{color=#6a6a6a}There’s still more to learn about them.{/color}"
                                elif journal_beast == "beastwolvesdescription":
                                    label _("{color=#f6d6bd}Wolves{/color}"):
                                        style "journal_prompt"
                                    text "These four-legged critters are among the most feared hunters in the wilderness, though they are not as interested in human flesh as the large cats, and tend to hunt for strong, adult humans only if they’re on the verge of starvation. The largest of them are solitary, competing with other beasts over the biggest game and carcasses, while the smaller ones demonstrate an uncanny intelligence, and group in packs to defeat creatures they can’t take down without assistance."
                                    if dalit_beastiary_unlocked:
                                        text "According to {color=#f6d6bd}[dalit_name]{/color}: “There’s a lovely pack of red ones, those that jump really far, and once they bite you, they never let go. Also some blue wolves, they spend their time spread around, but howl to one another when they find good prey. Trust me, don’t ever try to fight a pack. Their furs are valuable, even the gray ones, but the only way to hurt them is setting up a trap. They abandon those that can’t be helped. But the furless wolves... These are the worst. They live alone, but are as dangerous as an entire group. Once you find one, you can’t run away from it, you can’t scare it off if it’s not bleeding. You must stay brave, especially when it charges at you. It’s going to jump at your neck. Duck beneath it, as quickly as you can.”"
                                    if foragers_about_furlesswolf:
                                        text "According to {color=#f6d6bd}Ilan{/color}: “A furless wolf charges at you like a runner, and jumps right at your throat.”"
                                    if not dalit_beastiary_unlocked or not foragers_about_furlesswolf:
                                        text "{color=#6a6a6a}There’s still more to learn about them.{/color}"
                                else:
                                    text "No creature selected."
                        vbar value YScrollValue ("journalbeasts"):
                            xpos 60
                            unscrollable "hide"

                elif journalmode == "glossary":
                    hbox:
                        xmaximum 330
                        viewport id "listglossary":
                            draggable True
                            xmaximum 320
                            mousewheel True
                            xpos 10
                            vbox:
                                style_prefix "journal"
                                xalign 0.0
                                yalign 0.0
                                xmaximum 320
                                xpos 10
                                ypos 6
                                spacing 20
                                text "{color=#6a6a6a}Daily life{/color}" xalign 0.5
                                textbutton "Animal Husbandry" action [SetVariable("journal_glossary", "animalhusbandryjournal_glossary")]
                                textbutton "Dragon Bones" action [SetVariable("journal_glossary", "dragonbonesjournal_glossary")]
                                textbutton "Family Life" action [SetVariable("journal_glossary", "familylifejournal_glossary")]
                                textbutton "Farming" action [SetVariable("journal_glossary", "farmingjournal_glossary")]
                                textbutton "Fogs" action [SetVariable("journal_glossary", "fogsjournal_glossary")]
                                textbutton "Foraging" action [SetVariable("journal_glossary", "foragingjournal_glossary")]
                                textbutton "Herbalism" action [SetVariable("journal_glossary", "herbalismjournal_glossary")]
                                textbutton "Hunting" action [SetVariable("journal_glossary", "huntingjournal_glossary")]
                                textbutton "Languages" action [SetVariable("journal_glossary", "languagesjournal_glossary")]
                                textbutton "Law" action [SetVariable("journal_glossary", "lawjournal_glossary")]
                                textbutton "Plague" action [SetVariable("journal_glossary", "plaguejournal_glossary")]
                                textbutton "Roadwardens" action [SetVariable("journal_glossary", "roadwardensjournal_glossary")]
                                textbutton "Seasons" action [SetVariable("journal_glossary", "seasonsjournal_glossary")]
                                textbutton "Traveling" action [SetVariable("journal_glossary", "travelingjournal_glossary")]
                                textbutton "Wrath of the Herds" action [SetVariable("journal_glossary", "wrathoftheherdsjournal_glossary")]
                                text "{size=10}\n{/size}{color=#6a6a6a}Magic{/color}" xalign 0.5
                                textbutton "Alchemy" action [SetVariable("journal_glossary", "alchemyjournal_glossary")]
                                textbutton "Blood Magic" action [SetVariable("journal_glossary", "bloodmagicjournal_glossary")]
                                textbutton "Curses & Blessings" action [SetVariable("journal_glossary", "cursesandblessingsjournal_glossary")]
                                textbutton "Enchanting" action [SetVariable("journal_glossary", "enchantingjournal_glossary")]
                                textbutton "Learning Magic" action [SetVariable("journal_glossary", "learningmagicjournal_glossary")]
                                textbutton "Necromancy" action [SetVariable("journal_glossary", "necromancyjournal_glossary")]
                                text "{size=10}\n{/size}{color=#6a6a6a}Politics & Geography{/color}" xalign 0.5
                                textbutton "Dragonwoods" action [SetVariable("journal_glossary", "dragonwoodsjournal_glossary")]
                                textbutton "Emperors & Empresses" action [SetVariable("journal_glossary", "emperorsandempressesjournal_glossary")]
                                textbutton "Growing Mountains" action [SetVariable("journal_glossary", "growingmountainsjournal_glossary")]
                                textbutton "Land" action [SetVariable("journal_glossary", "landjournal_glossary")]
                                textbutton "The Southern Invasion" action [SetVariable("journal_glossary", "southerninvasionjournal_glossary")]
                                textbutton "Southern Realms" action [SetVariable("journal_glossary", "southernrealmsjournal_glossary")]
                                textbutton "Ten Cities" action [SetVariable("journal_glossary", "tencitiesjournal_glossary")]
                                textbutton "Tribes & Northerners" action [SetVariable("journal_glossary", "tribesandnorthernersjournal_glossary")]
                                textbutton "Warfare" action [SetVariable("journal_glossary", "warfarejournal_glossary")]
                                text "{size=10}\n{/size}{color=#6a6a6a}Religion{/color}" xalign 0.5
                                textbutton "Adir" action [SetVariable("journal_glossary", "adirjournal_glossary")]
                                textbutton "Atheism" action [SetVariable("journal_glossary", "atheismjournal_glossary")]
                                textbutton "Fellowships" action [SetVariable("journal_glossary", "fellowshipsjournal_glossary")]
                                textbutton "Orders of Truth" action [SetVariable("journal_glossary", "ordersoftruthjournal_glossary")]
                                textbutton "Pagans" action [SetVariable("journal_glossary", "pagansjournal_glossary")]
                                textbutton "Pyres" action [SetVariable("journal_glossary", "pyresjournal_glossary")]
                                textbutton "Soul, Shell, Pneuma" action [SetVariable("journal_glossary", "soulshellpneumajournal_glossary")]
                                textbutton "Spirits" action [SetVariable("journal_glossary", "spiritsjournal_glossary")]
                                textbutton "Three Rivers" action [SetVariable("journal_glossary", "threeriversjournal_glossary")]
                                textbutton "The United Church" action [SetVariable("journal_glossary", "unitedchurchjournal_glossary")]
                                textbutton "Winged Hourglass" action [SetVariable("journal_glossary", "wingedhourglassjournal_glossary")]
                                textbutton "Wright & Sacred Tablets" action [SetVariable("journal_glossary", "wrightjournal_glossary")]
                        vbar value YScrollValue ("listglossary"):
                            xpos 30
                            unscrollable "hide"
                    hbox:
                        xmaximum 1100
                        viewport id "journalglossary":
                            draggable True
                            xmaximum 1008
                            mousewheel True
                            xpos 80
                            vbox:
                                style_prefix "journal"
                                xalign 0.0
                                yalign 0.0
                                xpos 80
                                xmaximum 968
                                ypos 10
                                spacing 20
                                #######
                                if journal_glossary == "animalhusbandryjournal_glossary":
                                    label _("{color=#f6d6bd}Animal Husbandry{/color}"):
                                        style "journal_prompt"
                                    text "The grounds around villages are rarely large enough to allow villagers to feed large herds, and therefore animals are mostly kept to help with labor, or to provide products other than meat."
                                    text "Mouflons and ibexes produce wool, milk, and skins used for the production of parchment. Boars don’t require much attention and eat almost anything, so they are bred for fat, meat, tusks, skins, or just to get rid of the leftovers produced in the house. Ducks, geese, partridges, pheasants, and quails produce eggs and feathers, and can be used as a quick backup meal during harder times. Chickens are valued more than any other poultry, since they rarely get through the tall walls and aren’t picky eaters."
                                    text "Animals are killed for meat on special occasions, or when they are too old to provide other types of products. A single family won’t eat a large animal by itself, so it’s common to share meat with the entire community, which will return the favor later on. If the relationships among the villagers are a bit cold, they trade instead."
                                    text "When an animal is butchered, it’s crucial to waste as little of it as possible. Their hides are used to produce clothes, the hooves and bones add taste to soups, and the offal is either eaten or turned into unique materials, such as glue."
                                elif journal_glossary == "dragonbonesjournal_glossary":
                                    label _("{color=#f6d6bd}Dragon Bones{/color}"):
                                        style "journal_prompt"
                                    text "Known also as coins, dragons, or bone dragons. They are small, hollow, ring-like pieces of bones, often kept on a string. While their shape and thickness are not precisely supervised by the state, most people can judge when the coin is too thin to be usable in the marketplace."
                                    text "Dragons are gigantic beasts and killing them is something that only the most audacious people have interest in. When possible, the bones are taken from an already deceased shell, but sometimes a weakened beast needs to be helped along. Dragon hunters do what they can to not spoil their prey."
                                    text "Counterfeiting coins takes a lot of effort and requires gathering bones of smaller, but still dangerous saurians, then carving distinctive grooves inside every single coin. Using or producing large amounts of counterfeited coins ends in a lifetime of banishment from the province."
                                    text "The prices of goods are fluid and related to the accessibility of a specific good. The country is too poorly organized to maintain the banking system, so the merchants don’t mind storing any type of bartered wares, from seeds to magical weapons."
                                elif journal_glossary == "familylifejournal_glossary":
                                    label _("{color=#f6d6bd}Family Life{/color}"):
                                        style "journal_prompt"
                                    text "Different traditions and religions lead tribes to have their own, unique view of the role and structure of a family. In some areas, one can’t abandon their spouse if they have a young child together, while in others, marriages don’t exist, allowing the adults to stay loosely attached to anyone who shares their affections, and the children are raised by the entire community."
                                    text "Some villages allow loosely defined and non-binding monogamous marriages, while in others a single family can be made of a few adults if they so desire, but they have to stay together until death. In one village, premarital sex is not a big deal, while in another it’s seen as taboo, especially if it’s required to find a spouse from a different tribe."
                                    text "If a relationship is restricted by the laws, it’s mostly for the sake of the children, or to make sure that the possessions of a dead person will stay with the rest of the family. In such cases, the belongings are passed to one’s children, and if there are none, the priority goes to the spouses, then parents, then siblings. If, however, there's no soul left, the possessions are claimed by the entire village. In The Cities, there are ways to complicate the process through a more official, written will."
                                    text "When nothing stands in the way, young people try to expand their families, with many women going through three to ten pregnancies before they’re forty. Since wars, famines, and illnesses are rare in the North, the child mortality rate isn’t high, and people don’t necessarily aim at having a new baby every other year. Nevertheless, the more children there are, the easier it is for them to provide for their elders, and magical healers do their best to protect women in labor from dying."
                                elif journal_glossary == "farmingjournal_glossary":
                                    label _("{color=#f6d6bd}Farming{/color}"):
                                        style "journal_prompt"
                                    text "The fields are small and treated with special care. While cereals are not the base of the common diet, well-kept fields can deliver two or even three harvests a year, thanks to the gentle climate and short winters. Through fertilizers, especially animal dung, villagers keep the ground rich for as long as possible. Experienced farmers and druids also support their trade with magical rituals — while it takes time and long preparation, it doesn’t require large amounts of magical power and can, for example, protect one’s plants from common diseases or insects."
                                    text "The cultivated grasses include barley, oat, rye, and wheat. They provide groats, cereals, and fodder for animals. Cereals are mostly used to produce flours, which can be quickly turned into bread and pies, and are the most welcome goods taken by the tax collectors."
                                    text "Whole broad beans are used as a meal, or ground and added to the tastier cereal flours. Artichokes, cabbages, and eggplants are often used as a base for soups and stews and are rarely eaten raw."
                                    text "The villages that don’t depend on farming, such as those with large forest gardens or those focused on artisanship and trade, sometimes cultivate flax, turning it into linen, a high-quality fabric. Hemp isn’t a fine fodder base, but it can be used both as a food source and to produce cheap clothes, sacks, bags, and ropes."
                                elif journal_glossary == "fogsjournal_glossary":
                                    label _("{color=#f6d6bd}Fogs{/color}"):
                                        style "journal_prompt"
                                    text "Fogs appear in every season aside from spring, but the majority of them occur in autumn. They are feared and hated by the Northerners, since whenever they touch a dead human shell, they awaken it. It’s unknown why this happens or why it doesn’t affect animal carcasses, but the common understanding is that the fog itself contains dense pneuma, which then spontaneously fills an empty human shell, replacing one’s soul."
                                    text "Humans can replicate this effect thanks to the forbidden art of necromancy."
                                    text "Fogs also increase the potential of spellcasters. “The fog is power,” the Tablets say, and while most people stay inside their homes while it’s around, it makes casting spells easier by supplying wizards with pneuma. During foggy days, magical potions are easier to brew, golems act faster, and the blood magic becomes less demanding."
                                elif journal_glossary == "foragingjournal_glossary":
                                    label _("{color=#f6d6bd}Foraging & Forest Gardens{/color}"):
                                        style "journal_prompt"
                                    text "The older villages tame the wilderness slowly, making it safer and less tempting for predators. They construct small shelters, surround minor areas with fences, remove smaller trees, gather branches, and weed the less desirable plants. This process may take generations, but when done carefully, the village becomes prosperous — forest-gardens offer wood, food, and herbs."
                                    text "Nevertheless, the settlers forage in the forests from day one. They look for wild vegetables, spices, honey, eggs, and small game. Nuts can be stored almost anywhere and are a valuable backup food. Mushrooms are dried and kept for later, just like the small, sour wild fruits, especially quinces. Grapes, apples, pears, plums, and berries may be eaten fresh, but are more often added to meat or gruels."
                                    text "In desperate times, the foragers either hunt or look for edible barks, roots, worms, and insects, especially termites and ants. They learn to recognize edible acorns, turning them into a roasted beverage, or make a semi-sweet flour from some types of chestnuts, though this procedure takes quite a lot of time and preparation."
                                elif journal_glossary == "herbalismjournal_glossary":
                                    label _("{color=#f6d6bd}Herbalism{/color}"):
                                        style "journal_prompt"
                                    text "The healers are not aware what causes illnesses and how the human shell works. If there exists medical science in this realm, it’s practiced by the herbalists. Their knowledge of herbs and other ingredients required for medicaments and antidotes may turn into the foundation of their alchemical practices, although traditional herbalists don’t need magic, and their profession is much more forgiving, especially since they are supported strongly by the placebo effect."
                                elif journal_glossary == "huntingjournal_glossary":
                                    label _("{color=#f6d6bd}Hunting{/color}"):
                                        style "journal_prompt"
                                    text "From time to time, every village has to hunt, but not all of them have specialized hunters. Careless hunting may irritate the beasts and provoke them to attack the settlement, and the process in itself can be extremely dangerous. Hunters avoid fighting with their prey and prefer to use traps, crossbows, or spells to overcome their physical disadvantages."
                                    text "The true masters of the hunt know when and how to track their prey, how to flay it, and how to collect valuable trophies and alchemical ingredients from it. When they aren’t looking for game, they search for eggs, explore the wilderness, or look for valuable bones and antlers."
                                    text "Most hunters retire before they pass their 40th birthday. Since their life involves constant learning and complex decision making, they teach their trade to their children."
                                    text "Fishing is a safer type of hunting, though it involves just as much knowledge to efficiently support an entire village. It doesn’t provoke nature’s counterattacks as much, yet it still isn’t a safe activity. Water sources gather predators hoping to catch thirsty animals. Setting up fishing equipment at night or crossing deeper waters on a boat is never a time to relax."
                                elif journal_glossary == "languagesjournal_glossary":
                                    label _("{color=#f6d6bd}Languages{/color}"):
                                        style "journal_prompt"
                                    text "There are three major languages used in the North: Adir’s language (known also as the language of the Tablets), the City Tongue, and the Old Speech."
                                    text "While no soul speaks using {i}Adir’s language{/i}, it’s a useful tool based on the language used by the tribe of Adir, the first emperor. It was used to write down Wright’s Tablets, as well as poems, songs, historical archives, philosophical contemplations, and alchemical and magical research. It developed the writing system and intellectual tradition of the realm, and is constantly used by scholars."
                                    text "The language that took over and is known by almost everyone is known as the {i}City Tongue{/i}, used by the majority of the tribes that Adir conquered. It spread quickly and widely, helping to find people to trade with without forcing them to learn a foreign language first. The City Tongue is not popular in writing, but most people use it in their thoughts, speech, and dreams."
                                    text "{i}The Old Speech{/i} is seen as the language of pagans, or rather a large group of vaguely related languages. The city officials are discouraged from learning it and using it. Only the most isolated (or the most isolationist) villages and settlements use it in their daily conversations, and therefore it evolves at a much slower pace than the City Tongue. Those who use it are often considered alien and strange. It has no written form, though literate necromancers use Adir’s alphabet to represent the sounds they want to write down — though the results are far from perfect. The relics of the Old Speech are still present in names and proverbs."
                                elif journal_glossary == "lawjournal_glossary":
                                    label _("{color=#f6d6bd}Law{/color}"):
                                        style "journal_prompt"
                                    text "In The Ten Cities, the religious figures influence both the legislation processes and the judiciary of the state. Not only have the priests developed and maintained this system, but they are also the ones who keep all the records in their archives and temples. The space for abuse is virtually limitless and The Cities experienced it at every step. Every city has its own set of laws and regulations, and even the officials can’t easily bend them."
                                    text "Living in the countryside, on the other hand, is not strictly regulated. If a building stands empty, one can ask to simply move in. When one commits a crime, the village judges how to handle it. If one is more of a burden to the community than help, they may be asked to take on additional duties, or even to leave. No soul owns the fish in the lakes, the game in the forests, the rights to the land or to craft."
                                    text "It’s uncommon to punish for sinful deeds that don’t hurt anyone in a significant matter. Improper behavior may lead to a small fine, but in most cases, only harmful actions are punished, usually by being forced to do involuntary work, or by being banished from a settlement, sometimes with a mark on one’s face, carved by a blade or hot iron."
                                    text "There’s one rule shared by the entire North — don’t provoke nature, and don’t exploit it to the point where it attacks the villages, or you will face the most severe of punishments."
                                elif journal_glossary == "plaguejournal_glossary":
                                    label _("{color=#f6d6bd}The Plague{/color}"):
                                        style "journal_prompt"
                                    text "The decentralized civilization of the North makes it difficult for epidemics to spread. Most of the time, the deadliest illnesses wipe out entire settlements before they have a chance to transfer outside. The Cities keep an eye on dangerous symptoms and use magic to eliminate any pestilence before it gets out of control."
                                    text "However, just ten years before The Southern Invasion, the Plague overran the realm, surprising even the mages and the most experienced herbalists. Its symptoms were difficult to spot, and it attacked most of The Cities pretty much at the same time, spreading to the closest villages quickly. Every twentieth Northerner had died before the healers found efficient ways to overcome this crisis."
                                elif journal_glossary == "roadwardensjournal_glossary":
                                    label _("{color=#f6d6bd}Roadwardens{/color}"):
                                        style "journal_prompt"
                                    text "They use many titles, but are essentially travelers who patrol selected routes or roam about an entire province on their expensive palfreys. While some of them are simple mercenaries hired on a long-term contract by village mayors, most roadwardens get paid directly by the city officials, recruited among army veterans or trusted allies. Their duties include dealing with human corpses that can be found on the roads, delivering messages, and protecting travelers, especially merchants. They may also be required to learn the basics of the city laws, and serve as judges to distant, troubled communities."
                                    text "Even though their salary is high, they often look for bounties, participate in commerce, or simply loot the unfortunate deceased in the middle of nowhere. A roadwarden may retire quite early, though the job is extremely dangerous and, as a result, also very respectable."
                                    text "There are also the self-proclaimed roadwardens. Ambitious ex-soldiers, mercenaries, or trophy hunters who didn’t get the job or decided to work outside the boundaries of the law. Some of them have noble intentions and help others live in peace and safety, though more often they are little more than roaming bounty hunters."
                                elif journal_glossary == "seasonsjournal_glossary":
                                    label _("{color=#f6d6bd}Seasons{/color}"):
                                        style "journal_prompt"
                                    text "{i}Summer{/i} lasts for half a year. During this period, the wild animals dominate in the wilderness, but the days are warm, winds gentle, nights short, and roads passable. It’s good enough for the roaming merchants, bandits, and travelers, while the farmers take care of their animals and fields, going through two or three harvests."
                                    text "The next three seasons take less than sixty days each. {i}Autumn{/i} annoys people with its cold nights and rainy or foggy days. The monstrous beasts and the undead migrate through The Land, making the muddy roads even more dangerous. The poor gather supplies, make warm clothes, and fix their houses, while the rich close their deals, manage the final journeys, collect the taxes (usually food), and gather in The Cities."
                                    text "{i}Winter{/i} paralyzes the realm. Heavy snowfalls cover the roads, the predators are hungry, and the nights cut the days in half. Only the most essential trails are cleared, so the distant villages are on their own. The tribes focus on crafting and killing time, locked in their homes, sometimes sharing space to save firewood. The social life in The Cities is louder than ever, and the daily struggles are not as severe."
                                    text "{i}Spring{/i} brings the new calendar year. The melting snows reveal food supplies for animals, resulting in safer roads. It’s the best period to build new roads and bridges, prepare fields, cut down the weaker trees, and repair walls without provoking the wild creatures. It’s also when the villagers travel more for entertainment than out of necessity, visiting their neighbors or participating in religious rituals."
                                elif journal_glossary == "travelingjournal_glossary":
                                    label _("{color=#f6d6bd}Traveling{/color}"):
                                        style "journal_prompt"
                                    text "Attempts to pave the roads are rarely successful, as they provoke the monsters and are a logistical nightmare. The main traveling routes are a result of organized efforts to clear parts of the forests and beat paths through the meadows and hills, but such labor can rarely take place outside of the springtime."
                                    text "The trails are little more than firm ground covered by rocks, if by anything at all, and with trunks and roots that could damage the wagon wheels removed. They don’t change the wilderness more than is necessary, unless the locals have a safe shelter nearby and many years to put their plans into action. That’s why the safest trails are close to the settlements, especially The Cities, which send out patrols and build secure havens, such as inns, chapels, and strongholds."
                                elif journal_glossary == "wrathoftheherdsjournal_glossary":
                                    label _("{color=#f6d6bd}Wrath of the Herds{/color}"):
                                        style "journal_prompt"
                                    text "Whenever the Northerners interfere greatly with nature in a short timespan (by clearing the forests, making roads, creating new fields, killing large amounts of wild game), especially during seasons other than spring, the wild creatures, from rodents to dragons, join forces to remove the threat. The animals can’t get through the walls of The Ten Cities, but the state doesn’t have power to just expand its control as it pleases. The territorial expansion of the Northerners is extremely slow, and every City has at least a thousand years of history behind it."
                                    text "This phenomenon doesn’t occur in other parts of the world."
                                elif journal_glossary == "alchemyjournal_glossary":
                                    label _("{color=#f6d6bd}Alchemy{/color}"):
                                        style "journal_prompt"
                                    text "Alchemical potions, balms, and powders are a subcategory of magical items, but alchemists don’t try to influence their structure for centuries to come. Once the mixtures are consumed, put on skin, poured on the ground, or left alone for a long time, their effect takes place, then vanishes."
                                    text "While it’s possible to create potions the same way the enchanters make magical items, most alchemists keep their pneuma unaffected by using precisely measured ingredients to substitute the power required to brew. Even a master alchemist doesn’t have to possess advanced magical abilities to fulfill their profession."
                                    text "Alchemists use animal shells, plants, herbs, special types of water, fungi, gemstones, and other ingredients, which often have to be collected or used in particular conditions. An alchemist needs to supervise the temperature, pressure, and the time it takes to complete specific tasks while brewing. All these details led the alchemists to write down their knowledge and research. The huge prices of their services have turned their scrolls and codices into cryptic texts filled with ciphers and mysterious, symbolic pictures, and their true meaning is reserved for the alchemists’ crafting circles."
                                elif journal_glossary == "bloodmagicjournal_glossary":
                                    label _("{color=#f6d6bd}Blood Magic{/color}"):
                                        style "journal_prompt"
                                    text "People who can’t develop efficient magical skills can substitute them with the power held in human blood. The possibilities of this discipline are potentially limitless — as long as one can perform the correct ritual and supply it with the required energy, even a child would be able to use blood sorcery to summon an earthquake."
                                    text "However, this source of power is very inefficient. One can achieve minor results by cutting their skin and using their own blood, but greedy blood mages sacrifice human lives or collect the supplies from captives held on the verge of death."
                                    text "According to the stories, Adir, the first Emperor, executed a mage who had murdered hundreds of people just to cast a single spell, turning them into an army of the undead. Wright’s Tablets explicitly forbid any sort of blood magic, although for some pagans there are times when using it is excusable."
                                elif journal_glossary == "cursesandblessingsjournal_glossary":
                                    label _("{color=#f6d6bd}Curses & Blessings{/color}"):
                                        style "journal_prompt"
                                    text "Most scholars perceive them as magical illnesses. They are mostly linked to blood sorcery and complex rituals and can affect an object, place, or one’s shell and thoughts. Basic curses last for a short time, while others never deplete themselves or even drain the victim’s pneuma to grow in strength with every passing day."
                                    text "The Northerners condemn those who know how to curse others. Unlike regular illnesses, curses can’t spread on their own, but at the same time they are completely resistant to placebo effects. They require specific medicines or the long and exhaustive efforts of magical healers."
                                    text "Blessings, on the other hand, are beneficial spells enhancing human shells or their surroundings with a desirable effect. While they are appreciated, for an unexplained reason they are more difficult to cast, and their effects are much shorter than in the case of curses."
                                elif journal_glossary == "enchantingjournal_glossary":
                                    label _("{color=#f6d6bd}Enchanting{/color}"):
                                        style "journal_prompt"
                                    text "Filling an item with magic requires time, power, practice, and a lot of planning. This long process ultimately gives an item a place in The Companion, turning it into a physical manifestation of a magic spell. The stronger the effect, the more pneuma it requires, so a mage may need to saturate an item for even hundreds of hours."
                                    text "Because of this, most enchanters don’t have much interest in spells. They value knowledge and experience, sometimes willing to exchange their secrets and research with other manufacturers, or even create craft guilds. Their services may get ridiculously expensive, so they use their own creations to protect themselves from troublesome clients or bandits."
                                elif journal_glossary == "learningmagicjournal_glossary":
                                    label _("{color=#f6d6bd}Learning Magic{/color}"):
                                        style "journal_prompt"
                                    text "Most people have enough potential to learn a simple spell. It’s common among the villagers to cast them to heal their crops or animals, to ignite fireplaces, or wash laundry with a single breath. Such spells are passed from parents to their children or taught by the village elders as a part of basic survival."
                                    text "It’s also not uncommon to find a person who takes their mastery of a spell quite far, but is focused on other activities. Warriors use magic to enhance their strength, blacksmiths to control fire, priests to heal others — such people are known as sorcerers."
                                    text "Mages, on the other hand, are people who are not only unusually talented, but also committed to learning or inventing new spells. They are specialists who completely depend on their powers."
                                    text "People consider magic to be extremely difficult, so some of them limit their options to the usage of blood magic. Just as rarely someone possesses a magnificent talent, being able to learn or develop powerful spells after just a couple of weeks of free experimentation. In most cases, magical abilities require hard work, practice, and years of effort, which makes it not the most attractive option for the busy people of the North."
                                elif journal_glossary == "necromancyjournal_glossary":
                                    label _("{color=#f6d6bd}Necromancy{/color}"):
                                        style "journal_prompt"
                                    text "Awakening empty human shells with magic. It’s forbidden by Wright’s churches and difficult to encounter in The Cities, though more common in the distant villages, especially among the pagans. The undead are used as a free workforce, substituting slaves, mules, cart-horses, field workers, warriors, or hunters."
                                    text "The undead controlled by the necromancers are obedient, but once their owner loses consciousness (outside of falling asleep) or dies, the corpses they control are set free and filled with the desire to murder as many humans as they can for the rest of eternity, and feast on their blood. As a result, overly ambitious necromancers are condemned by their communities."
                                elif journal_glossary == "dragonwoodsjournal_glossary":
                                    label _("{color=#f6d6bd}The Dragonwoods{/color}"):
                                        style "journal_prompt"
                                    text "A territory set in the northern part of The Land, separated from The Southern Realms by The Growing Mountains. It’s covered with forests, wetlands, jungles, and meadows, sewn together with a dense web of rivers. The swamps, lakes, and thickets force the locals to use long, meandering roads."
                                elif journal_glossary == "emperorsandempressesjournal_glossary":
                                    label _("{color=#f6d6bd}Emperors & Empresses{/color}"):
                                        style "journal_prompt"
                                    text "The North used to be ruled by an emperor or an empress. They, or rather their court, were a chief of the capital city, the head of The United Church, and the commander in chief. While the villagers were aware of the existence of the court, almost none of them ever had an opportunity to see the royal faces. The Ten Cities united the cityfolk, but the vast majority of the common folk felt attached only to their own villages, or to the larger tribe to which their settlement belonged, and called themselves “the Northerners.”"
                                    text "The role of the emperors was shaped by 1500 years of tradition. Ideally, the most suitable candidate was elected by the ten chiefs of The Cities, but thanks to the nepotism and power held by the court, almost all of the elected emperors belonged to a small group of royal families."
                                    text "Losing in The Southern Invasion has discredited the position of the emperors. The ruling empress has disappeared, and never officially lost her position. At first her duties were carried out by the court and city chiefs, but after their army lost to the Southerners, the first usurpers came to the surface. The interregnum, political intrigues, rivalry, and assassinations brought the cityfolk to the point where they are losing their faith in the state."
                                elif journal_glossary == "growingmountainsjournal_glossary":
                                    label _("{color=#f6d6bd}The Growing Mountains{/color}"):
                                        style "journal_prompt"
                                    text "A massive mountain chain with hundreds of springs, caves, short plants, and snow at the peaks. With its narrow gorges and the watchtowers built by The Ten Cities, it separates The Dragonwoods from The Wastelands. Even the waters next to it are difficult to cross without entering the deep seas."
                                    text "The local tribes are known as clans, both independent and connected by their tight cultural bonds."
                                elif journal_glossary == "landjournal_glossary":
                                    label _("{color=#f6d6bd}The Land{/color}"):
                                        style "journal_prompt"
                                    text "The continent known to the Northerners. It’s surrounded by great oceans, separated from other, distant regions that were just recently discovered. Colonizing these realms is still at its dawn, and only a few ships have returned from them."
                                elif journal_glossary == "southerninvasionjournal_glossary":
                                    label _("{color=#f6d6bd}The Southern Invasion{/color}"):
                                        style "journal_prompt"
                                    text "Since the rise of The Ten Cities, their state, priests, and artists have portrayed the lands south of The Growing Mountains as barbaric, primitive, and inferior. The pagan beliefs and technological advancements of the {i}barbarians{/i} were mocked and diminished, while the corsairs who were sent against them to pillage were seen as just servants of Wright’s people."
                                    text "These were the times of a complex mix of bigotry, cruelty, and the arms races. The nations living in the deserts joined their forces (not always willingly) with the realms from even deeper south, which strengthened their defenses and allowed them to push against The Cities."
                                    text "The turning point occurred when an alchemist introduced black powder to the nations in the South. Twenty-five years ago, the Tribes launched a massive campaign through The Growing Mountains, this time using the new weapon to take down the unprepared strongholds. The Cities, unaware of the existence of explosives, took heavy losses. The clans of The Growing Mountains knew they could do nothing to stop the enemy troops and let them pass freely. The invaders set the camps at the feet of the mountains and began their expansion."
                                    text "The city forces, weakened by the Plague, weren’t able to keep up with the numbers of the Tribes, this time prepared for guerilla warfare. The invaders conquered multiple settlements, releasing slaves and gaining valuable knowledge. The Southerners realized they should avoid The Cities at any cost, slowly moving toward the northern coast and fighting over the villages and lesser military outposts — either burning them to the ground or sparing them in exchange for food and other forms of support."
                                    text "After just three years, the war already had its winner, but The Cities refused to give up, no matter the cost. When The Southern Tribes finally took control over a couple of provinces at once, they used new supplies of black powder to, for the first time in history, conquer one of The Cities. Since the empress was nowhere to be found, the imperial court surrendered in her name."
                                elif journal_glossary == "southernrealmsjournal_glossary":
                                    label _("{color=#f6d6bd}The Southern Realms{/color}"):
                                        style "journal_prompt"
                                    text "A vast, varied area known to the older Northerners as The Wastelands. The realms near The Growing Mountains are indeed little more than deserts, marshes, and barren hills, but the farther south one travels, the more fields, herds, and cities they’ll find. Since there are no jungles and homes for gigantic beasts, the Tribes have to compete with each other over resources."
                                    text "Before the invasion that took place one generation ago, The Southern Tribes were called {i}barbarians{/i}, and The Southern Realms were known as The Wastelands."
                                elif journal_glossary == "tencitiesjournal_glossary":
                                    label _("{color=#f6d6bd}The Ten Cities{/color}"):
                                        style "journal_prompt"
                                    text "The state fell a generation ago but the idea of it still unites the cityfolk, and those villagers who collaborate with The Cities closely. The so-called barbarians from The Southern Tribes have pillaged the realm, pushing the locals away from The Growing Mountains. Many settlements have been pillaged, burnt, or abandoned, and while The Cities still stand, their governments can’t maintain the old order, splitting its power with the churches and merchant guilds. As these groups compete with each other, they are additionally weakened by their petty games."
                                    text "There’s only nine of The Ten Cities left, with the last one being overrun by scavengers, undead, and monsters. The remaining ones are ruled independently by their own chiefs, controlling the territory that belongs to their province. They’re focused on maintaining the taxation system to feed the officials, artisans, scholars, mages, soldiers, and artists. They have to collaborate with the nearby villages or settle in new areas, but there’s not many people interested in such a dangerous venture."
                                    text "Aside from protecting those living among the walls, The Cities patrol the roads, pay the innkeepers to maintain shelters, guard the temples and chapels of The United Church, send soldiers to settlements, and hunt for the undead, unusual beasts, or criminals, though, if possible, the soldiers would rather hire specialists to take care of such tasks."
                                    text "The villages collaborate with The Cities by signing taxation deals. Their representatives, usually the elected mayors, are paid for learning how to read, collecting taxes, and maintaining order. These contracts resemble other trade deals — the city gets a chunk of the food or other goods produced by the village, while the villagers gain access to soldiers, master artisans, traders, and priests."
                                    text "The further away from The Cities, the less the villages are connected to them — not only economically, but even more so culturally. Every tribe has its own way of governing itself, responding to the traditions and needs of the community. Settlements that don’t pay taxes won’t receive the city’s protection and may deal with fewer traders, but in return sustain the independence of their beliefs, culture, and laws."
                                elif journal_glossary == "tribesandnorthernersjournal_glossary":
                                    label _("{color=#f6d6bd}Tribes & Northerners{/color}"):
                                        style "journal_prompt"
                                    text "Emperors and empresses called themselves “the protectors of the ten provinces and their tribes,” but the rural areas — where the majority of the population lives — rarely attached much weight to such claims. While the disappearance of the empress has wounded the integrity of the realm, it didn’t end up in complete anarchy."
                                    text "The imperial court, even without an official leader, is also the core religious institution of The United Church. It influences the city governments, designing systems to maintain the loyalty of the chiefs and their taxpayers. To this day, the laws are signed in the name of the empress, and the priests stress the significance of loyalty to The Cities."
                                    text "This influence isn’t as strong in the distant villages. The pagan communities tend to completely cut their ties to The Cities to protect themselves from possible persecution from the Unites, while the Fellowships idealize living in small communities and perceive the differences between various villages as a source of pride. Even the taxpaying settlements consider their duties a transaction, rather than an act of patriotism — they pay for protection, security on the roads, and to maintain a good relationship with city merchants."
                                    text "Most villagers asked where they are from would answer that they are from “here,” meaning their home. They wouldn’t even consider stating that they are tied to a province or a city, or that they belong to the same “nation” as someone who lives a week of traveling away from them. Some villages are closely related to each other, even by blood, and therefore see themselves as being one tribe, but such ties get looser with the passage of time."
                                elif journal_glossary == "warfarejournal_glossary":
                                    label _("{color=#f6d6bd}Warfare{/color}"):
                                        style "journal_prompt"
                                    text "The armies of The Ten Cities can’t move in large groups or plan open battles in the middle of nowhere, and are divided into squads between 5 and 20 people each. For them, there isn’t much of a difference between fighting bandits, blood sorcerers, or beasts. They travel in groups, scouting and engaging in combat whenever possible, relying on the experience of their leader."
                                    text "The Northerners are focused on keeping their sparse settlements from collapsing. The tall walls were built this way to protect the locals from the wilderness, not siege weapons. Over the centuries, there have only been a couple of open wars between The Cities, and all of them were focused on overtaking villages and trade routes. For most people, the main role of soldiers is to deal with monsters, necromancers, and highwaymen, not to participate in political games."
                                    text "Focusing military tactics on guerrilla warfare results in a unique approach to designing weapons and armors. The crude force capable of penetrating the skins of monsters is valued more than fancy dueling equipment, while traps are more important than any mount."
                                elif journal_glossary == "adirjournal_glossary":
                                    label _("{color=#f6d6bd}Adir{/color}"):
                                        style "journal_prompt"
                                    text "Over 1500 years Adir was one of many chieftains aiming to unite the nearby tribes, though he was the first one who managed to establish an alliance with the clans of The Growing Mountains. Adir’s army gained access to steel equipment, which allowed him to dominate more villages than any leader before him. After a few spectacular conquests that helped him grow and feed his army, another dozen chiefs agreed to assist his campaign and provide him with recruits and supplies in exchange for their survival and partial independence."
                                    text "Adir became the ruler of the first major province, and the influence of his tribe’s religion kept growing as the first laws were based upon the values presented in the Tablets. During the next five centuries, the emperors and empresses conquered new grounds, dividing the lands north of The Growing Mountains into ten provinces, all of which were following the teachings of The United Church — the religion led by the imperial court."
                                elif journal_glossary == "atheismjournal_glossary":
                                    label _("{color=#f6d6bd}Atheism{/color}"):
                                        style "journal_prompt"
                                    text "There are plenty of people who don’t follow any type of religious beliefs. In some places atheists are the majority, while in others they are treated as pagans, and protect themselves by participating in religious rituals despite their lack of conviction."
                                elif journal_glossary == "wrightjournal_glossary":
                                    label _("{color=#f6d6bd}The Wright & Wright’s Tablets{/color}"):
                                        style "journal_prompt"
                                    text "Wright’s Tablets were written almost 2000 years ago by many authors. After 500 years, Adir, the first emperor, turned some of them into a collection of religious teachings."
                                    text "The Wright is the monotheistic god described in Wright’s Tablets. They tell about superhuman deeds of colorful heroes struggling with symbolic challenges and creatures. They don’t focus on a specific ethnic group and were created when the Northern Tribes were still far from forming shared identities. The Tablets also don’t explain much about the creation, purpose, or destiny of the world, focusing more on daily life and ethics."
                                    text "The passage of time and the complexity of these sources makes them confusing, almost incomprehensible, and they often contradict each other. The churches put a lot of effort into analyzing them, yet often disagree on even the most basic topics."
                                    text "The teachings most priests agree on are that The Wright is the only god, who fills human shells with souls. It’s willing to forgive human wrongdoings if one decides to turn away from their evil deeds and bases their lives on truth, kindness, and justice. The value of one's life is not grand, thus every believer ought to be ready to sacrifice their life in the name of what’s right, and listen to The Wright’s will, just as the heroes of the Tablets did. All humans will be judged by their deeds, both in this life and after death."
                                elif journal_glossary == "fellowshipsjournal_glossary":
                                    label _("{color=#f6d6bd}Fellowships - The River of Freedom{/color}"):
                                        style "journal_prompt"
                                    text "The Tablets tell stories about the people who pursue strong morals and try to free themselves from malice, about simple humans doing their best to live an honest, pious life. Since the tribes bring their own doom through greed and ignorance, these stories focus on the importance of an average person, a priceless member of a larger community."
                                    text "Fellowships, or the Eremites, are present in the villages, especially those that are not too fond of The United Church or decided to cut any ties to the city. They are in no way a unified organization as each one of them holds a different set of beliefs and traditions, focused on the value of independence and of an individual. They believe that the Tablets were meant to help people live in small gatherings, focused on humble existence and piety, and adapting the laws to the needs of the greater good. The fellowships often consider The Cities to be a parody of Wright’s will, a result of the blind lust for power, a prison for human shell and soul. The longer the fellowships stay independent, the more they merge their beliefs with pagan practices."
                                    text "The Eremites seek freedom in all forms. They want to be free from sin, independent from The Cities, and to create their own stories and ideas. They consider the Orders of Truth to be too cryptic and enigmatic, too obsessed with proving that their truth is the only one that matters. While the fellowships hold Wright’s Tablets in great esteem and consider them to be the greatest source of knowledge, they don’t try to explain all of their nuances, focusing mostly on the most practical advice and directions."
                                    text "The Fellowships have no significance in grand politics and hold little power. Every church is unique and even if a few of them find common ground, they never unite for long enough to finish any larger endeavor, usually collapsing and dividing themselves once they grow. Many of them are directly responsible for breaking tribes into smaller ones. At the same time, they can be essential for survival — their priests aim to spend their entire life in a single village, teaching kids interested in reading, and guiding the locals through ceremonies, but on the other hand, some communities are controlled by a corrupt, despotic religious figure."
                                    text "The Eremites see the wilderness as a part of life but separate from their spirituality. They try to influence their surroundings and live in harmony with it, but are much more pragmatic in their approach than those who follow the other Rivers of Faith."
                                elif journal_glossary == "ordersoftruthjournal_glossary":
                                    label _("{color=#f6d6bd}Orders - The River of Truth{/color}"):
                                        style "journal_prompt"
                                    text "The Tablets portray people pursuing knowledge of both spiritual and physical worlds. They rarely focus on children, instead describing experienced, mature people looking for wisdom, contemplating their faith, exploring philosophical ideas, or inventing new technology: sages, wizards, herbalists, and inventors."
                                    text "The Orders of Truth, known as the Seekers, had no interest in pursuing political power or gathering wealth. Instead of creating hierarchies of priests and priestesses, they invited anyone ready to abandon their personal possessions — or, in some cases, even their families — to live in small communities focused on gathering knowledge, creating and copying hand-written books, developing new technologies, exploring art, and studying medicine, alchemy, or magic. While these gatherings, later known as the Orders, were focused on different activities, they were ready to share their knowledge with each other and support themselves in times of need."
                                    text "At first, The United Church allowed the Seekers to carry on with their research. After a couple of centuries, some Orders gathered large collections of priceless books and talented artisans, able to sell their works for huge prices. The Unites tried to force them to adapt the traditional structures and join the priesthood, as well as share their riches and knowledge with the grand temples. The Orders refused, engaging in a long political conflict. Some monasteries were forced to succumb to the law, while others moved to rural areas, trying to live in harmony with the villages willing to exchange supplies for their knowledge and artisanship."
                                    text "A couple of the orders turned out to be influential and powerful enough to stay in The Cities after all. Their large monasteries are generously rewarded for their abilities, but their knowledge is veiled in secrecy, securing the position of those who have access."
                                    text "The monks aren’t explorers. They usually stay in their strongholds, only sometimes organizing expeditions to gather information and resources that can’t be obtained otherwise, or to transport books or goods for sale. The Orders don’t keep military squads, but the monasteries settled in rural areas are well-protected and even fortified."
                                    text "The Seekers portray nature as a mysterious force, a realm where the ancient heroes were illuminated by The Wright or understood the secrets of life and magic. While they condemn necromancy and blood sorcery, they don’t alienate themselves from the pagan tribes, considering them to be lost, rather than wicked. At the same time, they express contempt toward The United Church, portraying it as spiritually hollow and too invested in political intrigues and violence. They had mixed feelings toward emperors and empresses but remained loyal to their military authority."
                                elif journal_glossary == "pagansjournal_glossary":
                                    label _("{color=#f6d6bd}Pagans{/color}"):
                                        style "journal_prompt"
                                    text "Wright’s followers see other religions as paganism. The United Church oppressed pagans’ beliefs in many ways, including military raids. Some areas, especially the villages set far away from The Cities, still follow the beliefs of their ancestors, even if they have to keep it a secret. Some of them are indeed limited to a single tribe, but there are also popular ideas that reappear in various shapes across the entire realm. Some communities praise minor deities connected to specific trees, hills, or rivers, while others tend to focus on living in harmony with nature or on practicing strict sets of rules, following an archaic, conservative lifestyle."
                                    text "Even though most pagans condemn blood sorcery, it’s common for shamans, druids, and witches to practice necromancy. Some practices can get dark — animal or human sacrifices are considered especially appalling."
                                    text "The number of pagan settlements, as well as those that merge paganism with the teachings of Fellowships, has been increasing ever since The Southern Invasion reduced the influence of The United Church. The settlers from the South also bring their own traditions."
                                elif journal_glossary == "pyresjournal_glossary":
                                    label _("{color=#f6d6bd}Pyres{/color}"):
                                        style "journal_prompt"
                                    text "Wright’s followers cremate the shells to stop them from awakening. The burning ceremonies are practiced in many forms, sometimes highly ritualized, even though Wright’s Tablets depict them rather vaguely, as something simple and pragmatic. It’s common for pagans to bury the shells instead, or even embrace the art of necromancy and use their dead to take care of mundane tasks."
                                elif journal_glossary == "soulshellpneumajournal_glossary":
                                    label _("{color=#f6d6bd}Soul, Shell, Pneuma{/color}"):
                                        style "journal_prompt"
                                    text "The people of The Land see a correlation between magic and breath. They describe all living creatures as empty shells filled with pneuma, the life force sustained by breathing. They believe that creatures who use magic do so because of their souls — a unique identity held in their shells, which turns pneuma into something greater. That’s why almost the entirety of magic is used through speech and breathing."
                                    text "Thus, all living creatures use pneuma, but only a few are the soul carriers — humans and spirits, such as the deities living in the forests, demons, or ghosts."
                                    text "All of these ideas are in some way lacking when they are confronted with reality. Some believe that dragons, goblins, beastfolk, or howlers do possess a soul, while others distinguish between souls of a higher and lower rank. It’s not clear why some humans can cast spells by gestures alone, or why animals don’t rise as the undead, or why a small number of humans can’t use magic at all, while the others have unusual talents."
                                    text "The various views and interpretations are not just a part of an advanced theological debate, but also shape stories and laws. Wright’s churches don’t consider magic to be different from any other human activity, while minor religions believe that it’s either an essential part of nature or a divine domain."
                                elif journal_glossary == "spiritsjournal_glossary":
                                    label _("{color=#f6d6bd}Spirits{/color}"):
                                        style "journal_prompt"
                                    text "It’s difficult to draw a line between religions and belief in the presence of supernatural soul carriers. One Order of Truth may claim that spirits don’t exist, another one that they do, but are a part of harmful magic aimed against humans, while yet another one may consider The Wright to be the most important of the spirits, but only one of many."
                                    text "The general understanding is that spirits are minor deities that rule over small areas or beings, such as a valle, a lake, a road, a tree, or a pack of wolves. Pagans tie their traditions to pleasing the spirits with their deeds and gifts, while the more superstitious followers of The Wright offer them humble sacrifices on occasion, mostly to gain a specific favor."
                                    text "Various traditions portray spirits in their own, unique ways. They may be living creatures and plants; shell-less souls circling through the air, the memories of ancestors tied to their tomb; a pantheon of gods; or a set of ancient laws of nature. It’s safe to say they are tied strongly to specific cultures, both reflecting its worldview, and shaping it."
                                elif journal_glossary == "threeriversjournal_glossary":
                                    label _("{color=#f6d6bd}The Three Rivers of Faith{/color}"):
                                        style "journal_prompt"
                                    text "Before the ancient stories were written down, they were present as loose tales, spread around by word of mouth, constantly changing their form and meaning. The invention of the sophisticated writing system allowed for the creation of a canonical set of stories, but even in the days of Adir there existed multiple sources and variants that did not portray a cohesive system of beliefs. Their symbols were also not understood clearly outside of Adir’s tribe. After another few centuries, they additionally lost their historical context."
                                    text "Three major doctrines were born during the first 500 years of The Ten Cities. These Rivers of Faith are focused on different virtues taught by Wright’s Tablets. While every doctrine accepts that the other Rivers have value, they vary when it comes to prioritizing them, and build unique narratives about the ethics and the purpose of human life."
                                    text "According to tradition, The River of Order is attached to The United Church; The River of Truth - to the Orders; and The River of Freedom - to the fellowships."
                                elif journal_glossary == "unitedchurchjournal_glossary":
                                    label _("{color=#f6d6bd}The United Church - The River of Order{/color}"):
                                        style "journal_prompt"
                                    text "The Tablets tell stories about the extraordinary leaders who inspire and lead their tribes to greatness and safety. They are warriors, blacksmiths, and builders who raise new villages and temples, or gain access to rare resources."
                                    text "The United Church, or the Unites, is the largest, the richest, and the most unified organization in the North, and is tightly connected to the politics of The Cities. It has strict hierarchies of power, traditionally with an emperor or empress at the top. For hundreds of years, it was the Church’s duty to record the government’s activities and create rules and laws enforced by the city officials. Strong laws, hierarchies, and strong leaders are considered to be valuable in and of themselves. The powerful cities are meant to juxtapose the wild, dangerous forests that can never be trusted — only conquered."
                                    text "It claims to reflect the image of Adir, the greatest leader of the North. The grand temples of The United Church can be found in every city and are the cultural centers of the entire province, using their wealth and spectacular art to maintain their rank. Various ceremonies, songs, prayers, and holidays help to unify the spread communities with shared traditions, values, and hatred."
                                    text "It teaches that believers should follow their priests without question and extinguishes all sorts of heretic or foreign beliefs. It persecutes pagans, necromancers, and blood sorcerers, the so-called “disruptors of peace,” forcing them to live outside the city walls."
                                    text "Temples develop their own military squads, sending them to villages or road chapels, protecting the locals and travelers from the undead and beasts, or cremating their corpses. Since The Southern Invasion has reduced the Church’s power, many communities see the lack of these fighters as a worthy trade for restoring their independence."
                                    text "Unites also have a long history of corruption, manipulation, coercion, and nepotism. The priests and priestesses designed many laws to maintain their influence and develop connections for the sake of their families, offspring, and friends. In most cities, the priesthood doesn’t even pretend to be impartial."
                                elif journal_glossary == "wingedhourglassjournal_glossary":
                                    label _("{color=#f6d6bd}Winged Hourglass{/color}"):
                                        style "journal_prompt"
                                    text "The most common holy symbol used in the North, representing the vanity and triviality of life. It decorates jewelry, tombstones, and weapons. The most appreciated are the ones made of animal bones or a high-quality steel."
                                else:
                                    text "No entry selected."
                        vbar value YScrollValue ("journalglossary"):
                            xpos 60
                            unscrollable "hide"

                elif journalmode == "notes":

                    hbox:
                        xsize 1338
                        viewport id "journalnotes":
                            draggable True
                            xmaximum 1338
                            mousewheel True
                            xpos 10
                            #xmaximum 968
                            #ypos 10
                            #######
                            vbox:
                                if tutorial_notes == 0 and persistent.tutorial_display:
                                    frame:
                                        ypos 0
                                        xpos 0
                                        # top_padding 12
                                        # bottom_padding 8
                                        xpadding 8
                                        maximum (1200,130)
                                        minimum (1200,130)
                                        if persistent.textstyle == "basic":
                                            # textbutton "Unless you’re occupied with another task, you can eat food, drink potions,\nand use your items from this menu. You can examine your possessions at all times.": #Be sure to examine each new item - some of them may have .
                                            textbutton "You need to confirm a note you’re editing to save it.\nNotes are shared across all of your saves.":
                                                action SetVariable("tutorial_notes", 1)
                                                text_slow_cps False
                                                text_font "philosopher.ttf"
                                                text_size 28
                                                yalign 0.5
                                                text_line_spacing + 2
                                                xpos 6
                                        if persistent.textstyle == "pixel":
                                            # textbutton "Unless you’re occupied with another task, you can eat food, drink potions,\nand use your items from this menu. You can examine your possessions at all times.":
                                            textbutton "You need to confirm a note you’re editing to save it.\nNotes are shared across all of your saves.":
                                                action SetVariable("tutorial_notes", 1)
                                                text_slow_cps False
                                                text_font "munro.ttf"
                                                text_size 28
                                                yalign 0.5
                                                xpos 8
                                xpos 10
                                ypos 6
                                #xpos 80
                                style_prefix "journal"
                                xalign 0.0
                                yalign 0.0
                                spacing 20     

                                    # def replace_journal_note_at_index(i, new_value): 
                                    # renpy.say(None, "helloworld")

                                    # persistent.journal_notes = persistent.journal_notes                  
                                    # enumerable = enumerate([])
                                    # persistent.journal_notes.append("aaaa")
                                    # for note in persistent.journal_notes:
                                    #     python.say(None, "[note]")

                                for i, val in enumerate(persistent.journal_notes):                                    
                                    if journal_notes_currently_entering is i:
                                        hbox:
                                            vbox:
                                                xsize 230
                                                textbutton "confirm" action [Function(confirm_editing)]
                                                textbutton "cancel" action [Function(cancel_editing)]
                                                key "K_KP_ENTER" action Function(confirm_editing)
                                                key "K_RETURN" action Function(confirm_editing)
                                                key "game_menu" action Function(cancel_editing)
                                            hbox:
                                                xsize 1108
                                                input:
                                                    default val style "journal_text" color "#f6d6bd"
                                                    value VariableInputValue("journal_notes_currently_entering_value")
                                                    exclude "}{" # <>?;'][,./1234567890!@#$%^&*()-_=+
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                    else:
                                        hbox:
                                            vbox:
                                                xsize 230
                                                textbutton "edit" action [Function(start_editing_journal_note, i)]
                                                textbutton "delete" action [Confirm(_("Are you sure you want to delete this entry?"), yes=[Function(delete_journal_note, i)])]
                                            hbox:
                                                xsize 1108
                                                text "[val]"
                                        add "gui/horizontalline.png":
                                            xalign 0.5                                

                                if journal_notes_currently_entering is None:
                                    # textbutton "this does nothing"
                                    textbutton "new note\n" action [Function(add_new_journal_note)]
                                    # textbutton "new note\n" action [AddToSet(journal_notes, "dsjhfgjhdsgfjh")]

                        vbar value YScrollValue ("journalnotes"):
                            xpos 60
                            unscrollable "hide"


                else:
                    vbox:
                        style_prefix "journal"
                        xalign 0.0
                        yalign 0.0
                        xmaximum 400
                        xpos 10
                        ypos 6
                        spacing 20
                        text "No page selected."
            null height (4 * gui.pref_spacing)

#### JOURNAL STYLE
style journal_button is default:
    properties gui.button_properties("journal_button")
style journal_button_text is button_text:
    color '#997577'
    size 30
    hover_color '#f6d6bd'
    selected_color '#c3a38a'
    properties gui.button_text_properties("journal")
style journal_text is gui_text:
    size 30
    color '#c3a38a'
    line_spacing +4
style journalmode_button is default
style journalmode_button_text is button_text:
    color '#997577'
    size 40
    hover_color '#f6d6bd'
    selected_color '#c3a38a'
    properties gui.button_text_properties("journal")
style journalmode_text is gui_text:
    size 40
    color '#c3a38a'

default journal = False
default journalmode = "notes"

style journal_prompt is confirm_prompt:
    xalign 0.0
style journal_prompt_text is confirm_prompt_text:
    color "#c3a38a"
    xalign 0.0
    text_align 0.0
    size 40
