import os
import unittest
import tempfile
from nested_env_manager.nested_env_manager import NestedEnvManager

class TestNestedEnvManager(unittest.TestCase):
    def setUp(self):
        self.nem = NestedEnvManager()
        self.main_env_requirements = ["requests"]
        self.sub_env_requirements = ["numpy"]

        self.main_env_path = tempfile.mkdtemp()
        self.sub_env_path = tempfile.mkdtemp()

    def test_create_main_env(self):
        self.nem.create_main_env(self.main_env_requirements, self.main_env_path)
        self.assertTrue(os.path.exists(self.main_env_path))

    def test_create_sub_env(self):
        self.nem.create_main_env(self.main_env_requirements, self.main_env_path)
        self.nem.create_sub_env(self.sub_env_requirements, self.sub_env_path)
        self.assertTrue(os.path.exists(self.sub_env_path))

    def test_inheritance_from_main_env(self):
        self.nem.create_main_env(self.main_env_requirements, self.main_env_path)
        self.nem.create_sub_env(self.sub_env_requirements, self.sub_env_path)
        # Add your test for checking if the main environment packages are accessible in the sub-environment.

if __name__ == '__main__':
    unittest.main()
