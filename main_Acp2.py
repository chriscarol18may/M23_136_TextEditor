import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        # Retrieve user inputs and convert to floats
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        time = float(entry_time.get())
        
        # Check which radio button is selected (1 = Simple, 2 = Compound)
        interest_type = var_type.get()
        
        if interest_type == 1:
            # Simple Interest Formula: (P * R * T) / 100
            interest = (principal * rate * time) / 100
            total = principal + interest
        else:
            # Compound Interest Formula: P * (1 + R/100)^T
            total = principal * ((1 + (rate / 100)) ** time)
            interest = total - principal
            
        # Update result labels, formatted to 2 decimal places
        lbl_result_interest.config(text=f"Interest Earned: {interest:.2f}")
        lbl_result_total.config(text=f"Total Amount: {total:.2f}")
        
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values for Principal, Rate, and Time.")

# Set up the main window
window = tk.Tk()
window.title("Interest Calculator")
window.geometry("350x400")

# Principal Input
tk.Label(window, text="Principal Amount:").pack(pady=(15, 2))
entry_principal = tk.Entry(window, justify="center")
entry_principal.pack(pady=2)

# Rate Input
tk.Label(window, text="Rate of Interest (%):").pack(pady=(10, 2))
entry_rate = tk.Entry(window, justify="center")
entry_rate.pack(pady=2)

# Time Input
tk.Label(window, text="Time (Years):").pack(pady=(10, 2))
entry_time = tk.Entry(window, justify="center")
entry_time.pack(pady=2)

# Interest Type Selection (Radio Buttons)
var_type = tk.IntVar(value=1)  # Default value is 1 (Simple Interest)
frame_radio = tk.Frame(window)
frame_radio.pack(pady=15)

tk.Radiobutton(frame_radio, text="Simple Interest", variable=var_type, value=1).grid(row=0, column=0, padx=10)
tk.Radiobutton(frame_radio, text="Compound Interest", variable=var_type, value=2).grid(row=0, column=1, padx=10)

# Calculate Button
btn_calculate = tk.Button(window, text="Calculate", command=calculate_interest)
btn_calculate.pack(pady=10)

# Result Labels
lbl_result_interest = tk.Label(window, text="Interest Earned: 0.00", font=("Arial", 11))
lbl_result_interest.pack(pady=5)

lbl_result_total = tk.Label(window, text="Total Amount: 0.00", font=("Arial", 12, "bold"))
lbl_result_total.pack(pady=5)

# Run the application
window.mainloop()