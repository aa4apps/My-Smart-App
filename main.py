import os
from kivy.app import App
from kivy.uix.widget import Widget

class MyWebApp(App):
    def build(self):
        # یہ کوڈ صرف اینڈرائیڈ پر چلے گا
        try:
            from android.runnable import run_on_ui_thread
            from jnius import autoclass
            
            WebView = autoclass('android.webkit.WebView')
            WebViewClient = autoclass('android.webkit.WebViewClient')
            Activity = autoclass('org.kivy.android.PythonActivity').mActivity

            @run_on_ui_thread
            def create_webview():
                webview = WebView(Activity)
                webview.getSettings().setJavaScriptEnabled(True)
                webview.getSettings().setDomStorageEnabled(True)
                webview.getSettings().setAllowFileAccess(True)
                webview.getSettings().setAllowContentAccess(True)
                webview.setWebViewClient(WebViewClient())
                Activity.setContentView(webview)
                
                # آپ کی انڈیکس فائل v27 کو لوڈ کرنے کا راستہ
                file_path = os.path.join(os.getcwd(), "index.html")
                webview.loadUrl("file://" + file_path)

            create_webview()
        except ImportError:
            print("Native WebView is only available on Android.")
        
        return Widget()

if __name__ == '__main__':
    MyWebApp().run()
