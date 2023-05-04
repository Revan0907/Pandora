from setuptools import setup, find_packages


setup (
    name             = "pandora",
    version          = "1.0",
    description      = "ML Chatbot for mental health support",
    packages         = find_packages(),
    install_requires = ["gunicorn"],
)
