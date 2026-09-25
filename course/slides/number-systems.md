<!-- Lecture notes for the slides on `number-systems`, written in German. They follow the slides in order; frame numbers refer to the deck. The slides themselves are embedded on https://docs.lifi-project.de/concepts/number-systems.html -->

# Skript: why ten?

Dieser Text erläutert den Input zum Konzept „Zahlensysteme" zum Nachlesen. Er folgt der Reihenfolge der Folien, die Verweise zählen Frames (jeder Aufbauschritt ist ein eigener Frame), lässt sich aber auch ohne die Folien lesen.

Der Satz ist der erste von zwei Inputs derselben Sitzung; der zweite, [Codesysteme](../08-code-systems/skript.md), beantwortet die Frage, was die Zahlen bedeuten, die hier entstehen.

Ein Schema trägt den ganzen Input: oben die Ziffern, darunter die Stellenwerte, unten die Summe. Es kommt dreimal, mit Basis 10, Basis 8 und Basis 2, und danach noch zweimal, mit Basis 16 und mit euren Farben. Wer es einmal gesehen hat, liest jede Basis, ohne eine neue Regel zu lernen.

## Warum zählen wir bis zehn? (Frame 4)

Fragt einmal in die Runde, warum unser Zahlensystem gerade zehn Ziffern hat. Die Antworten fallen meist ehrfürchtig aus: weil es sich gut teilen lässt, weil es mathematisch praktisch ist, weil es so gewachsen ist.

Die richtige Antwort ist banaler. Wir haben zehn Finger. Das ist alles. Es steckt keine Naturkonstante darin und keine besondere Eigenschaft der Zehn, nur Anatomie.

Das ist der Aufhänger für alles Weitere. Wenn die Zehn ein Zufall ist, dann geht es auch anders, und alles, was uns an unserer Zahlschreibweise selbstverständlich vorkommt, zerfällt in zwei Teile: den einen, der reine Vereinbarung ist, und den anderen, der Mathematik ist und in jedem System gleich funktioniert.

## Was bei 123 wirklich dasteht (Frames 5 und 6)

Nehmt die Zahl 123. Was steht da eigentlich?

Nicht „eins, zwei, drei". Da steht: einmal hundert, zweimal zehn, dreimal eins. Jede Stelle trägt eine Zehnerpotenz, und die Ziffer sagt nur, wie oft diese Potenz vorkommt.

    1 · 100  +  2 · 10  +  3 · 1  =  123

Das weiß jeder, aber kaum jemand hat es je so hingeschrieben. Genau diese Bauanleitung heißt **Stellenwertsystem**, und sie ist der einzige Grund, warum zehn Ziffern für unendlich viele Zahlen reichen: Statt für jede Zahl ein neues Zeichen zu erfinden, gibt man der Position eine Bedeutung.

## Das Achtfinger-Wesen schreibt 123 (Frames 7 und 8)

Jetzt stellt euch ein Wesen mit acht Fingern vor. Es hat dasselbe Verfahren erfunden, nur zählt es bis acht, bevor die Stelle überläuft. Es schreibt ebenfalls `123` auf ein Blatt.

Welche Zahl meint es? Rechnet mit, bevor ihr weiterlest.

Dasselbe Schema, nur Achterpotenzen statt Zehnerpotenzen: 64, 8, 1.

    1 · 64  +  2 · 8  +  3 · 1  =  83

Dieselben drei Ziffern, dasselbe Verfahren, eine andere Zahl. Daraus folgt etwas, das den Rest der Sitzung trägt: Eine Ziffernfolge allein bedeutet gar nichts, solange die Basis nicht dabeisteht.

## Zwei Flossen: binär zählen (Frames 9 und 10)

Der Delfin auf Frame 9 hat zwei Flossen. Sein Zahlensystem kennt also genau zwei Ziffern, 0 und 1, und das ist der Trick am Anschlag.

| wir | der Delfin |
| --- | ---------- |
| 0 | 0 |
| 1 | 1 |
| 2 | 10 |
| 3 | 11 |
| 4 | 100 |
| 5 | 101 |
| 6 | 110 |
| 7 | 111 |
| 8 | 1000 |

Zählt gemeinsam mit. Beim Übergang von 1 auf 10 stutzen die meisten kurz, und dann fällt der Groschen: Das ist genau dasselbe, was bei uns zwischen 9 und 10 passiert. Die Ziffern sind aufgebraucht, also wird eine neue Stelle geöffnet. Nur passiert es bei zwei Ziffern eben ständig, und die Zahlen werden schnell lang.

