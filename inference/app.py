from langchain.llms import HuggingFaceTextGenInference
import argparse
import requests

# Set up argparse to accept a command-line argument for the client IP address
parser = argparse.ArgumentParser(description="Test LLM inference server")
parser.add_argument("--url", type=str, required=True, help="URL of inference server")
parser.add_argument("--input", type=str, required=False, help="Input text to generate from")
args = parser.parse_args()

def get_info(url):
  response = requests.get(f"{url}/info")
  print(response.json())
  return response.json()

def get_generated_text(input_text):
    # Create an instance of HuggingFaceTextGenInference
    llm = HuggingFaceTextGenInference(
        inference_server_url=args.url if args.url else "http://hf-tgi-server.llms.svc.cluster.local:3000/",
        max_new_tokens=512,
        top_k=10,
        top_p=0.95,
        typical_p=0.95,
        temperature=0.01,
        repetition_penalty=1.03,
    )

    # Generate text using the llm instance
    generated_text = llm(input_text)
    return generated_text


# # Create an instance of HuggingFaceTextGenInference
# llm = HuggingFaceTextGenInference(
#   inference_server_url=args.url if args.url else "http://hf-tgi-server.llms.svc.cluster.local:3000/",
#   max_new_tokens=512,
#   top_k=10,
#   top_p=0.95,
#   typical_p=0.95,
#   temperature=0.01,
#   repetition_penalty=1.03,
# )

# Generate text using the llm instance
if not args.input:
  args.input = "What is the capital of Spain"
else:
  args.input = args.input

input_text = args.input
generated_text = get_generated_text(input_text)

# Print the generated text
print("Input text:", input_text)
print(generated_text)

print("Model Info:")
get_info(args.url)