from tiktoken import get_encoding

from count_tokens import count_tokens


messages = [{
    "role": "system",
    "content": "Hey, you!"
}]

num = count_tokens(messages, "gpt-4")
print("Token count", num)

encoding = get_encoding("cl100k_base")
print("Token IDs: ", encoding.encode(messages[0]["content"]))
