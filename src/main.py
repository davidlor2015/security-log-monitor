from parser import parse_auth_log

LOG_PATH = "data/auth.log"

def main():
    results = parse_auth_log(LOG_PATH)

    print("\n=== Failed SSH Logins ===")
    for (user, ip), count in results["failed_logins"].most_common(5):
        print(f"{user} from {ip}: {count}")

    print("\n=== Accepted SSH Logins ===")
    for (user, ip), count in results["accepted_logins"].most_common(5):
        print(f"{user} from {ip}: {count}")

    print("\n=== sudo Usage ===")
    for user, count in results["sudo_usage"].most_common(5):
        print(f"{user}: {count}")

if __name__ == "__main__":
    main()