# How

`how` is a simple Linux terminal application that lets you query an AI chatbot (powered by xAI's Grok) and get plain text answers directly in your terminal. Ask anything—like how to find file sizes in a directory—and get a concise response.

Example:
```bash
how --q "find size of files in directory and list by file size"
```

Response:
```bash
du -sh | sort -h
```

## **Features**

* Lightweight and dependency-minimal (only requires requests).  
* Configurable via a local file (\~/.how\_config) for your xAI API key.  
* Installable system-wide with a simple setup process.
 
## **Installation**

**1. Install from PyPI**  
 
```bash
pip3 install how --user
```
   
This installs how to \~/.local/bin, which should be in your PATH. If not, add it:  
```bash
export PATH="$HOME/.local/bin:$PATH"` 
```

2. **Set Your API Key** Configure your xAI API key:   
```bash
how --key "your-xai-api-key-here"
```
This saves the key to \~/.how\_config.

## **Usage**

* **Ask a Question**   
```bash
how --q "your question here"
```
Example:   
```bash
how --q "how do I list all running processes?"
```
Output:   
```bash
"Use this command: ps aux"
```

* **Set or Update API Key**   
```bash
how --key "new-xai-api-key"
```

* **Check Help**   
```bash
how --help
```

## **Troubleshooting**

* **"No API key found" Error** Run how \--key "\<your-api-key\>" to set your key.  
* **403 Forbidden Error** Verify your API key is valid and has access to the grok-2-latest model in the xAI Console. Regenerate it if needed.  
* **Command Not Found** Ensure \~/.local/bin is in your PATH (see installation step 3).  
* **ModuleNotFoundError: No module named 'setuptools'** Install it with pip3 install setuptools.

## **Uninstallation**

Remove the application:

bash  
```bash
pip3 uninstall how
```

Delete the config file (optional):

bash  
```bash
rm ~/.how_config
```

## **Contributing**

Feel free to fork this project, submit issues, or send pull requests. Ideas for improvements:

* Add response caching.  
* Support additional AI models.  
* Enhance error messages.

## **License**

This project is open-source under no license.

## **Credits**

Built by Gregory Ellis.
 

