import shapes as sh

print("Enter choice:")
print("1--circle")
print("2--triangle")
print("3--rectangle")
print("4--square")
print("5--exit")

sum_area=0
total_square_count=0
total_circle_count=0
total_triangle_count=0
total_rectangle_count=0
filled_area=0
unfilled_area=0   

while True:
    ch = int(input("Enter your choice: "))
    if ch ==1:
        obj=sh.circle(5,"red",True)
        obj.show_info()
        total_circle_count += 1
    elif ch==2:
        obj=sh.triangle(5,10,"blue",False)
        obj.show_info()
        total_triangle_count += 1
    elif ch==3:
        obj=sh.rectangle(8,4,"Yellow",True)
        obj.show_info()
        total_rectangle_count += 1
    elif ch==4:
        obj=sh.square(4,"green",False)
        obj.show_info()
        total_square_count += 1
    else:
        print("Summary: ")
        print("Total Area",sum_area)
        print("Total Squares",total_square_count)
        print("Total Circles",total_circle_count)
        print("Total Triangles",total_triangle_count)
        print("Total Rectangles",total_rectangle_count)
        print("Total Filled area",filled_area)
        print("Total Unfilled area",unfilled_area)
        print("exit")
        break

    sum_area+=obj.calc_area()

    if obj.is_filled == True:
        filled_area += obj.calc_area()
    else:
        unfilled_area += obj.calc_area()
