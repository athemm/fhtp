from Modals.Zone import Zone
from tkinterhtml import HtmlFrame
from tkinter import *

def html_render(resp):
    root2 = Tk()
    print(resp)
    frame = HtmlFrame(root2, horizontal_scrollbar="auto")
    frame.pack()
    frame.set_content("<html></html>")
    frame.set_content(resp)
    mainloop()

def load_webpage():
    uri_val = uri.get()
    host = uri_val.split("/")[0]
    path = "/".join(uri_val.split("/")[1:])
    d = html_render(rocks.request_page(host, path))

rocks = Zone(("127.0.0.1", 42031))

root = Tk()
# set window size
root.geometry("500x300")

#set window color
root.configure(bg='white')

uri = StringVar()
uriwidget = Entry(root,textvariable=uri,width=40)
uriwidget.grid(column=1,row=1)

send_widget = Button(root, text ="Send", command = load_webpage)
send_widget.grid(column=2,row=1)
root.mainloop()
