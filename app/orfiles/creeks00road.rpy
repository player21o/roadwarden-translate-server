############### ROAD TO CREEKS
default creeks_road_firstreaction = 0 # aggro / cautious
default creeks_road_attitude = 0
default creeks_road_helped = 0
default creeks_road_triedtohelp = 0
default creeks_road_food_fruit = 0
default creeks_road_food_fruit_asked = 0 # 1, 2
default creeks_road_food_meat = 0
default creeks_road_food_fish = 0

label roadtocreeks01:
    show areapicture foggylaketocreeks00 at basicfade
    stop music fadeout 4.0
    play nature "audio/ambient/shortcutwoodenroad01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    nvl clear
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ creeks_traveling = 1
    menu:
        'The road east is beaten and clean, with enough space to fit two wagons side-by-side. You pass by a few plum trees, apple trees, and cherry trees, but many more stumps, likely belonging to what has been turned into {color=#f6d6bd}Foggy Lake{/color}.
        \n\nThe life in the plains is busy and loud, but so far you don’t see any lurking beasts. Judging by the many trampled parts of the meadows and the fresh food trails, the foragers search this corner of the peninsula quite often.
        '
        'They didn’t leave much behind.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- They didn’t leave much behind.')
            show areapicture foggylaketocreeks01 at basicfade
            menu:
                'You reach a shining pond at the edge of the forest. You ride beneath two trimmed trees growing on the opposite sides of the path, like columns leading to Wright’s temple. Shouts and heavy steps prepare you for trouble ahead.
                \n\nTwo shells are circling around each other. One of them is a four-legged saurian, with dark-gray skin, as long as your palfrey but only knee-high. It’s wandering left and right along the bank, hissing, repetitively sticking its split tongue out and then retracting it. The stout monster doesn’t look like a born hunter of humans, but its long tail is swinging like a whip, for now only threateningly so, but you don’t doubt that getting hit by it would likely break your bones.
                \n\nThe second one belongs to a brown-skinned man wearing leather pants, a long, brown woolen cloak, and the matching pelt of a wolf on his head and shoulders, like a haunting hood. His voice is both gentle and scared, and he’s stretching his hands in front of him, trying to make the beast stay away as if it’s a mouflon.
                \n\nA third shell is right in the middle between the other two, a creature you don’t recognize from a distance, but it is in a puddle of its own blood and isn’t moving.
                '
                'Axe in hand, I jump on the ground and rush to help.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Axe in hand, I jump on the ground and rush to help.')
                    $ creeks_road_firstreaction = "aggro"
                    $ at_activate = 1
                    $ at = 0
                    menu:
                        '{color=#f6d6bd}[horsename]{/color} charges forward, though strays a bit to the left, as if hoping that you’ll change your mind before you ride into the saurian. You allow it to do so, and land on the ground between the two enemies. The man’s voice turns into laughter, and you realize that the dead shell belongs not to a human, but to a creature covered with white fur.
                        \n\n“Don’t worry, friend! I’m trying to scare it away from the ibex!”
                        '
                        ' (disabled)' ( condition="at == 0" ):
                            pass
                        '“How can I help?”' ( condition="at == 'friendly'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='(friendly) - “How can I help?”')
                            $ efren_friendship += 1
                            $ creeks_reputation += 0
                            $ creeks_road_attitude = "friendly"
                            $ custom1 = "He grins and triumphantly raises a finger. “That’s the spirit! This ibex is {i}our{/i} destiny, friend!” He points at the beast, and as his {i}hat{/i} moves around, the loose, shaking jaw distracts you. “Say, friend, d’you have any fruit in those sacks? Throw some at it.”"
                            jump roadtocreeks02
                        '“I don’t think your ibex can be helped, kind stranger.”' ( condition="at == 'playful'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='(playful) - “I don’t think your ibex can be helped, kind stranger.”')
                            $ custom1 = "He tilts his head, then lets out a chuckle. “Nah, not mine was the kill, and I’m not a beast breeder!” He points at his {i}hat{/i}, as if it’s meant to be proof of some sort. The brown mouth resting on his forehead is quite distracting. “But there's food in the middle of the road, how can I look away? This ibex is {i}our{/i} destiny, friend!” After a short pause, he whispers. “Say, d’you have any fruit in those sacks? Throw some at it,” he points at the beast."
                            $ efren_friendship += 2
                            $ creeks_reputation += 1
                            $ creeks_road_attitude = "playful"
                            jump roadtocreeks02
                        'I frown, still raising my weapon. “Why? It would be easier to catch something by yourself.”' ( condition="at == 'distanced'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='(distanced) - I frown, still raising my weapon. “Why? It would be easier to catch something by yourself.”')
                            $ custom1 = "He shakes his head, and the wolf’s loose jaw shakes as well. “That was the plan, but when a chance lands just in front of me, how can I look away? You’re not too proud, aye? It’s not carrion,” he adjusts his {i}hat{/i} a bit, but it drops right back.“Say, friend, d’you have any fruit in those sacks? Throw some at it,” he points at the beast."
                            $ efren_friendship -= 1
                            $ creeks_reputation += 0
                            $ creeks_road_attitude = "distanced"
                            jump roadtocreeks02
                        '“Just step away. I’m not going to help you die for a scrap of meat.”' ( condition="at == 'intimidating'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='(intimidating) - “Just step away. I’m not going to help you die for a scrap of meat.”')
                            $ custom1 = "“Well, thanks a lot for that,” he takes a deep breath and looks at you, as if preparing for a harsh riposte, but then shrugs and steps away from the corpse. The constantly jumping {i}hat{/i} of his, with the loose jaw and dead eyes, makes it difficult to focus on his face. “My home is this way, in {color=#f6d6bd}Creeks{/color}. Are You coming?” Before you answer, he turns around and heads uphill.\n\nThe saurian observes him for a bit, but you can’t read anything in its eyes. Once you grab the reins and lead your mount forward, the beast doesn’t waste any time - it puts the ibex’s head into its mouth, as if it is trying to swallow the entire creature at once."
                            $ creeks_road_attitude = "intimidating"
                            $ at_activate = 0
                            $ at = 0
                            jump roadtocreeks03noteventrying # different spot
                        'I breathe out with relief. “I thought the beast killed someone.”' ( condition="at == 'vulnerable'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='(vulnerable) - I breathe out with relief. “I thought it killed someone.”')
                            $ efren_friendship -= 1
                            $ creeks_reputation += 0
                            $ creeks_road_attitude = "vulnerable"
                            $ custom1 = "He frowns and shakes his head, and the wolf’s loose jaw shakes as well. “Well, it wouldn’t be that big of a deal, aye? Monsters have to eat. And I do, too,” he points at the beast and as his {i}hat{/i} moves around, the loose, shaking jaw distracts you. “Say, friend, d’you have any fruit in those sacks? Throw some at it.”"
                            jump roadtocreeks02
                'I ride slowly, taking a closer look at the entire situation.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ride slowly, taking a closer look at the entire situation.')
                    $ creeks_road_firstreaction = "cautious"
                    $ at_activate = 1
                    $ at = 0
                    menu:
                        'You stand up in the saddle to have a better view, and realize that the corpse on the ground is but that of a white ibex. The man, who acknowledges your presence with a nod, speaks with a hint of playfulness in his voice, asking the saurian to be so nice as to stay away.
                        \n\nHe then turns toward you and points at the prey. “Friend! Lend me a hand, will you! I’m trying to seize it.”
                        \n\nAs you dismount, the saurian takes a step closer to the pond.
                        '
                        ' (disabled)' ( condition="at == 0" ):
                            pass
                        '“How can I help?”' ( condition="at == 'friendly'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='(friendly) - “How can I help?”')
                            $ efren_friendship += 1
                            $ creeks_reputation += 0
                            $ creeks_road_attitude = "friendly"
                            $ custom1 = "He grins and triumphantly raises a finger. “That’s the spirit! This ibex is {i}our{/i} destiny, friend!” He points at the beast, and as his {i}hat{/i} moves around, the loose, shaking jaw distracts you. “Say, friend, d’you have any fruit in those sacks? Throw some at it.”"
                            jump roadtocreeks02
                        '“I don’t think your ibex can be helped, kind stranger.”' ( condition="at == 'playful'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='(playful) - “I don’t think your ibex can be helped, kind stranger.”')
                            $ custom1 = "He tilts his head, then lets out a chuckle. “Nah, not mine was the kill, and I’m not a beast breeder!” He points at his {i}hat{/i}, as if it’s meant to be proof of some sort. The brown mouth resting on his forehead is quite distracting. “But there's food in the middle of the road, how can I look away? This ibex is {i}our{/i} destiny, friend!” After a short pause, he whispers. “Say, d’you have any fruit in those sacks? Throw some at it,” he points at the beast."
                            $ efren_friendship += 2
                            $ creeks_reputation += 1
                            $ creeks_road_attitude = "playful"
                            jump roadtocreeks02
                        'I frown, raising my weapon. “Why? It would be easier to catch something by yourself.”' ( condition="at == 'distanced'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='(distanced) - I frown, raising my weapon. “Why? It would be easier to catch something by yourself.”')
                            $ custom1 = "He shakes his head, and the wolf’s loose jaw shakes as well. “That was the plan, but when a chance lands just in front of me, how can I look away? You’re not too proud, aye? It’s not carrion,” he adjusts his {i}hat{/i} a bit, but it drops right back.“Say, friend, d’you have any fruit in those sacks? Throw some at it,” he points at the beast."
                            $ efren_friendship -= 1
                            $ creeks_reputation += 0
                            $ creeks_road_attitude = "distanced"
                            jump roadtocreeks02
                        '“Just step away. I’m not going to help you die for a scrap of meat.”' ( condition="at == 'intimidating'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='(intimidating) - “Just step away. I’m not going to help you die for a scrap of meat.”')
                            $ custom1 = "“Well, thanks a lot for that,” he takes a deep breath and looks at you, as if preparing for a harsh riposte, but then shrugs and steps away from the corpse. The constantly jumping {i}hat{/i} of his, with the loose jaw and dead eyes, makes it difficult to focus on his face. “My home is this way, in {color=#f6d6bd}Creeks{/color}. Are You coming?” Before you answer, he turns around and heads uphill.\n\nThe saurian observes him for a bit, but you can’t read anything in its eyes. Once you grab the reins and lead your mount forward, the beast doesn’t waste any time - it puts the ibex’s head into its mouth, as if it is trying to swallow the entire creature at once."
                            $ creeks_road_attitude = "intimidating"
                            $ at_activate = 0
                            $ at = 0
                            jump roadtocreeks03noteventrying # different spot
                        'I breathe out with relief. “I thought the beast killed someone.”' ( condition="at == 'vulnerable'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='(vulnerable) - I breathe out with relief. “I thought it killed someone.”')
                            $ efren_friendship -= 1
                            $ creeks_reputation += 0
                            $ creeks_road_attitude = "vulnerable"
                            $ custom1 = "He frowns and shakes his head, and the wolf’s loose jaw shakes as well. “Well, it wouldn’t be that big of a deal, aye? Monsters have to eat. And I do, too,” he points at the beast and as his {i}hat{/i} moves around, the loose, shaking jaw distracts you. “Say, friend, d’you have any fruit in those sacks? Throw some at it.”"
                            jump roadtocreeks02

label roadtocreeks02:
    $ at_activate = 0
    $ at = 0
    menu:
        '[custom1]
        '
        'I unpack some wild fruits.' if item_wildplants and not creeks_road_food_fruit and creeks_road_food_fruit_asked < 2:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I unpack some wild fruits.')
            $ custom1 = "You show him a sack and he eagerly nods."
            jump roadtocreeks02feedingwithfruit
        'I’ve no fruits with me. (disabled)' if item_wildplants <= 0 and not creeks_road_food_fruit and creeks_road_food_fruit_asked < 2:
            pass
        '“Why would it care about fruits? It has a whole ibex to eat.”' if not creeks_road_food_fruit and not creeks_road_food_fruit_asked:
            jump roadtocreeks02questioningfruit01
        '“There’s no way a few apples would work. Maybe a cart of them.”' if not creeks_road_food_fruit and creeks_road_food_fruit_asked == 1 and not dalit_bestiary_saurians:
            jump roadtocreeks02questioningfruit02
        '“I asked this huntress about it and I’m {i}confident{/i} this saurian is a meat eater.”' if not creeks_road_food_fruit and creeks_road_food_fruit_asked == 1 and dalit_bestiary_saurians:
            jump roadtocreeks02questioningfruit02alt
        'I grab my own trophy of a wolf. “This may satisfy it.”' if item_furlesswolftrophy and not creeks_road_food_meat:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab my own trophy of a wolf. “This may satisfy it.”')
            $ efren_friendship += 2
            $ custom1 = "Quite the prey you’ve got there"
            jump roadtocreeks02feedingwithmeat
        'I grab the dead stoat I’ve been carrying in my sacks. “Let’s barter with it.”' if item_stoat and not creeks_road_food_meat:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab the dead stoat I’ve been carrying in my sacks. “Let’s barter with it.”')
            $ efren_friendship += 1
            $ custom1 = "That could make for quite a fur"
            jump roadtocreeks02feedingwithmeat
        'I throw a raw fish at the creature.' if item_rawfishtotalnumber and not creeks_road_food_fish:
            jump roadtocreeks02feedingwithfish
        '{image=d6} I sigh and look at my weapon. “I’ll distract it, you grab the ibex and drag it away.”' if pc_hp:
            jump roadtocreeks02attack01
        'I’m too exhausted to take on a fight now. (Required vitality: 1) (disabled)' if not pc_hp:
            pass
        'I step away. “Well, I guess we’re out of luck.”' if creeks_road_food_fruit or creeks_road_food_meat or creeks_road_triedtohelp:
            jump roadtocreeks03aftertrying
        'I shrug. “This is really not worth the risk.”' if not creeks_road_food_fruit and not creeks_road_food_meat and not creeks_road_triedtohelp:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shrug. “This is really not worth the risk.”')
            $ custom1 = "“Well, not with {i}that{/i} attitude.” He takes a deep breath and raises a finger, but then steps away from the corpse. “My home is this way, in {color=#f6d6bd}Creeks{/color}. You coming?” Before you answer, he turns around and heads uphill.\n\nThe saurian observes him for a bit, but you can’t read anything in its eyes. Once you grab the reins and lead your mount forward, the beast doesn’t waste any time - it puts the ibex’s head into its mouth, as if it is trying to swallow the entire creature at once."
            jump roadtocreeks03noteventrying

label roadtocreeks02feedingwithfruit:
    $ creeks_road_food_fruit = 1
    $ highisland_yellowdotsaurian_knowsabout = 1
    $ creeks_road_triedtohelp += 1
    $ item_wildplants -= 1
    $ renpy.notify("You lost a bunch of wild plants.")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a bunch of wild plants.{/i}')
    menu:
        '[custom1] “Perfect! Go ahead, throw them!”
        \n\nYou grab apples and pears that don’t look so appetizing, and toss them toward the beast. They land just next to it, and while it walks left and right, moving its tongue in and out rapidly, it only crushes some of the fruits with its feet.
        \n\n“Maybe more would do it!” Without asking for your permission, the man grabs a few more plums, throwing them right at the beast’s head. They land, and the creature cuts the air with its tail, hissing angrily, but other than that, nothing changes.
        \n\n“Know hwat? I think the fruit eaters have those yellow dots on their backs,” he starts, but clears his throat after he meets your eyes.
        '
        'I unpack some wild fruits.' if item_wildplants and not creeks_road_food_fruit and creeks_road_food_fruit_asked < 2:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I unpack some wild fruits.')
            $ custom1 = "You show him a sack and he eagerly nods."
            jump roadtocreeks02feedingwithfruit
        'I’ve no fruits with me. (disabled)' if item_wildplants <= 0 and not creeks_road_food_fruit and creeks_road_food_fruit_asked < 2:
            pass
        '“Why would it care about fruits? It has a whole ibex to eat.”' if not creeks_road_food_fruit and not creeks_road_food_fruit_asked:
            jump roadtocreeks02questioningfruit01
        '“There’s no way a few apples would work. Maybe a cart of them.”' if not creeks_road_food_fruit and creeks_road_food_fruit_asked == 1 and not dalit_bestiary_saurians:
            jump roadtocreeks02questioningfruit02
        '“I asked this huntress about it and I’m {i}confident{/i} this saurian is a meat eater.”' if not creeks_road_food_fruit and creeks_road_food_fruit_asked == 1 and dalit_bestiary_saurians:
            jump roadtocreeks02questioningfruit02alt
        'I grab my own trophy of a wolf. “This may satisfy it.”' if item_furlesswolftrophy and not creeks_road_food_meat:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab my own trophy of a wolf. “This may satisfy it.”')
            $ efren_friendship += 2
            $ custom1 = "Quite the prey you’ve got there"
            jump roadtocreeks02feedingwithmeat
        'I grab the dead stoat I’ve been carrying in my sacks. “Let’s barter with it.”' if item_stoat and not creeks_road_food_meat:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab the dead stoat I’ve been carrying in my sacks. “Let’s barter with it.”')
            $ efren_friendship += 1
            $ custom1 = "That could make for quite a fur"
            jump roadtocreeks02feedingwithmeat
        'I throw a raw fish at the creature.' if item_rawfishtotalnumber and not creeks_road_food_fish:
            jump roadtocreeks02feedingwithfish
        '{image=d6} I sigh and look at my weapon. “I’ll distract it, you grab the ibex and drag it away.”' if pc_hp:
            jump roadtocreeks02attack01
        'I’m too exhausted to take on a fight now. (Required vitality: 1) (disabled)' if not pc_hp:
            pass
        'I step away. “Well, I guess we’re out of luck.”' if creeks_road_food_fruit or creeks_road_food_meat or creeks_road_triedtohelp:
            jump roadtocreeks03aftertrying
        'I shrug. “This is really not worth the risk.”' if not creeks_road_food_fruit and not creeks_road_food_meat and not creeks_road_triedtohelp:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shrug. “This is really not worth the risk.”')
            $ custom1 = "“Well, not with {i}that{/i} attitude.” He takes a deep breath and raises a finger, but then steps away from the corpse. “My home is this way, in {color=#f6d6bd}Creeks{/color}. You coming?” Before you answer, he turns around and heads uphill.\n\nThe saurian observes him for a bit, but you can’t read anything in its eyes. Once you grab the reins and lead your mount forward, the beast doesn’t waste any time - it puts the ibex’s head into its mouth, as if it is trying to swallow the entire creature at once."
            jump roadtocreeks03noteventrying

label roadtocreeks02questioningfruit01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why would it care about fruits? It has a whole ibex to eat.”')
    $ creeks_road_food_fruit_asked = 1
    menu:
        '“Just {i}trust{/i} me, aye,” he grumpily whispers. “It hunts only when there’s nothing better for it to pick. They live on trees, you know?”
        \n\nYou look at the saurian’s shell, wet from water in which it was sitting not so long ago. The man notices your gaze. “I’m {i}almost{/i} sure.”
        '
        'I unpack some wild fruits.' if item_wildplants and not creeks_road_food_fruit and creeks_road_food_fruit_asked < 2:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I unpack some wild fruits.')
            $ custom1 = "You show him a sack and he eagerly nods."
            jump roadtocreeks02feedingwithfruit
        'I’ve no fruits with me. (disabled)' if item_wildplants <= 0 and not creeks_road_food_fruit and creeks_road_food_fruit_asked < 2:
            pass
        '“Why would it care about fruits? It has a whole ibex to eat.”' if not creeks_road_food_fruit and not creeks_road_food_fruit_asked:
            jump roadtocreeks02questioningfruit01
        '“There’s no way a few apples would work. Maybe a cart of them.”' if not creeks_road_food_fruit and creeks_road_food_fruit_asked == 1 and not dalit_bestiary_saurians:
            jump roadtocreeks02questioningfruit02
        '“I asked this huntress about it and I’m {i}confident{/i} this saurian is a meat eater.”' if not creeks_road_food_fruit and creeks_road_food_fruit_asked == 1 and dalit_bestiary_saurians:
            jump roadtocreeks02questioningfruit02alt
        'I grab my own trophy of a wolf. “This may satisfy it.”' if item_furlesswolftrophy and not creeks_road_food_meat:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab my own trophy of a wolf. “This may satisfy it.”')
            $ efren_friendship += 2
            $ custom1 = "Quite the prey you’ve got there"
            jump roadtocreeks02feedingwithmeat
        'I grab the dead stoat I’ve been carrying in my sacks. “Let’s barter with it.”' if item_stoat and not creeks_road_food_meat:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab the dead stoat I’ve been carrying in my sacks. “Let’s barter with it.”')
            $ efren_friendship += 1
            $ custom1 = "That could make for quite a fur"
            jump roadtocreeks02feedingwithmeat
        'I throw a raw fish at the creature.' if item_rawfishtotalnumber and not creeks_road_food_fish:
            jump roadtocreeks02feedingwithfish
        '{image=d6} I sigh and look at my weapon. “I’ll distract it, you grab the ibex and drag it away.”' if pc_hp:
            jump roadtocreeks02attack01
        'I’m too exhausted to take on a fight now. (Required vitality: 1) (disabled)' if not pc_hp:
            pass
        'I step away. “Well, I guess we’re out of luck.”' if creeks_road_food_fruit or creeks_road_food_meat or creeks_road_triedtohelp:
            jump roadtocreeks03aftertrying
        'I shrug. “This is really not worth the risk.”' if not creeks_road_food_fruit and not creeks_road_food_meat and not creeks_road_triedtohelp:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shrug. “This is really not worth the risk.”')
            $ custom1 = "“Well, not with {i}that{/i} attitude.” He takes a deep breath and raises a finger, but then steps away from the corpse. “My home is this way, in {color=#f6d6bd}Creeks{/color}. You coming?” Before you answer, he turns around and heads uphill.\n\nThe saurian observes him for a bit, but you can’t read anything in its eyes. Once you grab the reins and lead your mount forward, the beast doesn’t waste any time - it puts the ibex’s head into its mouth, as if it is trying to swallow the entire creature at once."
            jump roadtocreeks03noteventrying

label roadtocreeks02questioningfruit02:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There’s no way a few apples would work. Maybe a cart of them.”')
    $ creeks_road_food_fruit_asked = 2
    $ efren_friendship -= 1
    menu:
        'He purses his lips and for a moment you expect the wolf head to follow his lead. “Hwatever.”
        '
        'I unpack some wild fruits.' if item_wildplants and not creeks_road_food_fruit and creeks_road_food_fruit_asked < 2:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I unpack some wild fruits.')
            $ custom1 = "You show him a sack and he eagerly nods."
            jump roadtocreeks02feedingwithfruit
        'I’ve no fruits with me. (disabled)' if item_wildplants <= 0 and not creeks_road_food_fruit and creeks_road_food_fruit_asked < 2:
            pass
        '“Why would it care about fruits? It has a whole ibex to eat.”' if not creeks_road_food_fruit and not creeks_road_food_fruit_asked:
            jump roadtocreeks02questioningfruit01
        '“There’s no way a few apples would work. Maybe a cart of them.”' if not creeks_road_food_fruit and creeks_road_food_fruit_asked == 1 and not dalit_bestiary_saurians:
            jump roadtocreeks02questioningfruit02
        '“I asked this huntress about it and I’m {i}confident{/i} this saurian is a meat eater.”' if not creeks_road_food_fruit and creeks_road_food_fruit_asked == 1 and dalit_bestiary_saurians:
            jump roadtocreeks02questioningfruit02alt
        'I grab my own trophy of a wolf. “This may satisfy it.”' if item_furlesswolftrophy and not creeks_road_food_meat:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab my own trophy of a wolf. “This may satisfy it.”')
            $ efren_friendship += 2
            $ custom1 = "Quite the prey you’ve got there"
            jump roadtocreeks02feedingwithmeat
        'I grab the dead stoat I’ve been carrying in my sacks. “Let’s barter with it.”' if item_stoat and not creeks_road_food_meat:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab the dead stoat I’ve been carrying in my sacks. “Let’s barter with it.”')
            $ efren_friendship += 1
            $ custom1 = "That could make for quite a fur"
            jump roadtocreeks02feedingwithmeat
        'I throw a raw fish at the creature.' if item_rawfishtotalnumber and not creeks_road_food_fish:
            jump roadtocreeks02feedingwithfish
        '{image=d6} I sigh and look at my weapon. “I’ll distract it, you grab the ibex and drag it away.”' if pc_hp:
            jump roadtocreeks02attack01
        'I’m too exhausted to take on a fight now. (Required vitality: 1) (disabled)' if not pc_hp:
            pass
        'I step away. “Well, I guess we’re out of luck.”' if creeks_road_food_fruit or creeks_road_food_meat or creeks_road_triedtohelp:
            jump roadtocreeks03aftertrying
        'I shrug. “This is really not worth the risk.”' if not creeks_road_food_fruit and not creeks_road_food_meat and not creeks_road_triedtohelp:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shrug. “This is really not worth the risk.”')
            $ custom1 = "“Well, not with {i}that{/i} attitude.” He takes a deep breath and raises a finger, but then steps away from the corpse. “My home is this way, in {color=#f6d6bd}Creeks{/color}. You coming?” Before you answer, he turns around and heads uphill.\n\nThe saurian observes him for a bit, but you can’t read anything in its eyes. Once you grab the reins and lead your mount forward, the beast doesn’t waste any time - it puts the ibex’s head into its mouth, as if it is trying to swallow the entire creature at once."
            jump roadtocreeks03noteventrying

label roadtocreeks02questioningfruit02alt:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I asked this huntress about it and I’m {i}confident{/i} this saurian is a meat eater.”')
    $ creeks_road_food_fruit_asked = 2
    $ efren_friendship += 1
    $ highisland_yellowdotsaurian_knowsabout = 1
    menu:
        'His eyes widen. “Know hwat? I think the fruit eaters have those yellow dots on their backs,” he starts, but clears his throat after he meets your eyes.
        '
        'I unpack some wild fruits.' if item_wildplants and not creeks_road_food_fruit and creeks_road_food_fruit_asked < 2:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I unpack some wild fruits.')
            $ custom1 = "You show him a sack and he eagerly nods."
            jump roadtocreeks02feedingwithfruit
        'I’ve no fruits with me. (disabled)' if item_wildplants <= 0 and not creeks_road_food_fruit and creeks_road_food_fruit_asked < 2:
            pass
        '“Why would it care about fruits? It has a whole ibex to eat.”' if not creeks_road_food_fruit and not creeks_road_food_fruit_asked:
            jump roadtocreeks02questioningfruit01
        '“There’s no way a few apples would work. Maybe a cart of them.”' if not creeks_road_food_fruit and creeks_road_food_fruit_asked == 1 and not dalit_bestiary_saurians:
            jump roadtocreeks02questioningfruit02
        '“I asked this huntress about it and I’m {i}confident{/i} this saurian is a meat eater.”' if not creeks_road_food_fruit and creeks_road_food_fruit_asked == 1 and dalit_bestiary_saurians:
            jump roadtocreeks02questioningfruit02alt
        'I grab my own trophy of a wolf. “This may satisfy it.”' if item_furlesswolftrophy and not creeks_road_food_meat:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab my own trophy of a wolf. “This may satisfy it.”')
            $ efren_friendship += 2
            $ custom1 = "Quite the prey you’ve got there"
            jump roadtocreeks02feedingwithmeat
        'I grab the dead stoat I’ve been carrying in my sacks. “Let’s barter with it.”' if item_stoat and not creeks_road_food_meat:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab the dead stoat I’ve been carrying in my sacks. “Let’s barter with it.”')
            $ efren_friendship += 1
            $ custom1 = "That could make for quite a fur"
            jump roadtocreeks02feedingwithmeat
        'I throw a raw fish at the creature.' if item_rawfishtotalnumber and not creeks_road_food_fish:
            jump roadtocreeks02feedingwithfish
        '{image=d6} I sigh and look at my weapon. “I’ll distract it, you grab the ibex and drag it away.”' if pc_hp:
            jump roadtocreeks02attack01
        'I’m too exhausted to take on a fight now. (Required vitality: 1) (disabled)' if not pc_hp:
            pass
        'I step away. “Well, I guess we’re out of luck.”' if creeks_road_food_fruit or creeks_road_food_meat or creeks_road_triedtohelp:
            jump roadtocreeks03aftertrying
        'I shrug. “This is really not worth the risk.”' if not creeks_road_food_fruit and not creeks_road_food_meat and not creeks_road_triedtohelp:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shrug. “This is really not worth the risk.”')
            $ custom1 = "“Well, not with {i}that{/i} attitude.” He takes a deep breath and raises a finger, but then steps away from the corpse. “My home is this way, in {color=#f6d6bd}Creeks{/color}. You coming?” Before you answer, he turns around and heads uphill.\n\nThe saurian observes him for a bit, but you can’t read anything in its eyes. Once you grab the reins and lead your mount forward, the beast doesn’t waste any time - it puts the ibex’s head into its mouth, as if it is trying to swallow the entire creature at once."
            jump roadtocreeks03noteventrying

label roadtocreeks02feedingwithmeat:
    $ creeks_road_food_meat = 1
    $ creeks_road_triedtohelp += 1
    menu:
        'He whistles. “[custom1]! Don’t waste it on some scraps. Take it to {color=#f6d6bd}Foggy{/color} the innkeeper!” The creature, noticing the distraction, tries to grab the ibex. The man moves forward to scare it away, then both of the shells step back, afraid to make the first move.\n\nHe wipes his forehead and whistles through his teeth. “But I’m glad you tried!”
        '
        'I unpack some wild fruits.' if item_wildplants and not creeks_road_food_fruit and creeks_road_food_fruit_asked < 2:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I unpack some wild fruits.')
            $ custom1 = "You show him a sack and he eagerly nods."
            jump roadtocreeks02feedingwithfruit
        'I’ve no fruits with me. (disabled)' if item_wildplants <= 0 and not creeks_road_food_fruit and creeks_road_food_fruit_asked < 2:
            pass
        '“Why would it care about fruits? It has a whole ibex to eat.”' if not creeks_road_food_fruit and not creeks_road_food_fruit_asked:
            jump roadtocreeks02questioningfruit01
        '“There’s no way a few apples would work. Maybe a cart of them.”' if not creeks_road_food_fruit and creeks_road_food_fruit_asked == 1 and not dalit_bestiary_saurians:
            jump roadtocreeks02questioningfruit02
        '“I asked this huntress about it and I’m {i}confident{/i} this saurian is a meat eater.”' if not creeks_road_food_fruit and creeks_road_food_fruit_asked == 1 and dalit_bestiary_saurians:
            jump roadtocreeks02questioningfruit02alt
        'I grab my own trophy of a wolf. “This may satisfy it.”' if item_furlesswolftrophy and not creeks_road_food_meat:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab my own trophy of a wolf. “This may satisfy it.”')
            $ efren_friendship += 2
            $ custom1 = "Quite the prey you’ve got there"
            jump roadtocreeks02feedingwithmeat
        'I grab the dead stoat I’ve been carrying in my sacks. “Let’s barter with it.”' if item_stoat and not creeks_road_food_meat:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab the dead stoat I’ve been carrying in my sacks. “Let’s barter with it.”')
            $ efren_friendship += 1
            $ custom1 = "That could make for quite a fur"
            jump roadtocreeks02feedingwithmeat
        'I throw a raw fish at the creature.' if item_rawfishtotalnumber and not creeks_road_food_fish:
            jump roadtocreeks02feedingwithfish
        '{image=d6} I sigh and look at my weapon. “I’ll distract it, you grab the ibex and drag it away.”' if pc_hp:
            jump roadtocreeks02attack01
        'I’m too exhausted to take on a fight now. (Required vitality: 1) (disabled)' if not pc_hp:
            pass
        'I step away. “Well, I guess we’re out of luck.”' if creeks_road_food_fruit or creeks_road_food_meat or creeks_road_triedtohelp:
            jump roadtocreeks03aftertrying
        'I shrug. “This is really not worth the risk.”' if not creeks_road_food_fruit and not creeks_road_food_meat and not creeks_road_triedtohelp:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shrug. “This is really not worth the risk.”')
            $ custom1 = "“Well, not with {i}that{/i} attitude.” He takes a deep breath and raises a finger, but then steps away from the corpse. “My home is this way, in {color=#f6d6bd}Creeks{/color}. You coming?” Before you answer, he turns around and heads uphill.\n\nThe saurian observes him for a bit, but you can’t read anything in its eyes. Once you grab the reins and lead your mount forward, the beast doesn’t waste any time - it puts the ibex’s head into its mouth, as if it is trying to swallow the entire creature at once."
            jump roadtocreeks03noteventrying

label roadtocreeks02feedingwithfish:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I throw a raw fish at the creature.')
    $ creeks_road_food_fish = 1
    $ efren_friendship += 1
    $ creeks_road_triedtohelp += 1
    $ item_rawfishtotalnumber -= 1
    $ item_rawfish_losing = 1
    $ renpy.notify("You lost a fish.")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a fish.{/i}')
    menu:
        'He and his wolf’s head nod enthusiastically. “That’s a great idea!”
        \n\nYou toss the cold creature a few feet ahead of you, making it land just in front of the beast. For a moment, it doesn’t even lean forward, instead moving its tongue in and out rapidly. After a short hiss, it cuts the air to its left and right with its tail, then dashes forward to swallow the fish whole.
        \n\nYou and the hooded man wait for a few breaths, but nothing changes. The creature tries to grab the ibex, the man moves forward to scare it away, then both of the shells step back, afraid to make the first move.
        \n\n“Are you sure it was fresh?” He turns away after you give him a harsh look.
        '
        'I unpack some wild fruits.' if item_wildplants and not creeks_road_food_fruit and creeks_road_food_fruit_asked < 2:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I unpack some wild fruits.')
            $ custom1 = "You show him a sack and he eagerly nods."
            jump roadtocreeks02feedingwithfruit
        'I’ve no fruits with me. (disabled)' if item_wildplants <= 0 and not creeks_road_food_fruit and creeks_road_food_fruit_asked < 2:
            pass
        '“Why would it care about fruits? It has a whole ibex to eat.”' if not creeks_road_food_fruit and not creeks_road_food_fruit_asked:
            jump roadtocreeks02questioningfruit01
        '“There’s no way a few apples would work. Maybe a cart of them.”' if not creeks_road_food_fruit and creeks_road_food_fruit_asked == 1 and not dalit_bestiary_saurians:
            jump roadtocreeks02questioningfruit02
        '“I asked this huntress about it and I’m {i}confident{/i} this saurian is a meat eater.”' if not creeks_road_food_fruit and creeks_road_food_fruit_asked == 1 and dalit_bestiary_saurians:
            jump roadtocreeks02questioningfruit02alt
        'I grab my own trophy of a wolf. “This may satisfy it.”' if item_furlesswolftrophy and not creeks_road_food_meat:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab my own trophy of a wolf. “This may satisfy it.”')
            $ efren_friendship += 2
            $ custom1 = "Quite the prey you’ve got there"
            jump roadtocreeks02feedingwithmeat
        'I grab the dead stoat I’ve been carrying in my sacks. “Let’s barter with it.”' if item_stoat and not creeks_road_food_meat:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab the dead stoat I’ve been carrying in my sacks. “Let’s barter with it.”')
            $ efren_friendship += 1
            $ custom1 = "That could make for quite a fur"
            jump roadtocreeks02feedingwithmeat
        'I throw a raw fish at the creature.' if item_rawfishtotalnumber and not creeks_road_food_fish:
            jump roadtocreeks02feedingwithfish
        '{image=d6} I sigh and look at my weapon. “I’ll distract it, you grab the ibex and drag it away.”' if pc_hp:
            jump roadtocreeks02attack01
        'I’m too exhausted to take on a fight now. (Required vitality: 1) (disabled)' if not pc_hp:
            pass
        'I step away. “Well, I guess we’re out of luck.”' if creeks_road_food_fruit or creeks_road_food_meat or creeks_road_triedtohelp:
            jump roadtocreeks03aftertrying
        'I shrug. “This is really not worth the risk.”' if not creeks_road_food_fruit and not creeks_road_food_meat and not creeks_road_triedtohelp:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shrug. “This is really not worth the risk.”')
            $ custom1 = "“Well, not with {i}that{/i} attitude.” He takes a deep breath and raises a finger, but then steps away from the corpse. “My home is this way, in {color=#f6d6bd}Creeks{/color}. You coming?” Before you answer, he turns around and heads uphill.\n\nThe saurian observes him for a bit, but you can’t read anything in its eyes. Once you grab the reins and lead your mount forward, the beast doesn’t waste any time - it puts the ibex’s head into its mouth, as if it is trying to swallow the entire creature at once."
            jump roadtocreeks03noteventrying

label roadtocreeks02attack01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I sigh and look at my weapon. “I’ll distract it, you grab the ibex and drag it away.”')
    $ creeks_road_triedtohelp += 1
    menu:
        'He scratches his hood and nods with approval. “You know hwat, friend? That’s an {i}excellent{/i} plan. Do so.”
        \n\nWithout another glance, he once again shouts at the beast, then dashes away from you, followed by his cape. The monster hisses and reaches forward, as if waiting to see what are you going to do.
        \n\nYou step forward, hoping to draw the monster’s attention as far away from the carcass as possible. It answers your challenge, and shortens the distance even further.
        '
        '{image=d6} I focus on avoiding its attacks.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I focus on avoiding its attacks.')
            menu:
                'How do you expect it to strike?
                '
                'I keep an eye on its tail.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I keep an eye on its tail.')
                    menu:
                        'The saurian still surprises you with the range of its attacks. It turns around while pouncing forward, and swings the tail at your chest. Thanks to all the attention you paid to its movement, you duck beneath it, then jump away. The next few sways are distant enough that you don’t have to fear them.
                        \n\n“Ha! Dumb beast,” you hear. The thief is running away with the ibex on his back, holding it by the legs while it hangs from his shoulders. You chase after him, barely able to outspeed the monster yourself as it has already lost any interest in you. Without your help with the weight of the carcass, you doubt the man could get far.
                        '
                        'I shout at {color=#f6d6bd}[horsename]{/color} to run.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shout at {color=#f6d6bd}%s{/color} to run.' %horsename)
                            $ custom1 = "“It didn’t even touch you aye? Some good dodging!” He warmly laughs. “But let’s not tempt fate!” He looks back, yells in panic, and speeds up."
                            jump roadtocreeks03aftercombat
                'I jump away when it opens its mouth.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I jump away when it opens its mouth.')
                    if armor >= 3:
                        $ armor = limit_armor(armor-1)
                        show minus1armor at armorchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                        $ custom4 = ". Your fine gambeson keeps you in one piece."
                    elif armor >= 1:
                        $ armor = limit_armor(armor-1)
                        show minus1armor at armorchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                        $ custom4 = ". Your gambeson keeps you in one piece."
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp-1)
                        show minus1hp at hpchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                        $ custom4 = ", but your gambeson was already in such bad shape that it made little difference."
                    menu:
                        'You almost don’t notice where the hit comes from. You stare at the saurian’s head, but it turns around while pouncing forward, and swings the tail at your stomach. You fly back and fall on the ground, gasping. The next few sways are distant enough that you don’t have to fear them[custom4]
                        \n\n“Ha! Dumb beast,” you hear. The thief is running away with the ibex on his back, holding it by the legs while it hangs from his shoulders. You try to ignore the pain and chase after him, barely able to outspeed the monster, which has already lost any interest in you. Without your help with the weight of the carcass, you doubt the man could get far.
                        '
                        'I shout at {color=#f6d6bd}[horsename]{/color} to run.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shout at {color=#f6d6bd}%s{/color} to run.' %horsename)
                            $ custom1 = "“Enjoy your flight?” He mocks you with laughter. “But at least you’re in one piece!” He looks back, yells in panic, and speeds up."
                            jump roadtocreeks03aftercombat
                'I jump aside when it tries to pin me to the ground.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I jump aside when it tries to pin me to the ground.')
                    if armor >= 3:
                        $ armor = limit_armor(armor-1)
                        show minus1armor at armorchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                        $ custom4 = ". Your fine gambeson keeps you in one piece."
                    elif armor >= 1:
                        $ armor = limit_armor(armor-1)
                        show minus1armor at armorchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                        $ custom4 = ". Your gambeson keeps you in one piece."
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp-1)
                        show minus1hp at hpchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                        $ custom4 = ", but your gambeson was already in such bad shape that it made little difference."
                    menu:
                        'You almost don’t notice where the hit comes from. You move away when you see its pounce, but it then turns around and swings its tail at your stomach. You fall on the ground, gasping. The next few sways are distant enough that you don’t have to fear them[custom4]
                        \n\n“Ha! Dumb beast,” you hear. The thief is running away with the ibex on his back, holding it by the legs while it hangs from his shoulders. You try to ignore the pain and chase after him, barely able to outspeed the monster, which has already lost any interest in you. Without your help with the weight of the carcass, you doubt the man could get far.
                        '
                        'I shout at {color=#f6d6bd}[horsename]{/color} to run.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shout at {color=#f6d6bd}%s{/color} to run.' %horsename)
                            $ custom1 = "“Enjoy your flight?” He mocks you with laughter. “But at least you’re in one piece!” He looks back, yells in panic, and speeds up."
                            jump roadtocreeks03aftercombat
        '{image=d6} I try to wound it.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I try to wound it.')
            menu:
                'You reach for...
                '
                '{image=d6} A spear.' if item_mountainroadspear or item_asterionspear:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} A spear.')
                    $ d100roll = 0
                    $ d100roll = renpy.random.randint(1, 100)
                    if not pc_food:
                        $ d100roll += 10
                    if pc_food == 3:
                        $ d100roll -= 10
                    if pc_food == 4:
                        $ d100roll -= 20
                    if armor == 4:
                        $ d100roll -= 5
                    if pc_class == "warrior":
                        $ d100roll -= (pc_battlecounter*2)
                    else:
                        $ d100roll -= (pc_battlecounter)
                    if d100roll > 75: # fail
                        if armor >= 3:
                            $ armor = limit_armor(armor-1)
                            show minus1armor at armorchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                            $ custom4 = ". Your fine gambeson keeps you in one piece."
                        elif armor >= 1:
                            $ armor = limit_armor(armor-1)
                            show minus1armor at armorchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                            $ custom4 = ". Your gambeson keeps you in one piece."
                        else:
                            $ pc_hp = limit_pc_hp(pc_hp-1)
                            show minus1hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                            $ custom4 = ", but your gambeson was already in such bad shape that it made little difference."
                        menu:
                            'You lunge at it and almost don’t notice where the hit comes from. The beast turns around while pouncing forward, and swings the tail at your stomach at the same time as you scratch its shoulder. You fall on the ground, gasping. The next few sways are distant enough that you don’t have to fear them[custom4]
                            \n\n“Ha! Dumb beast,” you hear. The thief is running away with the ibex on his back, holding it by the legs while it hangs from his shoulders. You try to ignore the pain and chase after him, barely able to outspeed the monster, which has already lost any interest in you. Without your help with the weight of the carcass, you doubt the man could get far.
                            '
                            'I shout at {color=#f6d6bd}[horsename]{/color} to run.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shout at {color=#f6d6bd}%s{/color} to run.' %horsename)
                                $ custom1 = "“Enjoy your flight?” He mocks you with laughter. “But at least you’re in one piece!” He looks back, yells in panic, and speeds up."
                                jump roadtocreeks03aftercombat
                    else: # success
                        $ efren_club = 1
                        menu:
                            'You lunge at it and surprise the saurian with your speed. It tries to turn around, but not before you pierce its back with your spear. You even try to step on its tail, but to no avail - hissing in pain, it simply gets up and flees into the water, disappearing beneath the surface and leaving a trail of blood behind.
                            \n\n“Ha! Dumb beast,” you hear. The thief is already next to the ibex. You wait for a bit, observing how the beast swims with ease, though it’s heading to the opposite side of the pond, instead of staying in it. “That was risky,” the man chatters. “You sure have a blade better than my garbage here.” He shows you his club, a nicely shaped plank embedded with blades made of black, glass-like obsidian. It looks more than sharp to you.
                            '
                            '“Maybe. I still wouldn’t like to be hit by it.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe. I still wouldn’t like to be hit by it.”')
                                $ custom1 = "He gives you a shining smile. “Aye, it can chop off a head,” he points at his neck, “but it’s hard to land a strong hit. Well, I’ll grab it by the legs, you by the head.”"
                                jump roadtocreeks03aftercombatalt
                            '“It’s about technique and confidence, you know.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s about technique and confidence, you know.”')
                                $ custom1 = "“Yeah, probably! I’m lucky you were around, friend,” he smiles without looking at you."
                                jump roadtocreeks03aftercombatalt
                'The crossbow.' if item_crossbow and item_crossbowquarrels:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- The crossbow.')
                    $ item_crossbowquarrels -= 1
                    $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                    $ efren_club = 1
                    menu:
                        'You jump away to reach your saddle, then grab the loaded weapon. The saurian starts chasing after you, but you have enough time to aim. A quarrel sinks into the shoulder, and, hissing in pain, the beast simply gets up and flees into the water, disappearing beneath the surface and leaving a trail of blood behind. You see no disturbances in its movements.
                        \n\n“Ha! Dumb beast,” you hear. The thief is already next to the ibex. You wait for a bit, observing how the beast swims with ease, though it’s heading to the opposite side of the pond, instead of staying in it. “That was risky,” the man chatters. “You sure can afford weapons better than my garbage here.” He shows you his club, a nicely shaped plank embedded with blades made of black, glass-like obsidian. It looks more than sharp to you.
                        '
                        '“Maybe. I still wouldn’t like to be hit by it.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe. I still wouldn’t like to be hit by it.”')
                            $ custom1 = "He gives you a shining smile. “Aye, it can chop off a head,” he points at his neck, “but it’s hard to land a strong hit. Well, I’ll grab it by the legs, you by the head.”"
                            jump roadtocreeks03aftercombatalt
                        '“It’s about technique and patience.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s about technique and patience.”')
                            $ custom1 = "“Yeah, probably! I’m lucky you were around, friend,” he smiles without looking at you."
                            jump roadtocreeks03aftercombatalt
                'I don’t have any quarrels. (disabled)' if item_crossbow and not item_crossbowquarrels:
                    pass
                '{image=d6} My axe.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} My axe.')
                    $ d100roll = 0
                    $ d100roll = renpy.random.randint(1, 100)
                    if not pc_food:
                        $ d100roll += 10
                    if pc_food == 3:
                        $ d100roll -= 10
                    if pc_food == 4:
                        $ d100roll -= 20
                    if item_golemglove:
                        $ d100roll -= 10
                    if item_axe03:
                        $ d100roll -= 20
                    if armor == 4:
                        $ d100roll -= 5
                    elif item_axe02 or item_axe02alt:
                        $ d100roll -= 10
                    if pc_class == "warrior":
                        $ d100roll -= (pc_battlecounter*2)
                    else:
                        $ d100roll -= (pc_battlecounter)
                    if d100roll > 50: # fail
                        if armor >= 3:
                            $ armor = limit_armor(armor-1)
                            show minus1armor at armorchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                            $ custom4 = ". Your fine gambeson keeps you in one piece."
                        elif armor >= 1:
                            $ armor = limit_armor(armor-1)
                            show minus1armor at armorchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                            $ custom4 = ". Your gambeson keeps you in one piece."
                        else:
                            $ pc_hp = limit_pc_hp(pc_hp-1)
                            show minus1hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                            $ custom4 = ", but your gambeson was already in such bad shape that it made little difference."
                        menu:
                            'You lunge at it and almost don’t notice where the hit comes from. The beast turns around while pouncing forward, and swings the tail at your stomach while you’re in the middle of an attack. You fall on the ground, gasping. The next few sways are distant enough that you don’t have to fear them[custom4]
                            \n\n“Ha! Dumb beast,” you hear. The thief is running away with the ibex on his back, holding it by the legs while it hangs from his shoulders. You try to ignore the pain and chase after him, barely able to outspeed the monster, which has already lost any interest in you. Without your help with the weight of the carcass, you doubt the man could get far.
                            '
                            'I shout at {color=#f6d6bd}[horsename]{/color} to run.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shout at {color=#f6d6bd}%s{/color} to run.' %horsename)
                                $ custom1 = "“Enjoy your flight?” He mocks you with laughter. “But at least you’re in one piece!” He looks back, yells in panic, and speeds up."
                                jump roadtocreeks03aftercombat
                    else: # success
                        $ efren_club = 1
                        menu:
                            'You lunge at it and surprise the saurian with your speed. It tries to turn around, but not before you cut its back with your axe. You even try to step on it, but to no avail - hissing in pain, it simply gets up and flees into the water, disappearing beneath the surface and leaving a trail of blood behind.
                            \n\n“Ha! Dumb beast,” you hear. The thief is already next to the ibex. You wait for a bit, observing how the beast swims with ease, though it’s heading to the opposite side of the pond, instead of staying in it. “That was risky,” the man chatters. “You sure have a blade better than my garbage here.” He shows you his club, a nicely shaped plank embedded with blades made of black, glass-like obsidian. It looks more than sharp to you.
                            '
                            '“Maybe. I still wouldn’t like to be hit by it.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe. I still wouldn’t like to be hit by it.”')
                                $ custom1 = "He gives you a shining smile. “Aye, it can chop off a head,” he points at his neck, “but it’s hard to land a strong hit. Well, I’ll grab it by the legs, you by the head.”"
                                jump roadtocreeks03aftercombatalt
                            '“It’s about technique and confidence, you know.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s about technique and confidence, you know.”')
                                $ custom1 = "“Yeah, probably! I’m lucky you were around, friend,” he smiles without looking at you."
                                jump roadtocreeks03aftercombatalt
                'I have nothing else. (disabled)' if not item_crossbow and not item_mountainroadspear and not item_asterionspear:
                    pass
        '{image=d6} I try to look big and scare it away with shouts and gestures.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I try to look big and scare it away with shouts and gestures.')
            $ d100roll = 0
            $ d100roll = renpy.random.randint(1, 100)
            if not pc_food:
                $ d100roll += 10
            if pc_food == 3:
                $ d100roll -= 10
            if pc_food == 4:
                $ d100roll -= 20
            $ d100roll -= (pc_hp*20)
            if d100roll > 10: # fail
                if armor >= 3:
                    $ armor = limit_armor(armor-1)
                    show minus1armor at armorchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                    $ custom4 = ". Your fine gambeson keeps you in one piece."
                elif armor >= 1:
                    $ armor = limit_armor(armor-1)
                    show minus1armor at armorchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                    $ custom4 = ". Your gambeson keeps you in one piece."
                else:
                    $ pc_hp = limit_pc_hp(pc_hp-1)
                    show minus1hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                    $ custom4 = ", but your gambeson was already in such bad shape that it made little difference."
                menu:
                    'You take a big breath, push your chest forward, and almost don’t notice where the hit comes from. The beast turns around while pouncing forward, and swings the tail at your stomach before you even make a sound. You fall on the ground, gasping. The next few sways are distant enough that you don’t have to fear them[custom4]
                    \n\n“Ha! Dumb beast,” you hear. The thief is running away with the ibex on his back, holding it by the legs while it hangs from his shoulders. You try to ignore the pain and chase after him, barely able to outspeed the monster, which has already lost any interest in you. Without your help with the weight of the carcass, you doubt the man could get far.
                    '
                    'I shout at {color=#f6d6bd}[horsename]{/color} to run.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shout at {color=#f6d6bd}%s{/color} to run.' %horsename)
                        $ custom1 = "“Enjoy your flight?” He mocks you with laughter. “But at least you’re in one piece!” He looks back, yells in panic, and speeds up."
                        jump roadtocreeks03aftercombat
            else: # success
                menu:
                    'You take a big breath, push your chest forward, raise your arms above your head, and shout. The saurian looks at you for a bit, then turns around and heads toward the pond.
                    \n\n“Ha! Dumb beast,” you hear. The thief is already next to the ibex. You wait for a bit, observing how the creature gets into the water. It swims with ease, though you notice it’s heading to the opposite side of the pond, instead of staying in it. “I don’t know,” the man chatters. “I tried to do it the same way, maybe I don’t look as scary as you.”
                    '
                    'I look at the wolf pelt on his head. “Yeah. Maybe.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at the wolf pelt on his head. “Yeah. Maybe.”')
                        $ custom1 = "“Well, I’ll grab it by the legs, you by the head,” he smiles without looking at you. “I’m lucky you were around, stranger.”"
                        jump roadtocreeks03aftercombatalt
                    '“It was probably afraid to fight two against one.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It was probably afraid to fight two against one.”')
                        $ custom1 = "He gives you a shining smile. “Yeah, probably! I’m lucky you were around, stranger.”"
                        jump roadtocreeks03aftercombatalt

