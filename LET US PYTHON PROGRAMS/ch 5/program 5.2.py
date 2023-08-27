'''in a company an employ is paid as under:

if his basic salary is less than ₹ 1500 the HRA(house rent allowence) = 10 % of his basic salary and DA(dearness allowence) = 90% of basic salary.If his salary is either equal to or above ₹ 1500
then HRA = ₹500 and DA = 98% of basic salary.write a program to find gross salary. 
'''
basicsalary = int(input("enter basic salary in rupees --> ₹"))

if basicsalary < 1500:
    HRA = 10/100 * basicsalary
    DA = 90/100 * basicsalary
else:
    HRA = 500
    DA = 98/100 * basicsalary

totalsalary = basicsalary + HRA + DA
print("total salary >>> ₹",totalsalary)