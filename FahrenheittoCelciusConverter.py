

"""
Project Name:Fahrenheit to Celcius Converter
By: Shilpa Jayant Patil
Input:
Output:
"""


def main():
    faherenheit=int(input("enter a  tempreture in faherenheit:"))
    print(faherenheit)
    res=converter(faherenheit)
    print("faherenheit convert into celcius:",res)

def converter(faherenheit):
    return(5/9 * (faherenheit-32))

if __name__ == "__main__":
    main()