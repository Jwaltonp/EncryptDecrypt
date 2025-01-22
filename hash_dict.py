import base64
import json
from werkzeug.security import generate_password_hash, check_password_hash

# Current credentials
sample_dict = {
    'test_key': 'test_value',
}
print(f"This is the sample dict: {sample_dict}")

# Hash and encrypt dict example
# default method is scrypt:32768:8:1 however
# you can select you own
hashed_dict = generate_password_hash(json.dumps(sample_dict), method='pbkdf2:sha256:600000')
# Encode the hash string into bytes for b64encode() which takes bytes
encoded_hashed_dict_bytes = hashed_dict.encode()
# Convert to base64 encoded string
hashed_dict_str = base64.b64encode(encoded_hashed_dict_bytes).decode()
print(f"This is the hashed dict: {hashed_dict_str}")

# Decode the Base64 str to bytes
encoded_hashed_dict_bytes = base64.b64decode(hashed_dict_str).decode()

# Check if the dicts match
is_match = check_password_hash(encoded_hashed_dict_bytes, json.dumps(sample_dict))

print(f"Does the dict and hashed dict match? {is_match}")
