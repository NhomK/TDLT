﻿def chucnang():
    print('_'*50)
    entry = int(input('1. Hiển thị danh sách liên lạc\n2. Thêm liên lạc\n3. Kiểm tra liên lạc\n4. Xóa liên lạc\n5. Sửa liên lạc\n6. Thoát\nNhập chức năng bạn sử dụng: '))
    print('_'*50)
    return entry

def phonebook():
    lienlac = []
    while True:
        entry = chucnang()
        if entry == 1:
            f = open(r"D:\Tu_duy_lap_trinh\ĐỒ ÁN\contact.txt", "r", encoding="utf-8-sig")
            lienlac = f.readlines()
            f.close()
            if not lienlac:
                print("Danh sách liên lạc trống")
            else:
                for i in lienlac:
                    print(i) 

        elif entry == 2:
            sdt = input("Nhập số điện thoại cần thêm: ")
            ktra = False
            f = open(r"D:\Tu_duy_lap_trinh\ĐỒ ÁN\contact.txt", "r", encoding="utf-8-sig")
            lienlac = f.readlines()
            f.close()
            for i in lienlac:
                if i.find(sdt) != -1:
                    print("Liên lạc đã tồn tại!")
                    ktra = True
                    break
            if ktra == False:
                ten = input('Nhập tên liên lạc cần thêm: ')
                f = open(r"D:\Tu_duy_lap_trinh\ĐỒ ÁN\contact.txt", "a", encoding="utf-8-sig")
                lienlac.append( ten + " - " + sdt + "\n")
                lienlac = f.write(lienlac[-1])
                f.close()
                print("Liên lạc đã được lưu! ")

        elif entry == 3:
            ktra = False
            f = open(r"D:\Tu_duy_lap_trinh\ĐỒ ÁN\contact.txt", "r", encoding="utf-8-sig")
            lienlac = f.readlines()
            f.close()
            ten = input("Nhập tên liên lạc muốn tìm:")
            for i in lienlac:
                if i.find(ten) != -1:
                    print(i)
                    ktra = True
                    break
            if ktra == False:
                print("Liên lạc không tồn tại!")


        elif entry == 4:
            ktra = False
            delete_var = 0
            f = open(r"D:\Tu_duy_lap_trinh\ĐỒ ÁN\contact.txt", "r", encoding="utf-8-sig")
            lienlac = f.readlines()
            f.close()
            ten = input("Nhập tên liên lạc muốn xoá:")
            for i in lienlac:
                if i.find(ten) != -1:
                    print(i)
                    delete_var = lienlac.index(i)
                    ktra = True
                    confirm = input("Bạn có chắc chắn xóa? Y/N:")
                    if confirm.capitalize() == "Y":
                        lienlac.pop(delete_var)
                        print(f'Đã xoá khỏi danh bạ')
                        f = open(r"D:\Tu_duy_lap_trinh\ĐỒ ÁN\contact.txt", "w", encoding="utf-8-sig")
                        for i in lienlac:
                            f.write(i)
                        f.close()
                    else:
                        print("Quay trở lại menu!")
                    break
            if ktra == False:
                print("Liên lạc không tồn tại")

        elif entry == 5:            
            ktra = False
            fix = 0
            f = open(r"D:\Tu_duy_lap_trinh\ĐỒ ÁN\contact.txt", "r", encoding="utf-8-sig")
            lienlac = f.readlines()
            f.close()
            ten = input("Nhập tên liên lạc cần sửa:")
            for i in lienlac:
                if i.find(ten) != -1:
                    fix = lienlac.index(i)
                    ktra = True
                    sua_ten = str(input("Nhập lại tên cần sửa:"))
                    sua_sdt = str(input("Nhập lại sdt cần sửa:"))
                    lienlac.pop(fix)
                    lienlac.append(sua_ten + " - " + sua_sdt)
                    print(">>>> Đã lưu")
                    f = open(r"D:\Tu_duy_lap_trinh\ĐỒ ÁN\contact.txt", "w", encoding="utf-8-sig")
                    for i in lienlac:
                        lienlac = f.write(i)
                    f.close()
                    break               
            if ktra == False:
               print("Liên lạc không tồn tại")

        elif entry == 6:
            print("Xin cảm ơn đã sử dụng!")
            break
        else:
            print("Mời bạn nhập lại!")

phonebook()