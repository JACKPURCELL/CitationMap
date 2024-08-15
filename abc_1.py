from openai import OpenAI

import json

client = OpenAI()

def get_institution_address(affiliation_map):
    # Replace 'YOUR_API_KEY' with your actual OpenAI API key
    
    # Construct the prompt
    system_message = {
        "role": "system",
        "content": (
            "Please find the address of each institute listed in the 'affiliation_map' and return it in the following JSON format where the key is the affiliation and value is the address details:\n"
            "{\n"
            "  'affiliation': {\n"
            "    'institute_name': 'string',\n"
            "    'institute_full_address': 'string',\n"
            "    'county': 'string',\n"
            "    'city': 'string',\n"
            "    'state': 'string',\n"
            "    'country': 'string',\n"
            "    'latitude': 'float',\n"
            "    'longitude': 'float'\n"
            "  }\n"
            "}\n"
            "If the institution is not found, please return None for that affiliation."
        )
    }

    user_message = {
        "role": "user",
        "content": str(affiliation_map)
    }

    # Make the API call
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type": "json_object"},
        
        messages=[system_message, user_message]
    )
    print(completion)
    # Extract the JSON response
    address_json = completion.choices[0].message.content
    address_json = json.loads(address_json)
    return address_json

# Example usage
affiliation_map = ["Harvard University", "MIT", "Stanford", "BDHUISHIU"]


address_json = get_institution_address(affiliation_map)
print(address_json)
