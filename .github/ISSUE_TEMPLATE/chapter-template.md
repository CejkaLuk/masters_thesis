---
name: Chapter Template
about: Template for a chapter issue
title: ''
labels: enhancement
assignees: CejkaLuk

---

## General draft & post-supervisor quality points to check
### Grammar, Spelling, etc.
- [ ] Address and remove TODOs (including `\TODO`)
- [ ] Hyphenation:
  - [ ] "non-zero" is not as popular -> use "nonzero" instead
  - [ ] Replace all "sub-" prefixes with "sub" (for example: "sub-optimal" -> "suboptimal" - correct according to the Oxford dictionary)
- [ ] Full stops and commas:
  - [ ] Full stops and commas after equations if the equations are part of a sentence
  - [ ] Thousands separated by comma
  - [ ] Bullet points that are meant to be a part of the sentence should be separated by a comma and the last bullet should have a dot at the end (if it ends the sentence)
- [ ] Titles of Chapter/Section/etc. follow [correct capitalization](https://ksi.fjfi.cvut.cz/aktualne/anglicky-nazev-prace-pravidla-pro-psani-velkychmalych-pismen)
- [ ] Double-check spelling using TeXstudio and Grammarly
### Text formatting
- [ ] Numbers in the text must *not* be in math mode
- [ ] References to sections etc. have a capital letter in the text (`Section~\ref{}`, `Figure~\ref{}`, `Table~\ref{}`)
- [ ] Quotes, or statements in "" should be italicized
- [ ] No indented line after an object that slices a text in two
- [ ] Use "*" for multiplication only in in-line code, e.g., `U = R * I`
- [ ] Mathematics formatting:
  - [ ] Variables in _cursive_ font
  - [ ] Constants in non-cursive (using `\mathrm{}`)
  - [ ] Do not use "*" for multiplication in math mode as it signifies convolution
  - [ ] Use `\mathbf{}` for matrices and vectors (`\mathbb{}` is used for sets)
  - [ ] Shortcuts in sub- and super-script should not be in cursive, e.g. X^{new} "new" should not be cursive)
  - [ ]  `\nonumber\,.` should be before newline
- [ ] Code formatting:
  - [ ] Courier font and grey background (in-line and code block)
  - [ ] Check code in all `lstlistings` for correct syntax highlighting
  - [ ] Code blocks:
    - [ ] Consistent spacing in code - Do: `for( int... i++ )`; Don't: `for ()`
    - [ ] Consistent formatting of `{}` - Do: `void func()\n{ \n}`; Don't `void func() { \n}`
    - [ ] No spacing from the left part of the listing
- [ ] Citations in the text:
  - [ ] Spaces between text and citations
  - [ ] Multiple citations must be in one `\cite{a, b, c}` command, not `\cite{a}\cite{b}\cite{c}`
- [ ] Variables in _cursive_ font, e.g., ICM_x_ (_x_ can be one of 8, 16, 32)
- [ ] Consistent label names
  - Template: `{Type:chapter->section->subsection->subsubsection->specific-content-name}`
- [ ] No line overflowing (text, in-line code, etc.)
### Low priority
- [ ] TiKZ Figures:
  - [ ] Either convert the necessary figures to TiKZ OR create an issue to fix a specific figure
  - Some papers include the TiKZ source code

## Post-supervisor checks quality points
- [ ] Remove any `\TO`
