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
C:\Users\nso89\Documents\Books\A Gentle Introduction to Python\0.0.1\Book.odt
```
#### <a name="setup"></a>Setup
1. Under your `USERPROFILE`, extract the `version-control.zip`

#### <a name="running-the-script"></a>Running the Script
1. Open `cmd.exe` and change the directory to the `version-control` folder.
2. Start the `main.py` script.

**Example**:
```
C:\Users\nso89>python main.py
```

4. It asks you for the `folder` name and `version #`

**Example**:
```
Folder: Documents\Books\A Gentle Introduction to Python\0.0.1\Book.odt
Version #: 0.0.1

Source: C:\Users\nso89\Documents\Books\A Gentle Introduction to Python\0.0.1 to 
Destination: C:\Users\nso89\Documents\Books\A Gentle Introduction to Python\0.0.2
```

#### <a name="configuration"></a>Configuration
If you need to change the `source` folder:
1. Open the `main.py` script in any text editor.
2. Locate the `source` variable.

**Example**:
```python
source = Path.home()
```
3. When you finish changing the variable, save and close the editor.
