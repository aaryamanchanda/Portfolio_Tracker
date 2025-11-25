# Project Statement

## Problem Statement
Managing a stock portfolio often requires complex financial software or manual, error-prone spreadsheet entries. Beginner investors and students need a simplified, distraction-free environment to track their holdings, understand their average buy prices, and calculate potential profits or losses without the complexity of professional trading terminals.

## Scope of the Project
The **CLI Portfolio Tracker** is a lightweight, command-line-based application designed to manage stock investments locally.
* **Interface:** Text-based User Interface (TUI/CLI).
* **Data Source:** Simulates market data via a local JSON file (`market_data.json`), allowing for offline usage and controlled testing environments.
* **Persistence:** All user transaction data is saved automatically to a local file (`user_portfolio.json`), ensuring data remains available between sessions.
* **Logic:** Handles weighted average cost calculations (Dollar Cost Averaging) automatically upon purchasing.

## Target Users
* **College Students:** For learning the basics of stock portfolio management and coding logic.
* **Beginner Investors:** To practice buying and selling logic without risking real capital (Paper Trading).
* **Minimalists:** Users who prefer terminal-based tools over GUI applications.

## High-Level Features
1.  **Portfolio Overview:** Display a tabular view of all current holdings, including quantity, current market price, and total value.
2.  **Buy Mechanism:** Allows users to "buy" stocks. The system automatically calculates the new weighted average price if the stock is already owned.
3.  **Sell Mechanism:** Allows users to liquidate assets. The system verifies ownership quantity and calculates the Realized Profit/Loss (P/L) for the transaction.
4.  **Data Persistence:** Automatically loads portfolio data on startup and saves updates after every transaction.
5.  **Input Validation:** Prevents errors such as selling more shares than owned or entering invalid ticker symbols.