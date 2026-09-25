# Links

Online: <https://docs.lifi-project.de/links.html>

Everything this module points to, in one place.

## Course

- [This website](https://docs.lifi-project.de/): the course companion, also the knowledge base your AI assistant reads.
- [Team cockpit](https://lifi.uber.space/cockpit): your light link live in the browser; how to use it is explained under [Software](software/cockpit.md).
- Course repository: link follows once it exists (knowledge base and the `AGENTS.md` for your assistant).

## Code and material

- [lifi-hardware](https://github.com/winf-hsos/lifi-hardware): the Python module `lifi_hardware` that talks to your device, with source code and readme.
- [lifi-concept-demos](https://github.com/winf-hsos/lifi-concept-demos): the source of the demonstrators below.
- [lifi-website](https://github.com/winf-hsos/lifi-website): the source of this website.
- [Device case](hardware/index.md#the-case): the OpenSCAD source and STL files of the 3D-printed case, CC0.

## Tools you install

- [Python](https://www.python.org/downloads/): the language you program in.
- [Git](https://git-scm.com/downloads): fetches the course material and the `lifi_hardware` module.
- [Visual Studio Code](https://code.visualstudio.com/): the editor.
- [OpenCode](https://opencode.ai/): your AI assistant, running in the terminal.
- [Tinkerforge downloads](https://www.tinkerforge.com/de/doc/Downloads.html): Brick Daemon and Brick Viewer for the hardware.
- [Tinkerforge documentation](https://www.tinkerforge.com/de/doc/): the raw API underneath `lifi_hardware`, for when you want to go one level deeper.

## Demonstrators

Small interactive pages, one idea each. The explanation lives on the concept page each one belongs to.

| Demonstrator | What you can do there | Concept |
|---|---|---|
| [The IPO Test Lab](https://winf-hsos.github.io/lifi-concept-demos/ipo-test-lab/) | change sensor values and the classification rule, then compare actual with expected output | [Problem Solving with Computers](concepts/input-processing-output.md) |
| [The Noisy Sensor](https://winf-hsos.github.io/lifi-concept-demos/noisy-sensor/) | send a symbol over a noisy link and let the same readings decide it three times: alone, averaged over five, averaged over ten | [Measuring and Experimenting](concepts/measurement-and-experiments.md) |
| [Question Game](https://winf-hsos.github.io/lifi-concept-demos/question-game/) | find the secret face; every answer is measured in bits | [Symbols and Information](concepts/symbols-and-information.md) |
| [The Copier](https://winf-hsos.github.io/lifi-concept-demos/copier/) | copy an analog picture until it fades, then compare with a file | [Analog and Digital](concepts/analog-and-digital.md) |
| [The Photo Digitiser](https://winf-hsos.github.io/lifi-concept-demos/photo-digitiser/) | choose resolution and colour depth, watch the bytes grow | [Analog and Digital](concepts/analog-and-digital.md) |
| [The Audio Digitiser](https://winf-hsos.github.io/lifi-concept-demos/audio-digitiser/) | the same two cuts for sound, and hear the difference | [Analog and Digital](concepts/analog-and-digital.md) |
| [Distinguishability Lab](https://winf-hsos.github.io/lifi-concept-demos/distinguishability-lab/) | send symbols over a noisy channel, trade error rate for throughput | [Signal und Rauschen](concepts/signal-and-noise.md) |
| [Drift Simulator](https://winf-hsos.github.io/lifi-concept-demos/drift-simulator/) | two clocks drift apart until the message breaks; a marker saves it | [Abtastung und Synchronisation](concepts/sampling-and-synchronization.md) |
| [Byte Switchboard](https://winf-hsos.github.io/lifi-concept-demos/byte-switchboard/) | flip eight bits, read the number in binary, decimal, hex and ASCII | [Zahlensysteme](concepts/number-systems.md) |
| [Pixel Painter](https://winf-hsos.github.io/lifi-concept-demos/pixel-painter/) | paint an 8×8 picture and watch its bytes write themselves | [Codesysteme](concepts/code-systems.md) |
| [Inside a File](https://winf-hsos.github.io/lifi-concept-demos/inside-a-file/) | a real bitmap in a hex editor; change a byte, watch the picture obey | [Memory and Storage](concepts/memory-and-storage.md) |
| [The Pixel Filter](https://winf-hsos.github.io/lifi-concept-demos/pixel-filter/) | make a photo brighter, one addition per pixel; step through the bits, then run all 16,384 | [Logik und Arithmetik](concepts/logic-and-arithmetic.md) |
| [The Gate Lab](https://winf-hsos.github.io/lifi-concept-demos/gate-lab/) | switches in, lamps out: gates, adders, a comparator, a flip-flop and a register | [Logik und Arithmetik](concepts/logic-and-arithmetic.md) |

## Background

- [Hochschule Osnabrück](https://www.hs-osnabrueck.de/): where this module is taught.
