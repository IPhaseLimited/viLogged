import os

from lib.dot_env import DotEnv
DotEnv.read_dotenv('.env')
DB = os.environ.get('DB')

print DB