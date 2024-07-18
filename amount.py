from datetime import datetime

current_date = datetime.now().date()
print("Report of Amount Details")
p_Description = []
p_Wages = []
p_Singles = []
p_Amount = []
p_Magimai = []
p_Tharam = []


serial_number = 1
no = "RGGST837/21-22"
date = current_date
tin_no = "955"
cst_no = "9646ryfh"

while True:
    Person_code = input("Enter the person code (or type 'exit' to quit): ")
    if Person_code.lower() == 'exit':
        break
    try:
        Person_code = int(Person_code)
        if Person_code == 1:
            print("Mani M K")
            Des = input("Enter the Description:")
            Wages = float(input("Enter the Wages:"))
            Singles = float(input("Enter the singles:"))
            Amount = Wages * Singles
            Magimai = float(input("Enter the Less:Magimai:"))
            Tharam = float(input("Enter the Less:Tharam:"))
            Tds = input("Enter the TDS on Contract:")
            Round_off = float(input("Enter the round_off:"))
            Total_singles = float(input("Enter the Total singles:"))
            p_Description.append((serial_number, Des))
            p_Wages.append(Wages)
            p_Singles.append(Singles)
            p_Amount.append(Amount)
            p_Magimai.append(Magimai)
            p_Tharam.append(Tharam)

            serial_number += 1

        elif Person_code == 2:
            print("Raman M K")
            Des = input("Enter the Description:")
            Wages = float(input("Enter the Wages:"))
            Singles = float(input("Enter the singles:"))
            Amount = Wages * Singles
            Magimai = float(input("Enter the Less:Magimai:"))
            Tharam = float(input("Enter the Less:Tharam:"))
            Tds = input("Enter the TDS on Contract:")
            Round_off = float(input("Enter the round_off:"))
            Total_singles = float(input("Enter the Total singles:"))
            p_Description.append((serial_number, Des))
            p_Wages.append(Wages)
            p_Singles.append(Singles)
            p_Amount.append(Amount)
            p_Magimai.append(Magimai)
            p_Tharam.append(Tharam)
            serial_number += 1
        elif Person_code == 3:
            print("Tamil M K")
            Des = input("Enter the Description:")
            Wages = float(input("Enter the Wages:"))
            Singles = float(input("Enter the singles:"))
            Amount = Wages * Singles
            Magimai = float(input("Enter the Less:Magimai:"))
            Tharam = float(input("Enter the Less:Tharam:"))
            Tds = input("Enter the TDS on Contract:")
            Round_off = float(input("Enter the round_off:"))
            Total_singles = float(input("Enter the Total singles:"))
            p_Description.append((serial_number, Des))
            p_Wages.append(Wages)
            p_Singles.append(Singles)
            p_Amount.append(Amount)
            p_Magimai.append(Magimai)
            p_Tharam.append(Tharam)
            serial_number += 1

        elif Person_code == 4:
            print("Prakash M K")
            Des = input("Enter the Description:")
            Wages = float(input("Enter the Wages:"))
            Singles = float(input("Enter the singles:"))
            Amount = Wages * Singles
            Magimai = float(input("Enter the Less:Magimai:"))
            Tharam = float(input("Enter the Less:Tharam:"))
            Tds = input("Enter the TDS on Contract:")
            Round_off = float(input("Enter the round_off:"))
            Total_singles = float(input("Enter the Total singles:"))
            p_Description.append((serial_number, Des))
            p_Wages.append(Wages)
            p_Singles.append(Singles)
            p_Amount.append(Amount)
            p_Magimai.append(Magimai)
            p_Tharam.append(Tharam)
            serial_number += 1

        else:
            print("Invalid person code. Please enter either '1', '2', '3', or '4'.")
    except ValueError:
        print("Invalid input. Please enter a valid integer for the person code.")

print("Detail of report:")
print("No:", no)
print("Date:", date)
print("TIN NO:", tin_no)
print("CST NO:", cst_no)
print("Serial - Description - Wages - Singles - Amount")
for i in range(len(p_Description)):
    serial, Des = p_Description[i]
    Wages = p_Wages[i]
    Singles = p_Singles[i]
    Amount = p_Amount[i]
    print(f"{serial} - {Des} - {Wages} - {Singles} - {Amount}")

print("Sub Amount:", sum(p_Amount))
print("Less : Magimai:", sum(p_Magimai))
print("Less : Tharam:", sum(p_Tharam))
print("TDS ON CONTRACT:", Tds)
print("Rounded off:", Round_off)

final_total = sum(p_Amount) - sum(p_Magimai) - sum(p_Tharam) - Round_off
print("Final Total:", final_total)

print("Singles Details")
print("Total Singles:", Total_singles)
print("Received Singles:", sum(p_Singles))
print("Balanced singles:", Total_singles- sum(p_Singles))
