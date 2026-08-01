[app]
# (str) ชื่อของแอปพลิเคชันคุณ
title = M3U8 Cloud Player

# (str) ชื่อแพ็กเกจห้ามซ้ำ (ตัวพิมพ์เล็กภาษาอังกฤษเท่านั้น)
package.name = m3u8cloudplayer

# (str) โดเมนของแอปพลิเคชัน
package.domain = org.example

# (str) โฟลเดอร์ตำแหน่งโค้ดหลัก
source.dir = .

# (list) นามสกุลไฟล์ที่ต้องการรวมเข้าไปในแอป
source.include_exts = py,png,jpg,kv,atlas,ttf

# (str) เวอร์ชันของแอปพลิเคชัน
version = 0.1

# (list) ไลบรารี Python ที่แอปต้องใช้ (เพิ่มโมดูลความปลอดภัย SSL ป้องกันแอปแครช)
requirements = python3,kivy,requests,openssl,urllib3,certifi

# (str) บังคับทิศทางหน้าจอแนวตั้ง
orientation = portrait

# (int) เปิด/ปิด โหมดเต็มหน้าจอ (0 = ปิด, 1 = เปิด)
fullscreen = 0

# (list) ขอสิทธิ์การใช้งานอินเทอร์เน็ตของระบบแอนดรอยด์
android.permissions = INTERNET

# 🔒 ล็อกเวอร์ชันแอนดรอยด์สากล และสั่งกดยอมรับสัญญาอนุญาตผ่านระบบคลาวด์อัตโนมัติ
android.api = 33
android.minapi = 21
android.ndk_api = 21
android.accept_sdk_license = True
android.skip_update = False

# (list) สถาปัตยกรรมชิปมือถือที่ต้องการรองรับ (ครอบคลุมมือถือแอนดรอยด์ 99% ในปัจจุบัน)
android.archs = arm64-v8a, armeabi-v7a

# (bool) คัดลอกไลบรารีแทนการสร้างลิงก์จำลองเพื่อความเสถียรบน GitHub
android.copy_libs = 1

[buildozer]
# (int) ระดับการบันทึกประวัติการบิลด์ (2 = บันทึกข้อมูลละเอียดลงไฟล์สเปก)
log_level = 2

# (int) แจ้งเตือนหากใช้งานสิทธิ์ผู้ดูแลระบบสูงสุด (1 = เปิด)
warn_on_root = 1
