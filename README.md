# MachineLearning
# Projekt-Dokumentation

Lennard Bühler, Filip Kritzner

| Datum | Version | Zusammenfassung                                              |
| ----- | ------- | ------------------------------------------------------------ |
|10.01.25| 0.0.1   |Informiert und geplant|
|17.01.25| 0.0.2   |Anfangen von Realisieren und der Dokumentation|
|24.01.25| 0.0.3   |Angefangen Modell zu erstellen|
|31.01.25| 0.0.4  |Modell Training, GUI angefangen|
|21.02.254| 0.0.5   |GUI weitergearbeitet|
|28.02.25| 0.0.6   |Modell finalisiert, GUI finalisiert|
|07.03.25| 1.0.0   |Dokumentation und Programm fertiggestellt|

## 1 Informieren

### 1.1 Ihr Projekt

Ein Bildklassifikationsmodell basierend auf dem CIFAR-10-Datensatz, das hochgeladene Bilder analysiert und eine Klassifizierung ermöglicht. Ausserdem gibt es ein GUI mit Tkinter.


### 1.2 User Stories

| US-№ | Verbindlichkeit | Typ  | Beschreibung                       |
| ---- | --------------- | ---- | ---------------------------------- |
| 1    |   Muss              | Funtional     | Als User möchte ich wissen wie genau das Modell ist.|
| 2  |   Muss              |  Funtional    |   Als User möchte ich Bilder hochladen können, die klassifiziert werden.|
| 3  |       Muss          | Funtional     |   Als User möchte ich, dass der CIFAR-10 Datensatz verwendet wird.                      |
| 4  |     Kann            |   Qualität   |  Als User möchte ich, dass ich ein Klassifikations-Ergebnis erhalte, damit ich weiss was man auf dem Bild sieht.                   |
| 5  |     Muss            |Funktional      |Als User möchte ich, dass das Modell um die 70% Genauigkeit hat, damit viele Bilder richtig klassifiziert werden. |
| 6  |   Muss              | Funktional     |  Als User möchte ich, dass die Bilder, die ich hochlade, in jeder Grösse akzeptiert werden. |
| 7  |   Muss              |  Rand    |   Als User möchte ich, dass das Model gespeichert wird und nicht jedes Mal neu kompiliert und trainiert werden muss.  |


### 1.3 Testfälle

| TC-№ | Ausgangslage | Eingabe | Erwartete Ausgabe |
| ---- | ------------ | ------- | ----------------- |
| 1.1  |     Benutzer lädt ein Bild hoch.        |Beliebiges Bild im PNG/JPG-Format.     |   Das Bild wird erfolgreich verarbeitet und skaliert.|
| 2.1  |   Benutzer lädt ein nicht unterstütztes Format hoch.         | Bild im BMP oder GIF-Format.      | Fehlermeldung: „Ungültiges Bildformat.“                |
| 3.1  |  Benutzer lädt ein sehr großes Bild hoch.            |Bild mit 4000x4000 Pixeln.       | Das Bild wird skaliert und akzeptiert.               |
| 4.1  | SBenutzer lädt ein sehr kleines Bild hoch.             |Bild mit 10x10 Pixeln.         |   Das Bild wird skaliert und akzeptiert.               |
| 5.1  | Benutzer lädt ein Bild hoch.           |Bild mit einem CIFAR-10-ähnlichen Objekt.        |    Eine Klassifikation aus den 10 Kategorien wird zurückgegeben.              |
| 6.1  | Benutzer lädt ein zufälliges Bild hoch.        | Bild, das nicht in CIFAR-10 vorkommt.     | Möglicherweise falsche Klassifikation mit niedrigerer Wahrscheinlichkeit.       |
| 7.1  |Benutzer wiederholt eine Vorhersage.        |    Gleiches Bild mehrmals hochladen.     |  Konsistente Klassifikation bei jedem Upload.               |
| 8.1  | System verwendet ein gespeichertes Modell.            | Bild hochladen.        |  Modellklassifikation erfolgt ohne erneutes Training.             |
|9.1   |System läuft ohne GPU.                      |Bild hochladen.              |Modell führt die Klassifikation erfolgreich auf der CPU durch.|
|10.1  |System ist offline.                         |Bild hochladen.              |Fehlermeldung: „Keine Verbindung zum Klassifikationsserver.“|






### 1.4 Diagramme

