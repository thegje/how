# How

`how` is a simple Linux terminal application that lets you query an AI chatbot (powered by xAI's Grok) and get plain text answers directly in your terminal. Ask anything—like how to find file sizes in a directory—and get a concise response.

Example:
```bash
how --q "find size of files in directory and list by file size"
```

## **Features**

* Lightweight and dependency-minimal (only requires requests).  
* Configurable via a local file (\~/.how\_config) for your xAI API key.  
* Installable system-wide with a simple setup process.

## **Prerequisites**

* **Python 3**: Available on most Linux systems (check with python3 \--version).  
* **pip**: For installing dependencies (install with sudo apt-get install python3-pip on Debian/Ubuntu or equivalent).  
* **xAI API Key**: Sign up at [xAI](https://x.ai) and generate a key from the [xAI Console API Keys Page](https://console.x.ai).

## **Installation**

**Clone or Download the Repository**  
 bash  
CollapseWrapCopy  
`git clone <repository-url>`

1. `cd how`  
    Or download and extract the zip file.  
2. **Install Dependencies** Install setuptools if not already present:  
    bash  
   CollapseWrapCopy  
   `pip3 install setuptools`

3. **Install the Application** Run the setup script to install how for your user:  
    bash  
   CollapseWrapCopy  
   `python3 setup.py install --user`  
    This installs how to \~/.local/bin, which should be in your PATH. If not, add it:  
    bash  
   CollapseWrapCopy  
   `export PATH="$HOME/.local/bin:$PATH"`  
    Make it permanent by adding that line to \~/.bashrc or \~/.zshrc.  
4. **Set Your API Key** Configure your xAI API key:  
    bash  
   CollapseWrapCopy  
   `how --key "your-xai-api-key-here"`  
    This saves the key to \~/.how\_config.

## **Usage**

* **Ask a Question**  
   bash  
  CollapseWrapCopy  
  `how --q "your question here"`  
   Example:  
   bash  
  CollapseWrapCopy  
  `how --q "how do I list all running processes?"`  
   Output:  
   text  
  CollapseWrapCopy  
  `"Use this command: ps aux"`

* **Set or Update API Key**  
   bash  
  CollapseWrapCopy  
  `how --key "new-xai-api-key"`

* **Check Help**  
   bash  
  CollapseWrapCopy  
  `how --help`

## **Troubleshooting**

* **"No API key found" Error** Run how \--key "\<your-api-key\>" to set your key.  
* **403 Forbidden Error** Verify your API key is valid and has access to the grok-2-latest model in the xAI Console. Regenerate it if needed.  
* **Command Not Found** Ensure \~/.local/bin is in your PATH (see installation step 3).  
* **ModuleNotFoundError: No module named 'setuptools'** Install it with pip3 install setuptools.

## **Uninstallation**

Remove the application:

bash  
CollapseWrapCopy  
`pip3 uninstall how`

Delete the config file (optional):

bash  
CollapseWrapCopy  
`rm ~/.how_config`

## **Contributing**

Feel free to fork this project, submit issues, or send pull requests. Ideas for improvements:

* Add response caching.  
* Support additional AI models.  
* Enhance error messages.

## **License**

This project is open-source under the MIT License (or specify your preferred license).

## **Credits**

Built with ❤️ by Gregory Ellis using xAI’s Grok API.
 

