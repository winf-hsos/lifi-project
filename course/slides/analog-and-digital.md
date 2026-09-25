<!-- Lecture notes for the slides on `analog-and-digital`, written in German. They follow the slides in order; frame numbers refer to the deck. The slides themselves are embedded on https://docs.lifi-project.de/concepts/analog-and-digital.html -->

# Skript: drawing the line

Dieser Text erläutert den Input zum Konzept „Analog und digital" zum Nachlesen. Er folgt der Reihenfolge der Folien, die Verweise zählen Frames (jeder Aufbauschritt ist ein eigener Frame), lässt sich aber auch ohne die Folien lesen.

Der Satz ist der erste von zwei Inputs derselben Sitzung; der zweite, [what light means](../06-symbols-and-information/skript.md), macht aus unterscheidbaren Zuständen Symbole und Information zählbar.

## Ist das digital? (Frame 4)

Ein Bahnhof vor der Chip-Zeit. Die Fallblattanzeige klappert, Buchstabe für Buchstabe fällt an seinen Platz. Kein Computer weit und breit, und trotzdem ist das Ding lupenrein digital.

Jedes Blatt kennt genau zwei Lagen, oben oder unten. Beim Umklappen gibt es keinen gültigen Zwischenzustand, und genau deshalb ist die Anzeige aus zwanzig Metern lesbar.

## Digital ist nicht dasselbe wie elektronisch (Frame 5)

Digital sind die von Hand umgeklappte Anzeigetafel aus der Sporthalle, der Lichtschalter, der Abakus und der Würfel. Analog sind Rechenschieber, Zeigerthermometer, Dimmer und Sanduhr. Kein einziges dieser Dinge enthält einen Chip.

Elektronik ist nur der heute übliche Träger, nicht das Merkmal. Andersherum gilt dasselbe: Ein Verstärker ist elektronisch und trotzdem stufenlos.

## Das Wort dafür (Frame 6)

**Digital heißt: endlich viele Zustände, und nichts dazwischen zählt.** Beide Hälften tragen. Die erste ist die harmlose, die zweite ist die, an der die ganze Technik hängt: Weil zwischen den Zuständen nichts gilt, verschwindet dort auch jede Störung.

## Das Stück, das kein Programm kontrolliert (Frame 7)

Der Sender macht aus Zahlen Licht, der Sensor macht aus Licht wieder Zahlen: digital, analog, digital. Die Mitte ist Physik. Sie ist stufenlos und gestört von Umgebungslicht, Abstand und Rauschen, und kein Programm der Welt kontrolliert sie.

Wer diese analoge Mitte vergisst, wundert sich später über jede Störung. Wer sie ernst nimmt, weiß, warum gemessen werden muss.

## Stufenlos gegen Zustände (Frames 8 und 9)

Licht ist analog: Zwischen zwei Helligkeiten liegt immer noch eine dritte, es gibt keine kleinste Stufe. Euer Programm braucht das Gegenteil, nämlich endlich viele, klar voneinander getrennte Zustände.

Ein Signal zu digitalisieren heißt nichts anderes, als es durch eine endliche Folge von Zahlen darzustellen.

## Gleiches Rauschen, mehr Bereiche (Frames 10 bis 12)

Dreimal dieselbe Messung mit demselben Schwankungsband, und nur die Zahl der Bereiche wächst. Bei zwei Bereichen liegt das Band bequem im eigenen Bereich. Bei vier wird es knapp. Bei acht überragt dasselbe Band die Grenzen, und einzelne Messungen landen im Nachbarbereich.

Nicht das Rauschen wächst, der Abstand schrumpft. Der Abstand zwischen den Bereichen ist eure Sicherheitsreserve, und mehr Bereiche verteilen dieselbe Reserve auf mehr Grenzen. Damit ist die Wettbewerbsfrage von Challenge 1 gestellt, bevor sie gestellt wird.

## Was die weggeworfene Genauigkeit einkauft (Frame 13)

Zwei Kopierketten. Die Kassette kopiert ihre stufenlose Welle mitsamt allem Rauschen und legt bei jeder Generation eigenes darauf; hörbar schlechter mit jeder Kopie. Die Datei wird bei jeder Kopie aus sauberen Zuständen neu geboren: ablesen, frisch setzen, fertig.

Jede Störung, die kleiner ist als der Zustandsabstand, verschwindet dabei vollständig. Deshalb ist digitale Technik zuverlässig, nicht obwohl, sondern **weil** sie Information wegwirft. Und deshalb ist die tausendste Dateikopie das Original.

## Digitalisieren wirft Information weg (Frame 15)

Welcher der unendlich vielen Werte innerhalb eines Bereichs es wirklich war, ist nach der Zuordnung nicht mehr feststellbar. Digitalisieren ist eine Einbahnstraße. Das ist kein Unfall, sondern der Kaufpreis für alles, was der vorige Abschnitt gezeigt hat.

## Die zwei Schnitte (Frames 16 und 17)

