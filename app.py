import os
import json
import requests
from datetime import datetime
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import dotenv

dotenv.load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
dispatcher = updater.dispatcher

def get_node_data(nodeID: str):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,ru-RU;q=0.6,ru;q=0.5",
        "sec-ch-ua": '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "Referer": "https://tiascan.com/",
        "Referrer-Policy": "strict-origin-when-cross-origin",
    }
    response = requests.get(f"https://leaderboard.celestia.tools/api/v1/nodes/{nodeID}", headers=headers)
    return response.json()

def handle_message(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    nodeID = update.message.text

    if "12D3" in nodeID and len(nodeID) == 52:
        try:
            data = get_node_data(nodeID)
            nodeId = data["node_id"]
            uptime = int(data["uptime"])
            type_ = data["node_type_str"]
            total_synced_headers = data["total_synced_headers"]
            node_runtime_counter_in_seconds = data["node_runtime_counter_in_seconds"]
            network_height = data["network_height"]
            last_restart = datetime.strptime(data["last_restart_time"], "%Y-%m-%dT%H:%M:%SZ")
            icon = "🟢" if uptime >= 80 else "🟡" if uptime >= 40 else "🔴"

#             message = f"""🚀 Node ID: {nodeId}

# {icon} Uptime: {uptime}

# 💡 Type: {type_}

# 💎 Total Sync Headers: {total_synced_headers}

# ⏰ Node runtime counter in seconds: {node_runtime_counter_in_seconds}

# 📈 Network height: {network_height}

# 🕑 Last Restart: {last_restart.strftime("%d/%m/%Y %H:%M:%S")}"""
            message = f"""💻 Celestia Node Information 💻

🔗 Node ID: {nodeId}

🌍 Node type: {type_}

{icon} Uptime value: {uptime}

📊 Network height: {network_height}

🚀 Total Sync Headers: {total_synced_headers}

🛠 Last Restart: {last_restart.strftime("%d/%m/%Y %H:%M:%S")}

🔔 Stay on top of things! 🚀"""
            context.bot.send_message(chat_id=chat_id, text=message)
        except Exception as error:
            print(error)
            context.bot.send_message(chat_id=chat_id, text="Sorry, there was an error retrieving data for that wallet.")


message_handler = MessageHandler(Filters.text & ~Filters.command, handle_message)
dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()
