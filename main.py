from customtkinter import *

#logitalk app with menu panel on the left side which can hide and show smoothly
class LogiTalkApp(CTk):
    def __init__(self):
        super().__init__()

        self.title("LogiTalk")
        self.geometry("800x600")

        self.menu_panel = CTkFrame(self, width=200, height=600, corner_radius=0)
        self.menu_panel.pack(side="left", fill="y")

        self.toggle_button = CTkButton(self.menu_panel, text="Toggle Menu", command=self.toggle_menu)
        self.toggle_button.pack(pady=20)

        self.content_frame = CTkFrame(self, width=600, height=600, corner_radius=0)
        self.content_frame.pack(side="right", fill="both", expand=True)

        self.menu_visible = True

    def toggle_menu(self):
        if self.menu_visible:
            self.hide_menu()
        else:
            self.show_menu()

    def hide_menu(self):
        for i in range(200, 0, -20):
            self.menu_panel.configure(width=i)
            self.update()
            self.after(10)
        self.menu_visible = False

    def show_menu(self):
        for i in range(0, 200, 20):
            self.menu_panel.configure(width=i)
            self.update()
            self.after(10)
        self.menu_visible = True


if __name__ == "__main__":
    app = LogiTalkApp()
    app.mainloop()