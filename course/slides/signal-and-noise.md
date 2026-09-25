<!-- Lecture notes for the slides on `signal-and-noise`, written in German. They follow the slides in order; frame numbers refer to the deck. The slides themselves are embedded on https://docs.lifi-project.de/concepts/signal-and-noise.html -->

# Skript: why 16 and not 4? (Input Signal und Rauschen)

Dieses Skript erläutert die Inhalte des Foliensatzes `web/index.html` zum Nachlesen. Es folgt der Folienreihenfolge; Verweise wie „(Frame 9)" zeigen auf die Nummer, die das Deck unten rechts anzeigt, und zählen Aufbauschritte einzeln. Das zugehörige Konzept auf der Website: [Signal and Noise](../../../website/concepts/signal-and-noise.qmd).

## Worum es geht

Wie viel eure Strecke trägt, entscheidet nicht euer Code. Es entscheidet das Verhältnis von Abstand zwischen den Symbolen zu Streuung der Messwerte, und jede Maßnahme dagegen hat einen Preis, den ihr kennen solltet, bevor ihr ihn zahlt.

Der Satz läuft in Sitzung 5, direkt nach dem Wettbewerb zu Challenge 1, und die erste Folie hängt sich an eure frischen Ergebnisse. Er ist trotzdem ein **normaler Input** und steht für sich: Wer ihn später allein durchgeht, braucht weder die Rangliste an der Wand noch den Saal. **Zwei Folien werden in der Sitzung ausgefüllt** (Frame 5 und Frame 24). Sie stehen vorbelegt da, damit sie auch beim Nachlesen etwas aussagen, und weil das Deck HTML ist, lässt sich wirklich hineintippen.

## Teil 1: what your data says

**Der Leuchtturm im Nebel (Frame 4).** Die Lampe brennt genauso hell wie in einer klaren Nacht, und trotzdem stirbt der Strahl nach wenigen Metern. Dem Signal ist nichts passiert. Passiert ist etwas mit allem anderen. Genau das ist eure Lage nach dem Wettbewerb: Alle Teams hatten dieselbe LED, denselben Sensor, denselben Raum, alle Sender waren gleich hell, und trotzdem bringt ein Team 16 Farben durch und ein anderes 4.

**Eure Ergebnisse (Frame 5).** Team, Alphabetgröße, Trefferquote, und was gegen das Rauschen getan wurde. Die letzte Spalte ist die wichtigste, sie wird beim Ausfüllen selbst zur Antwort. Erst sammeln, nicht kommentieren; dann die Frage stellen und stehen lassen: Gleiche Hardware, gleiche Aufgabe, Faktor vier zwischen erstem und letztem. Woher kommt der Unterschied?

**Zehn Messungen einer Farbe (Frames 6 bis 8).** Richtet den Sensor auf eine Farbe und lest ihn zehnmal aus, ohne irgendetwas zu verändern. Ihr bekommt zehn verschiedene Zahlen. Das überrascht die meisten, denn ein Computer ist die eine Maschine, die bei gleicher Eingabe zuverlässig dieselbe Ausgabe liefert. Aber der Sensor bekommt nie zweimal dieselbe Eingabe: Das Licht schwankt, die Elektronik rauscht, jemand geht am Fenster vorbei. Diese Schwankung heißt **Rauschen**, und sie hat jedes Messgerät der Welt.

Im dritten Schritt liegen dieselben zehn Werte auf einer Zahlenachse, und man sieht, was von ihnen bleibt: eine Spannweite von 207 bis 220. Daraus folgt etwas, das die ganze Sitzung trägt: **Eine einzelne Messung sagt fast nichts.** Der Wert 220 kann diese Farbe sein oder eine Nachbarfarbe in einem schlechten Moment. Erst die zehn zusammen sagen, wo die Farbe wirklich liegt und wie weit sie wandert.

**Nicht der Code, die Streuung (Frame 9).** Die Pointe früh setzen, danach wird sie belegt. Dass die Programmierqualität hier fast nichts entscheidet, überrascht die meisten; genau darum geht es. Rauschen ist kein Defekt und kein Codefehler, es ist eine Eigenschaft jeder Messung, und wer es kleiner bekommt, bringt mehr Symbole unter.

