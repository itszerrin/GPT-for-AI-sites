# GPT Generation Client for AI Integration

## Overview

This application facilitates seamless integration of GPT language models (LLM) into various AI sites by utilizing Flask to host the LLM locally and globally. The implementation involves LLM wrappers, ensuring compatibility with any site using the "/chat/completions" route for text generation. It is essential to adhere to the terms of service of the LLM provider. Usable as a free OpenAI reverse proxy.

## Supported Sites

The application supports integration with any site employing the "/chat/completions" route for text generation.

## Prerequisites

- Python 3.10
- Unzipped directory

## Installation

1. Run the `install_requirements.bat` file for automatic installation or execute `pip3.10 install -r requirements.txt` in the command prompt in the application directory.

## Running the Server

1. After installation, launch the server by double-clicking the `app.py` file or using the `start.bat` file.
2. Ensure successful server initiation by checking the command prompt for the indicated success message.
3. In the API settings, select "OpenAI" and "Reverse Proxy."
4. Copy the local URL for use on the AI site.

## Check Proxy

1. Verify your settings and press the "Check Proxy" button.
2. A successful check will be indicated by a green checkmark.

## Choosing a Model

1. Select a model from the provided list.

## Google Colab Integration

This application is also compatible with Google Colab. [Access the hosted version on Google Colab here](https://colab.research.google.com/drive/1WIHWe2w_i-Lg2efd7jLIWEN_319017rJ?usp=sharing).

## Finalizing Settings

1. After choosing a model, scroll down and press "Save Settings."

## Additional Information

1. This application does not utilize the resources of the user's PC as a language model.
3. The `gpt4free` module is used in the development, and any errors related to it are beyond the control of the developer.
4. The "Chat Memory" function is currently non-functional.

## Copyright

**GPT Generation Client for AI Sites:** A hosted wrapper for AI sites.
Copyright (C) 2023 Recentaly

This program is distributed under the terms of the GNU General Public License as published by the Free Software Foundation. For details, refer to [GNU General Public License](https://www.gnu.org/licenses/).

Developed with [gpt4free module](https://github.com/xtekky/gpt4free).
