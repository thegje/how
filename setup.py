from setuptools import setup

setup(
    name="howdo",                     # Package name (must be unique on PyPI)
    version="0.1.0",                # Initial version
    author="thegje",                # Your GitHub username or name
    author_email="thegje@gmail.com", # Your email
    description="A terminal app to query xAI's Grok API",
    long_description=open("README.md").read(),  # Use README as description
    long_description_content_type="text/markdown",  # Markdown format
    url="https://github.com/thegje/how",  # GitHub repo URL
    py_modules=["how"],             # Single module (how.py)
    install_requires=["requests"],  # Dependency
    entry_points={
        "console_scripts": [
            "how = how:main"        # Command 'how' runs how.main()
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.6",        # Minimum Python version
)
