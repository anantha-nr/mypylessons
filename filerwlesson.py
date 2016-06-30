f = open('scores.txt',mode='w')

while True:
    participant = input("Enter the Participant name > ")
    if participant == 'quit':
        print("Quitting....")
        break
    score = input("Enter the score fo the " + participant + " > ")
    f.write(participant + "," + score + '\n')
f.close()
f=open("scores.txt",mode='r')
for line in f:
    print(line)
f.close()