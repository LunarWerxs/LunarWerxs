"""Bytes a profile visitor downloads: committed size at HEAD of README.md and the images under icons/. Prints shipped_bytes=<n>."""
import subprocess

IMAGES = (".svg", ".png", ".jpg", ".jpeg", ".webp", ".avif", ".gif", ".ico")
listing = subprocess.run(["git", "ls-tree", "-r", "-l", "-z", "HEAD"], capture_output=True, check=True).stdout
total = 0
for entry in listing.split(b"\0"):
    if not entry:
        continue
    meta, path = entry.decode("utf-8", "replace").split("\t", 1)
    size = meta.split()[3]
    parts = path.split("/")
    if size == "-" or any(p.startswith(".") for p in parts):
        continue
    if path == "README.md" or (parts[0] == "icons" and path.lower().endswith(IMAGES)):
        total += int(size)
print(f"shipped_bytes={total}")
