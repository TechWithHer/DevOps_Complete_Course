import base64

def check_presentation():
    sample = "Hello DevOps!"
    encoded = base64.b64encode(sample.encode())
    decoded = base64.b64decode(encoded).decode()
    print(f"Encoded: {encoded}\nDecoded: {decoded}")
    print("Presentation layer check completed.")