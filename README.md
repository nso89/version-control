# version-control
A quick and simple version control system

* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Running the Script](#running-the-script)
* [Configuration](#configuration)

#### <a name="prerequisites"></a>Prerequisites
1. A completed install of `Python 3.x`.
2. Under your `USERPROFILE`, the folder we want to copy.

**Example**:
```
C:\Users\nso89\Documents\Books\A Gentle Introduction to Python\0.0.0\Book.odt
```
#### <a name="setup"></a>Setup
1. Under your `USERPROFILE`, extract the `version-control.zip`

#### <a name="running-the-script"></a>Running the Script
1. Open `cmd.exe` and change the directory to the `version-control` folder.
2. Start the `python main.py`.
3. It asks you for the `folder` name and `version #`

**Example**:
```
Folder: Documents\Books\A Gentle Introduction to Python\0.0.0\Book.odt
Version #: 0.0.1

Copying C:\Users\nso89\Documents\Books\A Gentle Introduction to Python\0.0.0 to 
        C:\Users\nso89\Documents\Books\A Gentle Introduction to Python\0.0.1
```

#### <a name="configuration"></a>Configuration
If you need to change the `source` or `destination` folder:
1. Open the `main.py` script in any text editor.
2. Locate the `list of variable names` variables.

**Example**:
```python
# Insert code sample here.
```
3. When you finish changing the variables, save and close the editor.
