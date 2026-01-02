import threading
import tkinter as tk
from tkinter import filedialog, messagebox
import queue
import traceback

from converter import convert_rbxlx

# CORES
BG_MAIN = "#1e1e1e"
BG_CARD = "#2a2a2a"
BG_INPUT = "#e6e6e6"

FG_TEXT = "#ffffff"
FG_MUTED = "#cfcfcf"

BTN_BLUE = "#2f8fa2"
BTN_GREEN = "#43d17a"


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("RBXLX → Rojo Converter")
        self.geometry("860x540")
        self.minsize(860, 540)

        self.rbxlx_path = tk.StringVar()
        self.output_dir = tk.StringVar()

        self.log_queue = queue.Queue()

        self._build_ui()
        self.after(50, self.process_logs)

    # UI
    def _build_ui(self):
        self.configure(bg=BG_MAIN)

        root = tk.Frame(self, bg=BG_MAIN)
        root.pack(fill="both", expand=True, padx=20, pady=20)

        tk.Label(
            root,
            text="RBXLX → ROJO CONVERTER",
            bg=BG_MAIN,
            fg=FG_TEXT,
            font=("Sans", 16, "bold")
        ).pack(anchor="w")

        tk.Label(
            root,
            text="Convert Roblox game scripts (.rbxlx) to a rojo project.",
            bg=BG_MAIN,
            fg=FG_MUTED,
            font=("Sans", 10)
        ).pack(anchor="w", pady=(0, 20))

        card = tk.Frame(root, bg=BG_CARD)
        card.pack(fill="x", pady=(0, 18), ipadx=20, ipady=18)

        tk.Label(
            card,
            text="Settings",
            bg=BG_CARD,
            fg=FG_TEXT,
            font=("Sans", 12, "bold")
        ).pack(anchor="w", pady=(0, 12), padx=6)

        self._labeled_input(
            card,
            ".rbxlx file",
            self.rbxlx_path,
            "Choose File",
            BTN_BLUE,
            self.pick_rbxlx
        )

        self._labeled_input(
            card,
            "Output folder",
            self.output_dir,
            "Choose Folder",
            BTN_BLUE,
            self.pick_output
        )

        self.convert_btn = tk.Button(
            root,
            text="Convert",
            bg=BTN_GREEN,
            fg="#000000",
            font=("Sans", 11, "bold"),
            relief="flat",
            bd=0,
            highlightthickness=0,
            activebackground=BTN_GREEN,
            activeforeground="#000000",
            height=2,
            command=self.start_conversion
        )
        self.convert_btn.pack(fill="x", pady=(0, 18))

        log_card = tk.Frame(root, bg=BG_CARD)
        log_card.pack(fill="both", expand=True, ipadx=20, ipady=18)

        tk.Label(
            log_card,
            text="Logs",
            bg=BG_CARD,
            fg=FG_TEXT,
            font=("Sans", 12, "bold")
        ).pack(anchor="w", pady=(0, 8))

        self.log_box = tk.Text(
            log_card,
            bg=BG_CARD,
            fg=FG_TEXT,
            relief="flat",
            bd=0,
            highlightthickness=0,
            font=("Monospace", 10),
            state="disabled"
        )
        self.log_box.pack(fill="both", expand=True)

        self.log("Okay. Select an .rbxlx file to begin.")

    def _labeled_input(self, parent, label, var, btn_text, btn_color, command):
        tk.Label(parent, text=label, bg=BG_CARD, fg=FG_TEXT).pack(anchor="w", padx=6)

        row = tk.Frame(parent, bg=BG_CARD)
        row.pack(fill="x", pady=(4, 12), padx=6)

        tk.Entry(
            row,
            textvariable=var,
            bg=BG_INPUT,
            relief="flat",
            bd=0,
            highlightthickness=0
        ).pack(side="left", fill="x", expand=True, padx=(0, 10), ipady=6)

        tk.Button(
            row,
            text=btn_text,
            bg=btn_color,
            fg="white",
            relief="flat",
            bd=0,
            highlightthickness=0,
            command=command
        ).pack(side="right", ipady=6, ipadx=12)

    # THREAD SAFE LOG
    def log(self, text):
        self.log_queue.put(text)

    def process_logs(self):
        while not self.log_queue.empty():
            msg = self.log_queue.get()
            self.log_box.config(state="normal")
            self.log_box.insert(tk.END, msg + "\n")
            self.log_box.see(tk.END)
            self.log_box.config(state="disabled")
        self.after(50, self.process_logs)

    def pick_rbxlx(self):
        path = filedialog.askopenfilename(filetypes=[("Roblox XML", "*.rbxlx")])
        if path:
            self.rbxlx_path.set(path)

    def pick_output(self):
        path = filedialog.askdirectory()
        if path:
            self.output_dir.set(path)

    def start_conversion(self):
        if not self.rbxlx_path.get() or not self.output_dir.get():
            messagebox.showerror("Error", "Select the .rbxlx file and the output folder.")
            return

        self.convert_btn.config(state="disabled")
        self.log_box.config(state="normal")
        self.log_box.delete("1.0", tk.END)
        self.log_box.config(state="disabled")

        self.log("Starting conversion...")

        threading.Thread(target=self.run_conversion, daemon=True).start()

    def run_conversion(self):
        try:
            convert_rbxlx(
                self.rbxlx_path.get(),
                self.output_dir.get(),
                self.log
            )
            self.log("🎉 Conversion finished successfully.")
        except Exception:
            self.log("🔥 Fatal error:")
            self.log(traceback.format_exc())
        finally:
            self.convert_btn.config(state="normal")


if __name__ == "__main__":
    App().mainloop()
