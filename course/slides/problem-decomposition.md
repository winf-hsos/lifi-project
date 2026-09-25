<!-- Lecture notes for the slides on `problem-decomposition`, written in German. They follow the slides in order; frame numbers refer to the deck. The slides themselves are embedded on https://docs.lifi-project.de/concepts/problem-decomposition.html -->

# Skript: cutting problems (Input, Sitzung 1)

Deck 01, der erste Input des Semesters, zum Konzept „Probleme zerlegen“. Dieses Skript erläutert die Folien zum Nachlesen. Es folgt der Folienreihenfolge und nennt die Nummern, wie sie das HTML-Deck zählt (jeder Aufbauschritt ist eine eigene Nummer, 36 Frames), ist aber als eigenständiger Text lesbar.

## Worum es geht

Große Probleme werden nicht in einem Stück gelöst. Sie werden so lange geschnitten, bis die Teile lösbar und prüfbar sind. Dieser Input zeigt, dass ihr das längst könnt, gibt euch drei bewährte Schnittmuster an die Hand und erklärt, woran man einen guten Schnitt erkennt. Am Ende steht, warum genau diese Fähigkeit im Umgang mit KI-Assistenten den Unterschied macht.

## Teil 1: you can already do this

**Wie isst man einen Elefanten? (Folie 4).** Ein Bissen nach dem anderen. Der Spruch ist alt, aber er trägt: Niemand isst einen Elefanten am Stück, und niemand löst ein großes Problem am Stück. Große Probleme werden nicht gelöst, sie werden geschnitten.

**Die Party (Folien 5 und 6).** Eure Mitbewohnerin wird 25, Party am Samstag, 30 Gäste. Auf Folie 5 steht dieses eine Ding, und niemand plant es als ein Ding. Folie 6 zeigt, was ihr sofort tut: schneiden. Getränke, Essen, Musik, Einladungen, Aufräumen, und dann verteilen. Das ist Zerlegung, ihr könnt sie längst, ihr habt sie nur nie so genannt. Nebenbei sind die Teile so geschnitten, dass man einzeln nachfragen kann, ob sie erledigt sind. Darauf kommen wir zurück.

## Teil 2: this semester's elephant

**Die Aufgabe (Folie 8).** „transfer a file from one laptop to another, using light.“ So, als ein Stück formuliert, kann das niemand lösen. Kein Profi, keine KI, ihr auch nicht. Das ist keine Drohung, sondern der Normalzustand: Interessante Probleme sind am Anfang immer zu groß.

**Die Zerlegung (Folien 9 bis 11).** Auf Folie 9 steht das große Problem allein. Folie 10 zeigt es geschnitten, in vier Teilen: Farben auseinanderhalten, Buchstaben in Farben übersetzen, Anfang und Ende finden, eine ganze Datei übertragen. Jedes Teil ist lösbar, von euch, in zwei bis drei Wochen. Folie 11 nennt die Teile beim Namen, und da liegt der Punkt: Euer Semesterplan ist genau diese Zerlegung. Die vier Teile heißen Challenge 1 bis 4. Dieses Semester ist nicht zufällig so gebaut, es ist die Zerlegung eines Problems, das sich anders nicht lösen lässt.

**Eine Frage, vier Fragen (Folie 12).** Hinter der Zerlegung in vier Challenges steckt die Karte des ganzen Moduls. Die große Frage lautet: Wie lösen wir komplexe Probleme mit Computern? Darunter liegen vier Fragen über Information: Wie stellen Computer sie dar, wie speichern sie sie, wie übertragen sie sie, wie verarbeiten sie sie. Unter jeder Frage stehen ihre wichtigsten Konzepte, beim Übertragen etwa Signal und Rauschen, Takt und Protokolle. Alle vier Fragen gehen euch an, wenn auch nicht gleich stark: Die Lichtstrecke ist das Übertragen, aber ihr stellt Farben als Symbole dar, ihr speichert eine Datei, und eine Prüfsumme verarbeitet sie. Unter der großen Frage stehen die Fähigkeiten, mit denen wir sie angehen: Probleme zerlegen, das IPO-Modell, Programme schreiben, messen, in Schichten denken. Jede Sitzung arbeitet an einer der vier Fragen; auf der Website hängt dieselbe Karte über allen Konzepten.

## Teil 3: three ways to cut

Schneiden kann man auf viele Arten. Drei davon werdet ihr ständig brauchen.

**Divide and Conquer: halbieren, bis es leicht ist (Folien 14 bis 21).** Denkt euch eine Zahl zwischen 1 und 100. Folie 14 zeigt den Ausgangszustand: hundert Kandidaten, ein Balken über die volle Breite, und irgendwo darin die gesuchte 73. Mit jeder Ja/Nein-Frage kommt eine Zeile dazu, und der Balken wird kürzer: „größer als 50?“ ja, und die Hälfte ist weg; „größer als 75?“ nein, und wieder die Hälfte. So geht es weiter über 25, 12, 6, 3, 2 Kandidaten bis zur letzten Frage auf Folie 21, und die Zahl steht fest. Sieben Fragen genügen immer, egal welche Zahl gesucht ist. Die Strategie heißt in der Informatik Divide and Conquer und funktioniert überall dort, wo man nach jedem Schnitt eine Hälfte ausschließen kann. Die gelbe Frage am Fuß der letzten Folie, „how many steps in general?“, bleibt bewusst offen. Sie ist der Ausblick auf ein späteres Thema: Jede Ja/Nein-Frage ist ein Bit Information.

