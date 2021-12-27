def welcome():
    entry = int(input("""
                        1. Hiển thị
                        2. Thêm liên lạc
                        3. Kiểm tra danh bạ
                        4. Xóa liên lạc
                        5. Sửa liên lạc
                        6. Thoát
                        Enter your number: """))
    return entry


def phonebook():
    contacts = []
    while True:
        entry = welcome()
        if entry == 1:
            f = open(r"D:\Tu_duy_lap_trinh\ĐỒ ÁN\contact.txt", "r", encoding="utf-8-sig")
            contacts = f.readlines()
            f.close()
            if not contacts:
                print("Danh sách liên lạc trống")
            else:
                for i in contacts:
                    print(i) 

        elif entry == 2:
            phone_number = input("So dien thoai: ")
            name = input("Ten lien lac: ")
            check = False
            f = open(r"D:\Tu_duy_lap_trinh\ĐỒ ÁN\contact.txt", "r", encoding="utf-8-sig")
            contacts = f.readlines()
            f.close()
            for i in contacts:
                if i.find(phone_number) != -1:
                    print("Lien lac da ton tai!")
                    check = True
                    break
            if check == False:
                f = open(r"D:\Tu_duy_lap_trinh\ĐỒ ÁN\contact.txt", "w", encoding="utf-8-sig")
                contacts.append(name + " - " + phone_number + "\n")
                contacts = f.write(contacts[-1])
                f.close()
                print("Lien lac da duoc luu")

        elif entry == 3:
            checked = False
            f = open(r"D:\Tu_duy_lap_trinh\ĐỒ ÁN\contact.txt", "r", encoding="utf-8-sig")
            contacts = f.readlines()
            f.close()
            name = input("Nhập tên liên lạc:")
            for i in contacts:
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
            contacts = f.readlines()
            f.close()
            name = input("Nhập tên liên lạc:")
            for i in contacts:
                if i.find(name) != -1:
                    print(i)
                    delete_var = contacts.index(i)
                    checked = True
                    confirm = input("Bạn có chắc chắn xóa? Y/N:")
                    if confirm.capitalize() == "Y":
                        contacts.pop(delete_var)
                        print(f'Đã xoá khỏi danh bạ')
                        f = open(r"D:\Tu_duy_lap_trinh\ĐỒ ÁN\contact.txt", "w", encoding="utf-8-sig")
                        for i in contacts:
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
            contacts = f.readlines()
            f.close()
            name = input("Nhập tên liên lạc:")
            for i in contacts:
                if i.find(name) != -1:  
                    checked == True
                    fix = contacts.index(i)                    
                    fix_name = str(input(" Nhập lại tên cần sửa:"))
                    fix_phone = str(input(" Nhập lại phone cần sửa:"))
                    contacts.pop(fix)
                    contacts.append(fix_name + " - " + fix_phone)
                    print(">>>> Đã lưu")
                    f = open(r"D:\Tu_duy_lap_trinh\ĐỒ ÁN\contact.txt", "w", encoding="utf-8-sig")
                    for i in contacts:
                        contacts = f.write(contacts(i))
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