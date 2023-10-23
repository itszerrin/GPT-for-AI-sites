# GPT generation client for AI sites

## Brief introduction

**10/23/2023: Currently not working ⚠️**

This application uses LLM wrappers but uses Flask to host the LLM locally and make it usable within other AI sites.

I do not condone acts which go against the LLM provider's TOS.

## Supported Sites:

- Any site which uses the ``"/chat/completions"`` route for generation

## Prerequisites

Python (**ONLY 3.10 SUPPORTED**)

Have unzipped the directory to a folder

## Installation of Modules

1. Run the ``install_requirements.bat`` file. This will auto-install everything for you. (simply double-click it)

2. Alternatively, open ``cmd.exe`` in the directory where all the files are and write ``pip3.10 install -r requirements.txt``
   
   ![INSTALL_MODULES_CMD](https://i.imgur.com/HiIIOQN.jpg)

## Running the server

1. After the modules are installed, double click the ```app.py``` file.

2. Alternatively, you can double click the ``start.bat`` file to run the server.
3. The cmd should look something like this if everything works:
   
   ![CMD_SUCCESS](https://i.imgur.com/kqCpct9.jpg)
4. In the API settings, select ``OpenAI`` and ``Reverse Proxy``
5. Copy that URL (it's a local URL, don't worry, it's only accessible from devices in the same network and isn't public)
6. Insert that URL to the AI site ([Venus Chub AI](https://venus.chub.ai) for reference)

   ![INSERT_URL_TO_BAR](https://i.imgur.com/o1qjELe.png)

## Check Proxy

1. If your settings look alike, press the ``"Check Proxy"`` button. ![CHECK_PROXY_BUTTON](https://i.imgur.com/7L2KqfN.jpg)

2. If everything worked, you should get a green checkmark.

 ![GREEN_CHECKMARK](https://i.imgur.com/RPlhFQZ.png)

## Choosing a model

1. Thanks to the [vercel_ai module](https://github.com/ading2210/vercel-llm-api), you may use any model for ***free.***

2. Select either model from the list: ![CHOOSE_MODEL_GPT](https://i.imgur.com/ePKD0lR.png)

## Finalize

1. Once you've chosen a model, scroll down and press ``Save Settings``

 ![SAVE_SETTINGS](https://i.imgur.com/GKxpx5y.jpg)

## For mobile users

1. You dont need to install anything
   
2. Simply head to this [google colab link](https://colab.research.google.com/drive/1-9EEf1oaEo2IT7COtBVbpE7iKmRUxcQP#scrollTo=gu9v0Iei9vE-) (also works on pc)

## Some more information

1. This does only **partially** support the Impersonation feature

2. No, this does not utilize your pc's resources as a LLM.

3. This supports **Venus Chub's** group chat feature.

4. I have no influence over the ``vercel_ai`` module and any errors that occur from it are unfixable by me.

5. The ``Chat Memory`` function does not seem to work at the moment.

6. The ``Context Length`` is always at the model's max supported amount.

7. If you get an error about "utf-8 decoding", simply generate again. No need to restart the server.

## Copyright

Recentaly/GPT-for-AI-sites: A hosted wrapper for AI sites.
Copyright (C) 2023 Recentaly

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Developed with [vercel_ai module](https://github.com/ading2210/vercel-llm-api)


