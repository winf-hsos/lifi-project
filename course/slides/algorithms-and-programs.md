<!-- Lecture notes for the slides on `algorithms-and-programs`, written in German. They follow the slides in order; frame numbers refer to the deck. The slides themselves are embedded on https://docs.lifi-project.de/concepts/algorithms-and-programs.html -->

# Skript: what is a program? (Input, Sitzung 2, zweiter Teil)

Deck 02 zum Konzept „Algorithmen und Programme“. Dieses Skript erläutert die Folien zum Nachlesen. Es folgt der Folienreihenfolge und nennt die Nummern, wie sie das HTML-Deck zählt (jeder Aufbauschritt ist eine eigene Nummer, 40 Frames), ist aber als eigenständiger Text lesbar. Das zugehörige Konzept auf der Website: [Algorithmen und Programme](../../../website/concepts/algorithms-and-programs.qmd).

## Worum es geht

Der IPO-Teil davor hat eine Frage offen gelassen: Wie verrichtet der Kasten seine Arbeit? Die Antwort kommt in zwei Stufen: erst der Algorithmus, den ihr längst kennt, weil ihr einen ausgeführt habt, dann das Programm, derselbe Ablauf, aufgeschrieben für eine Maschine. Danach die vier Bausteine, aus denen jedes Programm besteht, der Umgang mit Fehlermeldungen, und wie man mit dem KI-Assistenten arbeitet, ohne Code nur entgegenzunehmen.

## Teil 1: last week

**Wer spielt hier? (Folie 4).** Ein Klavier spielt, die Tasten bewegen sich, die Bank ist leer. Solche selbstspielenden Klaviere standen um 1900 in vielen Salons. Der Spieler ist die Papierrolle über der Tastatur: Jedes gestanzte Loch bedeutet „drücke jetzt diese Taste“. Das Klavier versteht nichts von Musik, es führt nur aus. Der eigentliche Pianist ist der Mensch, der die Rolle gestanzt hat, vielleicht Jahrzehnte vorher. Die Rolle ist das Programm, das Klavier die Maschine, der Stanzer der Programmierer. Und so etwas wie dieses Klavier wart ihr selbst schon.

**Ihr wart schon der Empfänger (Folie 5).** In der ersten Sitzung habt ihr im Farbkarten-Experiment selbst empfangen: auf die Karte schauen, entscheiden, welche Farbe es ist, das passende Zeichen notieren, auf die nächste warten.

**Das war ein Algorithmus, und ihr wart die Maschine (Folie 6).** Jetzt bekommt das Kind seinen Namen: Eine Schrittfolge, die so genau beschrieben ist, dass man sie ausführen kann, ohne zu verstehen, worum es geht, heißt Algorithmus. Er braucht keinen Computer, er kann auf einem Zettel stehen, und genau so habt ihr ihn abgearbeitet.

**Vier Zeilen, eine davon schwer (Folie 7).** Dieselben vier Zeilen noch einmal, diesmal ist die zweite hervorgehoben. Drei davon übernimmt ab heute Stück für Stück der Rechner. Das Entscheiden, welche Farbe da liegt, ist Challenge 1 und wird euch drei Wochen beschäftigen.

**Noch ein Algorithmus, live (Folien 8 und 9).** Sechs Freiwillige stellen sich unsortiert in eine Reihe und führen strikt fünf Regeln aus: in einer Reihe stehen, auf den rechten Nachbarn schauen, tauschen, wenn er kleiner ist, am Reihenende wieder von vorn, und ein vollständiger Durchlauf ohne Tausch heißt fertig. Kein Nachdenken, nur Ausführen. Nach zwei, drei Minuten steht die Reihe der Größe nach, und ihr habt Bubble Sort ausgeführt; so sortieren auch Computer, nur schneller. Zwei Beobachtungen nehmt ihr mit: Woran hat der Ablauf sein Ende erkannt? Am vollständigen Durchlauf ohne Tausch, das ist eine Terminierungsbedingung, sie kommt in Teil 3 wieder. Und wie viele Vergleiche waren das bei sechs Personen, was wäre es bei vierzig? Auch das kommt wieder, beim Aufwand.

**Ein Programm ist ein Algorithmus, aufgeschrieben für eine Maschine (Folie 10).** Beim Übergang kommt eine Anforderung dazu, die der Zettel nicht hatte: Vollständigkeit. Ein Mensch ergänzt beim Lesen, was offensichtlich gemeint war. Die Maschine ergänzt nichts.

## Teil 2: the instruction follower

**Ein Programm ist eine Liste (Folie 12).** Eine Liste von Anweisungen, und etwas, das dieser Liste folgt, exakt und der Reihe nach. Mehr Magie ist nicht im Spiel.

**Die Liste bei der Arbeit (Folie 13).** Drei Zeilen von oben nach unten, und rechts daneben, was man sieht: Die erste macht die LED rot, die zweite lässt sie eine Sekunde rot, die dritte macht sie blau. Jede Zeile verändert etwas Sichtbares. Und die Maschine weiß dabei nicht, was gemeint war: Sie führt aus, was dasteht, in der Reihenfolge, in der es dasteht, und nichts sonst. Aus genau diesem Unterschied entstehen fast alle Fehler dieses Semesters.

**Anatomie einer Zeile (Folien 14 bis 17).** Die Zeile besteht aus drei Teilen. Das erste Stück sagt, welches Ding angesprochen wird, hier die LED. Das zweite sagt, was es tun soll. Das dritte sagt, mit welchen Werten, hier voller Rotanteil, kein Grün, kein Blau.

