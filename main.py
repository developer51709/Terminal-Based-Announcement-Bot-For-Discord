import discord
import os
import subprocess
import asyncio

TOKEN = input("Enter your Discord bot token: ").strip()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def banner():
    print(r"""
  ____  _                       _   
 |  _ \(_)___  ___ ___  _ __ __| |  
 | | | | / __|/ __/ _ \| '__/ _` |  
 | |_| | \__ \ (_| (_) | | | (_| |  
 |____/|_|___/\___\___/|_|  \__,_|  

   Discord Announcement Bot
   By: developer51709
   """)

def update():
    print("\nChecking for updates...")
    try:
        subprocess.run(["git", "pull"], check=True)
        print("Update complete.")
    except Exception as e:
        print(f"Update failed: {e}")

async def list_servers():
    print("\nConnected. Servers:")
    for i, guild in enumerate(client.guilds, start=1):
        print(f"{i}. {guild.name} (ID: {guild.id})")

    while True:
        try:
            selection = int(await asyncio.to_thread(input, "\nChoose a server number (0 to go back): "))
            if selection == 0:
                break
            if 1 <= selection <= len(client.guilds):
                guild = client.guilds[selection - 1]
                print(f"\nChannels in {guild.name}:")
                for channel in guild.channels:
                    if isinstance(channel, discord.TextChannel):
                        print(f"- {channel.name} (ID: {channel.id})")
                await asyncio.to_thread(input, "\nPress Enter to return to server list...")
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid input.")

async def send_announcement():
    try:
        server_id = int(await asyncio.to_thread(input, "Enter Server ID: "))
        channel_id = int(await asyncio.to_thread(input, "Enter Channel ID: "))
        message = await asyncio.to_thread(input, "Enter announcement message: ")

        guild = client.get_guild(server_id)
        if guild:
            channel = guild.get_channel(channel_id)
            if channel:
                print(f"Sending to {guild.name} -> {channel.name}")
                await channel.send(f"📢 Announcement:\n{message}")
                print("Announcement sent successfully.")
            else:
                print("Channel ID not found in that server.")
        else:
            print("Server ID not found.")
    except ValueError:
        print("Invalid input.")

async def main_menu():
    while True:
        os.system("clear")
        banner()
        print("=== Discord Bot Menu ===")
        print("1. List servers and channels")
        print("2. Send announcement (by IDs)")
        print("3. Update from GitHub")
        print("4. Exit")

        choice = await asyncio.to_thread(input, "Select an option: ")

        if choice == "1":
            await list_servers()
        elif choice == "2":
            await send_announcement()
        elif choice == "3":
            update()
            await asyncio.to_thread(input, "\nPress Enter to return to menu...")
        elif choice == "4":
            print("Exiting…")
            await client.close()
            break
        else:
            print("Invalid option. Try again.")

@client.event
async def on_ready():
    print(f"\nBot connected as {client.user}")
    await main_menu()

asyncio.run(client.start(TOKEN))
