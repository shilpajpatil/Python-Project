import pyqrcode
from pyqrcode import QRCode
def main():
    s="www.linkedin.com/in/ shilpa-patil-1178b3137"

    url=pyqrcode.create(s)

    url.svg("mypage.svg",scale=8)


if __name__ =="__main__":
    main()