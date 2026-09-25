<!-- Lecture notes for the slides on `input-processing-output`. They follow the slides in order; frame and slide numbers refer to the deck. The slides themselves are embedded on https://docs.lifi-project.de/concepts/input-processing-output.html -->

# Lecture notes: solving problems with computers (Problem Solving with Computers)

These notes accompany the input "Solving problems with computers" in session 2. They can be read as a text of their own and follow the order of the stagekit deck. A slide with a build-up appears as several frames in the talk and in the export; that is why the references run from Frame 1 to Frame 41.

The matching concept on the website is [Problem Solving with Computers](../../website/concepts/input-processing-output.qmd).

## What it is about

From the first input, students know how a big problem is cut into testable pieces. Now comes the follow-up question: what does such a piece have to look like if a computer is to solve it?

The answer is the IPO pattern: input, processing and output. It holds for a logic gate just as it does for a function or a whole system. Once the input and the expected output are clear, the box can be tested. Programs answer the question of the processing; the representation of the data is a second question in its own right.

## Part 1: What happens in the middle?

### The invisible in-between (Frames 1 to 4)

The opening shows an ordering terminal in a restaurant. At the front we enter an order, and at the back a tray appears later. The kitchen in between stays invisible. For ordering, it is still enough to know the input and the expected output.

The terminal also hints at a second question: we do not simply speak our order into the room. We choose tiles, quantities and options. Even before the kitchen gets to work, the order has been brought into a form the system can process. This question of representation comes back at the end of the input.

### The shape of a solvable piece (Frames 5 to 8)

A piece that a computer can solve always has the same shape. At the front data go in: the input. At the back data come out: the output. In between lies the processing. Together the three parts are called input, processing and output, IPO for short.

The box is not a particular device. It is a way of thinking. We can use it to describe a pocket calculator, a Python function, a sensor, a sender or a whole transmission system. What matters first is not the technical details but the edges of the box: what really goes in, and what is really supposed to come out?

### The built-in test (Frames 9 to 12)

A small example makes the connection to the decomposition from session 1 visible. The function `add()` gets `2, 3` and is supposed to return `5`. With that, a test has already been written:

1. Put `2, 3` in.
2. Run the processing.
3. Compare the actual output with the expected `5`.

If the box returns `5`, the test passes. If it returns `6`, the test fails. To find that out, we do not yet need to know how `add()` works inside. Clear inputs and expected outputs make a box testable.

The sentence to remember: if you know the input and the expected output, you have a test.

## Part 2: The boxes in our project

### The sender (Frames 13 and 14)

The sender of the light link is an IPO box. A message such as `"hi"` goes in. `encode()` processes the text. A sequence of colour symbols comes out.

The edges matter: before `encode()` there are characters, after it there are colour symbols. Which colour carries which meaning is not a fact of nature. It is an agreement within the team. Only this agreement makes the sender's output understandable for the next piece.

### What does the receiver really see? (Frames 15 and 16)

At the receiver, it looks at first as if red light goes in and the text `"red"` comes out. For the computer, though, no concept "red" goes in. The sensor delivers readings, for example:

`r = 203, g = 41, b = 57, c = 310`

The first three numbers stand for the measured red, green and blue components, the fourth for the overall brightness. What these numbers mean is decided by the processing, `classify()`. Our eyes see red. The box sees four numbers.

### The interactive IPO test (Frame 17)

The demonstrator shows the receiver as an IPO box you can change. On the left you can set the four sensor values. In the middle there are two decision boundaries:

- Below a minimum brightness, the output is `off`.
- If the two strongest colour channels are too close together, it is `uncertain`.
- Otherwise the strongest colour channel wins.

On the right are the actual and the expected output. If they match, the test passes; otherwise it fails.

The preset "clear red" starts with an unambiguous success. With "weak red" you can lower the brightness so far that the same relative colour components count as `off`. "Mixed light" shows that a changed decision boundary can produce a different output while the readings stay the same. That way input, processing, output and test become something you experience directly.

### Boxes can be plugged together (Frames 18 to 20)

The output of one box can become the input of the next. The whole link can be read as a chain:

`"hi" → encode() → colour symbols → light → decode() → "hi"`

At every connection point, the form and meaning of the data have to be agreed. A piece can work correctly on its own and the whole link can still fail, if two neighbouring boxes expect different things at their boundary.

Boxes in a row show the data flow. This view also gives you a route for debugging: if `"hi"` does not arrive at the end, we follow the data from boundary to boundary. We check the code that was produced, the LED, the sensor values and finally `decode()`. The guiding question is: up to which boundary are the data still correct?

The sentence to remember in Frame 21 is therefore: to find the fault, follow the data and test one boundary after the other.

## Part 3: Boxes at every level

### Opening a box (Frames 22 to 25)

From the outside, the whole sender can be seen as one box. A message goes in, light comes out, and `send()` names the whole processing.

If we open this box, its processing turns into a chain of smaller boxes: encode the text, choose a colour symbol and drive the LED. Each small box again has its own inputs and outputs and can be checked separately.

How far we open a box depends on our question. If you test the whole link, you need different inputs and outputs than someone who only looks at `encode()` or at driving the LED. We open a box only as far as the current question requires.

### The same shape at three levels (Frames 26 to 28)

The IPO pattern survives across the levels:

- System: message in, sender works, light out.
- Function: text in, `encode()` works, symbols out.
- Logic gate: `1, 1` in, the AND rule is applied, `1` out.

The resolution changes, the shape does not. That is why IPO can connect very different technical things with one another without blurring their differences.

### Chain and nesting (Frame 29)

There are two relationships between boxes that must not be confused:

- Boxes in a row show data flow: where do the data go next?
- Boxes inside boxes show hierarchical decomposition: what smaller work happens inside?

Both views are useful. Which one fits depends on the question. The fitting level is the one at which a clear input and an expected output can be stated. Frame 30 sums this up: the right level is the one we can test.

## Part 4: Two questions in every box

### Processing and representation (Frames 31 to 35)

Every IPO box gives rise to two basic questions.

The first is: how does the box work? That is the question of processing. Its answer is called a program. In the next input this answer is examined more closely.

The second is: how do we write things down so that a machine can work with them? That is the question of how inputs and outputs are represented. The sensor case has already shown it: "red" had to become four numbers before a program could work with it.

Almost all further concepts of the module can be placed at one of these two questions.

### The map of the next weeks (Frame 36)

The processing question leads directly to "Algorithms and Programs". The representation question leads first to readings, and after that to symbols and information, code systems and number systems. The IPO box stays as the map throughout. Only the place we zoom into changes.

### An AI agent is a box, too (Frames 37 to 40)

An AI agent can also be seen as an IPO box. A task goes in, code comes out. The inside of this box is hard to look into. That is exactly why clear examples and expected results matter.

A precise input improves the task. An expected output provides the yardstick. Only the comparison between the actual and the expected result decides whether the suggestion is usable. Testability replaces trust not only for simple functions, but above all for systems that are hard to see through.

### Transition to the next input (Frame 41)

The closing picture shows the kitchen counter from the opening story. At the beginning we stood in front of the closed door and knew only the order and the tray. Now we know the shape of every piece a computer can solve, and we know how its edges make a test possible.

Next, we open the box in the middle. The processing inside it is called a program.
