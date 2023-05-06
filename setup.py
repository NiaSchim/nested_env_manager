from setuptools import setup, find_packages

setup(
    name="nested_env_manager",
    version="1.0.0",
    description="A Python package to manage nested virtual environments",
    author="Nia Schimnoski aka Niaschim",
    author_email="theschim02@gmail.com",
    url="https://github.com/NiaSchim/nested_env_manager",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    license="BSD-3-Clause",
)
