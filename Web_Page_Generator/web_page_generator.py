import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        self.master.geometry('350x200')

        # label that prompts user to enter custom text

        self.lbl_custom_text_prompt = tk.Label(self.master, text="Enter custom text or click the Default HTML page button")
        self.lbl_custom_text_prompt.grid(row=0, column=0, padx=(27, 0), pady=(10, 0), sticky=N+W)

        # input box for custom text

        self.txt_custom_text_prompt = tk.Entry(self.master, text='')
        self.txt_custom_text_prompt.grid(row=1, column=0, rowspan=1, columnspan=11, padx=(30, 40), pady=(0, 0), sticky=N + E + W)

        # creates "Default HTML Page" button

        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(padx=(10, 10), pady=(10, 10))

        # creates "Submit Custom Text" button

        self.btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.submitCustom)
        self.btn.grid(padx=(10,10), pady=(10, 10))


    # functionality for "Default HTML Page" button

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")                   # NOTE: this code doesn't work on a Mac
                                                                # possible issue with OS permissions to open a browser?

    # functionality that allows user to submit custom text to display on webpage
    # writes to custom.html so it doesn't override the default HTML file

    def submitCustom(self):
        htmlCustomText = self.txt_custom_text_prompt.get()
        htmlCustomFile = open("custom.html", "w")
        htmlCustomContent = "<html>\n<body>\n<h1>" + htmlCustomText + "</h1>\n</body>\n</html>"
        htmlCustomFile.write(htmlCustomContent)
        htmlCustomFile.close()
        webbrowser.open_new_tab("custom.html")

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
