import customtkinter as ctk








if __name__=='__main__':
    root = ctk.CTk()


# CREATING FRAMES >>>>>>>>>>>>>>>>>>>>>>

    frame = ctk.CTkFrame(root, width=20, corner_radius=0, fg_color='#4D96FF', border_width=1, border_color='red')
    frame.grid(row = 0, rowspan=2, column = 0, sticky='nswe')
    frame = ctk.CTkFrame(root, width=200, height=200,corner_radius=0, fg_color='#3A3845', border_width=1, border_color='white')
    frame.grid(row = 0, column = 1, sticky='nswe')
    frame = ctk.CTkFrame(root, width=200, height=200,corner_radius=0, fg_color='#3A3845', border_width=1, border_color='white')
    frame.grid(row = 0, column = 2, sticky='nswe')
    # frame = ctk.CTkFrame(root, width=200, height=200,corner_radius=0, fg_color='#3A3845', border_width=1, border_color='white')
    # frame.grid(row = 1, column = 0, sticky='nswe')
    frame = ctk.CTkFrame(root, width=200, height=200,corner_radius=0, fg_color='#3A3845', border_width=1, border_color='white')
    frame.grid(row = 1, column = 1, sticky='nswe')
    frame = ctk.CTkFrame(root, width=200, height=200,corner_radius=0, fg_color='#3A3845', border_width=1, border_color='white')
    frame.grid(row = 1, column = 2, sticky='nswe')
   

    # frame2 = ctk.CTkFrame(root, width=200, height=200,corner_radius=0, fg_color='#F7CCAC')
    # frame2.grid(row = 1, column = 0, sticky='nswe')

    # frame3 = ctk.CTkFrame(root, width=250, height=250,corner_radius=0, fg_color='#FFD93D')
    # frame3.grid(row = 0, column = 1, sticky='nswe')

    # frame4 = ctk.CTkFrame(root, width=150, height=100,corner_radius=0, fg_color='#6BC877')
    # frame4.grid(row = 1, column = 1, sticky='nsew')

    # horizontal = ctk.CTkFrame(root, width=500, height=100,corner_radius=0, fg_color='#4D96FF')
    # horizontal.grid(row = 2, column=0, columnspan=2, sticky='nswe')

    # vertical = ctk.CTkFrame(root, width=100, height=350,corner_radius=0, fg_color='#FF6B6B')
    # vertical.grid(row = 0, column=2, rowspan=3, sticky='nswe')

# CONFIGURING THE FRAMES >>>>>>>>>>>>>>>>>>>>>>>>

    root.columnconfigure(0, weight=1)
    root.columnconfigure((1, 2), weight=2)
    root.rowconfigure((0, 1), weight=1)

   

    root.mainloop()