# Cryptocurrency display panel from Tidex API
Display panel to see sell, buy and volume values of Ethereum and Bitcoin cryptocurrencies.
Additional, it contains a tutorial of configuration and use.

## Tutorial
This tutorial was designed to be done on a personal computer and their steps require using command-line interpreter, text editor, etc.

### Required software
* Command-line interpreter like Terminal, PowerShell, etc.
* Text editor like Notepad++, Visual Studio Code, etc.

### 1. Install Python
1.1 Install stable/latest version of [Python 3](https://www.python.org/downloads/).

1.2 Verify Python installation.
> Command-line
```
py -3 --version
```
```
pip3 --version
```

1.3 Install and verify PLY library.
> Command-line
```
pip3 install ply
```
```
pip3 show ply
```

> If you can't see the library version on Windows, launch a PowerShell window as an administrator and enter this following command. Later, try again to verify.
> Command-line
```
Set-ExecutionPolicy Unrestricted
```

### 2. Run the apps
2.1 Run the app locally.
> Command-line
```
python frontend.py
```

2.2 See results of executions of app.
(Some here!)

2.3 Stop the apps.<br>
Close the app closing the Tkinter window.