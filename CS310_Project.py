from tkinter import *
import ast

root = Tk()
root.title("Stock Program")

# อ่านไฟล์เพื่อนำเข้าโปรแกรม
with open("products.txt") as FILE:
    FILE = FILE.read()
    products = ast.literal_eval(FILE)

# Global varibles
second_loop_used = False
not_found_label_show = False
Not_Found_label = None
delete_rows = False
code_label = None
name_label = None
category_label = None
amount_label = None
add_button= None
delete_button = None

def ADD_BUTTON(index: int, mode = 1):
    '''
    ฟังก์ชันการทำงานเมื่อกดปุ่มเพิ่มสินค้า
    '''
    find = ""
    counts = 1
    for category in products:
        if find != "":
            break
        for code in products[category]:
            if find != "":
                break
            for name in products[category][code]:
                if index == counts:
                    find = name
                    break
                else:
                    counts += 1
    
    def add_to(num, find):
        '''
        sub function ของปุ่มเพิ่มสินค้า ทำหน้าที่อัพเดทจำนวนสินค้าแบบ real time
        '''
        num = int(num)
        for category in products:
            for code in products[category]:
                for name in products[category][code]:
                    if find == name:
                        products[category][code][name] += num
        main_loop()
    
    def CANCEL_BUTTON():
        '''
        sub function ของปุ่มเพิ่มสินค้า หากมีกดปุ่มยกเลิก
        '''
        global delete_rows, second_loop_used
        if second_loop_used == True:
            delete_rows = True
            second_loop()
        summit_button.destroy()
        e.destroy()
        cancel_button.destroy()

    if mode == 1:
        e = Entry(root, width=20, borderwidth=5)
        summit_button = Button(root, text="เพิ่มจำนวนสินค้า", command=lambda: add_to(e.get(), find))
        cancel_button = Button(root, text="ยกเลิก", command=CANCEL_BUTTON)
        line = len(products["Bakery"]) + len(products["Drink"])
        e.grid(row=line+1, column=1)
        summit_button.grid(row=line+1, column=2)
        cancel_button.grid(row=line+1, column=3)
        e.delete(0, END)
    else:
        e = Entry(root, width=20, borderwidth=5)
        summit_button = Button(root, text="เพิ่มจำนวนสินค้า", command=lambda: add_to(e.get(), find))
        cancel_button = Button(root, text="ยกเลิก", command=CANCEL_BUTTON)
        line = len(products["Bakery"]) + len(products["Drink"]) + 3
        e.grid(row=line+1, column=1)
        summit_button.grid(row=line+1, column=2)
        cancel_button.grid(row=line+1, column=3)
        e.delete(0, END)

def DELETE_BUTTON(index: int, mode = 1):
    '''
    ฟังก์ชันการทำงาน เมื่อมีการกดปุ่มลดสินค้า
    '''
    find = ""
    counts = 1
    for category in products:
        if find != "":
            break
        for code in products[category]:
            if find != "":
                break
            for name in products[category][code]:
                if index == counts:
                    find = name
                    break
                else:
                    counts += 1
    def delete_to(num, find):
        '''
        sub function ของปุ่มลดสินค้า มีหน้าที่อัพเดทจำนวนสินค้าแบบ real time
        '''
        num = int(num)
        for category in products:
            for code in products[category]:
                for name in products[category][code]:
                    if find == name:
                        products[category][code][name] -= num
        main_loop()

    def CANCEL_BUTTON():
        '''
        sub function ของปุ่มลดสินค้า เมื่อมีการกดปุ่มยกเลิก
        '''
        global delete_rows, second_loop_used
        if second_loop_used == True:
            delete_rows = True
            second_loop()
        summit_button.destroy()
        e.destroy()
        cancel_button.destroy()

    if mode == 1:
        e = Entry(root, width=20, borderwidth=5)
        summit_button = Button(root, text="ลดจำนวนสินค้า", command=lambda: delete_to(e.get(), find))
        cancel_button = Button(root, text="ยกเลิก", command=CANCEL_BUTTON)
        line = len(products["Bakery"]) + len(products["Drink"])
        e.grid(row=line+1, column=1)
        summit_button.grid(row=line+1, column=2)
        cancel_button.grid(row=line+1, column=3)
        e.delete(0, END)
    else:
        e = Entry(root, width=20, borderwidth=5)
        summit_button = Button(root, text="ลดจำนวนสินค้า", command=lambda: delete_to(e.get(), find))
        cancel_button = Button(root, text="ยกเลิก", command=CANCEL_BUTTON)
        line = len(products["Bakery"]) + len(products["Drink"]) + 3
        e.grid(row=line+1, column=1)
        summit_button.grid(row=line+1, column=2)
        cancel_button.grid(row=line+1, column=3)
        e.delete(0, END)


