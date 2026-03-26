from datetime import datetime

LOG_FILE = "activity_log.txt"

def log_action(action):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as file:
        file.write(f"[{timestamp}] {action} \n")


def main():
    print("----- Action Logger -----")

    while True:
        action = input("Enter action (or type 'exit' to quit): ")

        if action.lower() == "exit":
            print("Exiting logger.....")
            break

        log_action(action)
        print("✅ Action logged.")

if __name__ == "__main__":
    main()