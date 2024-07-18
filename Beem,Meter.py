print("Report of Beam and Meter")
total_Bno = []
total_Mtr = []
total_Col = []
serial_number = 1

while True:
    Person_code = input("Enter the person code (or type 'exit' to quit): ")
    if Person_code.lower() == 'exit':
        break

    try:
        Person_code = int(Person_code)
        if Person_code == 1:
            print("Mani M K")
            Bno = int(input("Enter the Beam.no : "))
            Mtr = int(input("Enter the Meter   : "))
            Col = input("Enter the colour  : ")

            total_Bno.append((serial_number, Bno))
            total_Mtr.append(Mtr)
            total_Col.append(Col)
            serial_number += 1

        elif Person_code == 2:
            print("Raman M K")
            Bno = int(input("Enter the Beam.no : "))
            Mtr = int(input("Enter the Meter   : "))
            Col = input("Enter the colour  : ")

            total_Bno.append((serial_number, Bno))
            total_Mtr.append(Mtr)
            total_Col.append(Col)
            serial_number += 1

        elif Person_code == 3:
            print("Tamil M K")
            Bno = int(input("Enter the Beam.no : "))
            Mtr = int(input("Enter the Meter   : "))
            Col = input("Enter the colour  : ")

            total_Bno.append((serial_number, Bno))
            total_Mtr.append(Mtr)
            total_Col.append(Col)
            serial_number += 1

        elif Person_code == 4:
            print("Prakash M K")
            Bno = int(input("Enter the Beam.no : "))
            Mtr = int(input("Enter the Meter   : "))
            Col = input("Enter the colour  : ")

            total_Bno.append((serial_number, Bno))
            total_Mtr.append(Mtr)
            total_Col.append(Col)
            serial_number += 1

        else:
            print("Invalid person code. Please enter either '1' or '2'.")

    except ValueError:
        print("Invalid input. Please enter a valid integer or 'exit'.")

print("Beam.no:")
print("Serial - Beem.no - Meter - Color")
for i in range(len(total_Bno)):
    serial, bno = total_Bno[i]
    Mtr = total_Mtr[i]
    Col = total_Col[i]
    print(f"{serial} - {bno} - {Mtr} - {Col}")

print("Total Beem.No:", serial_number - 1)
print("Total Meter:", sum(total_Mtr))
print("Total Colors:", len(set(total_Col)))
