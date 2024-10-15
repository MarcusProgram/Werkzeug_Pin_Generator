# Werkzeug_Pin_Generator
[![Python 3.12](https://img.shields.io/badge/Python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/)<br>
This is an example of operation from LFI to RCE if Werkzeug c debug=true is installed on the server

___

## Screenshots
<img src='https://github.com/MarcusProgram/Werkzeug_Pin_Generator/blob/main/Screenshots/swappy-20241010-142003.png?raw=true'/>
<img src='https://github.com/MarcusProgram/Werkzeug_Pin_Generator/blob/main/Screenshots/swappy-20241010-143009.png?raw=true' widht="200px" height="300px"/>

## Installation

Clone the git with `git clone`:
```bash
git clone https://github.com/MarcusProgram/Werkzeug_Pin_Generator.git
```

Then navigate to the file folder using `cd`:
```bash
cd Werkzeug_Pin_Generator/Exploit
```

Next, install all the necessary Python dependencies from the file `requirements.txt`:

```bash
sudo pip install -r requirements.txt
```

And then you enjoy the script:

```bash
sudo python3 main.py
```

## Up Flask Server
This is the server to test this exploit

Navigate to the folder with the file using `cd`:
```bash
cd Werkzeug_Pin_Generator/Flask
```

Next, install all the necessary Python dependencies from the file `requirements.txt`:

```bash
sudo pip install -r requirements.txt
```

And then we run the Python file and go to the server we were kindly given:

```bash
sudo python3 main.py
```
