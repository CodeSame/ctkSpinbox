import customtkinter as ctk
from typing import Callable

class Spinbox(ctk.CTkFrame):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 32,
                 step_size: int = 1,
                 min_value,max_value,
                 command: Callable = None,
                 **kwargs):
        self.min_value = min_value
        self.max_value = max_value
        super().__init__(*args, width=width, height=height, **kwargs)
        
        self.step_size = step_size
        self.command = command

        self.configure(fg_color=("gray78", "gray28"))  

        self.grid_columnconfigure((0, 2), weight=0)  
        self.grid_columnconfigure(1, weight=1)  

        self.subtract_button = ctk.CTkButton(self, text="-", width=height-6, height=height-6,
                                                        command=self.subtract_button_callback)
        self.subtract_button.grid(row=0, column=0, padx=(3, 0), pady=3)

        self.entry = ctk.CTkEntry(self, width=width-(70), height=height-6, border_width=0)
        self.entry.grid(row=0, column=1, columnspan=1, padx=3, pady=3, sticky="nsew")

        self.add_button = ctk.CTkButton(self, text="+", width=height-6, height=height-6,
                                                  command=self.add_button_callback)
        self.add_button.grid(row=0, column=2, padx=(0, 3), pady=3)
    
        # default value
        self.entry.insert(0, "0")
        # All elements on mouswhel event
        self.entry.bind("<MouseWheel>", self.on_mouse_wheel)
        self.subtract_button.bind("<MouseWheel>", self.on_mouse_wheel)
        self.add_button.bind("<MouseWheel>", self.on_mouse_wheel)
        self.bind("<MouseWheel>", self.on_mouse_wheel)
        
    def add_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = int(self.entry.get()) + self.step_size
            if value <=self.max_value: 
                self.entry.delete(0, "end")
                self.entry.insert(0, value)
        except ValueError:
            return
    
    def subtract_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = int(self.entry.get()) - self.step_size
            if value >=self.min_value: 
                self.entry.delete(0, "end")
                self.entry.insert(0, value)
        except ValueError:
            return

    def get(self) -> int:
        try:
            return int(self.entry.get())
        except ValueError:
            return 0
            
    def on_mouse_wheel(self, event):
        if event.delta > 0:
            self.add_button_callback()
        else:
            self.subtract_button_callback()
            
    def set(self, value: int):
        self.entry.delete(0, "end")
        self.entry.insert(0, int(value))      

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_default_color_theme("green") 
        self.title("Spinbox_sample")
        self.geometry(f"{300}x{100}")
        #Creating Main_Frame
        self.main_frame = ctk.CTkFrame(self, width=510,height=290, corner_radius=0)
        self.main_frame.grid(row=0, column=10,columnspan=10, rowspan=10, ipadx=5, ipady=0, padx=0, pady=0, sticky="nw")
        self.main_frame.grid_rowconfigure(3, weight=1)
        #Spinboxes
        self.spinbox_hours = Spinbox(self.main_frame, width=105, step_size=1, min_value=0, max_value=23)
        self.spinbox_hours.grid(row=0, column=2, rowspan=1, ipadx=0, ipady=0, padx=0, pady=0)
        self.spinbox_hours.set(0)      
        self.spinbox_minutes = Spinbox(self.main_frame, width=105, step_size=1, min_value=0,max_value=59)
        self.spinbox_minutes.grid(row=0, column=4, rowspan=1, ipadx=0, ipady=0, padx=0, pady=0)
        self.spinbox_minutes.set(0)
        self.spinbox_seconds = Spinbox(self.main_frame, width=105, step_size=1,min_value=0,max_value=59)
        self.spinbox_seconds.grid(row=0, column=6, rowspan=1, ipadx=0, ipady=0, padx=0, pady=0)
        self.spinbox_seconds.set(0)       
        
if __name__ == "__main__":
    app = App()
    app.resizable(width=False, height=False)
    app.mainloop()
#https://github.com/TomSchimansky/CustomTkinter and CodeSame @2023
