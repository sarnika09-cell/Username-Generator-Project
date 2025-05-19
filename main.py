def generate_username():
    # Ask user for their nickname and real name
    nickname = input("Enter your nickname: ").strip()
    real_name = input("Enter your real name: ").strip()

    # Combine names with underscore
    username = f"{nickname}_{real_name}"

    # Display suggested username
    print(f"Your username could be: {username}")

if __name__ == "__main__":
    generate_username()
