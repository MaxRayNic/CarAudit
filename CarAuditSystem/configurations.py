import importlib
import os

flask_env_name = os.getenv('FLASK_ENV', 'base')

config_file_name = f'config.{flask_env_name.strip()}'
print(config_file_name)
settings = importlib.import_module(config_file_name)
