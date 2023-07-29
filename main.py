from settings import *


class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Book Reg ID")
        self.geometry("1000x500")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure((1, 2), weight=3)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure((1, 2), weight=3)

        self.side_frame = SideFrame(self, fg_color="red", width=50)
        self.side_frame.grid(row=0, rowspan=3, column=0, sticky="nsew")
        self.top_bar = TopFrame(
            self
        )  # fg_color=TOP_BG_COLOR, height=50, corner_radius=0
        self.top_bar.grid(row=0, column=1, columnspan=2, padx=(0, 0), sticky="nsew")
        self.main_frame = MainFrame(self)  # fg_color="gray", corner_radius=0
        self.main_frame.grid(
            row=1, column=1, rowspan=2, columnspan=2, padx=(0, 0), sticky="nsew"
        )


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
