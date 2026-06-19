num = 0

def number_of_times_being_looked_up():
    global num
    num += 1
    print(num)
    return num
def commands(command):
    if command == "/reset":
        print("resetting all data, count number, and history of looked up data")
        global num
        num = 0
        print(num)
        return num


def command_list():
    print('"/reset" to reset all data, count number, and history of looked up data')


def check_question(answer):
    number_of_times_being_looked_up()
    if answer == "random_data":
        look_up_data(answer)
        return
    elif answer == "/help":
        command_list()
        return
    elif answer.startswith("/"):
        commands(answer)
        return


def look_up_data(answer):
    print("def look_up_data was executed")
    
while False:
    class ask_question:
        def __init__(self, question):
            self.question = question

        def ask(self):
            return input(self.question)

    user_prompt = ask_question("What do you want to look up? (type your question, say 'random_data' for rondom information of a star or type /help to check stuff): ")
    user_answer = user_prompt.ask()
    check_question(user_answer)