## Der Delfin schreibt 110 (Frames 11 und 12)

Das Schema zum dritten Mal, und jetzt sitzt es. Zweierpotenzen: 4, 2, 1.

    1 · 4  +  1 · 2  +  0 · 1  =  6

`110` ist keine hundertzehn. Wer bis hierher mitgekommen ist, kann jede Basis lesen, denn es gibt keine neue Regel mehr. Es ist immer dasselbe: Ziffer mal Stellenwert, aufsummiert.

## Warum ausgerechnet zwei? (Frames 14 und 15)

Ein Rechner könnte im Prinzip jede Basis benutzen. Dezimalrechner hat es wirklich gegeben, sie sind ausgestorben. Warum?

Die Antwort ist keine Mathematik, sondern Technik. Stellt euch eine Leitung vor, auf der eine Spannung zwischen null und fünf Volt liegt. Wollt ihr zehn Ziffern übertragen, müsst ihr diesen Bereich in zehn Fächer schneiden, und jedes Fach ist ein halbes Volt breit. Wollt ihr zwei Ziffern übertragen, gibt es zwei Fächer von zweieinhalb Volt.

Nun wackelt jede echte Leitung. Kabel wirken als Antennen, Bauteile werden warm, Netzteile brummen. Derselbe Wackler, der bei zwei Fächern nie etwas ausmacht, wirft bei zehn Fächern die Ziffer regelmäßig ins Nachbarfach. Das ist die Messfolie aus „Analog und digital", von der anderen Seite gelesen: Je mehr Zustände in denselben Bereich passen sollen, desto kleiner die Abstände, desto eher gewinnt das Rauschen.

Zwei Zustände sind das Billigste, was sich zuverlässig bauen lässt. An und aus, Strom und kein Strom, hell und dunkel. Der Preis dafür sind mehr Stellen, und Stellen sind billig.

## Acht Bit sind ein Byte (Frames 16 bis 18)

Dasselbe Schema mit acht Stellen. Die Stellenwerte sind 128, 64, 32, 16, 8, 4, 2, 1, jede Stelle das Doppelte der rechten Nachbarin.

    0 1 0 0 0 0 0 1   →   64 + 1 = 65

Acht Stellen mit je zwei Möglichkeiten ergeben 2⁸ gleich 256 Werte, als Zahl gelesen 0 bis 255. Deshalb laufen die Farbkanäle eurer LED von 0 bis 255: Ein Kanal ist genau ein Byte.

Das Wort **Bit** kennt ihr aus Sitzung 4 als Informationsmaß, und hier taucht es als Ziffer wieder auf, als *binary digit*. Das ist kein Zufall und kein Wortspiel: Eine Stelle mit zwei möglichen Werten fasst genau eine Ja/Nein-Antwort. Der Behälter ist nach seinem Inhalt benannt. Nützlich bleibt die Unterscheidung trotzdem, denn ein Behälter kann auch halb leer sein; darauf kommt die Kompression zurück.

