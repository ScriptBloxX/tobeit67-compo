def create_box(X, Y, n):
    box = [[' ' for _ in range(X)] for _ in range(Y)]  # สร้างกล่องเปล่า

    # ใส่ดาว (*) ลงในกล่อง
    for col in range(X):
        for row in range(Y):
            if n > 0:
                box[row][col] = '*'
                n -= 1

    # แสดงผลลัพธ์
    print("------")
    for row in range(Y):
        print('|' + ''.join(box[row]) + '|')
    print("------")

    # นับจำนวนดาวที่เหลือ
    remaining_stars = sum(row.count('*') for row in box)
    print(f"There are {remaining_stars} star left.")

# รับค่า X, Y, และ n จากผู้ใช้
X = int(input())
Y = int(input())
n = int(input())

# เรียกใช้ฟังก์ชัน
create_box(X, Y, n)
