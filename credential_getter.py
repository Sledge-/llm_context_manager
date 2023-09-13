import os

def get_environment_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        print(f"Environment variable '{var_name}' not found")
        return None
