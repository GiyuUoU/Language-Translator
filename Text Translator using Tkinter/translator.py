
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from googletrans import Translator, LANGUAGES

# Load language names
languages = {code: name.title() for code, name in LANGUAGES.items()}

# Function to translate text
def translate_text():
    text = input_text.get("1.0", tk.END).strip()
    target_lang = lang_combo.get()

    if not text:
        messagebox.showwarning("Warning", "Please enter text to translate.")
        return

    target_code = next((code for code, name in languages.items() if name == target_lang), None)
    
    if target_code:
        translator = Translator()
        translation = translator.translate(text, dest=target_code)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translation.text)
    else:
        messagebox.showerror("Error", "Invalid language selection.")

# Create main window
root = tk.Tk()
root.title("Translator")
root.geometry("450x500")
root.resizable(False, False)

# Load and display the logo
try:
    img = Image.open("Python projects/Google Translator.png").resize((80, 80))
    logo = ImageTk.PhotoImage(img)
    tk.Label(root, image=logo).pack(pady=5)
except:
    pass  # Skip if image not found

# Title
ttk.Label(root, text="Language Translator", font=("Arial", 14, "bold")).pack(pady=5)

# Input text box
input_text = tk.Text(root, height=5, width=50)
input_text.pack(pady=5)

# Language selection
ttk.Label(root, text="Select Target Language:").pack()
lang_combo = ttk.Combobox(root, values=list(languages.values()), state="readonly", width=25)
lang_combo.set("Hindi")  # Default selection
lang_combo.pack(pady=5)

# Translate button
ttk.Button(root, text="Translate", command=translate_text).pack(pady=10)

# Output text box
ttk.Label(root, text="Translated Text:").pack()
output_text = tk.Text(root, height=5, width=50)
output_text.pack(pady=5)

# Run application
root.mainloop()
