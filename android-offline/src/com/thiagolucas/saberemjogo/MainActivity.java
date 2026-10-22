package com.thiagolucas.saberemjogo;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.ActivityNotFoundException;
import android.content.Intent;
import android.content.DialogInterface;
import android.graphics.Color;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.widget.TextView;
import android.widget.Button;
import android.widget.LinearLayout;
import android.content.ClipData;
import android.content.ClipboardManager;
import android.view.View;
import android.view.WindowInsets;
import android.webkit.*;
import android.widget.FrameLayout;
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.util.HashMap;

public final class MainActivity extends Activity {

 public final class StudyBridge {
  @JavascriptInterface public void configureReminder(final String label,final String body,final int hour,final int minute){
   if(hour<0||hour>23||minute<0||minute>59||body==null||body.length()>500)return;
   runOnUiThread(new Runnable(){public void run(){
    StudyReminder.prefs(MainActivity.this).edit().putBoolean("enabled",true).putString("body",body).putInt("hour",hour).putInt("minute",minute).apply();
    if(Build.VERSION.SDK_INT>=33&&checkSelfPermission("android.permission.POST_NOTIFICATIONS")!=android.content.pm.PackageManager.PERMISSION_GRANTED)requestPermissions(new String[]{"android.permission.POST_NOTIFICATIONS"},710);
    else StudyReminder.schedule(MainActivity.this);
   }});
  }
  @JavascriptInterface public void cancelReminder(){StudyReminder.cancel(MainActivity.this);}
  @JavascriptInterface public void updateProgress(String body){if(body!=null&&body.length()<=500)StudyReminder.prefs(MainActivity.this).edit().putString("body",body).apply();}
 }
 @Override public void onRequestPermissionsResult(int code,String[] permissions,int[] results){super.onRequestPermissionsResult(code,permissions,results);if(code==710){if(results.length>0&&results[0]==android.content.pm.PackageManager.PERMISSION_GRANTED)StudyReminder.schedule(this);else StudyReminder.cancel(this);}}
 private WebView web;
 private FrameLayout frame;
 private final Handler handler=new Handler(Looper.getMainLooper());
 private boolean disposed=false, failed=false;
 private String diagnostic="";
 private final Runnable startupTimeout=new Runnable(){public void run(){showFailure("INICIO-15S", "O jogo não terminou de carregar. Tente novamente. Se persistir, atualize o Android System WebView pela Play Store.");}};
 private final Runnable checkReady=new Runnable(){public void run(){
  if(disposed || failed || web==null)return;
  web.evaluateJavascript("(function(){var a=document.getElementById('app');return a&&a.dataset.ready==='1';})()",new ValueCallback<String>(){public void onReceiveValue(String result){
   if(disposed || failed)return;
   if("true".equals(result))handler.removeCallbacks(startupTimeout);
   else handler.postDelayed(checkReady,300);
  }});
 }};
 private void showFailure(String code,String message){
  if(disposed || failed)return;
  failed=true; handler.removeCallbacksAndMessages(null);
  diagnostic="Saber em Jogo 0.7 | "+code+" | Android "+Build.VERSION.RELEASE+" | "+Build.MANUFACTURER+" "+Build.MODEL;
  android.util.Log.e("SaberEmJogo",diagnostic);
  if(frame==null)return;
  if(web!=null && !"RENDER".equals(code))web.stopLoading();
  frame.removeAllViews();
  LinearLayout box=new LinearLayout(this);box.setOrientation(LinearLayout.VERTICAL);box.setPadding(32,48,32,32);
  TextView title=new TextView(this);title.setText("Vamos colocar o jogo de volta");title.setTextColor(Color.WHITE);title.setTextSize(24);box.addView(title);
  TextView detail=new TextView(this);detail.setText(message+"\n\n"+diagnostic);detail.setTextColor(Color.LTGRAY);detail.setTextSize(16);box.addView(detail);
  Button retry=new Button(this);retry.setText("Tentar novamente");retry.setOnClickListener(new View.OnClickListener(){public void onClick(View v){recreate();}});box.addView(retry);
  Button copy=new Button(this);copy.setText("Copiar diagnóstico");copy.setOnClickListener(new View.OnClickListener(){public void onClick(View v){ClipboardManager c=(ClipboardManager)getSystemService(CLIPBOARD_SERVICE);if(c!=null)c.setPrimaryClip(ClipData.newPlainText("Diagnóstico",diagnostic));}});box.addView(copy);
  frame.addView(box,new FrameLayout.LayoutParams(-1,-1));
 }
 private static final String HOST = "appassets.androidplatform.net";
 @Override public void onCreate(Bundle saved) {
  super.onCreate(saved);
  frame = new FrameLayout(this);
  setContentView(frame);
  try {
  frame.setBackgroundColor(Color.rgb(16,20,38));
  if (Build.VERSION.SDK_INT >= 30) getWindow().setDecorFitsSystemWindows(false);
  frame.setOnApplyWindowInsetsListener(new View.OnApplyWindowInsetsListener(){ @Override public WindowInsets onApplyWindowInsets(View v,WindowInsets insets) {
   if(Build.VERSION.SDK_INT>=30) {
    android.graphics.Insets bars=insets.getInsets(WindowInsets.Type.systemBars() | WindowInsets.Type.displayCutout());
    v.setPadding(bars.left,bars.top,bars.right,bars.bottom);
   }
   return insets;
  }});
  web=new WebView(this);
  web.setBackgroundColor(Color.rgb(16,20,38));
  WebSettings settings=web.getSettings();
  settings.setJavaScriptEnabled(true);
  settings.setDomStorageEnabled(true);
  settings.setAllowFileAccess(false);
  settings.setAllowContentAccess(false);
  settings.setJavaScriptCanOpenWindowsAutomatically(false);
  settings.setSupportMultipleWindows(false);
  settings.setMixedContentMode(WebSettings.MIXED_CONTENT_NEVER_ALLOW);
  web.addJavascriptInterface(new StudyBridge(),"AndroidStudy");
  web.setWebViewClient(new WebViewClient(){
   @Override public void onReceivedError(WebView view,WebResourceRequest request,WebResourceError error){if(request.isForMainFrame())showFailure("WEB-"+error.getErrorCode(),"Não foi possível abrir a tela inicial do jogo.");}
   @Override public boolean onRenderProcessGone(WebView view,RenderProcessGoneDetail detail){frame.removeView(view);view.destroy();web=null;showFailure("RENDER", "O componente de exibição do Android foi encerrado. Tente novamente.");return true;}
   @Override public void onPageFinished(WebView view,String url){if(!failed)handler.post(checkReady);}
   @Override public WebResourceResponse shouldInterceptRequest(WebView view,WebResourceRequest request){
    Uri uri=request.getUrl();
    if(!"https".equals(uri.getScheme()) || !HOST.equals(uri.getHost())) return blocked();
    String path=uri.getPath();
    if(path==null || !path.startsWith("/assets/") || path.contains("..")) return blocked();
    String name=path.substring(8);
    String mime=name.endsWith(".html")?"text/html":name.endsWith(".js")?"application/javascript":name.endsWith(".json")?"application/json":name.endsWith(".svg")?"image/svg+xml":"application/octet-stream";
    try {
     WebResourceResponse response=new WebResourceResponse(mime,"UTF-8",getAssets().open(name));
     HashMap<String,String> headers=new HashMap<>();
     headers.put("Content-Security-Policy","default-src 'self' data:; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; connect-src 'self'; img-src 'self' data:; object-src 'none'; frame-src 'none'");
     response.setResponseHeaders(headers);
     return response;
    } catch(IOException e){return blocked();}
   }
   @Override public boolean shouldOverrideUrlLoading(WebView view,WebResourceRequest request){
    Uri uri=request.getUrl();
    if("https".equals(uri.getScheme()) && HOST.equals(uri.getHost())) return false;
    if("https".equals(uri.getScheme())) {
     try{startActivity(new Intent(Intent.ACTION_VIEW,uri));}catch(ActivityNotFoundException e){new AlertDialog.Builder(MainActivity.this).setMessage("Não há navegador disponível para abrir esta fonte.").setPositiveButton("OK",null).show();}
    }
    return true;
   }
  });
  web.setWebChromeClient(new WebChromeClient(){
   @Override public boolean onJsConfirm(WebView view,String url,String message,final JsResult result){
    new AlertDialog.Builder(MainActivity.this).setTitle("Saber em Jogo").setMessage(message).setPositiveButton("Sim",new DialogInterface.OnClickListener(){public void onClick(DialogInterface d,int w){result.confirm();}}).setNegativeButton("Cancelar",new DialogInterface.OnClickListener(){public void onClick(DialogInterface d,int w){result.cancel();}}).setOnCancelListener(new DialogInterface.OnCancelListener(){public void onCancel(DialogInterface d){result.cancel();}}).show();return true;
   }
  });
  frame.addView(web,new FrameLayout.LayoutParams(-1,-1));
  frame.requestApplyInsets();
  handler.postDelayed(startupTimeout,15000);
  web.loadUrl("https://"+HOST+"/assets/index.html");
  } catch(RuntimeException e){showFailure("NATIVE-"+e.getClass().getSimpleName(),"Não foi possível iniciar a exibição. Confira se o Android System WebView está atualizado na Play Store.");}
    catch(LinkageError e){showFailure("COMPAT-"+e.getClass().getSimpleName(),"O componente de exibição está incompatível. Atualize o Android System WebView na Play Store.");}
 }
 private WebResourceResponse blocked(){return new WebResourceResponse("text/plain","UTF-8",404,"Not Found",null,new ByteArrayInputStream(new byte[0]));}
 @Override public void onBackPressed(){if(failed||web==null){finish();return;}web.evaluateJavascript("(typeof handleAppBack==='function'?handleAppBack():true)",new ValueCallback<String>(){public void onReceiveValue(String result){if("true".equals(result))finish();}});}
 @Override protected void onPause(){super.onPause();if(web!=null&&!failed)web.onPause();}
 @Override protected void onResume(){super.onResume();if(web!=null&&!failed)web.onResume();}
 @Override protected void onDestroy(){disposed=true;handler.removeCallbacksAndMessages(null);if(web!=null){frame.removeView(web);web.destroy();web=null;}super.onDestroy();}
}
