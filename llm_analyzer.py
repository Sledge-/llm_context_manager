import openai
from credential_getter import get_environment_variable
import json
import ast
from utils import parse_string_to_list

openai.api_key = get_environment_variable("OPENAI_KEY")

FUNCTIONS = [
    {
        "name": "compute_total_debt",
        "description": "Sums up the total debt from a list of numbers.",
        "parameters": {
            "type": "object",
            "properties": {
                "debts": {
                    "type": "array",
                    "items": {
                        "type": "integer"
                    },
                    "minItems": 1,
                    "maxItems": 50,
                    "description": "Should be an array of numbers.  The function will read in the array and sum the numbers.",
                },
            },
            "required": ["debts"],
        },
    },
]

class LLMAnalyzer():
    def __init__(self):
        with open('config.json', 'r') as file:
            self.config = json.load(file)
        self.prompt = self.config['compute_total_debt']
        print(f"self.prompt: {self.prompt}")    

    def do_analysis(self, input_text):
        #: Via OpenAI ChatCompletion API
        messages = [
            {"role": "system", "content": self.prompt},
            {"role": "user", "content": input_text}
        ]
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            temperature=0,
            functions=FUNCTIONS,
            function_call={f"name": "compute_total_debt"}
        )
        full_message = response["choices"][0]
        print(f"full_message: {full_message}")
        function_call = full_message
        return function_call
    

def extract_args(s):
    '''
    '''
    print(f"s: {s}")
    print(f"type(s): {type(s)}")
    
    corrected_s = s.replace('"{', '{').replace('}"', '}').replace('\\"', '"').strip()

    # Now, let's attempt to parse the corrected string
    outer_dict = json.loads(corrected_s)

    # Extract the direction and num_steps values
    debts = outer_dict["debts"]

    return debts

if __name__ == "__main__":
    from termcolor import colored
    from llm_context_manager import LLMContextManager, dict_to_text
    llm_context_manager = LLMContextManager()
    llm_analyzer = LLMAnalyzer()

    llm_context_manager = LLMContextManager.load_from_directory(dir_path='examples')
    #: Get summarized content:
    summarized_context = dict_to_text(llm_context_manager.get_summarized_context())
    print(colored(f"\nsummarized_context: \n {summarized_context}","blue"))

    function_call = llm_analyzer.do_analysis(summarized_context)
    print(colored(f"function_call: {function_call}", "green"))

    function_args = function_call['message']['function_call']['arguments']
    args = extract_args(function_args)
    args = parse_string_to_list(args)

    print(type(args))
    print(colored(f"args: {args}", "red"))

    final_result = sum(args)
    print(f"final_result: {final_result}")
    