label roadtocreeks03aftertrying:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away. “Well, I guess we’re out of luck.”')
    menu:
        '“Maybe you’re right.” He sighs exaggeratedly, though his voice remains cheerful. “But at least we tried! You win, o great hunter,” he makes a mocking bow toward the beast, and the brown wolf bounces on his head. He steps away from the corpse. “Well, my home is this way, in {color=#f6d6bd}Creeks{/color}. You coming?” Before you answer, he turns around and goes uphill.
        \n\nThe saurian observes him for a bit, but you can’t read anything in its eyes. Once you grab the reins and lead your mount forward, the beast doesn’t waste any time - it puts the ibex’s head into its mouth, as if it is trying to swallow the entire creature at once.
        '
        'I catch up with the man.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I catch up with the man.')
            jump roadtocreeks03aftertryingp02

label roadtocreeks03noteventrying:
    $ efren_friendship -= 1
    $ creeks_reputation -= 1
    menu:
        '[custom1]
        '
        'I catch up with the man.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I catch up with the man.')
            label roadtocreeks03aftertryingp02:
                show areapicture foggylaketocreeks01b at basicfade
                menu:
                    'You leave the pond behind and approach the woods. Even from a distance you can see a distinct trail leading between the trees. “It’s not a forest garden, but it’s not bad.” With every word, the man’s voice gets more cheerful. “It’s not that gloomy, and I haven’t seen a cat there in a year. But with no cats, there are boars there now, and as there are boars, there are also more gargoyles,” he sighs. His steps get lighter, and so he leaps forward and bows to you, showing you the tip of its furry hood. “Better not go too deep, kind traveler. There are no roads there.”
                    \n\nHis face is not much older than twenty, shaved with great care, cleaner even than among the cityfolk. While his hood and heavy cloak mask his figure, he seems well-fed and healthy.
                    '
                    '“I’m not a pathfinder. The wilderness isn’t for me.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m not a pathfinder. The wilderness isn’t for me.”')
                        menu:
                            '“It isn’t for anyone at all!” He laughs and straightens up. “But still, it’s a safer place than most. We even walk from {color=#f6d6bd}Foggy’s{/color} to our homes after dark. Not a soul has died like that in, hwat, two years?” His words are full of pride. “But we’re halfway there, friend. {color=#f6d6bd}Creeks{/color} is a gorgeous place, you know. You’ll love it.”
                            '
                            'I smile. “I’m sure I will.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “I’m sure I will.”')
                                jump roadtocreeks03noteventrying02
                            '“We’ll see. Don’t ruin the surprise.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll see. Don’t ruin the surprise.”')
                                jump roadtocreeks03noteventrying02
                    '“Well, one can never know where their path will lead them.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Well, one can never know where their path will lead them.”')
                        menu:
                            '“Aye, the spirits can be nastier than a sack of apeshit. But from all the places, I’d be glad to be led to {color=#f6d6bd}Creeks{/color}. We don’t starve, the work is hard, but there are no merchants above us. And it’s a gorgeous place, you know. You’ll love it.”
                            '
                            'I smile. “I’m sure I will.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “I’m sure I will.”')
                                jump roadtocreeks03noteventrying02
                            '“We’ll see. Don’t ruin the surprise.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll see. Don’t ruin the surprise.”')
                                jump roadtocreeks03noteventrying02

    label roadtocreeks03noteventrying02:
        stop nature fadeout 4.0
        if not renpy.music.get_playing(channel='music') == "<loop 18.6>audio/track_11creeks01loop.ogg":
            play music "<loop 18.6>audio/track_11creeks01loop.ogg" fadeout 1.0 fadein 1.0
        show areapicture foggylaketocreeks02 at basicfade
        menu:
            'The road is gentle, but the man is incapable of being silent. Every unusual tree seems to be tied to a story from his life, and he makes sure that you notice the first stream you cross on a new, solid bridge. “One of many {i}creeks{/i}, you see,” he says with untamed amusement.
            \n\nA thin gorge leads you between the mountains.
            '
            'This place is quite susceptible to bandits.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- This place is quite susceptible to bandits.')
                jump finaldestinationafterevent
            'It truly feels like an end of the realm.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It truly feels like an end of the realm.')
                jump finaldestinationafterevent

