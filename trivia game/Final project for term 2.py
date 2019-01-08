#Gabriel Harrison
#1/2/2018
#Trivia Game
import sys

def open_file(file_name,mode):
    #Open the file#
    try:
        the_file=open(file_name,mode)
    except IOError as e:
        print("Can not open the file:","term_2_final_project_trivia_text.txt","Ending the program.\n", e)
        input("\n\nPress the enter key to exit")
        sys.exit()
    else:
        return the_file
def next_line(the_file):
    #Return the next line from the trivia file, formatted correctly.#
    line=the_file.readline()
    line=line.replace("/","\n")
    return line
    
##file_name="term_2_final_project_trivia_text.txt"
##the_file=open_file(file_name,"r")
##line=next_line(the_file)
##print(line)

def next_block(the_file):
    category=next_line(the_file)
    question=next_line(the_file)
    answer_list=[]
    for i in range(4):
        answer_list.append(next_line(the_file))
    correct=next_line(the_file)
    if correct:
        correct=correct[0]
    explanation=next_line(the_file)
    return category,question,answer_list,correct,explanation
def welcome(title):
    #Welcome the user to the game#
    print("\tWelcome to the EPIC Trivia")
    print("\t\t",title,"\n")
def main():
    the_file=open_file("term_2_final_project_trivia_text.txt","r")
    title=next_line(the_file)
    welcome(title)
    score=0
    category,question,answer_list,correct,explanation=next_block(the_file)
    while category:
        print(category)
        print(question)
        for i in range(4):
            print(answer_list[i])
        user_answer=input("What is your answer?")
        if user_answer==correct:
            print("You got it correct")
            score+=1
        else:
            print("You failed")
            print(explanation)
        print(score)
        category,question,answer_list,correct,explanation=next_block(the_file)
    #Close file
    print("Nice job")
    print(score)
    input("Press enter to exit.")
        
main()
















    


