import os
import sys
import subprocess

class NestedEnvManager:
    def __init__(self):
        self.bin_folder = "Scripts" if sys.platform == "win32" else "bin"

    def _run_command(self, command):
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if process.returncode != 0:
            print(f"Error executing command: {command}")
            print(stderr.decode("utf-8"))
        return stdout.decode("utf-8")

    def create_main_env(self, requirements, main_env_path):
        self.main_env_path = main_env_path
        os.makedirs(self.main_env_path, exist_ok=True)

        # Create and activate main virtual environment
        self._run_command(f"python -m venv {self.main_env_path}")

        # Install requirements
        for req in requirements:
            self._run_command(f"{os.path.join(self.main_env_path, self.bin_folder, 'pip')} install {req}")

        # Create virtual_root directory
        self.virtual_root = os.path.join(self.main_env_path, "virtual_root")
        os.makedirs(self.virtual_root, exist_ok=True)

    def create_sub_env(self, requirements, sub_env_path):
        os.makedirs(sub_env_path, exist_ok=True)

        # Create and activate sub virtual environment
        self._run_command(f"python -m venv {sub_env_path}")

        # Link main environment packages
        main_site_packages = os.path.join(self.main_env_path, "lib", f"python{sys.version_info.major}.{sys.version_info.minor}", "site-packages")
        sub_site_packages = os.path.join(sub_env_path, "lib", f"python{sys.version_info.major}.{sys.version_info.minor}", "site-packages")
        os.makedirs(sub_site_packages, exist_ok=True)  # Add this line
        with open(os.path.join(sub_site_packages, "_main_packages.pth"), "w") as pth_file:
            pth_file.write(main_site_packages.replace('\\', '\\\\'))

        # Install sub-environment specific requirements
        for req in requirements:
            self._run_command(f"{os.path.join(sub_env_path, self.bin_folder, 'pip')} install {req}")

