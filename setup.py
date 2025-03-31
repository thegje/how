from setuptools import setup

setup(
    name="howdo",                     
    version="0.1.1",                
    author="thegje",                 
    author_email="thegje@gmail.com", 
    description="A terminal app to query xAI's Grok API",
    long_description=open("README.md").read(),  
    long_description_content_type="text/markdown",  
    url="https://github.com/thegje/how",  
    py_modules=["how"],             
    install_requires=["requests"],   
    entry_points={
        "console_scripts": [
            "how = how:main"       
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.6",        
)