def SEARCH_BUTTON():
    '''
    ฟังก์ชันการทำงานของปุ่ม ค้นหาสินค้า
    '''
    search_button1.destroy()
    def FIND_BUTTON(target):
        '''
        sub function ของปุ่มค้นหาสินค้า มีหน้าที่แสดงผลการค้นหา
        '''
        second_loop(target)
        search_bar.delete(0, END)
    
    def CANCEL_BUTTON():
        '''
        sub fucntion ของปุ่มค้นหาสินต้า เมื่อมีการกดปุ่มยกเลิก
        '''
        search_button1.destroy()
        global delete_rows, second_loop_used, not_found_label_show, Not_Found_label
        if second_loop_used == True:
            delete_rows = True
            second_loop()
        if not_found_label_show == True:
            Not_Found_label.destroy()
        search_bar.destroy()
        new_search_button.destroy()
        details.destroy()
        cancel_button.destroy()
        search_button = Button(root, text="ค้นหาสินค้า", padx=10, command=SEARCH_BUTTON)
        search_button.grid(row=len(products["Bakery"]) + len(products["Drink"]) + 2, columnspan=8)
    search_bar = Entry(root, width=35, borderwidth=5)
    details = Label(root, text="ใส่รหัสสินค้าที่ต้องการค้นหา:")
    new_search_button = Button(root, text="ค้นหา", command=lambda: FIND_BUTTON(search_bar.get()))
    cancel_button = Button(root, text="ยกเลิก",command=CANCEL_BUTTON)
    details.grid(row=(len(products["Bakery"])+len(products["Drink"])+2))
    search_bar.grid(row=(len(products["Bakery"])+len(products["Drink"])+2), column=1)
    new_search_button.grid(row=(len(products["Bakery"])+len(products["Drink"])+2), column=2)
    cancel_button.grid(row=len(products["Bakery"]) + len(products["Drink"]) + 2, column=3)

def ADD_PRODUCT():
    '''
    เพิ่มประเภทสินต้า
    '''

def main_loop():
    '''
    เป็น loop หลักเพื่อแสดงตารางรายการสินค้าที่มีการเปลี่ยนแปลงตลอดเวลา
    '''
    i = 1
    for category in products:
        for code in products[category]:
            for name in products[category][code]:
                code_label1 = Label(root, text=code, relief="groove", padx=10, bg="white", fg="black")
                code_label1.grid(row=i, column=0, sticky="news")
                name_label1 = Label(root, text=name, relief="groove", padx=100,  bg="white", fg="black")
                name_label1.grid(row=i, column=1, sticky="news")
                category_label1 = Label(root, text=category, relief="groove", padx=10,  bg="white", fg="black")
                category_label1.grid(row=i, column=2, sticky="news")
                amount_label1 = Label(root, text=str(products[category][code][name]), relief="groove", padx=10, bg="white", fg="black")
                amount_label1.grid(row=i, column=3, sticky="news")
                add_button1 = Button(root, text="เพิ่ม", padx=10, command=lambda x=i: ADD_BUTTON(x))
                add_button1.grid(row=i, column=4, sticky="news")
                delete_button1 = Button(root, text="ลด", padx=10, command=lambda x=i: DELETE_BUTTON(x))
                delete_button1.grid(row=i, column=5, sticky="news")
                i += 1


