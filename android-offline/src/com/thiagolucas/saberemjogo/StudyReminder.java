package com.thiagolucas.saberemjogo;
import android.app.*;
import android.content.*;
import android.os.Build;
import java.util.Calendar;

public final class StudyReminder extends BroadcastReceiver {
 static android.content.SharedPreferences prefs(Context c){return c.getSharedPreferences("study_reminder",Context.MODE_PRIVATE);}
 static void schedule(Context c){
  android.content.SharedPreferences p=prefs(c);if(!p.getBoolean("enabled",false))return;
  Calendar at=Calendar.getInstance();at.set(Calendar.HOUR_OF_DAY,p.getInt("hour",20));at.set(Calendar.MINUTE,p.getInt("minute",40));at.set(Calendar.SECOND,0);at.set(Calendar.MILLISECOND,0);if(at.getTimeInMillis()<=System.currentTimeMillis())at.add(Calendar.DAY_OF_YEAR,1);
  AlarmManager a=(AlarmManager)c.getSystemService(Context.ALARM_SERVICE);if(a!=null)a.setAndAllowWhileIdle(AlarmManager.RTC_WAKEUP,at.getTimeInMillis(),pending(c));
 }
 static PendingIntent pending(Context c){return PendingIntent.getBroadcast(c,710,new Intent(c,StudyReminder.class).setAction("com.thiagolucas.saberemjogo.REMIND"),PendingIntent.FLAG_UPDATE_CURRENT|PendingIntent.FLAG_IMMUTABLE);}
 static void cancel(Context c){prefs(c).edit().putBoolean("enabled",false).apply();AlarmManager a=(AlarmManager)c.getSystemService(Context.ALARM_SERVICE);if(a!=null)a.cancel(pending(c));NotificationManager n=(NotificationManager)c.getSystemService(Context.NOTIFICATION_SERVICE);if(n!=null)n.cancel(710);}
 @Override public void onReceive(Context context,Intent intent){
  if(!prefs(context).getBoolean("enabled",false))return;
  if(Intent.ACTION_BOOT_COMPLETED.equals(intent.getAction())){schedule(context);return;}
  NotificationManager n=(NotificationManager)context.getSystemService(Context.NOTIFICATION_SERVICE);
  if(n!=null && n.areNotificationsEnabled() && (Build.VERSION.SDK_INT<33||context.checkSelfPermission("android.permission.POST_NOTIFICATIONS")==android.content.pm.PackageManager.PERMISSION_GRANTED)){
   n.createNotificationChannel(new NotificationChannel("study_progress","Lembretes de estudo",NotificationManager.IMPORTANCE_DEFAULT));
   String text=prefs(context).getString("body","Seu próximo tema espera por você.");
   PendingIntent open=PendingIntent.getActivity(context,711,new Intent(context,MainActivity.class),PendingIntent.FLAG_UPDATE_CURRENT|PendingIntent.FLAG_IMMUTABLE);
   int icon=context.getResources().getIdentifier("ic_launcher","drawable",context.getPackageName());
   Notification notification=new Notification.Builder(context,"study_progress").setSmallIcon(icon).setContentTitle("Saber em Jogo · hora de estudar").setContentText(text).setStyle(new Notification.BigTextStyle().bigText(text)).setContentIntent(open).setAutoCancel(true).build();n.notify(710,notification);
  }
  schedule(context);
 }
}
