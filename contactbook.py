contacts = {}
phone_numbers = set()

Num_Of_Contacts = int(input("Enter the number of contacts you want to add: "))

for i in range(Num_Of_Contacts):
    name = input(f"\nEnter the name of person {i+1}: ")
    phone = input("Enter the number: ")

    if phone in phone_numbers:
        print("his number already exists! Contact not added.")
        continue  

    contacts[name] = phone
    phone_numbers.add(phone)

print("\n Contact Book ")
for cname, cphone in contacts.items():
    print(f"{cname} : {cphone}")

Saved_Name = input("\nEnter a name to search the contact number: ")

if Saved_Name in contacts:
    print(f"Phone number: {contacts[Saved_Name]}")
else:
    print("Contact not found!")
