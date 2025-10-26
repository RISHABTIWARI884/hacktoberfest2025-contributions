import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def ascii_clock():
    while True:
        clear()
        current_time = time.strftime("%H:%M:%S", time.localtime())
        print("╔════════════╗")
        print(f"║  {current_time}  ║")
        print("╚════════════╝")
        time.sleep(1)

if __name__ == "__main__":
    try:
        ascii_clock()
    except KeyboardInterrupt:
        print("\nClock stopped.")
