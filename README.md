Text Summarization Tool
This repository contains a simple text summarization tool built with Python using the Hugging Face transformers library and Tkinter for the graphical user interface (GUI). The tool allows you to input any text and get a summarized version using the Facebook BART model.

> Features
a. Text Summarization: The tool uses the BART model (facebook/bart-large-cnn) to summarize input text.
b. GUI Interface: Built with Tkinter, making it easy to input text and view summarized output.
c. Dynamic Summarization: Adjusts the summarization parameters based on the length of the input text.

> Requirements
a. Python 3.x
b. Install the necessary libraries by running:
   pip install tkinter transformers textwrap
c. transformers library is used for the text summarization model.

> Usage
a. Clone the repository: Clone this repository to your local machine using:
git clone https://github.com/jagveersandhu/text-summarization-tool.git
cd text-summarization-tool

b. Run the tool: Simply run the Python script to start the tool:
python summarization_tool.py
Input: Type or paste your text into the text box.
Summarize: Click on the "Summarize" button to generate the summary.
Output: The summary will appear in the output box below.

> Code Explanation
a.  Summarization: The tool uses the Hugging Face transformers library to load the facebook/bart-large-cnn model for text summarization.
The summarize_input_text function handles text input and adjusts the summarization parameters like max_length and min_length based on the length of the input.
Long texts are split into chunks to fit within the model's token limit.

b. GUI: The GUI is built using the Tkinter library, which allows for easy interaction with the tool. It includes:
A text box for entering text.
A button to trigger the summarization.
A text box to display the summarized output.

> Example
Input:
Artificial Intelligence (AI) refers to the simulation of human intelligence processes by machines, especially computer systems. These processes include learning, reasoning, and self-correction. AI has evolved significantly over the years, from basic rule-based systems to advanced machine learning algorithms capable of performing complex tasks such as image recognition, natural language processing, and autonomous driving.

Output:
Artificial Intelligence (AI) refers to the simulation of human intelligence processes by machines. These processes include learning, reasoning, and self-correction. AI has evolved from basic rule-based systems to advanced machine learning algorithms.

> Contributing
If you'd like to contribute to this project, feel free to fork the repository and create a pull request. Bug reports and feature requests are also welcome!
