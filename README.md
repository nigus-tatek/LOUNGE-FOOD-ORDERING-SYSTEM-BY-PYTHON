T# DBU Lounge Food Ordering System

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Screenshots](#screenshots)
7. [File Structure](#file-structure)
8. [Team Members](#team-members)

## Introduction

Welcome to the **DBU Lounge Food Ordering System**! This is a comprehensive system designed to manage food orders efficiently at the DBU lounge. The system allows users to add, search, display, and remove food items, as well as manage food orders. It's built using Python and Tkinter for a user-friendly graphical interface.

## Features

- **Add Food Items:** Add new food items to the menu with details such as name, price, ID, category, and quantity.
- **Display Menu:** View the complete list of food items available in the menu.
- **Search Food:** Search for a food item by its ID.
- **Remove Food:** Remove food items based on their category or ID.
- **Order Food:** Place an order for a food item using its ID.
- **Cancel Order:** Cancel an existing order.
- **Order Status:** Check the status of a food order.
- **Data Persistence:** Menu data is saved and loaded from a JSON file for persistence.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Tkinter library (usually included with Python)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/DBU-Lounge-Food-Ordering-System.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd DBU-Lounge-Food-Ordering-System
   ```

3. **Run the application:**

   ```bash
   python app.py
   ```

## Usage

1. **Launch the application:**

   ```bash
   python app.py
   ```

2. **Add Food Items:**
   - Enter the food name, price, ID, category, and quantity.
   - Click the "ADD FOOD" button to add the item to the menu.

3. **Display Menu:**
   - Click the "DISPLAY MENU" button to view all food items.

4. **Search Food:**
   - Click the "SEARCH FOOD (by_id)" button.
   - Enter the food ID and click "SEARCH".

5. **Remove Food:**
   - Click the "REMOVE FOOD (by category)" or "REMOVE FOOD (by id)" button.
   - Enter the category or ID and click "REMOVE" or "DELETE".

6. **Order Food:**
   - Click the "ORDER FOOD (ID)" button.
   - Enter the food ID and click "ORDER".

7. **Cancel Order:**
   - Click the "CANCEL ORDER" button.
   - Enter the food ID and click "CANCEL".

8. **Check Order Status:**
   - Click the "ORDER STATUS" button.
   - Enter the food ID and click "CHECK STATUS".

## Screenshots

Here are some screenshots of the application:

### Main Interface
![Main Interface](screenshots/main_interface.png)

### Add Food
![Add Food](screenshots/add_food.png)

### Display Menu
![Display Menu](screenshots/display_menu.png)

### Search Food
![Search Food](screenshots/search_food.png)

### Order Food
![Order Food](screenshots/order_food.png)

## File Structure

The project directory is structured as follows:

```
DBU-Lounge-Food-Ordering-System/
│
├── app.py                    # Main application file
├── menu.json                 # JSON file to store menu data
├── README.md                 # Readme file
├── screenshots/              # Directory for screenshots
│   ├── main_interface.png
│   ├── add_food.png
│   ├── display_menu.png
│   └── ...
└── requirements.txt          # List of required packages (if any)
```

## Team Members

- **Nigus Tatek** (ID: dbu1501416)
- **Hailemeskel** (ID: dbu)
- **Halid Faruk** (ID: dbu)

We hope you find this system useful and easy to use! If you have any questions or suggestions, feel free to contact us.

---

Thank you for using the DBU Lounge Food Ordering System!
