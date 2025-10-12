#store admin password
adminpass="InstProject20"
#store info for later code sections
quiz_length=0
correct=0
i=1
#create a function to insert edited quiz questions/answers into a quiz
def quiz_edit(quiz,questions):
    f = open(quiz+".txt","w")
    f.write(str(questions))
    f.close()
while True:
    #ask the user what type of user they are, store response in a variable
    user_type=input("What type of user are you, quiz-taker or admin? You can also type 'quit' to quit:").lower()
    #creating a quiz
    #if the user is an admin
    if user_type=="admin":
        #ask them for the admin password, which is stored in the adminpass variable
        pass_input=input("What is the admin password? This is case sensitive:")
        #if the password is correct
        if pass_input==adminpass:
            #empty the 'quiz' dictionary to ensure existing data is cleared
            quiz={}
            #Ask the user if they want to create or edit a quiz and store their response
            dec=input("Enter 'new' to create a new quiz or 'edit' to edit an existing quiz").lower()
            #if they want to create a new quiz
            if dec=="new":
                #until the loop is exited
                while True:
                    #ask the user for a quiz question and store it
                    quiz_q=input("Enter a quiz question, or type 'quit' to finalize the quiz:")
                    #if the user types 'quit'
                    if quiz_q.lower()=='quit':
                        #print out the quiz
                        print("Here is your quiz:")
                        print(quiz)
                        #ask the user to name the quiz, store response
                        quiz_name=input("What would you like to name your quiz?")
                        #create a text file named the quiz name and store the quiz dictionary in it
                        f = open(quiz_name+".txt","w")
                        f.write(str(quiz))
                        f.close()
                        #update the list of quizzes to include the new quiz
                        try:
                            #if the quiz list file exists
                            quiz_list=[]
                            #read its contents into a list variable
                            with open("quiz_list.txt",'r') as inf:
                                f = eval(inf.read())
                            for line in f:
                                quiz_list.append(line)
                        #if the file does not exist, create a blank list variable
                        except:
                            quiz_list=[]
                        #append the new quiz name to the list of quizzes
                        quiz_list.append(quiz_name)
                        #store the updated list in the quiz list file, creating the file if it didn't exist
                        f = open("quiz_list.txt","w")
                        f.write(str(quiz_list))
                        f.close()
                        print("Quiz saved. Exiting.")
                        break
                    #if the user is not done entering question/answer pairs
                    else:
                        #ask the user for a answer 
                        quiz_a=input("Enter a quiz answer:").lower()
                        #update the quiz dictionary with the new question/answer pair
                        quiz.update({quiz_q:quiz_a})
            #if the user wants to edit an existing quiz
            elif dec=="edit":
                while True:
                    #try to open the quiz list file
                    try:
                        #if the file exists, open it and read its contents into a variable
                        f=open("quiz_list.txt")
                        #print the list of quizzes
                        print("Saved quizzes:")
                        for line in f:
                            print(line)
                        f.close()
                    except:
                        #if there is no quiz list file, tell the user that they must create a quiz before it can be edited and return to the menu
                        print("There are no quizzes saved. You must create a quiz before you can edit it.")
                        break
                    #ask the user which quiz they want to edit
                    quiz_select=input("Please enter the name of a quiz you would like to edit, or type 'quit' to quit:")
                    #if the user types 'quit', return to the menu
                    if quiz_select.lower()=="quit":
                        print("Ok, exiting")
                        break
                    else:
                        #try to open the quiz the user entered
                        try:
                            #open the quiz file and make it into a dictionary
                            with open(quiz_select+".txt",'r') as inf:
                                quiz = eval(inf.read())
                            #store the list of quiz questions in a variable
                            quiz_qs=list(quiz.keys())
                            #print the list of quiz questions
                            print("Available questions to edit:")
                            print(quiz_qs)
                            #ask the user which question they want to edit and store that question in a variable
                            q_choice=int(input("Which number question would you like to edit?"))
                            edit_q=quiz_qs[q_choice-1]
                            #ask the user if they want to edit the question or the answer
                            edit_choice=input("Would you like to edit the question or the answer?").lower()
                            #if the user wants to edit the question
                            if edit_choice=="question":
                                #ask them to enter the new question and store it
                                new_q=input("Enter a new question:")
                                #update the quiz dictionary with the new question
                                quiz.update({new_q:quiz[edit_q]})
                                #remove the dictionary item with the old question
                                quiz.pop(edit_q)
                                #call the function to insert the edited quiz into the file and save the file
                                quiz_edit(quiz_select,quiz)
                            #if the user wants to edit the answer
                            if edit_choice=="answer":
                                #print the current answer
                                print("Current answer:")
                                print(quiz[edit_q])
                                #ask them to enter the new answer and store it
                                new_a=input("Enter a new answer:")
                                #update the quiz dictionary with the new answer
                                quiz.update({edit_q:new_a})
                                #call the function to insert the edited quiz into the file and save the file
                                quiz_edit(quiz_select,quiz)
                        #if the selected quiz does not exist, tell the user
                        except:
                            print("Selection not found.")
        #if the admin password is incorrect, tell the user
        else:
            print("Password is incorrect.")
    #taking a quiz
    #if the user is a quiz-taker
    elif user_type=="quiz-taker":
        while True:
            #try to open the list of quizzes
            try:
                #open and print the list of quizzes
                f=open("quiz_list.txt")
                print("Saved quizzes:")
                for line in f:
                    print(line)
                f.close()
            #if the list of quizzes does not exist, tell the user that an admin must create a quiz before they can take one and quit to the menu
            except:
                print("There are no quizzes saved. If you are an admin, please log in to create a quiz.")
                break
            #ask the user which quiz they want to take and store their response
            quiz_select=input("Welcome! Please enter the name of a quiz you would like to take, or type 'quit' to quit:")
            #if the user enters 'quit', thank them for playing and quit to the menu
            if quiz_select.lower()=="quit":
                print("Thanks for playing!")
                break
            #if the user wants to take a quiz
            else:
                try:
                    #try to read the selected quiz in and make it into a dictionary
                    with open(quiz_select+".txt",'r') as inf:
                        quiz = eval(inf.read())
                    #save the length of the quiz
                    quiz_length=len(quiz)
                    #save the list of quiz questions
                    quiz_qs=list(quiz.keys())
                    #until the quiz runs out of questions
                    while (i-1) < quiz_length:
                        #save the current question
                        question=quiz_qs[i-1]
                        #print the current question number and question
                        print("Question %d:" %i)
                        print(question)
                        #ask the user for the answer
                        answer=input("What is the answer?").lower()
                        #if the answer is correct, tell the user and add 1 to the number of questions they have gotten correct
                        if answer==quiz[question]:
                            print("Correct!")
                            correct+=1
                        #if the answer is wrong, tell the user
                        else:
                            print("Incorrect. The correct answer is %s." %quiz[question])
                        #advance the current question number by 1
                        i+=1
                    #when the quiz runs out of questions, print the number of questions the user has answered correctly and their percent correct
                    print("This quiz has run out of questions. You answered %d questions correctly, for a score of %d percent." %(correct, (correct/quiz_length)*100))
                except:
                    #if the selected quiz file does not exist, tell the user
                    print("File not found.")
    #when the user types 'quit', exit the quiz program
    elif user_type=="quit":
        print("Ok, exiting.")
        break
    else:
        #if the user does not enter a correct user type, tell them
        print("Please enter a correct user type.")