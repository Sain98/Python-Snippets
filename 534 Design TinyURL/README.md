Simeple URL generator based on TinyUrl
Problem from : https://leetcode.com/problems/design-tinyurl/#/description

Usage:

```python
  import generator
  
  # Load the key
  KEY = generator.load_key()
  
  # Key exists set max length
  if KEY != None:
	  # Loaded key lets set the max_length
	  MAX_LENGTH = len(KEY)

  # Key does not exist
  elif KEY == None:
	  # Unable to load key
	  # So we load default values
	  # Max length for the generated url
	  MAX_LENGTH = 6
	  KEY = [0 for x in range(MAX_LENGTH)]
    
   # Generate URL (increments the key automatically):
   url, KEY = generator.url_gen(KEY, MAX_LENGTH)
   
   print("URL: {}".format(url))
   print("KEY: {}".format(KEY))
   
   # Save the incremented key
   generator.save_key(KEY)
```
