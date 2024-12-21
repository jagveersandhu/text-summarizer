import tkinter as tk
from tkinter import messagebox
from transformers import pipeline
import textwrap

# Initialize the summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Function to summarize the input text
def summarize_input_text():
    input_text = input_text_box.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showerror("Error", "Please enter some text to summarize.")
        return

    try:
        # Adjust `max_length` based on input length
        input_length = len(input_text.split())
        if input_length < 50:
            max_length = max(10, input_length // 2)  # Ensure it's less than input length
            min_length = max(5, input_length // 4)  # Avoid very short outputs
        else:
            max_length = 150
            min_length = 50

        # Split long texts into chunks
        max_token_limit = 1024  # Maximum token limit for the model
        wrapped_text = textwrap.wrap(input_text, width=max_token_limit)
        
        summaries = []
        for chunk in wrapped_text:
            summary = summarizer(chunk, max_length=max_length, min_length=min_length, do_sample=False)
            summaries.append(summary[0]['summary_text'])

        # Combine all summaries into a final output
        final_summary = ' '.join(summaries)
        output_text_box.delete("1.0", tk.END)
        output_text_box.insert(tk.END, final_summary)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during summarization: {e}")

# Create the GUI window
root = tk.Tk()
root.title("Text Summarization Tool")

# Input text label and box
tk.Label(root, text="Enter text to summarize:").pack(pady=10)
input_text_box = tk.Text(root, height=10, width=60, wrap=tk.WORD)
input_text_box.pack(pady=5)

# Summarize button
summarize_button = tk.Button(root, text="Summarize", command=summarize_input_text)
summarize_button.pack(pady=10)

# Output text label and box
tk.Label(root, text="Summary:").pack(pady=10)
output_text_box = tk.Text(root, height=10, width=60, wrap=tk.WORD)
output_text_box.pack(pady=5)

# Run the GUI loop
root.mainloop()
