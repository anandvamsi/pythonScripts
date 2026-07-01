# Pydantic

## What is Pydantic


## Real time usecases

### Usecase 1
#### Integratin with FastAPI
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AdditionRequest(BaseModel):
    a: int
    b: int


@app.post("/add")
async def add(request: AdditionRequest):
    return {
        "result": request.a + request.b
    }
```



### Usecase 2

#### Integration with FastMCP
```python
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel

mcp = FastMCP("Demo")

class AdditionRequest(BaseModel):
    a: int
    b: int

@mcp.tool()
def add_numbers(request: AdditionRequest) -> int:
    return request.a + request.b

if __name__ == "__main__":
 mcp.run()
```

### To Run the code
```bash
pip install fastapi uvicorn
Uvicorn running on http://127.0.0.1:8000
```

#### Testing the code
```
curl -X POST http://localhost:8000/add \
-H "Content-Type: application/json" \
-d '{"a":10,"b":20}'
```

```
curl -X POST http://localhost:8000/add \
-H "Content-Type: application/json" \
-d '{"a":"abc","b":20}'
```
#### Ouput 
```bash
{
  "detail": [
    {
      "type": "int_parsing",
      "loc": ["body","a"],
      "msg": "Input should be a valid integer"
    }
  ]
}```
```
### Note we can integrade LLM to MCP and use pydantic here is the flow.
```
Prompt :: my name is Raj kumar and age is 33 years old

User Input
      ↓
LLM extracts fields
      ↓
{
   "name": "Raj Kumar",
   "age": 33
}
      ↓
Pydantic Validation
      ↓
Tool Execution
```

## For MCP tools:
- Let the LLM interpret human text.
- Convert it to structured JSON.
- Use Pydantic to validate the JSON before calling the tool.
