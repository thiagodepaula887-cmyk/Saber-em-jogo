#!/usr/bin/env python3
"""Compila o APK offline usando SDK Android 35, build-tools 35 e ECJ/Java 17.
Assinatura padrão de TESTE: não usar esta chave em publicação de produção.
"""
from pathlib import Path
import subprocess,os,zipfile,sys,shutil
root=Path(__file__).resolve().parent
sdk=Path(os.environ.get('QUIZ_ANDROID_TOOLS',str(root.parent/'android-toolchain')))
bt=sdk/'android-15';platform=sdk/'android-35'/'android.jar'
build=root/'build'
if build.exists():shutil.rmtree(build)
build.mkdir(exist_ok=True);(build/'classes').mkdir(exist_ok=True);(build/'dex').mkdir(exist_ok=True)
def run(*args):subprocess.run([str(a) for a in args],check=True,cwd=root)
run(bt/'aapt2','compile','--dir',root/'res','-o',build/'resources.zip')
run(bt/'aapt2','link','-o',build/'base.apk','--manifest',root/'AndroidManifest.xml','-I',platform,'-A',root/'assets',build/'resources.zip')
run('java','-jar',sdk/'ecj.jar','-1.8','-proc:none','-bootclasspath',platform,'-d',build/'classes',*root.glob('src/**/*.java'))
classes=list((build/'classes').rglob('*.class'))
run(bt/'d8','--lib',platform,'--min-api','26','--output',build/'dex',*classes)
with zipfile.ZipFile(build/'base.apk','a',zipfile.ZIP_DEFLATED) as apk:apk.write(build/'dex/classes.dex','classes.dex')
run(bt/'zipalign','-f','-p','4',build/'base.apk',build/'aligned.apk')
key=root/'test-signing.keystore'
if not key.exists():run('keytool','-genkeypair','-keystore',key,'-storepass','android','-keypass','android','-alias','androiddebugkey','-keyalg','RSA','-keysize','2048','-validity','10000','-dname','CN=Saber em Jogo Teste, O=Desenvolvimento, C=BR')
output=root.parent/'Saber_em_Jogo_0.6_Android.apk'
run(bt/'apksigner','sign','--ks',key,'--ks-pass','pass:android','--key-pass','pass:android','--out',output,build/'aligned.apk')
run(bt/'apksigner','verify','--verbose',output)
run(bt/'zipalign','-c','-p','4',output)
print(output)