**Derselbe Trick, wenn etwas kaputt ist (Folien 22 bis 24).** WLAN tot. Wie geht ihr vor? Folie 22 zeigt die Kette der Verdächtigen: Laptop, WLAN, Router, Anbieter, Internet. Auf Folie 23 kommt der Test in der Mitte, und die halbe Kette ist erledigt: Geht der Handy-Hotspot, liegt es nicht am Laptop. Genau das tut ihr instinktiv, wenn ihr Router-Lämpchen anschaut oder ein anderes Gerät probiert. Folie 24 stellt dieselbe Kette für das Projekt daneben: Sender, LED, Luft, Sensor, Empfänger. Ihr werdet sie oft entlanglaufen, wenn „nichts ankommt“: Leuchtet die LED überhaupt? Sieht der Sensor eine Taschenlampe? Wer grob zerlegt hat, weiß nur, dass etwas kaputt ist. Wer gut zerlegt hat, weiß wo.

**Erst die kleinere Version lösen (Folie 25).** Wenn das Problem zu groß ist, löst erst eine kleinere Fassung, die ihr wirklich könnt, und wachst von dort: erst Licht an und aus, dann möglichst viele unterscheidbare Farben, dann ein Zeichen, dann ein Wort, am Ende eine ganze Datei. Die Treppe auf der Folie ist euer Semester, die Stufen sind die Challenges 0 bis 4. Auf der untersten steht ihr heute.

## Teil 4: a good cut is testable

**Das Klausurbeispiel (Folien 27 und 28).** „Ich muss Mathe lernen“ und „ich schaffe die Altklausur von 2023 in 90 Minuten“ klingen beide nach Klausurvorbereitung. Der Unterschied steht auf Folie 28: Beim ersten wisst ihr nie, ob ihr fertig seid. Das zweite könnt ihr heute Abend ausprobieren und bekommt ein Ja oder Nein. Ein gutes Teil ist eines mit eingebautem Test.

**Dasselbe im Projekt (Folien 29 und 30).** „Die LED funktioniert“ ist ein Gefühl. „Rot oder Blau, 50-mal in Folge richtig erkannt“ ist ein Messwert. Genau so sind alle Challenges formuliert, und genau so laufen die Abnahmen: Es gibt immer einen Test, der Ja oder Nein sagt.

**Die Werkstattregel (Folie 31).** „done means: the test passes.“ Fertig heißt nicht „sieht gut aus“, fertig heißt: Der Test läuft durch. Jede Aufgabe in diesem Modul endet mit einem Prüfschritt, den ihr selbst ausführen könnt, ohne auf jemanden zu warten.

## Teil 5: cuts are agreements

**Wo ihr schneidet, entscheidet, wie viel ihr reden müsst (Folie 33).** Zurück zur Party. Links auf der Folie zwei Zuständigkeiten mit einer klaren Kante: „Du machst die Vorspeise, ich den Nachtisch.“ Das funktioniert. Rechts überlappen sich zwei Zuständigkeiten, beide machen irgendwie das Essen, und im Überschnitt steht die Frage, die dann offen bleibt: Wer kauft das Brot? Teile funktionieren, wenn die Grenze klar ist. Im Zweierteam gilt dasselbe: eine Person je Ende der Strecke, und was die Grenze überquert, etwa welche Farbe welches Zeichen bedeutet, wird aufgeschrieben. Wie ernst das wird, merkt ihr in Challenge 3, wenn ein fremdes Team eure Absprache lesen und umsetzen muss.

**Die Arbeitsteilung mit dem KI-Assistenten (Folien 34 und 35).** Zwei Arten, den Assistenten zu beauftragen. „build me the file transfer“ ist ein großer Wunsch. Der Agent kann ihn nicht gut erfüllen, und ihr könntet das Ergebnis nicht einmal prüfen. Dagegen der kleine Auftrag, der seinen Test gleich mitbringt: „read the sensor ten times and return the average. test: covered, it stays under 10. red led on, it goes over 100.“ Der Auftrag sagt, was herauskommen soll, und wie ihr es prüft: Sensor zuhalten, Mittelwert unter 10; rote LED an, Mittelwert über 100. Das dauert zehn Sekunden, und danach wisst ihr es, statt es zu glauben. Zerlegen ist die Fähigkeit, die euch von „ich hoffe, die KI hat recht“ zu „ich habe es geprüft“ bringt. Deshalb steht sie in den vier Zielen dieses Moduls, und deshalb ist sie der erste Input des Semesters: Ihr schneidet. Der Assistent löst Teile. Ihr prüft.

**Ein Bissen nach dem anderen (Folie 36).** Der Elefant vom Anfang, zum Schluss noch einmal. Ihr könnt das schon, ihr habt heute drei Schnittmuster dazubekommen, und ihr wisst jetzt, woran man einen guten Schnitt erkennt: am eingebauten Test.

## Zum Weiterlesen

Die Konzeptseite [Probleme zerlegen](../../../website/concepts/problem-decomposition.qmd) fasst das Ganze mit den Abbildungen zusammen. Wie ein geschnittenes Teil aussieht, wenn ein Computer es lösen soll, ist das Thema des nächsten Inputs (Eingabe, Verarbeitung, Ausgabe).
