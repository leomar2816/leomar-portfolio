"""Inline the portrait frames into src/index.src.html and write index.html (self-contained page).
Usage: python3 scripts/build.py"""
import base64, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
s = (root / 'src' / 'index.src.html').read_text(encoding='utf-8')
for p in 'FN':
    for i in range(6):
        data = (root / 'src' / 'frames' / f'{p.lower()}{i}.webp').read_bytes()
        s = s.replace(f'__{p}{i}__', 'data:image/webp;base64,' + base64.b64encode(data).decode())
assert '__F' not in s and '__N' not in s, 'unreplaced placeholder'
(root / 'index.html').write_text(s, encoding='utf-8')
print('index.html written,', len(s)//1024, 'KB')
