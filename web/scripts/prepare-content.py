#!/usr/bin/env python3
"""Expand versioned, compressed content into both runtime asset directories."""
from pathlib import Path
import gzip,json,hashlib,subprocess,sys
root=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(root/'scripts/review-content.py')],check=True)
for name in ['questions','law-library']:
 source=root/'content'/(name+('.v9.json.gz' if name=='questions' else '.v7.json.gz'));raw=gzip.decompress(source.read_bytes());json.loads(raw)
 for target in [root/'dist'/(name+'.json'),root.parent/'android-offline/assets'/(name+'.json')]:target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(raw)
 print(name,hashlib.sha256(raw).hexdigest())
