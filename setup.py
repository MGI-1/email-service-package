from setuptools import setup, find_packages

setup(
    name="email-service",
    version="0.1.1",  # Increment version
    description="Shared email service for Flask applications",
    author="Sameer Rawat",
    author_email="samraw1904@gmail.com",
    packages=find_packages(),
    install_requires=[
        "Flask>=2.0.0",
        "Flask-Mail>=0.9.1",
    ],
    python_requires=">=3.7",
)