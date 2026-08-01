[app]
title = M3U8 Cloud Player
package.name = m3u8cloudplayer
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf
version = 0.1

# ไลบรารีเน็ตเวิร์กที่ถูกต้องสำหรับระบบ Python บนแอนดรอยด์
requirements = python3,kivy,requests,openssl,urllib3,certifi

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# 🔒 ปล่อยให้ Buildozer สรรหาเวอร์ชันที่ลงตัวที่สุดอัตโนมัติ ห้ามข้ามการอัปเดตเด็ดขาด
android.api = 33
android.minapi = 21
android.ndk_api = 21
android.accept_sdk_license = True
android.skip_update = False

android.archs = arm64-v8a, armeabi-v7a
android.copy_libs = 1

[buildozer]
log_level = 2
warn_on_root = 1