## Teil 2: what decides your alphabet

**Dasselbe Signal, anders gemessen (Frames 11 bis 14).** Es gibt einen Weg, die Zahlen ruhiger zu machen, und ihr habt ihn schon: länger messen und mitteln, was ankommt. Oben das Rohsignal, wie es beim Sensor ankommt, viel zu unruhig für eine Entscheidung in einem einzelnen Augenblick. Darunter dasselbe Signal, über Fenster von 4, 12 und 32 Messungen gemittelt; jeder dicke Strich ist ein Messwert, und die Striche legen sich immer näher an den wahren Pegel.

Der Blick gehört aber an den rechten Rand. Dieselbe Zeitspanne enthält 288 Rohwerte, dann 72, dann 24, dann 9. **Ruhe ist nicht umsonst, ihr bezahlt sie in Messwerten je Sekunde**, und Messwerte je Sekunde sind genau das, woraus euer Tempo besteht. Das ist das erste Preisschild dieses Inputs und nicht das letzte.

**Zwei Symbole, zwei Wolken (Frames 15 und 16).** Jetzt zwei Symbole auf derselben Skala. Jedes ist kein einzelner Wert, sondern eine Wolke von Werten, und die Breite dieser Wolke ist das Rauschen von eben. Links sind die Wolken schmal, die Grenze zwischen ihnen liegt im Leeren, jede Messung landet auf ihrer Seite. Rechts ist der Abstand derselbe, aber die Wolken sind breiter, und die Teile, die über die Grenze ragen, sind genau die Messungen, die der Empfänger falsch zuordnet. Weder der Abstand noch die Breite entscheidet für sich allein.

**Das Verhältnis entscheidet (Frame 17).** Die Größe, um die es in diesem ganzen Input geht, ist ein Quotient: der Abstand `d` zwischen zwei Symbolen, geteilt durch die Streuung `s` der Messwerte. Eure Alphabetgröße misst nichts anderes, und deshalb erklärt sie die Tabelle vom Anfang.

Daraus folgt eine schärfere Fassung eines Wortes, das wir bis hierher lose benutzt haben. **Sicher unterscheidbar** heißt nicht, dass die Mittelwerte verschieden sind. Es heißt, dass sich die Wolken nicht überlappen, auch an ihren äußersten Werten nicht. Eine einzige Messung, die über die Grenze rutscht, ist ein falsches Symbol, und ein falsches Symbol in fünfzig Läufen kostet euch eine Alphabetstufe. Wer eine Farbe nur mit ihrem Mittelwert dokumentiert, weiß noch nicht, ob sie brauchbar ist.

**Wie viele Symbole passen hinein? (Frame 18).** Sobald man in Bändern denkt statt in Punkten, hört „wie viele Farben können wir nehmen?" auf, eine Sache des Ausprobierens zu sein, und wird eine Rechnung. Messt den nutzbaren Bereich eurer Strecke, vom dunkelsten bis zum hellsten Wert, den ihr zuverlässig erzeugen könnt. Messt die Breite einer Wolke. Teilt, und ihr habt die Zahl der Symbole.

Ein Beispiel zum Mitrechnen: Der Bereich reicht von 40 bis 840, also 800 Einheiten. Jede Farbe streut um ihren Mittelwert um plus minus 25, ihr Band ist also 50 breit und nicht 25, denn die Wolke reicht in beide Richtungen. Und 800 geteilt durch 50 sind 16. Daher kommt ein Alphabet aus 16 Symbolen, und wer diese Rechnung vor dem Ausprobieren macht, spart in Challenge 2 eine halbe Sitzung.

