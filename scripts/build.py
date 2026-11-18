"""Inline the portrait frames, logos and Arabic translations into src/index.src.html and write index.html (self-contained page).
Usage: python3 scripts/build.py"""
import base64, pathlib, re
root = pathlib.Path(__file__).resolve().parent.parent
s = (root / 'src' / 'index.src.html').read_text(encoding='utf-8')
def uri(path): return 'data:image/webp;base64,' + base64.b64encode(path.read_bytes()).decode()
for p in 'FN':
    for i in range(6):
        s = s.replace(f'__{p}{i}__', uri(root / 'src' / 'frames' / f'{p.lower()}{i}.webp'))
cache = {}
def logo(m):
    n = m.group(1)
    if n not in cache: cache[n] = uri(root / 'src' / 'logos' / f'{n}.webp')
    return cache[n]
s = re.sub(r'__L_([a-z0-9]+)__', logo, s)
import json
ar = json.loads((root / 'src' / 'i18n' / 'ar.json').read_text(encoding='utf-8'))
s = s.replace('__I18N_AR__', json.dumps(ar, ensure_ascii=False).replace('</', '<\\/'))
assert not re.search(r'__[FNL][_0-9]|__I18N_', s), 'unreplaced placeholder'
(root / 'index.html').write_text(s, encoding='utf-8')
print('index.html written,', len(s)//1024, 'KB')
