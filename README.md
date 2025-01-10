# LaTeX-Unterlagen

Dieses Repository enthält die LaTeX-Unterlagen zum Modul "Werkzeuge für das wissenschaftliche Arbeiten".

## Inhalt

Die Unterlagen entsprechen der Aufgabe 2 des Moduls. Es kann hilfreich sein, sich die dazugehörige PDF-Datei anzusehen.

## Erstellung der PDF

### Schritte:
1. Installieren Sie LaTeX:
   - Besuchen Sie [tug.org/texlive](https://tug.org/texlive/).
2. Erstellen Sie die PDF mit einem der folgenden Befehle:
   - Mit PDFLaTeX:
     ```bash
     pdflatex ./task.tex
     ```
     (mehrfach ausführen, bis die PDF vollständig ist).
   - Alternativ mit LaTeX Mk:
     ```bash
     latexmk -pdf ./task.tex
     ```

**Achtung**: LaTeX erstellt temporäre Dateien (z. B. `.aux`, `.log`), die gelöscht werden sollten, bevor Sie einen Commit durchführen.

## Hinweise

- Temporäre Dateien wie `.aux` und `.log` sollten nicht ins Repository geladen werden.
- Führen Sie vor einem Commit folgende Schritte aus:
  ```bash
  rm *.aux *.log