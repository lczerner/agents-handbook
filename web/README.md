# web/

`handbook.html` is the source of the published one-page handbook. It contains
both the English and Czech versions with a language switcher, and is otherwise
the same material as `HANDBOOK.md` + `WALKTHROUGHS.md` + `PROMPTS.md`.

Published at: https://claude.ai/code/artifact/d4440c12-5a6d-46d1-b421-2bc930337e6c
(private until shared from the page's share menu)

To update the published page, edit this file and republish it to the same URL.

Notes on how it works:
- One page, two content trees: `<div class="doc" data-lang="en">` and
  `data-lang="cs"`, plus a matching pair of `.navcol` sidebars.
- CSS shows English by default, so the page still works without JavaScript.
- An inline script at the top picks the language before first paint: a stored
  choice in `localStorage`, otherwise the browser locale (`cs*` gets Czech).
- Czech section ids are the English ones prefixed with `cs-`, so switching
  language keeps the reader on the same section.
- Self-contained by necessity: the artifact host blocks every external
  request, so there are no CDN fonts, scripts, or images.
