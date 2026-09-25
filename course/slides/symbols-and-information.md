<!-- Lecture notes for the slides on `symbols-and-information`, written in German. They follow the slides in order; frame numbers refer to the deck. The slides themselves are embedded on https://docs.lifi-project.de/concepts/symbols-and-information.html -->

# Skript: what light means

Dieser Text erläutert den Input zum Konzept „Symbole und Information" zum Nachlesen. Er folgt der Reihenfolge der Folien, die Verweise zählen Frames (jeder Aufbauschritt ist ein eigener Frame), lässt sich aber auch ohne die Folien lesen.

Der Satz ist der zweite von zwei Inputs derselben Sitzung; der erste, [drawing the line](../05-analog-and-digital/skript.md), klärt, was digital überhaupt heißt und wo die Grenzen zwischen den Zuständen liegen.

## Was macht Licht bedeutsam? (Frame 4)

Nordatlantik, 1942. Funkstille, weil Funksprüche den Gegner anziehen. Zwei Schiffe sprechen trotzdem miteinander: eine Lampe, eine Klappe davor, kurz kurz kurz lang.

Das Licht selbst weiß nichts. Es bedeutet nur deshalb etwas, weil beide Seiten dieselbe Tabelle im Kopf haben.

## Ein Symbol ist ein vereinbarter, unterscheidbarer Zustand (Frames 5 bis 7)

Beide Wörter tragen.

**Unterscheidbar** ist eine Frage an die Physik und an euren Sensor: Kann der Empfänger diesen Zustand von allen anderen trennen? Darum ging es im ersten Input dieser Sitzung.

**Vereinbart** ist eine Frage an euch beide: Haben Sender und Empfänger demselben Zustand dieselbe Bedeutung gegeben, und zwar vorher? Diese Frage kann keine Messung beantworten.

## Perfekter Empfang, perfekter Unsinn (Frames 8 und 9)

Zwei Freiwillige bekommen heimlich abweichende Zuordnungstabellen. Der Sender schickt vier Farben, alle vier kommen fehlerfrei an, und der Empfänger liest ein völlig anderes Wort.

Kein Übertragungsfehler, keine Störung, keine schlechte Messung. Trotzdem ist die Nachricht wertlos, weil die Vereinbarung fehlte. Genau deshalb steht in der Definition „vereinbart" gleichberechtigt neben „unterscheidbar".

## Die Vereinbarung, aufgeschrieben (Frame 10)

Als Code ist die Vereinbarung ein Wörterbuch:

```python
ALPHABET = {
    "red":    "00",
    "green":  "01",
    "blue":   "10",
    "yellow": "11",
}
```

Diese Tabelle wird nie übertragen. Sie muss vorher bei beiden liegen, und sie ist damit keine Daten, sondern ein Versprechen. Wer sie ändert, ohne es dem Partner zu sagen, baut die Unsinn-Folie nach.

## Das Kartenraten, gemessen (Frames 12 bis 14)

Eine von 32 Karten ist gezogen, erlaubt sind nur Ja/Nein-Fragen. Wer immer halbiert, ist nach fünf Fragen fertig: 32, 16, 8, 4, 2, 1.

Fünf, und zwar in jedem Fall, nicht im Glücksfall. Diese Zahl der nötigen Halbierungen ist das Maß, um das es in diesem Teil geht.

## Nicht jede Antwort ist ein Bit wert (Frame 15)

Die Gegenprobe. „Ist es das Pik-Ass?" kann alles auf einmal auflösen, tut das aber nur in einem von 32 Fällen. In den anderen 31 bleibt fast alles übrig.

Die halbierende Frage dagegen liefert immer dasselbe Ergebnis: genau eine Halbierung, egal wie die Antwort ausfällt. **Ihr könnt euch nicht aussuchen, welche Antwort ihr bekommt**, und deshalb zählt nicht der beste Fall, sondern der Durchschnitt.

## Was eine Frage im Schnitt wert ist (Frame 16)

| Frage | Antwort | Chance | ihr lernt | im Schnitt |
| --- | --- | --- | --- | --- |
| „ist sie rot?" | ja | 1/2 | 1 Bit | 1 Bit |
| | nein | 1/2 | 1 Bit | |
| „ist es das Pik-Ass?" | ja | 1/32 | 5 Bit | 0,2 Bit |
| | nein | 31/32 | 0,05 Bit | |

Eine seltene Antwort trägt viel, eine erwartbare wenig. Weil die seltene Antwort aber selten ist, gewinnt im Durchschnitt die Frage, deren Ausgang offen ist. Die schiefe Frage lohnt sich erst ganz am Ende, wenn nur noch zwei Möglichkeiten übrig sind.

## Und allgemein (Frames 17 und 18)

Dieselbe Rechnung, nur ohne die konkreten Zahlen. Jede mögliche Antwort steuert zwei Dinge bei: wie wahrscheinlich sie ist, und was sie wert wäre. Beides multipliziert und über alle Antworten addiert ergibt den **Erwartungswert** einer Frage:

