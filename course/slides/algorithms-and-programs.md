<!-- Lecture notes for the slides on `algorithms-and-programs`. They follow the slides in order; frame and slide numbers refer to the deck. The slides themselves are embedded on https://docs.lifi-project.de/concepts/algorithms-and-programs.html -->

# Lecture notes: what is a program? (Algorithms and Programs)

Deck 02 on the concept "Algorithms and Programs", the input in session 2, second part. These notes explain the slides for reading afterwards. They follow the order of the slides and give the numbers as the HTML deck counts them (every build-up step has its own number, 40 frames), but they can be read as a text on their own. The corresponding concept on the website: [Algorithms and Programs](../../website/concepts/algorithms-and-programs.qmd).

## What this is about

The IPO part before left one question open: how does the box do its work? The answer comes in two stages: first the algorithm, which you already know because you carried one out, then the program, the same procedure written down for a machine. After that come the four building blocks every program consists of, how to deal with error messages, and how to work with the AI assistant without just receiving code.

## Part 1: last week

**Who is playing? (slide 4).** A piano is playing, the keys move, the bench is empty. Around 1900, self-playing pianos like this stood in many parlours. The player is the paper roll above the keyboard: every punched hole means "press this key now". The piano understands nothing about music, it only executes. The real pianist is the person who punched the roll, perhaps decades earlier. The roll is the program, the piano the machine, the puncher the programmer. And you have already been something like this piano yourselves.

**You were already the receiver (slide 5).** In the first session you did the receiving yourselves, in the colour card experiment: look at the card, decide which colour it is, write down the matching symbol, wait for the next one.

**That was an algorithm, and you were the machine (slide 6).** Now the thing gets its name: a sequence of steps described so precisely that you can carry it out without understanding what it is about is called an algorithm. It needs no computer, it can stand on a piece of paper, and that is exactly how you worked through it.

**Four lines, one of them hard (slide 7).** The same four lines again, this time with the second one highlighted. From today, the computer takes over three of them, one piece at a time. Deciding which colour is there is Challenge 1, and it will keep you busy for three weeks.

**One more algorithm, live (slides 8 and 9).** Six volunteers line up unsorted in a row and strictly follow five rules: stand in a row, look at your right neighbour, swap if they are shorter, at the end of the row start again, and a full pass without a swap means done. No thinking, only executing. After two or three minutes the row stands in order of height, and you have run bubble sort; computers sort like this too, only faster. Take two observations with you. How did the procedure recognise its end? By the full pass without a swap; that is a termination condition, and it comes back in part 3. And how many comparisons was that with six people, and what would it be with forty? That comes back too, when we get to cost.

**A program is an algorithm written down for a machine (slide 10).** In this transition a requirement comes in that the piece of paper did not have: completeness. A person reading it fills in what was obviously meant. The machine fills in nothing.

## Part 2: the instruction follower

**A program is a list (slide 12).** A list of instructions, and something that follows this list, exactly and in order. There is no more magic involved than that.

**The list at work (slide 13).** Three lines from top to bottom, and next to them on the right, what you see: the first makes the LED red, the second keeps it red for a second, the third makes it blue. Every line changes something visible. And the machine does not know what was meant: it executes what is written, in the order it is written, and nothing else. Almost all the errors of this semester come from exactly this difference.

**Anatomy of a line (slides 14 to 17).** The line consists of three parts. The first piece says which thing is being addressed, here the LED. The second says what it should do. The third says with which values, here full red, no green, no blue.

**Same instruction, different values (slide 18).** The same instruction twice, once with red, once with blue. The name says what happens; the values say how.

## Part 3: four building blocks

Every program in this world consists of four building blocks: instructions one after another, values with names, repetition, condition. You see all four on the LED.

**Building block 1: one after another (slides 20 to 22).** Instructions run in order. Slide 21 puts two programs side by side, both correct: with a pause, red stays visible for a second; without a pause, red lives for about a millisecond, far too short for an eye, and you only see blue. The program is not broken, it is too fast. Your eyes are slow, the machine is not. Slide 22 shows the same for the order: move the pause to the end, and the machine waits with a blue LED, and red is once again visible for only a millisecond. No line is missing, and still it is a different program.

**Building block 2: a value with a name (slide 23).** A name for a value that you then use everywhere. The gain is not brevity, but one place to change instead of many.

**Building block 3: repetition (slides 24 and 25).** A list of colours and a loop over it. A loop is not magic but a way of writing: the same two lines run four times, each time with the next value from the list. Slide 25 rolls this out against time: on the left what you write, on the right four passes with one value and one second each, four seconds in total.

**Building block 4: only if (slide 26).** A condition runs the indented line only if it holds, and "else" says what happens otherwise. With that, a program can react to something instead of stubbornly reeling off the same thing.

**When does this end? (slide 27).** You know the termination condition from the sorting exercise; here it is missing. The condition is always true, and there is no way out in the loop body, so this program never ends. For continuous blinking that is even right; a receiver's main loop, on the other hand, needs a stopping condition. The workshop classic "my program hangs" almost always means "my loop has no way out".

**What does it cost? (slide 28).** Two procedures can both be correct and still be worlds apart. In the number guessing game from session 1, one asks up to 99 times, the other at most seven times. With a thousand numbers it is 999 against 10. Correctness is the minimum requirement; after that you compare algorithms by how their cost grows with the problem. For your transmission this becomes the concrete question of how many seconds a file is on its way. The thread is picked up again in session 13.

## Part 4: it does what is written

**Reading the error message (slides 30 to 33).** A traceback looks threatening, but it is a precise report, and the slide reads it with you line by line: which file and which line, what stood there, and what exactly does not exist, here the spelling "set_colour" with a u instead of "set_color". The machine did not fail; it did what was written and reports exactly where it got stuck.

**Information, not a verdict (slides 34 and 35).** An error message is information about the program, not a judgement of you as a person. Read it out loud; most of the time it says literally what is wrong. And you see how to deal with it live: at the front, on the projector, errors are built in on purpose, one after another, and resolved.

## Part 5: working with the assistant

**Two ways to ask (slides 37 and 38).** The first question gets you code you do not understand. The second says what should come out and orders the explanation along with it: it gets you code and understanding.

**The rule (slide 39).** Never keep code you cannot change. Every hand-over ends with a small change you make yourself: swap a colour, adjust a waiting time. If you cannot do that, you have not taken the code over, you have only copied it.

**The workshop task (slide 40).** Today: first, one colour on; second, four colours in a loop; third, blinking with adjustable speed. Number three is the real task: the speed must be changeable in exactly one place, without digging through the code, so use building block 2.

## Further reading

The concept page [Algorithms and Programs](../../website/concepts/algorithms-and-programs.qmd) sums up the whole thing with the figures. How to compare two correct procedures you saw in session 1 with the number guessing game: 99 questions or 7, both correct, one of them uselessly slow.
