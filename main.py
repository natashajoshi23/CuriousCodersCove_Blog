import os
import datetime

class Journal:
    def __init__(self, journal_file="journal.txt"):
        self.journal_file = journal_file
        self.entries = []

    def load_entries(self):
        if os.path.exists(self.journal_file):
            with open(self.journal_file, "r") as file:
                self.entries = file.readlines()

    def save_entries(self):
        with open(self.journal_file, "w") as file:
            file.writelines(self.entries)

    def add_entry(self, entry):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.entries.append(f"{timestamp}\n{entry}\n\n")

    def view_entries(self):
        for entry in self.entries:
            print(entry)

def main():
    journal = Journal()
    journal.load_entries()

    while True:
        print("\n1. Add Entry")
        print("2. View Entries")
        print("3. Exit")

        choice = input("Select an option (1/2/3): ")

        if choice == "1":
            entry_text = input("Enter your journal entry: ")
            journal.add_entry(entry_text)
            print("Entry added successfully!")

        elif choice == "2":
            print("\n--- Journal Entries ---")
            journal.view_entries()

        elif choice == "3":
            print("Exiting the journaling app.")
            journal.save_entries()
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
