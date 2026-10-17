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
import android.view.View;
import android.view.WindowInsets;
import android.webkit.*;
import android.widget.FrameLayout;
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.util.HashMap;

public final class MainActivity extends Activity {
 private WebView web;
 private static final String HOST = "appassets.androidplatform.net";
 @Override public void onCreate(Bundle saved) {
  super.onCreate(saved);
  final FrameLayout frame = new FrameLayout(this);
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
  web.setWebViewClient(new WebViewClient(){
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
     headers.put("Content-Security-Policy","default-src 'self' data:; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; connect-src 'self'; img-src 'self' data:; object-src 'none'");
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
  setContentView(frame);
  frame.requestApplyInsets();
  web.loadUrl("https://"+HOST+"/assets/index.html");
 }
 private WebResourceResponse blocked(){return new WebResourceResponse("text/plain","UTF-8",404,"Not Found",null,new ByteArrayInputStream(new byte[0]));}
 @Override public void onBackPressed(){web.evaluateJavascript("(()=>{if(typeof round!=='undefined'&&round.length){if(confirm('Sair da partida?'))home();return false;}if(typeof mode!=='undefined'&&mode){home();return false;}return true;})()",new ValueCallback<String>(){public void onReceiveValue(String result){if("true".equals(result))finish();}});}
 @Override protected void onPause(){super.onPause();web.onPause();}
 @Override protected void onResume(){super.onResume();if(web!=null)web.onResume();}
 @Override protected void onDestroy(){if(web!=null){web.destroy();web=null;}super.onDestroy();}
}
