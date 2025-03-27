import tkinter as tk
import sys
import threading
from lifi import LiFiDevice

class LiFiUI(tk.Tk):
    def __init__(self, lifi_device):
        super().__init__()
        self.lifi_device = lifi_device
        self.title(f"LiFi Device UI - {lifi_device.master_brick_uid}")
        self.geometry("900x400")
        
        # Label for input field
        label = tk.Label(self, text="Text Message:")
        label.pack(anchor="w", padx=20, pady=(10, 5))
        
        # Frame for input and button
        input_frame = tk.Frame(self)
        input_frame.pack(anchor="w", padx=20, pady=(0, 10))
        
        # Input field
        self.entry = tk.Entry(input_frame, width=30)
        self.entry.pack(side=tk.LEFT)
        
        # Button that sends text when clicked
        button = tk.Button(input_frame, text="Submit", command=self.send_text)
        button.pack(side=tk.LEFT, padx=5)
        
        # Log section using grid for equal-size columns
        log_frame = tk.Frame(self)
        log_frame.pack(fill="both", expand=True, padx=20, pady=10)
        log_frame.columnconfigure(0, weight=1)
        log_frame.columnconfigure(1, weight=1)
        log_frame.rowconfigure(1, weight=1)
        
        # Sending log (left)
        tk.Label(log_frame, text="Sending Log:").grid(row=0, column=0, sticky="w")
        self.sending_log = tk.Text(log_frame, wrap="word", font=("Arial", 10))
        self.sending_log.grid(row=1, column=0, sticky="nsew", padx=(0, 10))
        sending_scrollbar = tk.Scrollbar(log_frame, command=self.sending_log.yview)
        sending_scrollbar.grid(row=1, column=0, sticky="nse", padx=(0, 10))
        self.sending_log.config(yscrollcommand=sending_scrollbar.set)
        
        # Receiving log (right)
        tk.Label(log_frame, text="Receiving Log:").grid(row=0, column=1, sticky="w")
        self.receiving_log = tk.Text(log_frame, wrap="word", font=("Arial", 10))
        self.receiving_log.grid(row=1, column=1, sticky="nsew")
        receiving_scrollbar = tk.Scrollbar(log_frame, command=self.receiving_log.yview)
        receiving_scrollbar.grid(row=1, column=1, sticky="nse")
        self.receiving_log.config(yscrollcommand=receiving_scrollbar.set)
        
        # Define color tags for both logs
        for widget in [self.sending_log, self.receiving_log]:
            widget.tag_config("red", foreground="red")
            widget.tag_config("green", foreground="green")
            widget.tag_config("blue", foreground="blue")
            widget.tag_config("black", foreground="black")
            widget.tag_config("white", foreground="white")
            widget.tag_config("yellow", foreground="yellow")
            widget.config(bg="black")
        
        # Register the UI's log callback with the LiFi device
        self.lifi_device.register_callback(self.write_send_log, callback_type=LiFiDevice.SEND_LOG)
        self.lifi_device.register_callback(self.write_receive_log, callback_type=LiFiDevice.RECEIVE_LOG)
        
        # Start the sensor in a separate thread
        threading.Thread(target=self.lifi_device.start, daemon=True).start()

    def send_text(self):
        """Called when the Submit button is pressed.
        It retrieves the text from the entry, clears the entry, and calls send_text on the LiFi device
        in a separate thread."""
        user_input = self.entry.get()
        self.entry.delete(0, tk.END)
        threading.Thread(target=self.lifi_device.send_text, args=(user_input,), daemon=True).start()

    def write_log(self, widget, message, color="black", end="\n"):
        if color not in ("red", "green", "blue", "black", "white", "yellow"):
            color = "black"

        def log_to_ui():
            widget.insert(tk.END, f"{message}{end}", color)
            widget.see(tk.END)
            widget.update_idletasks()

        # Schedule the UI update safely on the main thread.
        self.after(0, log_to_ui)
 
    def write_send_log(self, message, color="black", end="\n"):
        self.write_log(self.sending_log, message, color, end)

    def write_receive_log(self, message, color="black", end="\n"):
        self.write_log(self.receiving_log, message, color, end)
        
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python lifi_ui.py <master_brick_uid>")
        sys.exit(1)

    # Initialize LiFiDevice with the provided master_brick_uid.
    lifi_device = LiFiDevice(sys.argv[1])
        
    # Create the UI, passing in the LiFi device instance.
    app = LiFiUI(lifi_device)
    app.mainloop()
