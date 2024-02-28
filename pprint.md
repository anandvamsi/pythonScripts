# To print json in proper format
we use pretty print module to print json in proper method.
```python
import json
import pprint

# Sample JSON data
json_data = '''
{
  "name": "John",
  "age": 30,
  "city": "New York",
  "pets": [
    {"name": "Fluffy", "species": "cat"},
    {"name": "Fido", "species": "dog"}
  ]
}
'''

# Parse the JSON data
parsed_data = json.loads(json_data)

# Pretty print the parsed data
pprint.pprint(parsed_data)
```
