import datetime

# Counter for serial number
serial_number = 1

# Lists to store delivery details
delivery_details = []

udai_total = {"Box_60s": 0, "Kg": 0, "Bondhu": 0}
pavu_total = {"_2_80_box": 0, "Kg_Pavu": 0, "Bondhu_Pavu": 0}

print("Delivery Report of Pavu, Udai, Nul")
print("Sender\n"
      "Sri Dhanam COMPANY\n"
      "27 EST Nagar\n"
      "First Street\n"
      "podhaturpet - 631208")

while True:
    Person_code = input("Enter the person code: ")
    if Person_code == '1':
        name = "Mani M K"
        address = "Big Street\nAthimanjeripet - 631202"
    elif Person_code == '2':
        name = "Raman M K"
        address = "School Street\nKunrathur - 600069"
    elif Person_code == '3':
        name = "Tamil M K"
        address = "Peri Street\nAnna Nagar - 631203"
    elif Person_code == '4':
        name = "Prakash M K"
        address = "Peri Street\nThiruttani - 631209"
    else:
        print("Invalid person code. Please try again.")
        continue

    print(f"TO\n{name}\n{address}")
    Delivery_No = input("Enter the Delivery No: ")
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print("Date:", formatted_datetime)
    Gst_No = input("Enter the GST NO: ")
    Beem_No = int(input("Enter the Beem No:"))
    Meter = int(input("Enter the Meter:"))
    Design = input("Enter the Design:")
    Design1 = input("Enter the Design:")
    print("SIZING DHANAM")
    vibaram = input("Enter the vibaram:")
    print("Detail of udai")
    box_60s = float(input("Enter the 60s Box:"))
    kg = float(input("Enter the Kg:"))
    bondhu = int(input("Enter the Bondhu:"))
    udai_total["Box_60s"] += box_60s
    udai_total["Kg"] += kg
    udai_total["Bondhu"] += bondhu
    print("Detail of Pavu")
    _2_80_box = float(input("Enter the 2/80 Box:"))
    kg_pavu = float(input("Enter the Kg_Pavu:"))
    bondhu_pavu = int(input("Enter the bondhu_Pavu:"))
    pavu_total["_2_80_box"] += _2_80_box
    pavu_total["Kg_Pavu"] += kg_pavu
    pavu_total["Bondhu_Pavu"] += bondhu_pavu

    delivery_details.append({
        "Name": name,
        "Address": address,
        "Delivery No": Delivery_No,
        "Date": formatted_datetime,
        "GST NO": Gst_No,
        "Beem No": Beem_No,
        "Meter": Meter,
        "Design": Design,
        "Design1": Design1,
        "Vibaram": vibaram,
        "60s Box": box_60s,
        "Kg": kg,
        "Bondhu": bondhu,
        "2/80 Box": _2_80_box,  # Corrected key
        "Kg Pavu": kg_pavu,
        "Bondhu Pavu": bondhu_pavu
    })

    print("Delivery details added successfully.")

    if input("Do you want to continue (y/n)? ").strip().lower() != 'y':
        break

# Print the delivery details table
print("\nDelivery Details Table")
print(
    "--------------------------------------------------------------------------------------------------------------------")
print(
    "Sr. No | Name      | Address                      | Delivery No | Date                | GST NO | Beem No | Meter | Design | Design1 | Vibaram | 60s Box | Kg | Bondhu | 2/80 Box | Kg_Pavu | Bondhu_Pavu")
print(
    "--------------------------------------------------------------------------------------------------------------------")
for i, details in enumerate(delivery_details, start=1):
    print(
        f"{i:6} | {details['Name']:9} | {details['Address']:28} | {details['Delivery No']:11} | {details['Date']:19} | {details['GST NO']:6} | {details['Beem No']:8} | {details['Meter']:6} | {details['Design']:7} | {details['Design1']:8} | {details['Vibaram']:8} | {details['60s Box']:8} | {details['Kg']:2} | {details['Bondhu']:6} | {details['2/80 Box']:8} | {details['Kg Pavu']:2} | {details['Bondhu Pavu']:6}")
print(
    "--------------------------------------------------------------------------------------------------------------------")

# Print Total for Detail of udai
print("\nTotal for Detail of Udai:")
print(f"Box_60s: {udai_total['Box_60s']}")
print(f"Kg: {udai_total['Kg']}")
print(f"Bondhu: {udai_total['Bondhu']}")

# Print Total for Detail of Pavu
print("\nTotal for Detail of Pavu:")
print(f"2/80 Box: {pavu_total['_2_80_box']}")
print(f"Kg_Pavu: {pavu_total['Kg_Pavu']}")
print(f"Bondhu_Pavu: {pavu_total['Bondhu_Pavu']}")