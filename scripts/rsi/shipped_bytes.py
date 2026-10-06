"""Bytes a profile visitor downloads: committed size at HEAD of README.md plus each distinct local image that
README.md actually loads (hero, showcase shots, product icons, legend glyphs, footer). Images in icons/ that
README.md does not reference are never downloaded and are not counted. A repeated image (e.g. icons/_site.svg)
counts once, since the browser caches it. Prints shipped_bytes=<n>."""
import re
import subprocess
import sys
import urllib.parse

listing = subprocess.run(["git", "ls-tree", "-r", "-l", "-z", "HEAD"], capture_output=True, check=True).stdout
sizes = {}
for entry in listing.split(b"\0"):
    if not entry:
        continue
    meta, path = entry.decode("utf-8", "replace").split("\t", 1)
    size = meta.split()[3]
    if size != "-":
        sizes[path] = int(size)

readme = subprocess.run(["git", "show", "HEAD:README.md"], capture_output=True, check=True).stdout
readme = readme.decode("utf-8", "replace")

# <img src="..."> and markdown ![alt](...) image references.
REF = re.compile(r"""(?:\bsrc\s*=\s*["']|!\[[^\]]*\]\(\s*<?)([^"')\s>]+)""", re.IGNORECASE)
refs = set()
for match in REF.finditer(readme):
    ref = match.group(1).split("#", 1)[0].split("?", 1)[0]
    if not ref or "://" in ref or ref.startswith(("//", "data:", "mailto:")):
        continue  # remote (shields.io badges etc.) or inline: not served from this repo
    ref = urllib.parse.unquote(ref).lstrip("/")
    while ref.startswith("./"):
        ref = ref[2:]
    refs.add(ref)

missing = sorted(r for r in refs if r not in sizes)
if missing:
    sys.exit("README.md references files missing at HEAD: " + ", ".join(missing))

total = sizes.get("README.md", 0) + sum(sizes[r] for r in refs)
print(f"shipped_bytes={total}")
