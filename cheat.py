import pymem

def main():
    print("TRAINER SENGOKU BASARA 2 HEROES")

    try:
        pm = pymem.Pymem('rpcs3.exe')
        print('Berhasil Terhubung ke RPCS3')

        address_money = 0x3300D6330
        address_matsunaga = {
            "characters":0x3300D7FF5,
            "weapon":0x3300D7FF3
        }

        matsunaga_status = False
        characters = 0
        weapon = 0

        address_element = 0x33B508F37

        while True:
            print("1.Matsunaga Hisahide")
            print("2.Cheat duit coyy")
            print("3.Element")
            print("4.Keluar")

            select = input('Pilih Program (1/2/3/4): ')

            if select == '1':
                    while True:
                        status_matsunaga = "[ON]" if matsunaga_status else "[OFF]"

                        print(f"1.Matsunaga Hisahide {status_matsunaga}")
                        print("2.Keluar")

                        select_matsunaga = input("Apakah kamu mau memainkan matsunaga?(1/2): ")

                        if select_matsunaga == "1":
                            if not matsunaga_status:
                                characters = pm.read_uchar(address_matsunaga["characters"])
                                weapon = pm.read_uchar(address_matsunaga["weapon"])

                                pm.write_uchar(address_matsunaga["characters"], 0x1f)
                                pm.write_uchar(address_matsunaga["weapon"], 0xF8)

                                matsunaga_status = True
                                print("Matsunaga Hisahide Berhasil Dimainkan")
                        
                            else:
                                pm.write_uchar(address_matsunaga["characters"], characters)
                                pm.write_uchar(address_matsunaga["weapon"], weapon)

                                matsunaga_status = False
                                print("Matsunaga OFF")

                        elif select_matsunaga == '2':
                            print("Thanks Cuyy")
                            break
                        else:
                            print("gak ada dipilihan")

            elif select == '2':
                input_user = input("Masukkan jumlah duit: ")

                try:
                    money = int(input_user)

                    money_byte = money.to_bytes(4, byteorder='big')

                    pm.write_bytes(address_money, money_byte, 4)

                    print(f'Sukses!!, jumlah yang anda masukkan {money}')
            
                except ValueError:
                    print("Error!! Masukkan Angka mas")
            
            elif select == '4':
                print("Terimakasih cuyy!!")
                break
            else:
                print(f"Pilihan {select} tidak valid, cuman ada 1, 2, 3")


    except pymem.exception.ProcessNotFound:
        print("RPCS3 Belum Terhubung")
    except Exception as e:
        print(f"[-] Ada error nih: {e}")

if __name__ == "__main__":
    main()
