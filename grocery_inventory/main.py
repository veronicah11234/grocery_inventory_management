from cli import menu, print_all_products, print_all_suppliers, get_item_details_from_cli, get_category_details_from_cli, exit_program

class Welcome:
    print("Welcome to our shop kindly request the order of your choice?")

    def main():
        while True:
            menu()
            choice = input("> ")
            if choice == "0":
                exit()
            elif choice == "1":
                print_all_products()
            elif choice == "2":
                print_all_suppliers()
            elif choice == "3":
                get_category_details_from_cli()
            elif choice == "4":
                get_item_details_from_cli()
            else:
                print("Invalid choice")
                
    main()