import distutils.text_file
from pathlib import Path
import unittest

import pkg_resources


#REQUIREMENTS_PATH = Path(__file__).parents[1].with_name('requirements.in')
REQUIREMENTS_PATH = "requirements.txt"

def test_requirements():
    """Test that each requirement is available."""
    # Ref: https://stackoverflow.com/a/45474387/
    requirements = distutils.text_file.TextFile(filename=REQUIREMENTS_PATH).readlines()
    for requirement in requirements:
        pkg_resources.require(requirement)


if __name__ == '__main__':
    test_requirements()