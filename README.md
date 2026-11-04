# Math 112 Midterm 2 Study Tool

An interactive study page that maps every Midterm 2 learning goal to the lecture items, homework problems, PCRQ questions, exit tickets and practice-exam problems that cover it.

## Use it

- **Online:** turn on GitHub Pages (Settings → Pages → Deploy from branch → `main` / root), then open `https://vknguyen-cmyk.github.io/studytool-math112-midterm2/`.
- **Locally:** run `python3 -m http.server` in this folder and open `http://localhost:8000`. Opening `index.html` straight from disk won't load the data, because browsers block `fetch()` on `file://`.

## Features

- Each goal lists its related items, labeled by source (e.g. `Lecture 12 · §1 Proposition 1.1`, `Homework 6 · Problem 4(e)`).
- "Open PDF, page N" opens the original handout at that page.
- Filter by week or ★ practice-exam goals, or search the goals and questions.
- Every lecture passage, homework problem and practice-exam problem is cut directly from the original PDF, so it looks exactly like the handout. PCRQ and exit-ticket questions are typed out word for word.
- Check off goals you know. Outside the Claude artifact, this is saved in your browser only.
- "Quiz me" writes new questions only inside the Claude artifact. Here it steps through the goal's practice questions.

## Files

| Path | Contents |
| --- | --- |
| `index.html` | The page |
| `data.json` | Goals, items, labels and page numbers |
| `pdf/` | Lectures 9–16, Homework 5–9, Practice Exams 2A–2B |
| `img/` | Each passage and problem, cropped from the PDFs |
| `source/` | Scripts that build the page (`goals.py` = goal → item mapping, `typed.py` = PCRQ and exit-ticket questions, `crop.py` = PDF cropping) |
