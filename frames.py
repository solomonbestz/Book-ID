from settings import *



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

        # >>>>>>>>>>>>>>>>>CONFIGURING THE FRAMES
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)


class SubMainFrame(ctk.CTkFrame):
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

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)


class FormFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        years = ['2023', '2024', '2025', '2026', '2027', '2028', '2029']
        months = ['January', 'February', 'March','April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

        font_1 = ctk.CTkFont(family="Roboto", size=12, weight="bold")
        btn_font = ctk.CTkFont(family="Robot", size=16, weight="bold")

        self.sch_name = ctk.CTkLabel(
            self, text="School Name: ", text_color=BLACK_COLOR, font=font_1
        )
        self.sch_entry = ctk.CTkEntry(
            self,
           width=300,
            height=45,
            fg_color=SUB_MAIN_BG,
            text_color=BLACK_COLOR,
            border_width=1,
            border_color=BLACK_COLOR,
            font=('Roboto', 15,),
            corner_radius=2,
        )
        self.book_name = ctk.CTkLabel(
            self, text="Book Name: ", text_color=BLACK_COLOR, font=font_1
        )
        self.book_entry = ctk.CTkEntry(
            self,
            width=300,
            height=45,
            fg_color=SUB_MAIN_BG,
            text_color=BLACK_COLOR,
            border_width=1,
            border_color=BLACK_COLOR,
            font=('Roboto', 15,),
            corner_radius=2,
        )
        self.year = ctk.CTkLabel(
            self, text="Year: ", text_color=BLACK_COLOR, font=font_1
        )
        self.year_entry = ctk.CTkComboBox(
            self,
            width=300,
            height=45,
            fg_color=SUB_MAIN_BG,
            text_color=BLACK_COLOR,
            border_width=1,
            border_color=BLACK_COLOR,
            font=('Roboto', 15,),
            corner_radius=2,
            values=years
        )
        self.month = ctk.CTkLabel(
            self, text="Month: ", text_color=BLACK_COLOR, font=font_1
        )
        self.month_entry = ctk.CTkComboBox(
            self,
           width=300,
            height=45,
            fg_color=SUB_MAIN_BG,
            text_color=BLACK_COLOR,
            border_width=1,
            border_color=BLACK_COLOR,
            font=('Roboto', 15,),
            corner_radius=2,
            values=months
        )
        self.class_name = ctk.CTkLabel(
            self, text="Class: ", text_color=BLACK_COLOR, font=font_1
        )
        self.class_name_entry = ctk.CTkEntry(
            self,
            width=300,
            height=45,
            fg_color=SUB_MAIN_BG,
            text_color=BLACK_COLOR,
            border_width=1,
            border_color=BLACK_COLOR,
            font=('Roboto', 15,),
            corner_radius=2,
        )
        self.volume = ctk.CTkLabel(
            self, text="Book Volume: ", text_color=BLACK_COLOR, font=font_1
        )
        self.volume_entry = ctk.CTkEntry(
            self,
            width=300,
            height=45,
            fg_color=SUB_MAIN_BG,
            text_color=BLACK_COLOR,
            border_width=1,
            border_color=BLACK_COLOR,
            font=('Roboto', 15,),
            corner_radius=2,
        )

        self.button = ctk.CTkButton(
            self,
            text="Generate",
            width=200,
            height=40,
            fg_color=SIDE_BG_COLOR,
            text_color=BLACK_COLOR,
            hover_color=GRAY_COLOR,
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

class TableFrame(ctk.CTkScrollableFrame):
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

        # take the data
        lst = [
            (1, "Raj", "Mumbai", 19),
            (2, "Aaryan", "Pune", 18),
            (3, "Vaishnavi", "Mumbai", 20),
            (4, "Rachna", "Mumbai", 21),
            (5, "Shubham", "Delhi", 21),
        ]

        # find total number of rows and
        # columns in list
        total_rows = len(lst)
        total_columns = len(lst[0])
        for i in range(total_rows):
            for j in range(total_columns):
                self.table_entry = ctk.CTkEntry(
                    self,
                    width=200,
                    text_color=BLACK_COLOR,
                    fg_color=SUB_MAIN_BG,
                    corner_radius=0,
                    font=("Arial", 16, "bold"),
                )

                self.table_entry.grid(row=i, column=j)
                self.table_entry.insert(ctk.END, lst[i][j])
                self.table_entry.configure(state='disabled')
        self.columnconfigure(0, weight=1)
        # self.rowconfigure(0, weight=1)