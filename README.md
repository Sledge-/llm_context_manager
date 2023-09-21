# LLMSummarizer

LLMSummarizer is a Python tool designed to streamline the extraction of specific fields from a batch of legal documents, presenting them in a predefined format. This tool leverages the OpenAI Davinci model to extract the key data points from verbose legal texts, transforming them into digestible summaries. It is designed to be flexible and can be adapted for various future use cases involving efficient data extraction.

## Features

### LLMSummarizer Class

The cornerstone of the tool, it encompasses a prompt and input data, directing the OpenAI Davinci model to extract specific fields from the text based on a "single-shot" pattern.

### Content Manager

A Python class designed to process batches of legal documents through the LLMSummarizer, preparing the data for other applications. It iterates over each section in a dictionary, summarizes the values, and returns the results.

### LLMAnalyzer Class

A tool that leverages OpenAI's newer function-calling feature to instruct the system to extract debt amounts and compute their sum, facilitating this task based on the contextual information provided.

## Getting Started

To get started with the LLMSummarizer project, you will need to have Python installed on your system. Follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Install the necessary Python packages by running the following command:

pip install -r requirements.txt


### Usage

## To use the LLMSummarizer tool, follow these steps:

1. Import the necessary classes and functions from your Python script. For example:
```python
from llm_summarizer import LLMSummarizer
from utils import count_words_in_values
```

## Output
Upon running the code on a document, you will receive a condensed version highlighting the key data points, facilitating a more digestible summary of legal texts.

## Contributions
Feel free to contribute to the LLMSummarizer project by opening a pull request with your changes.

## License
This project is open-source and available under the MIT License.

## Contact
If you have any questions, issues, or feedback, please open an issue on the GitHub repository.

## Acknowledgements
Special thanks to OpenAI for providing the Davinci model, which made this project possible.





