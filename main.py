import discord
import os
import subprocess
import asyncio
from colorama import Fore, Style, init

# Initialize colorama for cross-platform colored output
init(autoreset=True)

TOKEN = input(Fore.YELLOW + "Enter your Discord bot token: " + Style.RESET_ALL).strip()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def banner():
    print(Fore.CYAN + r"""
  ____  _                       _   
 |  _ \(_)___  ___ ___  _ __ __| |  
 | | | | / __|/ __/ _ \| '__/ _` |  
 | |_| | \__ \ (_| (_) | | | (_| |  
 |____/|_|___/\___\___/|_|  \__,_|  

   Discord Announcement Bot
   By: developer51709
    """ + Style.RESET_ALL)

def update():
    print(Fore.CYAN + "\nChecking for updates..." + Style.RESET_ALL)
    try:
        subprocess.run(["git", "pull"], check=True)
        print(Fore.GREEN + "✅ Update complete." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"❌ Update failed: {e}" + Style.RESET_ALL)

async def list_servers():
    print(Fore.CYAN + "\nConnected. Servers:" + Style.RESET_ALL)
    for i, guild in enumerate(client.guilds, start=1):
        print(Fore.YELLOW + f"{i}. " + Style.RESET_ALL + f"{guild.name} (ID: {guild.id})")

    while True:
        try:
            selection = int(await asyncio.to_thread(input, Fore.GREEN + "\nChoose a server number (0 to go back): " + Style.RESET_ALL))
            if selection == 0:
                break
            if 1 <= selection <= len(client.guilds):
                guild = client.guilds[selection - 1]
                print(Fore.CYAN + f"\nChannels in {guild.name}:" + Style.RESET_ALL)
                for channel in guild.channels:
                    if isinstance(channel, discord.TextChannel):
                        print(Fore.YELLOW + f"- {channel.name} (ID: {channel.id})" + Style.RESET_ALL)
                await asyncio.to_thread(input, Fore.GREEN + "\nPress Enter to return to server list..." + Style.RESET_ALL)
            else:
                print(Fore.RED + "Invalid selection." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Invalid input." + Style.RESET_ALL)

async def send_announcement():
    try:
        server_id = int(await asyncio.to_thread(input, Fore.YELLOW + "Enter Server ID: " + Style.RESET_ALL))
        channel_id = int(await asyncio.to_thread(input, Fore.YELLOW + "Enter Channel ID: " + Style.RESET_ALL))
        message = await asyncio.to_thread(input, Fore.YELLOW + "Enter announcement message: " + Style.RESET_ALL)

        guild = client.get_guild(server_id)
        if guild:
            channel = guild.get_channel(channel_id)
            if channel:
                perms = channel.permissions_for(guild.me)
                if not perms.send_messages:
                    print(Fore.RED + "❌ Bot lacks permission to send messages in this channel." + Style.RESET_ALL)
                    return

                print(Fore.CYAN + f"Sending to {guild.name} -> {channel.name}" + Style.RESET_ALL)
                await channel.send(f"📢 Announcement:\n{message}")
                print(Fore.GREEN + "✅ Announcement sent successfully." + Style.RESET_ALL)
            else:
                print(Fore.RED + "❌ Channel ID not found in that server." + Style.RESET_ALL)
        else:
            print(Fore.RED + "❌ Server ID not found." + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + "❌ Invalid input." + Style.RESET_ALL)

async def main_menu():
    while True:
        os.system("clear")
        banner()
        print(Fore.CYAN + "=== Discord Bot Menu ===" + Style.RESET_ALL)
        print(Fore.YELLOW + "1." + Style.RESET_ALL + " List servers and channels")
        print(Fore.YELLOW + "2." + Style.RESET_ALL + " Send announcement (by IDs)")
        print(Fore.YELLOW + "3." + Style.RESET_ALL + " Update from GitHub")
        print(Fore.YELLOW + "4." + Style.RESET_ALL + " Exit")

        choice = await asyncio.to_thread(input, Fore.GREEN + "Select an option: " + Style.RESET_ALL)

        if choice == "1":
            await list_servers()
        elif choice == "2":
            await send_announcement()
        elif choice == "3":
            update()
            await asyncio.to_thread(input, Fore.YELLOW + "\nPress Enter to return to menu..." + Style.RESET_ALL)
        elif choice == "4":
            print(Fore.CYAN + "Exiting…" + Style.RESET_ALL)
            await client.close()
            break
        else:
            print(Fore.RED + "❌ Invalid option. Try again." + Style.RESET_ALL)

@client.event
async def on_ready():
    print(Fore.GREEN + f"\n✅ Bot connected as {client.user}" + Style.RESET_ALL)
    await main_menu()

# --- Silent Auto-Reconnect Loop ---
async def run_bot():
    while True:
        try:
            await client.start(TOKEN)
        except (discord.ConnectionClosed, discord.HTTPException, Exception) as e:
            # Silent auto-reconnect: log minimal info and retry
            print(Fore.RED + f"⚠️ Connection lost: {e}. Reconnecting..." + Style.RESET_ALL)
            await asyncio.sleep(5)  # wait before retrying

# Entry point
asyncio.run(run_bot())
