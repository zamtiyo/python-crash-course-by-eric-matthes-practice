#146
message_list = ["Nigga","Ngentod","Bangsat"]
sent_messages = []

def show_message(messages):
    for message in messages:
        print(f"The message is {message}")

def send_message():
    for message in message_list:
        sent_messages.append(message)
        print(f"Sent: {message}")
    print(f"All sent messages: {sent_messages}")

# Call the functions
send_message()
show_message(message_list)
