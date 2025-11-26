# Terminal-Based Announcement Bot for Discord

A simple yet professional **terminal-driven Discord bot** for sending announcements.  
Built by [developer51709](https://github.com/developer51709), this bot emphasizes **clarity, auditability, and ease of use** — no web UI required.

---

## ✨ Features
- 📢 Send announcements directly from the terminal
- 🖥️ Interactive menu system with colorized output
- 🔐 Permission checks before sending messages
- 📜 List servers and channels with IDs for easy selection
- 🔄 Update the bot directly from GitHub (`git pull`)
- 🛡️ Error handling with clear feedback

---

## 📦 Requirements
- Python 3.8+
- [discord.py](https://pypi.org/project/discord.py/) (`pip install discord.py`)
- [colorama](https://pypi.org/project/colorama/) (`pip install colorama`)

---

## 🚀 Setup & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/developer51709/Terminal-Based-Announcement-Bot-For-Discord.git
   cd Terminal-Based-Announcement-Bot-For-Discord

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   
3. **Run the bot**
   ```bash
   python bot.py

4. **Enter your bot token when prompted.**

---

## 🖥️ Menu Options
- **1. List servers and channels** → Browse your servers and see channel IDs
- **2. Send announcement (by IDs)** → Post a message to a specific channel
- **3. Update from GitHub** → Pull the latest changes
- **4. Exit** → Close the bot

---

## 🔐 Permissions
Make sure your bot has:
- View Channels
- Send Messages

If permissions are missing, the bot will warn you before attempting to send.

---

## 📜 Future Improvements
- Scheduled announcements (send at a specific time)
- Rich embeds for styled announcements
- Config file for default server/channel IDs

---

## ⚠️ Notes
- Keep your **bot token private** — never commit it to GitHub.
- This bot is intended for **personal and team use**.  
- Contributions and improvements are welcome!

---

## 👨‍💻 Author
**developer51709**
[GitHub Profile](https://github.com/developer51709)

---
