# GPT generation client for AI sites

## Supported Sites:

[Venus Chub AI](https://venus.chub.ai)

## About other sites:

- [JanitorAI](https://janitorai.com) only seems to work partially. it's success is never guaranteed. There seem to be issues with authorization, might rework soon.
- [Harpy Chat](https://harpy.chat) Does NOT work at all. There seems to be a completely unfamiliar error occuring during generation on their end and not mine.

## Prerequisites

Python (use 3.10 for guaranteed result) (make sure to install pip alongside)

## Installation of Modules

1. Open a new cmd window
2. Set the current directory to the root of the folder. Comamnd: ```cd "path_to_folder"```
3. type ```pip install -r requirements.txt``` this will install all neccessary modules for you automatically.

## Running the server

1. After the modules are installed, double click the ```app.py``` file.
2. The cmd should look something like this if everything works:
   
   ![CMD_SUCCESS](https://i.imgur.com/kqCpct9.jpg)
3. Copy that URL (it's a local URl, don't worry, it's only accessible from devices in the same network and isn't public)
4. Insert that URL to the AI site ([Venus Chub AI](https://venus.chub.ai) for reference)

   ![INSERT_URL_TO_BAR](https://i.imgur.com/o1qjELe.png)

## Getting the auth code

1. Head to the ``settings`` folder.
2. Double click ``auth.json`` and open it in any text editor. It should look like this (using notepad.exe)

   ![AUTH_JSON_OPENED](https://i.imgur.com/K6VEqbN.png)

3. Copy the contents of the quotes. You should have ``NMPH-874631259`` as your code.

## Inserting the code

1. Insert the code into the box. It should look like this:

   ![CODE_ENTERED_VENUS_AI](https://i.imgur.com/gY73YL0.png)

## Verify 

1. Make sure your settings look like this currently:

   ![TOTAL_SETTINGS_OVERVIEW](https://i.imgur.com/hQIsSnk.png)
   (and don't forget your jailbreak, lol)

## Check Proxy

1. If your settings look alike, press the ``"Check Proxy"`` button. ![CHECK_PROXY_BUTTON](https://i.imgur.com/7L2KqfN.jpg)

2. If everything worked, you should get a green checkmark. ![GREEN_CHECKMARK](https://i.imgur.com/RPlhFQZ.png)

## Choosing a model

1. Thanks to the [g4f module](https://github.com/xtekky/gpt4free), you can use ``gpt-3.5-turbo`` and ``gpt-4-0613`` for ***free.***

2. Select either ``gpt-3.5-turbo`` or ``gpt-4-0613`` from the list: ![CHOOSE_MODEL_GPT](https://i.imgur.com/OyWPJP9.png)

## Finalize

1. Once you've chosen a model, scroll down and press ``Save Settings`` ![SAVE_SETTINGS](https://i.imgur.com/GKxpx5y.jpg)
   
