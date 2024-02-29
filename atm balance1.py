def main():
    denominations = []
    notes = []
    for i in range(4):
        denomination = int(input(f"Enter the {i+1}st Denomination: "))
        num_notes = int(input(f"Enter the {i+1}st Denomination number of notes: "))
        denominations.append(denomination)
        notes.append(num_notes)

    total_balance = sum(denomination * note for denomination, note in zip(denominations, notes))
    print("Total Available Balance in ATM:", total_balance)

if __name__ == "__main__":
    main()
