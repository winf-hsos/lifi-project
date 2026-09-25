<!-- Lecture notes for the slides on `input-processing-output`, written in German. They follow the slides in order; frame numbers refer to the deck. The slides themselves are embedded on https://docs.lifi-project.de/concepts/input-processing-output.html -->

# Skript: Probleme lösen mit Computern

Dieses Skript begleitet den Input „Solving problems with computers“ in Sitzung 2. Es ist als eigenständiger Text lesbar und folgt der Reihenfolge des stagekit-Decks. Eine Folie mit Aufbau erscheint im Vortrag und Export als mehrere Frames; deshalb laufen die Verweise von Frame 1 bis Frame 41.

Das zugehörige Konzept auf der Website ist [Probleme lösen mit Computern](../../../website/concepts/input-processing-output.qmd).

## Worum es geht

Aus dem ersten Input wissen die Studierenden, wie ein großes Problem in prüfbare Teile zerlegt wird. Jetzt folgt die Anschlussfrage: Wie muss ein solches Teil aussehen, wenn ein Computer es lösen soll?

Die Antwort ist das IPO-Muster: Eingabe, Verarbeitung und Ausgabe. Es gilt für ein Logikgatter ebenso wie für eine Funktion oder ein ganzes System. Sind die Eingabe und die erwartete Ausgabe klar, lässt sich der Kasten testen. Programme beantworten dabei die Frage nach der Verarbeitung; die Darstellung der Daten ist eine zweite, eigenständige Frage.

## Teil 1: Was passiert in der Mitte?

### Das unsichtbare Dazwischen (Frames 1 bis 4)

Der Einstieg zeigt ein Bestellterminal in einem Restaurant. Vorn geben wir eine Bestellung ein, hinten erscheint später ein Tablett. Die Küche dazwischen bleibt unsichtbar. Für die Bestellung genügt es trotzdem, die Eingabe und die erwartete Ausgabe zu kennen.

Das Terminal deutet zugleich eine zweite Frage an: Wir sprechen unsere Bestellung nicht einfach in den Raum. Wir wählen Kacheln, Mengen und Optionen. Noch bevor die Küche arbeitet, ist die Bestellung in eine Form gebracht, die das System verarbeiten kann. Diese Darstellungsfrage kehrt am Ende des Inputs wieder.

### Die Form eines lösbaren Teils (Frames 5 bis 8)

Ein für den Computer lösbares Teil hat immer dieselbe Gestalt. Vorn gehen Daten hinein: die Eingabe. Hinten kommen Daten heraus: die Ausgabe. Dazwischen liegt die Verarbeitung. Auf Englisch heißen die drei Teile Input, Processing und Output, kurz IPO.

Der Kasten ist kein bestimmtes Gerät. Er ist eine Denkform. Wir können damit einen Taschenrechner, eine Python-Funktion, einen Sensor, einen Sender oder ein ganzes Übertragungssystem beschreiben. Entscheidend sind zunächst nicht die technischen Einzelheiten, sondern die Grenzen des Kastens: Was geht wirklich hinein, und was soll wirklich herauskommen?

### Der eingebaute Test (Frames 9 bis 12)

Ein kleines Beispiel macht die Verbindung zur Zerlegung aus Sitzung 1 sichtbar. Die Funktion `add()` bekommt `2, 3` und soll `5` liefern. Damit ist bereits ein Test formuliert:

1. Gib `2, 3` hinein.
2. Führe die Verarbeitung aus.
3. Vergleiche die tatsächliche Ausgabe mit der erwarteten `5`.

Liefert der Kasten `5`, besteht der Test. Liefert er `6`, schlägt er fehl. Um das festzustellen, müssen wir noch nicht wissen, wie `add()` im Inneren arbeitet. Klare Eingaben und erwartete Ausgaben machen einen Kasten prüfbar.

Der Merksatz lautet: Wer Eingabe und erwartete Ausgabe kennt, hat einen Test.

## Teil 2: Die Kästen in unserem Projekt

### Der Sender (Frames 13 und 14)

