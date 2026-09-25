# Working with your AI assistant

Online: <https://docs.lifi-project.de/ai/index.html>

You may use the AI assistant in this project without any restriction. I want you to. It is part of the task, not a way around it.

Here is the picture to keep in mind. The assistant has read more about programming, sensors and protocols than any of us ever will. It has never seen your device. It does not know how bright your room is, how far apart your boxes stand, or what your sensor reports when the LED is red. Everything it says about those things is a guess, sometimes a good one. Everything you measure about them is a fact. Working well with the assistant means knowing, at every moment, which of the two you are holding.

## What you can use it for

Writing code is the obvious use, and it is far from the only one. Some concrete suggestions, roughly in the order you will need them.

**Installing the software.** The [Required Software](../software/index.md) page has eight steps, and something usually goes wrong in one of them. As soon as OpenCode itself is running, it can take over: paste the error message, or take a screenshot of the window you are stuck at and give it that. The assistant can read screenshots. It will tell you what the message means and what to do next, on your operating system, in your language.

**Understanding what was said in class.** If something stayed unclear, have it explained again, in other words, with an example, until it sits. An assistant is patient and thinks no question is too simple. For many students this is the most valuable use of all.

**Reading an error message.** Python's error messages are honest but unfriendly. Paste the whole message, including the lines above it, and ask what it is complaining about. Then fix it yourself. You will start recognising the common ones within a week.

**Finding ideas when you are stuck.** Describe your problem and ask for several ways to solve it. You do not have to take any of them. Often it is enough to see three options to notice which one fits your setup.

**Getting feedback before you build.** Describe what you plan to do and ask what could go wrong. Show your code and ask what you have overlooked. This is different from having a solution handed to you, and it is where the assistant is at its best.

**Making sense of your measurements.** Your module writes a log of everything the device did. Give the assistant that file, or a table you copied from it, and ask what it sees: which two colours are closest together, how much the readings wobble, whether something drifted over time. It is good at spotting patterns in numbers. It is not good at knowing whether the numbers are right, so keep that part.

**Looking things up.** Datasheets, libraries, technical terms you meet and do not know. Check what can be checked, especially numbers.

**Writing your documentation.** Dictate what you did and let it draft the text, then correct it. A measurement log that the assistant has tidied up is easier for your partner to read. What you must not let it do is invent the measurements.

**Testing your protocol specification.** In Challenge 3 another team has to build a receiver from your specification. Before you hand it over, give it to the assistant in a fresh session and ask it to describe the receiver it would build. Where it guesses, your specification has a hole.

**Practising for the exam.** Ask it to quiz you on a concept from the [overview](../concepts/index.md), then explain your answers back to it. It will tell you where your explanation is thin.

## Two conditions

### You must be able to explain your code

Every time you show your work, you will be asked to make a small change to your running program on the spot. Whoever has only copied notices there, and early enough to change that.

This is not a trick. It is the test that matters: not whether you can produce a program, which the assistant can do, but whether you can tell what it does and why, which only you can.

### The log of mistakes

For every challenge you document two or three places where the assistant suggested something and a measurement proved it wrong, and what actually turned out to be true.

This is the most useful document you will write, and it is not a confession. It marks exactly where the assistant's knowledge ends and yours begins. A team with a good log of mistakes has learned to tell a plausible answer from a true one, and that is a skill you will need in every subject from now on.

### Why this matters

No language model knows how *your* setup behaves in *your* room. It can help you with code very well, but every statement about range, speed or reliability you have to measure yourselves. That is exactly what the real work in this project consists of.

## Good questions to ask

The difference between a useful answer and a useless one is usually in the question. A few patterns that work.

**Give it the facts it cannot know.** "My two boxes are 25 cm apart, the room has daylight from the left, integration time is 154 ms, gain is 16. Here are ten readings for red and ten for orange. Are these two reliably distinguishable?" is a question it can help with. "Which colours should I use?" is not, because it has no idea what your sensor sees.

**Ask for options, not for the answer.** "Give me three ways the receiver could detect the start of a message, with the drawback of each" leaves the decision with you, which is where it belongs.

**Ask it to find holes.** "Here is my plan for Challenge 2. What will break first when I double the symbol rate?" It is better at criticising than at inventing.

**Ask for the smallest test.** "What is the simplest experiment that would tell me whether the problem is my timing or my thresholds?" The answer is often a five-line program, and running it is worth more than an hour of discussion.

**Ask it to explain, not to do.** "Explain what this line does" teaches you something. "Fix this" teaches you nothing, and you will be asked to explain the fix anyway.

And when it gives you a number about your device, a range, a rate, a threshold, do not write it down. Measure it. Then write down what you measured, and if the two differ, you have your next entry for the log of mistakes.
