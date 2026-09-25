<!-- Lecture notes for the slides on `abstraction-and-layers`, written in German. They follow the slides in order; frame numbers refer to the deck. The slides themselves are embedded on https://docs.lifi-project.de/concepts/abstraction-and-layers.html -->

# Skript: what's under the switch?

Dieser Text erläutert den Input zum Konzept „Abstraktion und Schichten" zum Nachlesen. Er folgt der Reihenfolge der Folien, die Verweise zählen Frames (jeder Aufbauschritt ist ein eigener Frame), lässt sich aber auch ohne die Folien lesen.

Der Satz hat im Semesterplan keinen eigenen Termin. Teil 1 und Teil 4 gehören an das Ende von Sitzung 7, nach dem Input zu Abtastung und Synchronisation; Teil 2 und Teil 3 tragen den Rückblick in Sitzung 14. Keine Folie setzt voraus, an welcher Stelle des Semesters sie gezeigt wird, der Satz funktioniert in Woche 7 genauso wie in Woche 14. Wer ihn am Stück liest, hat das ganze Konzept.

## Der Schalter (Frame 4)

Heute Morgen hat jeder von euch einen Lichtschalter gedrückt. Zwischen dem Finger und der Lampe liegen ein Kraftwerk, ein Netz über das ganze Land, ein Transformator in der Straße und ein Draht in der Wand. Nichts davon wusstet ihr in dem Moment, und nichts davon hat gefehlt.

Das ist keine Bildungslücke. Es ist der Grund, warum ihr überhaupt Licht anmachen könnt, ohne Elektrotechniker zu sein.

## Was der Schalter verspricht (Frames 5 bis 7)

Hinter dem Schalter hängt eine Kette: Draht, Transformator, Netz, Kraftwerk. Für die Benutzung des Schalters ist diese Kette vollständig unsichtbar. Der Schalter verspricht genau zwei Dinge, hoch und runter, und dieses Versprechen hält er, egal was dahinter passiert.

Genau deshalb kann sich die Stromversorgung eines ganzen Landes umbauen, von Kohle auf Wind, ohne dass irgendjemand einen neuen Schalter lernen müsste. Was hinter der Zusage liegt, darf sich ändern. Die Zusage bleibt.

## Das Wort dafür (Frame 8)

**Eine Abstraktion verbirgt, wie etwas funktioniert, und zeigt, was man damit tun kann.** Der zweite Halbsatz ist der wichtigere. Eine Abstraktion versteckt nicht nur, sie stellt auch etwas bereit, und dieser bereitgestellte Teil heißt **Schnittstelle**.

Eine Schnittstelle ist eine Zusage: Solange du dich an sie hältst, funktioniert es. Beim Schalter besteht die ganze Zusage aus zwei Stellungen.

## Drei, die ihr heute schon benutzt habt (Frame 9)

Keine Zeile in diesem Projekt steht nicht auf mehreren solcher Zusagen.

`led.set_color(255, 0, 0)` verbirgt USB, das Tinkerforge-Protokoll, Spannungen und den Treiber der Leuchtdiode. Drei Zahlen hinein, Licht heraus. `python` verbirgt Maschinencode, Speicher und Prozessor. `photo.jpg` verbirgt Bytes auf einer Platte, ein Dateisystem und einen Controller.

`set_color` ist der Lichtschalter dieses Kurses. Wer bei jedem Aufruf an USB-Pakete denken müsste, käme nie zu einer Challenge.

## Euer eigener Stapel (Frames 11 bis 16)

Jetzt der Perspektivwechsel: Ihr benutzt nicht nur Abstraktionen, ihr baut selbst welche, ungefähr eine je Challenge.

Nehmt ein Foto und schickt es über die Strecke. Von oben nach unten sieht das so aus:

| Schicht | Was auf dieser Ebene vorliegt |
| --- | --- |
| Bedeutung | das Foto |
| Codesystem | die Bytes der Datei, `FF D8 FF E0 …` |
| Rahmen | Präambel, Typ, Länge, Nutzdaten, Prüfsumme, Ende |
| Bits | `1101 0010 0110 1001` |
| Symbole | vier unterscheidbare Farben |
| Träger | Licht |

Von oben gelesen ist es ein Foto. Von unten gelesen ist es eine Leuchtdiode, die an und aus geht. Dazwischen liegt alles, worum es in diesem Kurs geht.

## Die eine Regel (Frame 17)

