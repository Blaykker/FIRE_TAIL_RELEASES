import hashlib, json, pathlib, zipfile
root = pathlib.Path(__file__).resolve().parent.parent
client = root / "client"
version = json.loads((client / "client-version.json").read_text())["version"]
archive = root / f"Fire-Tail-Client-{version}.zip"
with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as output:
    for path in sorted(client.rglob("*")):
        if path.is_file():
            output.write(path, path.relative_to(client).as_posix())
data = {"schema": 1, "version": version, "notes": "Alpha 0.9.10: cartas tarot, dados de madeira, combate e recompensas revisados, relatos no pause e metricas opcionais.", "payload": {"kind": "web", "url": f"https://github.com/Blaykker/FIRE_TAIL_RELEASES/releases/download/v{version}/{archive.name}", "sha256": hashlib.file_digest(archive.open("rb"), "sha256").hexdigest(), "size": archive.stat().st_size, "entrypoint": "index.html"}}
(root / "channel.json").write_text(json.dumps(data, indent=2) + "\n")
if (root / 'launcher/manifest.json').exists():
    import subprocess,sys
    subprocess.check_output([sys.executable,str(root/'scripts/package-launcher.py')])
print(version)