Der Sender der Lichtstrecke ist ein IPO-Kasten. Eine Nachricht wie `"hi"` geht hinein. `encode()` verarbeitet den Text. Eine Folge von Farbsymbolen kommt heraus.

Die Grenzen sind wichtig: Vor `encode()` liegen Zeichen, danach liegen Farbsymbole. Welche Farbe welche Bedeutung trägt, ist keine Naturtatsache. Sie ist eine Vereinbarung im Team. Erst diese Vereinbarung macht die Ausgabe des Senders für den nächsten Teil verständlich.

### Was sieht der Empfänger wirklich? (Frames 15 und 16)

Beim Empfänger scheint zunächst rotes Licht hineinzugehen und der Text `"red"` herauszukommen. Für den Computer geht jedoch kein Begriff „Rot“ hinein. Der Sensor liefert Messwerte, zum Beispiel:

`r = 203, g = 41, b = 57, c = 310`

Die ersten drei Zahlen stehen für gemessene Rot-, Grün- und Blauanteile, die vierte für die Gesamthelligkeit. Was diese Zahlen bedeuten, entscheidet die Verarbeitung `classify()`. Unsere Augen sehen Rot. Der Kasten sieht vier Zahlen.

### Der interaktive IPO-Test (Frame 17)

Der Demonstrator zeigt den Empfänger als veränderbaren IPO-Kasten. Links lassen sich die vier Sensorwerte einstellen. In der Mitte stehen zwei Entscheidungsgrenzen:

- Unterhalb einer Mindesthelligkeit lautet die Ausgabe `off`.
- Liegen die beiden stärksten Farbkanäle zu dicht beieinander, lautet sie `uncertain`.
- Andernfalls gewinnt der stärkste Farbkanal.

Rechts stehen tatsächliche und erwartete Ausgabe. Stimmen sie überein, besteht der Test; andernfalls schlägt er fehl.

Mit dem Preset „clear red“ beginnt ein eindeutiger Erfolgsfall. Bei „weak red“ lässt sich die Helligkeit so weit absenken, dass dieselben relativen Farbanteile als `off` gelten. „Mixed light“ zeigt, dass eine veränderte Entscheidungsgrenze bei unveränderten Messwerten eine andere Ausgabe erzeugen kann. So werden Eingabe, Verarbeitung, Ausgabe und Test unmittelbar erfahrbar.

### Kästen lassen sich stecken (Frames 18 bis 20)

Die Ausgabe eines Kastens kann zur Eingabe des nächsten werden. Die gesamte Strecke lässt sich als Kette lesen:

`"hi" → encode() → Farbsymbole → Licht → decode() → "hi"`

An jeder Steckstelle muss die Form und Bedeutung der Daten vereinbart sein. Ein Teil kann für sich korrekt arbeiten und die Gesamtstrecke trotzdem scheitern, wenn zwei benachbarte Kästen an ihrer Grenze Unterschiedliches erwarten.

Kästen hintereinander zeigen den Datenfluss. Diese Sicht gibt auch eine Debugging-Route vor: Wenn hinten nicht `"hi"` ankommt, folgen wir den Daten von Grenze zu Grenze. Wir prüfen den erzeugten Code, die LED, die Sensorwerte und schließlich `decode()`. Die Leitfrage lautet: Bis zu welcher Grenze sind die Daten noch richtig?

Der Merksatz in Frame 21 ist deshalb: Um den Fehler zu finden, folge den Daten und teste eine Grenze nach der anderen.

## Teil 3: Kästen auf jeder Ebene

### Einen Kasten öffnen (Frames 22 bis 25)

Von außen kann der ganze Sender als ein Kasten betrachtet werden. Eine Nachricht geht hinein, Licht kommt heraus, und `send()` bezeichnet die gesamte Verarbeitung.

Öffnen wir diesen Kasten, wird seine Verarbeitung zu einer Kette kleinerer Kästen: Text codieren, ein Farbsymbol auswählen und die LED ansteuern. Jeder kleine Kasten besitzt wiederum eigene Eingaben und Ausgaben und kann separat geprüft werden.

