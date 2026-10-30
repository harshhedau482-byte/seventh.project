# 🛠️ Multi-Utility Toolkit

A feature-rich, menu-driven console application written in Python. This project demonstrates modular programming by integrating Python's robust standard libraries with custom modules and packages to handle everyday utility tasks seamlessly.

---

## 🚀 Features

The toolkit is organized into an intuitive interactive console menu with 6 core capability groups:

### 1. 🕒 Datetime and Time Operations
* **Display Current Date & Time:** View the current timestamp in standard and user-friendly long formats.
* **Date Difference Calculator:** Calculate the exact number of days between two user-provided dates (`YYYY-MM-DD`).
* **Custom Date Formatter:** Format dates into ISO, Long, Short, Day of Week, and Month-Day-Year formats.
* **Stopwatch:** A lightweight interactive stopwatch measuring elapsed time in seconds.
* **Countdown Timer:** A visual countdown timer with live updates in the console.

### 2. 📐 Mathematical Operations & Unit Conversions
* **Factorial Calculation:** Compute factorials using custom math utilities.
* **Compound Interest Solver:** Calculate total compound interest and net interest earned.
* **Trigonometric Calculations:** Compute Sine, Cosine, and Tangent for any angle in degrees.
* **Geometric Area Calculator:** Compute areas for circles, rectangles, triangles, and squares.
* **Unit Converters:** Convert temperature (°C/°F), distance (Kilometers/Miles), and weight (Kilograms/Pounds).

### 3. 🎲 Random Data Generation
* **Random Number & List Generator:** Generate random integers within custom bounds or create lists of random numbers.
* **Secure Password Generator:** Generate strong custom-length passwords containing letters, numbers, and special symbols.
* **OTP Generator:** Generate 6-digit One-Time Passwords instantly.
* **Dataset Random Sampling:** Draw random samples from a mock dataset of names.

### 4. 🔑 Unique Identifier (UUID) Generation
* **Single UUID Generation:** Generate standard UUIDv4 identifiers along with version inspection.
* **Purpose-Specific UUIDs:** Simultaneously generate structured IDs for Files, Records, and Sessions.

### 5. 📁 File Operations (Custom Package)
* Perform safe file management tasks through a dedicated custom module (`toolkit_package.file_operations`):
  * Create new files
  * Write and append data
  * Read file contents
  * Delete files with confirmation prompts

### 6. 🔍 Dynamic Module Exploration (`dir()`)
* Inspect any built-in or custom module dynamically at runtime using Python's built-in `dir()` function and attribute counting.

---

## 📁 Project Structure

```text
multi-utility-toolkit/
│
├── main.py                  # Main entry point and menu controller
├── toolkit_package/         # Custom package directory
│   ├── __init__.py          # Package initializer
│   ├── file_operations.py   # Custom file handling logic
│   └── math_utilities.py    # Custom mathematical & conversion functions
│
└── README.md                # Project documentation
