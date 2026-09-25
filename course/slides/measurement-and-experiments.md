<!-- Lecture notes for the slides on `measurement-and-experiments`, written in German. They follow the slides in order; frame numbers refer to the deck. The slides themselves are embedded on https://docs.lifi-project.de/concepts/measurement-and-experiments.html -->

# Skript: Messen und Experimentieren

Dieses Skript begleitet den Stagekit-Foliensatz „Measuring and Experimenting“ für Sitzung 3 im Modul „Digitalisierung und Programmierung“. Die Folien sind englisch, das Skript erläutert die Inhalte auf Deutsch. Aufbauschritte zählen im Player und im Export als eigene Frames; die Verweise beziehen sich deshalb auf Frames.

Die Kernbotschaft lautet: Eine einzelne Ablesung ist noch kein Beleg. Wissen entsteht erst aus einer kontrollierten Messreihe: Erwartung vorher festhalten, genau eine Größe verändern, wiederholen und alle Ergebnisse dokumentieren.

## 1. Measuring settles it

### Welche Kugel landet zuerst? (Frame 4)

Zweitausend Jahre lang klang Aristoteles plausibel: Schwere Körper müssten schneller fallen als leichte. Der Legende nach ließ Galileo zwei unterschiedlich schwere Kugeln vom Schiefen Turm von Pisa fallen. Beide kamen zugleich an. Eine Messung entschied damit, was Nachdenken und Autorität nicht entscheiden konnten.

Das Bild überträgt sich direkt auf das Semester. Der KI-Assistent kennt Sensoren dieser Art und kann gute Begründungen liefern. Er kennt aber nicht den konkreten Aufbau auf dem Tisch. Dieser Aufbau ist unser Turm, und eine Messreihe ist der Fallversuch.

### Drei Arten, dieselbe Frage zu beantworten (Frames 5–7)

Eine plausible Erklärung sagt, warum etwas gelten könnte. Eine KI-Prognose kann die Behauptung sogar mit konkreten Zahlen oder einer Handlungsanweisung versehen. Beides bleibt eine Behauptung. Erst die Messreihe am eigenen Aufbau liefert Evidenz darüber, ob und wie stark der Effekt tatsächlich auftritt.

Das Beispiel ist die Integrationszeit. „Längere Messungen sammeln mehr Licht“ klingt vernünftig. „Verdoppelt die Integrationszeit, dann verbessert sich die Erkennung“ ist eine klare Prognose. Ob die Erkennungsrate bei diesem Aufbau wirklich von 41 auf 47 richtige Erkennungen steigt, entscheidet nur der Versuch.

### Aus einer Behauptung wird ein Test (Frames 8–11)

Ein Experiment beginnt mit einer Frage. Daraus folgt eine Vorhersage, die vor der Messung notiert wird. Dann wird unter kontrollierten Bedingungen gemessen. Zum Schluss wird das Ergebnis mit der Vorhersage verglichen: Die Behauptung wird unterstützt oder widerlegt.

Die Reihenfolge ist entscheidend. Wer erst misst und danach festlegt, welches Ergebnis als Erfolg gelten soll, kann fast jedes Resultat passend deuten. Eine vorher festgehaltene Erwartung schützt davor, die eigene Hoffnung nachträglich in die Daten hineinzulesen.

## 2. Know what you measure

### Heute arbeiten wir an der Eingabe (Frame 13)

Im vorherigen Input war der Empfänger ein Kasten nach dem IPO-Muster: Licht geht hinein, `classify()` verarbeitet die Eingabe, ein Farbname kommt heraus. Nun zoomen wir in die Eingabeseite. Für unsere Augen fällt rotes Licht auf den Sensor. Für das Programm kommt dort kein Begriff „Rot“ an, sondern eine Messung.

### Vier Zahlen statt einer Farbe (Frames 14–16)

Der Farbsensor liefert vier Werte. Drei Kanäle messen durch rote, grüne und blaue Filter. Der vierte Kanal heißt Clear und misst ohne Farbfilter das gesamte einfallende Licht. Dadurch reagiert Clear besonders empfindlich auf Hell und Dunkel.

Die vier Zahlen `r`, `g`, `b` und `c` sind die tatsächliche Eingabe des Programms. Erst eine Verarbeitung macht daraus die Ausgabe `"red"`, `"blue"` oder einen anderen Symbolnamen. Genau diese Trennung verhindert die Fehlvorstellung, ein Sensor liefere bereits die Bedeutung des gemessenen Signals.

### Gesendet ist nicht gemessen (Frame 17)

Wer die LED auf `r=255, g=0, b=0` setzt, erwartet leicht dieselben Zahlen am Sensor. Tatsächlich kann dort etwa `r=203, g=41, b=57, c=310` ankommen. Das ist kein Defekt, sondern der Normalfall.

Die Farbfilter überlappen. Licht verliert sich mit Abstand und Winkel. Das Raumlicht gelangt ebenfalls zum Sensor. Eine Formel, die die Messwerte heute genau auf die LED-Werte zurückrechnet, wäre am nächsten Tisch oder am nächsten Tag bereits falsch. Wir müssen lernen, mit den Messwerten unseres Aufbaus zu arbeiten.

