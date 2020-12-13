from tkinter import*
import os
from tkinter.messagebox import*
from tkinter.filedialog import*

root=Tk()
root.geometry("350x350")
root.minsize(height=350,width=350)
root.maxsize(height=1000,width=1000)
root.title("Notepad")
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
text_info=Text(root,yscrollcommand=scrollbar.set)
text_info.pack(fill=BOTH)
scrollbar.config(command=text_info.yview)
self._thisFileMenu.add_command(label="new",command=self._newFile)
self.
root.mainloop()
