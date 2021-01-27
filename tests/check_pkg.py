"""Test availability of required packages."""

import unittest
from pathlib import Path

import pkg_resources

_REQUIREMENTS_PATH = Path(__file__).parent.resolve().with_name("requirements.txt")


class TestRequirements(unittest.TestCase):
    """Test availability of required packages."""

    def test_requirements(self):
        """Test that each required package is available."""
        requirements = pkg_resources.parse_requirements(_REQUIREMENTS_PATH.open())
        for requirement in requirements:
            print(f'Checking {requirement}')
            requirement = str(requirement)
            with self.subTest(requirement=requirement):
                pkg_resources.require(requirement)
