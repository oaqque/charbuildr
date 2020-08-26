# charbuildr
charbuildr is a project to build a chatbot that is able to adopt personality traits from a given corpus and generate responses accordingly. I hope this will allow game developers to build interactive characters with less manual story writing. 

## Setup and Installation
To setup your python environment, dependencies can be found in `requirements.txt` or a virtual environment may be used instead. 

To setup a virtual environment in Python3 : 
`python3 -m venv [name_of_dir]`

Activate your virtual environment : 
`source [name_of_dir]/bin/activate`

Install dependencies in your virtual environment : 
`pip3 install -r requirements.txt`

If you want to leave this environment to work on another project : 
`deactivate`

For more information on virtual environments see [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/). 

In order to setup the Azure Endpoint see [here](https://www.notion.so/willye/Azure-Text-Analytics-b2066f9e1623491ab253488820660bd7).

## Usage
To start the chatbot :  `python3 chatbot_main.py`
