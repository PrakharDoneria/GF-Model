# gfmodel

A simple Python client for the GitHub Models API. This package provides an easy-to-use interface to interact with GitHub's free, OpenAI-compatible inference API, allowing you to integrate large language models into your projects with a GitHub Personal Access Token (PAT) instead of a paid API key.

## Installation

The package requires `requests` as a dependency. You can install it from PyPI using `pip`:

```bash
pip install gfmodel
````

## Features

  - **Easy Authentication**: Log in with a GitHub Personal Access Token (PAT).
  - **OpenAI Compatibility**: Utilizes an OpenAI-compatible `chat/completions` endpoint.
  - **Simple Interface**: Methods to log in, set a model, and interact with the model via a simple chat function.

## Usage

Here is a basic example of how to use the `gfmodel` client to chat with a model.

First, ensure you have a GitHub Personal Access Token with the `models:read` scope.

```python
import gfmodel

# Replace with your actual GitHub PAT.
# You can also set this as a GITHUB_TOKEN environment variable.
gfmodel.login("YOUR_GITHUB_ACCESS_TOKEN")

# Get a list of all available models
gfmodel.show()

# Set the model to use.
gfmodel.set("openai/gpt-4o")

# Start a chat.
response = gfmodel.chat("Hello!")
print(response)
```

## Available Models (as of 08/09/2025)
```
- openai/gpt-4.1
- openai/gpt-4.1-mini
- openai/gpt-4.1-nano
- openai/gpt-4o
- openai/gpt-4o-mini
- openai/gpt-5
- openai/gpt-5-chat
- openai/gpt-5-mini
- openai/gpt-5-nano
- openai/o1
- openai/o1-mini
- openai/o1-preview
- openai/o3
- openai/o3-mini
- openai/o4-mini
- openai/text-embedding-3-large
- openai/text-embedding-3-small
- ai21-labs/ai21-jamba-1.5-large
- ai21-labs/ai21-jamba-1.5-mini
- cohere/cohere-command-a
- cohere/cohere-command-r-08-2024
- cohere/cohere-command-r-plus-08-2024
- cohere/cohere-embed-v3-english
- cohere/cohere-embed-v3-multilingual
- core42/jais-30b-chat
- deepseek/deepseek-r1
- deepseek/deepseek-r1-0528
- deepseek/deepseek-v3-0324
- meta/llama-3.2-11b-vision-instruct
- meta/llama-3.2-90b-vision-instruct
- meta/llama-3.3-70b-instruct
- meta/llama-4-maverick-17b-128e-instruct-fp8
- meta/llama-4-scout-17b-16e-instruct
- meta/meta-llama-3.1-405b-instruct
- meta/meta-llama-3.1-8b-instruct
- mistral-ai/codestral-2501
- mistral-ai/ministral-3b
- mistral-ai/mistral-large-2411
- mistral-ai/mistral-medium-2505
- mistral-ai/mistral-nemo
- mistral-ai/mistral-small-2503
- xai/grok-3
- xai/grok-3-mini
- microsoft/mai-ds-r1
- microsoft/phi-3.5-mini-instruct
- microsoft/phi-3.5-moe-instruct
- microsoft/phi-3.5-vision-instruct
- microsoft/phi-3-medium-128k-instruct
- microsoft/phi-3-medium-4k-instruct
- microsoft/phi-3-mini-128k-instruct
- microsoft/phi-3-mini-4k-instruct
- microsoft/phi-3-small-128k-instruct
- microsoft/phi-3-small-8k-instruct
- microsoft/phi-4
- microsoft/phi-4-mini-instruct
- microsoft/phi-4-mini-reasoning
- microsoft/phi-4-multimodal-instruct
- microsoft/phi-4-reasoning
```

## Project Details

  - **Version**: 1.0.0
  - **Description**: Simple Python client for GitHub Models API
  - **License**: MIT
  - **Author**: Prakhar Doneria
  - **Homepage**: https://github.com/prakhardoneria/gfmodel