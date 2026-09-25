<!-- Lecture notes for the slides on `problem-decomposition`, written in German. They follow the slides in order; frame numbers refer to the deck. The slides themselves are embedded on https://docs.lifi-project.de/concepts/problem-decomposition.html -->

# Lecture notes: cutting problems (Cutting Problems)

Deck 01, the first input of the semester, on the concept "Cutting Problems". These notes explain the slides for you to read afterwards. They follow the order of the slides and give the numbers as the HTML deck counts them (every build-up step has a number of its own, 36 frames), but they can be read as a text on their own.

## What this is about

Big problems are not solved in one piece. They are cut, again and again, until the pieces can be solved and checked. This input shows that you can already do this, hands you three tried and tested cutting patterns, and explains how to recognise a good cut. At the end it says why exactly this skill makes the difference when you work with AI assistants.

## Part 1: you can already do this

**How do you eat an elephant? (slide 4).** One bite at a time. The saying is old, but it holds: nobody eats an elephant in one piece, and nobody solves a big problem in one piece. Big problems are not solved, they are cut.

**The party (slides 5 and 6).** Your flatmate turns 25, party on Saturday, 30 guests. Slide 5 shows this one thing, and nobody plans it as one thing. Slide 6 shows what you do straight away: cut. Drinks, food, music, invitations, cleaning up, and then hand the pieces out. That is decomposition. You have been able to do it for a long time, you have just never called it that. Along the way, the pieces are cut so that you can ask about each one separately whether it is done. We will come back to that.

## Part 2: this semester's elephant

**The task (slide 8).** "transfer a file from one laptop to another, using light." Put like this, as one piece, nobody can solve it. No professional, no AI, and not you either. That is not a threat, it is the normal state of things: interesting problems are always too big at the start.

**The decomposition (slides 9 to 11).** Slide 9 shows the big problem on its own. Slide 10 shows it cut into four pieces: telling colours apart, turning letters into colours, finding the beginning and the end, transferring a whole file. Every piece is solvable, by you, in two to three weeks. Slide 11 calls the pieces by their names, and that is the point: your semester plan is exactly this decomposition. The four pieces are called Challenge 1 to 4. This semester is not built this way by accident; it is the decomposition of a problem that cannot be solved any other way.

**One question, four questions (slide 12).** Behind the decomposition into four challenges sits the map of the whole module. The big question is: how can we solve complex problems with computers? Beneath it lie four questions about information: how do computers represent it, how do they store it, how do they transfer it, how do they process it. Under each question stand its most important concepts, for transferring for instance signal and noise, timing and protocols. All four questions concern you, if not all equally: the light link is the transferring, but you represent colours as symbols, you store a file, and a checksum processes it. Beneath the big question stand the skills we tackle it with: cutting problems, the IPO model, writing programs, measuring, thinking in layers. Every session works on one of the four questions; on the website the same map hangs above all the concepts.

## Part 3: three ways to cut

There are many ways to cut. You will need three of them all the time.

**Divide and conquer: halve until it's easy (slides 14 to 21).** Think of a number between 1 and 100. Slide 14 shows the starting state: a hundred candidates, a bar across the full width, and somewhere inside it the 73 we are looking for. With every yes/no question a row is added and the bar gets shorter: "bigger than 50?" yes, and half is gone; "bigger than 75?" no, and again half. It goes on like this through 25, 12, 6, 3, 2 candidates to the last question on slide 21, and the number is settled. Seven questions are always enough, whatever the number. In computer science the strategy is called divide and conquer, and it works wherever you can rule out one half after every cut. The yellow question at the foot of the last slide, "how many steps in general?", is deliberately left open. It is a preview of a later topic: every yes/no question is one bit of information.

**The same trick when something is broken (slides 22 to 24).** The wifi is dead. How do you go about it? Slide 22 shows the chain of suspects: laptop, wifi, router, provider, internet. On slide 23 the test in the middle arrives, and half the chain is dealt with: if the phone hotspot works, it is not the laptop. That is exactly what you do by instinct when you look at the lights on the router or try another device. Slide 24 puts the same chain for the project next to it: sender, LED, air, sensor, receiver. You will walk along it often when "nothing arrives": is the LED lit at all? Does the sensor see a torch? Whoever cut coarsely only knows that something is broken. Whoever cut well knows where.

**Solve the smaller version first (slide 25).** When the problem is too big, first solve a smaller version that you really can do, and grow from there: first light on and off, then as many distinguishable colours as possible, then a character, then a word, and at the end a whole file. The staircase on the slide is your semester, the steps are Challenges 0 to 4. Today you are standing on the bottom one.

## Part 4: a good cut is testable

**The exam example (slides 27 and 28).** "I need to learn maths" and "I can pass the 2023 exam in 90 minutes" both sound like exam preparation. The difference is on slide 28: with the first you never know whether you are done. The second you can try out tonight, and you get a yes or a no. A good piece is one with a test built into it.

**The same in the project (slides 29 and 30).** "The LED works" is a feeling. "Red or blue, recognised correctly 50 times in a row" is a measurement. Every challenge is written exactly like that, and the acceptance tests run exactly like that: there is always a test that says yes or no.

**The workshop rule (slide 31).** "done means: the test passes." Done does not mean "looks good", done means: the test passes. Every task in this module ends with a checking step that you can carry out yourself, without waiting for anyone.

## Part 5: cuts are agreements

**Where you cut decides how much you have to talk (slide 33).** Back to the party. On the left of the slide, two responsibilities with a clear edge: "You do the starters, I do the dessert." That works. On the right, two responsibilities overlap, both of you somehow do the food, and in the overlap stands the question that then stays open: who buys the bread? Pieces work when the border is clear. The same holds in a team of two: one person at each end of the link, and whatever crosses the border, for instance which colour means which character, gets written down. You will find out how serious that is in Challenge 3, when another team has to read your agreement and implement it.

**Dividing the work with the AI assistant (slides 34 and 35).** Two ways to give the assistant a job. "build me the file transfer" is one big wish. The agent cannot fulfil it well, and you could not even check the result. Against it, the small job that brings its test along: "read the sensor ten times and return the average. test: covered, it stays under 10. red led on, it goes over 100." The job says what should come out and how you check it: cover the sensor, average under 10; red LED on, average over 100. That takes ten seconds, and afterwards you know instead of believing. Cutting is the skill that takes you from "I hope the AI is right" to "I have checked it". That is why it is among the four goals of this module, and that is why it is the first input of the semester: you cut. The assistant solves pieces. You check.

**One bite at a time (slide 36).** The elephant from the start, one more time at the end. You can already do this, today you have gained three cutting patterns, and you now know how to recognise a good cut: by the test built into it.

## Further reading

The concept page [Cutting Problems](../../website/concepts/problem-decomposition.qmd) sums the whole thing up with the figures. What a cut piece looks like when a computer is supposed to solve it is the topic of the next input (input, processing, output).
