coded_message = input("Enter coded message: ")
secret_message = input("Enter secret message: ")

if secret_message and secret_message in coded_message:
    print("Secret message found!")
else:
    print("Secret message not found!")