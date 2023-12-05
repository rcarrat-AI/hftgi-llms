import argparse
import requests
import json
from langchain.llms import HuggingFaceTextGenInference
import warnings

# Suppress specific Pydantic UserWarnings
warnings.filterwarnings("ignore", message="Field \"model_id\" has conflict with protected namespace")


def get_info(url):
    response = requests.get(f"{url}/info")
    info = response.json()
    print(json.dumps(info, indent=4))
    return info

def get_generated_text(url, input_text):
    # Create an instance of HuggingFaceTextGenInference
    llm = HuggingFaceTextGenInference(
        inference_server_url=url,
        max_new_tokens=512,
        top_k=10,
        top_p=0.95,
        typical_p=0.95,
        temperature=0.01,
        repetition_penalty=1.03,#
    )

    # Generate text using the llm instance
    generated_text = llm(input_text)
    return generated_text

# Set up argparse to handle subcommands
parser = argparse.ArgumentParser(description="Test LLM inference server")
subparsers = parser.add_subparsers(dest="command")

# Subparser for 'info' command
info_parser = subparsers.add_parser('info', help='Get server info')
info_parser.add_argument("--url", type=str, required=True, help="URL of inference server")

# Subparser for 'generate' command
generate_parser = subparsers.add_parser('generate', help='Generate text')
generate_parser.add_argument("--url", type=str, required=True, help="URL of inference server")
generate_parser.add_argument("--input", type=str, required=True, help="Input text to generate from")

# Parse arguments
args = parser.parse_args()

# Execute based on command
if args.command == "info":
    print("Model Info:")
    get_info(args.url)
elif args.command == "generate":
    print("Input text:", args.input)
    generated_text = get_generated_text(args.url, args.input)
    print("LLM answer:", generated_text)