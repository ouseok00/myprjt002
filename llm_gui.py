import tkinter as tk
from tkinter import scrolledtext
from transformers import pipeline

# Initialize the LLM model
model = pipeline('text-generation', model='gpt2')

# Function to generate text
def generate_text():
    input_text = input_text_box.get("1.0", tk.END).strip()
    if input_text:
        output = model(input_text, max_length=100, num_return_sequences=1)
        output_text_box.config(state=tk.NORMAL)
        output_text_box.delete("1.0", tk.END)
        output_text_box.insert(tk.END, output[0]['generated_text'])
        output_text_box.config(state=tk.DISABLED)

# Create the main window
window = tk.Tk()
window.title("LLM Text Generator")

# Create and place the input text box
input_text_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=10)
input_text_box.grid(row=0, column=0, padx=10, pady=10)

# Create and place the generate button
generate_button = tk.Button(window, text="Generate Text", command=generate_text)
generate_button.grid(row=1, column=0, padx=10, pady=10)

# Create and place the output text box
output_text_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=10, state=tk.DISABLED)
output_text_box.grid(row=2, column=0, padx=10, pady=10)

# Start the main loop
window.mainloop()
