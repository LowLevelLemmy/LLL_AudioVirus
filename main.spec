# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['AudioVirus.py'],
             pathex=['C:\\Folders\\yt\\LLL\\videos\\AudioVirus\\AudVirus'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)


for d in a.datas:
    if 'pyconfig' in d[0]:
        a.datas.remove(d)
        break

a.datas += [('Logo.png','C:\\Folders\\yt\\LLL\\videos\\AudioVirus\\AudVirus\\Logo.png', 'Data'),
('intro.mp3','C:\\Folders\\yt\\LLL\\videos\\AudioVirus\\AudVirus\\intro.mp3', 'Data'),
('outro.mp3','C:\\Folders\\yt\\LLL\\videos\\AudioVirus\\AudVirus\\outro.mp3', 'Data')]


pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='LLLs AudioVirus',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          icon='favicon.ico')