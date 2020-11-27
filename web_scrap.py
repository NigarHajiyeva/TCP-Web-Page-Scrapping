import requests
from bs4 import BeautifulSoup
import argparse
import re
import socket
import sys

HOST = '127.0.0.1'
PORT = 6543
MAXBYTES = 65535

class server:
    def __init__(self):
            return

        
    
    def connectToClient(self):
       sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
       sock.bind((HOST, PORT))
       sock.listen(5)

       print("[SERVER] is started at....", sock.getsockname())

       print(" ")
       while True:
            sc, addr = sock.accept()
            print(f'ACCEPTED CONNECTION FROM...... {addr}')


            url = sc.recv(MAXBYTES).decode("utf-8")
            
            countedData = self.countOfData(url)
            sc.sendall(countedData.encode('utf-8'))
            

            print(" ")
            print(f'COUNTED DATA WAS SENT .......{addr}')
            sc.close()

            print("\n \n")


    def countOfData(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        images = soup.find_all('img')

        #images
        count1 = len(images)

        count2 = 0
        
        # paragraphs
        paragraphs = soup.find_all('p')
        for p in paragraphs:
            if not p.find_all('p'):
                count2 += 1

        result = f"The number of pictures:{count1} \nThe number of leaf paragraphs:{count2}"

        return result



    
class client:
    def __init__(self):
        #self.URL = URL
        return


    def connectToServer(self,URL):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST,PORT))

        print("[CLIENT] is connected...")
        print(" ")


        #check url 
        checkedUrl = re.search("^http",URL)
        if not checkedUrl:
            URL  = "https://" + URL


        sock.sendall(URL.encode("utf-8"))
        
        print("COUNTED DATA IN PROCESS......")

        answer =(sock.recv(MAXBYTES)).decode('utf-8')
        print(" ")
        print(answer)

        sock.close()


if __name__=="__main__":
    parser = argparse.ArgumentParser(description = "WEB SCRAPPING")
    choices = {"server": server, "client": client}
    parser.add_argument('choices', choices = choices, help = "server or client")
       
    if 'client' in sys.argv:
        parser.add_argument('-p', type=str,help="Enter URl")


    args = parser.parse_args()

    
    if args.choices == "server":
        server().connectToClient()
    elif args.choices == "client":
        client().connectToServer(args.p)
      

        


