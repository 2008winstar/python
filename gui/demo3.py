import tkinter as tk


def quit():
    print('Hello, getting out of here')
    import sys
    sys.exit()

widget = tk.Button(None, text='Press me to quit', command=quit)
widget.pack()
widget.mainloop()
