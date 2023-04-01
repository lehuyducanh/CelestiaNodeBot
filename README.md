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

## Usage

1. Add the bot to your Telegram account
2. Send the Node ID (starting with "12D3" and 52 characters long) to the bot
3. The bot will display the node information

## Example

Input:

\`\`\`
12D3KooWMfJj8P5px6grkmsnFsaNX1M9E4iKh1cJYfQ3koXad8oQ
\`\`\`

Output:

\`\`\`
💻 Celestia Node Information 💻

🔗 Node ID: 12D3KooWMfJj8P5px6grkmsnFsaNX1M9E4iKh1cJYfQ3koXad8oQ

🌍 Node type: Celestia-Light

🟢 Uptime value: 98

📊 Network height: 145001

🚀 Total Sync Headers: 144994

🛠 Last Restart: 01/04/2023 03:01:12

🔔 Stay on top of things! 🚀
\`\`\`