**Jede Schicht spricht nur mit der unmittelbar darunterliegenden.** Diese eine Regel klingt harmlos und ist der Grund für alles, was danach kommt: Austauschbarkeit, Arbeitsteilung im Team und eine Fehlersuche, die nicht im Nebel stochert.

## Was die Trennung einbringt (Frame 18)

Eure Funktion, die Text in Bits übersetzt, weiß nichts über Farben. Eure Farberkennung weiß nichts über Buchstaben. Das Einzige, was beide kennen, ist der Bitstrom dazwischen, und genau der ist ihre Schnittstelle.

Die häufigste Fehlvorstellung ist, das sei Ordnungsliebe. Es ist eine Versicherung: Wer die Farbzuordnung ändert, kann die Textkodierung dabei nicht kaputt machen, weil er sie gar nicht anfasst.

## Wer darf die Leuchtdiode ansteuern? (Frames 19 bis 21)

Drei Funktionen, drei Schichten: `send_text()`, `send_frame()`, `send_symbols()`. Welche von ihnen darf `led.set_color()` aufrufen?

Die Frage klingt nach einer Eigenschaft der Funktionen, ist aber eine Frage nach einem **Aufruf**. Deshalb steht die Antwort auf der Folie am Pfeil und nicht am Kasten.

Erlaubt ist der grüne Pfeil: `send_symbols()` darf. Sie ist die unterste der drei, und nur dort ist überhaupt bekannt, welche Farbe ein Symbol trägt. Die beiden anderen wissen es nicht und sollen es nicht wissen.

Der rote Pfeil ist die Abkürzung von ganz oben direkt nach ganz unten, die jeder einmal nimmt, wenn es schnell gehen muss. Ihr Preis fällt später an: Wer sie nimmt, hat die Farben in `send_text` einbetoniert und kann das Alphabet nicht mehr ändern, ohne den Textcode anzufassen.

## Die unterste Schicht tauschen (Frames 23 und 24)

Jetzt der Test, ob die Trennung wirklich trägt. Ersetzt die Leuchtdiode durch einen Lautsprecher und den Farbsensor durch ein Mikrofon. Was muss sich ändern?

Oberhalb der Symbolschicht keine Zeile. Fünf Schichten bleiben unverändert, eine wird ausgetauscht. Wir bauen das im Kurs nicht um; als Gedankenexperiment reicht es, und wer die Schichten sauber getrennt hat, könnte es an einem Nachmittag.

**Dieselben Bits, drei Träger.** Der Gedanke hinter dem Tausch ist größer als der Tausch. Information braucht immer etwas Physikalisches, das sie trägt: eine Farbe auf der LED, eine Spannung auf einer Leitung, einen Ton aus dem Lautsprecher, die Magnetisierung auf einer Festplatte. Aber sie ist nicht dieses Physikalische, und sie hängt nicht daran. Derselbe Bitstrom, den ihr durch Licht schickt, könnte durch ein Kabel laufen oder über einen Lautsprecher, und alles über der untersten Schicht würde davon nichts merken. Genau deshalb gibt es eine eigene Disziplin für Information und nicht nur Elektrotechnik; außerhalb der Informatik heißt dieselbe Idee Substratunabhängigkeit. Was ihr sendet, sind die Bits. Licht ist nur, was sie heute trägt.

Ehrlicherweise gehört dazu: Die erreichbare Symbolrate ändert sich sehr wohl. Alles läuft weiter, aber anders schnell. Eine Abstraktion macht den Tausch möglich, sie macht ihn nicht folgenlos.

## Das Alphabet erweitern (Frames 25 und 26)

Ein Team geht von vier auf acht Farben. Welche Teile müssen sich ändern?

Die Antwort steht im selben Stapel wie überall: Gelb ist nur die Symbolschicht, und daneben steht, was in ihr liegt, nämlich die Farbtabelle, die Kalibrierung und die Übersetzung zwischen Bits und Symbolen. Jede andere Schicht bleibt, wie sie ist.

Die verlockende falsche Antwort lautet „alle Schichten, denn jedes Symbol trägt jetzt mehr Bits". Der Bitstrom ist aber derselbe Bitstrom; er wird nur anders auf Farben verteilt. Und der Empfänger erfährt die Farbzahl nicht aus dem Rahmen, sondern weil er zum selben Team gehört.

## Warum im Rahmen nichts über Zeit steht (Frame 27)

