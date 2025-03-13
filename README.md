# 📐Scientific Calculator with Dark/Light Mode

A responsive web-based scientific calculator built with Flask, JavaScript, HTML, and CSS. This calculator features both standard and scientific operations, calculation history tracking, and a dark/light theme toggle.

## 🌟 Features

- **Standard Calculations**: Addition, subtraction, multiplication, division
- **Scientific Functions**: Square root, factorial, trigonometry (sin, cos, tan), logarithms (log, ln)
- **Memory Functions**: Store and recall values
- **Calculation History**: View and reuse previous calculations
- **Dark/Light Theme**: Toggle between light and dark mode with preference saved between sessions
- **Keyboard Support**: Use your keyboard for input

## 🗃️ File Structure

```
scientific-calculator/
├── app.py                # Flask backend application
├── static/
│   ├── css/
│   │   └── styles.css    # Styling including dark/light mode
│   └── js/
│       └── calculator.js # Frontend functionality
└── templates/
    └── calculator.html   # Main HTML template
```

### 🔢 Basic Operations
- Click the number buttons (0-9) to input numbers
- Use the operation buttons (+, -, ×, ÷) for basic arithmetic
- Press "=" to calculate the result
- Press "AC" to clear the display
- Press "⌫" to delete the last character

### 🧰 Scientific Functions
- Square Root (√): Enter a number and click "√"
- Power (^): Enter base, click "^", enter exponent, click "="
- Factorial (x!): Enter a number and click "x!"
- Trigonometric Functions: Enter an angle in degrees and click "sin", "cos", or "tan"
- Logarithmic Functions: Enter a number and click "log" (base 10) or "ln" (natural)
- Constants: Click "π" or "e" to input these mathematical constants

### 💾 Memory Functions
- MS: Store the current displayed value in memory
- MR: Recall the stored value from memory

### 🌗 Theme Toggle
- Click the "🌓 Theme" button in the menu bar to switch between light and dark mode
- Your preference is saved and will be remembered when you return

### 📅 History
- Click the "History" button to view your calculation history
- Click on any history item to use that result in a new calculation
- Use "Clear History" to remove all history items

### 🚀 Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python, Flask

### 🌍 Deployed on Render
The project is live on **Render**:
➡️ https://scientific-calculator-with-gui.onrender.com

### 🤝 Contributions
Contributions are welcome! Please feel free to submit a Pull Request.
