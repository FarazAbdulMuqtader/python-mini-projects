import bank as b
import HEI 


b1 = b.Bank("UBL")
b1.add_emp("Faraz", "Manager")
print(b1.find_emp("Faraz"))    
print(b1.find_emp("ali"))     

h1 = HEI.HEI("UoK")
h1.add_emp("XYZ", "manager")
print(h1.find_emp("XYZ"))
print(h1.find_emp("zeeshan"))

uni = HEI.HEI("UoK")
uni.pay_salary(526689,"Faraz",50000)
