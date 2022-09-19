## Install Label Studio
1. Five ways of installation (Local/Cloud)
    - Install with pip
    - Install with Docker
    - Install on Ubuntu
    - Install from source
    - Install with Anaconda

2. I will show the steps to install with pip on Windows 10.
    - [Refer here](https://labelstud.io/guide/install.html) if you want to try other way of installation

Requirement: Python 3.6+ <br>
Check way to install Python: https://techdecodetutorials.com/how-to-install-python-on-windows-11/

### Create Python Virtual Environment

1. Open your terminal/command prompt and run to install virtualenv package.
```
pip install virtualenv
```

2. To create a virtual environment, you must specify a path. For example to create one in the local directory called ‘env’.
```
virtualenv env
```
_Snapshot of directory of virtual environment_ <br>
<img src="https://github.com/teohsinyee/resume-parsing/blob/main/images/virtualenv.png" width="550" height="250">

3. Activate virtual environment in directory ‘env’.
```
Scripts\activate
```
_After activation_ <br>
<img src="https://github.com/teohsinyee/resume-parsing/blob/main/images/activate.png" width="450" height="250">

### Install Label Studio in Virtual Environment

4. Check if the virtual environment has been activated before running the command below.
```
python -m pip install label-studio
```

5. Start server using the command below.
```
label-studio
```
The default web browser opens automatically at http://localhost:8080 with Label Studio.

_Snapshot after running Label Studio successfully_ <br>
<img src="https://github.com/teohsinyee/resume-parsing/blob/main/images/loginls.png" width="450" height="250">


(Repeat steps 3 & 5 everytime when you want to use Label Studio! Make sure change directory to the virtual environment)

Extra notes:
1. Sign up Label Studio if this is your first time use.
2. You may [raise a ticket in Github](https://github.com/heartexlabs/label-studio/issues) if you have any questions/issues. 
3. If required faster response, you can [join the Slack community](https://label-studio.slack.com/ssb/redirect).
