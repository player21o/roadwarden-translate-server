###################### Foggy Lake
default foggylake_firsttime = 0
default foggylake_bath = 0

default foggylake_firsttime_pcdrinks = 0 # 0 - nikt nic nie pije. 1 - piją oboje. 2 - ona pije, PC ma darmowy posiłek. 3 - ona pije, PC ma przekąskę.
default foggylake_firsttime_afterdrink = 0
default foggylake_firsttime_hall = 0
default foggylake_firsttime_basement = 0
default foggylake_firsttime_floor = 0

default foggylake_inside_lastvisit = 0

default foggylake_fluff_outside = ""
default foggylake_fluff_outsideold = 0
default foggylake_fluff_outside2 = ""
default foggylake_fluff_outside2old = 0
default foggylake_fluff_inside = ""
default foggylake_fluff_insideold = 0
default foggylake_fluff_inside2 = ""
default foggylake_fluff_inside2old = 0
default foggylake_fluff_inside3 = ""
default foggylake_fluff_inside3old = 0
default foggylake_fluff_relaxing = ""
default foggylake_fluff_relaxingold = 0
default foggylake_horsename_fluff = ""
default foggylake_horsename_fluff_old = 0

default alchemytable_timer = 0
default foggylake_alchemytable_firsttime = 0
default foggylake_alchemytable_firsttime_introduction = 0

default nalia_met = 0