![WhatsApp Image 2025-03-07 at 11 31 51](https://github.com/user-attachments/assets/e8ff33d8-a013-49b5-921e-db925b266498)


## 2 Planen

| AP-№ | Frist | Zuständig | Beschreibung | geplante Zeit |
| ---- | ----- | --------- | ------------ | ------------- |
| 1.A  | 24.01.2025 | Lennard | Projektstruktur erstellen (Ordnerstruktur, Git-Repo einrichten) | 120 min |
| 2.A  | 24.01.2025 | Filip | CIFAR-10-Datensatz vorbereiten (Download, Vorverarbeitung, Normalisierung) | 120 min |
| 3.A  | 24.01.2025| Lennard | Neurales Netzwerk definieren (CNN-Modellarchitektur in TensorFlow/Keras erstellen) | 120 min |
| 4.A  | 31.01.2025 | Filip | Trainingsprozess implementieren (Modell trainieren und evaluieren) | 120 min |
| 5.A  | 31.01.2025 | Lennard | Trainiertes Modell speichern (Gewichte und Architektur sichern) | 120 min |
| 6.A  | 31.01.2025 | Filip | Modell laden und für Inferenz nutzen | 120 min |
| 7.A  | 21.02.2025 | Lennard | Bild-Upload-Funktion bereitstellen (Upload-Funktion für Benutzer einrichten) | 120 min |
| 8.A  | 21.02.2025 | Filip | Bilder auf Standardgröße bringen (Hochgeladene Bilder auf CIFAR-10-Format skalieren) | 120 min |
| 9.A  | 21.02.2025 | Lennard | Vorhersagepipeline implementieren (Bild in das Modell einspeisen und Label zurückgeben) | 120 min |
| 10.A | 21.02.2025 | Filip | Genauigkeitsprüfung des Modells durchführen | 120 min |
| 11.A | 21.02.2025 | Lennard | Fehlermeldungen bei ungültigen Bildern anzeigen | 120 min |
| 12.A | 28.02.2025 | Filip | Testfälle für unterschiedliche Bildgrößen entwickeln | 120 min |
| 13.A | 28.02.2025 | Lennard | Benutzeroberfläche für den Upload erstellen (Web oder CLI) | 120 min |
| 14.A | 28.02.2025 | Filip | Performance-Optimierung des Modells (z. B. Batch-Normalisierung, Dropout anpassen) | 120 min |
| 15.A | 28.02.2025 | Lennard | Logging und Fehlerhandling integrieren | 120 min |
| 16.A | 28.02.2025 | Filip | Dokumentation für Benutzer und Entwickler schreiben | 120 min |
| 17.A | 28.02.2025 | Lennard | Automatische Tests für die Bildverarbeitung implementieren | 120 min |
| 18.A | 28.02.2025 | Filip | Vergleich mit anderen vortrainierten Modellen durchführen | 120 min |
| 19.A | 28.02.2025 | Lennard | Finale Tests durchführen und Genauigkeit messen | 120 min |
| 20.A | 28.02.2025 | Filip | Deployment für Web-Anwendung oder API vorbereiten | 120 min |

## 3 Entscheiden

In unserem Projekt haben wir mehrere wichtige Entscheidungen getroffen, um eine effiziente Umsetzung zu gewährleisten. Zunächst haben wir uns für die Verwendung von TensorFlow/Keras entschieden, da es eine leistungsstarke und gut dokumentierte Bibliothek für neuronale Netze ist. Zudem haben wir den CIFAR-10-Datensatz als Grundlage gewählt, weil er ideal für Bildklassifikationsaufgaben geeignet ist.

## 4 Realisieren

| AP-№ | Datum  | Zuständig | geplante Zeit | tatsächliche Zeit |
| ---- | ------ | --------- | ------------- | ----------------- |
| 1.A  | 24.01.2025 | Lennard | 120 min | 130 min |
| 2.A  | 24.01.2025 | Filip   | 120 min | 110 min |
| 3.A  | 24.01.2025 | Lennard | 120 min | 125 min |
| 4.A  | 31.01.2025 | Filip   | 120 min | 130 min |
| 5.A  | 31.01.2025 | Lennard | 120 min | 120 min |
| 6.A  | 31.01.2025 | Filip   | 120 min | 115 min |
| 7.A  | 21.02.2025 | Lennard | 120 min | 135 min |
| 8.A  | 21.02.2025 | Filip   | 120 min | 110 min |
| 9.A  | 21.02.2025 | Lennard | 120 min | 125 min |
| 10.A | 21.02.2025 | Filip   | 120 min | 120 min |
| 11.A | 21.02.2025 | Lennard | 120 min | 110 min |
| 12.A | 28.02.2025 | Filip   | 120 min | 130 min |
| 13.A | 28.02.2025 | Lennard | 120 min | 140 min |
| 14.A | 28.02.2025 | Filip   | 120 min | 120 min |
| 15.A | 28.02.2025 | Lennard | 120 min | 115 min |
| 16.A | 28.02.2025 | Filip   | 120 min | 125 min |
| 17.A | 28.02.2025 | Lennard | 120 min | 135 min |
| 18.A | 28.02.2025 | Filip   | 120 min | 120 min |
| 19.A | 28.02.2025 | Lennard | 120 min | 130 min |
| 20.A | 28.02.2025 | Filip   | 120 min | 110 min |





## 5 Kontrollieren

| TC-№ | Datum | Resultat | Tester |
| ---- | ----- | -------- | ------ |
| 1.1  |  28.02.2025    |Funktioniert|  Filip und Lennard       |
| 2.1  |28.02.2025        |Funktioniert|  Filip und Lennard        |
| 3.1  |28.02.2025       |Funktioniert|  Filip und Lennard        |
| 4.1  |28.02.2025       |Funktioniert| Filip und Lennard         |
| 5.1  |28.02.2025       |Funktioniert nicht| Filip und Lennard         |
| 6.1  | 28.02.2025       |Funktioniert| Filip und Lennard         |
| 7.1  | 28.02.2025       |Funktioniert| Filip und Lennard         |
| 8.1  | 28.02.2025      |Funktioniert| Filip und Lennard         |
| 9.1  | 28.02.2025      |Funktioniert| Filip und Lennard         |
| 10.1  | 28.02.2025      |Funktioniert| Filip und Lennard         |



## Fazit
Das Projekt war insgesamt ein grosser Erfolg, auch wenn wir vor einigen Herausforderungen standen, die wir jedoch gemeinsam bewältigen konnten. Durch eine klare Aufgabenverteilung und gute Zusammenarbeit im Team konnten wir effizient arbeiten und wertvolle Erfahrungen sammeln. Besonders erfreulich war, dass die Implementierung unseres Modells sowie die Testphase ohne größere Probleme verliefen und fast alle unsere Ziele erreicht wurden. Rückblickend sind wir stolz auf das Ergebnis und nehmen viele neue Erkenntnisse für zukünftige Projekte mit.
