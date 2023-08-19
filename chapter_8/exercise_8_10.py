text_messages = ['test 1', 'test 2', 'test 3', 'test 4', 'test 5']
sent_messages = []

def send_messages(text_messages2):
    for message in text_messages2:
        print(message)
    
    while text_messages2:
        current_message = text_messages2.pop()
        sent_messages.append(current_message)

    print(sent_messages)

send_messages(text_messages[:])
print(text_messages)