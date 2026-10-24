import hashlib, json, pathlib, zipfile
root = pathlib.Path(__file__).resolve().parent.parent
client = root / "client"
version = json.loads((client / "client-version.json").read_text())["version"]
archive = root / f"Fire-Tail-Client-{version}.zip"
with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as output:
    for path in sorted(client.rglob("*")):
        if path.is_file():
            output.write(path, path.relative_to(client).as_posix())
data = {"schema": 1, "version": version, "notes": "Rounded pixel dialogue, mouse crew polish, faster dice clash and quieter participant arenas. Alpha development build.", "payload": {"kind": "web", "url": f"https://github.com/Blaykker/FIRE_TAIL_RELEASES/releases/download/v{version}/{archive.name}", "sha256": hashlib.file_digest(archive.open("rb"), "sha256").hexdigest(), "size": archive.stat().st_size, "entrypoint": "index.html"}}
(root / "channel.json").write_text(json.dumps(data, indent=2) + "\n")
launcher = root / 'launcher' / 'Fire-Tail-Launcher-Lite-0.2.4-Windows-x64.exe'
if launcher.exists():
    launcher_data = {'schema': 1, 'version': '0.2.4', 'payload': {'kind': 'launcher', 'platform': 'win32-x64', 'url': f'https://github.com/Blaykker/FIRE_TAIL_RELEASES/releases/download/v{version}/{launcher.name}', 'sha256': hashlib.file_digest(launcher.open('rb'), 'sha256').hexdigest(), 'size': launcher.stat().st_size}}
    (root / 'launcher-channel.json').write_text(json.dumps(launcher_data, indent=2) + '\n')
print(version)
