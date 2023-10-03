# GPT generation client for AI sites

## Brief introduction

This application uses LLM wrappers but uses Flask to host the LLM locally and make it usable within other AI sites.

I do not condone acts which go against the LLM provider's TOS.

## Supported Sites:

[Venus Chub AI](https://venus.chub.ai)

[JanitorAI](https://janitorai.com) 

## About other sites:

- [Harpy Chat](https://harpy.chat) Does NOT work at all. There seems to be a completely unfamiliar error occuring during generation on their end and not mine.

## Prerequisites

Python (**ONLY >=3.10 SUPPORTED**)

Have unzipped the directory to a folder

## Installation of Modules

1. Run the ``install_requirements.bat`` file. This will auto-install everything for you. (simply double-click it)

2. Alternatively, open ``cmd.exe`` in the directory where all the files are and write ``pip install -r requirements.txt``
   
   ![INSTALL_MODULES_CMD](https://i.imgur.com/HiIIOQN.jpg)

## Running the server

1. After the modules are installed, double click the ```app.py``` file.
2. The cmd should look something like this if everything works:
   
   ![CMD_SUCCESS](https://i.imgur.com/kqCpct9.jpg)
3. In the API settings, select ``OpenAI`` and ``Reverse Proxy``
4. Copy that URL (it's a local URl, don't worry, it's only accessible from devices in the same network and isn't public)
5. Insert that URL to the AI site ([Venus Chub AI](https://venus.chub.ai) for reference)

   ![INSERT_URL_TO_BAR](https://i.imgur.com/o1qjELe.png)

## Check Proxy

1. If your settings look alike, press the ``"Check Proxy"`` button. ![CHECK_PROXY_BUTTON](https://i.imgur.com/7L2KqfN.jpg)

2. If everything worked, you should get a green checkmark. ![GREEN_CHECKMARK](https://i.imgur.com/RPlhFQZ.png)

## Choosing a model

1. Thanks to the [vercel_ai module](https://github.com/ading2210/vercel-llm-api), you may use any model for ***free.***

2. Select either model from the list: ![CHOOSE_MODEL_GPT](https://i.imgur.com/ePKD0lR.png)

## Finalize

1. Once you've chosen a model, scroll down and press ``Save Settings`` ![SAVE_SETTINGS](https://i.imgur.com/GKxpx5y.jpg)


## Some more information

1. This does only **partially** support the Impersonation feature

2. This supports **Venus Chub's** group chat feature.

3. You can customize every setting except for ``max_tokens``

4. Due to limitations, ``max_tokens`` is **always** 255 tokens.

5. I have no influence over the ``vercel_ai`` module and any errors that occur from it are unfixable by me.

7. The ``Chat Memory`` function does not seem to work at the moment.

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
   
