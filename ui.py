import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class EvalynApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Evalyn")
        self.geometry("1000x600")
        self.resizable(False, False)
        self.configure(bg="white")
        self.current_photo = None
        self.frames = {}

        for F in (HomePage, UploadPage, InterviewPage):
            frame = F(self)
            self.frames[F] = frame
            frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.show_frame(HomePage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

    def set_photo(self, pil_img):
        self.current_photo = pil_img

    def get_photo(self):
        return self.current_photo

# --------- PAGE 1: HomePage --------------
class HomePage(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="white")

        # Evalyn Logo (replace with logo file if available)
        logo = tk.Label(self, text="🧠", font=("Arial", 90), bg="white")
        logo.pack(pady=25)

        tk.Label(self, text="Evalyn", font=("Arial Black", 48), bg="white").pack()

        tk.Label(
            self, text="AI-Powered Interview Assessment Suite\nSmarter · Fairer · Faster Hiring",
            font=("Arial", 16), bg="white", fg="black"
        ).pack(pady=10)

        tk.Button(
            self, text="Start Interview", font=("Arial", 22, "bold"),
            bd=2, relief="solid", fg="black", bg="white", padx=35, pady=10,
            command=lambda: master.show_frame(UploadPage)
        ).pack(pady=(48, 12))

        tk.Button(
            self, text="View Report", font=("Arial", 22, "bold"),
            bd=0, relief="solid", fg="white", bg="black", padx=45, pady=12,
            command=lambda: messagebox.showinfo("Report", "No reports yet!")
        ).pack()

        # Profile icon circle (top-right)
        profile_btn = tk.Label(self, text="👤", font=("Arial", 24), bg="#000", fg="#fff")
        profile_btn.place(relx=0.95, rely=0.03, anchor="ne") # position top right

# ------- PAGE 2: Upload Image ----------
class UploadPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="white")

        # Profile icon circle (top-right)
        profile_btn = tk.Label(self, text="👤", font=("Arial", 24), bg="#000", fg="#fff")
        profile_btn.place(relx=0.95, rely=0.03, anchor="ne")

        self.photo_label = tk.Label(self, bd=3, relief="solid", width=180, height=180, bg="white")
        self.photo_label.image = None
        self.photo_label.place(relx=0.6, rely=0.23)

        tk.Button(
            self, text="Upload Image", font=("Arial", 18, "bold"), fg="black", bg="white",
            bd=2, relief="solid", padx=15, pady=5,
            command=self.upload_img
        ).place(relx=0.18, rely=0.34, anchor="center")

        tk.Button(
            self, text="View Report", font=("Arial", 18, "bold"), fg="white", bg="black",
            bd=0, relief="solid", padx=18, pady=8,
            command=lambda: messagebox.showinfo("Report", "No reports yet!")
        ).place(relx=0.18, rely=0.48, anchor="center")

        tk.Button(
            self, text="Submit and Start", font=("Arial", 20, "bold"), fg="black", bg="white",
            bd=2, relief="solid", padx=24, pady=12,
            command=lambda: master.show_frame(InterviewPage)
        ).place(relx=0.5, rely=0.75, anchor="center")

    def upload_img(self):
        path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")]
        )
        if not path:
            return
        pil_img = Image.open(path).resize((180, 180))
        tk_img = ImageTk.PhotoImage(pil_img)
        self.photo_label.configure(image=tk_img)
        self.photo_label.image = tk_img
        self.master.set_photo(pil_img)

# -------- PAGE 3: Interview Page (Interview Start/End, Video/Transcript Box) ----
class InterviewPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="white")
        profile_btn = tk.Label(self, text="👤", font=("Arial", 24), bg="#000", fg="#fff")
        profile_btn.place(relx=0.95, rely=0.03, anchor="ne")

        # Main Transcript/Text box
        self.transcript_box = tk.Text(self, width=50, height=12, bd=3, relief="solid", font=("Arial", 15))
        self.transcript_box.place(relx=0.17, rely=0.20)

        # "Video" placeholder box (shows uploaded photo, in real app implement cam):
        self.video_frame = tk.Label(self, bd=4, relief="solid", width=210, height=260, bg="white")
        self.video_frame.place(relx=0.64, rely=0.17)
        self.update_photo()

        tk.Button(
            self, text="Start Interview", font=("Arial", 20, "bold"), fg="black", bg="white",
            bd=2, relief="solid", padx=22, pady=3,
            command=self.fake_start_interview
        ).place(relx=0.20, rely=0.65)

        tk.Button(
            self, text="End Interview", font=("Arial", 20, "bold"), fg="black", bg="white",
            bd=2, relief="solid", padx=16, pady=3,
            command=self.fake_end_interview
        ).place(relx=0.41, rely=0.65)

    def update_photo(self):
        photo = self.master.get_photo()
        if photo:
            img = photo.resize((210, 260))
            tk_img = ImageTk.PhotoImage(img)
            self.video_frame.configure(image=tk_img)
            self.video_frame.image = tk_img

    def fake_start_interview(self):
        self.transcript_box.delete(1.0, tk.END)
        self.transcript_box.insert(tk.END, "Interview started... [Mic/Recording logic here in real app]")

    def fake_end_interview(self):
        self.transcript_box.insert(tk.END, "\nInterview ended. Data saved!")

# --------- BOOTSTRAP ---------

if __name__ == "__main__":
    app = EvalynApp()
    app.mainloop()
