import customtkinter as ctk

# --- PENGATURAN TEMA ALA SENGOKU BASARA ---
ctk.set_appearance_mode("dark") # Wajib gelap!

class BasaraPremiumTrainer(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- JENDELA UTAMA ---
        self.title("Ankoku Trainer - HD Collection (BASARA THEME)")
        self.geometry("820x550")
        
        # Grid Utama
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # State Simulasi
        self.is_connected = False
        self.matsunaga_active = False

        self.setup_sidebar()
        self.setup_main_area()
        
        # Tampilkan Halaman Basara 2 Heroes dari awal
        self.show_frame("B2H")

    # ==========================================
    # 🖥️ 1. SETUP SIDEBAR (KIRI - HITAM PEKAT)
    # ==========================================
    def setup_sidebar(self):
        # Latar sidebar hitam pekat ala Ankoku
        self.sidebar_frame = ctk.CTkFrame(self, fg_color="#0D0D0D", width=220, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        
        # Logo Api Matsunaga
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="🔥", font=ctk.CTkFont(size=45), 
                                       text_color="#FF4500", fg_color="#1A1A1A", corner_radius=50, width=80, height=80)
        self.logo_label.pack(pady=(40, 20))

        self.trainer_name = ctk.CTkLabel(self.sidebar_frame, text="ANKOKU\nTRAINER", 
                                         font=ctk.CTkFont(size=18, weight="bold"), text_color="#D4AF37") # Warna Emas
        self.trainer_name.pack(pady=(0, 40))

        # --- TOMBOL NAVIGASI ---
        button_style = {"width": 180, "height": 38, "corner_radius": 8, "fg_color": "transparent", 
                        "text_color": "#A0A0A0", "hover_color": "#330000", "anchor": "w", "font": ctk.CTkFont(size=13, weight="bold")}

        self.btn_b1 = ctk.CTkButton(self.sidebar_frame, text="  🛡️   Basara 1", command=lambda: self.show_frame("B1"), **button_style)
        self.btn_b1.pack(pady=5)

        self.btn_b2 = ctk.CTkButton(self.sidebar_frame, text="  ⚔️   Basara 2", command=lambda: self.show_frame("B2"), **button_style)
        self.btn_b2.pack(pady=5)

        self.btn_b2h = ctk.CTkButton(self.sidebar_frame, text="  👹   Basara 2 Heroes", command=lambda: self.show_frame("B2H"), **button_style)
        self.btn_b2h.pack(pady=5)

        # Dorong elemen ke bawah
        ctk.CTkLabel(self.sidebar_frame, text="").pack(expand=True)
        
        # Tombol Connect RPCS3 (Merah Darah)
        self.btn_connect = ctk.CTkButton(self.sidebar_frame, text="🔌 Connect RPCS3", 
                                         fg_color="#8B0000", hover_color="#5C0000", corner_radius=15, width=180, height=45, 
                                         font=ctk.CTkFont(weight="bold", size=14), text_color="#FFD700")
        self.btn_connect.pack(pady=30)
        self.btn_connect.configure(command=self.simulasi_connect)

    # ==========================================
    # 🖥️ 2. SETUP AREA UTAMA (KANAN - ABU GELAP)
    # ==========================================
    def setup_main_area(self):
        # Background utama abu-abu gelap
        self.main_container = ctk.CTkFrame(self, fg_color="#1A1A1A", corner_radius=20)
        self.main_container.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.main_container.grid_rowconfigure(0, weight=1)
        self.main_container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        
        self.setup_halaman_kosong("B1", "Sengoku Basara 1", "Cheat NPC Basara 1 akan hadir di sini...")
        self.setup_halaman_kosong("B2", "Sengoku Basara 2", "Cheat NPC Basara 2 akan hadir di sini...")
        self.setup_basara2h_frame()

    def setup_halaman_kosong(self, id_frame, judul, subjudul):
        frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self.frames[id_frame] = frame
        frame.grid(row=0, column=0, sticky="nsew", padx=30, pady=30)
        ctk.CTkLabel(frame, text=judul, font=ctk.CTkFont(size=26, weight="bold"), text_color="#D4AF37").pack(anchor="w")
        ctk.CTkLabel(frame, text=subjudul, text_color="#A0A0A0", font=ctk.CTkFont(size=14)).pack(pady=20, anchor="w")

    # --- 🖥️ FRAME KHUSUS: BASARA 2 HEROES ---
    def setup_basara2h_frame(self):
        frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self.frames["B2H"] = frame
        frame.grid(row=0, column=0, sticky="nsew", padx=30, pady=30)

        self.judul = ctk.CTkLabel(frame, text="Sengoku Basara 2 Heroes", font=ctk.CTkFont(size=26, weight="bold"), text_color="#D4AF37")
        self.judul.pack(anchor="w", pady=(0, 20))

        # --- KARTU STATISTIK ---
        self.stat_frame = ctk.CTkFrame(frame, fg_color="transparent")
        self.stat_frame.pack(fill="x", pady=10)
        self.stat_frame.grid_columnconfigure((0, 1), weight=1)

        # Kartu Duit (Aksen Emas)
        self.card_duit = ctk.CTkFrame(self.stat_frame, fg_color="#262626", border_color="#B8860B", border_width=2, corner_radius=15, height=100)
        self.card_duit.grid(row=0, column=0, padx=(0, 10), sticky="ew")
        self.card_duit.pack_propagate(False)
        ctk.CTkLabel(self.card_duit, text="💰 Timbunan Ryo (Duit)", font=ctk.CTkFont(size=13, weight="bold"), text_color="#D4AF37").pack(pady=(15, 0), padx=20, anchor="w")
        self.val_card_duit = ctk.CTkLabel(self.card_duit, text="N/A", font=ctk.CTkFont(size=32, weight="bold"), text_color="white")
        self.val_card_duit.pack(pady=(5, 0), padx=20, anchor="w")

        # Kartu Status Matsunaga (Aksen Merah)
        self.card_status = ctk.CTkFrame(self.stat_frame, fg_color="#262626", border_color="#8B0000", border_width=2, corner_radius=15, height=100)
        self.card_status.grid(row=0, column=1, padx=(10, 0), sticky="ew")
        self.card_status.pack_propagate(False)
        ctk.CTkLabel(self.card_status, text="👹 Status Hisahide", font=ctk.CTkFont(size=13, weight="bold"), text_color="#D14B3A").pack(pady=(15, 0), padx=20, anchor="w")
        self.val_card_stat = ctk.CTkLabel(self.card_status, text="TERSEGEL", font=ctk.CTkFont(size=28, weight="bold"), text_color="#A0A0A0")
        self.val_card_stat.pack(pady=(5, 0), padx=20, anchor="w")

        # Garis Pemisah (Merah Gelap)
        ctk.CTkFrame(frame, fg_color="#330000", height=2, corner_radius=0).pack(fill="x", pady=25)

        # --- FORM INPUTS ---
        self.form_frame = ctk.CTkFrame(frame, fg_color="#262626", corner_radius=15, border_color="#330000", border_width=2)
        self.form_frame.pack(fill="x", pady=10)

        # Duit Input Area
        self.row_duit = ctk.CTkFrame(self.form_frame, fg_color="transparent")
        self.row_duit.pack(fill="x", padx=30, pady=(25, 10))
        ctk.CTkLabel(self.row_duit, text="Jumlah Ryo yang Diinginkan:", font=ctk.CTkFont(size=13, weight="bold"), text_color="#D4AF37").pack(anchor="w", pady=(0, 5))
        
        self.entry_frame = ctk.CTkFrame(self.row_duit, fg_color="#0D0D0D", corner_radius=10, height=45, border_color="#B8860B", border_width=1)
        self.entry_frame.pack(fill="x")
        self.entry_frame.pack_propagate(False)
        
        self.entry_duit = ctk.CTkEntry(self.entry_frame, fg_color="transparent", border_width=0, placeholder_text="Maks: 99999999", text_color="white", font=ctk.CTkFont(size=14))
        self.entry_duit.pack(side="left", padx=10, fill="both", expand=True)
        self.entry_duit.insert(0, "99999999")
        
        self.btn_duit = ctk.CTkButton(self.entry_frame, text="Suntik Dana", fg_color="#B8860B", hover_color="#8B6508", text_color="black", corner_radius=8, width=120, font=ctk.CTkFont(weight="bold"))
        self.btn_duit.pack(side="right", padx=5, pady=5)
        self.btn_duit.configure(command=self.simulasi_suntik_duit)

        # Matsunaga Toggle
        self.row_matsu = ctk.CTkFrame(self.form_frame, fg_color="transparent")
        self.row_matsu.pack(fill="x", padx=30, pady=(10, 25))
        ctk.CTkLabel(self.row_matsu, text="Segel Vile Incarnate:", font=ctk.CTkFont(size=13, weight="bold"), text_color="#D14B3A").pack(anchor="w", pady=(0, 5))
        
        self.btn_matsu = ctk.CTkButton(self.row_matsu, text="LEPAS SEGEL MATSUNAGA", 
                                      fg_color="#4A0E17", hover_color="#8B0000", text_color="#FFD700", border_color="#8B0000", border_width=2,
                                      height=45, corner_radius=10, font=ctk.CTkFont(size=14, weight="bold"))
        self.btn_matsu.pack(fill="x")
        self.btn_matsu.configure(command=self.simulasi_toggle_matsunaga)


    # ==========================================
    # 🧠 FUNGSI-FUNGSI LOGIKA UI (SIMULASI)
    # ==========================================
    def show_frame(self, frame_name):
        for f in self.frames.values():
            f.grid_remove()
        
        self.frames[frame_name].grid()
        
        # Reset warna tombol sidebar
        self.btn_b1.configure(fg_color="transparent", text_color="#A0A0A0")
        self.btn_b2.configure(fg_color="transparent", text_color="#A0A0A0")
        self.btn_b2h.configure(fg_color="transparent", text_color="#A0A0A0")

        # Highlight menu aktif (Merah Gelap)
        active_color = "#330000"
        active_text = "#FFD700" # Emas
        if frame_name == "B1": self.btn_b1.configure(fg_color=active_color, text_color=active_text)
        elif frame_name == "B2": self.btn_b2.configure(fg_color=active_color, text_color=active_text)
        elif frame_name == "B2H": self.btn_b2h.configure(fg_color=active_color, text_color=active_text)

    def simulasi_connect(self):
        self.is_connected = not self.is_connected
        if self.is_connected:
            self.btn_connect.configure(text="✅ EMULATOR TERHUBUNG", fg_color="#B8860B", hover_color="#8B6508", text_color="black")
            self.val_card_duit.configure(text="99.999.999")
        else:
            self.btn_connect.configure(text="🔌 Connect RPCS3", fg_color="#8B0000", hover_color="#5C0000", text_color="#FFD700")
            self.val_card_duit.configure(text="N/A")

    def simulasi_suntik_duit(self):
        if not self.is_connected:
            print("Pura-puranya ada error: Connect RPCS3 dulu bos!")
            return
        try:
            duit = int(self.entry_duit.get())
            self.val_card_duit.configure(text=f"{duit:,}".replace(",", "."))
            print(f"Sukses update UI Duit jadi: {duit}")
        except ValueError:
            print("Masukin angka aja cuy!")

    def simulasi_toggle_matsunaga(self):
        if not self.is_connected:
            print("Pura-puranya ada error: Connect RPCS3 dulu bos!")
            return

        self.matsunaga_active = not self.matsunaga_active
        if self.matsunaga_active:
            # Mode GILA Aktif (Merah Menyala)
            self.val_card_stat.configure(text="🔥 MENGAMUK", text_color="#FF4500")
            self.card_status.configure(border_color="#FF4500")
            self.btn_matsu.configure(text="KEMBALIKAN SEGEL (OFF)", fg_color="#8B0000", hover_color="#5C0000", text_color="white", border_width=0)
        else:
            # Mode Normal (Tersegel)
            self.val_card_stat.configure(text="TERSEGEL", text_color="#A0A0A0")
            self.card_status.configure(border_color="#8B0000")
            self.btn_matsu.configure(text="LEPAS SEGEL MATSUNAGA", fg_color="#4A0E17", hover_color="#8B0000", text_color="#FFD700", border_width=2)

if __name__ == "__main__":
    app = BasaraPremiumTrainer()
    app.mainloop()