Zum Selbstausprobieren gibt es das [Byte Switchboard](https://winf-hsos.github.io/lifi-concept-demos/byte-switchboard/): acht Schalter, die Zahl läuft mit. Drei Fragen lohnen sich dort: Welcher Schalter ändert am meisten? Wie stellt man 255 ein, wie die 1? Und was passiert, wenn man von 255 aus noch eins weiterzählen will?

## Hexadezimal: vier Bit auf einmal (Frames 20 bis 23)

Acht Nullen und Einsen kann kein Mensch auf einen Blick lesen. Dafür gibt es eine Abkürzung, und sie ist kein neues Zahlensystem im eigentlichen Sinn, sondern dasselbe Schema zur Basis 16.

Der Grund für gerade sechzehn liegt im Byte. Vier Bit haben 2⁴ gleich 16 Zustände, und 16 ist genau die Zahl der Hexziffern. Also passt eine Hexziffer auf ein Viererpäckchen, und ein ganzes Byte auf zwei Ziffern:

    1101 0010   →   D2

Weil unsere zehn Ziffern für sechzehn Werte nicht reichen, borgt man sich sechs Buchstaben: A steht für 10, B für 11, und so weiter bis F für 15. Wer diese Tabelle einmal gesehen hat, liest jeden Hex-Dump.

Genau so ein Dump steckt im Demonstrator [Inside a File](https://winf-hsos.github.io/lifi-concept-demos/inside-a-file/): links die Bytes einer echten Datei hexadezimal, rechts dieselben Bytes als Zeichen. Zwei Dinge sind dort zu sehen. Erstens verraten schon die ersten Bytes, um welche Art Datei es sich handelt. Zweitens stehen zwischen den lesbaren Stellen genauso viele unlesbare, und beide sind derselbe Stoff. Eine Datei ist nichts anderes als eine Folge von Zahlen.

Und damit wird auch die Farbschreibweise `#AC8909` nachrechenbar: drei Bytes, je zwei Hexstellen, ein Byte je Farbkanal.

## Zwei Leitern von Einheiten (Frame 24)

Bevor das berühmte Festplattenrätsel kommt, zwei Leitern nebeneinander.

Die dezimale Leiter nimmt je Sprosse den Faktor 1000: Kilobyte, Megabyte, Gigabyte, Terabyte. Die binäre Leiter nimmt 1024, denn Speicher ist in Zweierpotenzen organisiert und 2¹⁰ gleich 1024 ist die nächstgelegene runde Binärzahl zur 1000.

| Stufe | dezimal | binär |
| ----- | ------- | ----- |
| Byte | 1 | 1 |
| Kilo | 1 000 | 1 024 |
| Mega | 1 000 000 | 1 048 576 |
| Giga | 1 000 000 000 | 1 073 741 824 |
| Tera | 1 000 000 000 000 | 1 099 511 627 776 |

Im Alltag heißen beide Leitern gleich. Wer es genau nimmt, sagt Kibibyte, Mebibyte, Gibibyte zur binären Sprosse, aber das tut fast niemand, und daraus entsteht das Rätsel auf der nächsten Folie.

## Die fehlenden 69 Gigabyte (Frames 25 und 26)

Auf der Packung steht 1 Terabyte. Ihr baut die Platte ein, der Rechner zeigt 931 Gigabyte. Wer schummelt hier?

Ratet erst, bevor ihr weiterlest.

Niemand schummelt. Der Hersteller zählt die dezimale Leiter hinauf, ein Terabyte sind für ihn eine Billion Bytes. Das Betriebssystem nimmt genau dieselbe Billion Bytes und teilt sie die binäre Leiter hinunter, durch 1024³, und landet bei 931. Es fehlt kein einziges Byte. Über vier Sprossen summiert sich der Unterschied auf rund sieben Prozent, und beide Seiten nennen ihre Sprosse Gigabyte.

Das ist kein Betrug, sondern ein Wortproblem.

## Ihr habt längst eins gebaut (Frames 28 bis 30)

Und damit zur Pointe. Euer Farbalphabet ist ein Stellenwertsystem, und die Zahl eurer Farben ist die Basis.

Wer vier Farben sicher unterscheidet, arbeitet zur Basis 4. Legt fest, welche Farbe welche Ziffer ist, etwa Rot gleich 0, Grün gleich 1, Blau gleich 2, Gelb gleich 3. Dann ist die Farbfolge Rot-Gelb-Grün die Zahl

    0 · 16  +  3 · 4  +  1 · 1  =  13

und mit drei Stellen stehen 4³ gleich 64 Kombinationen zur Verfügung, genug für ein Alphabet aus 26 Buchstaben.

Zwei Dinge folgen daraus für Challenge 1. Erstens ist die Reihenfolge Teil der Nachricht: Rot-Gelb-Grün und Grün-Gelb-Rot sind verschiedene Codewörter, aus genau demselben Grund, aus dem 123 und 321 verschiedene Zahlen sind. Zweitens geht die Rechnung in beide Richtungen. Wer weiß, wie viele Zeichen er unterscheiden muss, kann ausrechnen, wie viele Stellen er dafür braucht, und wer sich für eine Zahl von Farben entscheidet, weiß sofort, wie lang seine Codewörter werden.

## Die Zehn war nie besonders (Frames 31 und 32)

Der Schlusssatz ist der Anfangssatz von der anderen Seite. Die Zehn ist die Zahl der Finger an zwei Händen, und sonst nichts.

Wer das einmal gesehen hat, hält keine Basis mehr für natürlich und keine für schwierig. Binär, hexadezimal und euer Farbsystem sind dasselbe Verfahren mit anderen Ziffern.
