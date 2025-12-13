# ConvertoBot

ConvertoBot is a Telegram bot designed to help you easily convert **units**, **number bases**, and **dates**.
Built with **Python** and **pyTelegramBotAPI**, it provides a fast and user-friendly way to perform various conversions directly inside Telegram.

---
## Telegram Bot

You can try the bot directly on Telegram:

👉 **@transmuterpro_bot**  
https://t.me/transmuterpro_bot

---

## Features

* **Unit Conversion**
  Convert different units by sending formatted input (length, weight, temperature, etc.).

* **Base Conversion**
  Convert numbers between different bases (binary, decimal, hexadecimal, etc.).

* **Date Conversion**
  Convert dates between:

  * Gregorian
  * Persian (Jalali)
  * Islamic (Hijri)

* **Daily Message**
  Sends a daily date message to all registered users.

---

## Technologies Used

* Python 3.9+
* pyTelegramBotAPI
* python-dotenv
* schedule

---

## Requirements

* Python **3.9 or higher**
* Telegram Bot Token from **@BotFather**

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ConvertoBot.git
cd ConvertoBot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

* **Windows**

```bash
venv\Scripts\activate
```

* **Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install pyTelegramBotAPI
pip install python-dotenv
pip install schedule
```

---

## Environment Variables

Create a `.env` file by copying `.env.example`:

```bash
cp .env.example .env
```

Fill in the required values:

```env
API_TOKEN=your_telegram_bot_token
```

---

## Usage

Run the bot using:

```bash
python main.py
```

The bot will start polling Telegram and also run the scheduled daily task.

---

## Bot Menu

Main menu buttons:

* **Unit** – Unit conversion mode
* **Base** – Base conversion mode
* **Date** – Date conversion menu
* **About** – Developer information

---

## Commands

* `/start` – Register user and show main menu

---

## Project Structure

```text
ConvertoBot/
│── main.py
│── database.py
│── text.py
│── transmuter.py
│── transmuter_base.py
│── transmuter_date.py
│── .env.example
│── README.md
```

---

## Author

**Alireza Tashani**
Python Developer & Programmer
📧 Email: [alirezatd80@gmail.com](mailto:alirezatd80@gmail.com)

---

## License

This project is licensed under the MIT License.
