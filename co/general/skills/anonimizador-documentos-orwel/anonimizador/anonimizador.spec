# -*- mode: python ; coding: utf-8 -*-
import sys
import spacy.util
from pathlib import Path

block_cipher = None
model_src = Path(spacy.util.get_package_path("es_core_news_sm"))

a = Analysis(
    ['anonimizador.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('lista_blanca.json', '.'),
        ('reemplazos.json', '.'),
        (str(model_src), 'es_core_news_sm'),
    ],
    hiddenimports=[
        'docx', 'docx.opc', 'docx.oxml', 'lxml', 'lxml.etree',
        'spacy', 'spacy.lang.es', 'spacy.pipeline',
        'thinc', 'srsly', 'catalogue', 'cymem', 'preshed', 'murmurhash',
        'motor_anonimizacion', 'procesar_pdf', 'rutas_app', 'fitz', 'pymupdf',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Anonimizador-Trifuerza',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=sys.platform == 'darwin',
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

# En macOS genera Anonimizador-Trifuerza.app; en Windows, .exe
if sys.platform == 'darwin':
    app = BUNDLE(
        exe,
        name='Anonimizador-Trifuerza.app',
        icon=None,
        bundle_identifier='co.trifuerza.anonimizador',
    )