`E = Σ pᵢ · log₂(1/pᵢ)`

Dabei ist `pᵢ` die Wahrscheinlichkeit einer Antwort und `log₂(1/pᵢ)` das, was diese Antwort wert wäre: Je unwahrscheinlicher sie ist, desto mehr trägt sie. Für eine Ja/Nein-Frage sind das genau zwei Summanden, für eine Frage mit mehr Ausgängen entsprechend mehr.

Eingesetzt ergeben sich die beiden Zeilen von vorhin: `0,5 · 1 + 0,5 · 1 = 1` Bit für die halbierende Frage, `0,03 · 5 + 0,97 · 0,05 = 0,2` Bit für die schiefe. **Ein ganzes Bit bekommt nur, wer wirklich halbiert**, und das gilt unabhängig davon, wie das Spiel diesmal ausgeht.

## Ein Bit, und zwei Formeln (Frames 19 und 20)

Ein **Bit** ist die Informationsmenge einer Entscheidung zwischen zwei gleich wahrscheinlichen Möglichkeiten. Ein Lichtschalter trägt eines, und kein Computer ist dafür nötig.

Damit lassen sich beide Größen aufschreiben, in dieser Reihenfolge:

**Unsicherheit:** `H = log₂(N)` bei N gleich wahrscheinlichen Möglichkeiten. Sie misst, wie viele Halbierungen noch fehlen.

**Information:** `I = H₁ − H₂`, Unsicherheit vorher minus Unsicherheit nachher. Sie misst, was eine Antwort tatsächlich beseitigt hat.

Die 32 Karten sind **nicht** die Unsicherheit, sie sind der Raum der Möglichkeiten. Die Unsicherheit sind die 5 Bit. Eine halbierende Frage senkt H um genau 1, ihre Antwort ist also 1 Bit wert.

## Selbst ausprobieren (Frame 21)

Im [Question Game](https://winf-hsos.github.io/lifi-concept-demos/question-game/) ist eines von sechzehn Gesichtern gesucht. Nach jeder Frage rechnet die Demo vor, was sie wert war, und zeigt vorher an, was sie im Erwartungswert bringt.

Zwei Runden lohnen sich: einmal absichtlich raten, einmal halbieren. Der Unterschied steht danach in Bit auf dem Schirm.

## Was ein größeres Alphabet einbringt (Frames 22 bis 24)

Dasselbe Werkzeug, jetzt auf euer Alphabet angewendet. Ein Symbol aus N gleich wahrscheinlichen Möglichkeiten trägt `log₂(N)` Bit: zwei Farben ein Bit, vier Farben zwei, acht Farben drei, sechzehn Farben vier.

Weil dieselbe Datei damit weniger Symbole braucht, ist sie schneller durch. Bei gleicher Symbolrate braucht sie mit acht Farben nur noch ein Drittel der Zeit, die sie mit zwei Farben brauchte.

## Zwei Symbole genügen für alles (Frame 25)

Was ein großes Alphabet je Symbol leistet, leisten zwei Symbole in der Gruppe. Fünf Blitze mit je zwei Möglichkeiten ergeben `2⁵ = 32` Kombinationen, genug für ein ganzes Alphabet.

Genau deshalb kommt jeder Computer mit null und eins aus, und genau deshalb ist ein kleines Alphabet keine Sackgasse, sondern nur langsamer.

## Wenn Symbole nicht gleich wahrscheinlich sind (Frame 26)

Bisher galten alle Symbole als gleich wahrscheinlich. In echtem Text sind sie das nicht, und Morse nutzt das aus: Das häufigste Zeichen, das „e", bekommt den kürzesten Code, einen einzelnen Punkt. Seltene Zeichen wie das „q" sind lang.

Das lohnt sich, weil die durchschnittliche Nachricht dadurch kürzer wird. Auf dieser Beobachtung beruht jede Kompression, und darauf kommen wir zurück.

## Der Haken (Frame 28)

Links der Gewinn: mehr Bit je Symbol, dieselbe Datei mit weniger Symbolen, früher fertig. Rechts der Preis: Die Farben rücken enger zusammen, das Rauschen reicht über den Abstand, und Symbole werden falsch gelesen.

Wo die Grenze liegt, verrät keine Formel. Die Größe eures Alphabets ist keine Geschmacksfrage, sie ist eine Messung. Die andere Hälfte davon steht bei [Signal und Rauschen](../../../website/concepts/signal-and-noise.qmd).

## In der Werkstatt (Frame 29)

Vier Schritte, und der erste ist der, den alle überspringen wollen:

1. das Alphabet vereinbaren **und aufschreiben**
2. für jedes Symbol einen Steckbrief messen
3. `send_symbol()` und `receive_symbol()` füllen
4. ein ganzes Wort durchlaufen lassen und die Fehler zählen

## Zum Schluss (Frames 30 und 31)

Licht bedeutet nichts, bis ihr vereinbart, was es bedeutet. Und wie viel es bedeutet, könnt ihr zählen.
