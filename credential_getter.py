import os

def get_environment_variable(var_name):
    '''
    1a. In Linux/Mac OS:
    export OPENAI_KEY="my_super_secret_key"

    1b. In Windows:
    set OPENAI_KEY="my_super_secret_key"

    2. In llm_summarizer.py:
    openai.api_key = get_environment_variable("OPENAI_KEY")
    '''
    try:
        return os.environ[var_name]
    except KeyError:
        print(f"Environment variable '{var_name}' not found")
        return None
