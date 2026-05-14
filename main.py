import customtkinter 
from PIL import Image
from trainer import ModTrainer

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.trainer = ModTrainer()

        self.title('Sengoku Basara Trainer')
        self.geometry('960x540')
        self.minsize(600, 400)
        self.resizable(True, True) 

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.sidebar()
        self.main_content()

    def sidebar(self):
        self.sidebar_frame = customtkinter.CTkFrame(
            self,
            fg_color='#0D0D0D',
            width=180,
            corner_radius=0
        )
        self.sidebar_frame.grid(row=0, column=0, sticky='nsew')

        self.logo = customtkinter.CTkImage(
            light_image=Image.open('logo.png'),
            dark_image=Image.open('logo.png'),
            size=(75, 75)
        )
        self.logo_ctk = customtkinter.CTkLabel(
            self.sidebar_frame,
            text='',
            image=self.logo
        )
        self.logo_ctk.pack(pady=(30, 10))

        self.title_label = customtkinter.CTkLabel(
            self.sidebar_frame,
            text='Sengoku Basara\nHD Collection Trainer',
            font=customtkinter.CTkFont(size=16, weight='bold')
        )
        self.title_label.pack(pady=(0, 15))

        self.line = customtkinter.CTkFrame(
            self.sidebar_frame,
            height=2,
            fg_color='#333333'
        )
        self.line.pack(fill='x', padx=20, pady=(0, 20))

        button_style = {
            'width':180,
            'height':32,
            'corner_radius':8,
            'fg_color':'transparent',
            'hover_color':'#A0A0A0',
            'anchor':'w',
            'font':customtkinter.CTkFont(size=12, weight='bold')
        }

        self.btn_basara1 = customtkinter.CTkButton(
            self.sidebar_frame,
            text='Sengoku Basara 1',
            command=lambda:self.show_pages('b1'),
            **button_style
        )
        self.btn_basara1.pack(pady=5)

        self.btn_basara2 = customtkinter.CTkButton(
            self.sidebar_frame,
            text='Sengoku Basara 2',
            command=lambda:self.show_pages('b2'),
            **button_style
        )
        self.btn_basara2.pack(pady=5)

        self.btn_basara2h = customtkinter.CTkButton(
            self.sidebar_frame,
            text='Sengoku Basara 2 heroes',
            command=lambda:self.show_pages('b2h'),
            **button_style
        )
        self.btn_basara2h.pack(pady=5)    

        self.btn_nav = {
            'b1':self.btn_basara1,
            'b2':self.btn_basara2,
            'b2h':self.btn_basara2h
        }
        
        self.btn_connect = customtkinter.CTkButton(
            self.sidebar_frame,
            text='RPCS3 Disconnected',
            fg_color='#8B0000',
            hover_color='#5C0000',
            corner_radius=15,
            width=180,
            font=customtkinter.CTkFont(weight='bold', size=14),
            command=self.action_connect
        )
        self.btn_connect.pack(pady=20, side='bottom')

        self.message_status = customtkinter.CTkLabel(
            self.sidebar_frame,
            text='',
            font=customtkinter.CTkFont(size=11),
            text_color='#FF4500'
        )
        self.message_status.pack(side='bottom')

    def action_connect(self):
        if not self.trainer.is_connect:
            sukses, pesan = self.trainer.connect()
            if sukses:
                self.btn_connect.configure(
                    text='Connected RPCS3',
                    fg_color='#1a5c1a',
                    hover_color='#144d14',
                    text_color='white'
                )
                self.message_status.configure(text='')

            else:
                self.btn_connect.configure(
                    text=f'{pesan}',
                    fg_color='#8B0000',
                    hover_color='#5C0000'
                )
                self.message_status.configure(text='RPCS3 Belum dibuka')
        
        else:
            self.trainer.disconnect()
            self.btn_connect.configure(
                self.sidebar_frame,
                text='Disconnected RPCS3',
                fg_color='#8B0000',
                hover_color='#5C0000',
                text_color='white'
            )
            self.message_status.configure(text='')

    def main_content(self):
        self.main_container = customtkinter.CTkFrame(self, fg_color='#1A1A1A', corner_radius=12)
        self.main_container.grid(row=0, column=1, sticky='nsew', padx=15, pady=15)
        self.main_container.grid_rowconfigure(0, weight=1)
        self.main_container.grid_columnconfigure(0, weight=1)

        self.page = {}

        self.content_empty('b1', 'Sengoku Basara 1', 'Sengoku Basara 1 Akan Segara Hadir...')
        self.content_empty('b2', 'Sengoku Basara 2', 'Sengoku Basara 2 Akan Segara Hadir...')
        self.content_b2h()

    def content_empty(self, lock, title_page, sub_title_page,):
        frame = customtkinter.CTkFrame(self.main_container, fg_color='transparent')
        self.page[lock] = frame
        frame.grid(row=0, column=0, sticky='nsew', padx=30, pady=30)

        title_pages = customtkinter.CTkLabel(
            frame,
            text=title_page,
            font=customtkinter.CTkFont(size=26, weight='bold')

        )
        title_pages.pack(anchor='w')

        sub_title_pages = customtkinter.CTkLabel(
            frame,
            text=sub_title_page,
            font=customtkinter.CTkFont(size=14),
            text_color='#A0A0A0'
        )
        sub_title_pages.pack(pady=20, anchor='w')
    
    def content_b2h(self):
        frame = customtkinter.CTkScrollableFrame(
            self.main_container,
            fg_color='transparent',
            scrollbar_button_color='#1A1A1A', 
            scrollbar_button_hover_color='#555555'
        )
        self.page['b2h'] = frame
        frame.grid(row=0, column=0, sticky='nsew', padx=30, pady=30)

        customtkinter.CTkLabel(
            frame,
            text='Sengoku Basara 2 Heroes',
            font=customtkinter.CTkFont(size=26, weight='bold'),
        ).pack(anchor='w')

        customtkinter.CTkLabel(
            frame,
            text='Pilih Cheat yang kamu inginkan',
            font=customtkinter.CTkFont(size=13),
            text_color='#A0A0A0'
        ).pack(anchor='w', pady=(5, 20))

        customtkinter.CTkFrame(
            frame, height=2, fg_color='#333333'
        ).pack(fill='x', pady=(0, 20))

        # Section Matsunaga Hisahide
        self.section_matsunaga = customtkinter.CTkLabel(
            frame,
            text='Playble Matsunaga Hisahide',
            font=customtkinter.CTkFont(size=13, weight='bold')
        )
        self.section_matsunaga.pack(anchor='w')

        self.description_matsunaga = customtkinter.CTkLabel(
            frame,
            text='Aktifkan untuk memainkan Matsunaga Hisahide',
            font=customtkinter.CTkFont(size=12),
            text_color='#A0A0A0'
        )
        self.description_matsunaga.pack(anchor='w', pady=(3, 10))

        self.btn_matsunaga = customtkinter.CTkButton(
            frame,
            text='OFF - Klik untuk Aktifkan',
            width=200,
            height=38,
            fg_color='#8B0000',
            hover_color='#5C0000',
            font=customtkinter.CTkFont(weight='bold'),
            command=self.action_matsunaga

        )
        self.btn_matsunaga.pack(anchor='w', pady=(0, 5))

        self.label_matsunaga = customtkinter.CTkLabel(
            frame,
            text='',
            font=customtkinter.CTkFont(size=12),
            text_color = '#A0A0A0'
        )
        self.label_matsunaga.pack(anchor='w', pady=(0, 20))

        # Section Element
        self.checkbox_element = customtkinter.CTkCheckBox(
            frame,
            text='Change Element',
            fg_color='#1a5c1a',
            hover_color='#144d14',
            checkmark_color='white',
            font=customtkinter.CTkFont(size=13, weight='bold'),   
            command=self.action_element     
        )
        self.checkbox_element.pack(anchor='w', pady=(0, 20))

        self.dropdown_element = customtkinter.CTkOptionMenu(
            frame,
            values=list(self.trainer.list_element.keys()),
            fg_color='#262626',
            button_color='#8B0000',
            button_hover_color='#5C0000',
            width=150,
            command=self.action_change_element
            
        )

        self.label_element = customtkinter.CTkLabel(
            frame,
            text='',
            font=customtkinter.CTkFont(size=12),
            text_color='#A0A0A0'
        )
        self.label_element.pack(anchor='w', pady=(5, 0))

        # Section Ganti Senjata
        self.checkbox_weapon = customtkinter.CTkCheckBox(
            frame,
            text='Ganti Senjata Karakter',
            fg_color='#1a5c1a',
            hover_color='#144d14',
            checkmark_color='white',
            font=customtkinter.CTkFont(size=13, weight='bold'),  
            command=self.action_toggle_weapon
        )
        self.checkbox_weapon.pack(anchor='w', pady=(0, 20))

        self.dropdown_weapon = customtkinter.CTkOptionMenu(
            frame,
            values=list(self.trainer.list_weapon.keys()),
            fg_color='#262626',
            button_color='#8B0000',
            button_hover_color='#5C0000',
            width=150,
            command=self.action_change_weapon
        )

        self.label_weapon = customtkinter.CTkLabel(
            frame,
            text='',
            font=customtkinter.CTkFont(size=12),
            text_color='#A0A0A0'
        )
        self.label_weapon.pack(anchor='w', pady=(5, 0))
            
        # Section Change Costumes
        self.checkbox_costumes = customtkinter.CTkCheckBox(
            frame,
            text='Ganti Kostum Karakter',
            fg_color='#1a5c1a',
            hover_color='#144d14',
            checkmark_color='white',
            font=customtkinter.CTkFont(size=13, weight='bold'),
            command=self.action_toggle_costumes
        )
        self.checkbox_costumes.pack(anchor='w', pady=(0, 20))

        self.dropdown_costumes = customtkinter.CTkOptionMenu(
            frame,
            values=list(self.trainer.list_costumes.keys()),
            fg_color='#262626',
            button_color='#8B0000',
            button_hover_color='#5C0000',
            width=150,
            command=self.action_change_costumes
        )

        self.label_costumes = customtkinter.CTkLabel(
            frame,
            text='',
            font=customtkinter.CTkFont(size=12),
            text_color='#A0A0A0'
        )
        self.label_costumes.pack(anchor='w', pady=(5, 0))

        # Section Cheat Money
        self.section_money = customtkinter.CTkLabel(
            frame,
            text='Cheat Jumlah Duit',
            font=customtkinter.CTkFont(size=13, weight='bold')
        )
        self.section_money.pack(anchor='w')
        
        frame_input_money = customtkinter.CTkFrame(frame, fg_color='transparent')
        frame_input_money.pack(fill='x', pady=(5, 0))

        self.entry_money = customtkinter.CTkEntry(
            frame_input_money,
            placeholder_text='Masukkan Jumlah Duit...',
            width=250,
            height=38,
            font=customtkinter.CTkFont(size=13)
        )
        self.entry_money.pack(side='left', padx=(0, 10))
        self.entry_money.bind('<Return>', lambda event:self.action_money())

        self.btn_money = customtkinter.CTkButton(
            frame_input_money,
            text='Konfirmasi',
            width=100,
            height=38,
            fg_color='#1a5c1a',
            hover_color='#144d14',
            font=customtkinter.CTkFont(weight='bold'),
            command=self.action_money
        )   
        self.btn_money.pack(side='left')
        

        self.label_hasil_duit = customtkinter.CTkLabel(
            frame,
            text='',
            font=customtkinter.CTkFont(size=12),
            text_color='#A0A0A0'
        )
        self.label_hasil_duit.pack(anchor='w', pady=(8, 0))
        
    def action_matsunaga(self): 
        sukses, pesan = self.trainer.matsunaga_playble()
        if sukses:
            if self.trainer.matsunaga_status:
                self.btn_matsunaga.configure(
                    text='ON - Matsunaga Playble',
                    fg_color='#1a5c1a',
                    hover_color='#144d14'
                )
                self.label_matsunaga.configure(text=f'Berhasil {pesan}', text_color='#1a5c1a')
            else:
                self.btn_matsunaga.configure(
                    text='OFF - Klik untuk Aktifkan',
                    fg_color='#8B0000',
                    hover_color='#5C0000'
                )
                self.label_matsunaga.configure(text=f'Berhasil {pesan}', text_color='#FF4500')
            
        else:
            self.label_matsunaga.configure(
                text=f'{pesan}',
                text_color='#FF4500'
            )
    
    def action_element(self):
        if not self.trainer.is_connect:
            self.checkbox_element.deselect()
            self.label_element.configure(
                text='Hubungkan RPCS3 Terlebih Dahulu',
                text_color='#FF4500'
            )
            return
        
        sukses, pesan = self.trainer.toggle_element()
        if sukses:
            if self.trainer.element_status:
                self.dropdown_element.set('Fire')
                self.dropdown_element.pack(anchor='w', before=self.label_element)
                self.trainer.start_freeze_element('Fire')
                self.label_element.configure(text=f'Fire di-Freeze!', text_color='#1a5c1a')

            else:
                self.dropdown_element.pack_forget()
                self.label_element.configure(text='', text_color='#A0A0A0')

        else:
            self.checkbox_element.deselect()
            self.label_element.configure(text=f'{pesan}', text_color='#FF4500')
    
    def action_change_element(self, select):
        if not self.trainer.is_connect:
            self.label_element.configure(
                text='Hubungkan RPCS3 Terlebih Dahulu',
                text_color='#FF4500'
            )
            return
    
        self.trainer.start_freeze_element(select)
        self.label_element.configure(
            text=f'🔒 {select} di-Freeze!',
            text_color='#1a5c1a'
        )
    
    def action_toggle_weapon(self):
        if not self.trainer.is_connect:
            self.checkbox_weapon.deselect()
            self.label_weapon.configure(
                text='Hubungkan RPCS3 Terlebih Dahulu',
                text_color='#FF4500'
            )
            return

        sukses, pesan = self.trainer.toggle_weapon()
        if sukses:
            if self.trainer.weapon_status:
                self.dropdown_weapon.pack(anchor='w', pady=(5, 0), before=self.label_weapon)
                self.label_weapon.configure(text=f'{pesan}', text_color='#1a5c1a')
            else:
                self.dropdown_weapon.pack_forget()
                self.label_weapon.configure(text=f'{pesan}', text_color='#A0A0A0')
        else:
            self.checkbox_weapon.deselect()
            self.label_weapon.configure(text=f'{pesan}', text_color='#FF4500')
    
    def action_change_weapon(self, select):
        sukses, pesan = self.trainer.change_weapon(select)
        if sukses:
            self.label_weapon.configure(text=f'{pesan}', text_color='#1a5c1a')
        else:
            self.label_weapon.configure(text=f'{pesan}', text_color='#FF4500')

    def action_toggle_costumes(self):
        if not self.trainer.is_connect:
            self.checkbox_costumes.deselect()
            self.label_costumes.configure(
                text='Hubungkan RPCS3 Terlebih dahulu',
                text_color='#FF4500'
            )
            return
        
        sukses, pesan = self.trainer.toggle_costumes()
        if sukses:
            if self.trainer.costumes_status:
                self.dropdown_costumes.pack(anchor='w', pady=(5, 0), before=self.label_costumes)
                self.label_costumes.configure(text=f'{pesan}', text_color='#1a5c1a')
            else:
                self.dropdown_costumes.pack_forget()
                self.label_costumes.configure(text=f'{pesan}', text_color='#A0A0A0')
        else:
            self.checkbox_costumes.deselect()
            self.label_costumes.configure(text=f'{pesan}', text_color='#FF4500')
    
    def action_change_costumes(self, select):
        sukses, pesan = self.trainer.change_costumes(select)
        if sukses:
            self.label_costumes.configure(text=f'{pesan}', text_color='#1a5c1a')
        else:
            self.label_costumes.configure(text=f'{pesan}', text_color='#FF4500')
                    
    def action_money(self):
        if not self.trainer.is_connect:
            self.label_hasil_duit.configure(
                text='RPCS3 Belum Terhubung',
                text_color='#FF4500'
            )
            return
        
        try:
            total = int(self.entry_money.get())
            sukses, pesan = self.trainer.cheat_money(total)
            if sukses:
                self.label_hasil_duit.configure(
                    text=f'{pesan}',
                    text_color='#1a5c1a'
                )
            else:
                self.label_hasil_duit.configure(
                    text=f'Gagal {pesan}',
                    text_color='#FF4500'
                )
        except ValueError:
            self.label_hasil_duit.configure(
                text=f'Masukkan Angka yang Valid!!',
                text_color='#FF4500'
            )

    
    def show_pages(self, lock):
        for pages in self.page.values():
            pages.grid_remove()
        
        self.page[lock].grid()

        for button in self.btn_nav.values():
            button.configure(fg_color='transparent', text_color='white') 
        
        self.btn_nav[lock].configure(fg_color = 'white', text_color='black') 


if __name__ == "__main__":
    app = App()
    app.mainloop()