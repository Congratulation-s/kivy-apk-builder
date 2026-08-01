[app]
# (str) Title of your application
title = M3U8 Cloud Player

# (str) Package name
package.name = m3u8cloudplayer

# (str) Package domain (needed for android packaging)
package.domain = org.example

# (str) Source code directory
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ttf

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# มีการเพิ่ม openssl, urllib3, certifi เพื่อแก้ปัญหา requests แครชบนแอนดรอยด์
requirements = python3,kivy,requests,openssl,urllib3,certifi

# (str) Supported orientations (valid options are: landscape, portrait, portrait-reverse, landscape-reverse)
orientation = portrait

# (int) Indicates if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# 🔒 ตั้งค่าระบบแอนดรอยด์และข้ามการดาวน์โหลด SDK ซ้ำซ้อนบน GitHub คลาวด์
android.api = 34
android.minapi = 26
android.ndk_api = 26
android.build_tools_version = 34.0.0
android.accept_sdk_license = True
android.skip_update = True

# (list) The Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a symbolic link
android.copy_libs = 1

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
