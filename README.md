# Restaurant Billing System

A simple and intuitive restaurant billing system built with Python and Tkinter. This application provides a graphical user interface (GUI) for managing restaurant orders and generating bills with automatic cost calculations.

## Features

- **User-Friendly Interface**: Clean and intuitive GUI built with Tkinter
- **Multiple Item Categories**: 
  - Food Items (Pizza, Fries, Burger, Pasta, Momos)
  - Drinks (Coke, Coffee, Faluda, Tea, Milkshake)
  - Pastries (Oreo, Apple, Kitkat, Vanilla, Pineapple)
- **Visual Menu**: Icons/images for each menu item
- **Dynamic Pricing**: Automatic calculation of costs for selected items
- **Service Tax**: Automatic addition of service charge (₹50)
- **Cost Breakdown**: Displays individual category costs and total bill
- **Reset Functionality**: Quick reset to prepare for next customer
- **Input Validation**: Error handling for invalid selections

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- PIL/Pillow library for image handling

## Installation

1. Clone the repository or download the files:
```bash
git clone https://github.com/bugsNburgers/Simple-Restuarant-billing-system.git
cd "Resto final final"
```

2. Install required dependencies:
```bash
pip install pillow
```

3. Ensure all image files are in the same directory as the application:
   - pizza.png.png
   - fries.png.png
   - burger.png.png
   - pasta.png.png
   - momos.png.png
   - coke.png.png
   - coffee.png.png
   - faluda.png.png
   - tea.png.png
   - milkshake.png.png
   - oreo.png.png
   - apple.png.png
   - kitkat.png.png
   - vanilla.png.png
   - pineapple.png.png

## Usage

Run the application using:
```bash
python App.py
```

### How to Use:

1. **Select Items**: Check the boxes next to the items you want to order
2. **Enter Quantity**: Once checked, enter the quantity in the enabled entry field
3. **Calculate Total**: Click the "Total" button to calculate the bill
4. **View Breakdown**: See the cost breakdown by category and the final total
5. **Reset**: Click "Reset" to clear all selections and start a new order

## Menu & Pricing

### Food Items
- Pizza: ₹120
- Fries: ₹80
- Burger: ₹120
- Pasta: ₹150
- Momos: ₹100

### Drinks
- Coke: ₹50
- Coffee: ₹40
- Faluda: ₹80
- Tea: ₹40
- Milkshake: ₹100

### Pastries
- Oreo: ₹50
- Apple: ₹40
- Kitkat: ₹60
- Vanilla: ₹50
- Pineapple: ₹40

**Service Tax**: ₹50 (fixed)

## Project Structure

```
.
├── App.py           # Main application file
├── burge.py         # Burger module
├── coffe.py         # Coffee module
├── cok.py           # Coke module
├── falud.py         # Faluda module
├── frie.py          # Fries module
├── milkshak.py      # Milkshake module
├── momo.py          # Momos module
├── past.py          # Pasta module
├── pizz.py          # Pizza module
├── te.py            # Tea module
└── README.md        # This file
```

## Technical Details

- **GUI Framework**: Tkinter
- **Image Processing**: PIL (Pillow)
- **Architecture**: Modular design with separate files for each menu item
- **Window Size**: 1000x550 pixels
- **Color Scheme**: Black background with cyan text

## Limitations

- Fixed service tax of ₹50
- No database integration for order history
- No print receipt functionality
- No payment processing integration

## Future Enhancements

- Add receipt printing functionality
- Implement database for order tracking
- Add payment method options
- Include discount/coupon codes
- Generate daily/monthly sales reports
- Add more customization options for menu items

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License

This project is open source and available for educational purposes.

## Author

Repository maintained by: bugsNburgers

---
**Note** In the assignment we had to define functions separately in different files hence the files are messy , you can define everything in one single file :)

**Note**: This is a simple billing system designed for educational purposes and small-scale restaurant operations.
