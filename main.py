from typing import Optional, Tuple, Union

from PIL import Image
from settings import *


class SideFrame(ctk.CTkFrame):
    def __init__(
        self,
        master: any,
        width: int = 200,
        height: int = 200,
        corner_radius: int | str | None = None,
        border_width: int | str | None = None,
        bg_color: str | Tuple[str, str] = "transparent",
        fg_color: str | Tuple[str, str] | None = None,
        border_color: str | Tuple[str, str] | None = None,
        background_corner_colors: Tuple[str | Tuple[str, str]] | None = None,
        overwrite_preferred_drawing_method: str | None = None,
        **kwargs
    ):
        super().__init__(
            master,
            width,
            height,
            corner_radius,
            border_width,
            bg_color,
            fg_color,
            border_color,
            background_corner_colors,
            overwrite_preferred_drawing_method,
            **kwargs
        )
        self.submain = SubMainFrame(self)
        self.home_image = load_image("/images/home.png", (40, 40))
        self.table_image = load_image("/images/table.png", (40, 40))
        self.switch_image = load_image("/images/switch.png", (40, 40))
        
        self.home_btn = ctk.CTkButton(
            self,
            width=50,
            text="",
            fg_color=SIDE_BG_COLOR,
            hover_color=SUB_MAIN_BG,
            corner_radius=0,
            image=self.home_image,
            command=lambda: self.submain.switch_frame('home')
        )
        self.home_btn.grid(row=0, column=0, pady=(50, 0), ipadx=10)

        self.table_btn = ctk.CTkButton(
            self,
            width=50,
            text="",
            fg_color=SIDE_BG_COLOR,
            hover_color=SUB_MAIN_BG,
            corner_radius=0,
            image=self.table_image,
            command=lambda: self.submain.switch_frame('table'),
        )
        self.table_btn.grid(row=1, column=0, pady=(15, 0), ipadx=10)

        self.switch_btn = ctk.CTkButton(
            self,
            width=50,
            text="",
            fg_color=SIDE_BG_COLOR,
            hover_color=SUB_MAIN_BG,
            corner_radius=0,
            image=self.switch_image,
            command=exit,
        )
        self.switch_btn.grid(row=2, column=0, pady=(350, 0), ipadx=10)
    
class MainFrame(ctk.CTkFrame):
    def __init__(
        self,
        master: any,
        width: int = 200,
        height: int = 200,
        corner_radius: int | str | None = None,
        border_width: int | str | None = None,
        bg_color: str | Tuple[str, str] = "transparent",
        fg_color: str | Tuple[str, str] | None = None,
        border_color: str | Tuple[str, str] | None = None,
        background_corner_colors: Tuple[str | Tuple[str, str]] | None = None,
        overwrite_preferred_drawing_method: str | None = None,
        **kwargs
    ):
        super().__init__(
            master,
            width,
            height,
            corner_radius,
            border_width,
            bg_color,
            fg_color,
            border_color,
            background_corner_colors,
            overwrite_preferred_drawing_method,
            **kwargs
        )

        # >>>>>>>>>>>>>>>>>CREATING THE SUB FRAME
        self.sub_main = SubMainFrame(
            self, width=600, height=400, fg_color=SUB_MAIN_BG, corner_radius=4
        )
        self.sub_main.grid(padx=(10, 10), pady=(50, 50), sticky="nsew")
        

        # >>>>>>>>>>>>>>>>>CONFIGURING THE FRAMES
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
    
    def __str__(self) -> str:
        return self

class SubMainFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.form_frame = FormFrame(self, fg_color=SUB_MAIN_BG)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def switch_frame(self, event):
        if event == 'home':
            self.form_frame.grid()
        elif event == 'table':
            self.form_frame.destroy()
        
    def __str__(self) -> str:
        return self

   

class FormFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self
        font_1 = ctk.CTkFont(family="Roboto", size=12, weight="bold")
        btn_font = ctk.CTkFont(family='Times', size=14, weight='bold')

        self.sch_name = ctk.CTkLabel(
            self, text="School Name: ", text_color=BLACK_COLOR, font=font_1
        )
        self.sch_entry = ctk.CTkEntry(
            self,
            width=200,
            height=40,
            fg_color=GRAY_COLOR,
            corner_radius=2,
            border_width=0,
        )
        self.book_name = ctk.CTkLabel(
            self, text="Book Name: ", text_color=BLACK_COLOR, font=font_1
        )
        self.book_entry = ctk.CTkEntry(
            self,
            width=200,
            height=40,
            fg_color=GRAY_COLOR,
            corner_radius=2,
            border_width=0,
        )
        self.year = ctk.CTkLabel(
            self, text="Year: ", text_color=BLACK_COLOR, font=font_1
        )
        self.year_entry = ctk.CTkEntry(
            self,
            width=200,
            height=40,
            fg_color=GRAY_COLOR,
            corner_radius=2,
            border_width=0,
        )
        self.month = ctk.CTkLabel(
            self, text="Month: ", text_color=BLACK_COLOR, font=font_1
        )
        self.month_entry = ctk.CTkEntry(
            self,
            width=200,
            height=40,
            fg_color=GRAY_COLOR,
            corner_radius=2,
            border_width=0,
        )
        self.class_name = ctk.CTkLabel(
            self, text="Class: ", text_color=BLACK_COLOR, font=font_1
        )
        self.class_name_entry = ctk.CTkEntry(
            self,
            width=200,
            height=40,
            fg_color=GRAY_COLOR,
            corner_radius=2,
            border_width=0,
        )
        self.volume = ctk.CTkLabel(
            self, text="Book Volume: ", text_color=BLACK_COLOR, font=font_1
        )
        self.volume_entry = ctk.CTkEntry(
            self,
            width=200,
            height=40,
            fg_color=GRAY_COLOR,
            corner_radius=2,
            border_width=0,
        )

        self.button = ctk.CTkButton(
            self,
            text="Generate",
            width=200,
            height=40,
            fg_color=SIDE_BG_COLOR,
            text_color=BLACK_COLOR,
            hover_color=TRANSPARENT_WHITE,
            font=btn_font,
            command="",
        )

        self.sch_name.grid(row=0, column=0, pady=(10, 0))
        self.sch_entry.grid(row=0, column=1, pady=(10, 0))
        self.book_name.grid(row=0, column=2, pady=(10, 0), padx=(5, 0))
        self.book_entry.grid(row=0, column=3, pady=(10, 0))
        self.year.grid(row=1, column=0, pady=(10, 0))
        self.year_entry.grid(row=1, column=1, pady=(10, 0))
        self.month.grid(row=1, column=2, pady=(10, 0), padx=(5, 0))
        self.month_entry.grid(row=1, column=3, pady=(10, 0))
        self.class_name.grid(row=2, column=0, pady=(10, 0))
        self.class_name_entry.grid(row=2, column=1, pady=(10, 0))
        self.volume.grid(row=2, column=2, pady=(10, 0), padx=(5, 0))
        self.volume_entry.grid(row=2, column=3, pady=(10, 0))
        self.button.grid(row=3, column=1, columnspan=3, pady=(10, 0), sticky="ew")

class App(ctk.CTk):
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    def __init__(self):
        super().__init__()

        self.app = self
        self.app.title("Book ID")
        self.app.iconbitmap("images/logo.ico")
        self.app.minsize(700, 600)
        self.app.maxsize(900, 800)
        

        # >>>>>>>>>>>>>>>>>CREATING THE MAIN FRAMES
        self.side_frame = SideFrame(
            self.app, width=80, height=600, fg_color=SIDE_BG_COLOR, corner_radius=0
        )
        self.side_frame.grid(row=0, column=0, rowspan=3, sticky="ns")

        self.main_frame = MainFrame(
            self.app, width=620, height=600, fg_color=MAIN_BG_COLOR, corner_radius=0
        )
        self.main_frame.grid(row=0, column=1, padx=(1, 0), columnspan=3, sticky="nsew")



        # >>>>>>>>>>>>>>>>>CONFIGURING THE FRAMES
        self.app.columnconfigure(1, weight=1)
        self.app.rowconfigure(0, weight=1)

    def check(self):
        if self.side_frame.get() == 'home':
            self.main_frame.sub_main.form_frame.grid()


def load_image(image_path: str, size: Tuple[int | int]):
    current_folder_path = os.path.dirname(os.path.realpath(__file__))
    open_img = ctk.CTkImage(Image.open(current_folder_path + image_path), size=size)
    return open_img


if __name__ == "__main__":
    app = App()
    app.mainloop()
