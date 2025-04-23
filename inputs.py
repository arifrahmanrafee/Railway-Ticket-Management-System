import tkinter as tk
from tkinter import ttk

class InputForm:
    def __init__(self, root):
        self.root = root
        self.root.title("10 Input Boxes")
        self.root.geometry("500x400")
        
        self.create_inputs()
        self.create_button()
    
    def create_inputs(self):
        # Create main container
        main_frame = ttk.Frame(self.root)
        main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
        
        # Create labels and entries
        self.entries = []
        labels = [
            "Name:", "age","No of seats:", "Email:", "phone:", 
            "From", "To:", "Time1:", "Time2:", "service:"
        ]
        
        for i in range(10):
            # Create frame for each input row
            row_frame = ttk.Frame(main_frame)
            row_frame.pack(fill=tk.X, pady=5)
            
            # Label
            label = ttk.Label(row_frame, text=labels[i], width=8)
            label.pack(side=tk.LEFT, padx=(0, 10))
            
            # Entry box
            entry = ttk.Entry(row_frame)
            entry.pack(fill=tk.X, expand=True)
            self.entries.append(entry)
    
    def create_button(self):
        # Submit button
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=20)
        
        submit_btn = ttk.Button(
            button_frame,
            text="Submit",
            command=self.get_values
        )
        submit_btn.pack()
    
    def get_values(self)->list:
        entry=[]
        values = [entry.get() for entry in self.entries]
        print("Entered values:")
        for i, value in enumerate(values, 1):
            entry.append(values);
            
        return entry;
if __name__ == "__main__":
    root = tk.Tk()
    app = InputForm(root)
    root.mainloop()