Digitalisieren besteht immer aus zwei Schnitten, und an einem Foto sieht man beide.

Der **erste Schnitt geht durch die Fläche**: Aus dem stufenlosen Bild werden Messpunkte, auf der Folie sechzehn mal sechzehn. Das ist die **Abtastung** (sampling), und wie fein sie ausfällt, ist die **Auflösung**.

Der **zweite Schnitt geht durch den Wert**: Die Helligkeit jedes Punkts wird auf eine der vereinbarten Stufen gerundet, auf der Folie auf vier Graustufen. Das ist die **Quantisierung**, und die Zahl der Stufen ist die **Farbtiefe**. Die Stufen sind genau die Bereiche von vorhin, nur jetzt auf ein Bild angewendet.

## Welcher Schnitt war zu grob? (Frame 18)

Beide Schnitte werfen Detail weg, aber sie hinterlassen verschiedene Spuren, und daran erkennt man, an welchem Regler zu drehen ist.

**Klötzchen** heißt zu wenige Punkte, also zu grobe Abtastung. **Harte Flecken in glatten Verläufen** heißen zu wenige Stufen, also zu grobe Quantisierung. Das lohnt sich zu merken, es kommt in der Werkstatt zurück.

## Was ein Bild kostet (Frame 19)

Die eine Rechnung, die jede Dateigröße trägt: **Punkte mal Bits je Punkt.** Ein Bild mit 64 mal 64 Punkten in 24 Bit Farbe sind 98.304 Bit, also 12 KB. Dasselbe Bild mit einem Bit je Punkt sind 4.096 Bit, also 512 Byte.

Auf eurer Lichtstrecke wird daraus sofort Zeit. Bei 30 bit/s braucht das erste Bild knapp eine Stunde, das zweite zwei Minuten. Auflösung und Farbtiefe sind damit keine Feinheiten, sondern die beiden Hebel, an denen die Übertragungsdauer hängt: Was ihr behaltet, bezahlt ihr in Minuten.

## Wie weit kann man gehen? (Frames 20 bis 23)

Dasselbe Foto, immer gröber: 128, 32, 8 und schließlich 2 Punkte je Kante. Irgendwo dazwischen kippt die Erkennbarkeit, und wo genau, darüber wird der Saal uneins sein.

Genau diese Uneinigkeit ist der Punkt. Es gibt kein richtiges Maß, es gibt nur eine Abwägung gegen die Übertragungszeit. In Challenge 4 habt ihr 2 KB, und dann steht diese Frage wirklich an.

## Selbst ausprobieren (Frame 24)

Im [Photo Digitiser](https://winf-hsos.github.io/lifi-concept-demos/photo-digitiser/) wählt ihr Auflösung und Farbtiefe selbst, seht sofort das Ergebnis und daneben die Rechnung samt Übertragungsdauer über die Lichtstrecke. Zwei Fragen lohnen sich: Bei welcher Einstellung würdet ihr das Bild noch verschicken? Und was spart mehr, die halbe Auflösung oder die halbe Farbtiefe?

## Dieselben zwei Schnitte für Ton (Frame 25)

Die zwei Schnitte sind kein Bildthema, sie sind das Verfahren. Beim Ton zerlegt die **Abtastrate** die Zeit statt der Fläche, und die **Bit-Tiefe** die Lautstärke statt der Helligkeit. 44.100 Messungen je Sekunde mit 16 Bit, das ist eine CD.

Im [Audio Digitiser](https://winf-hsos.github.io/lifi-concept-demos/audio-digitiser/) wird beides hörbar: Dreht die Abtastrate herunter, bis eine Stimme blechern wird.

## Wo euer Alphabet geboren wird (Frame 27)

```python
value = sensor.get_clear()

if value > 250:
    symbol = "bright"
else:
    symbol = "dark"
```

Diese eine Grenze im Code ist die Stelle, an der aus Hunderten möglicher Messwerte zwei Symbole werden. Sie ist keine Naturkonstante, sondern eure Entscheidung, und ab hier gilt sie und nicht die Physik.

Wo sie liegt, kommt nicht aus dem Bauch, sondern aus den Steckbriefen eurer Messreihe: erst kalibrieren, dann vergleichen.

## Wie viele Farben sind sicher? (Frames 28 und 29)

Zwei sind sicher, acht sind schnell, und irgendwo dazwischen liegt euer Alphabet. Wo genau, weiß nur eure eigene Messreihe: Die Bereichsbreite muss zur Schwankung passen, sonst rutschen einzelne Messungen in den Nachbarbereich.

## Zum Schluss (Frames 30 und 31)

Ihr entscheidet, wo die Grenzen liegen. Ab da gilt eure Entscheidung und nicht die Physik. Die Physik liefert einen stufenlosen Wertebereich und keine einzige Grenze dazu; jede Grenze in eurem System steht dort, weil ihr sie hingeschrieben habt. Deshalb ist sie auch euer Problem, wenn sie falsch liegt.
