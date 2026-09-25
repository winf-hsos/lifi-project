# Cutting Problems

Online: <https://docs.lifi-project.de/concepts/problem-decomposition.html>

## Summary

A big problem becomes solvable when you cut it into small pieces you can check one by one. There are cutting patterns that come back again and again. A good cut also settles two things at once: how you will know that a piece is done, and what has to be agreed at its borders.

In this chapter, we address the following questions:

- How do I cut a big task into pieces I can check on their own?
- How do I know that a piece is small enough?
- Which cutting patterns are there, and when does which one help?
- What happens when I cut too coarsely?
- What has to be agreed at the border between two pieces?

You need this concept from [Challenge 0](../challenges/challenge-0.md) onwards, in every single challenge. What a cut piece looks like once a computer is supposed to solve it is the subject of [Problem solving with computers](input-processing-output.md).

## Explanation

"Transfer a file using light" cannot be solved in one piece, by anyone. That is not a statement about you, it is the normal state of an interesting problem. Big problems are not solved in one go. They are cut, again and again, until the pieces are small enough to be solved and checked.

You can already do this, by the way. Somebody's birthday is on Saturday, thirty guests are coming, and nobody plans "the party" as one thing. You cut it immediately into drinks, food, music, invitations and cleaning up, and then you hand the pieces out. What is new here is only doing it on purpose, and knowing what makes one cut better than another.

[Figure: The big problem of this semester, cut into four solvable pieces. Each piece is something you can manage in two or three weeks, and your semester plan is exactly this cut: the four pieces are Challenge 1 to 4.]

### Three cutting patterns

There are tried and tested ways to cut, and you will use three of them all the time this semester.

**Halve it until it is easy.** Computer science calls this divide and conquer. Think of a number between 1 and 100. With yes-or-no questions that cut the range in half every time, you find any number in at most seven questions: a hundred candidates, then fifty, twenty-five, twelve, six, three, two, done. The strategy works wherever you can rule out one half after every cut.

[Figure: The range from 1 to 100, halved with every question. The bar is the range the number can still be in, and the red line is the 73 we are looking for. It stays inside the bar until exactly one number is left.]

**The same trick when something is broken.** You know this one too. When the wifi is dead, you test in the middle of the chain without thinking about it: if the phone hotspot works, it is not the laptop, and half the suspects are gone. Every test halves the chain. In this project your chain is sender, LED, air, sensor, receiver, and you will walk along it often: is the LED lit at all? Does the sensor see a torch? Whoever cuts well knows not only **that** something is broken, but **where**.

[Figure: Finding a fault by halving: one test in the middle rules out half the chain. Above the everyday case, below the same figure of thought in the project.]

**Solve a smaller version first.** When a problem is too big, solve a smaller version of it that you really can do, and grow from there. That is exactly how the semester is built: light on and off, then as many colours as you can tell apart, then a single character, then a word, and a whole file at the end.

[Figure: The staircase of the challenges: every step is a slightly bigger version of the same problem. On the first day you are standing on the bottom one.]

### A good cut is testable

Cutting alone is not enough, because not every cut is equally good. Compare two sentences: "I need to learn maths" and "I can pass the 2023 exam in 90 minutes". Both sound like exam preparation. With the first one you never know whether you are done. The second one you can try out tonight, and you get a yes or a no. A good piece is one with a test built into it.

In the project that reads: "the LED works" is a feeling. "Red or blue, recognised correctly 50 times in a row" is a measurement. Every challenge is written that way, and every acceptance test runs that way. From this follows the workshop rule of this module: **done means the test passes**, not "it looks good".

### Cuts are agreements

Where you cut decides how much you have to talk. "You do the starters, I do the dessert" works. "We both kind of do the food" turns into chaos, because nobody knows who buys the bread. Pieces work when the border between them is clear.

The same holds in your team: one person at each end of the link, and whatever crosses the border, for instance which colour means which symbol, gets written down. You will find out how serious that is in [Challenge 3](../challenges/challenge-3.md), when another team has to read your agreement and build against it.

And with an AI assistant, cutting is the key skill of all. "Build me the file transfer" is one big wish: the assistant cannot do it well, and you could not check the result if it did. A small piece with its test is a different thing: "read the sensor ten times and return the average. test: covered, it stays under 10; red LED on, it goes over 100." You cut, the assistant solves pieces, you check.

## Slides

The slides for this concept, right here. Page through them with the buttons in the top right corner, or click into the slides and use the arrow keys. The other buttons give you full screen, the slides in a new tab, and the deck as a PDF.

## Practice questions

Try questions in the exam format here, with the answer and its reasoning shown right away.

## Further reading

- George Pólya: How to Solve It. Princeton University Press, 1945. The classic on cutting problems, written for mathematics and readable far beyond it: understand the problem, make a plan, carry it out, look back. His questions ("Do you know a related problem?", "Can you solve a part of it?") are the long version of this page.
