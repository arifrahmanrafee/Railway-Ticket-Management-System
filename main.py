import tkinter as tk
from tkinter import ttk, messagebox

from Train_route import Train_route
from Strategy import Ticket as StrategyTicket, EconomyClass, ACClass, FirstClass
from Decorator import BasicTicket, VIPService, ExtraBaggage, MealOption
from Notifier import NotificationFactory, Factory_passanger_staff
from Admin import Concrete_Admin, Concrete_passanger, Concrete_staff

# In-memory data store
passenger_profiles = []
staff_profiles = []
ticket_bookings = []
train_routes = []


class UnifiedRailwayApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🚄 Unified Railway Management System")
        self.geometry("1000x700")
        self.configure(bg="#dfe6e9")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both")

        self.create_passenger_tab()
        self.create_staff_tab()
        self.create_ticket_booking_tab()
        self.create_ticket_pricing_tab()
        self.create_ticket_addons_tab()
        self.create_train_route_tab()
        self.create_admin_notification_tab()

    def create_passenger_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Passenger Dashboard")

        tk.Label(frame, text="👤 Passenger Dashboard", font=("Segoe UI", 16, "bold"), foreground="#0984e3").pack(pady=20)
        tk.Button(frame, text="Create Profile", command=self.create_passenger_profile).pack(pady=5)
        tk.Button(frame, text="View All Passengers", command=self.view_all_passengers).pack(pady=5)
        tk.Button(frame, text="View Ticket Bookings", command=self.view_ticket_bookings).pack(pady=5)

    def create_passenger_profile(self):
        win = tk.Toplevel(self)
        win.title("New Passenger Profile")

        name_var = tk.StringVar()
        age_var = tk.StringVar()
        ticket_count_var = tk.StringVar()
        email_var = tk.StringVar()
        phone_var = tk.StringVar()

        tk.Label(win, text="Name").pack()
        tk.Entry(win, textvariable=name_var).pack()
        tk.Label(win, text="Age").pack()
        # tk.Entry(win, textvariable=age_var).pack()
        # tk.Label(win, text="Number of Tickets").pack()
        tk.Entry(win, textvariable=ticket_count_var).pack()
        tk.Label(win, text="Email").pack()
        tk.Entry(win, textvariable=email_var).pack()
        tk.Label(win, text="Phone").pack()
        tk.Entry(win, textvariable=phone_var).pack()

        def save():
            profile = {
                "name": name_var.get(),
                "age": age_var.get(),
                "ticket_count": ticket_count_var.get(),
                "email": email_var.get(),
                "phone": phone_var.get()
            }
            passenger_profiles.append(profile)
            messagebox.showinfo("Success", "Passenger profile saved.")
            win.destroy()

        tk.Button(win, text="Save", command=save).pack(pady=10)

    def view_all_passengers(self):
        win = tk.Toplevel(self)
        win.title("Passenger List")

        if not ticket_bookings:
            tk.Label(win, text="No ticket bookings found.").pack(pady=10)
            return

        seen = set()

        for booking in ticket_bookings:
            unique_key = (booking['name'], booking['phone'])

            if unique_key not in seen:
                seen.add(unique_key)
                header = f"👤 {booking['name']} (Phone: {booking['phone']})"
                tk.Label(win, text=header, font=("Arial", 11, "bold"), fg="#2d3436").pack(anchor="w", padx=10, pady=2)

                # Get all bookings for this person
                related_bookings = [b for b in ticket_bookings if
                                    b['name'] == booking['name'] and b['phone'] == booking['phone']]

                for b in related_bookings:
                    booking_info = (
                        f"  ➤ Train: {b['train_name']}, "
                        f"From: {b['source']} → {b['destination']}, "
                        f"Class: {b['class']}, Add-ons: {b['addons']}, "
                        f"Price: {b['price']} BDT"
                    )
                    tk.Label(win, text=booking_info, font=("Arial", 9), fg="#636e72").pack(anchor="w", padx=30)

    def view_ticket_bookings(self):
        win = tk.Toplevel(self)
        win.title("Ticket Booking Details")

        if not ticket_bookings:
            tk.Label(win, text="No ticket bookings found.").pack(pady=10)
        else:
            for ticket in ticket_bookings:
                tk.Label(win, text=f"Name: {ticket['name']}, Age: {ticket['age']}, Source: {ticket['source']}, "
                                   f"Destination: {ticket['destination']}, Tickets: {ticket['ticket_count']}, "
                                   f"Class: {ticket['class']}, Add-ons: {ticket['addons']}, "
                                   f"Phone: {ticket['phone']}, Email: {ticket['email']}, "
                                   f"Price: {ticket['price']} BDT, Train Name: {ticket['train_name']}").pack(pady=5)

    def create_staff_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Staff Dashboard")

        tk.Label(frame, text="🧑‍💼 Staff Dashboard", font=("Segoe UI", 16, "bold"), foreground="#6c5ce7").pack(pady=20)
        tk.Button(frame, text="Create Staff Profile", command=self.create_staff_profile).pack(pady=5)
        tk.Button(frame, text="View All Staff", command=self.view_all_staff).pack(pady=5)

    def create_staff_profile(self):
        win = tk.Toplevel(self)
        win.title("New Staff Profile")

        name_var = tk.StringVar()
        id_var = tk.StringVar()
        contact_var = tk.StringVar()

        tk.Label(win, text="Name").pack()
        tk.Entry(win, textvariable=name_var).pack()
        tk.Label(win, text="ID").pack()
        tk.Entry(win, textvariable=id_var).pack()
        tk.Label(win, text="Contact").pack()
        tk.Entry(win, textvariable=contact_var).pack()

        def save():
            profile = {
                "name": name_var.get(),
                "id": id_var.get(),
                "contact": contact_var.get()
            }
            staff_profiles.append(profile)
            messagebox.showinfo("Success", "Staff profile saved.")
            win.destroy()

        tk.Button(win, text="Save", command=save).pack(pady=10)

    def view_all_staff(self):
        win = tk.Toplevel(self)
        win.title("Staff List")
        for s in staff_profiles:
            tk.Label(win, text=f"{s['name']} (ID: {s['id']}, Contact: {s['contact']})").pack()

    def create_ticket_booking_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Ticket Booking")

        fields = {
            "Name": tk.StringVar(),
            "Age": tk.StringVar(),
            "Source": tk.StringVar(),
            "Destination": tk.StringVar(),
            "Number of Tickets": tk.StringVar(),
            "Phone": tk.StringVar(),
            "Email": tk.StringVar(),
            "Class": tk.StringVar()
        }

        tk.Label(frame, text="Book Ticket", font=("Segoe UI", 14, "bold"), fg="#2d3436").pack(pady=10)
        for label, var in fields.items():
            tk.Label(frame, text=f"{label}:").pack()
            if label == "Class":
                ttk.Combobox(frame, textvariable=var, values=["Economy", "AC", "First"]).pack()
            else:
                tk.Entry(frame, textvariable=var).pack()

        vip_var = tk.BooleanVar()
        baggage_var = tk.BooleanVar()
        meal_var = tk.BooleanVar()

        tk.Checkbutton(frame, text="VIP Service (+50 BDT)", variable=vip_var).pack(anchor="w")
        tk.Checkbutton(frame, text="Extra Baggage (+20 BDT)", variable=baggage_var).pack(anchor="w")
        tk.Checkbutton(frame, text="Meal (+15 BDT)", variable=meal_var).pack(anchor="w")

        def book():
            ticket = BasicTicket()
            addons = []
            if vip_var.get():
                ticket = VIPService(ticket)
                addons.append("VIP Service")
            if baggage_var.get():
                ticket = ExtraBaggage(ticket)
                addons.append("Extra Baggage")
            if meal_var.get():
                ticket = MealOption(ticket)
                addons.append("Meal")

            train_info = Train_route(fields["Source"].get(), fields["Destination"].get())
            train_name = train_info.desired_train[0].train_name if train_info.desired_train else "N/A"

            ticket_info = {
                "name": fields["Name"].get(),
                "age": fields["Age"].get(),
                "source": fields["Source"].get(),
                "destination": fields["Destination"].get(),
                "ticket_count": fields["Number of Tickets"].get(),
                "class": fields["Class"].get(),
                "phone": fields["Phone"].get(),
                "email": fields["Email"].get(),
                "addons": ", ".join(addons) if addons else "None",
                "price": ticket.get_price(),
                "train_name": train_name
            }
            ticket_bookings.append(ticket_info)
            messagebox.showinfo("Booked", "Ticket booked successfully.")

        tk.Button(frame, text="Book Ticket", command=book).pack(pady=10)

    def create_ticket_pricing_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Ticket Pricing")

        tk.Label(frame, text="Select Class & Enter Distance (km):", font=("Arial", 12)).pack(pady=5)

        self.class_var = tk.StringVar()
        ttk.Combobox(frame, textvariable=self.class_var, values=["Economy", "AC", "First"]).pack(pady=5)

        self.distance_entry = tk.Entry(frame)
        self.distance_entry.pack(pady=5)

        result_label = tk.Label(frame, text="")
        result_label.pack(pady=5)

        def calculate():
            cls = self.class_var.get()
            try:
                dist = float(self.distance_entry.get())
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid distance")
                return

            if cls == "Economy":
                strategy = EconomyClass()
            elif cls == "AC":
                strategy = ACClass()
            else:
                strategy = FirstClass()

            ticket = StrategyTicket(strategy)
            result_label.config(text=f"Total Price: {ticket.get_price(dist)} BDT")

        tk.Button(frame, text="Calculate Price", command=calculate).pack(pady=5)

    def create_ticket_addons_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Ticket Add-ons")

        tk.Label(frame, text="Select Add-ons:", font=("Arial", 12)).pack(pady=5)

        vip_var = tk.BooleanVar()
        baggage_var = tk.BooleanVar()
        meal_var = tk.BooleanVar()

        tk.Checkbutton(frame, text="VIP Service (+50 BDT)", variable=vip_var).pack(anchor="w")
        tk.Checkbutton(frame, text="Extra Baggage (+20 BDT)", variable=baggage_var).pack(anchor="w")
        tk.Checkbutton(frame, text="Meal (+15 BDT)", variable=meal_var).pack(anchor="w")

        result_label = tk.Label(frame, text="")
        result_label.pack(pady=5)

        def calculate():
            ticket = BasicTicket()
            if vip_var.get():
                ticket = VIPService(ticket)
            if baggage_var.get():
                ticket = ExtraBaggage(ticket)
            if meal_var.get():
                ticket = MealOption(ticket)
            result_label.config(text=f"Description: {ticket.get_description()}\nTotal Price: {ticket.get_price()} BDT")

        tk.Button(frame, text="Generate Receipt", command=calculate).pack(pady=5)

    def create_train_route_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Train Routes")

        tk.Label(frame, text="Enter Source & Destination:", font=("Arial", 12)).pack(pady=5)

        src_entry = tk.Entry(frame)
        dest_entry = tk.Entry(frame)
        src_entry.pack(pady=2)
        dest_entry.pack(pady=2)

        result_box = tk.Text(frame, height=10)
        result_box.pack(pady=5)

        def search():
            result_box.delete(1.0, tk.END)
            src = src_entry.get()
            dest = dest_entry.get()
            route = Train_route(src, dest)

            if not route.desired_train:
                result_box.insert(tk.END, "No trains available for this route.")
            else:
                for train in route.desired_train:
                    result_box.insert(tk.END, f"Train Name: {train.train_name}\n")
                    result_box.insert(tk.END, f"Source: {train.source}\n")
                    result_box.insert(tk.END, f"Destination: {train.destination}\n")
                    result_box.insert(tk.END, f"Time: {train.time}\n")
                    result_box.insert(tk.END, f"Number of Passengers: {train.num_passengers}\n")
                    result_box.insert(tk.END, "-" * 40 + "\n")

        tk.Button(frame, text="Search Trains", command=search).pack(pady=5)

    def create_admin_notification_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Admin Notification")

        tk.Label(frame, text="Admin Notification Panel", font=("Arial", 14, "bold")).pack(pady=10)

        text_entry = tk.Entry(frame, width=50)
        text_entry.pack(pady=5)

        output_box = tk.Text(frame, height=10)
        output_box.pack(pady=5)

        admin = Concrete_Admin()
        admin.add_passanger(Concrete_passanger())
        admin.add_passanger(Concrete_staff())

        def send():
            msg = text_entry.get()
            output_box.insert(tk.END, f"Sending notification: {msg}\n")
            admin.notify(msg)
            output_box.insert(tk.END, "Notification sent.\n")

        tk.Button(frame, text="Send Notification", command=send).pack(pady=5)


if __name__ == "__main__":
    app = UnifiedRailwayApp()
    app.mainloop()
