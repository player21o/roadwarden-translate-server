default galerocks_dabate_abandonsglaucia = 0
default galerocks_dabate_loyaltoglaucia = 0

default galerocks_debate_argument_needed = 14
default galerocks_debate_arguments = 0
default galerocks_debate_noweapon = 0
default galerocks_debate_woodentoy = 0

default galerocks_debate_argument_quintusthreatened = 0
default galerocks_debate_argument_oldhavastory = 0
default galerocks_debate_argument_glauciaisallaboutrevenge = 0
default galerocks_debate_argument_peopleareafraidofher = 0
default galerocks_debate_argument_glauciawenttoofarforexbandit = 0
default galerocks_debate_argument_oldtunnelgetsmoredangerous = 0
default galerocks_debate_argument_hidingthingsfromthelocals = 0
default galerocks_debate_argument_livinginsin = 0
default galerocks_debate_argument_creekssupport = 0
default galerocks_debate_argument_howlersdellsupport = 0
default galerocks_debate_argument_stealingfromoldpagos = 0
default galerocks_debate_argument_arrow = 0

label galerocksdebate01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m ready to present my case against {color=#f6d6bd}Glaucia{/color} to the council.”')
    if not item_fancyclothes:
        $ custom1 = " and gambeson"
    else:
        $ custom1 = ""
    menu:
        '“So you say,” {color=#f6d6bd}Severina{/color} moves away from the table slowly, and, with a tired sigh, stands up, though it doesn’t make her much taller. After seeing the headwoman’s nod, the crossbowwoman leaves her weapon leaning against the chair and runs outside.
        \n\n“It will take a while before my granddaughter gathers everyone here, a few of the elders like to pretend she’s not there. I’ll pick up some berries with honey for us,” she heads upstairs, followed by the unusual creaking of the planks.
        \n\nThe perfumed guard approaches you with an awkward smile. “I won’t ask you to leave your blade in another room, but it would be {i}impolite{/i} to face the council, well,” he points at your axe[custom1]. “Like a thug.”
        '
        'I purse my lips. “My equipment is where it should be.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I purse my lips. “My equipment is where it should be.”')
            $ galerocks_debate_noweapon = 0
            jump galerocksdebate01b
        'I take a deep breath and undo my belt. “Here you go.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a deep breath and undo my belt. “Here you go.”')
            $ galerocks_debate_noweapon = 1
            label galerocksdebate01b:
                $ quarters += 4
                show areapicture galerockskeep02 at basicfade
                nvl clear
                with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
                $ pc_food = limit_pc_food(pc_food+1)
                show plus1food at foodchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 nourishment point.{/i}')
                menu:
                    'Many sweetened berries later, the room feels crowded by comparison with your regular visits, even though there’s less than two dozen people spread around the benches or sitting on the stairs. You’re told to sit down on {color=#f6d6bd}Severina’s{/color} chair, facing the entire council. For now, they’re mostly ignoring your presence, chatting about the increasing frequency of gatherings such as this one.
                    \n\n“We’re not getting any younger, darling,” says an elder introduced to you as the previous head fisher, and {color=#f6d6bd}Severina{/color} responds to him with a smile warmer than any you’ve seen from her. “That’s alright, no one here gets old quicker than I do behind this desk,” she responds, and the man chuckles.
                    \n\nYou’ve met some of them already, but the perfumed man is eager to announce every newcomer to you, dropping many names and the roles they are responsible for. Most of the elders are described to you by their past trades - artisans, overseers, fighters, and one storyteller, drawing a lot of attention with her hoarse, yet sonorous jokes. Even the faces you recognize look {i}different{/i} - wearing elegant tunics, robes, and dresses, with jewelry that for once doesn’t get in the way of their tiresome labor.
                    \n\nAside from them, there are a few younger people. The head salter, head cooper, head cook... Even though their backs are stronger, they seem more timid, not willing to interrupt the elders in their decades old conversations.
                    '
                    'I observe the door, waiting for the last soul.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I observe the door, waiting for the last soul.')
                        if galerocks_photios_firsttime:
                            $ custom1 = "{color=#f6d6bd}Photios{/color}"
                        else:
                            $ custom1 = "the head fisher"
                        menu:
                            'Gasping for air, [custom1] runs inside, still buckling his belt, explaining that there was more work to do. No one seems surprised, and one of the other artisans pats his shoulder. “Come, come, have a honeyed berry,” his predecessor invites him loudly, but {color=#f6d6bd}Severina{/color} claps her hands a few times, encouraging everyone to take a seat. She stays at the spot just next to the desk, and for the first time you notice the subtle scent of violet flowers that surrounds her. “We have rough hours ahead of us, we do,” she starts. “The roadwarden wants us to {i}reconsider{/i} the ties between our village and {color=#f6d6bd}Glaucia’s{/color} group.”
                            \n\n“It’s {i}our{/i} group, as well,” the fletcher chips in, and after the head digger scoffs, starting to respond, the headwoman claps again. “We ain’t arguing {i}right now{/i},” she runs her eyes over the crowd with a reprimand. “Over this summer, we’ve all had a chance to present our views thoroughly. Let’s allow the outsider to speak in peace, and once this is done,” she meets your eyes, “we’ll open the discussion, and move to the vote, so the officials of {color=#f6d6bd}Hovlavan{/color} may know our answer before autumn.”
                            \n\nThe puzzled looks and murmurs make you think not everyone here was aware of the scope of the topic at hand, but they don’t get much time to express their discontent. “So speak, outsider, will you?” Starts the old fisher, and the hall quiets down.
                            '
                            'I start with what I’ve already discussed with {color=#f6d6bd}Severina{/color}.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I start with what I’ve already discussed with {color=#f6d6bd}Severina{/color}.')
                                $ quarters += 1
                                $ questionpreset = "galerocksdebate"
                                menu:
                                    'You describe your search for the lost merchants, and the bandits’ willingness to act against the council’s orders. The response is mixed - some observe you with disbelief, others with anger, but the first words you hear belong to {color=#f6d6bd}Photios{/color}, the head fisher. “I’m sure they had a good reason.”
                                    \n\n“Reason or not, good or not, we need these tools, we do. And she takes them back south?” {color=#f6d6bd}Domitia{/color}, the cooper, raises her voice.
                                    \n\n“We better learn how to make iron and spices out of thin air,” adds one of the elders. “For we won’t see that caravan again.”
                                    \n\nAfter a few minutes of back-and-forth, {color=#f6d6bd}the headwoman{/color} tells you to move to the next thing, so that everyone has a broader understanding before they get bogged down by the details.
                                    '
                                    '(galerocksdebate set)':
                                        pass

label galerocks_debate_argument_ALL:
    label galerocks_debate_argument_glauciaisallaboutrevenge01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Glaucia’s{/color} priority is to take revenge on those who mistreated her, not to build a better life for herself, and even less so for {color=#f6d6bd}Gale Rocks{/color}.”')
        $ galerocks_debate_argument_glauciaisallaboutrevenge = 1
        $ galerocks_debate_arguments += 3
        menu:
            'Even though your words sound obvious to everyone, the clear connection you describe - the betrayal, the loss of one’s home, then seeing one’s family turned into undead workers - makes the locals lower their heads, or, in some cases, observe you keenly, as if some of the things you mention have always been known, but never said out loud.
            \n\n“Right. We all shed them tears after {color=#f6d6bd}Steep House{/color}, we did,” starts {color=#f6d6bd}Albus{/color}, the salt maker. “But {color=#f6d6bd}Glaucia{/color} went through nightmares no soul can witness unharmed. Can any of us say they would not do the same as she does?”
            \n\n“Ehm, if her dragon’s zeal was striking merely {color=#f6d6bd}Howler’s Dell{/color}, I’d say she has her reasons. But she’s torching all them lives in the North, and everything my friends and I tried to build,” {color=#f6d6bd}Fulvia{/color}, the blind shelter keeper, is holding {color=#f6d6bd}Severina’s{/color} hand. “Destroying our home won’t save her husband.”
            \n\nA thick silence follows.
            '
            '(galerocksdebate set)':
                pass

    label galerocks_debate_argument_stealingfromoldpagos01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The people of {color=#f6d6bd}Old Págos{/color} no longer trust you. You’ve lost a valuable ally.”')
        $ galerocks_debate_argument_stealingfromoldpagos = 1
        $ minutes += 5
        if not severina_about_galerockshelpingoldpagos2:
            $ galerocks_debate_arguments += 1
            $ custom1 = "“They call us thieves!” {color=#f6d6bd}Photios{/color}, the fisher, raises his hands in defense. “We’ve done nothing to them!”\n\nThe perfumed guard nods in agreement, giving you a challenging look. “We’ve no reason to apologize. We tried to reach out to their tribe, but they’re too proud to speak with us.”\n\nOne of the elders scoffs. “Without {color=#f6d6bd}Glaucia{/color} in the woods we would never have been accused in the first place. Now, after all them bandits got themselves killed by the cityfolk, every missing pie will be our fault.”\n\nThey argue for a few minutes, but seeing how the voices are in balance, you’re encouraged to carry on."
        else:
            $ galerocks_debate_arguments += 2
            $ custom1 = "“They call us thieves!” {color=#f6d6bd}Photios{/color}, the fisher, raises his hands in defense. “We’ve done nothing to them!”\n\nThe perfumed guard sighs, giving you a sad look. “After listening to the roadwarden I’ve no doubt {color=#f6d6bd}Glaucia{/color} is to blame. She’s a liar and a thief.”\n\nOne of the elders scoffs. “Without her in the woods we would never have been accused in the first place. Now, after all them bandits got themselves killed by the cityfolk, every missing pie will be our fault.”\n\nThey argue for a few minutes, but it seems like most people are convinced that there is only one possible thief of the statue."
        menu:
            '[custom1]
            '
            '(galerocksdebate set)':
                pass

    label galerocks_debate_argument_oldtunnelgetsmoredangerous01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Even though {color=#f6d6bd}Glaucia’s{/color} band knows only combat, they didn’t move a finger to secure the tunnel in the south. It’s no surprise to me that the wilds reclaim the roads with such ease.”')
        $ galerocks_debate_argument_oldtunnelgetsmoredangerous = 1
        if quest_easternpath_points >= 6:
            $ galerocks_debate_arguments += 2
            menu:
                '“Looking after roads is harder than it sounds, stranger,” starts the head woodcutter. “We used to send dozens of souls every season or less, clearing and cutting. That ain’t an easy task.”
                \n\nHearing that, you frown. You mention some of the deeds you are responsible for on the eastern path alone. “How is it I could do these things all by myself, while she has an entire group that’s familiar with the woods, yet does nothing?”
                \n\nThe silence is cut by the absent voice of {color=#f6d6bd}Iuno{/color}, the digger. “She wants the wilderness, she does.”
                '
                '(galerocksdebate set)':
                    pass
        else:
            $ galerocks_debate_arguments += 1
            menu:
                '“Looking after roads is harder than it sounds, stranger,” starts the head woodcutter. “We used to send dozens of souls every season or less, clearing and cutting. That ain’t an easy task.”
                \n\nHearing that, you frown, but it’s {color=#f6d6bd}Iuno{/color}, the digger, who speaks first. “She has enough of a group to do {i}some{/i} work. It would be risky, alright, but it would be a start.”
                '
                '(galerocksdebate set)':
                    pass

    label galerocks_debate_argument_arrow01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found this arrow at the place where {color=#f6d6bd}Glaucia{/color} attacked the merchants. You know it well - it was meant to kill humans, {i}especially{/i} humans. She’s ready to hurt others for her gain.”')
        $ galerocks_debate_argument_arrow = 1
        $ galerocks_debate_arguments += 2
        $ item_arrow = 0
        $ renpy.notify("You lost the arrow.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the arrow.{/i}')
        menu:
            'You raise it in front of your chest, walk around to let the elders take a look at the fletching, then place it on {color=#f6d6bd}Severina’s{/color} desk, hearing the infuriated voice of the old fisher. “And what {i}should{/i} she use? Rocks? She needs to defend herself, she does, make others know she’s to be feared!”
            \n\nThe perfumed guard speaks up. “No soul from our village would take such an arrow to merely wave it around, it ain’t like tribes know our spells. This arrow has only one purpose.”
            \n\nNo one is willing to argue with him, and after the silence is disrupted with an awkward grunt, you continue.
            '
            '(galerocksdebate set)':
                pass

    label galerocks_debate_argument_hidingthingsfromthelocals01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If you’ve no doubt your support for the bandits is justified, why do most of your people have no right to know the truth about everything that {color=#f6d6bd}Glaucia{/color} has done? She’s far from being just a {i}treasure hunter{/i}.”')
        $ galerocks_debate_argument_hidingthingsfromthelocals = 1
        $ galerocks_debate_arguments += 1
        menu:
            'One of the toothless elders chuckles. “Oh, we don’t merely hide things from them. We straight-out lie, for lying gets more {i}votes{/i},” his voice drips with disdain, but {color=#f6d6bd}Severina{/color} silences him with her stare. “More of them know than you think, outsider,” she turns her head toward you. “But don’t expect all them workers to push away their families.”
            \n\n“When I moved here as a young girl, I saw ma parents only three times before they died,” another elder looks at you reproachfully. “At least {i}I{/i} can see ma boy every season or so. En he’s ne a murderer, and I {i}will ne{/i} apologize for him to anyone.”
            \n\nA few people nod in agreement, while others observe their own boots.
            '
            '(galerocksdebate set)':
                pass

    label galerocks_debate_argument_peopleareafraidofher01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Asterion{/color} is no longer around, but he also recognized the threat presented by {color=#f6d6bd}Glaucia{/color}. People are afraid of her. {color=#f6d6bd}Eudocia{/color}, {color=#f6d6bd}%s{/color}. Trade can’t go on like this.”' %iason_name)
        $ galerocks_debate_argument_peopleareafraidofher = 1
        $ galerocks_debate_arguments += 2
        menu:
            '“Why do we care about {color=#f6d6bd}Asterion{/color}?” You look for contempt in {color=#f6d6bd}Domitia’s{/color} eyes, but her question seems to be honest, and doesn’t find a clear answer.
            \n\n“Fools are afraid of anything that doesn’t boil in their pot,” {color=#f6d6bd}Porcia{/color}, the cook, shrugs this topic off. “When {color=#f6d6bd}Glaucia{/color} and I were little lasses, she wouldn’t even break a squab’s neck.”
            \n\nA few other anecdotes follow, such as the one about her always caring for her parents, but {color=#f6d6bd}Rufina{/color} calls for them to shut it. “Don’t speak of her as if she were a child. She’s not the same. She went from a tailor to a bandit, from not even a mother to a leader. Haven’t you talked with her in the last few years? She wears a different soul now.”
            \n\nThe locals exchange looks, and none of them argue with the tailor’s statement.
            '
            '(galerocksdebate set)':
                pass

    label galerocks_debate_argument_glauciawenttoofarforexbandit01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Glaucia’s{/color} own people already see that she’s going too far. I spoke with one of them, he left her band in secret.”')
        $ galerocks_debate_argument_glauciawenttoofarforexbandit = 1
        $ galerocks_debate_arguments += 2
        menu:
            'Once you finish describing him and his perspective, the locals seem confused. “Could it be...” One of the elders starts, but {color=#f6d6bd}Severina{/color} raises her hand. “Let’s not name him at the moment. He tries to drop his past, like,” she looks at the ceiling, allowing {color=#f6d6bd}Domitia{/color} to finish. “Like a mere thug.”
            \n\n“Let’s talk about him once the outsider scats,” says the old fisher, and gives you a weird look, as if it’s meant to make you vanish.
            '
            '(galerocksdebate set)':
                pass

    label galerocks_debate_argument_quintusthreatened01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Glaucia{/color} is putting the lives of others in danger, out of fear of her.” I tell them about {color=#f6d6bd}Quintus{/color}.')
        $ galerocks_debate_argument_quintusthreatened = 1
        $ galerocks_debate_arguments += 2
        menu:
            '“She {i}threatened{/i} him?” The salter speaks with disbelief, but {color=#f6d6bd}Severina{/color} takes your claim seriously. “If we were to speak with this man sometime in the future, are you sure his testimony would not reveal you to be a liar?” Seeing your nod, an uncomfortable grumbling spreads through the crowd.
            \n\n“At least they protect the gate,” one of the elders starts, but {color=#f6d6bd}Fulvia{/color} waves it off. “They could guard the gate on their own, if they were keen to do so.” A brief quarrel is cut by the headwoman, who gestures for you to go on.
            '
            '(galerocksdebate set)':
                pass

    label galerocks_debate_argument_livinginsin01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s risky, but... “Should followers of The Wright really provide support for a group of outlaws?”')
        $ galerocks_debate_argument_livinginsin = 1
        if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship":
            if (pc_religion == "theunitedchurch" and pc_faithpoints-(achievement_animalssavedpoints/2) >= 5) or (pc_religion == "ordersoftruth" and pc_faithpoints >= 7) or (pc_religion == "fellowship" and pc_faithpoints >= 8):
                $ galerocks_debate_arguments += 2
                $ custom1 = "Suddenly, you’re met with questions “testing” your knowledge, but your own experience with Wright’s teachings is enough to help you answer them. After a brief dispute, the locals glance at the hourglasses some of them wear, but say nothing."
            elif pc_class == "scholar":
                $ galerocks_debate_arguments += 1
                $ custom1 = "Using your education, you describe the basic ideas leading The United Church, and while your tone is dry, the tension leaves the air. "
            else:
                $ custom1 = "Suddenly, you’re met with questions “testing” your knowledge, and while you can answer some basic questions, you get shut down quickly. You try to change the topic as you’re met with their heavy scowls."
                $ galerocks_debate_arguments += 0
        else:
            $ custom1 = "Suddenly, you’re met with questions “testing” your knowledge, and it’s no longer a secret that you don’t know much about Wright’s Tablets or their twisted paths. The harsh looks you receive are almost as cold as the air in the room, and you try to change the topic."
            $ galerocks_debate_arguments -= 1
        menu:
            'The perfumed guard speaks first. “Don’t go there, outsider,” he tries to sound firm, but one of the elders clamors over him. “And what do you think you know about The River of Order, {i}outsider{/i}?”
            \n\n[custom1]
            '
            '(galerocksdebate set)':
                pass

    label galerocks_debate_argument_oldhavastory01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think about {color=#f6d6bd}Old Hava{/color}. “Every bandit leader falls to their own desires, bringing only more suffering on to others.”')
        $ galerocks_debate_argument_oldhavastory = 1
        $ galerocks_debate_arguments += 2
        menu:
            'You share what you’ve learned from her, putting emphasis on what’s going to happen after {color=#f6d6bd}Glaucia’s{/color} death. {color=#f6d6bd}The head cook{/color} looks out the window, speaking with an absent voice. “Right. Hard to believe it’s been {i}ten years{/i},” she says menacingly. “She was meant to return after half that, remember? Yet she threatens others more, not less. How can we know she’ll stop, or that she won’t be replaced by... Ehm.” She doesn’t name anyone, just crosses her arms.
            \n\n“Right, so now we listen to some stories, instead of to what’s going on?” {color=#f6d6bd}The fisher{/color} scoffs, but the old storyteller addresses him gently. “No one is making any decisions yet. Let’s merely consider different views.”
            '
            '(galerocksdebate set)':
                pass

    label galerocks_debate_argument_creeksandhowlersdellsupport01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Both {color=#f6d6bd}Creeks{/color} and {color=#f6d6bd}Howler’s Dell{/color} are willing to negotiate with {color=#f6d6bd}Hovlavan{/color}. Don’t let yourselves be left behind.”')
        $ galerocks_debate_argument_creekssupport = 1
        $ galerocks_debate_argument_howlersdellsupport = 1
        $ galerocks_debate_arguments += 3
        menu:
            'The hall falls silent, and the locals stare first at you, then at {color=#f6d6bd}their headwoman{/color}. After a few moments, she turns toward them. “What is there to say? The change will come here, merely sooner than we’d expected. We were fools to think we are the ones throwing the dice.”
            '
            '(galerocksdebate set)':
                pass
        label galerocks_debate_argument_creekssupport01:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Creeks{/color} is already willing to negotiate with {color=#f6d6bd}Hovlavan{/color}. The endeavour to make the peninsula safer may be easier than you think.”')
            $ galerocks_debate_argument_creekssupport = 1
            $ galerocks_debate_arguments += 1
            menu:
                '“Something must have really grabbed their hair if those triflers are ready to grow up,” starts {color=#f6d6bd}Photios{/color} with a smirk, but the others stare at you in silence, then look at {color=#f6d6bd}their headwoman{/color}. After a few moments, she turns toward them. “What is there to say? If we are to take a place at the table, we ought to make sure it will be a good one.”
                '
                '(galerocksdebate set)':
                    pass
        label galerocks_debate_argument_howlersdellsupport01:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Howler’s Dell{/color} is already willing to negotiate with {color=#f6d6bd}Hovlavan{/color}. The endeavour to make the peninsula safer may be easier than you think.”')
            $ galerocks_debate_argument_howlersdellsupport = 1
            $ galerocks_debate_arguments += 1
            menu:
                '“{color=#f6d6bd}Thais{/color} must have some big plans, if she’s willing to loosen her grasp,” starts {color=#f6d6bd}Albus{/color}, the salter, and the wide-open eyes of the council show that they’re thinking the same. They stare at you in silence, then look at {color=#f6d6bd}their headwoman{/color}. After a few moments, she turns toward them. “What is there to say? If we are to take a place at the table, we ought to make sure it will be a good one.”
                '
                '(galerocksdebate set)':
                    pass

label severina_debatediscussion01:
    $ severina_annoyance = 8
    $ severina_annoyance_treshhold_reached = day
    $ quarters += 1
    if galerocks_debate_arguments < 2:
        $ galerocks_dabate_loyaltoglaucia = 2
        $ galerocks_reputation -= 1
        $ severina_friendship -= 1
        menu:
            '“Ehm, that’s {i}it{/i}?” {color=#f6d6bd}The old fisher{/color} stands up with spread arms. “I ain’t convinced. Do we really have to discuss this?”
            \n\n{color=#f6d6bd}Severina{/color} also gets on her feet, glancing at you with reluctance. “I do believe we can move to the vote. The outsider asked us to consider cutting our ties to {color=#f6d6bd}Glaucia’s{/color} group, and to negotiate the terms of taxing with {color=#f6d6bd}Hovlavan{/color} instead. Who’s open for that?”
            \n\nA handful of souls say “I am”, but there is no point in counting.
            \n\n“Request rejected, let’s disband and eat something.”
            '
            'I gather my belongings.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I gather my belongings.')
                $ quest_galerockssupport = 4
                $ renpy.notify("Quest completed: The Support of Gale Rocks")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Support of Gale Rocks{/i}')
                $ quest_galerockssupport_description02 = "The villagers are now convinced to take an even stronger stance on the side of the bandits. It’s going to be bad news for the city merchants."
                menu:
                    'You’re not bothered by anyone. The sparse comments you hear from the locals mention that it was unwise to even consider an outsider’s voice, and that they shouldn’t treat {color=#f6d6bd}Glaucia{/color} too harshly.
                    \n\nThe younger members of the council help the elders cross the yard, and as they engage in friendly chatter, they forget about the gathering quickly.
                    '
                    'I go down the hill.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go down the hill.')
                        jump galerocksleavingseverina01
    ##############
    if (galerocks_reputation+appearance_charisma >= 10 and not galerocks_debate_noweapon) or (galerocks_reputation+appearance_charisma >= 9 and galerocks_debate_noweapon):
        $ custom1 = "{color=#f6d6bd}Severina{/color} doesn’t look at you, but her voice is gentle. “Our neighbors see the roadwarden as a guest, not just a stranger. We have no promises to make, all we have to do is decide if we’re ready to speak with the city officials.”"
        $ galerocks_debate_arguments += 1
    elif (galerocks_reputation+appearance_charisma < 5 and not galerocks_debate_noweapon) or (galerocks_reputation+appearance_charisma < 4 and galerocks_debate_noweapon):
        $ custom1 = "{color=#f6d6bd}Severina{/color} doesn’t look at you, and her voice is harsh. “Right, the stranger has found no trust in our walls, but we have no promises to make just yet. The question is if we see a good reason to speak with the city officials, no matter what we think of the roadwarden’s actions.”"
        $ galerocks_debate_arguments -= 1
    else:
        $ custom1 = "{color=#f6d6bd}Severina{/color} doesn’t look at you, and her voice is strict. “We have no promises to make, and no trust to offer to the stranger. The question is if we see a good reason to speak with the city officials.”"
    ##############
    if galerocks_resource_barrels and galerocks_resource_fish and galerocks_resource_salt:
        $ custom2 = "“A few of our artisans have spoken with the roadwarden about our trade,” starts {color=#f6d6bd}Albus{/color}, the salter. “The city may have a reason to send their mouthpiece here after all.”"
        $ galerocks_debate_arguments += 1
    elif not galerocks_resource_barrels and not galerocks_resource_fish and not galerocks_resource_salt:
        $ custom2 = "“The artisans haven’t spoken with the roadwarden about our trade,” starts {color=#f6d6bd}Albus{/color}, the salter. “The city may see no point in sending their mouthpiece here at all.”"
        $ galerocks_debate_arguments -= 1
    else:
        $ custom2 = "“A few of our artisans have spoken with the roadwarden about our trade,” starts {color=#f6d6bd}Albus{/color}, the salter. “But the city may see no point in sending their mouthpiece here at all.”"
    ##############
    if (quest_spiritrock == 2 and galerocks_singlepeople_paulus_matched and galerocks_iuno_about_oldtunnel_explored) or (quest_spiritrock == 2 and galerocks_singlepeople_marina_notmatched and galerocks_iuno_about_oldtunnel_explored):
        $ custom3 = "{color=#f6d6bd}Porcia{/color}, the cook, mentions that from what she’s heard at her diner, you did some good for the villagers."
        $ galerocks_debate_arguments += 1
    else:
        $ custom3 = "{color=#f6d6bd}Porcia{/color}, the cook, mentions that from what she’s heard at her diner, you didn’t do much good for the villagers."
    ##############
    if quest_spiritrock == 2:
        if galerocks_phoibe_coma:
            $ custom5 = " {color=#f6d6bd}Photios{/color} admits, though resentfully, that you’ve done for him exactly what he asked of you."
            $ galerocks_debate_arguments += 1
        else:
            $ custom5 = " {color=#f6d6bd}Photios{/color} admits enthusiastically that you’ve helped him more than he expected you to."
            $ galerocks_debate_arguments += 1
    elif quest_spiritrock == 3:
        $ custom5 = " {color=#f6d6bd}Photios{/color} mentions that you refused to help him, and that you’re as “useless as that previous vagabond.”"
        $ galerocks_debate_arguments -= 1
    elif quest_spiritrock == 1:
        $ custom5 = " {color=#f6d6bd}Photios{/color} looks at you resentfully."
    else:
        $ custom5 = " {color=#f6d6bd}Photios{/color}, the fisher, mentions that he could have used your help."
    ##############
    if galerocks_singlepeople_paulus_matched and galerocks_singlepeople_marina_notmatched:
        $ custom4 = " One of the elders, {color=#f6d6bd}Paulus’{/color} grandmother, mentions the help you offered to her family."
        $ galerocks_debate_arguments += 1
    else:
        $ custom4 = ""
    ##############
    if galerocks_iuno_about_oldtunnel_explored:
        $ custom6 = " {color=#f6d6bd}Iuno{/color}, the digger, says that the day when the village may once again need to use the southern tunnel may be approaching quickly, and that thanks to your help, it won’t take as much effort."
        $ galerocks_debate_arguments += 1
    elif galerocks_iuno_about_oldtunnel_cleared:
        $ custom6 = " {color=#f6d6bd}Iuno{/color}, the digger, says that the day when the village may once again need to use the southern tunnel may be approaching quickly, and that your help shows that at least some of the cityfolk are willing to take on a hard fight."
    elif galerocks_iuno_about_oldtunnel_cleared:
        $ custom6 = " {color=#f6d6bd}Iuno{/color}, the digger, says that the day when the village may once again need to use the southern tunnel may be approaching quickly, but that you, the {i}roadwarden{/i}, didn’t help them much with this endeavour yet."
        $ galerocks_debate_arguments -= 1
    menu:
        '“Right, so we’ve listened, we did,” starts {color=#f6d6bd}the old fisher{/color}, whose posture grows more lax the longer the gathering goes. “But why do we trust what {i}the outsider{/i},” he scowls at you, “thinks of our matters?”
        \n\n[custom1]
        \n\n[custom2]
        \n\n[custom3][custom5][custom4][custom6]
        '
        'I look around, waiting for everyone to speak.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look around, waiting for everyone to speak.')
            if severina_about_plague2 and severina_about_galerockshelpingoldpagos2:
                $ galerocks_debate_woodentoy = 1
                $ custom3 = "Alright, better get to the discussion before we all fall asleep. I vote a {i}strong yes{/i}, anyway. The news the roadwarden brought to us about {color=#f6d6bd}Old Págos{/color} is enough to convince me."
                $ galerocks_debate_arguments += 2
            elif severina_about_plague2 or severina_about_galerockshelpingoldpagos2:
                $ galerocks_debate_woodentoy = 1
                $ custom3 = "Alright, better get to the discussion before we all fall asleep. I vote a {i}weak yes{/i}, anyway. The news the roadwarden brought to us about {color=#f6d6bd}Old Págos{/color} is almost enough to convince me."
                $ galerocks_debate_arguments += 1
            else:
                 $ custom3 = "Alright, better get to the discussion before we all fall asleep. I vote a {i}weak no{/i}, anyway."
            menu:
                'The perfumed man clears his throat. “[custom3] Come, [pcname],” he nods at you and heads toward the exit.”
                '
                'We leave the hall.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- We leave the hall.')
                    jump severina_debatediscussion02

    label severina_debatediscussion02:
        show areapicture galerocks01 behind galerocksboat, galerocksoverlay at basicfade
        if quarters > world_daylength-10 or quarters < 34:
            show galerocksboat behind galerocksoverlay at basicfade
        else:
            hide galerocksboat
        show galerocksoverlay keep at basicfade
        if not galerocks_debate_woodentoy:
            menu:
                'You follow the scent of cloves, until the man closes the door behind you, and you hear the thudding window shutters on the ground floor of the keep. As you approach the gate, the village seems more empty than usual, but the smoke doesn’t stop coming from the buildings of artisans.
                \n\nThe guard tells you to stay nearby, places his pillow on the stairs, and sits down. He observes you for some time, but then tilts his head back, as if he’s trying to take a dreamless nap.
                '
                'I wander nervously around the yard.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wander nervously around the yard.')
                    $ quarters += 6
                    menu:
                        'You take a better look at the hill, noticing that some of the previous signs of negligence are now gone. No more drying laundry or abandoned weapons - what’s more, Severina’s granddaughter is now sitting on the wall’s walk, dangling her legs, with an unloaded crossbow at her side. She doesn’t pay you much attention, mostly focused on the falcons and harpies circling above the village.
                        \n\nEvery now and then, some sort of screaming or laughter reaches you from the keep, but other than that, the closed door and windows keep you without a clue. After more than an hour, both you and the man are called inside.
                        '
                        'Finally.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Finally.')
                            jump severina_debateresult01
                'I act as if I couldn’t care less.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I act as if I couldn’t care less.')
                    $ quarters += 6
                    menu:
                        'You sit down by the well, observing the pigeons on the ground and the falcons and harpies in the skies. After some time, the tiredness mixes with the boredom, making you think about anything in your pockets and bags that could distract you.
                        \n\nEvery now and then, some sort of screaming or laughter reaches you from the keep, but other than that, the closed door and windows keep you without a clue. After more than an hour, both you and the man are called inside.
                        '
                        'Finally.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Finally.')
                            jump severina_debateresult01
        else:
            menu:
                'You follow the scent of cloves, until the man closes the door behind you, and you hear the thudding window shutters on the ground floor of the keep. As you approach the gate, the village seems more empty than usual, but the smoke doesn’t stop coming from the buildings of artisans. There’s no time to stop the work.
                \n\nThe guard tells you to stay nearby, places his pillow on the stairs, and sits down. He observes you for some time, then takes out his usual knife and focuses his attention on a new wooden log.
                '
                'I wander nervously around the yard.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wander nervously around the yard.')
                    $ quarters += 6
                    menu:
                        'You take a better look at the hill, noticing that some of the previous signs of negligence are now gone. No more drying laundry or abandoned weapons - what’s more, Severina’s granddaughter is now sitting on the wall’s walk, dangling her legs, with an unloaded crossbow at her side. She doesn’t pay you much attention, mostly focused on the falcons and harpies circling above the village.
                        \n\nEvery now and then, some sort of screaming or laughter reaches you from the keep, but other than that, the closed door and windows keep you without a clue. After more than an hour, both you and the man are called inside.
                        '
                        'Finally.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Finally.')
                            jump severina_debateresult01
                'I look at the object in his hands. “What are you carving?”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at the object in his hands. “What are you carving?”')
                    $ galerocks_debate_woodentoy = 2
                    menu:
                        'He shows you what looks like a few tiny planks, already detached from the rest of the log, as well as four wheels, cored in the center. “It will be a wagon. Last time, I made a wheeled fish. I’m good with wheels,” he explains, giving you a warm, yet sad smile.
                        '
                        '“Then I won’t bother you.” I wander around the yard.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Then I won’t bother you.” I wander around the yard.')
                            $ quarters += 6
                            menu:
                                'You take a better look at the hill, noticing that some of the previous signs of negligence are now gone. No more drying laundry or abandoned weapons - what’s more, Severina’s granddaughter is now sitting on the wall’s walk, dangling her legs, with an unloaded crossbow at her side. She doesn’t pay you much attention, mostly focused on the falcons and harpies circling above the village.
                                \n\nEvery now and then, some sort of screaming or laughter reaches you from the keep, but other than that, the closed door and windows keep you without a clue. After more than an hour, both you and the man are called inside.
                                '
                                'Finally.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Finally.')
                                    jump severina_debateresult01
                        '“You’ve got a kid?” I look at his wrinkles. “A grandkid?”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’ve got a kid?” I look at his wrinkles. “A grandkid?”')
                            $ quarters += 6
                            $ galerocks_debate_woodentoy = 3
                            menu:
                                'He grins. “Oh, I have quite a family, I do. But this one is for my daughter. I’m still new at crafts, but she ain’t picky.” You ask him how old she is, and his eyes seem both defeated and accepting. “Thirty, she merely holds the soul of a child. She won’t ever go to the hills, beach, or forest, but has a good imagination, she does. I used to give her simple toys, swords and figurines, but she’d rather play with ones that can move, and wheels are the easiest for me.”
                                \n\nYou spend some time chatting about his experience, and the time goes quicker. Every now and then, some sort of screaming or laughter reaches you from the keep, but other than that, the closed door and windows keep you without a clue. After more than an hour, both you and the man are called inside.
                                '
                                '“Let’s go, then.”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s go, then.”')
                                    jump severina_debateresult01

label severina_debateresult01:
    show areapicture galerockskeep02 at basicfade
    hide galerocksoverlay
    hide galerocksboat
    if galerocks_debate_arguments >= (galerocks_debate_argument_needed+4):
        $ galerocks_dabate_abandonsglaucia = 1
        $ galerocks_reputation += 1
        $ severina_friendship += 1
        $ quest_galerockssupport = 2
        $ renpy.notify("Quest completed: The Support of Gale Rocks")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Support of Gale Rocks{/i}')
        $ quest_galerockssupport_description01 = "The villagers agreed to cut their ties with the bandits. The merchants and officials now have an open way to negotiate the terms of the new treaty."
        menu:
            'The eyes inside the keep are tired, yet kind, and you catch a few smiles. The council sits on the benches, with one of the elders napping, and some of the younger members look longingly at the exit. The windows are open once again, but the air is still stale, in part because of the flower perfumes.
            \n\n{color=#f6d6bd}Severina{/color} is standing behind her desk, leaning on the top, and welcomes you with a nod. You notice that many of her wax tablets have switched places, and half of them are open. “The vote is done. {i}Strong yes,{/i}” she states solemnly. “If {color=#f6d6bd}Glaucia{/color} wants to remain one of us, she needs to bring her band here, and stay free of robbery. We don’t trust the officials and merchants, but your words and deeds are enough to make us eager to negotiate with them. Now, let’s disband and eat something.”
            '
            'I thank the council.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I thank the council.')
                if pc_goal == "iwantstatus":
                    $ pc_goal_iwantstatuspoints += 2
                if pc_goal == "iwanttoberemembered":
                    $ pc_goal_iwanttoberememberedpoints += 1
                if quest_pc_goal == 1 and pc_goal == "iwantstatus":
                    $ renpy.notify("Journal updated: %s" %quest_pc_goal_name)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: %s{/i}' %quest_pc_goal_name)
                if quest_pc_goal == 1 and pc_goal == "iwanttoberemembered":
                    $ renpy.notify("Journal updated: %s" %quest_pc_goal_name)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: %s{/i}' %quest_pc_goal_name)
                menu:
                    'Many of the souls thank you for trying to make a change, while others congratulate you. {color=#f6d6bd}The old fisher{/color}, who found himself something stronger to drink, feels it’s necessary for him to take you to the side, and explain that you shouldn’t trust the guilds or priests anyway. You mostly nod, not entirely paying attention. Another elder pats your shoulder, whispering that you have “quite the support here,” but leaves before you can ask him what he means by that.
                    \n\nThe younger members of the council help the elders cross the yard, and as they engage in friendly chatter, they forget about the gathering quickly. {color=#f6d6bd}The headwoman{/color} stops you before you follow their lead. “There’s one more thing, [pcname],” coming from her lips, your name sounds strange to you. “If you don’t have to depart for {color=#f6d6bd}Hovlavan{/color} just yet, can you pass our decision to {color=#f6d6bd}Glaucia{/color}?”
                    '
                    '“What? No way, she’s going to kill me.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What? No way, she’s going to kill me.”')
                        menu:
                            '“I doubt it. On the other hand, by not bringing her the news you’ll make her life much harder, and so it would be unwise to return to the peninsula after winter. Give her the time to prepare herself, and to make the choice out of her will, not hunger. She’ll spare you.”
                            '
                            '“As a messenger, I deserve my pay.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “As a messenger, I deserve my pay.”')
                                $ custom1 = "She smirks. “And what do you need?”"
                                jump severina_rewardsafterdebate01
                    '“And for nothing in return, I expect?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And for nothing in return, I expect?”')
                        $ custom1 = "She scowls at you. “And what can I give you in return?”"
                        jump severina_rewardsafterdebate01
    elif galerocks_debate_arguments >= galerocks_debate_argument_needed:
        $ galerocks_dabate_abandonsglaucia = 1
        $ quest_galerockssupport = 2
        $ renpy.notify("Quest completed: The Support of Gale Rocks")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Support of Gale Rocks{/i}')
        $ quest_galerockssupport_description01 = "The villagers agreed to cut their ties with the bandits. The merchants and officials now have an open way to negotiate the terms of the new treaty."
        menu:
            'The eyes inside the keep are tired, yet gentle. The council sits on the benches, with one of the elders napping, and some of the younger members look longingly at the exit. The windows are open once again, but the air is still stale, in part because of the flower perfumes.
            \n\n{color=#f6d6bd}Severina{/color} is standing behind her desk, leaning on the top, glancing at you with hardly any emotion. You notice that many of her wax tablets have switched places, and half of them are open. “The vote is done. {i}Weak yes,{/i}” she states solemnly. “If {color=#f6d6bd}Glaucia{/color} wants to remain one of us, she needs to bring her band here, and stay free of robbery. We don’t trust the officials and merchants, but we’re ready to negotiate with them. Now, let’s disband and eat something.”
            '
            'I thank the council.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I thank the council.')
                if pc_goal == "iwantstatus":
                    $ pc_goal_iwantstatuspoints += 2
                if pc_goal == "iwanttoberemembered":
                    $ pc_goal_iwanttoberememberedpoints += 1
                if quest_pc_goal == 1 and pc_goal == "iwantstatus":
                    $ renpy.notify("Journal updated: %s" %quest_pc_goal_name)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: %s{/i}' %quest_pc_goal_name)
                if quest_pc_goal == 1 and pc_goal == "iwanttoberemembered":
                    $ renpy.notify("Journal updated: %s" %quest_pc_goal_name)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: %s{/i}' %quest_pc_goal_name)
                menu:
                    'A few of the souls thank you for trying to make a change, while others congratulate you. {color=#f6d6bd}The old fisher{/color}, who found himself something stronger to drink, feels it’s necessary for him to take you to the side, and explain that you shouldn’t trust the guilds or priests anyway. You mostly nod, not entirely paying attention.
                    \n\nThe younger members of the council help the elders cross the yard, and as they engage in friendly chatter, they forget about the gathering quickly. {color=#f6d6bd}The headwoman{/color} stops you before you follow their lead. “There’s one more thing, [pcname],” coming from her lips, your name sounds strange to you. “If you don’t have to depart for {color=#f6d6bd}Hovlavan{/color} just yet, can you pass our decision to {color=#f6d6bd}Glaucia{/color}?”
                    '
                    '“What? No way, she’s going to kill me.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What? No way, she’s going to kill me.”')
                        menu:
                            ' “I doubt it. Although, if she’s going to learn about it only after some time, I don’t wish you a healthy spring and summer. Bring her the news, give her time to prepare herself, and to make the choice out of her will, not hunger.”
                            '
                            '“As a messenger, I deserve my pay.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “As a messenger, I deserve my pay.”')
                                $ custom1 = "She smirks. “And what do you need?”"
                                jump severina_rewardsafterdebate01
                    '“And for nothing in return, I expect?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And for nothing in return, I expect?”')
                        $ custom1 = "She scowls at you. “And what can I give you in return?”"
                        jump severina_rewardsafterdebate01
    elif galerocks_debate_arguments < (galerocks_debate_argument_needed/2):
        $ galerocks_dabate_loyaltoglaucia = 2
        menu:
            'The eyes inside the keep are tired, yet stern. Some of the elders are sitting on the benches, but the majority of the council members are already in the back of the room, waiting to leave. The windows are open once again, but the air is still stale, in part because of the flower perfumes.
            \n\n{color=#f6d6bd}Severina{/color} is standing behind her desk, leaning on the top, glancing at you with reluctance. You notice that many of her wax tablets have switched places, and half of them are open. “The vote is done. {i}Strong no,{/i}” she states solemnly. “{color=#f6d6bd}Glaucia{/color} is one of us, and you offered us no reason to trust the officials more than we would her. Now, let’s disband and eat something.”
            '
            'I nod to the council.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod to the council.')
                $ quest_galerockssupport = 4
                $ renpy.notify("Quest completed: The Support of Gale Rocks")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Support of Gale Rocks{/i}')
                $ quest_galerockssupport_description02 = "The villagers are now convinced to take an even stronger stance on the side of the bandits. It’s going to be bad news for the city merchants."
                menu:
                    'A few of the souls thank you for trying to make a change, while others mock your poor results. One of the comments, aimed at {color=#f6d6bd}Iuno{/color}, mentions that it was unwise to even consider an outsider’s voice, but she responds only with a shrug.
                    \n\nThe younger members of the council help the elders cross the yard, and as they engage in friendly chatter, they forget about the gathering quickly.
                    '
                    'I go down the hill.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go down the hill.')
                        jump galerocksleavingseverina01
    elif galerocks_debate_arguments < galerocks_debate_argument_needed:
        $ galerocks_dabate_loyaltoglaucia = 1
        menu:
            'The eyes inside the keep are tired, yet stern. The council sits on the benches, with one of the elders napping, and some of the younger members look longingly at the exit. The windows are open once again, but the air is still stale, in part because of the flower perfumes.
            \n\n{color=#f6d6bd}Severina{/color} is standing behind her desk, leaning on the top, glancing at you with hardly any emotion. You notice that many of her wax tablets have switched places, and half of them are open. “The vote is done. {i}Weak no,{/i}” she states solemnly. “{color=#f6d6bd}Glaucia{/color} is one of us, and, at least for now, we trust her more than we would the officials and merchants. Now, let’s disband and eat something.”
            '
            'I nod to the council.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod to the council.')
                $ quest_galerockssupport = 3
                $ renpy.notify("Quest completed: The Support of Gale Rocks")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Support of Gale Rocks{/i}')
                $ quest_galerockssupport_description02 = "The villagers are now convinced to take an even stronger stance on the side of the bandits. It’s going to be bad news for the city merchants."
                menu:
                    'A few of the souls thank you for trying to make a change, while others admit your attempt was fair. {color=#f6d6bd}The old fisher{/color}, who found himself something stronger to drink, feels it’s necessary for him to take you to the side, and explain that you too shouldn’t trust the guilds or priests. You mostly nod, not entirely paying attention.
                    \n\nThe younger members of the council help the elders cross the yard, and as they engage in friendly chatter, they forget about the gathering quickly.
                    '
                    'I go down the hill.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go down the hill.')
                        jump galerocksleavingseverina01
