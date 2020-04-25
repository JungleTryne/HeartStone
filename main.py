from botCore.message_handler import MessageHandler


def main():
    server_answer = MessageHandler.handle_request('/pick_card two', '4623746327')[0]
    print(server_answer.user.card_set_selected)
    print(server_answer.message)
    server_answer = MessageHandler.handle_request('/pick_card two', '4623746327')[0]
    print(server_answer.user.card_set_selected)
    print(server_answer.message)
    server_answer = MessageHandler.handle_request('/remove_card two', '4623746327')[0]
    print(server_answer.user.card_set_selected)
    print(server_answer.message)

    print(server_answer.user.fraction)
    server_answer = MessageHandler.handle_request('/change_fraction two', '4623746327')[0]
    print(server_answer.user.card_set_selected)
    print(server_answer.message)
    print(server_answer.user.fraction)


if __name__ == '__main__':
    main()
