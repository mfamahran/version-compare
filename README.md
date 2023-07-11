# Version Compare

Given 2 versions, this CLI tool will will compare them and do the following:
- version1 > version2 return 1
- version1 < version2 return -1
- otherwise return 0


## Installation
In the project directory execute 
```sh
python -m venv ./venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

## Features

- Compare 2 versions and display desired result

# Usage
Compare the 2 versions the following command executed within the venv shell
```sh
python -m src compare
```
#### Parameters:
- ```-v1 / --version1``` for file path
- ```-v2 / --version2``` for threshold configuration

To run tests
```sh
python -m pytest tests/
```
You can execute the command without providing any parameters and you will be prompted to enter the required parameters or leave as is/
## Improvements
- Input validation for versions to ensure that it won't accept other inputs
- Project structure could receive minor changes in case more commands are going to be added for readability and maintainability
- Typer is being used which is a very powerful package that can make user interactions with the CLI much better in case it's requried