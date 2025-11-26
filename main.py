import discord
import os
import subprocess

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
    """)

def update():
    print("\nChecking for updates...")
    try:
        subprocess.run(["git", "pull"], check=True)
        print("Update complete.")
    except Exception as e:
        print(f"Update failed: {e}")

def menu():
    while True:
        os.system("clear")
        banner()
        print("=== Discord Bot Menu ===")
        print("1. Start bot (background connection)")
        print("2. List servers and channels")
        print("3. Send announcement (by IDs)")
        print("4. Update from GitHub")
        print("5. Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            client.run(TOKEN)
            break
        elif choice == "2":
            temp_client = discord.Client(intents=intents)
            @temp_client.event
            async def on_ready():
                print("\nConnected. Servers:")
                for i, guild in enumerate(temp_client.guilds, start=1):
                    print(f"{i}. {guild.name} (ID: {guild.id})")
                try:
                    selection = int(input("\nChoose a server number to list its channels: ").strip())
                    if 1 <= selection <= len(temp_client.guilds):
                        guild = temp_client.guilds[selection - 1]
                        print(f"\nChannels in {guild.name}:")
                        for channel in guild.channels:
                            if isinstance(channel, discord.TextChannel):
                                print(f"- {channel.name} (ID: {channel.id})")
                    else:
                        print("Invalid selection.")
                except ValueError:
                    print("Invalid input.")
                await temp_client.close()
            temp_client.run(TOKEN)
        elif choice == "3":
            server_id = int(input("Enter Server ID: ").strip())
            channel_id = int(input("Enter Channel ID: ").strip())
            message = input("Enter announcement message: ").strip()
            temp_client = discord.Client(intents=intents)
            @temp_client.event
            async def on_ready():
                guild = temp_client.get_guild(server_id)
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
                await temp_client.close()
            temp_client.run(TOKEN)
        elif choice == "4":
            update()
            input("\nPress Enter to return to menu...")
        elif choice == "5":
            print("Exiting…")
            break
        else:
            print("Invalid option. Try again.")

menu()
