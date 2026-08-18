import tollbooth as tb
while True:
    I=input("Enter 1 for car passed with payment, 2 for car passed without payment, 3 to exit: ")
    if I=="1":
        tb.toll1.car_passed(True)
    elif I=="2":
        tb.toll1.car_passed(False)
    elif I=="3":
        print("Total cars passed without payment:", tb.toll1.car_count)
        print("Total amount collected:", tb.toll1.amount)
        print("Collection of registration numbers:", tb.toll1.collection_of_reg)
        print(tb.toll1.defaulters())
        break