📈 CLI Portfolio Tracker

A robust Command Line Interface (CLI) application built with Python to track, manage, and analyze investment portfolios. This tool allows users to add assets, remove holdings, and view real-time performance summaries using a JSON-based storage system.

🚀 Features

Portfolio Management: Add, remove, and update asset holdings easily.

Performance Tracking: Calculate total portfolio value, profit/loss, and asset allocation.

Persistent Storage: Automatically saves data to JSON, ensuring your portfolio persists between sessions.

Modular Architecture: Clean separation of concerns between UI, logic, and data storage.

Error Handling: Robust validation for user inputs (e.g., preventing negative quantities).

📂 Project Structure

The project follows a modular design pattern:

cli-portfolio-tracker/
├── main.py              # Entry point: Handles User Interface and CLI loop
├── portfolio.py         # Business Logic: Calculations and data processing
├── storage.py           # Data Persistence: Handles reading/writing JSON files
├── market_data.json     # Mock/Real data source for current asset prices
└── user_portfolio.json  # Database: Stores user's specific holdings


🛠️ Installation & Setup

Prerequisites: Ensure you have Python 3.x installed.

Clone the repository:

git clone [https://github.com/aaryamanchanda/Portfolio-Tracker.git](https://github.com/aaryamanchanda/Portfolio-Tracker.git)
cd Portfolio-Tracker


Run the Application:

python main.py


📖 Usage Guide

Once the application is running, follow the on-screen menu prompts:

Add Asset: Enter the ticker symbol (e.g., AAPL), buy price, and quantity.

View Portfolio: Displays a table of your holdings, current value, and P/L.

Remove Asset: Sell or remove a specific asset from your list.

Exit: Saves any final changes and closes the program.

🧠 Implementation Approach

This project uses a modular architecture to ensure maintainability and scalability:

Controller (main.py): Acts as the bridge between the user and the system. It handles the input loop and routes commands to specific modules, keeping the UI logic distinct from calculation logic.

Core Logic (portfolio.py): Contains the "brains" of the operation. It handles the math (calculating allocation %, total equity) and processes raw data into readable formats.

Data Layer (storage.py): Abstracts file I/O. The main application doesn't need to know how data is saved, only that it is safe. We use JSON for storage because it maps perfectly to Python dictionaries and is lightweight.

💡 Key Learnings

State Management: Synchronizing in-memory data with disk storage is critical. I implemented a "save-on-write" strategy (saving immediately after adding/removing assets) rather than "save-on-exit" to prevent data loss during crashes.

Robust Error Handling: The importance of wrapping user inputs in try/except blocks became evident quickly. Handling non-numeric inputs for prices or quantities prevents the CLI from crashing unexpectedly.

Separation of Concerns: Initially, much of the logic was in main.py. Refactoring code into storage.py and portfolio.py made the codebase significantly cleaner and easier to debug.

🔮 Future Improvements

API Integration: Replace market_data.json with a live API (e.g., Yahoo Finance or CoinGecko) for real-time pricing.

Visualization: Integrate matplotlib to generate pie charts of portfolio allocation.

Transaction History: Create a log file to track buy/sell history over time.

Created by Aarya Manchanda