label foggylake01:
    nvl clear
    $ pc_area = "foggylake"
    $ shop = "foggylakefoggy"
    $ renpy.music.play("audio/track_02foggylake.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    stop nature fadeout 4.0
    $ foggylake_inside_lastvisit = 0
    $ foggylake_foragers_lastvisit = 0
    label foggylake_fluff_outsideloop: # przyroda lub coś pozostawionego przez ludzi
        $ foggylake_fluff_outside = ""
        $ foggylake_fluff_outside = renpy.random.choice(['The surface of the lake is restless, and the cold wind strikes the tavern’s hanging barrel again and again. You adjust your cloak.', 'The light shines on the water and the empty road. With no herbal beds or travelers in sight, the tavern looks like an abandoned hamlet.', 'The grass in the animal pen has managed to grow back a bit, which your mount welcomes with droopy, relaxed ears.', 'The screeching birds are sitting on the logs of the palisade. Some of them observe you, but the group doesn’t cease its squabbling.', 'There’s a hint of a strange stench and fresh claw marks left on the ground. A large saurian entered and left the yard through the lake.', 'You hear a commotion coming from the lake, drawing your eyes to the air bubbles and water ripples. After a couple of moments a scrap of the lake turns red.'])
        if foggylake_fluff_outsideold == foggylake_fluff_outside:
            jump foggylake_fluff_outsideloop
        else:
            $ foggylake_fluff_outsideold = foggylake_fluff_outside
    label foggylake_fluff_outside2loop: # działania związane z ludźmi, np. kogoś widać
        $ foggylake_fluff_outside2 = ""
        $ foggylake_fluff_outside2 = renpy.random.choice(['There are new wares near the cart, either recently left here, or prepared to be taken away. The tavern staff stops their discussion by a basket to welcome your arrival.', 'You spot a baited clap trap set near the palisade.', 'There are dozens of feathers scattered around the yard, as well as some blood stains on an apron that’s hung on the fence.', 'The tavern staff is sitting on the stairs, enjoying the light in silence as they share a roasted fish.', 'The foragers are inspecting the boat, talking about their recent fishing trip. The taller man welcomes you with a nod.', 'The tavern’s windows and doors are open, and a bunch of furs are spread over the fence. “We’re fighting bugs,” says the shorter man when he sees your look.', 'The foragers are carving a new set of throwing clubs.'])
        if foggylake_fluff_outside2old == foggylake_fluff_outside2:
            jump foggylake_fluff_outside2loop
        else:
            $ foggylake_fluff_outside2old = foggylake_fluff_outside2
    label foggylake_fluff_insideloop: # coś zmienionego w miejscu
        $ foggylake_fluff_inside = ""
        $ foggylake_fluff_inside = renpy.random.choice(['The air is humid and stuffy. The tables were just washed with a wet cloth.', 'The room has been recently aired out.', 'There’s a strong scent of boiled fat coming from the stew in the cauldron. It could use more herbs.', 'The place is messy, but quiet and warm.', 'You smell food. There are empty bowls and mugs scattered around, right next to a bucket with water.', 'There’s a heavy scent of hard drinks. You spot a closed bottle and a small cup on one of the tables.', 'There’s a pleasant scent of chamomile coming from the unusually clean cauldron.', 'Someone is snorting in the attic.'])
        if foggylake_fluff_insideold == foggylake_fluff_inside:
            jump foggylake_fluff_insideloop
        else:
            $ foggylake_fluff_insideold = foggylake_fluff_inside
    label foggylake_fluff_inside2loop: # zachowanie osoby w miejscu, głównie Foggy
        $ foggylake_fluff_inside2 = ""
        $ foggylake_fluff_inside2 = renpy.random.choice(['{color=#f6d6bd}Foggy{/color} is standing in the middle of the room, lost in her thoughts.', '{color=#f6d6bd}Foggy{/color} is resting on a chair, observing you with a single open eye.', '{color=#f6d6bd}Foggy{/color} is kneeling by the hearth, removing ash and washing the cauldron.', '{color=#f6d6bd}Foggy{/color} looks at you through the hole leading to the attic. She gets down - having only one arm doesn’t seem to hinder her.', 'As {color=#f6d6bd}Foggy{/color} walks around, she towers over every piece of furniture.', '{color=#f6d6bd}Foggy{/color} is sitting on a stool, observing the dishes in a bucket. They move and wash themselves without her touch.', '{color=#f6d6bd}Foggy{/color} is eating stew from a bowl, but once she sees you, she finishes it with a few large gulps.'])
        if foggylake_fluff_inside2old == foggylake_fluff_inside2:
            jump foggylake_fluff_inside2loop
        else:
            $ foggylake_fluff_inside2old = foggylake_fluff_inside2
    label foggylake_fluff_inside3loop: # zachowanie Foggy po powrocie
        $ foggylake_fluff_inside3 = ""
        $ foggylake_fluff_inside3 = renpy.random.choice(['{color=#f6d6bd}Foggy{/color} is resting on a chair, observing you with a single open eye.', '{color=#f6d6bd}Foggy{/color} is kneeling by the hearth, removing ash and washing the cauldron.', '{color=#f6d6bd}Foggy{/color} is eating stew from a bowl, but once she sees you, she finishes it with a few large gulps.', '{color=#f6d6bd}Foggy{/color} is bringing inside a bucket of water from the lake.', '{color=#f6d6bd}Foggy{/color} and the one-armed man cease their conversation.', '{color=#f6d6bd}Foggy{/color} sniffs contents of one of the bottles.'])
        if foggylake_fluff_inside3old == foggylake_fluff_inside3:
            jump foggylake_fluff_inside3loop
        else:
            $ foggylake_fluff_inside3old = foggylake_fluff_inside3
    label foggylake_horsename_fluffloop1:
        $ foggylake_horsename_fluff = ""
        $ foggylake_horsename_fluff = renpy.random.choice(['enjoying some fresh grass', 'napping', 'observing the movement on the lake', 'around slowly moving, as far as its cord allows it', 'pawing the ground', 'fighting off some flies with its tail', 'lazily looking around', 'drinking from the lake'])
        if foggylake_horsename_fluff_old == foggylake_horsename_fluff:
            jump foggylake_horsename_fluffloop1
        else:
            $ foggylake_horsename_fluff_old = foggylake_horsename_fluff
    label foggy_food_mealloop:
        $ foggy_food_meal = ""
        $ foggy_food_meal = renpy.random.choice(['a bowl of simple gruel, two roasted bird thighs, and a mug of acorn brew', 'a bowl of berries, two fresh, though cold, roasted perches and a cup of chamomile tisane', 'old rye bread, a fistful of nuts, a roasted rat, and a mug of acorn brew', 'old, toasted acorn bread, a large slice of mouflon cheese, and a piece of roasted pike', 'a nettle tisane and a simple root stew with plenty of meat in it', 'a slice of roasted trout, a boiled egg, and a bowl of broad beans', 'a bowl of flat gruel, another bowl with fish soup, and a soft-boiled egg', 'some monster meat you can’t identify, a couple of apples, and a cup of birch sap', 'a baked, cold pheasant and a raw eggplant', 'roasted badger meat with mushroom sauce and a bowl of simple cabbage soup', 'boar offals, a couple of carrots, and a refreshingly cold cup of water', 'a large mug of cold mint tisane and a bit stale scraps of roasted squirrel', 'two bowls, one with roasted ants and crickets and one with a warm stew'])
        if foggy_food_mealold == foggy_food_meal:
            jump foggy_food_mealloop
        else:
            $ foggy_food_mealold = foggy_food_meal
    if not foggylake_firsttime:
        $ world_known_npcs += 2 # foggy / foragers
        $ foggylake_firsttime = day
        $ world_known_areas += 1
        $ wanderer = 1
        $ creeks_unlocked = 1
        $ northernroad_unlocked = 1
        $ oldtunnel_unlocked = 1
        $ wanderer_unlocked = 1
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        if not foragingground_quest_timer:
            $ foragingground_quest_timer = (day+6)
        show areapicture foggylakeoutsideopen01 at basicfade
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        jump foggylakefirsttime01
    elif elah_quest_easternpath_lumberjacks == 1:
        jump creekselahaboutquesteasternroadfallentree04
    elif elah_quest_easternpath_lumberjacks == 2:
        jump creekselahaboutquesteasternroadfallentree10
    elif foragingground_foragers_tofoggylake:
        $ foragingground_foragers_tofoggylake = 0
        $ foragingground_foragers_toforagingground = 0
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        show areapicture foggylakeoutsideopen01 at basicfade
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        jump foggylakereturningwiththebird01
    elif efren_about_missinghunters_dayreported and efren_about_missinghunters_dayreported < day and not foggy_about_missinghunters_dayreported and not creeks_feast:
        $ foggy_about_missinghunters_dayreported = 1
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        show areapicture foggylakeoutsideopen01 at basicfade
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        jump foggy_about_missinghunters_dayreported01
    elif item_rawhide and not foragers_about_rawhide and not efren_about_missinghunters_dayreported and not creeks_feast:
        $ foragers_about_rawhide = 1
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        show areapicture foggylakeoutsideopen01 at basicfade
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        jump foragers_about_rawhide01
    else:
        $ can_leave = 1
        if foggy_about_shelter == 1:
            $ can_rest = 1
        else:
            $ can_rest = 0
        $ can_items = 1
        if quarters >= 36 and quarters < (world_daylength-4):
            show areapicture foggylakeoutsideopen01 at basicfade
        else:
            show areapicture foggylakeoutsideclosed01 at basicfade
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        jump foggylakeregular01

label foggylakefirsttimeALL:
    label foggylakefirsttime01: # pc arrives and interacts with foragers
        $ renpy.force_autosave(take_screenshot=True, block=True)
        menu:
            '{color=#f6d6bd}[horsename]{/color} carries you toward the open gate on its own, welcoming an opportunity to rest by pushing out the air loudly through its nostrils. A nearby wooden pen won’t offer much space for a horse, but should be enough for grazing and a nap.
            \n\nAs you dismount, {color=#f6d6bd}two men{/color} get up from the front stairs. Their clean-shaven faces reveal that they’re in their early twenties. {color=#f6d6bd}The first one{/color} is taller than you, broad-shouldered, and wears light brown pants and a darker jacket, both of them made of leather. With an inviting smile, he gets up and moves to open the enclosure. His steps are heavy and slow, but every movement is marked with care, ensuring he won’t knock down anything, or anyone.
            \n\n{color=#f6d6bd}The second man{/color} looks as different from his colleague as the sun from the moon. He’s unusually short and wears a heavy cloak made of black fur, so large it could cover his entire shell. He opens the door of the building, hides his hand, and peeks into the room. “{color=#f6d6bd}Foggy!{/color}” His voice is shrill and unconcerned. “A messenger, come!”
            '
            'I take off some of my bundles, let my horse rest.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take off some of my bundles, let my horse rest.')
                menu:
                    'A hanging barrel sways in the wind, marking the place as an inn or a tavern. The building resembles a merchant’s house from {color=#f6d6bd}Hovlavan{/color}, whitewashed and with oiled, elegant wooden beams. The fragile walls are high enough to avoid floods and snow, but you have no doubt that a troll, or even a pebbler, could easily break through them. The palisade is short, has hardly any support, and has no walkway for crossbowmen. Hardly enough for even a makeshift hamlet.
                    \n\nYet it’s the open harbor that makes you uneasy. Aside from the fish, any creature, aquatic or not, could just walk into the yard, undisturbed. The path is covered with paw prints and claw marks.
                    '
                    'Better not to leave {color=#f6d6bd}[horsename]{/color} outside during the night.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Better not to leave {color=#f6d6bd}%s{/color} outside during the night.' %horsename)
                        $ at_activate = 1
                        $ at = 0
                        menu:
                            'A black and white bird swoops into the water, then flaps its wings and takes off with a silver, twitching creature in its talons. {color=#f6d6bd}The large man{/color} clears his throat. “And hwat have we here! Coming from afar, friend? Are there now horses in {color=#f6d6bd}Howler’s{/color}?”
                            \n\nHis voice is stentorian, close to a shout. You vaguely recognize his accent as one found at the city harbor.
                            '
                            ' (disabled)' ( condition="at == 0" ):
                                pass
                            '“Quite far, kind soul. {color=#f6d6bd}[horsename]{/color} came with me from {color=#f6d6bd}Hovlavan{/color}.”' ( condition="at == 'friendly'" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='(friendly) - “Quite far, kind soul. {color=#f6d6bd}%s{/color} came with me from {color=#f6d6bd}Hovlavan{/color}.”' %horsename)
                                $ at_activate = 0
                                $ at = 0
                                $ foragers_friendship += 1
                                $ custom1 = "He nods appreciatively. “A weird beast, aye? A donkey that can kill a man.” You notice he keeps quite a distance from it, and holds his hand close to his throwing club. “Haven’t seen one in a hwile. The roads here aren’t that bad, they’ll take you north and east with ease.”"
                                $ custom2 = "The tall man spreads his arms, forming a chain between you and his mother. “Meet {color=#f6d6bd}Foggy{/color}, friend. Ma, the rider has come to us from {color=#f6d6bd}Hovlavan{/color}, just look at this horse!” His powerful voice turns timid and he keeps turning his head from left to right and back. “Too bad we have no hay, it looks hungry.”"
                                $ custom3 = "The woman looks at him with amusement, then glances at your palfrey. “Aye, a cute monster you’ve brought, but not enough fat on it. If it ever breaks a leg, bring it here, we’ll smoke it for winter.” She vaguely stretches out her only hand. “What brings you to {color=#f6d6bd}Foggy Lake{/color}, love? Just stopping by?” Her voice is hoarse, like that of a traveler who’s spent too many autumn nights in cold tents, yet carries a hint of motherly concern."
                                $ custom4 = "“You won’t find another shelter in this part of The Dragonwoods, especially not in {color=#f6d6bd}Creeks{/color}.” She scratches her broad chin with sausage-like fingers. “You drink?”"
                                jump foggylakefirsttime02
                            'I laugh. “Far, far away indeed! You can’t see it from here!”' ( condition="at == 'playful'" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='(playful) - I laugh. “Far, far away indeed! You can’t see it from here!”')
                                $ at_activate = 0
                                $ at = 0
                                $ foragers_friendship += 1
                                $ custom1 = "He puts his hand to his forehead and pretends to look out for something above the lake. “But I do see well enough. The city hides in your voice. A long way you had.”"
                                $ custom2 = "He spreads his arms, forming a chain between you and her. “Meet {color=#f6d6bd}Foggy{/color}, friend. Ma, the rider has come to us from {color=#f6d6bd}Hovlavan{/color}, such’ long way!” His powerful voice turns timid and he keeps turning his head from left to right and back. “I bet you’re hungry, aye?”"
                                $ custom3 = "The woman looks at him with amusement, then glances at your palfrey. “If you’re after food, I hope you know how to hunt. The land here is barren for us, but it’s a feast for boars, squirrels, and sparrows.” She vaguely stretches out her only hand. “What brings you to {color=#f6d6bd}Foggy Lake{/color}, love? Just stopping by?” Her voice is hoarse, like that of a traveler who’s spent too many autumn nights in cold tents, yet carries a hint of motherly concern."
                                $ custom4 = "“You won’t find another shelter in this part of The Dragonwoods, especially not in {color=#f6d6bd}Creeks{/color}.” She scratches her broad chin with sausage-like fingers. “You drink?”"
                                jump foggylakefirsttime02
                            '“They have donkeys and mouflons, but no horses. I came from the city.”' ( condition="at == 'distanced' and howlersdell_firsttime" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='(distanced) - “They have donkeys and mouflons, but no horses. I came from the city.”')
                                $ at_activate = 0
                                $ at = 0
                                $ custom1 = "“Smart of you to take the western road. The east is wild, only {color=#f6d6bd}Eudocia{/color} lives there, that weirdo mage.”"
                                $ custom2 = "He spreads his arms, forming a chain between you and her. “Meet {color=#f6d6bd}Foggy{/color}, friend. Ma, the rider has come to us from {color=#f6d6bd}Howler’s{/color}!” His powerful voice turns timid and he keeps turning his head from left to right and back. “But the horse is from the city. A monster, aye?”"
                                $ custom3 = "The woman looks at him with amusement, then glances at your palfrey. “It sure is. So you’ve met {color=#f6d6bd}Thais{/color}, dear? I bet that for you it’s a village like any other, but for us it’s the loudest place in the north, unbearably so.” She vaguely stretches out her only hand. “What brings you to {color=#f6d6bd}Foggy Lake{/color}, love? Just stopping by?” Her voice is hoarse, like that of a traveler who’s spent too many autumn nights in cold tents, yet carries a hint of motherly concern."
                                $ custom4 = "“You won’t find another shelter in this part of The Dragonwoods, especially not in {color=#f6d6bd}Creeks{/color}. And we’re not as costly as the damn {color=#f6d6bd}Ape Ale{/color}.” She scratches her broad chin with sausage-like fingers. “You drink?”"
                                jump foggylakefirsttime02
                            '“I haven’t been to the place you’ve mentioned. Me and my horse are from the city.”' ( condition="at == 'distanced' and not howlersdell_firsttime" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='(distanced) - “I haven’t been to the place you’ve mentioned. Me and my horse are from the city.”')
                                $ at_activate = 0
                                $ at = 0
                                $ custom1 = "“So you took the eastern road?” He frowns. “Were you hunting, or hwat? It’s a dangerous path, we don’t use it, we can’t even open the watchtower. {color=#f6d6bd}Eudocia{/color} lives nearby, but she keeps to herself.”"
                                $ custom2 = "He spreads his arms, forming a chain between you and her. “Meet {color=#f6d6bd}Foggy{/color}, friend. Ma, the rider has come to us through the tower!” His powerful voice turns timid, his head keeps turning from left to right and back. “All the way from {color=#f6d6bd}Hovlavan{/color}.”"
                                $ custom3 = "The woman nods. “Weird of you to choose that path. Haven’t you heard it’s safer to get here from the west? At least you saved some coins by staying away from {color=#f6d6bd}Howler’s Dell{/color}, they would gladly take your eye for a loaf of bread. Still, better stay away from the road that leads west from the watchtower. All sorts of monsters live there.”\n\nShe vaguely stretches out her only hand. “What brings you to {color=#f6d6bd}Foggy Lake{/color}, love? Just stopping by?” Her voice is hoarse, like that of a traveler who’s spent too many autumn nights in cold tents, yet carries a hint of motherly concern."
                                $ custom4 = "“You won’t find another shelter in this part of The Dragonwoods, especially not in {color=#f6d6bd}Creeks{/color}.” She scratches her broad chin with sausage-like fingers. “You drink?”"
                                jump foggylakefirsttime02
                            'I stare at him in silence, then look at the door, waiting for the keeper of this place.' ( condition="at == 'intimidating'" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='(intimidating) - I stare at him in silence, then look at the door, waiting for the keeper of this place.')
                                $ at_activate = 0
                                $ at = 0
                                $ foragers_friendship -= 1
                                $ custom1 = "The man stares at you, then shrugs and walks away, approaching the nearby boat. His steps make you think of a sneaking bear."
                                $ custom2 = "The gate closes in silence as the shorter man pays its attention to your horse, while his companion rubs the hull of the boat."
                                $ custom3 = "The woman looks at them briefly, then narrows her eyes. A cold gust of wind touches your neck. “I’m {color=#f6d6bd}Foggy{/color}, and this,” she makes a vague gesture toward the yard, “is {color=#f6d6bd}Foggy Lake{/color}”. Are you here to see me, love? Or just stopping by?” Her voice is hoarse, like that of a traveler who’s spent too many autumn nights in cold tents."
                                $ custom4 = "“You won’t find another shelter in this part of The Dragonwoods.” She scratches her broad chin with sausage-like fingers. “You drink?”"
                                jump foggylakefirsttime02
                            '“Yeah, I have a long journey behind me. I need a place to rest.”' ( condition="at == 'vulnerable'" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='(vulnerable) - “Yeah, I have a long journey behind me. I need a place to rest.”')
                                $ at_activate = 0
                                $ at = 0
                                $ custom1 = "“With your beast, it may not be the right place, you have to ask ma.” He scratches the back of his head. “You’d have to lead it inside, and I’m not going to clear its droppings, you know?"
                                $ custom2 = "He spreads his arms, forming a chain between you and her. “The traveler is looking for a place to rest.” His powerful voice turns timid and he keeps turning his head from left to right and back. “But there’s this horse, so I don’t know. Meet {color=#f6d6bd}Foggy{/color}, friend.”"
                                $ custom3 = "The woman looks at him with amusement, then glances at your palfrey. “Aye, and this,” she vaguely stretches out her hand over the yard, “is {color=#f6d6bd}Foggy Lake{/color}. Are you here to see me, love? Or just stopping by?” Her voice is hoarse, like that of a traveler who’s spent too many autumn nights in cold tents, yet carries a hint of motherly concern."
                                $ custom4 = "“Most folks who spend a night here are walkers, but if you have coin, we’ll let your horse inside. You won’t find another shelter in this part of The Dragonwoods, especially not in {color=#f6d6bd}Creeks{/color}.” She scratches her broad chin with sausage-like fingers. “You drink?”"
                                jump foggylakefirsttime02

    label foggylakefirsttime02: # pc greeted by foggy
        menu:
            '[custom1]
            \n\nYou hear heavy footsteps. {color=#f6d6bd}A woman{/color} shows up in the doorway and looks at you from the top of the stairs. She’s even more towering and stout than her son, the man who just welcomed you, with a massive chest and a pear-shaped face with a prominent chin. Her movements are composed and confident. She may be older than fifty, with a mixture of gray and dark blond hair.
            \n\nShe has only one arm, the left one, notably muscular and with a hand so large it could likely chop off {color=#f6d6bd}[horsename]’s{/color} head with a single strike, or crush yours like a berry. Through the slit of her robe, made of creamy worn fur, you spot her trunk-like legs.
            \n\nShe runs her eyes over your blade, armor, and mount. Her lips form into something of a smile, distorted by the scar that runs through her mouth.
            '
            'The tall guy looks a lot like her.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The tall guy looks a lot like her.')
                menu:
                    '[custom2]
                    \n\n[custom3]
                    '
                    'I close the animal pen behind me and head toward the stairs.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I close the animal pen behind me and head toward the stairs.')
                        $ at_activate = 1
                        $ at = 0
                        menu:
                            '[custom4]
                            '
                            'I smile. “In good company.”' ( condition="at == 'friendly'" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='(friendly) - I smile. “In good company.”')
                                $ at = 0
                                $ at_activate = 0
                                $ foggy_friendship += 1
                                $ foggylake_firsttime_pcdrinks = 1
                                menu:
                                    '“That’s hwat I like to hear!” Her brief, powerful laughter is enough to scare away the birds from above the lake. Your mount lets out a fearful snort. “Let’s not wait, then! Come, dear, share a story with me, and a mug.” Without waiting for your response, she walks inside.
                                    \n\n{color=#f6d6bd}The tall man{/color} takes a deep breath. “Go ahead, we’ll take care of your horse,” he encourages you with a gesture. "And by that he means we won’t do anything with it,” adds {color=#f6d6bd}the man in black fur{/color}. Whenever his screechy words follow the deep voices of his companions, he sounds like a brat. “We won’t be feeding or washing beasts that aren’t going in a stew. But we’ll keep an eye on it.”
                                    \n\nThey find new spots to rest - the side of a boat, and a stool near the palisade.
                                    '
                                    'Without another word, I go up the stairs.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Without another word, I go up the stairs.')
                                        jump foggylakefirsttime03
                                    'I ask them if they plan to join us.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask them if they plan to join us.')
                                        $ foragers_friendship += 1
                                        menu:
                                            'The large man chuckles. “We don’t have any guards. We need to stay sharp. No drinking, no leaving valued possessions behind.” He nods toward your horse. “We’ll feast in winter, when we get a break from this place.”
                                            '
                                            'I nod and go up the stairs.':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod and go up the stairs.')
                                                jump foggylakefirsttime03
                            'I shake my head gently. “I don’t, but go ahead. I’ll accompany you.”' ( condition="at == 'friendly'" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='(friendly) - I shake my head gently. “I don’t, but go ahead. I’ll accompany you.”')
                                $ at = 0
                                $ at_activate = 0
                                $ foggy_friendship += 1
                                $ foggylake_firsttime_pcdrinks = 3
                                menu:
                                    'She scoffs with a kind smile. “I don’t plan to get drunk either, but it’s your choice. Come, dear, share a story with me. I may have a snack to spare.” Without waiting for your response, she walks inside.
                                    \n\n{color=#f6d6bd}The tall man{/color} takes a deep breath. “Go ahead, we’ll take care of your horse,” he encourages you with a gesture. "And by that he means we won’t do anything with it,” adds {color=#f6d6bd}the man in black fur{/color}. Whenever his screechy words follow the deep voices of his companions, he sounds like a brat. “We won’t be feeding or washing beasts that aren’t going in a stew. But we’ll keep an eye on it.”
                                    \n\nThey find new spots to rest - the side of a boat, and a stool near the palisade.
                                    '
                                    'Without another word, I go up the stairs.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Without another word, I go up the stairs.')
                                        jump foggylakefirsttime03
                                    'I ask them if they plan to join us.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask them if they plan to join us.')
                                        $ foragers_friendship += 1
                                        menu:
                                            'The large man chuckles. “We don’t have any guards. We need to stay sharp. No drinking, no leaving valued possessions behind.” He nods toward your horse. “We’ll feast in winter, when we get a break from this place.”
                                            '
                                            'I nod and go up the stairs.':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod and go up the stairs.')
                                                jump foggylakefirsttime03
                            'I make a single loud clap and rub my hands together. “I wouldn’t dare to insult your hospitality!”' ( condition="at == 'playful'" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='(playful) - I make a loud clap and rub my hands together. “I wouldn’t dare to insult your hospitality!')
                                $ at = 0
                                $ at_activate = 0
                                $ foggy_friendship += 1
                                $ foggylake_firsttime_pcdrinks = 1
                                menu:
                                    'Her brief, powerful laughter is enough to scare away the birds from above the lake. Your mount lets out a fearful snort. “You have to visit {color=#f6d6bd}Creeks{/color}, dear! They will love you there. Come, share a story with me, and a mug.” Without waiting for your response, she walks inside.
                                    \n\n{color=#f6d6bd}The tall man{/color} takes a deep breath. “Go ahead, we’ll take care of your horse,” he encourages you with a gesture. "And by that he means we won’t do anything with it,” adds {color=#f6d6bd}the man in black fur{/color}. Whenever his screechy words follow the deep voices of his companions, he sounds like a brat. “We won’t be feeding or washing beasts that aren’t going in a stew. But we’ll keep an eye on it.”
                                    \n\nThey find new spots to rest - the side of a boat, and a stool near the palisade.
                                    '
                                    'Without another word, I go up the stairs.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Without another word, I go up the stairs.')
                                        jump foggylakefirsttime03
                                    'I ask them if they plan to join us.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask them if they plan to join us.')
                                        $ foragers_friendship += 1
                                        if day < foragingground_quest_timer and foragers_friendship >= 1:
                                            $ custom1 = "\n\nHe thinks for a moment. “Know hwat? We’re planning a humble hunt,” he says, “for someone with a thinking soul. Come speak with us, once you’re done here.”"
                                        else:
                                            $ custom1 = ""
                                        menu:
                                            'The large man chuckles. “We don’t have any guards. We need to stay sharp. No drinking, no leaving valued possessions behind.” He nods toward your horse. “We’ll feast in winter, when we get a break from this place.”[custom1]
                                            '
                                            'I nod and go up the stairs.':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod and go up the stairs.')
                                                jump foggylakefirsttime03
                            'I nod. “From time to time.”' ( condition="at == 'distanced'" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='(distanced) - I nod. “From time to time.”')
                                $ at = 0
                                $ at_activate = 0
                                $ foggylake_firsttime_pcdrinks = 1
                                menu:
                                    '“And I’d say this is the very {i}right{/i} time!” Her shouting enthusiasm makes your mount snort. “Come, dear, share a story with me, and a mug.” Without waiting for your response, she walks inside.
                                    \n\n{color=#f6d6bd}The tall man{/color} takes a deep breath. “Go ahead, we’ll take care of your horse,” he encourages you with a gesture. "And by that he means we won’t do anything with it,” adds {color=#f6d6bd}the man in black fur{/color}. Whenever his screechy words follow the deep voices of his companions, he sounds like a brat. “We won’t be feeding or washing beasts that aren’t going in a stew. But we’ll keep an eye on it.”
                                    \n\nThey find new spots to rest - the side of a boat, and a stool near the palisade.
                                    '
                                    'Without another word, I go up the stairs.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Without another word, I go up the stairs.')
                                        jump foggylakefirsttime03
                            'I shake my head. “Only if there’s no water around.”' ( condition="at == 'distanced'" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='(distanced) - I shake my head. “Only if there’s no water around.”')
                                $ at = 0
                                $ at_activate = 0
                                $ foggylake_firsttime_pcdrinks = 3
                                menu:
                                    '“We do have water, and I may find a snack or two. Come, dear!” Her shouting enthusiasm makes your mount snort. The loudness of her speech is quite unusual. “Share a story with me.” Without waiting for your response, she walks inside.
                                    \n\n{color=#f6d6bd}The tall man{/color} takes a deep breath. “Go ahead, we’ll take care of your horse,” he encourages you with a gesture. "And by that he means we won’t do anything with it,” adds {color=#f6d6bd}the man in black fur{/color}. Whenever his screechy words follow the deep voices of his companions, he sounds like a brat. “We won’t be feeding or washing beasts that aren’t going in a stew. But we’ll keep an eye on it.”
                                    \n\nThey find new spots to rest - the side of a boat, and a stool near the palisade.
                                    '
                                    'Without another word, I go up the stairs.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Without another word, I go up the stairs.')
                                        jump foggylakefirsttime03
                            'I raise my open palms. “Only with those I trust.”' ( condition="at == 'intimidating'" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='(intimidating) - I raise my open palms. “Only with those I trust.”')
                                $ at = 0
                                $ at_activate = 0
                                $ foggy_friendship -= 1
                                menu:
                                    'She observes you for a moment, then puts a hand on her side. “And d’you find such folks often?”
                                    \n\nThe two men stare at you, the shorter one with wide open eyes.
                                    '
                                    '“No.”':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “No.”')
                                        menu:
                                            '“{i}Those I trust{/i},” she mocks, “a silly thing to seek them without having kindness to offer. Come with me, stranger. Let’s talk trade.”
                                            \n\nThe two men remain reluctant. The taller one gestures at the door. “Go ahead, stranger. Your beast is safe with us.”
                                            '
                                            'Without another word, I go up the stairs.':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Without another word, I go up the stairs.')
                                                jump foggylakefirsttime03
                                    '“It always may happen.”':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It always may happen.”')
                                        menu:
                                            'She scratches her neck. “Hard to believe you make any friends.” She looks at the gate. “Come, stranger. Let’s talk trade, hwile you’re here.” Without waiting for your response, she enters the building.
                                            \n\nThe two men remain reluctant. The taller one gestures at the door. “Go ahead, stranger. Your beast is safe with us.”
                                            '
                                            'Without another word, I go up the stairs.':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Without another word, I go up the stairs.')
                                                jump foggylakefirsttime03
                                    '“I may tell you one day.”':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I may tell you one day.”')
                                        menu:
                                            'She scoffs. “If you must. Come, stranger. Let’s talk trade, hwile you’re here.” Without waiting for your response, she enters the building.
                                            \n\nThe two men remain reluctant. The taller one gestures at the door. “Go ahead, stranger. Your beast is safe with us.”
                                            '
                                            'Without another word, I go up the stairs.':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Without another word, I go up the stairs.')
                                                jump foggylakefirsttime03
                            'I put on a weak smile. “Not on an empty stomach.”' ( condition="at == 'vulnerable'" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='(vulnerable) - I put on a weak smile. “Not on an empty stomach.”')
                                $ at = 0
                                $ at_activate = 0
                                $ foggy_friendship += 2
                                $ foggylake_firsttime_pcdrinks = 2
                                menu:
                                    'She bursts into laughter and makes a face of an attentive, yet playful parent. “Poor thing!” Her powerful, low voice makes your mount snort. “Come, dear, come!” She walks down the stairs and approaches you with just two steps. “Let’s find us both something tasty.” Without waiting for your response, she puts her heavy arm on your shoulders and leads you upstairs.
                                    \n\nYou glance toward your horse, then notice that {color=#f6d6bd}the tall man{/color} gives you a reassuring shrug.
                                    '
                                    'Without another word, I enter the tavern.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Without another word, I enter the tavern.')
                                        jump foggylakefirsttime03
                            'I sigh. “I’m afraid not. Stronger drinks give me nightmares.”' ( condition="at == 'vulnerable'" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='(vulnerable) - I sigh. “I’m afraid not. Stronger drinks give me nightmares.”')
                                $ at = 0
                                $ at_activate = 0
                                $ foggy_friendship += 1
                                $ foggylake_firsttime_pcdrinks = 3
                                menu:
                                    'Her eyes are sympathetic. “I don’t plan to get drunk either, but hwat you say sounds serious. Don’t push yourself into drunkenness.” After an awkward pause, her voice gets stronger. “Come, dear, share a story with me. I may have a snack to spare.” Without waiting for your response, she walks inside.
                                    \n\n{color=#f6d6bd}The tall man{/color} takes a deep breath. “Go ahead, we’ll take care of your horse,” he encourages you with a gesture. "And by that he means we won’t do anything with it,” adds {color=#f6d6bd}the man in black fur{/color}. Whenever his screechy words follow the deep voices of his companions, he sounds like a brat. “We won’t be feeding or washing beasts that aren’t going in a stew. But we’ll keep an eye on it.”
                                    \n\nThey find new spots to rest - the side of a boat, and a stool near the palisade.
                                    '
                                    'Without another word, I go up the stairs.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Without another word, I go up the stairs.')
                                        jump foggylakefirsttime03
                                    'I ask them if they plan to join us.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask them if they plan to join us.')
                                        $ foragers_friendship += 1
                                        menu:
                                            'The large man chuckles. “We don’t have any guards. We need to stay sharp. No drinking, no leaving valued possessions behind.” He nods toward your horse. “We’ll feast in winter, when we get a break from this place. For now, you can rest in peace.”
                                            '
                                            'I nod and go up the stairs.':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod and go up the stairs.')
                                                jump foggylakefirsttime03

    label foggylakefirsttime03: # pc enters the tavern
        show areapicture foggylakeinside01 at basicfade
        menu:
            'The narrow, segmented window shutters let in a lot of light without letting the beasts inside. The air is humid, but carries not a hint of putridity. The heels of {color=#f6d6bd}Foggy’s{/color} boots make her steps thunder even though the planks don’t creak. “Make yourself at home,” she says without looking at you, heading to the trapdoor in the corner. “I’ll just grab a li’l something.”
            \n\nYour ears catch the screeches of hunting birds and the wind that leaks in through the windows, but other than that, the room is quiet.
            '
            'I investigate the main hall.' if not foggylake_firsttime_hall:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I investigate the main hall.')
                jump foggylakefirsttime03a
            'I check the basement.' if not foggylake_firsttime_basement:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I check the basement.')
                jump foggylakefirsttime03b
            'I look where the ladder leads.' if not foggylake_firsttime_floor:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look where the ladder leads.')
                jump foggylakefirsttime03c
            'I sit down at the table and wait for the keeper’s return.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I sit down at the table and wait for the keeper’s return.')
                jump foggylakefirsttime04

        label foggylakefirsttime03a:
            $ foggylake_firsttime_hall = 1
            menu:
                'The room is crammed with stuff. The bear pelt on the ground would be a nice resting spot, but the place doesn’t look like a real home. No chests, no cabinets for clothes, no toys or tools for simple crafts that would fill the time during rainy evenings. Living with so many windows in winter would be a struggle.
                \n\nOne could clear this place in one morning and move all that’s worth saving onto a single wagon. The only things of exceptional value are the cauldron, made of pricy steel, and the hanging head of an insect-like monster. Its mandibles don’t move, the dim eyes seem intact, and its armored head tells a long story of survival through scratches and cuts.
                '
                'I investigate the main hall.' if not foggylake_firsttime_hall:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I investigate the main hall.')
                    jump foggylakefirsttime03a
                'I check the basement.' if not foggylake_firsttime_basement:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I check the basement.')
                    jump foggylakefirsttime03b
                'I look where the ladder leads.' if not foggylake_firsttime_floor:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look where the ladder leads.')
                    jump foggylakefirsttime03c
                'I sit down at the table and wait for the keeper’s return.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I sit down at the table and wait for the keeper’s return.')
                    jump foggylakefirsttime04

        label foggylakefirsttime03b:
            $ foggylake_firsttime_basement = 1
            $ description_foggy04 = "Apparently she has a great interest in animal trophies, especially those gathered from dangerous creatures."
            menu:
                'The meager light hinders your view. There are dozens of barrels, sacks, stone tools, bowls, and pieces of roasted fish or bird meat. {color=#f6d6bd}Foggy{/color} notices you, but doesn’t say anything. She looks for something among a bunch of bottles.
                \n\nThere’s a couple more animal trophies placed on the top of the barrels and leaning against the walls. Fangs, claws, monster heads, and a lizard skin. Quite a collection.
                '
                'I investigate the main hall.' if not foggylake_firsttime_hall:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I investigate the main hall.')
                    jump foggylakefirsttime03a
                'I check the basement.' if not foggylake_firsttime_basement:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I check the basement.')
                    jump foggylakefirsttime03b
                'I look where the ladder leads.' if not foggylake_firsttime_floor:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look where the ladder leads.')
                    jump foggylakefirsttime03c
                'I sit down at the table and wait for the keeper’s return.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I sit down at the table and wait for the keeper’s return.')
                    jump foggylakefirsttime04

        label foggylakefirsttime03c:
            $ foggylake_firsttime_floor = 1
            menu:
                'You climb up the simple rope ladder and reach the attic. It smells like a haystack. The floor is covered with animal furs, bags, and clothes.
                \n\nThere’s a soul sitting in a corner - a bearded man in his twenties who has only the right hand, though unlike the tavern keeper he has kept the rest of his arm. His sleepy eyes observe you without a word. After he greets you with a nod, he starts to put on his boots.
                '
                'I investigate the main hall.' if not foggylake_firsttime_hall:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I investigate the main hall.')
                    jump foggylakefirsttime03a
                'I check the basement.' if not foggylake_firsttime_basement:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I check the basement.')
                    jump foggylakefirsttime03b
                'I look where the ladder leads.' if not foggylake_firsttime_floor:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look where the ladder leads.')
                    jump foggylakefirsttime03c
                'I sit down at the table and wait for the keeper’s return.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I sit down at the table and wait for the keeper’s return.')
                    jump foggylakefirsttime04

    label foggylakefirsttime04grouped: # conversation with foggy starts
        label foggylakefirsttime04:
            if quarters < 40:
                $ custom6 = "morning"
            elif quarters < (world_daylength-12):
                $ custom6 = "day"
            else:
                $ custom6 = "evening"
            if foggylake_firsttime_pcdrinks <= 0: # 0 - nikt nic nie pije
                $ foggylake_firsttime_afterdrink = 1
                menu:
                    'You take a glance at the blood on the table, the scattered yellow feathers, and a bowl of guts and talons. You find yourself a clean stool. {color=#f6d6bd}Foggy{/color} shows up soon, holding a cloth. She dips it in the bucket of water and wipes the table clean. “I’d rather dress birds in the yard, but the blood lures beasts. Sometimes the folks from {color=#f6d6bd}Creeks{/color} bring us meals, but we need to take care of ourselves.”
                    \n\nShe throws the bloody cloth back into the bucket, making a splash, then sits down on a stool, making it look like it was made for a doll. She rests her elbow on the table and looks you in the eyes. “So, who are you? A {color=#f6d6bd}Thais’{/color} wolf? A messenger?”
                    '
                    '“I’m your new roadwarden. Name’s [pcname].”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m your new roadwarden. Name’s %s.”' %pcname)
                        $ questionpreset = "foggy1"
                        if foggy_about_shelter == 1:
                            $ can_rest = 1
                        menu:
                            'She grasps the edge of the table. “Another one? You know of {color=#f6d6bd}Asterion{/color}, dear? He was here in spring.” You nod. “The roads were safer with him around, but he disappeared quickly. Saved some folks, aye. But I won’t put much faith in you.”
                            \n\nShe tilts her head a bit. “So. Hwat d’you want, [pcname]?”
                            '
                            '(preset foggy1)':
                                pass
                    '“I’m no soul’s wolf,” I say harshly. “I’m [pcname], the roadwarden.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m no soul’s wolf,” I say harshly. “I’m %s, the roadwarden.”' %pcname)
                        $ questionpreset = "foggy1"
                        if foggy_about_shelter == 1:
                            $ can_rest = 1
                        menu:
                            '“Say so now, but no traveler keeps to themselves for long. With every act of kindness you receive, every bit of help, you tie yourself just a li’l bit tighter. Stay around for long enough and you’ll have no option but to take a side, dear, hwatever it may be. The burden of favors rests on our souls.”
                            \n\nShe scratches her knee. “So. Hwat d’you want, [pcname]?”
                            '
                            '(preset foggy1)':
                                pass
                    '“I’ll carry messages for whoever’s willing to pay for it.” I introduce myself.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll carry messages for whoever’s willing to pay for it.” I introduce myself.')
                        if armor >= 3:
                            $ custom1 = "She points at your chest. “I see your jacket is plenty fine. If anything happens to it, take it to {color=#f6d6bd}Gale Rocks{/color}, or {color=#f6d6bd}Howler’s{/color}.” She nods approvingly."
                            if item_shield:
                                $ custom2 = "“And I saw a shield on your mount. Better keep it close.”"
                            else:
                                $ custom2 = "“But I haven’t seen any shield by your saddle. Better visit {color=#f6d6bd}Gale Rocks{/color} and buy yourself one.”"
                        elif armor == 2:
                            $ custom1 = "She points at your chest. “Your jacket could use some work. {color=#f6d6bd}Bion{/color} from {color=#f6d6bd}Howler’s Dell{/color} uses spider silk, she’s like a mage with a needle. But the folks at {color=#f6d6bd}Gale Rocks{/color} can also do some repairs.” She smiles."
                            if item_shield:
                                $ custom2 = "“And I saw a shield on your mount. Better keep it close.”"
                            else:
                                $ custom2 = "“But I haven’t seen any shield by your saddle. Better visit {color=#f6d6bd}Gale Rocks{/color} and buy yourself one.”"
                        else:
                            $ custom1 = "She points at your chest. “Your jacket won’t cut it. Better visit {color=#f6d6bd}Gale Rocks{/color}, they’ll be able to do something ‘bout it. Not for free, aye, but you won’t need a full pouch if you’re dead.” She smiles."
                            if item_shield:
                                $ custom2 = "“And I saw a shield on your mount. Better keep it close.”"
                            else:
                                $ custom2 = "“But I haven’t seen any shield by your saddle. You can also buy yourself one in the north.”"
                        menu:
                            'Her eyes soften. “A roadwarden who sounds like a mercenary. You will find some work around here.” She cracks her knuckles just by clenching her fist, then relaxes her hand and observes the fingers. “I may have a small job for you, love. And the boys outside want to hunt, ask them ‘bout it if you want to join them. Just be sure you have something to defend yourself with.” [custom1] [custom2]
                            '
                            '“Thanks for the tips, {color=#f6d6bd}Foggy{/color}.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks for the tips, {color=#f6d6bd}Foggy{/color}.”')
                                $ foggy_friendship += 1
                                $ questionpreset = "foggy1"
                                if foggy_about_shelter == 1:
                                    $ can_rest = 1
                                menu:
                                    'She smiles. “Just be sure to stay alive a bit longer. There are things to take care of, and we could use someone who knows how to travel.”
                                    \n\nShe scratches her knee. “So. Hwat d’you want, [pcname]?”
                                    '
                                    '(preset foggy1)':
                                        pass
                            '“I see you make sure people find a way to leave some coins around.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I see you make sure people find a way to leave some coins around.”')
                                $ questionpreset = "foggy1"
                                if foggy_about_shelter == 1:
                                    $ can_rest = 1
                                menu:
                                    'She scoffs. “Hwy wouldn’t I? The villages can grow stronger or weaker, but they’ll do so together, doesn’t matter if we want it or not. If you’re bad at your job, at least make sure to drop some dragons in our pockets before you vanish in the fogs.”
                                    \n\nShe scratches her knee. “So. Hwat d’you want, [pcname]?”
                                    '
                                    '(preset foggy1)':
                                        pass
            elif foggylake_firsttime_pcdrinks == 1: # 1 - piją oboje.
                menu:
                    'You take a glance at the blood on the table, the scattered yellow feathers, and a bowl of guts and talons. You find yourself a clean stool. {color=#f6d6bd}Foggy{/color} shows up soon, smiling, holding two cups in her hand, a bottle in her fingers, and a cloth under her shoulder. She puts everything on a stool and wipes the table clean. “Forgive the mess, just a part of the job,” she explains without a hint of apology. “I’d rather dress birds in the yard, but the blood lures beasts. Sometimes the folks from {color=#f6d6bd}Creeks{/color} bring us meals, but we need to take care of ourselves.”
                    \n\nShe throws the bloody cloth back into the bucket, making a splash, then sits down on a stool, making it look like it was made for a doll. She rests her elbow on the table and looks you in the eyes. Her voice is warm, yet intrusive. “So, who am I dealing with?”
                    '
                    'I introduce myself.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I introduce myself.')
                        menu:
                            'The bottle removes its seal seemingly by itself - the wax floats in the air briefly, then lands on the table gently. Without a word, she pours a thick liquid into the cups with her only hand, but doesn’t offer you your drink just yet.
                            '
                            '“I’m trying to learn more about the peninsula. A tavern seemed like a fair shot.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m trying to learn more about the peninsula. A tavern seemed like a fair shot.”')
                                jump foggylakefirsttime04p01learnaboutpeninsula
                            '“I’m looking for {color=#f6d6bd}Asterion{/color}, the previous roadwarden.”' if quest_asterion == 1 and not asterion_found:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for {color=#f6d6bd}Asterion{/color}, the previous roadwarden.”')
                                jump foggylakefirsttime04p01asterion
                            '“I’m going to need shelter every now and then. I stay on the road for most of my days.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m going to need shelter every now and then. I stay on the road for most of my days.”')
                                jump foggylakefirsttime04p01shelter
                            '“I hope to trade a fair bit in the coming days. I wanted to see what I can get here, leave behind some coins.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I hope to trade a fair bit in the coming days. I wanted to see what I can get here, leave behind some coins.”')
                                jump foggylakefirsttime04p01trade
                            '“I was hoping to find work. If nothing else, I can always carry a message for you.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I was hoping to find work. If nothing else, I can always carry a message for you.”')
                                jump foggylakefirsttime04p01work
                            '“I had to get here sooner or later.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I had to get here sooner or later.”')
                                jump foggylakefirsttime04p01noreason
            elif foggylake_firsttime_pcdrinks == 2: # 2 - ona pije, PC ma darmowy posiłek
                menu:
                    'You take a glance at the blood on the table, the scattered yellow feathers, and a bowl of guts and talons. You find yourself a clean stool.
                    \n\n{color=#f6d6bd}Foggy{/color} shows up soon, smiling, holding a plate with roasted meat and two cups squeezed right next to it, a bottle in her fingers, and a cloth under her shoulder. She puts everything on a stool and wipes the table clean. “Forgive the mess, just a part of the job,” she explains without a hint of apology. “I’d rather dress birds in the yard, but the blood lures beasts. Sometimes the folks from {color=#f6d6bd}Creeks{/color} bring us meals, but we need to take care of ourselves.”
                    \n\nShe throws the bloody cloth back into the bucket, making a splash, then sits down on a stool, making it look like it was made for a doll. She rests her elbow on the table and looks you in the eyes. Her voice is warm, yet intrusive. “So, who am I dealing with?”
                    '
                    'I introduce myself.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I introduce myself.')
                        menu:
                            'The bottle removes its seal seemingly by itself - the wax floats in the air briefly, then lands on the table gently. Without a word, she pours a thick liquid into the cups with her only hand, but doesn’t offer you your meal just yet.
                            '
                            '“I’m trying to learn more about the peninsula. A tavern seemed like a fair shot.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m trying to learn more about the peninsula. A tavern seemed like a fair shot.”')
                                jump foggylakefirsttime04p01learnaboutpeninsula
                            '“I’m looking for {color=#f6d6bd}Asterion{/color}, the previous roadwarden.”' if quest_asterion == 1 and not asterion_found:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for {color=#f6d6bd}Asterion{/color}, the previous roadwarden.”')
                                jump foggylakefirsttime04p01asterion
                            '“I’m going to need shelter every now and then. I stay on the road for most of my days.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m going to need shelter every now and then. I stay on the road for most of my days.”')
                                jump foggylakefirsttime04p01shelter
                            '“I always look for a place that will allow me to spend or gain a few coins.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I always look for a place that will allow me to spend or gain a few coins.”')
                                jump foggylakefirsttime04p01trade
                            '“I was hoping to find work. If nothing else, I can always carry a message for you.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I was hoping to find work. If nothing else, I can always carry a message for you.”')
                                jump foggylakefirsttime04p01work
                            '“I had to get here sooner or later.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I had to get here sooner or later.”')
                                jump foggylakefirsttime04p01noreason
            else: # 3 - ona pije, PC ma przekąskę.
                menu:
                    'You take a glance at the blood on the table, the scattered yellow feathers, and a bowl of guts and talons. You find yourself a clean stool.
                    \n\n{color=#f6d6bd}Foggy{/color} shows up soon, smiling, holding a plate with fruits and a cup squeezed among them, a bottle in her fingers, and a cloth under her shoulder. She puts everything on a stool and wipes the table clean. “Forgive the mess, just a part of the job,” she explains without a hint of apology. “I’d rather dress birds in the yard, but the blood lures beasts. Sometimes the folks from {color=#f6d6bd}Creeks{/color} bring us meals, but we need to take care of ourselves.”
                    \n\nShe throws the bloody cloth back into the bucket, making a splash, then sits down on a stool, making it look like it was made for a doll. She rests her elbow on the table and looks you in the eyes. Her voice is warm, yet intrusive. “So, who am I dealing with?”
                    '
                    'I introduce myself.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I introduce myself.')
                        menu:
                            'The bottle removes its seal seemingly by itself - the wax floats in the air briefly, then lands on the table gently. Without a word, she pours a thick liquid into the cup with her only hand, but doesn’t offer you any snacks just yet.
                            '
                            '“I’m trying to learn more about the peninsula. A tavern seemed like a fair shot.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m trying to learn more about the peninsula. A tavern seemed like a fair shot.”')
                                jump foggylakefirsttime04p01learnaboutpeninsula
                            '“I’m looking for {color=#f6d6bd}Asterion{/color}, the previous roadwarden.”' if quest_asterion == 1 and not asterion_found:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for {color=#f6d6bd}Asterion{/color}, the previous roadwarden.”')
                                jump foggylakefirsttime04p01asterion
                            '“I’m going to need shelter every now and then. I stay on the road for most of my days.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m going to need shelter every now and then. I stay on the road for most of my days.”')
                                jump foggylakefirsttime04p01shelter
                            '“I always look for a place that will allow me to spend or gain a few coins.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I always look for a place that will allow me to spend or gain a few coins.”')
                                jump foggylakefirsttime04p01trade
                            '“I was hoping to find work. If nothing else, I can always carry a message for you.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I was hoping to find work. If nothing else, I can always carry a message for you.”')
                                jump foggylakefirsttime04p01work
                            '“I had to get here sooner or later.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I had to get here sooner or later.”')
                                jump foggylakefirsttime04p01noreason

        label foggylakefirsttime04p01learnaboutpeninsula: # “I’m trying to learn more about the peninsula. A tavern seemed like a fair shot.”
            $ foggy_friendship -= 1
            if foggylake_firsttime_pcdrinks == 1: # 1 - piją oboje.
                $ custom1 = "She places the second cup in front of you. It’s made of dim brown wood, humble, wide, and short. Its surface is cold, rough, but elegant. In {color=#f6d6bd}Hovlavan{/color}, such vessels are often ornamented with metalwork, from bronze to gold, and bear all sorts of carvings and pictures."
                $ custom2 = "\n\nYou raise the cup to your nose. You smell flowers, yeast, and hops. The liquid is golden on the edges, but resembles red amber in the center. It’s as thick as an herbal medicament. You take a look at your companion, seeking a hint of what’s expected of you - in some places, people gulp down their mead, but your vessel allows you to appreciate the aroma. The huge keeper smiles and takes a sip. You follow her lead, allowing the drink to pass your lips.\n\nIt’s warm, hiding none of its subtleties. Drinking mead is a never-ending conflict between holding the taste in your mouth and saving yourself from the tormenting sweetness of honey. Yet the flavors of flowers are just as present, too difficult to capture just yet."
            elif foggylake_firsttime_pcdrinks == 2: # 2 - ona pije, PC ma darmowy posiłek
                $ pc_food = limit_pc_food(pc_food+2)
                show plus2food at foodchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 nourishment points.{/i}')
                $ custom1 = "She places the second cup in front of you. It’s made of dim brown wood, humble, wide, and short. Its surface is cold, rough, but elegant. In {color=#f6d6bd}Hovlavan{/color}, such vessels are often ornamented with metalwork, from bronze to gold, and bear all sorts of carvings and pictures."
                $ custom2 = "\n\nYou raise the cup to your nose. You smell flowers, yeast, and hops. The liquid is golden on the edges, but resembles red amber in the center. It’s as thick as an herbal medicament. You take a look at your companion, seeking a hint of what’s expected of you - in some places, people gulp down their mead, but your vessel allows you to appreciate the aroma. The huge keeper smiles and takes a sip. You follow her lead, allowing the drink to pass your lips.\n\nIt’s warm, hiding none of its subtleties. Drinking mead is a never-ending conflict between holding the taste in your mouth and saving yourself from the tormenting sweetness of honey. Yet the flavors of flowers are just as present, too difficult to capture just yet.\n\nThe food, on the other hand, is not too impressive. The torn pieces of a cold, roasted pheasant breast and a raw eggplant cut into slices. The fresh parsley and thyme will help you break the monotony of the meal."
            else: # 3 - ona pije, PC ma przekąskę.
                $ custom1 = "She places the simple, wooden plate in front of you. The snacks are divided into three small piles - dried plums, strips of a purple carrot, and slices of a juicy pear."
                $ custom2 = "\n\nThe flesh of the pear is still white, the carrot is firm and crisp. The plums can’t be from here - the place lacks a stove, so they were brought here from another settlement. They have a smoky aroma of burnt hazel twigs, smelling like winter food. Such snacks would be fitting even on the plates in the merchant guild."
            if foggylake_firsttime_pcdrinks == 1: # 1 - piją oboje.
                $ custom11 = "enjoy your drink"
            elif foggylake_firsttime_pcdrinks == 2: # 2 - ona pije, PC ma darmowy posiłek
                $ custom11 = "enjoy your meal"
            else: # 3 - ona pije, PC ma przekąskę.
                $ custom11 = "have a snack"
            menu:
                'She sighs and grabs her cup. It looks like she could crush it with just two fingers. “I don’t see hwat’s in it for me, dear. I’m sure you’ll find those who crave a pair of ears to fill it with gibberish, but I run this place to get more from it than I put into it.”
                \n\n[custom1]
                '
                '“Don’t you care about getting on a roadwarden’s good side?”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Don’t you care about getting on a roadwarden’s good side?”')
                    $ questionpreset = "foggy2"
                    menu:
                        '“Now, that would depend. Are we speaking of one who’s going to prove their worth and, let’s say, truthfulness? Or is it just a monkey on a horse who asks left and right for a free meal?” Her sudden grin makes you flinch. “The tales in this corner of The Land are as quick as a snail, but I’ve my ways of learning who makes waves around here. Hwy now, go ahead, [custom11].” [custom2]
                        \n\n{color=#f6d6bd}Foggy{/color} leans forward with an elbow resting on the table. “Well. For me, it’s a lazy [custom6]. At least the rains spare us, so nicely holding off till the evenings.”
                        '
                        '(preset foggy2)':
                            pass
                '“Keeping me around is an investment.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Keeping me around is an investment.”')
                    $ questionpreset = "foggy2"
                    $ foggy_about_rumors_available = 1
                    menu:
                        'She sighs, though with a smirk. “You’ve got me there. Sharing news is not a high price for an old hag if in return she gets a rider. The folks of {color=#f6d6bd}Gale Rocks{/color} trade more than anyone else, and the ones from {color=#f6d6bd}Creeks{/color} see a lot during their hunts. I know this and that ‘bout some places.” Her sudden grin makes you flinch. “Hwy, go ahead, [custom11].” [custom2]
                        \n\n{color=#f6d6bd}Foggy{/color} leans forward with an elbow resting on the table. “Well. For me, it’s a lazy [custom6]. At least the rains spare us, so nicely holding off till the evenings.”
                        '
                        '(preset foggy2)':
                            pass
                '“What would you like in return?”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What would you like in return?”')
                    $ foggy_friendship += 1
                    $ questionpreset = "foggy2"
                    menu:
                        'Her grin makes you think of a hungry wolf. “{i}Now{/i} we speak in the same tongue, just be sure to {i}act{/i} rather than {i}talk{/i}. I have a li’l thing on my soul that you could take care of. It’s not a hard task, but not something I’d trust the boys outside with.” She glances at both entrances. “We can talk ‘bout it later. Hwy now, go ahead, [custom11].” [custom2]
                        \n\n{color=#f6d6bd}Foggy{/color} leans forward with an elbow resting on the table. “Well. For me, it’s a lazy [custom6]. At least the rains spare us, so nicely holding off till the evenings.”
                        '
                        '(preset foggy2)':
                            pass
                'Awkward. For now, I don’t say anything.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Awkward. For now, I don’t say anything.')
                    $ foggy_friendship -= 1
                    $ questionpreset = "foggy1"
                    if foggy_about_shelter == 1:
                        $ can_rest = 1
                    if foggylake_firsttime_pcdrinks == 1: # 1 - piją oboje.
                        $ custom11 = "your cup"
                    elif foggylake_firsttime_pcdrinks == 2: # 2 - ona pije, PC ma darmowy posiłek
                        $ custom11 = "your cup"
                    else: # 3 - ona pije, PC ma przekąskę.
                        $ custom11 = "the plate with snacks"
                    menu:
                        'The keeper’s frustration grows in silence. Finally, she sighs. “Not much of a talker, are you? Go ahead, then,” she waves on you, looking at [custom11]. [custom2]
                        \n\nShe smiles, but her eyes are cold. “D’you need something?”
                        '
                        '(preset foggy1)':
                            pass

        label foggylakefirsttime04p01asterionALL:
            label foggylakefirsttime04p01asterion: # “I’m looking for {color=#f6d6bd}Asterion{/color}, the previous roadwarden.”
                if foggylake_firsttime_pcdrinks == 1: # 1 - piją oboje.
                    $ custom1 = "She places the second cup in front of you. It’s made of dim brown wood, humble, wide, and short. Its surface is cold, rough, but elegant. In {color=#f6d6bd}Hovlavan{/color}, such vessels are often ornamented with metalwork, from bronze to gold, and bear all sorts of carvings and pictures."
                    $ custom2 = "\n\nYou raise the cup to your nose. You smell flowers, yeast, and hops. The liquid is golden on the edges, but resembles red amber in the center. It’s as thick as an herbal medicament. You take a look at your companion, seeking a hint of what’s expected of you - in some places, people gulp down their mead, but your vessel allows you to appreciate the aroma. The huge keeper smiles and takes a sip. You follow her lead, allowing the drink to pass your lips.\n\nIt’s warm, hiding none of its subtleties. Drinking mead is a never-ending conflict between holding the taste in your mouth and saving yourself from the tormenting sweetness of honey. Yet the flavors of flowers are just as present, too difficult to capture just yet."
                elif foggylake_firsttime_pcdrinks == 2: # 2 - ona pije, PC ma darmowy posiłek
                    $ pc_food = limit_pc_food(pc_food+2)
                    show plus2food at foodchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 nourishment points.{/i}')
                    $ custom1 = "She places the second cup in front of you. It’s made of dim brown wood, humble, wide, and short. Its surface is cold, rough, but elegant. In {color=#f6d6bd}Hovlavan{/color}, such vessels are often ornamented with metalwork, from bronze to gold, and bear all sorts of carvings and pictures."
                    $ custom2 = "\n\nYou raise the cup to your nose. You smell flowers, yeast, and hops. The liquid is golden on the edges, but resembles red amber in the center. It’s as thick as an herbal medicament. You take a look at your companion, seeking a hint of what’s expected of you - in some places, people gulp down their mead, but your vessel allows you to appreciate the aroma. The huge keeper smiles and takes a sip. You follow her lead, allowing the drink to pass your lips.\n\nIt’s warm, hiding none of its subtleties. Drinking mead is a never-ending conflict between holding the taste in your mouth and saving yourself from the tormenting sweetness of honey. Yet the flavors of flowers are just as present, too difficult to capture just yet.\n\nThe food, on the other hand, is not too impressive. The torn pieces of a cold, roasted pheasant breast and a raw eggplant cut into slices. The fresh parsley and thyme will help you break the monotony of the meal."
                else: # 3 - ona pije, PC ma przekąskę.
                    $ custom1 = "She places the simple, wooden plate in front of you. The snacks are divided into three small piles - dried plums, strips of a purple carrot, and slices of a juicy pear."
                    $ custom2 = "\n\nThe flesh of the pear is still white, the carrot is firm and crisp. The plums can’t be from here - the place lacks a stove, so they were brought here from another settlement. They have a smoky aroma of burnt hazel twigs, smelling like winter food. Such snacks would be fitting even on the plates in the merchant guild."
                if foggylake_firsttime_pcdrinks == 1: # 1 - piją oboje.
                    $ custom3 = "enjoy your drink"
                elif foggylake_firsttime_pcdrinks == 2: # 2 - ona pije, PC ma darmowy posiłek
                    $ custom3 = "enjoy your meal"
                else: # 3 - ona pije, PC ma przekąskę.
                    $ custom3 = "have a snack"
                $ foggy_about_asterion = 1
                menu:
                    'She looks at you for a longer moment, without the slightest movement. “And hwy d’you think he’s here?”
                    '
                    '“I’m not saying that I do. But maybe you know where I can find him?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m not saying that I do. But maybe you know where I can find him?”')
                        $ custom5 = "“Ah, I misunderstood you,” she shakes her head and leans on the table. “I don’t know his whereabouts. He didn’t tell me a thing more than I needed to hear.”"
                        jump foggylakefirsttime04p01asterion02
                    '“{i}Is{/i} he here?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{i}Is{/i} he here?”')
                        $ foggy_friendship -= 1
                        menu:
                            'Her face darkens as she scratches her knee. “Don’t upset me.”
                            '
                            '“All I’m saying is that he might have been here. Wounded, or ill. I’m not trying to lure you into a game.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “All I’m saying is that he might have been here. Wounded, or ill. I’m not trying to lure you into a game.”')
                                $ custom5 = "“Every soul’s got a game, though some are not ready to admit it. But no, I don’t think he was struggling with health last time I saw him.”"
                                jump foggylakefirsttime04p01asterion02
                            '“Right now I suspect everyone. But I’m still looking for clues.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Right now I suspect everyone. But I’m still looking for clues.”')
                                $ custom5 = "“{i}Clues{/i}, aye. Ask me your questions, then. I don’t promise any answers, dear.”"
                                jump foggylakefirsttime04p01asterion02
                            '“He could have been swallowed by a toad for all I know. I’m just asking for help.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “He could have been swallowed by a toad for all I know. I’m just asking for help.”')
                                $ custom5 = "While her voice remains calm, her thin eyes get distrustful. “You’ve scared me a li’l bit. I don’t want any nasty rumors. Sure, some of those who travel through {color=#f6d6bd}Foggy’s{/color} disappear on the road, but it’s a safe place. We don’t hold slaves.” She waves toward the trapdoor. “You can check and see.”"
                                jump foggylakefirsttime04p01asterion02
                    '“I’m just asking around.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m just asking around.”')
                        $ custom5 = "While her voice remains calm, her thin eyes get distrustful. “You’ve scared me a li’l bit. I don’t want any nasty rumors. Sure, some of those who travel through {color=#f6d6bd}Foggy’s{/color} disappear on the road, but it’s a safe place. We don’t hold slaves.” She waves toward the trapdoor. “You can check and see.”"
                        jump foggylakefirsttime04p01asterion02

            label foggylakefirsttime04p01asterion02:
                menu:
                    '[custom5]
                    '
                    '“What can you tell me about him?”' if not foggy_about_questionsasterion4:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about him?”')
                        jump foggylakefirsttime04p01asterion03question04
                    '“When was the last time you saw {color=#f6d6bd}Asterion{/color}?”' if not foggy_about_questionsasterion1:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “When was the last time you saw {color=#f6d6bd}Asterion{/color}?”')
                        jump foggylakefirsttime04p01asterion03question01
                    '“Did he do any jobs for you?”' if not foggy_about_questionsasterion2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he do any jobs for you?”')
                        jump foggylakefirsttime04p01asterion03question02
                    '“Did he sell you anything unusual?”' if foggy_about_questionsasterion2 and not foggy_about_questionsasterion3:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he sell you anything unusual?”')
                        jump foggylakefirsttime04p01asterion03question03
                    '“You don’t sound especially bothered by his disappearance.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and not foggy_about_questionsasterion5:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t sound especially bothered by his disappearance.”')
                        jump foggylakefirsttime04p01asterion03question05
                    '“We’ll return to this later.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to this later.”')
                        jump foggylakefirsttime04p01asterion03

            label foggylakefirsttime04p01asterion03question04: # “What can you tell me about him?”
                $ foggy_about_questionsasterion4 = 1
                $ foggy_about_asterion_questions += 1
                $ minutes += 2
                menu:
                    'She rests her only hand across her stomach, which you identify as her version of crossing her arms. “A customer and an errand runner, hwat’s there to say?”
                    \n\nYour additional questions don’t get many more answers. She brings up the man’s looks and equipment, without adding much to what you’ve already learned from {color=#f6d6bd}Tulia{/color}.
                    \n\n“He was paying with dragons, rarely bartered,” she adds. “That’s hwat cityfolk do, aye? Seeking riches, then locking themselves in a chamber, prisoners of their might.”
                    '
                    'I smile. “Well said.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Well said.”')
                        menu:
                            'Her chuckle makes you think of a wolf’s growl.
                            '
                            '“What can you tell me about him?”' if not foggy_about_questionsasterion4:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about him?”')
                                jump foggylakefirsttime04p01asterion03question04
                            '“When was the last time you saw {color=#f6d6bd}Asterion{/color}?”' if not foggy_about_questionsasterion1:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “When was the last time you saw {color=#f6d6bd}Asterion{/color}?”')
                                jump foggylakefirsttime04p01asterion03question01
                            '“Did he do any jobs for you?”' if not foggy_about_questionsasterion2:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he do any jobs for you?”')
                                jump foggylakefirsttime04p01asterion03question02
                            '“Did he sell you anything unusual?”' if foggy_about_questionsasterion2 and not foggy_about_questionsasterion3:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he sell you anything unusual?”')
                                jump foggylakefirsttime04p01asterion03question03
                            '“You don’t sound especially bothered by his disappearance.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and not foggy_about_questionsasterion5:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t sound especially bothered by his disappearance.”')
                                jump foggylakefirsttime04p01asterion03question05
                            '“We’ll return to this later.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to this later.”')
                                jump foggylakefirsttime04p01asterion03
                    'I frown. “It’s not really what I’m aiming for.”' if pc_goal != "iwantmoney":
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I frown. “It’s not really what I’m aiming for.”')
                        menu:
                            '“We’ll see, love. We’ll see.”
                            '
                            '“What can you tell me about him?”' if not foggy_about_questionsasterion4:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about him?”')
                                jump foggylakefirsttime04p01asterion03question04
                            '“When was the last time you saw {color=#f6d6bd}Asterion{/color}?”' if not foggy_about_questionsasterion1:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “When was the last time you saw {color=#f6d6bd}Asterion{/color}?”')
                                jump foggylakefirsttime04p01asterion03question01
                            '“Did he do any jobs for you?”' if not foggy_about_questionsasterion2:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he do any jobs for you?”')
                                jump foggylakefirsttime04p01asterion03question02
                            '“Did he sell you anything unusual?”' if foggy_about_questionsasterion2 and not foggy_about_questionsasterion3:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he sell you anything unusual?”')
                                jump foggylakefirsttime04p01asterion03question03
                            '“You don’t sound especially bothered by his disappearance.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and not foggy_about_questionsasterion5:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t sound especially bothered by his disappearance.”')
                                jump foggylakefirsttime04p01asterion03question05
                            '“We’ll return to this later.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to this later.”')
                                jump foggylakefirsttime04p01asterion03
                    '(lie) I frown. “It’s not really what I’m aiming for.”' if pc_goal == "iwantmoney":
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) I frown. “It’s not really what I’m aiming for.”')
                        $ pc_lies += 1
                        menu:
                            '“We’ll see, love. We’ll see.”
                            '
                            '“What can you tell me about him?”' if not foggy_about_questionsasterion4:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about him?”')
                                jump foggylakefirsttime04p01asterion03question04
                            '“When was the last time you saw {color=#f6d6bd}Asterion{/color}?”' if not foggy_about_questionsasterion1:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “When was the last time you saw {color=#f6d6bd}Asterion{/color}?”')
                                jump foggylakefirsttime04p01asterion03question01
                            '“Did he do any jobs for you?”' if not foggy_about_questionsasterion2:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he do any jobs for you?”')
                                jump foggylakefirsttime04p01asterion03question02
                            '“Did he sell you anything unusual?”' if foggy_about_questionsasterion2 and not foggy_about_questionsasterion3:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he sell you anything unusual?”')
                                jump foggylakefirsttime04p01asterion03question03
                            '“You don’t sound especially bothered by his disappearance.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and not foggy_about_questionsasterion5:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t sound especially bothered by his disappearance.”')
                                jump foggylakefirsttime04p01asterion03question05
                            '“We’ll return to this later.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to this later.”')
                                jump foggylakefirsttime04p01asterion03
                    'I shrug. “I see no problem with that.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shrug. “I see no problem with that.”')
                        menu:
                            '“Sure you don’t. You can hide away from the awoken and the beasts, but having a {i}safe{/i} life is the dream of the fools. The next plague, the next war, the next dragon will come. There’s nowhere we can hide, but a pyre.”
                            '
                            '“What can you tell me about him?”' if not foggy_about_questionsasterion4:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about him?”')
                                jump foggylakefirsttime04p01asterion03question04
                            '“When was the last time you saw {color=#f6d6bd}Asterion{/color}?”' if not foggy_about_questionsasterion1:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “When was the last time you saw {color=#f6d6bd}Asterion{/color}?”')
                                jump foggylakefirsttime04p01asterion03question01
                            '“Did he do any jobs for you?”' if not foggy_about_questionsasterion2:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he do any jobs for you?”')
                                jump foggylakefirsttime04p01asterion03question02
                            '“Did he sell you anything unusual?”' if foggy_about_questionsasterion2 and not foggy_about_questionsasterion3:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he sell you anything unusual?”')
                                jump foggylakefirsttime04p01asterion03question03
                            '“You don’t sound especially bothered by his disappearance.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and not foggy_about_questionsasterion5:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t sound especially bothered by his disappearance.”')
                                jump foggylakefirsttime04p01asterion03question05
                            '“We’ll return to this later.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to this later.”')
                                jump foggylakefirsttime04p01asterion03

            label foggylakefirsttime04p01asterion03question01: # “When was the last time you saw {color=#f6d6bd}Asterion{/color}?”
                $ foggy_about_questionsasterion1 = 1
                $ foggy_about_asterion_questions += 1
                menu:
                    'She glances at a window. “Same as the others, in the late days of spring. We were waiting for his return, me and all the villages, then moved on. I’ve no idea where he went.”
                    '
                    '“{i}All{/i} of the villages, you say?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{i}All{/i} of the villages, you say?”')
                        menu:
                            'She turns toward you with the fierceness of a bear. “That’s hwat I said.”
                            '
                            '“What can you tell me about him?”' if not foggy_about_questionsasterion4:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about him?”')
                                jump foggylakefirsttime04p01asterion03question04
                            '“When was the last time you saw {color=#f6d6bd}Asterion{/color}?”' if not foggy_about_questionsasterion1:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “When was the last time you saw {color=#f6d6bd}Asterion{/color}?”')
                                jump foggylakefirsttime04p01asterion03question01
                            '“Did he do any jobs for you?”' if not foggy_about_questionsasterion2:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he do any jobs for you?”')
                                jump foggylakefirsttime04p01asterion03question02
                            '“Did he sell you anything unusual?”' if foggy_about_questionsasterion2 and not foggy_about_questionsasterion3:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he sell you anything unusual?”')
                                jump foggylakefirsttime04p01asterion03question03
                            '“You don’t sound especially bothered by his disappearance.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and not foggy_about_questionsasterion5:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t sound especially bothered by his disappearance.”')
                                jump foggylakefirsttime04p01asterion03question05
                            '“We’ll return to this later.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to this later.”')
                                jump foggylakefirsttime04p01asterion03
                    '“What can you tell me about him?”' if not foggy_about_questionsasterion4:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about him?”')
                        jump foggylakefirsttime04p01asterion03question04
                    '“When was the last time you saw {color=#f6d6bd}Asterion{/color}?”' if not foggy_about_questionsasterion1:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “When was the last time you saw {color=#f6d6bd}Asterion{/color}?”')
                        jump foggylakefirsttime04p01asterion03question01
                    '“Did he do any jobs for you?”' if not foggy_about_questionsasterion2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he do any jobs for you?”')
                        jump foggylakefirsttime04p01asterion03question02
                    '“Did he sell you anything unusual?”' if foggy_about_questionsasterion2 and not foggy_about_questionsasterion3:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he sell you anything unusual?”')
                        jump foggylakefirsttime04p01asterion03question03
                    '“You don’t sound especially bothered by his disappearance.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and not foggy_about_questionsasterion5:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t sound especially bothered by his disappearance.”')
                        jump foggylakefirsttime04p01asterion03question05
                    '“We’ll return to this later.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to this later.”')
                        jump foggylakefirsttime04p01asterion03

            label foggylakefirsttime04p01asterion03question02: # “Did he do any jobs for you?”
                $ foggy_about_questionsasterion2 = 2
                $ foggy_about_asterion_questions += 1
                menu:
                    'She presses her tongue against her cheek and lips. “Well, I’m not sure. He was bringing me news, or delivering my messages. Sold me some stuff, sometimes bought a thing or two. His life wasn’t really {i}that{/i} riveting. Just another mug guzzler, sitting in the corner, patching his clothes.”
                    '
                    '“What can you tell me about him?”' if not foggy_about_questionsasterion4:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about him?”')
                        jump foggylakefirsttime04p01asterion03question04
                    '“When was the last time you saw {color=#f6d6bd}Asterion{/color}?”' if not foggy_about_questionsasterion1:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “When was the last time you saw {color=#f6d6bd}Asterion{/color}?”')
                        jump foggylakefirsttime04p01asterion03question01
                    '“Did he do any jobs for you?”' if not foggy_about_questionsasterion2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he do any jobs for you?”')
                        jump foggylakefirsttime04p01asterion03question02
                    '“Did he sell you anything unusual?”' if foggy_about_questionsasterion2 and not foggy_about_questionsasterion3:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he sell you anything unusual?”')
                        jump foggylakefirsttime04p01asterion03question03
                    '“You don’t sound especially bothered by his disappearance.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and not foggy_about_questionsasterion5:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t sound especially bothered by his disappearance.”')
                        jump foggylakefirsttime04p01asterion03question05
                    '“We’ll return to this later.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to this later.”')
                        jump foggylakefirsttime04p01asterion03

            label foggylakefirsttime04p01asterion03question03: # “Did he sell you anything unusual?”
                $ foggy_about_questionsasterion3 = 1
                $ foggy_about_asterion_questions += 1
                menu:
                    'She stares at you without blinking. “Such’s hwat?”
                    '
                    '“Something that hints to where he went.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Something that hints to where he went.”')
                        menu:
                            'She frowns. “I’ll tell you if I think of anything.”
                            '
                            '“What can you tell me about him?”' if not foggy_about_questionsasterion4:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about him?”')
                                jump foggylakefirsttime04p01asterion03question04
                            '“When was the last time you saw {color=#f6d6bd}Asterion{/color}?”' if not foggy_about_questionsasterion1:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “When was the last time you saw {color=#f6d6bd}Asterion{/color}?”')
                                jump foggylakefirsttime04p01asterion03question01
                            '“Did he do any jobs for you?”' if not foggy_about_questionsasterion2:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he do any jobs for you?”')
                                jump foggylakefirsttime04p01asterion03question02
                            '“Did he sell you anything unusual?”' if foggy_about_questionsasterion2 and not foggy_about_questionsasterion3:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he sell you anything unusual?”')
                                jump foggylakefirsttime04p01asterion03question03
                            '“You don’t sound especially bothered by his disappearance.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and not foggy_about_questionsasterion5:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t sound especially bothered by his disappearance.”')
                                jump foggylakefirsttime04p01asterion03question05
                            '“We’ll return to this later.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to this later.”')
                                jump foggylakefirsttime04p01asterion03
                    '“Something he found in an unusual place.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Something he found in an unusual place.”')
                        menu:
                            '“Such tales stay between me and my guests.” She nods toward the wall that separates you from the lake. “This place may be open, maybe too open, but it guards secrets just fine.”
                            '
                            '“What can you tell me about him?”' if not foggy_about_questionsasterion4:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about him?”')
                                jump foggylakefirsttime04p01asterion03question04
                            '“When was the last time you saw {color=#f6d6bd}Asterion{/color}?”' if not foggy_about_questionsasterion1:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “When was the last time you saw {color=#f6d6bd}Asterion{/color}?”')
                                jump foggylakefirsttime04p01asterion03question01
                            '“Did he do any jobs for you?”' if not foggy_about_questionsasterion2:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he do any jobs for you?”')
                                jump foggylakefirsttime04p01asterion03question02
                            '“Did he sell you anything unusual?”' if foggy_about_questionsasterion2 and not foggy_about_questionsasterion3:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he sell you anything unusual?”')
                                jump foggylakefirsttime04p01asterion03question03
                            '“You don’t sound especially bothered by his disappearance.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and not foggy_about_questionsasterion5:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t sound especially bothered by his disappearance.”')
                                jump foggylakefirsttime04p01asterion03question05
                            '“We’ll return to this later.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to this later.”')
                                jump foggylakefirsttime04p01asterion03
                    '“Something useful. Maybe I could buy it back.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Something useful. Maybe I could buy it back.”')
                        $ foggy_friendship_tradepoints += 1
                        menu:
                            'The scar on her lips distorts her smile. “It just so happens...” She hesitates. “I promised to keep it around for some time. Ask me later, maybe after you’ve shown us what you’re made of. I’ll see what I can offer.”
                            '
                            '“What can you tell me about him?”' if not foggy_about_questionsasterion4:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about him?”')
                                jump foggylakefirsttime04p01asterion03question04
                            '“When was the last time you saw {color=#f6d6bd}Asterion{/color}?”' if not foggy_about_questionsasterion1:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “When was the last time you saw {color=#f6d6bd}Asterion{/color}?”')
                                jump foggylakefirsttime04p01asterion03question01
                            '“Did he do any jobs for you?”' if not foggy_about_questionsasterion2:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he do any jobs for you?”')
                                jump foggylakefirsttime04p01asterion03question02
                            '“Did he sell you anything unusual?”' if foggy_about_questionsasterion2 and not foggy_about_questionsasterion3:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he sell you anything unusual?”')
                                jump foggylakefirsttime04p01asterion03question03
                            '“You don’t sound especially bothered by his disappearance.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and not foggy_about_questionsasterion5:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t sound especially bothered by his disappearance.”')
                                jump foggylakefirsttime04p01asterion03question05
                            '“We’ll return to this later.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to this later.”')
                                jump foggylakefirsttime04p01asterion03

            label foggylakefirsttime04p01asterion03question05: # “You don’t sound especially bothered by his disappearance.”
                $ foggy_about_questionsasterion5 = 1
                menu:
                    '“You see me as someone eager to make friends with a vagabond? I’ll take it as a compliment to my skills as a tavernkeep. Folks come and go, their faces disappear, friends die in my arms,” she pauses, “families fade away. There was a different roadwarden years ago, and there is another one now. But there’s only one {color=#f6d6bd}Foggy{/color} in the North, and one {color=#f6d6bd}Ilan{/color}, that slow son of mine, and one {color=#f6d6bd}Creeks{/color}. I have only so many tears to spare.”
                    '
                    '“What can you tell me about him?”' if not foggy_about_questionsasterion4:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about him?”')
                        jump foggylakefirsttime04p01asterion03question04
                    '“When was the last time you saw {color=#f6d6bd}Asterion{/color}?”' if not foggy_about_questionsasterion1:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “When was the last time you saw {color=#f6d6bd}Asterion{/color}?”')
                        jump foggylakefirsttime04p01asterion03question01
                    '“Did he do any jobs for you?”' if not foggy_about_questionsasterion2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he do any jobs for you?”')
                        jump foggylakefirsttime04p01asterion03question02
                    '“Did he sell you anything unusual?”' if foggy_about_questionsasterion2 and not foggy_about_questionsasterion3:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he sell you anything unusual?”')
                        jump foggylakefirsttime04p01asterion03question03
                    '“You don’t sound especially bothered by his disappearance.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max and not foggy_about_questionsasterion5:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t sound especially bothered by his disappearance.”')
                        jump foggylakefirsttime04p01asterion03question05
                    '“We’ll return to this later.”' if foggy_about_asterion_questions >= foggy_about_asterion_questions_max:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll return to this later.”')
                        jump foggylakefirsttime04p01asterion03

            label foggylakefirsttime04p01asterion03:
                $ questionpreset = "foggy2"
                $ quarters += 1
                menu:
                    '“Maybe, maybe. Once our souls are too restless to stay quiet. But now, go ahead, [custom3].” [custom2]
                    \n\n{color=#f6d6bd}Foggy{/color} leans forward with an elbow resting on the table. “Well. For me, it’s a lazy [custom6]. At least the rains spare us, so nicely holding off till the evenings.”
                    '
                    '(preset foggy2)':
                        pass

        label foggylakefirsttime04p01shelter: # “I’m going to need shelter every now and then. I stay on the road for most of my days.”
            if foggylake_firsttime_pcdrinks == 1: # 1 - piją oboje.
                $ custom1 = "She places the second cup in front of you. It’s made of dim brown wood, humble, wide, and short. Its surface is cold, rough, but elegant. In {color=#f6d6bd}Hovlavan{/color}, such vessels are often ornamented with metalwork, from bronze to gold, and bear all sorts of carvings and pictures."
                $ custom2 = "\n\nYou raise the cup to your nose. You smell flowers, yeast, and hops. The liquid is golden on the edges, but resembles red amber in the center. It’s as thick as an herbal medicament. You take a look at your companion, seeking a hint of what’s expected of you - in some places, people gulp down their mead, but your vessel allows you to appreciate the aroma. The huge keeper smiles and takes a sip. You follow her lead, the drink touches your lips.\n\nIt’s warm, hiding none of its subtleties. Drinking mead is a never-ending conflict between holding the taste in your mouth and saving yourself from the tormenting sweetness of honey. Yet the flavors of flowers are just as present, too difficult to capture just yet."
            elif foggylake_firsttime_pcdrinks == 2: # 2 - ona pije, PC ma darmowy posiłek
                $ pc_food = limit_pc_food(pc_food+2)
                show plus2food at foodchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 nourishment points.{/i}')
                $ custom1 = "She places the second cup in front of you. It’s made of dim brown wood, humble, wide, and short. Its surface is cold, rough, but elegant. In {color=#f6d6bd}Hovlavan{/color}, such vessels are often ornamented with metalwork, from bronze to gold, and bear all sorts of carvings and pictures."
                $ custom2 = "\n\nYou raise the cup to your nose. You smell flowers, yeast, and hops. The liquid is golden on the edges, but resembles red amber in the center. It’s as thick as an herbal medicament. You take a look at your companion, seeking a hint of what’s expected of you - in some places, people gulp down their mead, but your vessel allows you to appreciate the aroma. The huge keeper smiles and takes a sip. You follow her lead, allowing the drink to pass your lips.\n\nIt’s warm, hiding none of its subtleties. Drinking mead is a never-ending conflict between holding the taste in your mouth and saving yourself from the tormenting sweetness of honey. Yet the flavors of flowers are just as present, too difficult to capture just yet.\n\nThe food, on the other hand, is not too impressive. The torn pieces of a cold, roasted pheasant breast and a raw eggplant cut into slices. The fresh parsley and thyme will help you break the monotony of the meal."
            else: # 3 - ona pije, PC ma przekąskę.
                $ custom1 = "She places the simple, wooden plate in front of you. The snacks are divided into three small piles - dried plums, strips of a purple carrot, and slices of a juicy pear."
                $ custom2 = "\n\nThe flesh of the pear is still white, the carrot is firm and crisp. The plums can’t be from here - the place lacks a stove, so they were brought here from another settlement. They have a smoky aroma of burnt hazel twigs, smelling like winter food. Such snacks would be fitting even on the plates in the merchant guild."
            if foggylake_firsttime_pcdrinks == 1: # 1 - piją oboje.
                $ custom3 = "enjoy your drink"
            elif foggylake_firsttime_pcdrinks == 2: # 2 - ona pije, PC ma darmowy posiłek
                $ custom3 = "enjoy your meal"
            else: # 3 - ona pije, PC ma przekąskę.
                $ custom3 = "have a snack"
            $ questionpreset = "foggy2"
            $ foggy_about_shelter = 1
            $ renpy.notify("New shelter unlocked.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New shelter unlocked.{/i}')
            menu:
                'She approaches a window above the table and looks outside. “Your beast won’t make it easy for us, dear.” She places her hand on the shutters. “It’s not a city inn, I don’t cook for a smile, I don’t work to feel noble. I allow folks to lie down there for free,” she points to the bear fur with her broad chin, “but that’s ‘bout it. If your horse stays outside, it’ll lure the beasts to us, but if we move it here, upstairs, it’ll leave its droppings on my floor.” She gets annoyed even by the idea of it happening. “If you want to rest here, love, be ready either to pay with a coin or some food rations, or to spend the night keeping your mount quiet. And clean after it in the morning, will you?” She gives you a wide grin and moves back to the stool. “Hwy now, go ahead, [custom3].” [custom2]
                \n\n{color=#f6d6bd}Foggy{/color} leans forward with an elbow resting on the table. “Well. For me, it’s a lazy [custom6]. At least the rains spare us, so nicely holding off till the evenings.”
                '
                '(preset foggy2)':
                    pass

        label foggylakefirsttime04p01trade: # “I always look for a place that will allow me to spend or gain a few coins.”
            $ foggy_friendship += 1
            if foggylake_firsttime_pcdrinks == 1: # 1 - piją oboje.
                $ custom1 = "She places the second cup in front of you. It’s made of dim brown wood, humble, wide, and short. Its surface is cold, rough, but elegant. In {color=#f6d6bd}Hovlavan{/color}, such vessels are often ornamented with metalwork, from bronze to gold, and bear all sorts of carvings and pictures."
                $ custom2 = "\n\nYou raise the cup to your nose. You smell flowers, yeast, and hops. The liquid is golden on the edges, but resembles red amber in the center. It’s as thick as an herbal medicament. You take a look at your companion, seeking a hint of what’s expected of you - in some places, people gulp down their mead, but your vessel allows you to appreciate the aroma. The huge keeper smiles and takes a sip. You follow her lead, allowing the drink to pass your lips.\n\nIt’s warm, hiding none of its subtleties. Drinking mead is a never-ending conflict between holding the taste in your mouth and saving yourself from the tormenting sweetness of honey. Yet the flavors of flowers are just as present, too difficult to capture just yet."
            elif foggylake_firsttime_pcdrinks == 2: # 2 - ona pije, PC ma darmowy posiłek
                $ pc_food = limit_pc_food(pc_food+2)
                show plus2food at foodchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 nourishment points.{/i}')
                $ custom1 = "She places the second cup in front of you. It’s made of dim brown wood, humble, wide, and short. Its surface is cold, rough, but elegant. In {color=#f6d6bd}Hovlavan{/color}, such vessels are often ornamented with metalwork, from bronze to gold, and bear all sorts of carvings and pictures."
                $ custom2 = "\n\nYou raise the cup to your nose. You smell flowers, yeast, and hops. The liquid is golden on the edges, but resembles red amber in the center. It’s as thick as an herbal medicament. You take a look at your companion, seeking a hint of what’s expected of you - in some places, people gulp down their mead, but your vessel allows you to appreciate the aroma. The huge keeper smiles and takes a sip. You follow her lead, allowing the drink to pass your lips.\n\nIt’s warm, hiding none of its subtleties. Drinking mead is a never-ending conflict between holding the taste in your mouth and saving yourself from the tormenting sweetness of honey. Yet the flavors of flowers are just as present, too difficult to capture just yet.\n\nThe food, on the other hand, is not too impressive. The torn pieces of a cold, roasted pheasant breast and a raw eggplant cut into slices. The fresh parsley and thyme will help you break the monotony of the meal."
            else: # 3 - ona pije, PC ma przekąskę.
                $ custom1 = "She places the simple, wooden plate in front of you. The snacks are divided into three small piles - dried plums, strips of a purple carrot, and slices of a juicy pear."
                $ custom2 = "\n\nThe flesh of the pear is still white, the carrot is firm and crisp. The plums can’t be from here - the place lacks a stove, so they were brought here from another settlement. They have a smoky aroma of burnt hazel twigs, smelling like winter food. Such snacks would be fitting even on the plates in the merchant guild."
            if foggylake_firsttime_pcdrinks == 1: # 1 - piją oboje.
                $ custom3 = "enjoy your drink"
            elif foggylake_firsttime_pcdrinks == 2: # 2 - ona pije, PC ma darmowy posiłek
                $ custom3 = "enjoy your meal"
            else: # 3 - ona pije, PC ma przekąskę.
                $ custom3 = "have a snack"
            $ questionpreset = "foggy2"
            $ description_foggy05 = "She has a great interest in animal trophies, especially those gathered from dangerous creatures, weapons, and hard drinks."
            menu:
                'Her grin makes you think of a hungry wolf. “We speak in the same tongue, love. This scrap of land has close to no traders, and I need dragons to turn this hovel into a real inn. I won’t take some trinkets or chunks of iron, but let me know once you find some animal trophies, as long as they’re impressive. Or strong drinks. Or weapons. I never have too many of those.” She leans back, relaxed and confident. “I’ll show you later what I have to sell. Hwy now, go ahead, [custom3].” [custom2]
                \n\n{color=#f6d6bd}Foggy{/color} leans forward with an elbow resting on the table. “Well. For me, it’s a lazy [custom6]. At least the rains spare us, so nicely holding off till the evenings.”
                '
                '(preset foggy2)':
                    pass

        label foggylakefirsttime04p01work: # “I was hoping to find work. If nothing else, I can always carry a message for you.”
            $ foggy_friendship += 1
            if foggylake_firsttime_pcdrinks == 1: # 1 - piją oboje.
                $ custom1 = "She places the second cup in front of you. It’s made of dim brown wood, humble, wide, and short. Its surface is cold, rough, but elegant. In {color=#f6d6bd}Hovlavan{/color}, such vessels are often ornamented with metalwork, from bronze to gold, and bear all sorts of carvings and pictures."
                $ custom2 = "\n\nYou raise the cup to your nose. You smell flowers, yeast, and hops. The liquid is golden on the edges, but resembles red amber in the center. It’s as thick as an herbal medicament. You take a look at your companion, seeking a hint of what’s expected of you - in some places, people gulp down their mead, but your vessel allows you to appreciate the aroma. The huge keeper smiles and takes a sip. You follow her lead, allowing the drink to pass your lips.\n\nIt’s warm, hiding none of its subtleties. Drinking mead is a never-ending conflict between holding the taste in your mouth and saving yourself from the tormenting sweetness of honey. Yet the flavors of flowers are just as present, too difficult to capture just yet."
            elif foggylake_firsttime_pcdrinks == 2: # 2 - ona pije, PC ma darmowy posiłek
                $ pc_food = limit_pc_food(pc_food+2)
                show plus2food at foodchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 nourishment points.{/i}')
                $ custom1 = "She places the second cup in front of you. It’s made of dim brown wood, humble, wide, and short. Its surface is cold, rough, but elegant. In {color=#f6d6bd}Hovlavan{/color}, such vessels are often ornamented with metalwork, from bronze to gold, and bear all sorts of carvings and pictures."
                $ custom2 = "\n\nYou raise the cup to your nose. You smell flowers, yeast, and hops. The liquid is golden on the edges, but resembles red amber in the center. It’s as thick as an herbal medicament. You take a look at your companion, seeking a hint of what’s expected of you - in some places, people gulp down their mead, but your vessel allows you to appreciate the aroma. The huge keeper smiles and takes a sip. You follow her lead, allowing the drink to pass your lips.\n\nIt’s warm, hiding none of its subtleties. Drinking mead is a never-ending conflict between holding the taste in your mouth and saving yourself from the tormenting sweetness of honey. Yet the flavors of flowers are just as present, too difficult to capture just yet.\n\nThe food, on the other hand, is not too impressive. The torn pieces of a cold, roasted pheasant breast and a raw eggplant cut into slices. The fresh parsley and thyme will help you break the monotony of the meal."
            else: # 3 - ona pije, PC ma przekąskę.
                $ custom1 = "She places the simple, wooden plate in front of you. The snacks are divided into three small piles - dried plums, strips of a purple carrot, and slices of a juicy pear."
                $ custom2 = "\n\nThe flesh of the pear is still white, the carrot is firm and crisp. The plums can’t be from here - the place lacks a stove, so they were brought here from another settlement. They have a smoky aroma of burnt hazel twigs, smelling like winter food. Such snacks would be fitting even on the plates in the merchant guild."
            if foggylake_firsttime_pcdrinks == 1: # 1 - piją oboje.
                $ custom11 = "enjoy your drink"
            elif foggylake_firsttime_pcdrinks == 2: # 2 - ona pije, PC ma darmowy posiłek
                $ custom11 = "enjoy your meal"
            else: # 3 - ona pije, PC ma przekąskę.
                $ custom11 = "have a snack"
            if armor >= 3:
                $ custom3 = "She points at your chest. “I see your jacket is plenty fine. It should be enough, but you can always fix it in {color=#f6d6bd}Gale Rocks{/color}, or in {color=#f6d6bd}Howler’s{/color}.” She nods approvingly."
                if item_shield:
                    $ custom4 = "“And I saw a shield on your mount. Better keep it close.”"
                else:
                    $ custom4 = "“But I haven’t seen any shield by your saddle. Better visit {color=#f6d6bd}Gale Rocks{/color} and buy yourself one.”"
            elif armor == 2:
                $ custom3 = "She points at your chest. “Your jacket could use some work. {color=#f6d6bd}Bion{/color} from {color=#f6d6bd}Howler’s Dell{/color} uses spider silk, she’s like a mage with a needle. But the folks at {color=#f6d6bd}Gale Rocks{/color} can also do some repairs.” She smiles."
                if item_shield:
                    $ custom4 = "“And I saw a shield on your mount. Better keep it close.”"
                else:
                    $ custom4 = "“But I haven’t seen any shield by your saddle. Better visit {color=#f6d6bd}Gale Rocks{/color} and buy yourself one.”"
            else:
                $ custom3 = "She points at your chest. “Your jacket won’t cut it. Better visit {color=#f6d6bd}Gale Rocks{/color}, they’ll be able to do something ‘bout it. Not for free, aye, but you won’t need a full pouch if you’re dead.” She smiles."
                if item_shield:
                    $ custom4 = "“And I saw a shield obn your mount. Better keep it close.”"
                else:
                    $ custom4 = "“But I haven’t seen any shield by your saddle. You can also buy yourself one in the village.”"
            $ questionpreset = "foggy2"
            menu:
                'Her grin makes you think of a hungry wolf. “To me, you sound more like a mercenary than a roadwarden, but we speak in the same tongue. You will find some work around here.” She cracks her knuckles just by clenching her fist, then relaxes her hand and observes the fingers. “I may have a small job for you, love. And the boys outside want to hunt, ask them ‘bout it if you want to join them. Just be sure you have something to defend yourself with.” [custom3] [custom4]
                \n\nShe leans back, relaxed and confident. “Hwy now, go ahead, [custom11].” [custom2]
                \n\n{color=#f6d6bd}Foggy{/color} leans forward with an elbow resting on the table. “Well. For me, it’s a lazy [custom6]. At least the rains spare us, so nicely holding off till the evenings.”
                '
                '(preset foggy2)':
                    pass

        label foggylakefirsttime04p01noreason: # “I had to get here sooner or later.”
            $ foggy_friendship -= 1
            if foggylake_firsttime_pcdrinks == 1: # 1 - piją oboje.
                $ custom1 = "She places the second cup in front of you. It’s made of dim brown wood, humble, wide, and short. Its surface is cold, rough, but elegant. In {color=#f6d6bd}Hovlavan{/color}, such vessels are often ornamented with metalwork, from bronze to gold, and bear all sorts of carvings and pictures."
                $ custom2 = "\n\nYou raise the cup to your nose. You smell flowers, yeast, and hops. The liquid is golden on the edges, but resembles red amber in the center. It’s as thick as an herbal medicament. You take a look at your companion, seeking a hint of what’s expected of you - in some places, people gulp down their mead, but your vessel allows you to appreciate the aroma. The huge keeper smiles and takes a sip. You follow her lead, allowing the drink to pass your lips.\n\nIt’s warm, hiding none of its subtleties. Drinking mead is a never-ending conflict between holding the taste in your mouth and saving yourself from the tormenting sweetness of honey. Yet the flavors of flowers are just as present, too difficult to capture just yet."
            elif foggylake_firsttime_pcdrinks == 2: # 2 - ona pije, PC ma darmowy posiłek
                $ pc_food = limit_pc_food(pc_food+2)
                show plus2food at foodchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 nourishment points.{/i}')
                $ custom1 = "She places the second cup in front of you. It’s made of dim brown wood, humble, wide, and short. Its surface is cold, rough, but elegant. In {color=#f6d6bd}Hovlavan{/color}, such vessels are often ornamented with metalwork, from bronze to gold, and bear all sorts of carvings and pictures."
                $ custom2 = "\n\nYou raise the cup to your nose. You smell flowers, yeast, and hops. The liquid is golden on the edges, but resembles red amber in the center. It’s as thick as an herbal medicament. You take a look at your companion, seeking a hint of what’s expected of you - in some places, people gulp down their mead, but your vessel allows you to appreciate the aroma. The huge keeper smiles and takes a sip. You follow her lead, allowing the drink to pass your lips.\n\nIt’s warm, hiding none of its subtleties. Drinking mead is a never-ending conflict between holding the taste in your mouth and saving yourself from the tormenting sweetness of honey. Yet the flavors of flowers are just as present, too difficult to capture just yet.\n\nThe food, on the other hand, is not too impressive. The torn pieces of a cold, roasted pheasant breast and a raw eggplant cut into slices. The fresh parsley and thyme will help you break the monotony of the meal."
            else: # 3 - ona pije, PC ma przekąskę.
                $ custom1 = "She places the simple, wooden plate in front of you. The snacks are divided into three small piles - dried plums, strips of a purple carrot, and slices of a juicy pear."
                $ custom2 = "\n\nThe flesh of the pear is still white, the carrot is firm and crisp. The plums can’t be from here - the place lacks a stove, so they were brought here from another settlement. They have a smoky aroma of burnt hazel twigs, smelling like winter food. Such snacks would be fitting even on the plates in the merchant guild."
            if foggylake_firsttime_pcdrinks == 1: # 1 - piją oboje.
                $ custom11 = "enjoy your drink"
            elif foggylake_firsttime_pcdrinks == 2: # 2 - ona pije, PC ma darmowy posiłek
                $ custom11 = "enjoy your meal"
            else: # 3 - ona pije, PC ma przekąskę.
                $ custom11 = "have a snack"
            $ questionpreset = "foggy2"
            $ foggy_about_bandits_available = 1
            menu:
                'Her tone is far from amused. “Almost no soul would say that these days, not in this corner of The Land. Every few days I get here my tribesfolk from {color=#f6d6bd}Creeks{/color}, every few dozen days some traders from {color=#f6d6bd}Gale Rocks{/color}, and a few times a year from distant villages. But travelers? They are a thing of the past. All that’s left are...” she hesitates, then waves it off. “Hwy now, go ahead, [custom11].” [custom2]
                \n\n{color=#f6d6bd}Foggy{/color} leans forward with an elbow resting on the table. “Well. For me, it’s a lazy [custom6]. At least the rains spare us, so nicely holding off till the evenings.”
                '
                '(preset foggy2)':
                    pass

label foggylakeregular01: # przybycie do zewnątrz
    $ renpy.force_autosave(take_screenshot=True, block=True)
    $ can_leave = 1
    if foggy_about_shelter == 1:
        $ can_rest = 1
    else:
        $ can_rest = 0
    $ can_items = 1
    menu:
        '[foggylake_fluff_outside]
        \n\n[foggylake_fluff_outside2]
        '
        'I enter the tavern.':
            jump foggylakeinside01
        'I approach the foragers.' ( condition="(quarters < (world_daylength-4) and quest_asterion == 1 and quest_gatheracrew == 1 and not asterion_found and not foragers_about_gatherthecrew_tzvi_recruited and not foragers_about_gatherthecrew_rejected) or (quarters < (world_daylength-4) and quest_missinghunters == 1 and not foragers_about_missinghunters) or (quarters < (world_daylength-4) and oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_knowledge and not foragers_about_traps) or (quarters < (world_daylength-4) and not foragers_quest and not day > foragingground_quest_timer and not foragingground_bird_gone) or (quarters < (world_daylength-4) and quest_birdhunting == 1) or (quarters < (world_daylength-4) and foragers_caius_heardabout and not foragers_caius_spokento) or (quarters < (world_daylength-4) and foggy_about_militarycamp and not foragers_caius_heardabout and not foragers_caius_aboutvision) or (quarters < (world_daylength-4) and foragers_caius_heardabout and foragers_caius_spokento and not foragers_caius_aboutvision) or (quarters < (world_daylength-4) and not foragers_about_travelers) or (quarters < (world_daylength-4) and not foragers_about_rumors) or (quarters < (world_daylength-4) and ruinedshelter_mushrooms and not foggy_about_mushroomsinruinedshelter and not foragers_about_mushrooms) or (quarters < (world_daylength-4) and not quest_recruitahunter_spokento_foragers and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed)" ):
            jump foggylakeforagers01
        'I have nothing to say to the foragers. (disabled)' ( condition="not (quest_asterion == 1 and quest_gatheracrew == 1 and not asterion_found and not foragers_about_gatherthecrew_tzvi_recruited and not foragers_about_gatherthecrew_rejected) and not (quest_missinghunters == 1 and not foragers_about_missinghunters) and not (oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_knowledge and not foragers_about_traps) and not (not foragers_quest and not day > foragingground_quest_timer and not foragingground_bird_gone) and not (quest_birdhunting == 1) and not (foragers_caius_heardabout and not foragers_caius_spokento) and not (foggy_about_militarycamp and not foragers_caius_heardabout and not foragers_caius_aboutvision) and not (foragers_caius_heardabout and foragers_caius_spokento and not foragers_caius_aboutvision) and not (not foragers_about_travelers) and not (not foragers_about_rumors) and not (ruinedshelter_mushrooms and not foggy_about_mushroomsinruinedshelter and not foragers_about_mushrooms) and not (not quest_recruitahunter_spokento_foragers and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed)" ):
            pass
        'The foragers are preparing for the night. (disabled)' ( condition="(quarters >= (world_daylength-4) and quest_asterion == 1 and quest_gatheracrew == 1 and not asterion_found and not foragers_about_gatherthecrew_tzvi_recruited and not foragers_about_gatherthecrew_rejected) or (quarters >= (world_daylength-4) and quest_missinghunters == 1 and not foragers_about_missinghunters) or (quarters >= (world_daylength-4) and oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_knowledge and not foragers_about_traps) or (quarters >= (world_daylength-4) and not foragers_quest and not day > foragingground_quest_timer and not foragingground_bird_gone) or (quarters >= (world_daylength-4) and quest_birdhunting == 1) or (quarters >= (world_daylength-4) and foragers_caius_heardabout and not foragers_caius_spokento) or (quarters >= (world_daylength-4) and foggy_about_militarycamp and not foragers_caius_heardabout and not foragers_caius_aboutvision) or (quarters >= (world_daylength-4) and foragers_caius_heardabout and foragers_caius_spokento and not foragers_caius_aboutvision) or (quarters >= (world_daylength-4) and not foragers_about_travelers) or (quarters >= (world_daylength-4) and not foragers_about_rumors) or (quarters >= (world_daylength-4) and ruinedshelter_mushrooms and not foggy_about_mushroomsinruinedshelter and not foragers_about_mushrooms) or (quarters >= (world_daylength-4) and not quest_recruitahunter_spokento_foragers and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed)" ):
            pass
        'I could wash myself in the lake.' if not foggylake_bath:
            jump foggylakelake01

label foggylakeinside01: # wejście do środka
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the tavern.')
    $ renpy.force_autosave(take_screenshot=True, block=True)
    $ can_leave = 0
    if foggy_about_shelter == 1:
        $ can_rest = 1
    else:
        $ can_rest = 0
    $ can_items = 1
    show areapicture foggylakeinside01 at basicfade
    if not foggylake_inside_lastvisit:
        $ foggylake_inside_lastvisit = 1
        if foggy_friendship < 0:
            $ custom1 = "She notices your arrival, but doesn’t say anything."
        elif foggy_friendship < 5:
            $ custom1 = "She welcomes you with a gentle nod."
        elif foggy_friendship < 10:
            $ custom1 = "She welcomes you with a smile."
        else:
            $ custom1 = "She welcomes you with a stentorian, cheerful shout. “Hello, love! Good to see you in one piece.”"
        if foggylake_alchemytable_firsttime:
            menu:
                '[foggylake_fluff_inside]
                \n\n[foggylake_fluff_inside2] [custom1]
                '
                'I approach {color=#f6d6bd}Foggy{/color}.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach {color=#f6d6bd}Foggy{/color}.')
                    $ questionpreset = "foggy1"
                    if foggy_friendship < 0:
                        $ custom2 = "“Aye? Need something?”"
                    elif foggy_friendship < 5:
                        $ custom2 = "“Need anything, dear?”"
                    elif foggy_friendship < 10:
                        $ custom2 = "“How can I help you, love?”"
                    else:
                        $ custom2 = ""
                        if foggy_about_shelter == 1:
                            $ can_rest = 1
                        $ can_rest = 0
                        $ can_items = 0
                        menu:
                            '“So, [pcname]! Hwat d’you need?”
                            '
                            '(preset foggy1)':
                                pass
                    $ can_leave = 0
                    if foggy_about_shelter == 1:
                        $ can_rest = 1
                    $ can_items = 0
                    menu:
                        '[custom2]
                        '
                        '(preset foggy1)':
                            pass
                '{image=cointest} I go downstairs, to {color=#f6d6bd}the alchemy set{/color}.' ( condition="(quarters < world_daylength and foggylake_alchemytable_firsttime and pc_hp) or (quarters >= world_daylength and foggylake_alchemytable_firsttime and pc_hp and alchemytable_timer < day)" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} I go downstairs, to {color=#f6d6bd}the alchemy set{/color}.')
                    jump foggylakealchemytable01
                'I’m too exhausted to brew potions. (Required vitality: 1) (disabled)' ( condition="foggylake_alchemytable_firsttime and not pc_hp" ):
                    pass
                'It’s already late, and my eyes hurt after the last potion I brewed. (disabled)' if foggylake_alchemytable_firsttime and alchemytable_timer >= day:
                    pass
                'I go outside.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
                    jump foggylakeoutside01
        else:
            $ questionpreset = "foggy1"
            $ can_leave = 0
            if foggy_about_shelter == 1:
                $ can_rest = 1
            $ can_items = 0
            menu:
                '[foggylake_fluff_inside]
                \n\n[foggylake_fluff_inside2] [custom1]
                '
                '(preset foggy1)':
                    pass
    else:
        label foggylake_fluff_inside3loop2: # zachowanie Foggy po powrocie
            $ foggylake_fluff_inside3 = ""
            $ foggylake_fluff_inside3 = renpy.random.choice(['{color=#f6d6bd}Foggy{/color} is resting on a chair, observing you with a single open eye.', '{color=#f6d6bd}Foggy{/color} is kneeling by the hearth, removing ash and washing the cauldron.', '{color=#f6d6bd}Foggy{/color} is eating stew from a bowl, but once she sees you, she finishes it with a few large gulps.', '{color=#f6d6bd}Foggy{/color} is bringing inside a bucket of water from the lake.', '{color=#f6d6bd}Foggy{/color} and the one-armed man cease their conversation.', '{color=#f6d6bd}Foggy{/color} sniffs contents of one of the bottles.'])
            if foggylake_fluff_inside3old == foggylake_fluff_inside3:
                jump foggylake_fluff_inside3loop2
            else:
                $ foggylake_fluff_inside3old = foggylake_fluff_inside3
            $ can_leave = 0
            if foggy_about_shelter == 1:
                $ can_rest = 1
            else:
                $ can_rest = 0
            $ can_items = 1
            if foggylake_alchemytable_firsttime:
                menu:
                    '[foggylake_fluff_inside3]
                    '
                    'I approach {color=#f6d6bd}Foggy{/color}.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach {color=#f6d6bd}Foggy{/color}.')
                        $ questionpreset = "foggy1"
                        if foggy_friendship < 0:
                            $ custom2 = "She looks at you in silence."
                        elif foggy_friendship < 5:
                            $ custom2 = "She turns toward you and waits for you to speak."
                        elif foggy_friendship < 10:
                            $ custom2 = "She smiles at you."
                        else:
                            $ custom2 = "She smiles at you. “Something else?”"
                        $ can_leave = 0
                        if foggy_about_shelter == 1:
                            $ can_rest = 1
                        $ can_items = 0
                        menu:
                            '[custom2]
                            '
                            '(preset foggy1)':
                                pass
                    '{image=cointest} I go downstairs, to {color=#f6d6bd}the alchemy set{/color}.' ( condition="(quarters < world_daylength and foggylake_alchemytable_firsttime and pc_hp) or (quarters >= world_daylength and foggylake_alchemytable_firsttime and pc_hp and alchemytable_timer < day)" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} I go downstairs, to {color=#f6d6bd}the alchemy set{/color}.')
                        jump foggylakealchemytable01
                    'I’m too exhausted to brew potions. (Required vitality: 1) (disabled)' ( condition="foggylake_alchemytable_firsttime and not pc_hp" ):
                        pass
                    'It’s already late, and my eyes hurt after the last potion I brewed. (disabled)' if foggylake_alchemytable_firsttime and alchemytable_timer >= day:
                        pass
                    'I go outside.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
                        jump foggylakeoutside01
            else:
                $ questionpreset = "foggy1"
                $ can_leave = 0
                if foggy_about_shelter == 1:
                    $ can_rest = 1
                $ can_items = 0
                menu:
                    '[foggylake_fluff_inside3]
                    '
                    '(preset foggy1)':
                        pass

label foggylakeafterfoggy01: # odstąpienie od foggy
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Time for me to go.”')
    $ can_leave = 0
    if foggy_about_shelter == 1:
        $ can_rest = 1
    else:
        $ can_rest = 0
    $ can_items = 1
    show areapicture foggylakeinside01 at basicfade
    menu:
        'You look around the chamber.
        '
        'I approach {color=#f6d6bd}Foggy{/color}.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach {color=#f6d6bd}Foggy{/color}.')
            $ questionpreset = "foggy1"
            if foggy_friendship < 0:
                $ custom2 = "“Aye? Need something?”"
            elif foggy_friendship < 5:
                $ custom2 = "“Need anything, dear?”"
            elif foggy_friendship < 10:
                $ custom2 = "“How can I help you, love?”"
            else:
                $ custom2 = ""
                $ can_leave = 0
                if foggy_about_shelter == 1:
                    $ can_rest = 1
                $ can_items = 0
                menu:
                    '“So, [pcname]! Hwat d’you need?”
                    '
                    '(preset foggy1)':
                        pass
            $ can_leave = 0
            if foggy_about_shelter == 1:
                $ can_rest = 1
            $ can_items = 0
            menu:
                '[custom2]
                '
                '(preset foggy1)':
                    pass
        '{image=cointest} I go downstairs, to {color=#f6d6bd}the alchemy set{/color}.' ( condition="(quarters < world_daylength and foggylake_alchemytable_firsttime and pc_hp) or (quarters >= world_daylength and foggylake_alchemytable_firsttime and pc_hp and alchemytable_timer < day)" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} I go downstairs, to {color=#f6d6bd}the alchemy set{/color}.')
            jump foggylakealchemytable01
        'I’m too exhausted to brew potions. (Required vitality: 1) (disabled)' ( condition="foggylake_alchemytable_firsttime and not pc_hp" ):
            pass
        'It’s already late, and my eyes hurt after the last potion I brewed. (disabled)' if foggylake_alchemytable_firsttime and alchemytable_timer >= day:
            pass
        'I go outside.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
            jump foggylakeoutside01

label foggylakeoutside01: # wyjście ze środka na zewnątrz
    $ renpy.force_autosave(take_screenshot=True, block=True)
    $ can_leave = 1
    if foggy_about_shelter == 1:
        $ can_rest = 1
    else:
        $ can_rest = 0
    $ can_items = 1
    if quarters >= 36 and quarters < (world_daylength-4):
        show areapicture foggylakeoutsideopen01 at basicfade
    else:
        show areapicture foggylakeoutsideclosed01 at basicfade
    $ foggylake_firsttime_afterdrink = 1
    if tutorial_selling == 1:
        $ tutorial_selling = 2
    if tutorial_selling2 == 1:
        $ tutorial_selling2 = 2
    $ foggylake_horsename_fluff = ""
    $ foggylake_horsename_fluff = renpy.random.choice(['enjoying some fresh grass', 'napping', 'observing the movement on the lake', 'around slowly moving, as far as its cord allows it', 'pawing the ground', 'fighting off some flies with its tail', 'lazily looking around', 'drinking from the lake'])
    menu:
        '{color=#f6d6bd}[horsename]{/color} is [foggylake_horsename_fluff].
        '
        'I enter the tavern.':
            jump foggylakeinside01
        'I approach the foragers.' ( condition="(quarters < (world_daylength-4) and quest_asterion == 1 and quest_gatheracrew == 1 and not asterion_found and not foragers_about_gatherthecrew_tzvi_recruited and not foragers_about_gatherthecrew_rejected) or (quarters < (world_daylength-4) and quest_missinghunters == 1 and not foragers_about_missinghunters) or (quarters < (world_daylength-4) and oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_knowledge and not foragers_about_traps) or (quarters < (world_daylength-4) and not foragers_quest and not day > foragingground_quest_timer and not foragingground_bird_gone) or (quarters < (world_daylength-4) and quest_birdhunting == 1) or (quarters < (world_daylength-4) and foragers_caius_heardabout and not foragers_caius_spokento) or (quarters < (world_daylength-4) and foggy_about_militarycamp and not foragers_caius_heardabout and not foragers_caius_aboutvision) or (quarters < (world_daylength-4) and foragers_caius_heardabout and foragers_caius_spokento and not foragers_caius_aboutvision) or (quarters < (world_daylength-4) and not foragers_about_travelers) or (quarters < (world_daylength-4) and not foragers_about_rumors) or (quarters < (world_daylength-4) and ruinedshelter_mushrooms and not foggy_about_mushroomsinruinedshelter and not foragers_about_mushrooms) or (quarters < (world_daylength-4) and not quest_recruitahunter_spokento_foragers and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed)" ):
            jump foggylakeforagers01
        'I have nothing to say to the foragers. (disabled)' ( condition="not (quest_asterion == 1 and quest_gatheracrew == 1 and not asterion_found and not foragers_about_gatherthecrew_tzvi_recruited and not foragers_about_gatherthecrew_rejected) and not (quest_missinghunters == 1 and not foragers_about_missinghunters) and not (oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_knowledge and not foragers_about_traps) and not (not foragers_quest and not day > foragingground_quest_timer and not foragingground_bird_gone) and not (quest_birdhunting == 1) and not (foragers_caius_heardabout and not foragers_caius_spokento) and not (foggy_about_militarycamp and not foragers_caius_heardabout and not foragers_caius_aboutvision) and not (foragers_caius_heardabout and foragers_caius_spokento and not foragers_caius_aboutvision) and not (not foragers_about_travelers) and not (not foragers_about_rumors) and not (ruinedshelter_mushrooms and not foggy_about_mushroomsinruinedshelter and not foragers_about_mushrooms) and not (not quest_recruitahunter_spokento_foragers and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed)" ):
            pass
        'The foragers are preparing for the night. (disabled)' ( condition="(quarters >= (world_daylength-4) and quest_asterion == 1 and quest_gatheracrew == 1 and not asterion_found and not foragers_about_gatherthecrew_tzvi_recruited and not foragers_about_gatherthecrew_rejected) or (quarters >= (world_daylength-4) and quest_missinghunters == 1 and not foragers_about_missinghunters) or (quarters >= (world_daylength-4) and oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_knowledge and not foragers_about_traps) or (quarters >= (world_daylength-4) and not foragers_quest and not day > foragingground_quest_timer and not foragingground_bird_gone) or (quarters >= (world_daylength-4) and quest_birdhunting == 1) or (quarters >= (world_daylength-4) and foragers_caius_heardabout and not foragers_caius_spokento) or (quarters >= (world_daylength-4) and foggy_about_militarycamp and not foragers_caius_heardabout and not foragers_caius_aboutvision) or (quarters >= (world_daylength-4) and foragers_caius_heardabout and foragers_caius_spokento and not foragers_caius_aboutvision) or (quarters >= (world_daylength-4) and not foragers_about_travelers) or (quarters >= (world_daylength-4) and not foragers_about_rumors) or (quarters >= (world_daylength-4) and ruinedshelter_mushrooms and not foggy_about_mushroomsinruinedshelter and not foragers_about_mushrooms) or (quarters >= (world_daylength-4) and not quest_recruitahunter_spokento_foragers and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed)" ):
            pass
        'I could wash myself in the lake.' if not foggylake_bath:
            jump foggylakelake01

label foggylakeafterforagers01: # odejście od foragerów
    $ renpy.force_autosave(take_screenshot=True, block=True)
    $ can_leave = 1
    if foggy_about_shelter == 1:
        $ can_rest = 1
    else:
        $ can_rest = 0
    $ can_items = 1
    $ foggylake_horsename_fluff = ""
    $ foggylake_horsename_fluff = renpy.random.choice(['enjoying some fresh grass', 'napping', 'observing the movement on the lake', 'around slowly moving, as far as its cord allows it', 'pawing the ground', 'fighting off some flies with its tail', 'lazily looking around', 'drinking from the lake'])
    menu:
        'You’re in the middle of the yard. {color=#f6d6bd}[horsename]{/color} is [foggylake_horsename_fluff].
        '
        'I enter the tavern.':
            jump foggylakeinside01
        'I approach the foragers.' ( condition="(quarters < (world_daylength-4) and quest_asterion == 1 and quest_gatheracrew == 1 and not asterion_found and not foragers_about_gatherthecrew_tzvi_recruited and not foragers_about_gatherthecrew_rejected) or (quarters < (world_daylength-4) and quest_missinghunters == 1 and not foragers_about_missinghunters) or (quarters < (world_daylength-4) and oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_knowledge and not foragers_about_traps) or (quarters < (world_daylength-4) and not foragers_quest and not day > foragingground_quest_timer and not foragingground_bird_gone) or (quarters < (world_daylength-4) and quest_birdhunting == 1) or (quarters < (world_daylength-4) and foragers_caius_heardabout and not foragers_caius_spokento) or (quarters < (world_daylength-4) and foggy_about_militarycamp and not foragers_caius_heardabout and not foragers_caius_aboutvision) or (quarters < (world_daylength-4) and foragers_caius_heardabout and foragers_caius_spokento and not foragers_caius_aboutvision) or (quarters < (world_daylength-4) and not foragers_about_travelers) or (quarters < (world_daylength-4) and not foragers_about_rumors) or (quarters < (world_daylength-4) and ruinedshelter_mushrooms and not foggy_about_mushroomsinruinedshelter and not foragers_about_mushrooms) or (quarters < (world_daylength-4) and not quest_recruitahunter_spokento_foragers and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed)" ):
            jump foggylakeforagers01
        'I have nothing to say to the foragers. (disabled)' ( condition="not (quest_asterion == 1 and quest_gatheracrew == 1 and not asterion_found and not foragers_about_gatherthecrew_tzvi_recruited and not foragers_about_gatherthecrew_rejected) and not (quest_missinghunters == 1 and not foragers_about_missinghunters) and not (oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_knowledge and not foragers_about_traps) and not (not foragers_quest and not day > foragingground_quest_timer and not foragingground_bird_gone) and not (quest_birdhunting == 1) and not (foragers_caius_heardabout and not foragers_caius_spokento) and not (foggy_about_militarycamp and not foragers_caius_heardabout and not foragers_caius_aboutvision) and not (foragers_caius_heardabout and foragers_caius_spokento and not foragers_caius_aboutvision) and not (not foragers_about_travelers) and not (not foragers_about_rumors) and not (ruinedshelter_mushrooms and not foggy_about_mushroomsinruinedshelter and not foragers_about_mushrooms) and not (not quest_recruitahunter_spokento_foragers and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed)" ):
            pass
        'The foragers are preparing for the night. (disabled)' ( condition="(quarters >= (world_daylength-4) and quest_asterion == 1 and quest_gatheracrew == 1 and not asterion_found and not foragers_about_gatherthecrew_tzvi_recruited and not foragers_about_gatherthecrew_rejected) or (quarters >= (world_daylength-4) and quest_missinghunters == 1 and not foragers_about_missinghunters) or (quarters >= (world_daylength-4) and oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_knowledge and not foragers_about_traps) or (quarters >= (world_daylength-4) and not foragers_quest and not day > foragingground_quest_timer and not foragingground_bird_gone) or (quarters >= (world_daylength-4) and quest_birdhunting == 1) or (quarters >= (world_daylength-4) and foragers_caius_heardabout and not foragers_caius_spokento) or (quarters >= (world_daylength-4) and foggy_about_militarycamp and not foragers_caius_heardabout and not foragers_caius_aboutvision) or (quarters >= (world_daylength-4) and foragers_caius_heardabout and foragers_caius_spokento and not foragers_caius_aboutvision) or (quarters >= (world_daylength-4) and not foragers_about_travelers) or (quarters >= (world_daylength-4) and not foragers_about_rumors) or (quarters >= (world_daylength-4) and ruinedshelter_mushrooms and not foggy_about_mushroomsinruinedshelter and not foragers_about_mushrooms) or (quarters >= (world_daylength-4) and not quest_recruitahunter_spokento_foragers and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed)" ):
            pass
        'I could wash myself in the lake.' if not foggylake_bath:
            jump foggylakelake01

label foggylakegroundflooraftersleep:
    label foggy_food_mealloop2:
        $ foggylake_inside_lastvisit = 1
        $ foggy_food_meal = ""
        $ foggy_food_meal = renpy.random.choice(['a bowl of simple gruel, two roasted bird thighs, and a mug of acorn brew', 'a bowl of berries, two fresh, though cold, roasted perches and a cup of chamomile tisane', 'old rye bread, a fistful of nuts, a roasted rat, and a mug of acorn brew', 'old, toasted acorn bread, a large slice of mouflon cheese, and a piece of roasted pike', 'a nettle tisane and a simple root stew with plenty of meat in it', 'a slice of roasted trout, a boiled egg, and a bowl of broad beans', 'a bowl of flat gruel, another bowl with fish soup, and a soft-boiled egg', 'some monster meat you can’t identify, a couple of apples, and a cup of birch sap', 'a baked, cold pheasant and a raw eggplant', 'roasted badger meat with mushroom sauce and a bowl of simple cabbage soup', 'boar offals, a couple of carrots, and a refreshingly cold cup of water', 'a large mug of cold mint tisane and a bit stale scraps of roasted squirrel', 'two bowls, one with roasted ants and crickets and one with a warm stew'])
        if foggy_food_mealold == foggy_food_meal:
            jump foggy_food_mealloop2
        else:
            $ foggy_food_mealold = foggy_food_meal
    show areapicture foggylakeinside01 at basicfade
    $ renpy.music.play("audio/track_02foggylake.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    nvl clear
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    $ can_leave = 0
    if foggy_about_shelter == 1:
        $ can_rest = 1
    else:
        $ can_rest = 0
    $ can_items = 1
    if day == 6 or day == 12 or day == 18 or day == 24 or day == 30 or day == 36 or day == 42:
        $ renpy.notify("The days are getting shorter.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}The days are getting shorter.{/i}')
    if foggylake_alchemytable_firsttime:
        menu:
            'It’s an exhausting night. {color=#f6d6bd}[horsename]{/color} keeps stepping in place or walking, taking only short naps. You can’t count how many times you try to calm it down, with your voice, touch, and by offering it water or a snack, but nothing helps.
            \n\nYou close your eyes for an hour or so in the late morning, then clean up after your mount. The stench alone is disarming.
            '
            'I approach {color=#f6d6bd}Foggy{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach {color=#f6d6bd}Foggy{/color}.')
                $ questionpreset = "foggy1"
                if foggy_friendship < 0:
                    $ custom2 = "She looks at you in silence."
                elif foggy_friendship < 5:
                    $ custom2 = "She turns toward you and waits for you to speak."
                elif foggy_friendship < 10:
                    $ custom2 = "She smiles at you."
                else:
                    $ custom2 = "She smiles at you. “Something else?”"
                $ can_leave = 0
                if foggy_about_shelter == 1:
                    $ can_rest = 1
                $ can_items = 0
                menu:
                    '[custom2]
                    '
                    '(preset foggy1)':
                        pass
            '{image=cointest} I go downstairs, to {color=#f6d6bd}the alchemy set{/color}.' ( condition="(quarters < world_daylength and foggylake_alchemytable_firsttime and pc_hp) or (quarters >= world_daylength and foggylake_alchemytable_firsttime and pc_hp and alchemytable_timer < day)" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} I go downstairs, to {color=#f6d6bd}the alchemy set{/color}.')
                jump foggylakealchemytable01
            'I’m too exhausted to brew potions. (Required vitality: 1) (disabled)' ( condition="foggylake_alchemytable_firsttime and not pc_hp" ):
                pass
            'It’s already late, and my eyes hurt after the last potion I brewed. (disabled)' if foggylake_alchemytable_firsttime and alchemytable_timer >= day:
                pass
            'I go outside.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
                jump foggylakeoutside01
    else:
        $ questionpreset = "foggy1"
        $ can_leave = 0
        if foggy_about_shelter == 1:
            $ can_rest = 1
        $ can_items = 0
        if foggy_friendship < 0:
            $ custom2 = "{color=#f6d6bd}Foggy{/color} looks at you in silence."
        elif foggy_friendship < 5:
            $ custom2 = "{color=#f6d6bd}Foggy{/color} turns toward you and waits for you to speak."
        elif foggy_friendship < 10:
            $ custom2 = "{color=#f6d6bd}Foggy{/color} smiles at you."
        else:
            $ custom2 = "{color=#f6d6bd}Foggy{/color} smiles at you. “Anything else?”"
        menu:
            'It’s an exhausting night. {color=#f6d6bd}[horsename]{/color} keeps stepping in place or walking, taking only short naps. You can’t count how many times you try to calm it down, with your voice, touch, and by offering it water or a snack, but nothing helps.
            \n\nYou close your eyes for an hour or so in the late morning, then clean up after your mount. The stench alone is disarming.
            \n\n[custom2]
            '
            '(preset foggy1)':
                pass

label foggylakeatticaftersleep:
    label foggy_food_mealloop3:
        $ foggylake_inside_lastvisit = 1
        $ foggy_food_meal = ""
        $ foggy_food_meal = renpy.random.choice(['a bowl of simple gruel, two roasted bird thighs, and a mug of acorn brew', 'a bowl of berries, two fresh, though cold, roasted perches and a cup of chamomile tisane', 'old rye bread, a fistful of nuts, a roasted rat, and a mug of acorn brew', 'old, toasted acorn bread, a large slice of mouflon cheese, and a piece of roasted pike', 'a nettle tisane and a simple root stew with plenty of meat in it', 'a slice of roasted trout, a boiled egg, and a bowl of broad beans', 'a bowl of flat gruel, another bowl with fish soup, and a soft-boiled egg', 'some monster meat you can’t identify, a couple of apples, and a cup of birch sap', 'a baked, cold pheasant and a raw eggplant', 'roasted badger meat with mushroom sauce and a bowl of simple cabbage soup', 'boar offals, a couple of carrots, and a refreshingly cold cup of water', 'a large mug of cold mint tisane and a bit stale scraps of roasted squirrel', 'two bowls, one with roasted ants and crickets and one with a warm stew'])
        if foggy_food_mealold == foggy_food_meal:
            jump foggy_food_mealloop3
        else:
            $ foggy_food_mealold = foggy_food_meal
    show areapicture foggylakeinside01 at basicfade
    $ can_leave = 0
    if foggy_about_shelter == 1:
        $ can_rest = 1
    else:
        $ can_rest = 0
    $ can_items = 1
    $ renpy.music.play("audio/track_02foggylake.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    nvl clear
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    if day == 6 or day == 12 or day == 18 or day == 24 or day == 30 or day == 36 or day == 42:
        $ renpy.notify("The days are getting shorter.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}The days are getting shorter.{/i}')
    if foggylake_alchemytable_firsttime:
        menu:
            'Listening to the grunts of the annoyed {color=#f6d6bd}[horsename]{/color} makes you feel uneasy, but at least the furs covering the floor are helping you relax. You don’t even notice when it’s already morning, and while the smell coming from the lower floor is not inviting, at least it’s not you who has to take care of it.
            '
            'I approach {color=#f6d6bd}Foggy{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach {color=#f6d6bd}Foggy{/color}.')
                $ questionpreset = "foggy1"
                if foggy_friendship < 0:
                    $ custom2 = "She looks at you in silence."
                elif foggy_friendship < 5:
                    $ custom2 = "She turns toward you and waits for you to speak."
                elif foggy_friendship < 10:
                    $ custom2 = "She smiles at you."
                else:
                    $ custom2 = "She smiles at you. “Something else?”"
                $ can_leave = 0
                if foggy_about_shelter == 1:
                    $ can_rest = 1
                $ can_items = 0
                menu:
                    '[custom2]
                    '
                    '(preset foggy1)':
                        pass
            '{image=cointest} I go downstairs, to {color=#f6d6bd}the alchemy set{/color}.' ( condition="(quarters < world_daylength and foggylake_alchemytable_firsttime and pc_hp) or (quarters >= world_daylength and foggylake_alchemytable_firsttime and pc_hp and alchemytable_timer < day)" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} I go downstairs, to {color=#f6d6bd}the alchemy set{/color}.')
                jump foggylakealchemytable01
            'I’m too exhausted to brew potions. (Required vitality: 1) (disabled)' ( condition="foggylake_alchemytable_firsttime and not pc_hp" ):
                pass
            'It’s already late, and my eyes hurt after the last potion I brewed. (disabled)' if foggylake_alchemytable_firsttime and alchemytable_timer >= day:
                pass
            'I go outside.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
                jump foggylakeoutside01
    else:
        $ questionpreset = "foggy1"
        $ can_leave = 0
        if foggy_about_shelter == 1:
            $ can_rest = 1
        $ can_items = 0
        if foggy_friendship < 0:
            $ custom2 = "{color=#f6d6bd}Foggy{/color} looks at you in silence."
        elif foggy_friendship < 5:
            $ custom2 = "{color=#f6d6bd}Foggy{/color} turns toward you and waits for you to speak."
        elif foggy_friendship < 10:
            $ custom2 = "{color=#f6d6bd}Foggy{/color} smiles at you."
        else:
            $ custom2 = "{color=#f6d6bd}Foggy{/color} smiles at you. “Anything else?”"
        menu:
            'Listening to the grunts of the annoyed {color=#f6d6bd}[horsename]{/color} makes you feel uneasy, but at least the furs covering the floor are helping you relax. You don’t even notice when it’s already morning, and while the smell coming from the lower floor is not inviting, at least it’s not you who has to take care of it.
            \n\n[custom2]
            '
            '(preset foggy1)':
                pass

label foggylakeafterrelaxing01:
    nvl clear
    show areapicture foggylakeinside01 at basicfade
    $ can_leave = 0
    if foggy_about_shelter == 1:
        $ can_rest = 1
    else:
        $ can_rest = 0
    $ can_items = 1
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    if pc_relax_dayof < (day-8):
        $ pc_relax_fluff = "Turns out the rest was much more necessary than you’d expected. Your belongings are a mess, the sacks and the blanket have too many holes to count, and you spend a good hour brushing and cleaning your mount. At the end of the day, you’re still a bit tired, but at least you feel prepared."
    elif pc_relax_dayof < (day-4):
        $ pc_relax_fluff = "You were pretty busy today, but not exhaustingly so. Taking care of your mount, as well as all the patches, scratches, bandages, and the general mess among your possessions took some reorganizing, but at the end of the day your muscles are grateful for not spending hours on riding."
    elif pc_relax_dayof < (day-2):
        $ pc_relax_fluff = "It’s been a relaxing day, but free of boredom. You spent almost an hour looking after your mount, but at least it’s now clean and cheerful. You patch holes in your bundles to the soothing sounds of a late summer drizzle."
    else:
        $ pc_relax_fluff = "It’s been a lazy day. Repairing your equipment and taking care of your mount didn’t take nearly as much time as you'd expected, and you instead enjoy some refreshing water, observe your surroundings with a clear head, wander about, and stretch out. After a few hours, you feel rather bored, but at least you have an opportunity to gather your thoughts."
    label foggylake_fluff_relaxingloop:
        $ foggylake_fluff_relaxing = ""
        $ foggylake_fluff_relaxing = renpy.random.choice(['Most of the time, you are all alone with {color=#f6d6bd}Foggy{/color}, who’s busy taking care of the entire place. The foragers left to look for food.', 'The foragers and {color=#f6d6bd}Foggy{/color} spend some time chatting with you, but are mostly focused on their own daily chores.', 'At one point a small group of traders from one of the villages shows up, but they’re too busy for chit-chat.', 'Most of the time, you are all alone with {color=#f6d6bd}Foggy{/color}, who’s busy taking care of the entire place. The foragers are setting up traps and spend some time on the boat.', 'Since the tavern is in a pretty good shape, {color=#f6d6bd}Foggy{/color} spends most of her day practicing her magic, while the foragers are training with staffs.'])
        if foggylake_fluff_relaxingold == foggylake_fluff_relaxing:
            jump foggylake_fluff_relaxingloop
        else:
            $ foggylake_fluff_relaxingold = foggylake_fluff_relaxing
    if foggylake_alchemytable_firsttime:
        menu:
            '[pc_relax_fluff]
            \n\n[foggylake_fluff_relaxing]
            '
            'I approach {color=#f6d6bd}Foggy{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach {color=#f6d6bd}Foggy{/color}.')
                $ questionpreset = "foggy1"
                if foggy_friendship < 0:
                    $ custom2 = "She looks at you in silence."
                elif foggy_friendship < 5:
                    $ custom2 = "She turns toward you and waits for you to speak."
                elif foggy_friendship < 10:
                    $ custom2 = "She smiles at you."
                else:
                    $ custom2 = "She smiles at you. “Something else?”"
                $ can_leave = 0
                if foggy_about_shelter == 1:
                    $ can_rest = 1
                $ can_items = 0
                menu:
                    '[custom2]
                    '
                    '(preset foggy1)':
                        pass
            '{image=cointest} I go downstairs, to {color=#f6d6bd}the alchemy set{/color}.' ( condition="(quarters < world_daylength and foggylake_alchemytable_firsttime and pc_hp) or (quarters >= world_daylength and foggylake_alchemytable_firsttime and pc_hp and alchemytable_timer < day)" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} I go downstairs, to {color=#f6d6bd}the alchemy set{/color}.')
                jump foggylakealchemytable01
            'I’m too exhausted to brew potions. (Required vitality: 1) (disabled)' ( condition="foggylake_alchemytable_firsttime and not pc_hp" ):
                pass
            'It’s already late, and my eyes hurt after the last potion I brewed. (disabled)' if foggylake_alchemytable_firsttime and alchemytable_timer >= day:
                pass
            'I go outside.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
                jump foggylakeoutside01
    else:
        $ questionpreset = "foggy1"
        $ can_leave = 0
        if foggy_about_shelter == 1:
            $ can_rest = 1
        $ can_items = 0
        if foggy_friendship < 0:
            $ custom2 = "{color=#f6d6bd}Foggy{/color} looks at you in silence."
        elif foggy_friendship < 5:
            $ custom2 = "{color=#f6d6bd}Foggy{/color} turns toward you and waits for you to speak."
        elif foggy_friendship < 10:
            $ custom2 = "{color=#f6d6bd}Foggy{/color} smiles at you."
        else:
            $ custom2 = "{color=#f6d6bd}Foggy{/color} smiles at you. “Anything else?”"
        menu:
            '[pc_relax_fluff]
            \n\n[foggylake_fluff_relaxing]
            \n\n[custom2]
            '
            '(preset foggy1)':
                pass

label foggylakealchemytableALL:
    label foggylakealchemytable01:
        if not foggylake_alchemytable_firsttime_introduction:
            $ foggylake_alchemytable_firsttime_introduction = 1
            $ custom6 = "The table and nearby shelves contain precise tools and a decent supply of basic substances used as a base for various potions, balms, or powders, but you’ll have to compensate {color=#f6d6bd}Foggy{/color} with dragon bones for using her store.\n\nAlchemical procedures take at least a couple of hours which involve complex preparations of tools, mixing of ingredients, and maintaining the brewing process. Because of this, you have to be of a strong shell and sharp soul to make any mixture. Some of them can only be used once.\n\nWhich mixture would you like to learn more about?"
        else:
            $ custom6 = "Which mixture would you like to learn more about?"
        menu:
            '[custom6]
            '
            'The herbal bug repellent I could use at the watchtower.' if quest_explorepeninsula_description05 and not watchtower_tower_bugs_cleared and not item_bugrepellent:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The herbal bug repellent I could use at the watchtower.')
                jump foggylakealchemytablebugrepellent01
            'The ointment that could help me at the ford.' if ford_firsttime and not ford_insects_dealtwith and not item_stingointment:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The ointment that could help me at the ford.')
                jump foggylakealchemytablestingointment01
            'A healing potion.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- A healing potion.')
                jump foggylakealchemytablehealingpotion01
            'The blinding powder that could help me in combat.' if not item_blindingpowder:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- A blinding powder that could help me in combat.')
                jump foggylakealchemytabletheblindingpowder01
            'The withering dust, for removing bushes and shrubs.' if not item_witheringdust:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The withering dust, for removing bushes and shrubs.')
                jump foggylakealchemytablewitheringdust01
            'The sharpening poison that can enhance my senses in combat.' if not achievement_alchemy_sharpeningpotion:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The sharpening poison that can enhance my senses in combat.')
                jump foggylakealchemytablesharpeningpotion01
            'I already have an herbal bug repellent. (disabled)' if item_bugrepellent:
                pass
            'I don’t need another bug repellent. (disabled)' if not item_bugrepellent and achievement_alchemy_bugrepellent:
                pass
            'I already have a sting ointment. (disabled)' if item_stingointment:
                pass
            'I already have the blinding powder. (disabled)' if item_blindingpowder:
                pass
            'I already have the withering dust. (disabled)' if item_witheringdust:
                pass
            'I already made the sharpening poison. (disabled)' if achievement_alchemy_sharpeningpotion:
                pass
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump foggylakeinside01

    label foggylakealchemytablebugrepellent01:
        if foggy_friendship <= 6:
            $ custom11 = "2 food rations"
        else:
            $ custom11 = "1 food ration"
        menu:
            'You can’t make all of the bugs disappear in a day, but you know the recipe for a strong, poisonous balm with a tempting smell. It will kill most of these creatures right after consumption, while others will take pieces of it to their lairs and either eliminate their colonies, or force them to resettle. At least that’s what you’ve read.
            \n\nIt won’t help much with spiders, but the little ones aren’t dangerous anyway.
            \n\n{color=#f6d6bd}Foggy’s due:{/color} [custom11]
            \n\n{color=#f6d6bd}Preparation time:{/color} 2 hours
            '
            'I don’t have enough food rations. (disabled)' if (foggy_friendship <= 6 and item_rations < 2) or (foggy_friendship > 6 and item_rations < 1):
                pass
            'I better get to foraging, then.' if (quarters <= (world_daylength-8) and foggy_friendship <= 6 and item_rations >= 2) or (quarters <= (world_daylength-8) and foggy_friendship > 6 and item_rations):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I better get to foraging, then.')
                $ quarters += 8
                $ item_bugrepellent = 1
                $ achievement_alchemy_bugrepellent += 1
                if foggy_friendship <= 6:
                    $ item_rations -= 2
                    $ renpy.notify("You made a jar of bug repellent.\nYou lost 2 food rations.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You made a jar of bug repellent. You lost 2 food rations.{/i}')
                else:
                    $ item_rations -= 1
                    $ renpy.notify("You made a jar of bug repellent.\nYou lost a food ration.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You made a jar of bug repellent. You lost a food ration.{/i}')
                menu:
                    'You look for rue, wormwood, catmint, pale lavender, and wolf leaf, and you’re lucky to come across some clover and dill. Once you bring them all back to the table, you start with your knife and end with a mortar. It may not be a “real” alchemy, but the smell is quite something. At first harsh, pinching, then gentle and sweet. You add a drop of linseed oil, and the leaves blend into a green ointment.
                    '
                    'I wash one of the jars that are on a shelf and use it to store the balm.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash one of the jars that are on a shelf and use it to store the balm.')
                        jump foggylakeinside01
            'It’s already too dark for collecting herbs. (disabled)' if quarters > (world_daylength-8):
                pass
            'Maybe another time.':
                jump foggylakealchemytable01

    label foggylakealchemytablestingointment01:
        if foggy_friendship <= 6:
            $ custom11 = "2 food rations"
        else:
            $ custom11 = "1 food ration"
        menu:
            'The balm you know of won’t be enough to make the insects leave the water bank, but once you’ll put it on your skin, they should cease their bites. You can easily make a whole jar at once, and share it with your mount.
            \n\n{color=#f6d6bd}Foggy’s due:{/color} [custom11]
            \n\n{color=#f6d6bd}Preparation time:{/color} 1 hour
            '
            'I don’t have enough food rations. (disabled)' if (foggy_friendship <= 6 and item_rations < 2) or (foggy_friendship > 6 and item_rations < 1):
                pass
            'I better get to foraging, then.' if (quarters <= (world_daylength-4) and foggy_friendship <= 6 and item_rations >= 2) or (quarters <= (world_daylength-4) and foggy_friendship > 6 and item_rations):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I better get to foraging, then.')
                $ quarters += 4
                $ item_stingointment = 1
                $ achievement_alchemy_stingointment += 1
                if foggy_friendship <= 6:
                    $ item_rations -= 2
                    $ renpy.notify("You made a jar of sting ointment.\nYou lost 2 food rations.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You made a jar of sting ointment. You lost 2 food rations.{/i}')
                else:
                    $ item_rations -= 1
                    $ renpy.notify("You made a jar of sting ointment.\nYou lost a food ration.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You made a jar of sting ointment. You lost a food ration.{/i}')
                menu:
                    'The herbs you’re looking for, such as basil, mint, and lavender, are common around here. You wash them with care and bring them all back to the table, where you start with your knife and end with a mortar. It would feel like cooking, if it wasn’t for the smell - harsh, overwhelming, it makes you sneeze more than once. You add a drop of linseed oil, and the leaves blend into a green and blue ointment.
                    '
                    'I wash one of the jars that are on a shelf and use it to store the balm.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash one of the jars that are on a shelf and use it to store the balm.')
                        jump foggylakeinside01
            'It’s already too dark for collecting herbs. (disabled)' if quarters > (world_daylength-4):
                pass
            'Maybe another time.':
                jump foggylakealchemytable01

    label foggylakealchemytabletheblindingpowder01:
        if item_cursedsoil:
            $ custom1 = "a jar of soil touched by a curse"
        else:
            $ custom1 = "{color=#6a6a6a}a jar of soil touched by a curse{/color}"
        if item_powderedrock:
            $ custom2 = "an entire basalt rock powdered at the top of a mountain"
        else:
            $ custom2 = "{color=#6a6a6a}an entire basalt rock powdered at the top of a mountain{/color}"
        if foggy_friendship <= 6:
            $ custom11 = "3 dragon bones"
        else:
            $ custom11 = "2 dragon bones"
        menu:
            'The blinding powder doesn’t affect dry skin, but once it touches one’s eyes or tongue, it causes a painful burn. A pinch of it will blind a creature for a few minutes, while the larger doses take away one’s eyesight indefinitely. A single pouch will be enough for a couple of uses.
            \n\n{color=#f6d6bd}Foggy’s due:{/color} [custom11]
            \n\n{color=#f6d6bd}The recipe requires:{/color} [custom1], [custom2]
            \n\n{color=#f6d6bd}Preparation time:{/color} 1 hour
            '
            'I don’t have enough dragon bones. (disabled)' if (foggy_friendship <= 6 and coins < 3) or (foggy_friendship > 6 and coins < 2):
                pass
            'I make the powder.' if (item_cursedsoil and item_powderedrock and foggy_friendship <= 6 and coins >= 3) or (item_cursedsoil and item_powderedrock and foggy_friendship > 6 and coins >= 2):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make the powder.')
                $ item_blindingpowder += 1
                $ achievement_alchemy_blindingpowder += 1
                $ item_cursedsoil -= 1
                $ item_powderedrock -= 1
                $ quarters += 4
                $ alchemytable_timer = day
                if foggy_friendship <= 6:
                    $ coins -= 3
                    show screen notifyimage( "You’ve created the blinding powder.\nYou lost the cursed soil\nand the powdered basalt.\n-3", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You’ve created the blinding powder. You lost the corpse eater blood and the powdered basalt. -3 {image=cointest}{/i}')
                else:
                    $ coins -= 2
                    show screen notifyimage( "You’ve created the blinding powder.\nYou lost the cursed soil\nand the powdered basalt.\n-2", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You’ve created the blinding powder. You lost the corpse eater blood and the powdered basalt. -2 {image=cointest}{/i}')
                menu:
                    'You place a stool in a convenient spot, letting your arms rest on the table. Paying close attention, you fill a copper cauldron with an even layer of powder, then warm it up slightly. Keeping track of time with an hourglass, you move the flame to a different spot after every minute, then mark these positions in your wax tablet to avoid any mistakes.
                    \n\nFor half an hour, you heat up the tiniest speck of dust, then open the jar with soil and add it to the pot, mixing with a ladle. You keep doing so until you notice the effects of the pneuma. The entire mixture suddenly gets clay-brown, shrinks in half, and after you touch it, it’s ice-cold.
                    \n\nYou fill up a pouch and shake it around. You won’t underestimate your new weapon.
                    '
                    'I clean up everything and step away from the table.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I clean up everything and step away from the table.')
                        jump foggylakeinside01
            'I don’t have all of the ingredients. (disabled)' if not item_cursedsoil or not item_powderedrock:
                pass
            'Maybe another time.':
                jump foggylakealchemytable01

    label foggylakealchemytablehealingpotion01:
        if item_blackwoundwort:
            $ custom1 = "a bundle of black woundwort"
        else:
            $ custom1 = "{color=#6a6a6a}a bundle of black woundwort{/color}"
        if item_marshbules:
            $ custom2 = "a bunch of marshbules"
        else:
            $ custom2 = "{color=#6a6a6a}a bunch of marshbules{/color}"
        if item_shortcutherbs:
            $ custom3 = "some of the of herbs from the heart of the forest"
        else:
            $ custom3 = "{color=#6a6a6a}a collection of meadow herbs from the deep forest{/color}"
        if foggy_friendship <= 6:
            $ custom11 = "2 dragon bones"
        else:
            $ custom11 = "1 dragon bone"
        menu:
            'Healing potions may be the most desired liquid in The Dragonwoods, especially among the travelers, hunters, and fighters. The ones you’ve followed so far are capable of keeping a soul on the verge of death, though it won’t “fix” a freshly cut off limb, nor cleanse one’s shell from an illness or poison.
            \n\nIt can only be used once.
            \n\n{color=#f6d6bd}Foggy’s due:{/color} [custom11]
            \n\n{color=#f6d6bd}The first recipe requires:{/color} [custom1], [custom2]
            \n\n{color=#f6d6bd}The second recipe requires:{/color} [custom1], [custom3]. You’ll keep the rest of the herbs.
            \n\n{color=#f6d6bd}Preparation time:{/color} 3 hours
            '
            'I don’t have enough dragon bones. (disabled)' if (foggy_friendship <= 6 and coins < 2) or (foggy_friendship > 6 and coins < 1):
                pass
            'I use the first recipe.' if (item_blackwoundwort and item_marshbules and foggy_friendship <= 6 and coins >= 2) or (item_blackwoundwort and item_marshbules and foggy_friendship > 6 and coins >= 1):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I use the first recipe.')
                $ item_generichealingpotion += 1
                $ achievement_alchemy_healingpotion += 1
                $ item_blackwoundwort -= 1
                $ item_marshbules -= 1
                $ quarters += 12
                $ alchemytable_timer = day
                if foggy_friendship <= 6:
                    $ coins -= 2
                    show screen notifyimage( "You’ve brewed a healing potion.\nYou lost a bundle of woundwort\nand a bunch of marshbules.\n-2", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You’ve brewed a healing potion. You lost a bundle of woundwort\nand a bunch of marshbules. -2 {image=cointest}{/i}')
                else:
                    $ coins -= 1
                    show screen notifyimage( "You’ve brewed a healing potion.\nYou lost a bundle of woundwort\nand a bunch of marshbules.\n-1", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You’ve brewed a healing potion. You lost a bundle of woundwort\nand a bunch of marshbules. -1 {image=cointest}{/i}')
                menu:
                    'You chop and grind over two dozen of various herbs into a green pulp, making an ointment with a strong, woundworty smell, then mix it with the juice of carefully squeezed marshbules, clean of any seeds and peels. So far, so good.
                    \n\nThen you spend long, long minutes at the table, constantly keeping the liquid on the brink of boiling, every now and then lowering and raising the small cauldron that hangs above the flame of an oil lamp. The boredom bites your fingers, but you don’t even have the time to go grab some water to drink.
                    \n\nYou think of the alchemists who spend day after day repeating this procedure in their workshops. Hardly a tempting vision.
                    \n\nAt least the room is now filled with a pleasant aroma, and according to what you hear from the conversations that take place upstairs, the smell reaches the main hall as well. You pour the grass-green liquid into one of the earthenware bottles, then seal it. The potion is ready.
                    '
                    'I clean up everything and step away from the table.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I clean up everything and step away from the table.')
                        jump foggylakeinside01
            'I can’t use the first recipe. (disabled)' if not item_blackwoundwort or not item_marshbules:
                pass
            'I use the second recipe.' if (item_blackwoundwort and item_shortcutherbs and foggy_friendship <= 6 and coins >= 2) or (item_blackwoundwort and item_shortcutherbs and foggy_friendship > 6 and coins >= 1):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I use the second recipe.')
                $ item_generichealingpotion += 1
                $ achievement_alchemy_healingpotion += 1
                $ item_blackwoundwort -= 1
                $ quarters += 12
                $ alchemytable_timer = day
                if foggy_friendship <= 6:
                    $ coins -= 2
                    show screen notifyimage( "You’ve brewed a healing potion.\nYou lost a bundle of woundwort.\n-2", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You’ve brewed a healing potion. You lost a bundle of woundwort. -2 {image=cointest}{/i}')
                else:
                    $ coins -= 1
                    show screen notifyimage( "You’ve brewed a healing potion.\nYou lost a bundle of woundwort.\n-1", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You’ve brewed a healing potion. You lost a bundle of woundwort. -1 {image=cointest}{/i}')
                menu:
                    'You chop and grind over a dozen of various herbs into a green pulp, making an ointment with a strong, woundworty smell. So far, so good.
                    \n\nThen you spend long, long minutes at the table, constantly keeping the liquid on the brink of boiling, every now and then lowering and raising the small cauldron that hangs above the flame of an oil lamp. The boredom bites your fingers, but you don’t even have the time to go grab some water to drink.
                    \n\nYou think of the alchemists who spend day after day repeating this procedure in their workshops. Hardly a tempting vision.
                    \n\nAt least the room is now filled with a pleasant aroma, and according to what you hear from the conversations that take place upstairs, the smell reaches the main hall as well. You pour the grass-green liquid into one of the earthenware bottles, then seal it. The potion is ready.
                    '
                    'I clean up everything and step away from the table.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I clean up everything and step away from the table.')
                        jump foggylakeinside01
            'I can’t use the second recipe. (disabled)' if not item_blackwoundwort or not item_shortcutherbs:
                pass
            'Maybe another time.':
                jump foggylakealchemytable01

    label foggylakealchemytablewitheringdust01:
        if item_driftwood:
            $ custom1 = "a piece of flower-shaped driftwood"
        else:
            $ custom1 = "{color=#6a6a6a}a piece of flower-shaped driftwood{/color}"
        if item_bogfriend:
            $ custom2 = "a bogfriend picked in the middle of the day"
        else:
            $ custom2 = "{color=#6a6a6a}a bogfriend picked in the middle of the day{/color}"
        if foggy_friendship <= 6:
            $ custom11 = "1 dragon bone"
        else:
            $ custom11 = "1 food ration"
        menu:
            'A yellow dust that’s meant to “wither” any plant. To use it, you should spread it on the ground near the roots, then sprinkle it with water. It doesn’t take a lot of dust at once, so a single bag will be a decent supply.
            \n\n{color=#f6d6bd}Foggy’s due:{/color} [custom11]
            \n\n{color=#f6d6bd}The recipe requires:{/color} [custom1], [custom2]
            \n\n{color=#f6d6bd}Preparation time:{/color} 1 hour
            '
            'I don’t have enough dragon bones. (disabled)' if (foggy_friendship <= 6 and coins < 1) or (foggy_friendship > 6 and item_rations < 1):
                pass
            'I make the dust.' if (item_driftwood and item_bogfriend and foggy_friendship <= 6 and coins >= 1) or (item_driftwood and item_bogfriend and foggy_friendship > 6 and item_rations >= 1):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make the dust.')
                $ item_witheringdust += 1
                $ achievement_alchemy_witheringdust += 1
                $ item_driftwood -= 1
                $ item_bogfriend -= 1
                $ quarters += 4
                $ alchemytable_timer = day
                if foggy_friendship <= 6:
                    $ coins -= 1
                    show screen notifyimage( "You’ve created a bag of withering dust.\nYou lost the driftwood and the bogfriend.\n-1", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You’ve created a bag of withering dust. You lost the driftwood and the bogfriend. -1 {image=cointest}{/i}')
                else:
                    $ item_rations -= 1
                    $ renpy.notify("You’ve created a bag of withering dust.\nYou lost the driftwood and the bogfriend.\nYou lost a food ration.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You’ve created a bag of withering dust. You lost the driftwood and the bogfriend. You lost a food ration.{/i}')
                menu:
                    'You start by setting the driftwood on fire, then chop and roast the bogfriend, which for reasons unknown to you turns into a dust-like powder. You grind together the seeds of coriander, pepper, and celery and add them to the mushroom, making a pleasantly smelling mixture.
                    \n\nYou then grab one of the yellow calcites and break it into smaller pieces with a stone-ended club, then grind it to dust in a mortar, together with the seeds and dried, toxic plants that you were carrying among your own supplies. The longer it takes, the more foul the smell becomes. You chop and mash the garlic, mix it with some of the dust that fell off of the wood, add to the bowl, and allow yourself to take a short break.
                    \n\nThe pneuma fills your creation, drying it in just a few moments, then turning the entire mixture into an ash-colored dust. You make sure that your gloves are dry, then grind some more, until the smell completely disappears. You sweep everything into a leather bag, leaving not a single mote behind.
                    '
                    'I clean up everything and step away from the table.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I clean up everything and step away from the table.')
                        jump foggylakeinside01
            'I don’t have all of the ingredients. (disabled)' if not item_driftwood or not item_bogfriend:
                pass
            'Maybe another time.':
                jump foggylakealchemytable01

    label foggylakealchemytablesharpeningpotion01:
        if item_snakebait:
            $ custom1 = "a snake bait flower"
        else:
            $ custom1 = "{color=#6a6a6a}a snake bait flower{/color}"
        if item_cavemushroom:
            $ custom2 = "a cave ear mushroom"
        else:
            $ custom2 = "{color=#6a6a6a}a cave ear mushroom{/color}"
        if foggy_friendship <= 6:
            $ custom11 = "3 dragon bones"
        else:
            $ custom11 = "2 dragon bones"
        menu:
            'After consumption, it makes one’s senses quicker and alerted. It gives an edge in combat for the rest of combat, but puts a burden on the shell during nightfall. You can make three doses at once.
            \n\n{color=#f6d6bd}Foggy’s due:{/color} [custom11]
            \n\n{color=#f6d6bd}The recipe requires:{/color} [custom1], [custom2]
            \n\n{color=#f6d6bd}Preparation time:{/color} 2 hours
            '
            'I don’t have enough dragon bones. (disabled)' if (foggy_friendship <= 6 and coins < 3) or (foggy_friendship > 6 and coins < 2):
                pass
            'I make the poison.' if (item_snakebait and item_cavemushroom and foggy_friendship <= 6 and coins >= 3) or (item_snakebait and item_cavemushroom and foggy_friendship > 6 and coins >= 2):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make the dust.')
                $ item_sharpeningpotion += 3
                $ achievement_alchemy_sharpeningpotion += 1
                $ item_snakebait -= 1
                $ item_cavemushroom -= 1
                $ quarters += 8
                $ alchemytable_timer = day
                if foggy_friendship <= 6:
                    $ coins -= 3
                    show screen notifyimage( "You’ve created three doses of sharpening poison.\nYou lost the snake bait\nand the cave ear.\n-3", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You’ve created three doses of sharpening poison.\nYou lost the snake bait\nand the cave ear. -3 {image=cointest}{/i}')
                else:
                    $ coins -= 2
                    show screen notifyimage( "You’ve created three doses of sharpening poison.\nYou lost the snake bait\nand the cave ear.\n-2", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You’ve created three doses of sharpening poison.\nYou lost the snake bait\nand the cave ear. -2 {image=cointest}{/i}')
                menu:
                    'You can’t dry up the mushroom, so you cut it in cubes and fry it above a gentle flame while keeping the orange petals in the hot air. You pick the mortar and pestle and prepare various dried herbs, tearing them with your fingers. You’re almost sure that at least the sage is not essential for the recipe, but adding to the powder’s final volume will reduce the substance’s intensity, and will make the dosing easier.
                    \n\nThe pleasant smell of a dinner is followed by long minutes of chopping, smashing, and grinding. Finally, the pneuma fills your creation - the entire mixture soaks up with the intense color of the snake bait. You fill up a small, wooden box.
                    '
                    'I clean up everything and step away from the table.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I clean up everything and step away from the table.')
                        jump foggylakeinside01
            'I don’t have all of the ingredients. (disabled)' if not item_snakebait or not item_cavemushroom:
                pass
            'Maybe another time.':
                jump foggylakealchemytable01

label foggylakelake01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could wash myself in the lake.')
    $ foggylake_bath = 1
    if not foragers_firsttime:
        $ custom1 = "{color=#f6d6bd}The large forager{/color} who’s wearing leather"
    else:
        $ custom1 = "{color=#f6d6bd}Ilan{/color}"
    if not foragers_firsttime:
        $ custom2 = "{color=#f6d6bd}The man in black fur{/color}"
    else:
        $ custom2 = "{color=#f6d6bd}Tvi{/color}"
    menu:
        'You enter the bridge and move to its edge. Somewhere below you, you notice a glimmer. “Hey you! Step back, run!”
        \n\nWithout even thinking, you leap toward the yard. A long, teeth-filled mouth breaks through the water surface, splashing it in every direction. It bites the empty place where you were just standing, while the front limbs, thick, scaled, and ending with claws as large as your fingers, land on the wood. Once the saurian’s yellow eyes notice that you’re outside of its reach, it nonchalantly slides into the lake.
        \n\nYou hear laughter coming from the yard. [custom1] was running with help, but now stands with hands on his thighs, cackling without rest. [custom2], on the other hand, looks at you with worry. You see a hand kept beneath his cloak, as if he was reaching for something. “What are you doing, aye? The lake isn’t for outsiders!”
        '
        'I gasp for air and thank them for the warning. “I’ll stay away, don’t you worry.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I gasp for air and thank them for the warning. “I’ll stay away, don’t you worry.”')
            $ can_leave = 1
            if foggy_about_shelter == 1:
                $ can_rest = 1
            else:
                $ can_rest = 0
            $ can_items = 1
            $ foragers_friendship -= 1
            menu:
                'He just nods and gestures for his companion to cut it. They both move toward the gate.
                '
                'I enter the tavern.':
                    jump foggylakeinside01
                'I approach the foragers.' ( condition="(quarters < (world_daylength-4) and quest_asterion == 1 and quest_gatheracrew == 1 and not asterion_found and not foragers_about_gatherthecrew_tzvi_recruited and not foragers_about_gatherthecrew_rejected) or (quarters < (world_daylength-4) and quest_missinghunters == 1 and not foragers_about_missinghunters) or (quarters < (world_daylength-4) and oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_knowledge and not foragers_about_traps) or (quarters < (world_daylength-4) and not foragers_quest and not day > foragingground_quest_timer and not foragingground_bird_gone) or (quarters < (world_daylength-4) and quest_birdhunting == 1) or (quarters < (world_daylength-4) and foragers_caius_heardabout and not foragers_caius_spokento) or (quarters < (world_daylength-4) and foggy_about_militarycamp and not foragers_caius_heardabout and not foragers_caius_aboutvision) or (quarters < (world_daylength-4) and foragers_caius_heardabout and foragers_caius_spokento and not foragers_caius_aboutvision) or (quarters < (world_daylength-4) and not foragers_about_travelers) or (quarters < (world_daylength-4) and not foragers_about_rumors) or (quarters < (world_daylength-4) and ruinedshelter_mushrooms and not foggy_about_mushroomsinruinedshelter and not foragers_about_mushrooms) or (quarters < (world_daylength-4) and not quest_recruitahunter_spokento_foragers and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed)" ):
                    jump foggylakeforagers01
                'I have nothing to say to the foragers. (disabled)' ( condition="not (quest_asterion == 1 and quest_gatheracrew == 1 and not asterion_found and not foragers_about_gatherthecrew_tzvi_recruited and not foragers_about_gatherthecrew_rejected) and not (quest_missinghunters == 1 and not foragers_about_missinghunters) and not (oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_knowledge and not foragers_about_traps) and not (not foragers_quest and not day > foragingground_quest_timer and not foragingground_bird_gone) and not (quest_birdhunting == 1) and not (foragers_caius_heardabout and not foragers_caius_spokento) and not (foggy_about_militarycamp and not foragers_caius_heardabout and not foragers_caius_aboutvision) and not (foragers_caius_heardabout and foragers_caius_spokento and not foragers_caius_aboutvision) and not (not foragers_about_travelers) and not (not foragers_about_rumors) and not (ruinedshelter_mushrooms and not foggy_about_mushroomsinruinedshelter and not foragers_about_mushrooms) and not (not quest_recruitahunter_spokento_foragers and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed)" ):
                    pass
                'The foragers are preparing for the night. (disabled)' ( condition="(quarters >= (world_daylength-4) and quest_asterion == 1 and quest_gatheracrew == 1 and not asterion_found and not foragers_about_gatherthecrew_tzvi_recruited and not foragers_about_gatherthecrew_rejected) or (quarters >= (world_daylength-4) and quest_missinghunters == 1 and not foragers_about_missinghunters) or (quarters >= (world_daylength-4) and oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_knowledge and not foragers_about_traps) or (quarters >= (world_daylength-4) and not foragers_quest and not day > foragingground_quest_timer and not foragingground_bird_gone) or (quarters >= (world_daylength-4) and quest_birdhunting == 1) or (quarters >= (world_daylength-4) and foragers_caius_heardabout and not foragers_caius_spokento) or (quarters >= (world_daylength-4) and foggy_about_militarycamp and not foragers_caius_heardabout and not foragers_caius_aboutvision) or (quarters >= (world_daylength-4) and foragers_caius_heardabout and foragers_caius_spokento and not foragers_caius_aboutvision) or (quarters >= (world_daylength-4) and not foragers_about_travelers) or (quarters >= (world_daylength-4) and not foragers_about_rumors) or (quarters >= (world_daylength-4) and ruinedshelter_mushrooms and not foggy_about_mushroomsinruinedshelter and not foragers_about_mushrooms) or (quarters >= (world_daylength-4) and not quest_recruitahunter_spokento_foragers and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed)" ):
                    pass
                'I approach the lake.' if not foggylake_bath:
                    jump foggylakelake01
        'I raise my voice. “Maybe warn me first!”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I raise my voice. “Maybe warn me first!”')
            $ can_leave = 1
            if foggy_about_shelter == 1:
                $ can_rest = 1
            else:
                $ can_rest = 0
            $ can_items = 1
            $ foragers_friendship -= 1
            menu:
                'He adjusts his cloak so that he’s fully covered. “How could I know a {i}roadwarden{/i} can’t handle a day without a bath? D’ye need some rose water with it?” His companion stops laughing and tells his companion to get back to work. They move toward the gate.
                '
                'I enter the tavern.':
                    jump foggylakeinside01
                'I approach the foragers.' ( condition="(quarters < (world_daylength-4) and quest_asterion == 1 and quest_gatheracrew == 1 and not asterion_found and not foragers_about_gatherthecrew_tzvi_recruited and not foragers_about_gatherthecrew_rejected) or (quarters < (world_daylength-4) and quest_missinghunters == 1 and not foragers_about_missinghunters) or (quarters < (world_daylength-4) and oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_knowledge and not foragers_about_traps) or (quarters < (world_daylength-4) and not foragers_quest and not day > foragingground_quest_timer and not foragingground_bird_gone) or (quarters < (world_daylength-4) and quest_birdhunting == 1) or (quarters < (world_daylength-4) and foragers_caius_heardabout and not foragers_caius_spokento) or (quarters < (world_daylength-4) and foggy_about_militarycamp and not foragers_caius_heardabout and not foragers_caius_aboutvision) or (quarters < (world_daylength-4) and foragers_caius_heardabout and foragers_caius_spokento and not foragers_caius_aboutvision) or (quarters < (world_daylength-4) and not foragers_about_travelers) or (quarters < (world_daylength-4) and not foragers_about_rumors) or (quarters < (world_daylength-4) and ruinedshelter_mushrooms and not foggy_about_mushroomsinruinedshelter and not foragers_about_mushrooms) or (quarters < (world_daylength-4) and not quest_recruitahunter_spokento_foragers and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed)" ):
                    jump foggylakeforagers01
                'I have nothing to say to the foragers. (disabled)' ( condition="not (quest_asterion == 1 and quest_gatheracrew == 1 and not asterion_found and not foragers_about_gatherthecrew_tzvi_recruited and not foragers_about_gatherthecrew_rejected) and not (quest_missinghunters == 1 and not foragers_about_missinghunters) and not (oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_knowledge and not foragers_about_traps) and not (not foragers_quest and not day > foragingground_quest_timer and not foragingground_bird_gone) and not (quest_birdhunting == 1) and not (foragers_caius_heardabout and not foragers_caius_spokento) and not (foggy_about_militarycamp and not foragers_caius_heardabout and not foragers_caius_aboutvision) and not (foragers_caius_heardabout and foragers_caius_spokento and not foragers_caius_aboutvision) and not (not foragers_about_travelers) and not (not foragers_about_rumors) and not (ruinedshelter_mushrooms and not foggy_about_mushroomsinruinedshelter and not foragers_about_mushrooms) and not (not quest_recruitahunter_spokento_foragers and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed)" ):
                    pass
                'The foragers are preparing for the night. (disabled)' ( condition="(quarters >= (world_daylength-4) and quest_asterion == 1 and quest_gatheracrew == 1 and not asterion_found and not foragers_about_gatherthecrew_tzvi_recruited and not foragers_about_gatherthecrew_rejected) or (quarters >= (world_daylength-4) and quest_missinghunters == 1 and not foragers_about_missinghunters) or (quarters >= (world_daylength-4) and oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_knowledge and not foragers_about_traps) or (quarters >= (world_daylength-4) and not foragers_quest and not day > foragingground_quest_timer and not foragingground_bird_gone) or (quarters >= (world_daylength-4) and quest_birdhunting == 1) or (quarters >= (world_daylength-4) and foragers_caius_heardabout and not foragers_caius_spokento) or (quarters >= (world_daylength-4) and foggy_about_militarycamp and not foragers_caius_heardabout and not foragers_caius_aboutvision) or (quarters >= (world_daylength-4) and foragers_caius_heardabout and foragers_caius_spokento and not foragers_caius_aboutvision) or (quarters >= (world_daylength-4) and not foragers_about_travelers) or (quarters >= (world_daylength-4) and not foragers_about_rumors) or (quarters >= (world_daylength-4) and ruinedshelter_mushrooms and not foggy_about_mushroomsinruinedshelter and not foragers_about_mushrooms) or (quarters >= (world_daylength-4) and not quest_recruitahunter_spokento_foragers and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed)" ):
                    pass
                'I approach the lake.' if not foggylake_bath:
                    jump foggylakelake01
