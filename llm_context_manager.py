from collections.abc import Iterable
import os
from llm_summarizer import LLMSummarizer

# Defining the entire LLMPrompt class with all modifications
class LLMContextManager:
    def __init__(self, L=10000, section_names=None, section_lengths=None):
        self.L = L  # default maximum length of each section
        self.section_lengths = section_lengths if section_lengths else {}  # custom section lengths
        self.flags = {}  # flags for overflow
        self.llm_summarizer = LLMSummarizer()

        # initializing sections
        self.sections = {}
        if section_names:
            for name in section_names:
                self.sections[name] = ""

    def _get_section_limit(self, section):
        """
        Returns the word limit for a given section.
        """
        return self.section_lengths.get(section, self.L)
    
    def get_section_keys(self):
        return list(self.sections.keys())

    def add_section(self, section, text):
        """
        Adds text to a section without truncation, keeping the full history.
        """
        if section in self.sections:
            self.sections[section] += text
        else:
            raise ValueError(f"Section {section} not found.")

    def get_truncated_context(self):
        """
        Retrieves the truncated context by keeping the most recent text up to the specified limits.
        """
        truncated_context = {}
        for section, content in self.sections.items():
            truncated_content = " ".join(content.split()[-self._get_section_limit(section):])
            truncated_context[section] = truncated_content
        return truncated_context

    def get_summarized_context(self, sections=None):
        """
        Retrieves the summarized context.
        If 'sections' is None, all sections are summarized.
        If 'max_words' is specified, it limits the total number of words in the summary.
        """
        if sections is None:
            sections = list(self.sections.keys())
        elif not isinstance(sections, Iterable):
            sections = [sections]

        summarized_context = {}
        for section in sections:
            content = self.sections.get(section, "")
            summarized_context[section] = self.llm_summarizer.summarize(content)  # Summarize the content
        return summarized_context
    
    @classmethod
    def load_from_directory(cls, dir_path):
        """
        Loads the contents of all text files in a directory into the sections. The key for each section is the filename.
        """
        instance = cls()
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                print(f"loading {file}")
                if file.endswith(".txt"):
                    section_name = os.path.splitext(file)[0]
                    with open(os.path.join(root, file), 'r') as f:
                        instance.sections[section_name] = f.read()
        return instance

def dict_to_text(data_dict):
    """
    Converts a dictionary to a text representation.
    
    Args:
    data_dict (dict): The dictionary to convert to text.
    
    Returns:
    str: A text representation of the dictionary.
    """
    text_list = []
    
    for doc_id, doc_content in data_dict.items():
        doc_text = f"Document ID: {doc_id}\n{doc_content}\n"
        text_list.append(doc_text)
    
    return "\n".join(text_list)

if __name__ == "__main__":
    # Load all files from the 'examples' directory
    llm_context_manager = LLMContextManager.load_from_directory(dir_path='examples')

    # Print out one of the loaded sections
    print(f"Contents of the 'example_section' section: {llm_context_manager.sections.get('doc1', 'Section not found.')}")
    print(f"llm_prompt.get_section_keys(): {llm_context_manager.get_section_keys()}")

    #: Get summarized content:
    summarized_context = llm_context_manager.get_summarized_context()
    print(f"\nsummarized_context: \n {dict_to_text(summarized_context)}")

