# Leomar Montesa — Portfolio

Personal portfolio website of Leomar Montesa, IT Specialist based in Jeddah, Saudi Arabia.

## Structure

- `index.html` — the complete, self-contained site, with its HTML, CSS, JavaScript, portrait frames and logos inlined. This is the file that gets deployed.
- `src/index.src.html` — the editable source, with `__F0__`–`__N5__` placeholders for the portrait frames and `__L_name__` placeholders for the logos.
- `src/frames/` — the portrait frames: `f0`–`f5` (hologram) and `n0`–`n5` (clear photo), at 0°, 45°, 90°, 180°, 270° and 315°.
- `src/logos/` — company logos, each inlined once by the build script.
- `src/i18n/ar.json` — Arabic translations, keyed by the exact English text. When you change English text in the source, update its key here too.
- `assets/Leomar-Montesa-CV.pdf` — the final one-page CV (exported from Canva) behind the “Download CV” buttons. To update it, replace the file and keep the same name.
- `scripts/build.py` — inlines the frames, logos and Arabic translations into the source and regenerates `index.html`.

## Editing

1. Edit `src/index.src.html`.
2. Run `python3 scripts/build.py`.
3. Commit both files.

## Hosting

Hosting needs no build step: serve `index.html` as a static file on GitHub Pages, Netlify, Vercel or any web server.
For GitHub Pages, go to Settings → Pages → Deploy from a branch, and choose `main` / root.

## Features

- A responsive layout with a dark, futuristic theme, subtle 3D card tilt and a 3D network background.
- A rotatable 2.5D portrait built from six reference photos. A hologram power-on sequence resolves into the clear photo, and visitors can drag, swipe or use the arrow keys to rotate it.
- An intro-first homepage: the menu and the other sections stay hidden until the visitor selects “View experience” or “Get in touch” (they remain visible without JavaScript, and a direct link to a section opens it).
- Company logos in the experience timeline, and linked logos for each company website.
- English and Arabic (right-to-left) versions, and dark and light themes, switchable from the header and remembered for the next visit.
- A typewriter text reveal from the Skills section onward; each block types once, when it first scrolls into view.
- Respects `prefers-reduced-motion`, pauses animations when they are off-screen, and falls back to static content when canvas or IntersectionObserver is unavailable.
