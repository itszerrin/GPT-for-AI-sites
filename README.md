# GPT generation client for AI sites

## Brief introduction

This application uses LLM wrappers but uses Flask to host the LLM locally and make it usable within other AI sites.

I do not condone acts which go against the LLM provider's TOS.

## Supported Sites:

[Venus Chub AI](https://venus.chub.ai)

[JanitorAI](https://janitorai.com) Due to the site's way it was coded, please only select gpt-3.5-turbo or else an error will occur. 

## About other sites:

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

## Check Proxy

1. If your settings look alike, press the ``"Check Proxy"`` button. ![CHECK_PROXY_BUTTON](https://i.imgur.com/7L2KqfN.jpg)

2. If everything worked, you should get a green checkmark. ![GREEN_CHECKMARK](https://i.imgur.com/RPlhFQZ.png)

## Choosing a model

1. Thanks to the [g4f module](https://github.com/xtekky/gpt4free), you can use ``gpt-3.5-turbo`` and ``gpt-4-0613`` for ***free.***

2. Select either ``gpt-3.5-turbo`` or ``gpt-4-0613`` from the list: ![CHOOSE_MODEL_GPT](https://i.imgur.com/OyWPJP9.png)

## Finalize

1. Once you've chosen a model, scroll down and press ``Save Settings`` ![SAVE_SETTINGS](https://i.imgur.com/GKxpx5y.jpg)


## Some more information

1. This does not support **Venus Chub's** impersonation feature.

2. This supports **Venus Chub's** group chat feature.

3. Due to limitations of the module, you cannot customize the model. (``max_tokens`` is always the same, ``temperature`` is always same and unchangeable)

4. I have no influence over the ``g4f`` module and any errors that occur from it are unfixable by me.

5. ``GPT-4`` says it's ``GPT-3.5``/based off of ``GPT-3.5``? Yes, it's a common bug in the OpenAI APi. [OpenAI forums thread](https://community.openai.com/t/gpt-4-through-api-says-its-gpt-3/286881)

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

Developed with [gpt4free module by xtekky](https://github.com/xtekky/gpt4free)
   
