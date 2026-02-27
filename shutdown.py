def shutdown():
    user_input = input("Do you want to shutdown? (Yes/No): ")

    if user_input.lower() == "yes":
        print("Shutting down...")
    elif user_input.lower() == "no":
        print("Abort shutdown.")
    else:
        print("Sorry.")

shutdown()