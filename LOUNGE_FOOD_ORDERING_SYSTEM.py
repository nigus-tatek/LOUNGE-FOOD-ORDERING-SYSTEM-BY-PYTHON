# group members           id number
#  1, nigus tatek           dbu1501416
#  2,hailemeskel          dbu
#  3, halid faruk         dbu


from tkinter import *
from tkinter import messagebox
import json

class LoungeFoodOrderingSystem:
    def __init__(self, root):
        self.root = root
        root.title("DBU Lounge Food Ordering System")
        root.configure(width=1500, height=600, bg='lightblue', bd="30", relief="sunken")

        self.menu = []  # List to hold existing menu items
        self.orders = []  # List to hold orders
        self.load_menu()  # Load existing menu data from file
        self.create_widgets()

    def create_widgets(self):
        self.label0 = Label(self.root, text="DBU LOUNGE FOOD ORDERING SYSTEM", bg="purple", bd="7", relief="sunken", fg="white", font=("Times", 30))

        # Entry fields and labels
        self.label1 = Label(self.root, text="ENTER FOOD NAME", bd="7", bg="yellow", relief="solid", fg="black", font=("Times", 12), width=25)
        self.entry1 = Entry(self.root, bd="5", relief="sunken", font=("Times", 12))

        self.label2 = Label(self.root, text="ENTER PRICE", bd="7", relief="solid", height="1", bg="yellow", fg="black", font=("Times", 12), width=25)
        self.entry2 = Entry(self.root, bd="5", relief="sunken", font=("Times", 12))

        self.label3 = Label(self.root, text="ENTER FOOD ID", bd="7", relief="solid", bg="yellow", fg="black", font=("Times", 12), width=25)
        self.entry3 = Entry(self.root, bd="5", relief="sunken", font=("Times", 12))

        self.label4 = Label(self.root, text="ENTER CATEGORY", bd="7", relief="solid", bg="yellow", fg="black", font=("Times", 12), width=25)
        self.entry4 = Entry(self.root, bd="5", relief="sunken", font=("Times", 12))

        self.label5 = Label(self.root, text="ENTER QUANTITY", bd="7", bg="yellow", relief="solid", fg="black", font=("Times", 12), width=25)
        self.entry5 = Entry(self.root, bd="5", relief="sunken", font=("Times", 12))

        # Buttons
        self.button1 = Button(self.root, text="ADD FOOD", bg="pink", relief="solid", fg="black", width=30, font=("Times", 12), command=self.add_food)
        self.button2 = Button(self.root, text="DISPLAY MENU", bg="pink", relief="solid", fg="black", width=30, font=("Times", 12), command=self.display_menu)
        self.button3 = Button(self.root, text="SEARCH FOOD (by_id)", bg="pink", relief="solid", fg="black", width=30, font=("Times", 12), command=self.open_search_window)
        self.button4 = Button(self.root, text="REMOVE FOOD (by category)", bg="pink", relief="solid", fg="black", width=30, font=("Times", 12), command=self.open_remove_window)
        self.button5 = Button(self.root, text="REMOVE FOOD (by id)", bg="pink", relief="solid", fg="black", width=30, font=("Times", 12), command=self.open_delete_window)
        self.button6 = Button(self.root, text="DISPLAY ALL FOODS", bg="pink", relief="solid", fg="black", width=30, font=("Times", 12), command=self.display_all_foods)
        self.button7 = Button(self.root, text="ORDER FOOD (ID)", bg="pink", relief="solid", fg="black", width=30, font=("Times", 12), command=self.open_order_window)
        self.button8 = Button(self.root, text="CANCEL ORDER", bg="pink", relief="solid", fg="black", width=30, font=("Times", 12), command=self.open_cancel_window)
        self.button9 = Button(self.root, text="ORDER STATUS", bg="pink", relief="solid", fg="black", width=30, font=("Times", 12), command=self.open_status_window)
        self.button10 = Button(self.root, text="EXIT", bg="pink", relief="solid", fg="black", width=30, font=("Times", 12), command=self.root.quit)

        # Grid placement
        self.label0.grid(columnspan=10, padx=10, pady=10)

        self.label1.grid(row=1, column=0, sticky=W, padx=10, pady=10)
        self.entry1.grid(row=1, column=1, padx=10, pady=10)
        self.button1.grid(row=1, column=2, padx=100, pady=10)

        self.label2.grid(row=2, column=0, sticky=W, padx=10, pady=10)
        self.entry2.grid(row=2, column=1, padx=10, pady=10)
        self.button2.grid(row=2, column=2, padx=10, pady=10)

        self.label3.grid(row=3, column=0, sticky=W, padx=10, pady=10)
        self.entry3.grid(row=3, column=1, padx=10, pady=10)
        self.button3.grid(row=3, column=2, padx=10, pady=10)

        self.label4.grid(row=4, column=0, sticky=W, padx=10, pady=10)
        self.entry4.grid(row=4, column=1, padx=10, pady=10)
        self.button4.grid(row=4, column=2, padx=10, pady=10)

        self.label5.grid(row=5, column=0, sticky=W, padx=10, pady=10)
        self.entry5.grid(row=5, column=1, padx=10, pady=10)

        self.button6.grid(row=1, column=3, padx=10, pady=10)

        self.button7.grid(row=2, column=3, padx=10, pady=10)
        self.button8.grid(row=3, column=3, padx=10, pady=10)
        self.button9.grid(row=4, column=3, padx=10, pady=10)
        self.button10.grid(row=6, columnspan=10, padx=10, pady=10)

        self.button5.grid(row=5, column=3, padx=10, pady=10)  # Add the delete button to the grid

    def add_food(self):
        name = self.entry1.get()
        price = float(self.entry2.get())
        food_id = int(self.entry3.get())
        category = self.entry4.get()
        quantity = int(self.entry5.get())

        # Check if food ID already exists
        if any(food['id'] == food_id for food in self.menu):
            messagebox.showerror("Error", "Food ID already exists")
            return

        food = {"name": name, "price": price, "id": food_id, "category": category, "quantity": quantity, "ordered": False}
        self.menu.append(food)
        self.save_menu()  # Save menu data to file after adding food
        messagebox.showinfo("Success", "Food added to menu")
        self.clear_entries()

    def display_menu(self):
        if self.menu:
            foods = "\n".join(f"Name: {food['name']}, Price: {food['price']}, ID: {food['id']}, Category: {food['category']}, Quantity: {food['quantity']}, Ordered: {food['ordered']}" for food in self.menu)
            messagebox.showinfo("Menu Items", foods)
        else:
            messagebox.showinfo("Menu Items", "No foods exist in the menu")

    def display_all_foods(self):
        self.display_menu()

    def open_search_window(self):
        self.destroy_current_window()
        search_window = Toplevel(self.root)
        search_window.title("Search Food")
        search_window.configure(width=400, height=200, bg='green')
        self.current_window = search_window

        label = Label(search_window, text="ENTER FOOD ID", bg="purple", relief="ridge", fg="white", font=("Times", 12), width=25)
        entry = Entry(search_window, font=("Times", 12))
        button = Button(search_window, text="SEARCH", bg="light blue", fg="black", width=30, font=("Times", 12), command=lambda: self.search_food(entry.get()))

        label.pack(padx=10, pady=10)
        entry.pack(padx=10, pady=10)
        button.pack(padx=10, pady=10)

    def open_remove_window(self):
        self.destroy_current_window()
        remove_window = Toplevel(self.root)
        remove_window.title("Remove Food")
        remove_window.configure(width=400, height=200, bg='red')
        self.current_window = remove_window

        label = Label(remove_window, text="ENTER FOOD CATEGORY", bg="purple", relief="ridge", fg="white", font=("Times", 12), width=25)
        entry = Entry(remove_window, font=("Times", 12))
        button = Button(remove_window, text="REMOVE", bg="light blue", fg="black", width=30, font=("Times", 12), command=lambda: self.remove_food(entry.get()))

        label.pack(padx=10, pady=10)
        entry.pack(padx=10, pady=10)
        button.pack(padx=10, pady=10)

    def open_delete_window(self):
        self.destroy_current_window()
        delete_window = Toplevel(self.root)
        delete_window.title("Delete Food")
        delete_window.configure(width=400, height=200, bg='red')
        self.current_window = delete_window

        label = Label(delete_window, text="ENTER FOOD ID", bg="purple", relief="ridge", fg="white", font=("Times", 12), width=25)
        entry = Entry(delete_window, font=("Times", 12))
        button = Button(delete_window, text="DELETE", bg="light blue", fg="black", width=30, font=("Times", 12), command=lambda: self.delete_food(entry.get()))

        label.pack(padx=10, pady=10)
        entry.pack(padx=10, pady=10)
        button.pack(padx=10, pady=10)

    def open_order_window(self):
        self.destroy_current_window()
        order_window = Toplevel(self.root)
        order_window.title("Order Food")
        order_window.configure(width=400, height=200, bg='orange')
        self.current_window = order_window

        label = Label(order_window, text="ENTER FOOD ID TO ORDER", bg="purple", relief="ridge", fg="white", font=("Times", 12), width=25)
        entry = Entry(order_window, font=("Times", 12))
        button = Button(order_window, text="ORDER", bg="light blue", fg="black", width=30, font=("Times", 12), command=lambda: self.order_food(entry.get()))

        label.pack(padx=10, pady=10)
        entry.pack(padx=10, pady=10)
        button.pack(padx=10, pady=10)

    def open_cancel_window(self):
        self.destroy_current_window()
        cancel_window = Toplevel(self.root)
        cancel_window.title("Cancel Order")
        cancel_window.configure(width=400, height=200, bg='orange')
        self.current_window = cancel_window

        label = Label(cancel_window, text="ENTER FOOD ID TO CANCEL", bg="purple", relief="ridge", fg="white", font=("Times", 12), width=25)
        entry = Entry(cancel_window, font=("Times", 12))
        button = Button(cancel_window, text="CANCEL", bg="light blue", fg="black", width=30, font=("Times", 12), command=lambda: self.cancel_order(entry.get()))

        label.pack(padx=10, pady=10)
        entry.pack(padx=10, pady=10)
        button.pack(padx=10, pady=10)

    def open_status_window(self):
        self.destroy_current_window()
        status_window = Toplevel(self.root)
        status_window.title("Order Status")
        status_window.configure(width=400, height=200, bg='green')
        self.current_window = status_window

        label = Label(status_window, text="ENTER FOOD ID", bg="purple", relief="ridge", fg="white", font=("Times", 12), width=25)
        entry = Entry(status_window, font=("Times", 12))
        button = Button(status_window, text="CHECK STATUS", bg="light blue", fg="black", width=30, font=("Times", 12), command=lambda: self.check_order_status(entry.get()))

        label.pack(padx=10, pady=10)
        entry.pack(padx=10, pady=10)
        button.pack(padx=10, pady=10)

    def destroy_current_window(self):
        if hasattr(self, 'current_window') and self.current_window is not None:
            self.current_window.destroy()
            self.current_window = None

    def save_menu(self):
        with open('menu.json', 'w') as file:
            json.dump(self.menu, file)

    def load_menu(self):
        try:
            with open('menu.json', 'r') as file:
                self.menu = json.load(file)
        except FileNotFoundError:
            self.menu = []

    def search_food(self, food_id):
        food_id = int(food_id)
        food = next((food for food in self.menu if food['id'] == food_id), None)
        if food:
            messagebox.showinfo("Food Found", f"Name: {food['name']}, Price: {food['price']}, ID: {food['id']}, Category: {food['category']}, Quantity: {food['quantity']}, Ordered: {food['ordered']}")
        else:
            messagebox.showerror("Error", "Food not found")

    def remove_food(self, category):
        initial_length = len(self.menu)
        self.menu = [food for food in self.menu if food['category'] != category]
        self.save_menu()
        if len(self.menu) < initial_length:
            messagebox.showinfo("Success", "Food(s) removed")
        else:
            messagebox.showinfo("Info", "No food found in the given category")

    def delete_food(self, food_id):
        food_id = int(food_id)
        self.menu = [food for food in self.menu if food['id'] != food_id]
        self.save_menu()
        messagebox.showinfo("Success", "Food deleted from menu")

    def order_food(self, food_id):
        food_id = int(food_id)
        for food in self.menu:
            if food['id'] == food_id:
                food['ordered'] = True
                self.orders.append(food)
                self.save_menu()
                messagebox.showinfo("Success", "Food ordered")
                return
        messagebox.showerror("Error", "Food not found")

    def cancel_order(self, food_id):
        food_id = int(food_id)
        for food in self.orders:
            if food['id'] == food_id:
                food['ordered'] = False
                self.orders = [order for order in self.orders if order['id'] != food_id]
                self.save_menu()
                messagebox.showinfo("Success", "Order cancelled")
                return
        messagebox.showerror("Error", "Order not found")

    def check_order_status(self, food_id):
        food_id = int(food_id)
        food = next((food for food in self.menu if food['id'] == food_id), None)
        if food:
            status = "Ordered" if food['ordered'] else "Not Ordered"
            messagebox.showinfo("Order Status", f"Food ID: {food_id}, Status: {status}")
        else:
            messagebox.showerror("Error", "Food not found")

    def clear_entries(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry5.delete(0, END)

if __name__ == "__main__":
    root = Tk()
    app = LoungeFoodOrderingSystem(root)
    root.mainloop()
