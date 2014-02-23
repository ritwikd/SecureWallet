# -*- mode: python -*-
a = Analysis(['securewallet.py'],
             pathex=['/media/ritwik/Important/workspace/securewallet'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='securewallet',
          debug=False,
          strip=None,
          upx=True,
          console=True )
