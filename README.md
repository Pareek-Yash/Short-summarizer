# Short-summarizer

The goal of this repo is to compare the results of summarization between `facebook/bart-large-cnn` using transformers pipelines API and training a custom summarizer using a news dataset available on TensorFlow.

## Overview

Text summarization is an important task in natural language processing, which involves condensing a piece of text into a shorter version, retaining the key information. This repository contains two approaches to text summarization:

1. Using a pre-trained model `facebook/bart-large-cnn` with Hugging Face's Transformers library.
2. Training a custom summarization model using a news dataset available through TensorFlow Datasets.

## ***************** Work in Progress *****************
## Getting Started

### Prerequisites

- Python 3.6 or later
- TensorFlow 2.x
- Transformers
- Requests (for fetching text from a remote source)

Install the required libraries using `pip`:

```sh
pip install tensorflow transformers requests
```

### Directory Structure

```
short-summarizer/
│
├── pre_trained_summarizer/
│   ├── pre_trained_summarizer.py    # script for summarization using pre-trained model
│   
├── custom_summarizer/
│   ├── data_preprocessing.py        # script for data preprocessing
│   ├── model.py                     # script defining the custom summarizer model
│   ├── train.py                     # script for training the custom summarizer
│   ├── evaluate.py                  # script for evaluating the custom summarizer
│   
└── README.md
```

## Usage

### Pre-trained Summarizer

Navigate to the `pre_trained_summarizer` directory.

To summarize text using the `facebook/bart-large-cnn` pre-trained model, run:

```sh
python pre_trained_summarizer.py --url <URL_OF_TEXT_FILE>
```

Replace `<URL_OF_TEXT_FILE>` with the URL of the text file you want to summarize.

### Custom Summarizer

Navigate to the `custom_summarizer` directory.

1. **Data Preprocessing**:

   Run `data_preprocessing.py` to download and preprocess the dataset:

   ```sh
   python data_preprocessing.py
   ```

2. **Training**:

   Run `train.py` to train the custom summarization model:

   ```sh
   python train.py
   ```

3. **Evaluation**:

   After training the model, use `evaluate.py` to evaluate it on test data:

   ```sh
   python evaluate.py
   ```

## Comparing Results

After generating summaries using both approaches, you can manually compare the quality of the summaries by reading them. Additionally, you can compute ROUGE scores to quantitatively measure the performance of the summarizers.

## Contributing

Contributions are welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.