def chucnang():
    entry = int(input('1. Hiển thị danh sách liên lạc\n2. Thêm liên lạc\n3. Kiểm tra liên lạc\n4. Xóa liên lạc\n5. Sửa liên lạc\n6. Thoát\nNhập chức năng bạn sử dụng: '))
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
            phone_number = input("So dien thoai: ")
            name = input("Ten lien lac: ")
            check = False
            f = open(r"D:\Tu_duy_lap_trinh\ĐỒ ÁN\contact.txt", "r", encoding="utf-8-sig")
            lienlac = f.readlines()
            f.close()
            for i in lienlac:
                if i.find(phone_number) != -1:
                    print("Lien lac da ton tai!")
                    check = True
                    break
            if check == False:
                f = open(r"D:\Tu_duy_lap_trinh\ĐỒ ÁN\contact.txt", "w", encoding="utf-8-sig")
                lienlac.append(name + " - " + phone_number + "\n")
                lienlac = f.write(lienlac[-1])
                f.close()
                print("Lien lac da duoc luu")

        elif entry == 3:
            checked = False
            f = open(r"D:\Tu_duy_lap_trinh\ĐỒ ÁN\contact.txt", "r", encoding="utf-8-sig")
            lienlac = f.readlines()
            f.close()
            name = input("Nhập tên liên lạc:")
            for i in lienlac:
                if i.find(name) != -1:
                    print(i)
                    checked = True
                    break
            if checked == False:
                print("Liên lạc không tồn tại")


        elif entry == 4:
            checked = False
            delete_var = 0
            f = open(r"D:\Tu_duy_lap_trinh\ĐỒ ÁN\contact.txt", "r", encoding="utf-8-sig")
            lienlac = f.readlines()
            f.close()
            name = input("Nhập tên liên lạc:")
            for i in lienlac:
                if i.find(name) != -1:
                    print(i)
                    delete_var = lienlac.index(i)
                    checked = True
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
            if checked == False:
                print("Liên lạc không tồn tại")

        elif entry == 5:            
            checked = False
            f = open(r"D:\Tu_duy_lap_trinh\ĐỒ ÁN\contact.txt", "r", encoding="utf-8-sig")
            lienlac = f.readlines()
            f.close()
            name = input("Nhập tên liên lạc:")
            for i in lienlac:
                if i.find(name) != -1:  
                    checked == True
                    fix = lienlac.index(i)                    
                    fix_name = str(input(" Nhập lại tên cần sửa:"))
                    fix_phone = str(input(" Nhập lại phone cần sửa:"))
                    lienlac.pop(fix)
                    lienlac.append(fix_name + " - " + fix_phone)
                    print(">>>> Đã lưu")
                    f = open(r"D:\Tu_duy_lap_trinh\ĐỒ ÁN\contact.txt", "w", encoding="utf-8-sig")
                    for i in lienlac:
                        lienlac = f.write(lienlac(i))
                    f.close()
                    break               
            if check == False:
               print(" Liên lạc không tồn tại")

        elif entry == 6:
            print("Xin cảm ơn!")
            break
        else:
            print("Mời bạn nhập lại!")

phonebook()