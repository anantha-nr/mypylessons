import random
import sys
capitals_dict = {}

if len(sys.argv) < 2:
    print("Please provide flashcard file")
    exit(1)
flashcard_file = sys.argv[1]
fh = open(flashcard_file, 'r')
for line in fh:
    line_entry = line.strip().split(',')
    question = line_entry[0]
    capitals_dict[question] = line_entry[1]
fh.close()

print("Welcome to the flashcard quizzer.")
print("At any time, type 'quit' to quit.")
print('File Loaded. Let\'s Play')
print("")

question_list = list(capitals_dict.keys())
while True:
    question = random.choice(question_list)
    answer = capitals_dict[question]
    print(question)
    user_answer = input('Your Guess :> ')
    if user_answer == 'quit':
        break;
    elif user_answer == answer:
        print('Correct Answer')
    elif user_answer != answer:
        print('Incorrect Answer')
