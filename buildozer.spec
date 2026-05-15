[app]
# (str) Title of your application
title = My Smart App

# (str) Package name
package.name = smartapp

# (str) Package domain (needed for android packaging)
package.domain = org.abdul

# (str) Source code where the main.py or index.html live
source.dir = .

# (list) Source files to include (let's include everything needed)
source.include_exts = py,png,jpg,kv,atlas,html,js,css

# (list) Application requirements
# Since it's a web-based app, we mainly need python3 and kivy
requirements = python3,kivy

# (str) Custom source folder for requirements
# (list) Permissions
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# (int) Android API to use
android.api = 31

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use setup.py from source.dir
# (str) Android entry point, default is to use main.py
# For HTML apps, we usually use index.html as the source
# but Buildozer expects a Python wrapper (like Kivy's WebView)
# to run the HTML. 

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1
