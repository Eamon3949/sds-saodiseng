# Screenshots

Release-quality PNGs in this directory:

| File | What it shows |
|---|---|
| `hero.png` | Main window after a scan — TreeView + Treemap + AI chat busy, ~3440×1400 hero banner, Zen Gold theme. |
| `empty.png` | Empty/idle state — top "Pick a disk or folder" prompt, Studio list populated with detected scaffold chips, ~3440×1377 banner. |

How the existing shots were captured:

```bash
pnpm -C apps/desktop dev
# open http://127.0.0.1:1420 in Chrome
# DevTools → Device toolbar → Responsive 1280×720
# Click Scan → drag a folder into the AI chat → screenshot
# Save to docs/screenshots/hero.png and docs/screenshots/empty.png
```

The historical `01-scan.png` / `02-scaffold.png` / `03-advisor.png` filenames
were retired when the docs were consolidated to the hero/empty banner pair.
Don't reintroduce them — the README only links to `hero.png` and `empty.png`.