**Der Demonstrator (Frame 19).** [The Distinguishability Lab](https://winf-hsos.github.io/lifi-concept-demos/distinguishability-lab/) hat drei Regler: Zahl der Symbole, Länge des Messfensters, Tempo. Zwei Aufträge. Erstens: die Fehlerquote auf null bringen und dabei den Durchsatz beobachten. Zweitens: den Störknopf drücken und sehen, was dann noch trägt. Die Zahlen sind simuliert, die Struktur ist echt; eure eigenen Zahlen kommen von eurer Strecke und von nirgendwo sonst.

## Teil 3: what it costs

**Die Werkzeugkiste mit Preisschildern (Frame 21).** Gegen das Rauschen gibt es Werkzeuge, und kaum eines ist gratis. Links vergrößert ihr den Abstand, rechts verkleinert ihr die Streuung. Auffällig ist, wie oft dasselbe auf den Preisschildern steht: weniger Bits je Symbol, oder weniger Symbole je Sekunde.

Drei Zeilen sind die Ausnahme, und sie sind der Grund, warum der optische Selbstbau in diesem Kurs erlaubt ist: Licht bündeln, Fremdlicht abschirmen, Geometrie festnageln. Die verbessern das Verhältnis, ohne dass ihr irgendetwas dafür hergebt, und sie kosten nur einen Nachmittag mit Pappe. Passiv, höchstens zehn Euro.

**Mitteln ist nicht umsonst (Frame 22).** Der häufigste Reflex nach dieser Auswertung ist mitteln. `read_stable()` macht es vor: zehn Messungen, ein Mittelwert. Zehnmal ruhigere Werte, zehnmal langsamer. Das ist kein Argument gegen das Mitteln, es ist ein Argument dafür, den Preis zu messen, statt ihn für null zu halten. Es ist dasselbe Geschäft wie eine längere Integrationszeit, nur an einer anderen Stelle: einmal im Sensor, einmal im Programm.

**Beide Wege enden an derselben Wand (Frame 23).** Es gibt zwei Wege, mehr aus der Strecke zu holen, und Studierende wollen fast immer beide gleichzeitig. Mehr Symbole drückt die Bänder zusammen. Schnellere Symbole macht die Wolken breiter. Beide verbrauchen denselben Sicherheitsabstand, und ihr habt nur einen. An dieser Wand fängt Challenge 2 an, und durch sie führt kein klügeres Programm, sondern eine Zahl, die ihr selbst gemessen habt.

**Ein ehrlicher Satz (Frame 24).** Zwei oder drei Teams lesen einen Eintrag aus ihrem Irrtumsprotokoll vor, am besten Fälle, in denen ein plausibler Vorschlag des Assistenten an der Messung gescheitert ist. Die Kurzfassung kommt in die zwei Zeilen, sie sind editierbar. Das ist der Moment, in dem das Irrtumsprotokoll seinen Sinn zeigt: Es unterscheidet diese Veranstaltung von einem Programmierkurs.

**Der Messstab im Nebel (Frame 25).** Alles in diesem Input ist eine Eigenschaft **eurer** Strecke: euer Raum, euer Abstand, euer Umgebungslicht. Wer am Fenster kalibriert, dessen Werte stimmen bei der Abnahme im abgedunkelten Teil des Raums nicht mehr. Dazu hat kein Sprachmodell Zugang, und keine noch so gute Lektüre. Eure Aufgabe ist nicht, das Rauschen zu besiegen, das geht nicht. Eure Aufgabe ist, es zu messen und dann zu entscheiden, welches Alphabet und welches Tempo eure Strecke ehrlich hergibt. Der Nebel bleibt; was ihr in der Hand habt, ist der Maßstab.

## Zum Weiterlesen

Die Konzeptseite [Signal and Noise](../../../website/concepts/signal-and-noise.qmd) fasst das Ganze zusammen und enthält dieselben Abbildungen. Wie man ehrlich misst, also Kontrollmessung, eine Variable auf einmal, Protokoll, steht bei [Measurement and Experiments](../../../website/concepts/measurement-and-experiments.qmd); dieser Input benutzt diese Messungen, statt sie zu erklären. Die andere Hälfte des Zielkonflikts, die Zahl der Symbole bei gleicher Messdauer, steht bei [Analog and Digital](../../../website/concepts/analog-and-digital.qmd). Und was ihr mit dem Alphabet dann anstellt, klärt [Code Systems](../../../website/concepts/code-systems.qmd) in der nächsten Sitzung.
