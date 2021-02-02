#-------------------------------------------------------
"""
Project Name:Email slicer
Purpose: dividing user name and domain name
By: Shilpa Jayant Patil
Input: pshilpa056@gmail.com
Output: username:pshilpa056      domain name: gmail.com
"""
#-------------------------------------------------------
#By using split function
import re
def main():
   # mail=input("enter a email id:")
    #mailslicer(mail)

def mailslicer(mail):
    re.split("@",mail)
    username=(mail.split("@"))
    uname=username[0]
    dname=username[1]
    print("user name is :",uname)
    print("domain name:",dname)


if __name__ =="__main__":
    main()

# By using strip function
"""
 email = input("Enter Your Email: ").strip()
   username = email[:email.index("@")]
   domain_name = email[email.index("@") + 1:]
   format_ = (f"Your user name is '{username}' and your domain is '{domain_name}'")
   print(format_)
"""