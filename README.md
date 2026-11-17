# Leomar Montesa — Portfolio

Personal portfolio website of Leomar Montesa, IT Specialist based in Jeddah, Saudi Arabia.

## Structure

- `index.html` — the complete, self-contained site (HTML, CSS, JS and portrait frames inlined). This is what gets deployed.
- `src/index.src.html` — editable source with `__F0__…__N5__` placeholders for the portrait frames.
- `src/frames/` — portrait frames: `f0–f5` hologram, `n0–n5` clear photo, at 0°, 45°, 90°, 180°, 270° and 315°.
- `scripts/build.py` — inlines the frames into the source and regenerates `index.html`.

## Editing

1. Edit `src/index.src.html`.
2. Run `python3 scripts/build.py`.
3. Commit both files.

## Hosting

No build step is needed to host it: serve `index.html` as a static file (GitHub Pages, Netlify, Vercel, any web server).
For GitHub Pages: Settings → Pages → Deploy from a branch → `main` / root.

## Features

- Responsive layout, dark futuristic theme, subtle 3D card tilt and a 3D network background.
- Rotatable portrait (2.5D, built from six reference photos): hologram power-on sequence that resolves into the clear photo; drag, swipe or arrow keys to rotate.
- Respects `prefers-reduced-motion`; pauses animation off-screen; static fallback when canvas is unavailable.
