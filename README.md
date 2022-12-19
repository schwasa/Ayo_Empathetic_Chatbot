# Ayo_Empathetic_Chatbot
This is the empathetic chatbot version used within my Masters Thesis. For further details and explanations I refer to my Master Thesis.

## Installation & Configuration

Here are the simple steps that you can follow to use a template:

* Create new folder/directory, install python and create virtual environment

    ```
    mkdir newfolder
    cd newfolder
    sudo apt install python3-venv
    python3 -m venv ./venv
    source ./venv/bin/activate
    ```
    
* Install RASA (https://rasa.com/docs/rasa/installation/installing-rasa-open-source)

    ```
    python -m pip install --upgrade pip rasa
    ```
* Initialize RASA within your project_directory by running command rasa init

    ```
    rasa init
    ```
    
* Replace the files in the project_directory with the ones found in this repository
* Install all the dependencies
* Train the bot with command rasa train

    ```
    rasa train
    ```
* OPTIONAL for empathetic chatbot: If you find a file called actions.py in your template directory, run this command in a new terminal rasa run actions

    ```
    rasa run actions
    ```
* Start talking to the bot in terminal with command rasa shell
