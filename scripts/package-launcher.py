import hashlib,json,pathlib,re

root=pathlib.Path(__file__).resolve().parent.parent
version=json.loads((root/'launcher/manifest.json').read_text())['version']
assert re.fullmatch(r'\d+\.\d+\.\d+',version), 'Invalid launcher version'
asset=root/'launcher'/f'Fire-Tail-Launcher-Lite-{version}-Windows-x64.exe'
assert asset.is_file() and asset.stat().st_size>1_000_000, 'Missing native launcher'
assert asset.open('rb').read(2)==b'MZ', 'Expected Windows executable'
data={'schema':1,'version':version,'payload':{'kind':'launcher','platform':'win32-x64','url':f'https://github.com/Blaykker/FIRE_TAIL_RELEASES/releases/download/launcher-v{version}/{asset.name}','sha256':hashlib.file_digest(asset.open('rb'),'sha256').hexdigest(),'size':asset.stat().st_size}}
(root/'launcher-channel.json').write_text(json.dumps(data,indent=2)+'\n')
print(version)