label roadtocreeks03aftercombat:
    $ pc_battlecounter += 1
    $ efren_friendship += 1
    $ creeks_reputation += 1
    $ creeks_road_helped += 1
    menu:
        'You follow the trail of blood, as well as the constantly bouncing head of a brown wolf. Once you get close, the man doesn’t mind sharing the burden with you. You now hold the creature by its head, and while running side-by-side is awkward, the weight isn’t overwhelming. Your palfrey leads the two of you up the hill.
        \n\n[custom1]
        '
        'I tell him to prepare for a fight.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell him to prepare for a fight.')
            show areapicture foggylaketocreeks01b at basicfade
            menu:
                'But the clash never comes. After another minute, the beast gives up on its pursuits, though you wouldn’t have realized if it wasn’t for {color=#f6d6bd}[horsename]{/color}, who now trots without a single care. You look back, and the saurian indeed backs down, moving to its pond slowly.
                \n\nOnce you approach the woods, you take a short break. Even from a distance you can see a distinct trail leading between the trees. “Not a garden, this forest,” the man speaks briefly, gasping from the burden, “but not too dark, and cats are but a few. Boars are there, though, and gargoyles. Better not go too deep, there are no roads there.”
                \n\nHis face is not much older than twenty, shaved with great care, cleaner even than among the cityfolk. While his hood and heavy cloak mask his figure, he seems well-fed and healthy.
                \n\n“We’re halfway there, friend. {color=#f6d6bd}Creeks{/color} is a gorgeous place, you know. You’ll love it.”
                '
                'I smile. “I’m sure I will.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “I’m sure I will.”')
                    jump roadtocreeks03aftercombat02
                '“We’ll see. Don’t ruin the surprise.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll see. Don’t ruin the surprise.”')
                    jump roadtocreeks03aftercombat02

    label roadtocreeks03aftercombatalt:
        $ pc_battlecounter += 1
        $ efren_friendship += 1
        $ creeks_reputation += 1
        $ creeks_road_helped += 1
        menu:
            '[custom1] You tell {color=#f6d6bd}[horsename]{/color} to run ahead, while the two of you carry the carcass, leaving a trail of blood behind you.
            \n\nThe road leads slightly uphill. You pass the pond and approach the woods, even from a distance seeing a distinct trail leading between the trees. “Not a garden, this forest,” the man speaks briefly, gasping from the burden, “but not too dark, and cats are but a few. Boars are there, though, and gargoyles. Better not go too deep, there are no roads there.”
            \n\nHis face is not much older than twenty, shaved with great care, cleaner even than among the cityfolk. While his hood and heavy cloak mask his figure, he seems well-fed and healthy.
            \n\n“We’re halfway there, friend. {color=#f6d6bd}Creeks{/color} is a gorgeous place, you know. You’ll love it.”
            '
            'I smile. “I’m sure I will.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “I’m sure I will.”')
                jump roadtocreeks03aftercombat02
            '“We’ll see. Don’t ruin the surprise.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ll see. Don’t ruin the surprise.”')
                jump roadtocreeks03aftercombat02

    label roadtocreeks03aftercombat02:
        stop nature fadeout 4.0
        if not renpy.music.get_playing(channel='music') == "<loop 18.6>audio/track_11creeks01loop.ogg":
            play music "<loop 18.6>audio/track_11creeks01loop.ogg" fadeout 1.0 fadein 1.0
        show areapicture foggylaketocreeks02 at basicfade
        $ quarters += 1
        menu:
            'Carrying the ibex takes a while, but the man is incapable of being silent. Every unusual tree seems to be tied to a story from his life, and he makes sure that you notice the first stream you cross on a new, solid bridge. “One of many {i}creeks{/i}, you see,” he says with untamed amusement.
            \n\nA thin gorge leads you between the mountains.
            '
            'This place is quite susceptible to bandits.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- This place is quite susceptible to bandits.')
                jump finaldestinationafterevent
            'It truly feels like an end of the realm.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It truly feels like an end of the realm.')
                jump finaldestinationafterevent
