import tkinter as tk
from tkinter import ttk

class StylishRailwayApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🚄 Railway Management System")
        self.geometry("900x550")
        self.configure(bg="#dfe6e9")
        self.resizable(True, True)

        self.sidebar_bg = "#2d3436"
        self.button_bg = "#636e72"
        self.highlight_bg = "#00cec9"
        self.main_bg = "#f5f6fa"

        self.create_sidebar()
        self.create_main_area()

    def create_sidebar(self):
        sidebar = tk.Frame(self, bg=self.sidebar_bg, width=220)
        sidebar.pack(side="left", fill="y")

        tk.Label(sidebar, text="🚄 Railway System", bg=self.sidebar_bg, fg="white",
                 font=("Segoe UI", 16, "bold")).pack(pady=30)

        # Buttons with styling
        self.make_nav_button(sidebar, "👤 Passenger", self.show_passenger_section)
        self.make_nav_button(sidebar, "🧑‍💼 Staff", self.show_staff_section)
        self.make_nav_button(sidebar, "❌ Exit", self.quit, bg="#d63031", hover_bg="#e17055")

    def make_nav_button(self, parent, text, command, bg=None, hover_bg=None):
        bg = bg or self.button_bg
        hover_bg = hover_bg or self.highlight_bg

        btn = tk.Label(parent, text=text, bg=bg, fg="white", font=("Segoe UI", 12), width=20, pady=10, cursor="hand2")
        btn.pack(pady=10)

        def on_enter(e): btn.config(bg=hover_bg)
        def on_leave(e): btn.config(bg=bg)
        btn.bind("<Button-1>", lambda e: command())
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

    def create_main_area(self):
        self.main_frame = tk.Frame(self, bg=self.main_bg)
        self.main_frame.pack(side="right", fill="both", expand=True)
        self.show_welcome()

    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_welcome(self):
        self.clear_main_frame()
        tk.Label(self.main_frame, text="Welcome to Railway Management System", font=("Segoe UI", 18, "bold"),
                 bg=self.main_bg, fg="#2d3436").pack(pady=40)

    def show_passenger_section(self):
        self.clear_main_frame()
        tk.Label(self.main_frame, text="👤 Passenger Dashboard", font=("Segoe UI", 16, "bold"),
                 bg=self.main_bg, fg="#0984e3").pack(pady=20)
##--------------------------------------------------------------
        self.styled_button("Passenger Profile", self.fake)
        self.styled_button("Ticket Booking", self.fake_action)
        self.styled_button("View Tickets", self.fake_action)

    def show_staff_section(self):
        self.clear_main_frame()
        tk.Label(self.main_frame, text="🧑‍💼 Staff Dashboard", font=("Segoe UI", 16, "bold"),
                 bg=self.main_bg, fg="#6c5ce7").pack(pady=20)

        self.styled_button("Route Management", self.fake_action)
        self.styled_button("Train Schedule", self.fake_action)
        self.styled_button("Staff Info", self.fake_action)

    def styled_button(self, text, command):
        btn = tk.Button(self.main_frame, text=text, command=command,
                        font=("Segoe UI", 12), bg="#74b9ff", fg="white", bd=0,
                        activebackground="#0984e3", activeforeground="white",
                        padx=15, pady=10)
        btn.pack(pady=10)

    def fake_action(self):
        self.clear_main_frame()
        self.styled_button("provides", self.fake)

    def fake(self):
        label = tk.Label(tk.Tk(), 
                textvariable=tk.StringVar(), 
                anchor=tk.CENTER,       
                bg="lightblue",      
                height=3,              
                width=30,              
                bd=3,                  
                font=("Arial", 16, "bold"), 
                cursor="hand2",   
                fg="red",             
                padx=15,               
                pady=15,                
                justify=tk.CENTER,    
                relief=tk.RAISED,     
                underline=0,           
                wraplength=250         
                )
        
# Run the app
if __name__ == "__main__":
    StylishRailwayApp().mainloop()