### Zuerst die Dunkelheit messen (Frames 18–21)

Der Sensor zeigt auch bei ausgeschalteter eigener LED nicht Null. Raumlicht ist immer vorhanden. Deshalb beginnt jede Messreihe mit einer Kontrollmessung bei ausgeschalteter LED. Sie liefert die Grundlinie, gegen die alle späteren Werte gelesen werden.

Der gemessene Wert lässt sich gedanklich in drei Beiträge zerlegen: Umgebungslicht, Licht der eigenen LED und Rauschen. Die Kontrollmessung schätzt den ersten Beitrag. Sie verrät außerdem, wenn sich während der Messreihe die Umgebung ändert, etwa durch Nachmittagssonne oder die LED eines Nachbarteams.

## 3. One reading is a guess

### Welcher Wert ist wahr? (Frames 23–25)

Fünf Ablesungen derselben roten LED unter denselben Einstellungen können 198, 205, 201, 195 und 206 ergeben. Keiner dieser Werte ist allein „der wahre Wert“, und doch ist jeder eine echte Messung. Jede reale Messung streut. Fünf vollkommen identische Werte wären bei einem echten Aufbau eher verdächtig als fünf leicht verschiedene.

Eine einzelne Ablesung ist eine Ziehung aus einer Verteilung. Sie verrät wenig darüber, wo die Werte normalerweise liegen und wie stark sie schwanken. Erst mehrere Ablesungen machen diese beiden Eigenschaften sichtbar.

### Demonstrator: The Noisy Sensor (Frame 26)

Im Demonstrator schickt ein Sender abwechselnd „led off“ und „led on“. Der Empfänger liest den Sensor und entscheidet an einer Schwelle, welches der beiden Symbole angekommen ist. Dieselben Ablesungen entscheiden dabei dreimal nebeneinander: einmal einzeln, einmal gemittelt über fünf Ablesungen, einmal über zehn.

Nach fünfundzwanzig Symbolen ist der Unterschied zu sehen. In der obersten Spur liegen einzelne Punkte auf der falschen Seite der Schwelle; sie sind rot und zählen als Fehlentscheidung. In den beiden unteren Spuren rücken die Punkte so weit zusammen, dass keiner mehr über die Schwelle rutscht. Genau das ist der Nutzen des Mittelns.

Der Preis steht daneben. Für dieselbe Zahl von Entscheidungen braucht die mittlere Spur fünfmal und die untere zehnmal so viele Ablesungen, und aus zwanzig Symbolen je Sekunde werden vier beziehungsweise zwei. Wer die Fehlerrate senken will, bezahlt mit Tempo.

Wie viel Mitteln nötig ist, hängt am Aufbau. Bei „low“ trifft schon die Einzelablesung immer richtig, dort kostet Mitteln nur Zeit; bei „high“ irrt selbst das Mittel aus fünf gelegentlich. Die Zahlen sind simuliert, die Struktur ist echt: Welcher Fall der eigene ist, verrät nur die eigene Messreihe. Mit „reset“ beginnt dieselbe Folge erneut, der Live-Moment bleibt reproduzierbar.

### Mitte und Streuung gehören zusammen (Frames 27–29)

Der Mittelwert beschreibt, wo eine Messreihe ungefähr liegt. Er sagt jedoch nicht, wie zuverlässig ein einzelner Wert in der Nähe dieses Mittels liegt. Zwei Reihen können denselben Mittelwert und sehr unterschiedliche Streuungen besitzen.

Darum gehören die Einzelwerte oder mindestens ein geeignetes Streuungsmaß ins Protokoll. Wer nur den Mittelwert notiert, verschweigt möglicherweise genau die Schwankung, die später zu falsch erkannten Symbolen führt.

### Der Drehknopf Integrationszeit (Frames 30–32)

Die Integrationszeit ist das Ablesefenster des Sensors. In einem langen Fenster sammelt der Sensor mehr Licht und mittelt kurzfristige Schwankungen. Die Werte liegen dadurch ruhiger beieinander, aber jede Messung benötigt mehr Zeit.

In der Abbildung ist jede Ablesung ein Balken, und seine Breite ist ihr Zeitfenster. Alle drei Zeilen zeigen dieselbe Sekunde: In der obersten passen vier lange Ablesungen hinein, in der untersten zwölf kurze. Die Höhe des Balkens ist der gemessene Wert. Kürzere Fenster liefern also mehr Messungen pro Sekunde, doch die Werte streuen stärker. Bei sehr kurzen Fenstern verlassen einzelne Ablesungen den Bereich, der noch korrekt einem Symbol zugeordnet wird. Auf der Folie sind diese Ausreißer rot markiert. Die Verstärkung ist der zweite Drehknopf: Sie skaliert Signal und Störung und kann den Sensor in die Sättigung treiben.

### Ruhiger oder schneller (Frame 33)

