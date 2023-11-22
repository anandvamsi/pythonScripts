
# Boolean

Example 1:
```python

def greet_user(name=None):
    greet = name or "there"
    print(f"hi {greet}, How you doing")

greet_user("Anand")
greet_user()
```
