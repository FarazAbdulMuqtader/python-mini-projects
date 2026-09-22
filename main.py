import vehicle as v
import drone_fire_fighter as dff
import drone as d
import fire_engine as fe

fire_engine=fe.fire_engine("5634021")
Drone=d.Drone("45932-1")
Drone_fire_fighter=dff.drone_fire("455833")
sh=[]
FE=[]
D=[]
DFF=[]
while True:
    print("Welcome to Metropolitan Service Station")
    print("1-> Add Vehicle ")
    print("2-> Raise Alarm ")
    print("3-> Maintain Vehicle ")
    print("4-> Recharge ")
    print("5-> Exit ")
    ch=input("Enter your choice: ")

    if ch == "1":
        while True:
            print("Options: ")
            print("1-> Fire Engine")
            print("2-> Drone")
            print("3-> Drone fire fighter")
            print("4-> Quit")
            op=input("Enter your Option: ")
            if op=="1":
                FE.append(fire_engine)
            elif op=="2":
                D.append(Drone)
            elif op=="3":
                DFF.append(Drone_fire_fighter)
            elif op=="4":
                print("Summary:")
                print(FE)
                print(D)
                print(DFF)
                break
            else:
                print("Invalid Key")
    elif ch == "2":
        while True:
            print("Options: ")
            print("1-> Fire Engine")
            print("2-> Drone")
            print("3-> Drone fire fighter")
            print("4-> Quit")
            op=input("Enter your Option: ")
            if op=="1":
                print(fire_engine.service_provided())
            elif op=="2":
                pass
            elif op=="3":
                pass
            elif op=="4":
                break
            else:
                print("Invalid Key")
    elif ch == "3":
        pass
    elif ch == "4":
        pass
    elif ch == "5":
        break
    else:
        print("Invalid Key.")