Wie weit wir einen Kasten öffnen, hängt von unserer Frage ab. Wer die gesamte Strecke testet, braucht andere Ein- und Ausgaben als jemand, der nur `encode()` oder die LED-Ansteuerung untersucht. Wir öffnen einen Kasten nur so weit, wie es die aktuelle Frage erfordert.

### Dieselbe Form auf drei Ebenen (Frames 26 bis 28)

Das IPO-Muster bleibt über die Ebenen hinweg erhalten:

- System: Nachricht hinein, Sender arbeitet, Licht heraus.
- Funktion: Text hinein, `encode()` arbeitet, Symbole heraus.
- Logikgatter: `1, 1` hinein, die UND-Regel wird angewendet, `1` heraus.

Die Auflösung ändert sich, die Form nicht. Deshalb kann IPO sehr unterschiedliche technische Gegenstände miteinander verbinden, ohne ihre Unterschiede zu verwischen.

### Kette und Verschachtelung (Frame 29)

Es gibt zwei Beziehungen zwischen Kästen, die nicht verwechselt werden dürfen:

- Kästen hintereinander zeigen Datenfluss: Wohin gehen die Daten als Nächstes?
- Kästen ineinander zeigen hierarchische Zerlegung: Welche kleinere Arbeit passiert im Inneren?

Beide Sichten sind nützlich. Die passende Sicht hängt von der Frage ab. Die passende Ebene ist diejenige, auf der sich eine klare Eingabe und erwartete Ausgabe angeben lassen. Frame 30 fasst das zusammen: Die richtige Ebene ist die, die wir testen können.

## Teil 4: Zwei Fragen in jedem Kasten

### Verarbeitung und Darstellung (Frames 31 bis 35)

Aus jedem IPO-Kasten entstehen zwei Grundfragen.

Die erste lautet: Wie arbeitet der Kasten? Das ist die Frage nach der Verarbeitung. Ihre Antwort heißt Programm. Im nächsten Input wird diese Antwort genauer untersucht.

Die zweite lautet: Wie schreiben wir Dinge so auf, dass eine Maschine damit arbeiten kann? Das ist die Frage nach der Darstellung von Eingaben und Ausgaben. Der Sensorfall hat sie bereits gezeigt: „Rot“ musste zu vier Zahlen werden, bevor ein Programm damit arbeiten konnte.

Fast alle weiteren Konzepte des Moduls lassen sich an einer dieser beiden Fragen verorten.

### Die Landkarte der nächsten Wochen (Frame 36)

Die Verarbeitungsfrage führt direkt zu „Algorithmen und Programme“. Die Darstellungsfrage führt zunächst zu Messwerten, anschließend zu Symbolen und Information, Codesystemen und Zahlensystemen. Der IPO-Kasten bleibt dabei als Landkarte bestehen. Nur die Stelle, in die wir hineinzoomen, wechselt.

### Auch ein KI-Agent ist ein Kasten (Frames 37 bis 40)

Ein KI-Agent kann ebenfalls als IPO-Kasten betrachtet werden. Eine Aufgabe geht hinein, Code kommt heraus. Das Innere dieses Kastens ist schwer einzusehen. Gerade deshalb sind klare Beispiele und erwartete Ergebnisse wichtig.

Eine präzise Eingabe verbessert den Auftrag. Eine erwartete Ausgabe liefert den Maßstab. Erst der Vergleich zwischen tatsächlichem und erwartetem Ergebnis entscheidet, ob der Vorschlag verwendbar ist. Prüfbarkeit ersetzt Vertrauen nicht nur bei einfachen Funktionen, sondern gerade bei schwer durchschaubaren Systemen.

### Übergang zum nächsten Input (Frame 41)

Das Schlussbild zeigt die Küchenausgabe aus der Eröffnungsgeschichte. Am Anfang standen wir vor der geschlossenen Tür und kannten nur Bestellung und Tablett. Jetzt kennen wir die Form jedes computergestützt lösbaren Teils und wissen, wie seine Grenzen einen Test ermöglichen.

Als Nächstes öffnen wir den mittleren Kasten. Die Verarbeitung darin heißt Programm.
