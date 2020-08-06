"""Main script for flow control and task execution."""
import os
from settings import config

settings_file = os.path.dirname(config.__file__) + "/settings.yml"

configuration = config.read_settings(settings_file)
print(configuration)


