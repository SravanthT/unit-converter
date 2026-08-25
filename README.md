# unit-converter
# Multi-Category Unit Converter

A lightweight, type-safe web application built with Python and Flask that allows users to instantly convert between various units of measurement for length, weight, and temperature. The project features dynamic server-side processing, persistent dropdown menus, and a unified presentation layer.

## 🚀 Features

- **Length Conversion:** Millimeter, centimeter, meter, kilometer, inch, foot, yard, and mile.
- **Weight Conversion:** Milligram, gram, kilogram, tonne, ounce, pound, and stone.
- **Temperature Conversion:** Celsius, Fahrenheit, and Kelvin.
- **Persistent Form States:** Keeps your input values and chosen units selected after form submission.
- **DRY Architecture:** Uses Jinja2 layout inheritance (`base.html`) for a consistent look and feel without code duplication.
- **Pylance Type Safe:** Fully type-annotated code avoiding static analyzer complaints.

## 🛠️ Tech Stack

- **Backend:** Python 3.x, Flask
- **Frontend:** HTML5, CSS3, Jinja2 Template Engine
- **Development Tooling:** Type hinting with `typing`

## 📦 Project Structure

```text
unit-converter/
├── app.py              # Main Flask application logic & conversions
├── README.md           # Documentation
└── templates/          # Frontend templates folder
    ├── base.html       # Shared master layout & styles
    ├── length.html     # Length conversion form
    ├── weight.html     # Weight conversion form
    └── temp.html       # Temperature conversion form
```

## ⚙️ Installation & Setup

Follow these steps to run the application locally on your machine:

1. **Clone or navigate to your project directory:**
   ```bash
   cd unit-converter
   ```

2. **Install Flask:**
   Make sure you have Flask installed in your active environment.
   ```bash
   pip install Flask
   ```

3. **Run the Application:**
   Execute the primary Python script to kick off the local development server.
   ```bash
   python app.py
   ```

4. **Access the App:**
   Open your preferred web browser and navigate to:
   `http://127.0.0`

## 🖥️ Usage

1. Select the metric type you want to convert from the top navigation bar (📏 Length, ⚖️ Weight, or 🌡️ Temperature).
2. Input the numerical value you want to modify.
3. Select your **Convert From** and **Convert To** units from the dropdown menus.
4. Click **Convert Value** to get your result instantly.

## 💾 Git Workflow Reminders

To push any updates or modifications you make to this project up to your remote repository, run the following sequence in your terminal:

```bash
git add .
git commit -m "Add update description here"
git push origin main
```
