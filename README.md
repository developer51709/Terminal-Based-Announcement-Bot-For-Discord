# Terminal-Based Announcement Bot for Discord

A professional, terminal-driven Discord bot for sending announcements with audit-friendly workflows and expressive feedback.

---

## ✨ Features

- 📢 **Send announcements** directly from the terminal
- 🖥️ **Interactive menu system** with colorized output
- 🔐 **Permission checks** before sending messages
- 📜 **List servers and channels** with interactive selection
- 📡 **Pick a channel directly** to send announcements (no need to copy IDs)
- 🔄 **Silent auto-reconnect** to recover from disconnects
- 🔌 **Graceful shutdown** with proper connector cleanup
- ⚙️ **Config file (`config.json`)** for storing bot token
- 🛠️ **Change token option** in the menu
- 🔄 **Update from GitHub** (`git pull`) directly from the menu

---

## 🚀 Future Improvements

- ⏰ Scheduled announcements (send at a specific time)
- 🔁 Recurring announcements (daily/weekly reminders)
- 🎨 Rich embeds for styled announcements
- 📝 Error logging and audit trails
- 📡 Multi-channel broadcast (send the same announcement to multiple channels)
- 🌐 Webhook integration for external triggers
- 🛡️ Permission diagnostics per channel

---

## 📦 Requirements

- Python 3.8+
- [discord.py](https://pypi.org/project/discord.py/)
- [colorama](https://pypi.org/project/colorama/)

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Setup

1. Clone the repo:
    ```bash
    git clone https://github.com/developer51709/Terminal-Based-Announcement-Bot-For-Discord.git
    cd Terminal-Based-Announcement-Bot-For-Discord

2. Create a bot in the [Discord Developer Portal](https://discord.com/developers/applications) and copy its token.

3. Run the bot:
   ```bash
   python main.py

4. On first run, you’ll be prompted for your bot token. It will be saved in config.json.

---

📜 Menu Options

1. List servers and channels → Browse servers, pick a channel, and send announcements  
2. Send announcement (by IDs) → Post a message to a specific channel manually  
3. Update from GitHub → Pull the latest changes  
4. Exit → Close the bot gracefully  
5. Change bot token → Update token stored in config.json

---

🛡️ Notes

- Make sure your bot has the Send Messages permission in the target channel.
- Invite your bot to servers using the OAuth2 URL from the Developer Portal.

---

👨‍💻 Author

Developed by [developer51709](https://github.com/developer51709)