**Dieselbe Anweisung, andere Werte (Folie 18).** Zweimal dieselbe Anweisung, einmal mit Rot, einmal mit Blau. Der Name sagt, was passiert; die Werte sagen, wie.

## Teil 3: four building blocks

Jedes Programm dieser Welt besteht aus vier Bausteinen: Anweisungen nacheinander, Werte mit Namen, Wiederholung, Bedingung. Alle vier seht ihr an der LED.

**Baustein 1: eins nach dem anderen (Folien 20 bis 22).** Anweisungen laufen der Reihe nach. Folie 21 stellt zwei Programme nebeneinander, beide richtig: Mit einer Pause bleibt Rot eine Sekunde sichtbar; ohne Pause lebt Rot etwa eine Millisekunde, viel zu kurz für ein Auge, und ihr seht nur Blau. Das Programm ist nicht kaputt, es ist zu schnell. Eure Augen sind langsam, die Maschine ist es nicht. Folie 22 zeigt dasselbe für die Reihenfolge: Rückt die Pause ans Ende, wartet die Maschine mit blauer LED, und Rot ist wieder nur eine Millisekunde zu sehen. Es fehlt keine Zeile, und trotzdem ist es ein anderes Programm.

**Baustein 2: ein Wert mit einem Namen (Folie 23).** Ein Name für einen Wert, den man danach überall benutzt. Der Gewinn ist nicht die Kürze, sondern die eine Stelle zum Ändern statt vieler.

**Baustein 3: Wiederholung (Folien 24 und 25).** Eine Liste von Farben und eine Schleife darüber. Eine Schleife ist keine Magie, sondern eine Schreibweise: Dieselben zwei Zeilen laufen viermal, mit jeweils dem nächsten Wert aus der Liste. Folie 25 rollt das gegen die Zeit aus: links, was ihr schreibt, rechts vier Durchläufe mit je einem Wert und je einer Sekunde, zusammen vier Sekunden.

**Baustein 4: nur wenn (Folie 26).** Eine Bedingung führt die eingerückte Zeile nur aus, wenn sie zutrifft, und „else“ sagt, was sonst passiert. Damit kann ein Programm auf etwas reagieren, statt stur abzuspulen.

**Wann endet das? (Folie 27).** Die Terminierungsbedingung kennt ihr aus der Sortierübung; hier fehlt sie. Die Bedingung ist immer wahr, und im Schleifenkörper gibt es keinen Ausweg, also endet dieses Programm nie. Fürs Dauerblinken ist das sogar richtig; eine Empfänger-Hauptschleife braucht dagegen eine Abbruchbedingung. Der Werkstatt-Klassiker „mein Programm hängt“ heißt fast immer „meine Schleife hat keinen Ausweg“.

**Was kostet das? (Folie 28).** Zwei Verfahren können beide korrekt sein und trotzdem Welten trennen. Beim Zahlenraten aus Sitzung 1 fragt das eine bis zu 99-mal, das andere höchstens siebenmal. Bei tausend Zahlen steht es 999 gegen 10. Richtigkeit ist die Mindestanforderung; danach vergleicht man Algorithmen darüber, wie ihr Aufwand mit dem Problem wächst. Für eure Übertragung wird daraus die handfeste Frage, wie viele Sekunden eine Datei unterwegs ist. Der Faden wird in Sitzung 13 wieder aufgenommen.

## Teil 4: it does what is written

**Die Fehlermeldung lesen (Folien 30 bis 33).** Ein Traceback sieht bedrohlich aus, ist aber eine präzise Auskunft, und die Folie liest sie Zeile für Zeile mit euch: welche Datei und welche Zeile, was dort stand, und was genau nicht existiert, hier die Schreibung „set_colour“ mit u statt „set_color“. Die Maschine hat nicht versagt; sie hat getan, was dastand, und meldet exakt, woran sie gescheitert ist.

**Auskunft, kein Urteil (Folien 34 und 35).** Eine Fehlermeldung ist Information über das Programm, keine Bewertung eurer Person. Lest sie laut vor; meistens sagt sie wortwörtlich, was falsch ist. Und ihr seht den Umgang live: Vorn am Beamer wird absichtlich Fehler für Fehler eingebaut und aufgelöst.

## Teil 5: working with the assistant

**Zwei Arten zu fragen (Folien 37 und 38).** Die erste Frage bringt euch Code, den ihr nicht versteht. Die zweite sagt, was herauskommen soll, und bestellt die Erklärung gleich mit: Sie bringt euch Code und Verständnis.

**Die Regel (Folie 39).** Behaltet nie Code, den ihr nicht ändern könnt. Jede Übernahme endet mit einer kleinen Änderung durch euch selbst: eine Farbe tauschen, eine Wartezeit anpassen. Wer das nicht kann, hat den Code nicht übernommen, sondern nur kopiert.

**Der Werkstattauftrag (Folie 40).** Heute: erstens eine Farbe an, zweitens vier Farben in einer Schleife, drittens Blinken mit einstellbarer Geschwindigkeit. Nummer drei ist die eigentliche Aufgabe: Die Geschwindigkeit muss sich an genau einer Stelle ändern lassen, ohne im Code zu wühlen, also Baustein 2 benutzen.

## Zum Weiterlesen

Die Konzeptseite [Algorithmen und Programme](../../../website/concepts/algorithms-and-programs.qmd) fasst das Ganze mit den Abbildungen zusammen. Wie man zwei richtige Verfahren vergleicht, habt ihr in Sitzung 1 am Zahlenraten gesehen: 99 Fragen oder 7, beide korrekt, eine davon unbrauchbar langsam.
