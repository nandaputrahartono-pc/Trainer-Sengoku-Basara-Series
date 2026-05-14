import pymem
import pymem.exception
import threading
import time

class ModTrainer:
    def __init__(self):
        self.pm = None
        self.is_connect = False

        self.address_money = 0x3300D6330

        self.address_matsunaga = {
            'characters': 0x3300D7FF5,
            'weapon': 0x3300D7FF3
        }
        self.matsunaga_status = False
        self.characters = 0
        self.weapon = 0

        self.address_element = 0x33B508F37
        self.freeze_element = False
        self.element_status = False
        self.element = 0
        self.list_element = {
            'Fire'    : 0x00,
            'Thunder' : 0x01,
            'Ice'     : 0x02,
            'Dark'    : 0x03,
            'Wind'    : 0x04,
            'Light'   : 0x05,
            'Physical': 0x07
        }

        self.address_weapon = 0x3300D7FFB
        self.weapon_status = False
        self.real_weapon = 0
        self.list_weapon = {
            "Weapon 1": 0x00,
            "Weapon 2": 0x01,
            "Weapon 3": 0x02,
            "Weapon 4": 0x03,
            "Weapon 5": 0x04,
            "Weapon 6": 0x05,
            "Weapon 7": 0x06,
            "Weapon 8": 0x07
        }

        self.address_costumes = 0x3300D7FF6
        self.costumes_status = False
        self.costumes = 0
        self.list_costumes = {
            "Costume 1": 0x00,
            "Costume 2": 0x01,
            "Costume 3": 0x02
        }

    def connect(self):
        try:
            self.pm = pymem.Pymem('rpcs3.exe')
            self.is_connect = True
            return True, 'RPCS3 Connected'
        
        except pymem.exception.ProcessNotFound:
            return False, 'RPCS3 Disconnected'
        
        except Exception as e:
            return False, f'error{e}'
    
    def disconnect(self):
        self.pm = None
        self.is_connect = False

    def matsunaga_playble(self):
        if not self.is_connect:
            return False, 'RPCS3 Belum Terhubung'
        
        try:
            if not self.matsunaga_status:
                self.characters = self.pm.read_uchar(self.address_matsunaga['characters'])
                self.weapon = self.pm.read_uchar(self.address_matsunaga['weapon'])

                self.pm.write_uchar(self.address_matsunaga['characters'], 0x1f)
                self.pm.write_uchar(self.address_matsunaga['weapon'], 0xf8)

                self.matsunaga_status = True
                return True, 'Matsunaga Aktif'
            
            else:
                self.pm.write_uchar(self.address_matsunaga['characters'], self.characters)
                self.pm.write_uchar(self.address_matsunaga['weapon'], self.weapon)
                
                self.matsunaga_status = False
                return True, 'Matsunaga Tidak Aktif'

        except Exception as e:
            return False, f'Error: {e}'
    
    def toggle_element(self):
        if not self.is_connect:
            return False, 'RPCS3 Belum Terhubung'
        
        try:
            if not self.element_status:
                self.element = self.pm.read_uchar(self.address_element)
                self.element_status = True
                return True, 'Element Aktif'
            
            else:
                self.stop_freeze_element()
                self.pm.write_uchar(self.address_element, self.element)
                self.element_status = False
                return True, 'Element tidak Aktif'
            
        except Exception as e:
            return False, f'error:{e}'
    
    def start_freeze_element(self, element_name):
        self.freeze_element = False
        time.sleep(0.15)

        self.freeze_element = True
        nilai = self.list_element[element_name]
        def loop():
            while self.freeze_element:
                try:
                    self.pm.write_uchar(self.address_element, nilai)
                except:
                    break
                threading.Event().wait(0.1)
        threading.Thread(target=loop, daemon=True).start()

    def stop_freeze_element(self):
        self.freeze_element = False
        time.sleep(0.15)
    
    def change_element(self, name_element):
        if not self.is_connect:
            return False, 'RPCS3 Belum Terhubung'
        
        try:
            value_element = self.list_element[name_element]
            self.pm.write_uchar(self.address_element, value_element)
            return True, f'Element {name_element} Berhasil Diterapkan!!'
        except Exception as e:
            return False, f'error:{e}'
        
    def toggle_weapon(self):
        if not self.is_connect:
            return False, 'Belum terhubung RPCS3'
        try:
            if not self.weapon_status:
                self.real_weapon = self.pm.read_uchar(self.address_weapon)
                self.weapon_status = True
                return True, 'Ganti Weapon diaktifkan'
            
            else:
                self.pm.write_uchar(self.address_weapon, self.real_weapon)
                self.weapon_status = False
                return True, 'Ganti Weapon dinonaktifkan'
        except Exception as e:
            return False, f'error:{e}'
    
    def change_weapon (self, name_weapon):
        if not self.is_connect:
            return False, 'Belum Terhubung RPCS3'
        try:
            nilai = self.list_weapon[name_weapon]
            self.pm.write_uchar(self.address_weapon, nilai)
            return True, f'{name_weapon} berhasil diterapkan'
        except Exception as e:
            return False, f'error{e}'
        
    def toggle_costumes(self):
        if not self.is_connect:
            return False, 'Belum Terhubung RPCS3'
        try:
            if not self.costumes_status:
                self.costumes = self.pm.read_uchar(self.address_costumes)
                self.costumes_status = True
                return True, 'Ganti  Kostum diaktifkan'
            else:
                self.pm.write_uchar(self.address_costumes, self.costumes)
                self.costumes_status = False
                return True, 'Ganti kostum dinonaktifkan'
            
        except Exception as e:
            return False, f'error:{e}'
    
    def change_costumes(self, name_costumes):
        if not self.is_connect:
            return False, 'Belum Terhubung RPCS3'
        try:
            nilai = self.list_costumes[name_costumes]
            self.pm.write_uchar(self.address_costumes, nilai)
            return True, f'{name_costumes} berhasil diterapkan'
        except Exception as e:
            return False, f'error:{e}'
        
    def cheat_money(self, total):
        if not self.is_connect:
            return False, 'Belum Terhubung RPCS3'
        
        try:
            money = total.to_bytes(4, byteorder='big')
            self.pm.write_bytes(self.address_money, money, 4)
            return True, f'Berhasil! Duit sekarang: {total:,}'
        
        except Exception as e:
            return False, f'Error: {e}'
