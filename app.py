
from frames import *

class App(ctk.CTk):
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    def __init__(self):
        super().__init__()

        self.app = self
        self.app.title("Book ID")
        self.app.iconbitmap("images/logo.ico")
        self.app.minsize(1000, 800)

        # >>>>>>>>>>>>>>>>>CREATING THE MAIN FRAMES
        self.side_frame = SideFrame(
            self.app, width=80, height=600, fg_color=SIDE_BG_COLOR, corner_radius=0
        )
        self.side_frame.grid(row=0, column=0, rowspan=3, sticky="ns")

        self.main_frame = MainFrame(
            self.app, width=720, height=600, fg_color=MAIN_BG_COLOR, corner_radius=0
        )
        self.main_frame.grid(row=0, column=1, padx=(1, 0), columnspan=3, sticky="nsew")

        # >>>>>>>>>>>>>>>>>CONFIGURING THE FRAMES
        self.app.columnconfigure(1, weight=1)
        self.app.rowconfigure(0, weight=1)

        # >>>>>>>>>>>>>>>>>CREATING THE MENU BUTTON
        "...Loading The Menu Image ...."
        self.home_image = load_image("/images/home.png", (40, 40))
        self.table_image = load_image("/images/table.png", (40, 40))
        self.switch_image = load_image("/images/switch.png", (40, 40))

        self.home_btn = ctk.CTkButton(
            self.side_frame,
            width=50,
            text="",
            fg_color=SIDE_BG_COLOR,
            hover_color=SUB_MAIN_BG,
            corner_radius=0,
            image=self.home_image,
            command=lambda: self.switch("home"),
        )
        self.home_btn.grid(row=0, column=0, pady=(50, 0), ipadx=10)

        self.table_btn = ctk.CTkButton(
            self.side_frame,
            width=50,
            text="",
            fg_color=SIDE_BG_COLOR,
            hover_color=SUB_MAIN_BG,
            corner_radius=0,
            image=self.table_image,
            command=lambda: self.switch("table"),
        )
        self.table_btn.grid(row=1, column=0, pady=(15, 0), ipadx=10)

        self.switch_btn = ctk.CTkButton(
            self.side_frame,
            width=50,
            text="",
            fg_color=SIDE_BG_COLOR,
            hover_color=SUB_MAIN_BG,
            corner_radius=0,
            image=self.switch_image,
            command=exit,
        )
        self.switch_btn.grid(row=2, column=0, pady=(550, 0), ipadx=10)

        # >>>>>>>>>>>>>>>>>CREATING THE SUB MAIN FRAME
        self.sub_main = SubMainFrame(
            self.main_frame,
            width=600,
            height=400,
            fg_color=SUB_MAIN_BG,
            corner_radius=4,
        )
        self.sub_main.grid(padx=(10, 10), pady=(50, 50), sticky="nsew")

        # >>>>>>>>>>>>>>>> CREATING AND DISPLAYING THE FORM FRAME
        self.form_frame = FormFrame(self.sub_main, fg_color=SUB_MAIN_BG)
        self.form_frame.grid()

        # >>>>>>>>>>>>>>>> CREATING THE TABLE FRAME
        self.table_frame = TableFrame(self.sub_main, width=600, fg_color=SUB_MAIN_BG, orientation='horizontal')

        # self.table_scroll = ctk.CTkScrollbar(self.sub_main, command=self.table_frame.yview)
        # self.table_scroll.grid(row = 0, column=0)

    def switch(self, event):
        if event == "home":
            self.table_frame.grid_remove()
            self.form_frame.grid()
        elif event == "table":
            self.form_frame.grid_remove()
            self.table_frame.grid(sticky='new', pady=(50, 0))


def load_image(image_path: str, size: Tuple[int | int]):
    current_folder_path = os.path.dirname(os.path.realpath(__file__))
    open_img = ctk.CTkImage(Image.open(current_folder_path + image_path), size=size)
    return open_img


if __name__ == "__main__":
    app = App()
    app.mainloop()