„Longer is calmer. Shorter is faster.“ Dieser Zielkonflikt prägt das gesamte Projekt. Mehr Ruhe kostet Symbolrate. Wo der beste Kompromiss liegt, hängt von Abstand, Raumlicht, Optik und Aufbau ab. Eine Tabelle oder ein KI-Assistent kann einen Startwert vorschlagen, aber die Grenze des eigenen Aufbaus muss gemessen werden.

Der spätere Input „Signal und Rauschen“ erklärt, was die Streuung für Alphabetgröße und Durchsatz bedeutet. Hier steht die Methode im Vordergrund, mit der diese Grenze überhaupt belastbar gefunden wird.

## 4. Build evidence

### Zwei Teams, zwei Veränderungen (Frames 35–36)

Team A verändert gleichzeitig den Abstand und die Integrationszeit. Team B verändert nur den Abstand. Bei beiden verbessert sich die Erkennungsrate. Nur Team B hat gelernt, wodurch die Verbesserung verursacht wurde. Bei Team A bleiben zwei mögliche Ursachen untrennbar miteinander vermischt.

Die Regel lautet daher: In einer Messreihe wird genau eine Größe gezielt verändert. Alle anderen Bedingungen bleiben möglichst konstant und werden aufgeschrieben.

### Was eine Messreihe ausmacht (Frames 37–39)

Vor der Messung werden die Bedingungen und die erwartete Wirkung notiert. Während der Messung wird genau eine Größe verändert, eine Kontrollmessung vorgenommen und oft genug wiederholt. Nach der Messung bleiben alle Werte erhalten, das Ergebnis wird mit der Erwartung verglichen und der Ausgang dokumentiert.

Diese drei Phasen sind zugleich die Checkliste des Messprotokolls. Bedingungen machen die Reihe wiederholbar. Die Erwartung macht sie ehrlich. Eine veränderte Größe macht sie deutbar. Wiederholungen machen sie belastbar. Alle Werte verhindern, dass nur die angenehmen Ergebnisse übrig bleiben. Wiederholbarkeit ist wertvoller als ein einzelnes beeindruckendes Resultat.

### Glück oder Können? (Frames 40–42)

Bei zwei möglichen Farben trifft reines Raten jede zweite Entscheidung. Fünf Treffer in Folge gelingen zufällig in etwa jedem 32. Anlauf. Im Semesterbetrieb passiert eine solche Glücksserie schnell irgendwo.

Fünfzig Treffer in Folge haben beim Raten eine Wahrscheinlichkeit von ungefähr eins zu 1.125.899.906.842.624. Das ist praktisch ausgeschlossen. Darum verlangen die Abnahmen lange Serien: Erst genügend Wiederholungen trennen Können von Glück.

### Kalibrieren, dann klassifizieren (Frames 43–46)

Kalibrieren heißt, bekannte Sendefarben unter den Bedingungen des eigenen Aufbaus wiederholt zu messen. Im Koordinatensystem entstehen daraus Wolken von Referenzwerten. Eine neue Messung wird anschließend mit diesen Wolken verglichen und der nächstliegenden zugeordnet.

Im Beispiel liegen die Rotmessungen in einem Bereich mit hohem Rot- und niedrigem Blauanteil, die Blaumessungen im gegenüberliegenden Bereich. Der Grünanteil ist hier ungefähr konstant und wird deshalb in der zweidimensionalen Darstellung weggelassen. Die neue Messung `r=170, b=80` liegt näher an den roten Referenzen. „Nearest match wins.“

Damit wird nicht zurückgerechnet, was die LED angeblich gesendet haben müsse. Stattdessen wird eine Entscheidung auf der Grundlage eigener Messreihen getroffen. Genau dieses Prinzip trägt Challenge 1.

### Wenn Assistent und Daten sich widersprechen (Frames 47–50)

Der Assistent schlägt vor, die Verstärkung zu erhöhen, weil dadurch die Erkennung besser werden solle. Die Messreihe zeigt jedoch einen Rückgang von 94 auf 82 Prozent. Bevor wir den Vorschlag als widerlegt ansehen, prüfen wir die Qualität der eigenen Reihe: Wurde nur eine Größe verändert? Gab es genügend Wiederholungen? War eine Kontrollmessung vorhanden?

Wenn diese Bedingungen erfüllt sind, ist die Messreihe die maßgebliche Wahrheit für den eigenen Aufbau. Der Widerspruch kommt ins Irrtumsprotokoll: Vorschlag, Messung, Ergebnis. Solche dokumentierten Fälle sind kein peinlicher Fehler, sondern Lernertrag und Prüfungsstoff.

### Der Schlusssatz (Frame 51)

„If you did not measure it, you do not know it.“ Ab heute ist jede Behauptung über den Aufbau eine Einladung zu einem Experiment. Nicht die schönste Erklärung gewinnt, sondern die sauberste Messreihe. Und eine einzelne Ablesung ist noch keine Messreihe.

## Zum Weiterlesen

Die Konzeptseite [Messen und Experimentieren](../../../website/concepts/measurement-and-experiments.qmd) fasst das methodische Handwerk zusammen. Die physikalischen Grenzen, die durch Streuung sichtbar werden, behandelt anschließend [Signal und Rauschen](../../../website/concepts/signal-and-noise.qmd).
