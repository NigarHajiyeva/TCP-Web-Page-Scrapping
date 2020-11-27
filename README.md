# TCP - "Web Scraper" Application
## Scenario:
The client-server-based console app “Web_Scraper”.
With the next abilities:

Get statistical data: 

  * Calculate the number of pictures in the webpage
 
 *  Calculate the number of the leaf paragraphs in the webpage

## Task:
Create console-based app with two roles server and the client. The server must be started and wait the
request from the client. Server must produce the web scraping of the webpage to get two parameters:
 * The number of pictures and the number of the leaf paragraphs. The leaf paragraphs in HTML document
  represents only the last paragraphs in the nested paragraphstructures. The client must send the request to the server to get the proper answer. The client has options page (-
p) to get the statistical data. All the calcluation must be done on the server side

## Installation 
Clone repository into your directory:

    git clone https://github.com/NigarHajiyeva/Web_Scraper

Install requirements for this application:

    pip install -r requirements.txt

## Usage

To use this application, open 2 terminal tabs for **Server** and **Client**. For **Server**, run following command:

In this application host and port given by default: HOST: 127.0.0.1 PORT: 6543

    python3 web_scrap.py server
    

For **Client**, use the following commands:

      python3 web_scrap.py client -p [URL]
      
 *For example:*

     python3 web_scrap.py client -p www.pcworld.com
    
To stop server, head to **Server** terminal and press `Ctrl+C` (Linux OS), `Ctrl+Pause/Break` (Windows OS) in terminal.
