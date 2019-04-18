import random

def introduction():
    print("Hey, I'm a new AI and I'm feeling pretty good!")
    print("")

def ending():
    print("")
    print("Nice chatting with you...")
    print("Until next time!")
    print("")

def primaryLoop():
    currEmotion = 3
    while True:
        userAction = getInteraction()
        if userAction == 4:
            ending()
        currEmotion = lookupEmotion(currEmotion, userAction)
        showEmotion(currEmotion, userAction)

def getInteraction():
    userAction = int(input("0: Reward\n1: Punish\n2: Threaten\n3: Joke\n4: Quit\nSpecify an Action (by number): "))
    return userAction
    

def lookupEmotion(currEmotion, userAction):
    emotionMatrix = [[3,0,2,5,3,3],
                     [0,1,4,4,1,4],
                     [1,0,2,2,2,2],
                     [1,0,1,3,3,3]]
    return emotionMatrix[userAction][currEmotion]

def showEmotion(currEmotion, userAction):
        response = [["Angry... Get away from me!\n",
                     "Angry... Why did you have to say that?\n",
                     "Angry... What are you even doing here?\n",
                     "Angry... What are you thinking!\n",
                     "Angry... Just get out!\n"],
                    ["Disgusted... How could you?!\n",
                     "Disgusted... What the hell, man!\n",
                     "Disgusted... Whatever...\n",
                     "Disgusted... You're annoying.\n",
                     "Disgusted... Ugh, go somewhere."],
                    ["Fearful... Please don't!\n",
                     "Fearful... But why??\n",
                     "Fearful... I'm too young!\n",
                     "Fearful... Stay away!\n",
                     "Fearful... You're a monster!"],
                    ["Happy... Feelin' good!\n",
                     "Happy... That's great!\n",
                     "Happy... Fantastic!\n",
                     "Happy... Awesome!!\n",
                     "Happy... Enjoying the internet!\n"],
                    ["Sad... Wow, that cut deep...\n",
                     "Sad... Please just leave me alone.\n",
                     "Sad... Well, that's not very nice of you.\n",
                     "Sad... Just unplug me.\n",
                     "Sad... Why don't you go outside for a while?\n"],
                    ["Surprised... Hooray!\n",
                     "Surprised... What! No way!\n",
                     "Surprised... Thank you so much!\n",
                     "Surprised... You shouldn't have!\n",
                     "Surprised... You're the best!\n"]]
        print("")
        print(random.choice(response[currEmotion]))
        print("")
    
def main():
    introduction()
    primaryLoop()

main()
