import tkinter as tk
from tkinter import messagebox

def add_data():
    try:
        person_code = int(person_code_entry.get())
        if person_code < 1 or person_code > 4:
            raise ValueError("Invalid person code. Please enter a value between 1 and 4.")

        person_names = ["Mani M K", "Raman M K", "Tamil M K", "Prakash M K"]
        person_name = person_names[person_code - 1]

        bno = int(beam_no_entry.get())
        mtr = int(meter_entry.get())
        col = color_entry.get()

        total_bno.append((len(total_bno) + 1, bno))
        total_mtr.append(mtr)
        total_col.append(col)

        result_text.insert(tk.END, f"{len(total_bno)}. {person_name} - {bno} - {mtr} - {col}\n")
        total_beam_no_var.set(len(total_bno))
        total_meter_var.set(sum(total_mtr))
        total_colors_var.set(len(set(total_col)))

        serial_number_var.set(len(total_bno) + 1)
        person_code_entry.delete(0, tk.END)
        beam_no_entry.delete(0, tk.END)
        meter_entry.delete(0, tk.END)
        color_entry.delete(0, tk.END)

    except ValueError as e:
        messagebox.showerror("Error", str(e))

def on_exit():
    window.destroy()

total_bno = []
total_mtr = []
total_col = []

window = tk.Tk()
window.title("Beam and Meter Report")

tk.Label(window, text="Person Code (1-4):").grid(row=0, column=0, padx=5, pady=5)
person_code_entry = tk.Entry(window)
person_code_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(window, text="Beam.no:").grid(row=1, column=0, padx=5, pady=5)
beam_no_entry = tk.Entry(window)
beam_no_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(window, text="Meter:").grid(row=2, column=0, padx=5, pady=5)
meter_entry = tk.Entry(window)
meter_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(window, text="Color:").grid(row=3, column=0, padx=5, pady=5)
color_entry = tk.Entry(window)
color_entry.grid(row=3, column=1, padx=5, pady=5)

add_button = tk.Button(window, text="Add Data", command=add_data)
add_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

result_text = tk.Text(window, height=10, width=40)
result_text.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

tk.Label(window, text="Total Beam No:").grid(row=6, column=0, padx=5, pady=5)
total_beam_no_var = tk.IntVar()
total_beam_no_label = tk.Label(window, textvariable=total_beam_no_var)
total_beam_no_label.grid(row=6, column=1, padx=5, pady=5)

tk.Label(window, text="Total Meter:").grid(row=7, column=0, padx=5, pady=5)
total_meter_var = tk.IntVar()
total_meter_label = tk.Label(window, textvariable=total_meter_var)
total_meter_label.grid(row=7, column=1, padx=5, pady=5)

tk.Label(window, text="Total Colors:").grid(row=8, column=0, padx=5, pady=5)
total_colors_var = tk.IntVar()
total_colors_label = tk.Label(window, textvariable=total_colors_var)
total_colors_label.grid(row=8, column=1, padx=5, pady=5)

serial_number_var = tk.IntVar()
serial_number_var.set(1)

exit_button = tk.Button(window, text="Exit", command=on_exit)
exit_button.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()