Ein Rahmen wird **in Bits** definiert, nicht in Farben, und er sagt nichts über Zeit.

Das ist kein Versehen. Takt ist eine Eigenschaft des Übertragungswegs, nicht der Nachricht. Stünde im Rahmen ein Feld „Symbole pro Sekunde", wäre der Substrattausch nicht mehr sauber, denn Ton verträgt eine andere Rate als Licht. Steht der Klassenstandard schon, ist das hier die Bestätigung; steht er noch aus, ist es die Vorgabe für die Normungssitzung.

## Die Umkehrung (Frames 28 und 29)

Alles in diesem Projekt sitzt auf Licht. Und Licht ist die eine Schicht, die man ersetzen könnte.

Der Kurs heißt nicht Lichtkommunikation. Er handelt davon, wie Information dargestellt wird, wie man ein Problem in prüfbare Teile zerlegt, wie man etwas baut, das größer ist als der eigene Kopf, und wie man mit einem Assistenten arbeitet, der alles behauptet. Licht ist der Gegenstand, an dem sich das zeigen lässt.

## Was Schichten kosten (Frames 31 bis 33)

Damit daraus keine Heilslehre wird: Schichten haben einen Preis.

**Jede Schicht legt eigene Daten dazu.** Der Rahmen kostet Bytes, die für die Nutzdaten nicht mehr zur Verfügung stehen.

**Jede Grenze verbirgt eine Stellschraube.** Und es ist zuverlässig die, an der man gerade drehen möchte.

**Man muss wissen, wo die Grenzen verlaufen.** Wer sie falsch vermutet, sucht an der falschen Stelle.

Die Antwort „es gibt keinen Preis" ist falsch. Schichten kosten Durchsatz und Durchgriff. Sie sind trotzdem meistens richtig, aber das ist eine Abwägung und kein Naturgesetz.

## Den Fehler nach Schichten eingrenzen (Frames 34 bis 36)

Bei einem Team kommen falsche Buchstaben an. Ein Test zeigt: Die Farberkennung liefert die gesendeten Symbole zu hundert Prozent richtig. Wo sucht ihr zuerst?

Oberhalb der Symbolschicht. Der Reflex geht zum Sensor, weil dort das Geheimnisvolle sitzt, aber der Test hat die untere Schicht entlastet. Damit ist die Suche halbiert, ohne dass irgendetwas repariert wurde.

Das ist dasselbe Vorgehen wie in Sitzung 1, nur angewendet auf einen Defekt statt auf eine Aufgabe: zerlegen, einzeln prüfen, den geprüften Teil beiseitelegen. **Eine geprüfte Schicht ist eine Schicht, die man nicht mehr verdächtigen muss.**

## Wie man eine einzelne Schicht prüft (Frame 37)

Man gibt ihr eine bekannte Eingabe, sieht sich ihre Ausgabe an und lässt alles darunter weg. Bits hinein, Bits heraus. Keine Leuchtdiode, kein Sensor, kein Raumlicht.

Die Übersetzung von Text zu Bits lässt sich so am Schreibtisch prüfen, in einer Sekunde statt in einem ganzen Durchlauf. Wer das einmal gemacht hat, sucht nie wieder eine Stunde am Sensor nach einem Fehler, der in einer Schleife steckt.

## Warum unser Modul nicht alles versteckt (Frame 38)

`lifi_hardware` verbirgt USB, das Tinkerforge-Protokoll, Spannungen und den Treiber. Zwei Dinge zeigt es offen: **Integrationszeit** und **Verstärkung**.

Das ist Absicht. Diese beiden Regler sind der Zielkonflikt, den nur ihr entscheiden könnt, und zwar mit einer Messreihe. Eine Abstraktion, die euch die entscheidende Frage abnimmt, nimmt euch die Arbeit weg, für die ihr hier seid.

**Eine gute Schnittstelle verbirgt, was ihr nicht braucht, und zeigt, was ihr entscheiden müsst.** Dazu ist sie klein und stabil: Das Innenleben darunter darf sich ändern, ohne dass oben jemand etwas merkt. Eine Schnittstelle, die für jeden Sonderfall eine eigene Funktion anbietet, ist keine gute, sondern nur eine große.

## Zum Schluss (Frame 39)

Ihr wisst jetzt, was unter einem Schalter liegt. Und jede Schicht, die ihr selbst schreibt, ist auch einer: schmal von außen, groß von innen, und absichtlich so gebaut.
