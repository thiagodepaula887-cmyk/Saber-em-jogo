#!/usr/bin/env python3
"""Generate a validated unsigned AAB; optionally sign with a private JSON config.
No private signing material is stored in the repository.
"""
from pathlib import Path
import subprocess,os,zipfile,json,sys
root=Path(__file__).resolve().parent;sdk=Path(os.environ.get('QUIZ_ANDROID_TOOLS',str(root.parent/'android-toolchain')));build=root/'build'
def run(*args):subprocess.run([str(a) for a in args],check=True,cwd=root)
if not (build/'dex/classes.dex').exists():raise SystemExit('Execute build.py antes.')
aapt=sdk/'android-15/aapt2';proto=build/'proto.apk'
run(aapt,'compile','--dir',root/'res','-o',build/'bundle-res.zip')
run(aapt,'link','--proto-format','-o',proto,'--manifest',root/'AndroidManifest.xml','-I',sdk/'android-36/android.jar','-A',root/'assets',build/'bundle-res.zip')
module=build/'base-module.zip'
with zipfile.ZipFile(proto) as src,zipfile.ZipFile(module,'w',zipfile.ZIP_DEFLATED) as out:
 for name in src.namelist():out.writestr('manifest/AndroidManifest.xml' if name=='AndroidManifest.xml' else name,src.read(name))
 out.write(build/'dex/classes.dex','dex/classes.dex')
output=root.parent/'Saber_em_Jogo_0.9_Play_Unsigned.aab'
run('java','-jar',sdk/'bundletool.jar','build-bundle','--modules='+str(module),'--output='+str(output),'--overwrite')
run('java','-jar',sdk/'bundletool.jar','validate','--bundle='+str(output))
if len(sys.argv)>1:
 config=json.loads(Path(sys.argv[1]).read_text());signed=root.parent/'Saber_em_Jogo_0.9_Play.aab'
 env=os.environ.copy();env['QUIZ_STORE_PASSWORD']=config['storePassword'];env['QUIZ_KEY_PASSWORD']=config['keyPassword']
 subprocess.run(['java','-m','jdk.jartool/sun.security.tools.jarsigner.Main','-keystore',config['keystore'],'-storepass:env','QUIZ_STORE_PASSWORD','-keypass:env','QUIZ_KEY_PASSWORD','-signedjar',str(signed),str(output),config['alias']],env=env,check=True)
 run('java','-m','jdk.jartool/sun.security.tools.jarsigner.Main','-verify',signed)
 print(signed)
else:print(output)
