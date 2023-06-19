import requests
from transformers import pipeline

# URL of the text file
url = "https://pareek-yash.github.io/files/sample_corpus.txt"

# Fetch the content of the text file
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Split the content into lines and exclude the first line (heading)
    lines = response.text.split('\n')
    article_text = '\n'.join(lines[1:])
    
    # Initialize the summarization pipeline with the BART model
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    # Summarize the text
    summary = summarizer(article_text, max_length=100, min_length=75, do_sample=False)

    # Output the summarized text
    print(summary[0]['summary_text'])
else:
    print("Failed to retrieve the text file.")