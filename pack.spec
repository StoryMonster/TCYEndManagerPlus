# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['.\\src\\main.py'],
             pathex=['.\\src\\main_window.py',
                     '.\\src\\components\\browser.py',
                     '.\\src\\components\\wx_client_ctrl_item.py',
                     '.\\src\\components\\wx_clients_ctrl_panel.py',
                     '.\\src\\components\\wx_clients_display_panel.py',
                     '.\\src\\components\\wx_clients_panel.py'],
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
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='同城游微信游戏多开工具',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='TcyWechatGameHelper')
