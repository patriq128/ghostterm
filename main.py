import tkinter as tk
import subprocess
import re
import threading
import os

spinner_chars = "⣾⣽⣻⢿⣟⡿⣯⣷⣶⣤⣄"
spinner_regex = re.compile(f"[{spinner_chars}]")

speach = True

root = tk.Tk()
root.geometry("400x200+500+0")
root.attributes("-topmost", True)
root.configure(bg="black")

output = tk.Text(root, height=10, bg="black", fg="white", insertbackground="white", borderwidth=0)
output.pack(fill="both")

entry = tk.Entry(root, bg="black", fg="#c46c6c", insertbackground="#c46c6c", borderwidth=0)
entry.pack(fill="x")

# FARBY
output.tag_config("user", foreground="#ff5555")
output.tag_config("bot", foreground="#50fa7b")

def run_tgpt(text):

    if text.startswith("-s "):
        text = text[3:]
        cmd = ["tgpt", "-s", text]
    else:
        cmd = ["tgpt", text]

    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    while True:
        line = process.stdout.readline()
        if not line:
            break

        if not spinner_regex.search(line):
            cleaned = line.strip()
            if cleaned:
                output.insert(tk.END, ">> ", "bot")
                output.insert(tk.END, cleaned + "\n")
                output.see(tk.END)

                if speach:
                    os.system(f'espeak "{cleaned}"')

    process.wait()

    if text.lower() in ("exit", "quit"):
        root.quit()

def send(event=None):
    text = entry.get()
    if not text:
        return

    output.insert(tk.END, "> ", "user")
    output.insert(tk.END, text + "\n")

    entry.delete(0, tk.END)

    threading.Thread(target=run_tgpt, args=(text,), daemon=True).start()

entry.bind("<Return>", send)

print("Welcome Sir")

root.mainloop()