from layers import physical, data_link, network, transport, session, ppt, app

def menu():
    print("=== OSI Layer Troubleshooter ===")
    print("1. Physical Layer")
    print("2. Data Link Layer")
    print("3. Network Layer")
    print("4. Transport Layer")
    print("5. Session Layer")
    print("6. Presentation Layer")
    print("7. Application Layer")
    print("0. Exit")

while True:
    menu()
    choice = input("Select layer to test: ")
    if choice == "1":
        physical.check_physical()
    elif choice == "2":
        data_link.check_data_link()
    elif choice == "3":
        network.check_network()
    elif choice == "4":
        transport.check_transport_layer()
    elif choice == "5":
        session.check_session()
    elif choice == "6":
        ppt.check_presentation()
    elif choice == "7":
        app.check_application()
    elif choice == "0":
        break
    else:
        print("Invalid choice")