def second_loop(target = ""):
    '''
    loop รองที่มีการแสดงผลคงที่ไม่มีการเปลี่ยนแปลง
    '''
    global delete_rows
    global second_loop_used
    global not_found_label_show, Not_Found_label
    global code_label, name_label, category_label, amount_label, add_button, delete_button
    if target != "":
        delete_rows = False
        second_loop_used = True
        i = 1
        found = False
        for category in products:
            for code in products[category]:
                for name in products[category][code]:
                    if code == target:
                        line = (len(products["Bakery"]) + len(products["Drink"])+3)
                        code_label = Label(root, text=code, relief="groove", padx=10, bg="white", fg="black")
                        code_label.grid(row=line, column=0, sticky="news")
                        name_label = Label(root, text=name, relief="groove", padx=100,  bg="white", fg="black")
                        name_label.grid(row=line, column=1, sticky="news")
                        category_label = Label(root, text=category, relief="groove", padx=10,  bg="white", fg="black")
                        category_label.grid(row=line, column=2, sticky="news")
                        amount_label = Label(root, text=str(products[category][code][name]), relief="groove", padx=10, bg="white", fg="black")
                        amount_label.grid(row=line, column=3, sticky="news")
                        add_button = Button(root, text="เพิ่ม", padx=10, command=lambda x=i: ADD_BUTTON(x, 2))
                        add_button.grid(row=line, column=4, sticky="news")
                        delete_button = Button(root, text="ลด", padx=10, command=lambda x=i: DELETE_BUTTON(x, 2))
                        delete_button.grid(row=line, column=5, sticky="news")
                        found = True
                        break
                    else:
                        i += 1
        if found == False:
            Not_Found_label = Label(root, text="ไม่พบสินค้าที่ค้นหา", relief="groove", padx=10, bg="white", fg="black")
            Not_Found_label.grid(row=(len(products["Bakery"]) + len(products["Drink"])+3), columnspan=8)
            second_loop_used = False
            not_found_label_show = True
    
    if delete_rows == True:
        code_label.destroy()
        name_label.destroy()
        category_label.destroy()
        amount_label.destroy()
        delete_button.destroy()
        add_button.destroy()
        second_loop_used = False

# การแสดงผลที่จำเป็นทั้งหมด
table1 = Label(root, text="รหัส", borderwidth=1, relief="groove", width=5, padx=10, pady=10, bg="white", fg="black")
table2 = Label(root, text="ชื่อสินค้า", borderwidth=1, relief="groove", width=10, padx=100, pady=10, bg="white", fg="black")
table3 = Label(root, text="หมวดหมู่", borderwidth=1, relief="groove", width=5, padx=10, pady=10, bg="white", fg="black")
table4 = Label(root, text="จำนวน", borderwidth=1, relief="groove", width=5, padx=10, pady=10, bg="white", fg="black")
table5 = Label(root, text="หมายเหตุ", borderwidth=1, relief="groove", width=8, padx=10, pady=10, bg="white", fg="black")
table1.grid(row=0, column=0, sticky="news")
table2.grid(row=0, column=1, sticky="news")
table3.grid(row=0, column=2, sticky="news")
table4.grid(row=0, column=3, sticky="news")
table5.grid(row=0, column=4, sticky="news", columnspan=2)
search_button1 = Button(root, text="ค้นหาสินค้า", padx=10, command=SEARCH_BUTTON)
search_button1.grid(row=(len(products["Bakery"])+len(products["Drink"])+2), columnspan=8)
main_loop()
    



root.mainloop()

# อัพเดทรายการสินค้าในไฟล์ เพื่อการใช้โปรแกรมครั้งต่อไป
with open("products.txt", "w") as file:
    file.write(str(products))