from pathlib import Path
from setuptools import find_namespace_packages, setup

# Load packages from requirements.txt
BASE_DIR = Path(__file__).parent
with open(Path(BASE_DIR, "requirements.txt"), "r") as file:
    required_packages = [ln.strip() for ln in file.readlines()]

# Define our package
setup(
    name="sentiment_analysis",
    version=0.1,
    description="Classify tweets.",
    author="Mohsin and Momil",
    author_email="momilijaz@gmail.com, mohsin.tariq10@gmail.com",
    python_requires=">=3.10",
    packages=find_namespace_packages(),
    install_requires=[required_packages],
)
