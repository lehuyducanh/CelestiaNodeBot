# Celestia Node Info Telegram Bot

A simple Python-based Telegram bot that allows users to monitor the status of Celestia nodes. It fetches node data and displays it in a clear and concise manner.

## Features

- Get node status by providing the Node ID
- Displays the following information:
  - Node ID
  - Node type
  - Uptime value (with emoji indicator)
  - Network height
  - Total Sync Headers
  - Last Restart timestamp

## Prerequisites

- Python 3.7 or higher
- `python-telegram-bot` library
- `python-dotenv` library

## Setup

1. Clone the repository or copy the provided code into a new Python file (e.g., `celestia_bot.py`).
2. Install the required libraries by running: `pip install python-telegram-bot python-dotenv`
3. Create a `.env` file in the same directory as the Python script and add your Telegram bot token: TELEGRAM_BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN

Replace `YOUR_TELEGRAM_BOT_TOKEN` with the actual token provided by the BotFather on Telegram.

## Usage

1. Run the Python script with the following command: `python celestia_bot.py`
2. Add the bot to your Telegram group, example group with bot: https://t.me/CelestiaTrackingwithBrian
3. Send the Node ID (starting with "12D3" and 52 characters long) to the bot
4. The bot will display the node information

## Example

Input:

<pre>
12D3KooWMfJj8P5px6grkmsnFsaNX1M9E4iKh1cJYfQ3koXad8oQ
</pre>



Output:

<pre>
💻 Celestia Node Information 💻

🔗 Node ID: 12D3KooWMfJj8P5px6grkmsnFsaNX1M9E4iKh1cJYfQ3koXad8oQ

🌍 Node type: Celestia-Light

🟢 Uptime value: 98

📊 Network height: 145001

🚀 Total Sync Headers: 144994

🛠 Last Restart: 01/04/2023 03:01:12

🔔 Stay on top of things! 🚀
</pre>
