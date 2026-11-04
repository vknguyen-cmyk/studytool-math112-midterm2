# Math 112 Midterm 2: learning-goal map

An interactive study page that maps every Midterm 2 learning goal to the lecture items, homework problems, PCRQ questions, exit tickets and practice-exam problems that cover it.

## Use it

- **Online:** turn on GitHub Pages (Settings → Pages → Deploy from branch → `main` / root), then open `https://vknguyen-cmyk.github.io/math112-midterm2/`.
- **Locally:** run `python3 -m http.server` in this folder and open `http://localhost:8000`. Opening `index.html` straight from disk won't load the data, because browsers block `fetch()` on `file://`.

## Features

- Each goal lists its related items, labeled by source (e.g. `Lecture 12 · §1 Proposition 1.1`, `Homework 6 · Problem 4(e)`).
- `p.N ↗` opens the original PDF at the cited page.
- Filter by week, ★ practice-exam goals, weak spots, unmastered goals and source type, or search the question text.
- Tick questions as practiced and mark goals mastered. Outside the Claude artifact, progress is saved in your browser only.
- "Quiz me" writes new questions only inside the Claude artifact. Here it shows flashcards built from your own questions.

## Files

| Path | Contents |
| --- | --- |
| `index.html` | The page |
| `data.json` | Goals, items, labels and page numbers |
| `pdf/` | Lectures 9–16, Homework 5–9, PCRQs, exit tickets, Practice Exams 2A–2B |
| `source/` | Python that generated `data.json` (`items.py` = item catalog, `goals.py` = goal → item mapping) |
