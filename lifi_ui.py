import tkinter as tk
import sys
from lifi import LiFiDevice
import threading

if len(sys.argv) != 2:
        print("Usage: python lifi_ui.py <master_brick_uid>")
        sys.exit(1)

def send_text():
    user_input = entry.get()
    entry.delete(0, tk.END)  # Clear input field immediately
    threading.Thread(target=lifi_device.send_text, args=(user_input,), daemon=True).start()

def write_log(message, color="black", end="\n", send_or_receive_log="sending"):

    if send_or_receive_log == "sending":
        text_widget = sending_log
    elif send_or_receive_log == "receiving":
        text_widget = receiving_log

    if color not in ("red", "green", "blue", "black", "white", "yellow"):
        color = "black"

    def log_to_ui():
        text_widget.insert(tk.END, f"{message}{end}", color)
        text_widget.see(tk.END)
        text_widget.update_idletasks()

    root.after(0, log_to_ui)

# Main window
root = tk.Tk()
root.geometry("900x400")

# Label for input field
label = tk.Label(root, text="Text Message:")
label.pack(anchor="w", padx=20, pady=(10, 5))

# Frame for input and button
input_frame = tk.Frame(root)
input_frame.pack(anchor="w", padx=20, pady=(0, 10))

# Input field
entry = tk.Entry(input_frame, width=30)
entry.pack(side=tk.LEFT)

# Button
button = tk.Button(input_frame, text="Submit", command=send_text)
button.pack(side=tk.LEFT, padx=5)

# Log section using grid for equal-size columns
log_frame = tk.Frame(root)
log_frame.pack(fill="both", expand=True, padx=20, pady=10)

log_frame.columnconfigure(0, weight=1)
log_frame.columnconfigure(1, weight=1)
log_frame.rowconfigure(1, weight=1)

# Sending log (left)
tk.Label(log_frame, text="Sending Log:").grid(row=0, column=0, sticky="w")

sending_log = tk.Text(log_frame, wrap="word", font=("Arial", 10))
sending_log.grid(row=1, column=0, sticky="nsew", padx=(0, 10))

sending_scrollbar = tk.Scrollbar(log_frame, command=sending_log.yview)
sending_scrollbar.grid(row=1, column=0, sticky="nse", padx=(0, 10))
sending_log.config(yscrollcommand=sending_scrollbar.set)

# Receiving log (right)
tk.Label(log_frame, text="Receiving Log:").grid(row=0, column=1, sticky="w")

receiving_log = tk.Text(log_frame, wrap="word", font=("Arial", 10))
receiving_log.grid(row=1, column=1, sticky="nsew")

receiving_scrollbar = tk.Scrollbar(log_frame, command=receiving_log.yview)
receiving_scrollbar.grid(row=1, column=1, sticky="nse")
receiving_log.config(yscrollcommand=receiving_scrollbar.set)

# Define color tags for both logs
for widget in [sending_log, receiving_log]:
    widget.tag_config("red", foreground="red")
    widget.tag_config("green", foreground="green")
    widget.tag_config("blue", foreground="blue")
    widget.tag_config("black", foreground="black")
    widget.tag_config("white", foreground="white")
    widget.tag_config("yellow", foreground="yellow")
    widget.config(bg="black")  

# Initialize LiFiDevice
lifi_device = LiFiDevice(sys.argv[1])
lifi_device.on_log(write_log)
lifi_device.setup_devices()


ui_title = f"LiFi Device UI - {lifi_device.master_brick_uid}"
root.title(ui_title)

# Start the GUI
root.mainloop()

