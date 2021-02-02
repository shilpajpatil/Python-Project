#----------------------------------------------------------------------
"""
Project Name:Acronyms creation
Purpose: acronyms is a short form of word created by long phrase
By: Shilpa Jayant Patil
Input: Random Access Memory
Output: RAM
"""
#---------------------------------------------------------------------

def main():
    print("----Acronyms Creation------")
    user_input = input("enter a input:")         #input from user
    acronym=acro_creation(user_input)            #passing input to a function
    print("acronym:",acronym)

def acro_creation(user_input):
    input=user_input.split()                   #spliting user input creare a list
    output=" "
    for i in input:
        output=output+str(i[0]).upper()         #list elements first strings first charactor converting into uppercase and saving in a variable

    return output




if __name__ == "__main__":
    main()