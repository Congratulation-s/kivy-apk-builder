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

# (list) ไลบรารี Python ที่ถูกต้อง (ลบคำว่า android ออกไปแล้ว และล็อกเวอร์ชันเพื่อความเสถียร)
requirements = python3==3.11.1,kivy==2.3.0,requests,openssl,urllib3,certifi

# (str) Supported orientations
orientation = portrait

# (int) Indicates if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# 🔒 ปรับระดับความปลอดภัยและรหัส API แอนดรอยด์ให้เข้าคู่กับชุดเครื่องมือ r28c ยุคใหม่
android.api = 34
android.minapi = 26
android.ndk_api = 26
android.build_tools_version = 34.0.0
android.accept_sdk_license = True
android.skip_update = False

# (list) The Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Copy library instead of making a symbolic link
android.copy_libs = 1

[buildozer]
# (int) Log level
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
