import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock

# 🔴 ใส่ URL จาก Firebase ของคุณ (ตรวจสอบว่ามี /playlist.json ต่อท้ายเสมอ)
FIREBASE_URL = "https://my-m3u8-play-default-rtdb.firebaseio.com/playlist.json"

# กำหนดระบบฟอนต์แอนดรอยด์ที่รองรับภาษาไทยมาตรฐาน (ไม่ต้องดาวน์โหลดไฟล์เพิ่ม)
# ดึงรายชื่อระบบฟอนต์ที่พบได้ทั่วไปในมือถือ Android เพื่อป้องกันอาการกล่องสี่เหลี่ยม ☒
THAI_FONT = "Roboto" 

class M3u8CloudPlayerApp(App):
    def build(self):
        self.title = "M3U8 Cloud Player"
        self.videos = {}
        
        # ตั้งค่ารูปแบบ Layout แนวกว้าง-สูงให้เข้ากับหน้าจอมือถือ
        main_layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # --- ส่วนที่ 1: หน้าต่างจำลองเครื่องเล่นวิดีโอ (Video Status Monitor) ---
        self.status_box = BoxLayout(orientation='vertical', size_hint_y=0.25, padding=10)
        self.video_status_label = Label(
            text="📺 ระบบคลาวด์ซิงค์: กรุณาเลือกช่องเพื่อจำลองสตรีมวิดีโอ",
            halign='center',
            valign='middle',
            font_size='15sp',
            font_name=THAI_FONT
        )
        self.video_status_label.bind(size=self.video_status_label.setter('text_size'))
        self.status_box.add_widget(self.video_status_label)
        main_layout.add_widget(self.status_box)
        
        # --- ส่วนที่ 2: ฟอร์มรับข้อมูล เพิ่มสถานีลง Firebase ---
        input_layout = BoxLayout(orientation='vertical', size_hint_y=0.35, spacing=5)
        
        input_layout.add_widget(Label(text="📝 ชื่อวิดีโอ / ชื่อช่อง:", size_hint_y=None, height=25, halign='left', font_name=THAI_FONT))
        self.name_input = TextInput(multiline=False, size_hint_y=None, height=45, hint_text="ระบุชื่อภาษาไทยหรืออังกฤษ", font_name=THAI_FONT)
        input_layout.add_widget(self.name_input)
        
        input_layout.add_widget(Label(text="🔗 URL ลิงก์สตรีม .m3u8:", size_hint_y=None, height=25, halign='left', font_name=THAI_FONT))
        self.url_input = TextInput(multiline=False, size_hint_y=None, height=45, hint_text="https://domain.com")
        input_layout.add_widget(self.url_input)
        
        # ปุ่มส่งคำสั่งขึ้นฐานข้อมูลออนไลน์
        btn_add = Button(text="➕ ส่งข้อมูลไปที่ Firebase Cloud", size_hint_y=None, height=50, background_color=(0.1, 0.6, 0.3, 1), font_name=THAI_FONT)
        btn_add.bind(on_press=self.add_video_to_cloud)
        input_layout.add_widget(btn_add)
        
        main_layout.add_widget(input_layout)
        
        # --- ส่วนที่ 3: พื้นที่เรียกคืนและอัปเดตช่องรายการแบบเรียลไทม์ ---
        list_section = BoxLayout(orientation='vertical', size_hint_y=0.4, spacing=5)
        list_section.add_widget(Label(text="📋 รายการช่องของคุณทั้งหมด:", size_hint_y=None, height=25, halign='left', font_name=THAI_FONT))
        
        self.scroll_view = ScrollView()
        self.list_layout = GridLayout(cols=1, spacing=8, size_hint_y=None)
        self.list_layout.bind(minimum_height=self.list_layout.setter('height'))
        
        self.scroll_view.add_widget(self.list_layout)
        list_section.add_widget(self.scroll_view)
        
        main_layout.add_widget(list_section)
        
        # เรียกการดาวน์โหลดสตรีมครั้งแรก และวนลูปดึงข้อมูลจาก Cloud อัตโนมัติทุก 4 วินาที
        self.load_videos_from_cloud()
        Clock.schedule_interval(self.load_videos_from_cloud, 4.0)
        
        return main_layout

    # ฟังก์ชันดึงข้อมูลจากฐานข้อมูล Firebase Realtime
    def load_videos_from_cloud(self, *args):
        try:
            response = requests.get(FIREBASE_URL, timeout=4)
            if response.status_code == 200:
                data = response.json()
                self.videos = data if data else {}
                self.refresh_video_list()
        except Exception as e:
            print(f"เชื่อมต่อฐานข้อมูลล้มเหลว: {e}")

    # ฟังก์ชันเคลียร์วิดเจ็ตและจัดแสดงแถบช่องสตรีมใหม่
    def refresh_video_list(self):
        self.list_layout.clear_widgets()
        
        if not self.videos:
            self.list_layout.add_widget(Label(text="ไม่มีข้อมูลช่องในฐานข้อมูลขณะนี้", size_hint_y=None, height=40, font_name=THAI_FONT))
            return
            
        for video_id, video_data in self.videos.items():
            row = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=5)
            
            # ปุ่มกดยิงคำสั่งเล่นสตรีม
            btn_play = Button(text=f"▶ {video_data.get('name', 'Unnamed')}", size_hint_x=0.8, halign='left', valign='middle', font_name=THAI_FONT)
            btn_play.bind(size=btn_play.setter('text_size'))
            btn_play.bind(on_press=lambda instance, v_data=video_data: self.play_video_stream(v_data))
            
            # ปุ่มลบข้อมูลบน Cloud ถาวร
            btn_delete = Button(text="❌", size_hint_x=0.2, background_color=(0.8, 0.2, 0.2, 1))
            btn_delete.bind(on_press=lambda instance, v_id=video_id: self.delete_video_from_cloud(v_id))
            
            row.add_widget(btn_play)
            row.add_widget(btn_delete)
            self.list_layout.add_widget(row)

    # ส่งสัญญาณจำลองการเปิดวิดีโอ
    def play_video_stream(self, video_data):
        name = video_data.get('name', '')
        url = video_data.get('url', '')
        self.video_status_label.text = f"🎬 กำลังเล่น: {name}\n🔗 ลิงก์สตรีม: {url}"

    # ฟังชั่นอัปโหลดเพิ่มแถวข้อมูลใหม่แบบ POST
    def add_video_to_cloud(self, instance):
        name = self.name_input.text.strip()
        url = self.url_input.text.strip()
        
        if name and url:
            new_video = {"name": name, "url": url}
            try:
                response = requests.post(FIREBASE_URL, json=new_video, timeout=4)
                if response.status_code == 200:
                    self.name_input.text = ""
                    self.url_input.text = ""
                    self.load_videos_from_cloud()
            except Exception as e:
                self.video_status_label.text = f"❌ เกิดข้อผิดพลาดในการบันทึก: {e}"

    # ฟังก์ชันส่งคำสั่งนำคีย์ข้อมูลออกจากเซิร์ฟเวอร์แบบ DELETE
    def delete_video_from_cloud(self, video_id):
        delete_url = FIREBASE_URL.replace(".json", f"/{video_id}.json")
        try:
            response = requests.delete(delete_url, timeout=4)
            if response.status_code == 200:
                self.video_status_label.text = "🗑 ลบวิดีโอออกจากระบบคลาวด์เรียบร้อยแล้ว"
                self.load_videos_from_cloud()
        except Exception as e:
            self.video_status_label.text = f"❌ เกิดข้อผิดพลาดในการลบ: {e}"

if __name__ == '__main__':
    M3u8CloudPlayerApp().run()
