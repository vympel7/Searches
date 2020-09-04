from setuptools import setup

version = "0.0"

setup(
    name = "Search Algorithms",
    version=version,
    description="Search algorithms to find a target within a sequence",
    author="Vympel",
    packages=["algs"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities"
    ],
    python_requires=">=3.5",
)