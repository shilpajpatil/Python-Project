"""

Project Name:converting  roman to decimal
Purpose: converting roman number into decimal
By: Shilpa Jayant Patil
Input: 'IX'
Output: 9
"""
indentation ={
        'I': 1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }


def main():

    decimal_Num=RomanNumberToDecimal('IX')
    print("roman number converted into decimal:",decimal_Num)


def RomanNumberToDecimal(romanNumber):
    sum=0

    for i in range(len(romanNumber)-1):
        left=romanNumber[i]
        right=romanNumber[i+1]
        if indentation[left] <indentation[right]:
            sum -= indentation[left]
        else:
            sum += indentation[left]

    #val=(indentation[romanNumber[-1]])
    #print(val)
    sum += indentation[romanNumber[-1]]
    return sum



if __name__ == "__main__":
    main()



