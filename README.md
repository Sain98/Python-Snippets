# Python-Snippets
Just using this to store small scripts etc.

# Cycle.py
Cycle is a simple thing i made to cycle through the characters in a string or the values in an array
Example usage would be:
```python
import cycle
x = cycle(['foo', 'bar'])
print(next(x))
```
```
Output:
foo
bar
foo
```

# Game.py
Simple rock paper scissor game made as an example on how to use functions

# **Hex, dec, ascii - converter**

### **About:**
Simple converter tool to convert hex, dec or ascii.
Requires Python 3.x!
Older versions dont seem to work with this

Conversions are :

	hex   -> dec & ascii
	dec   -> hex & ascii
	ascii -> hex & dec

### Startup arguments
	python hex_dec_ascii-converter.py -h
	usage: hex_dec_ascii-converter.py [-h] [-i {hex,ascii,ascii-table,dec}] [-n]
	
	optional arguments:
	  -h, --help            show this help message and exit
	  -i {hex,ascii,ascii-table,dec}, --input {hex,ascii,ascii-table,dec}
	                        The sort off input value you will give. Default is hex
	  -n, --no-exit         Disable all the exit commands you would need to exit
	                        using ctrl+c



### Example usage & output

Hex example - (If no -i params are given it defaults to hex)

	>> hex_dec_ascii-converter.py -i hex
	Startup args:
	Input = hex
	no-exit = False
	Starting hex_converter!
	Available exit commands: [':q', ':quit', ':e', ':exit', ':c', ':close']
	----
	HEX: ff
	HEX: ff | DEC: 255 | ASCII: ÿ
	HEX: 0xff
	HEX: 0xff | DEC: 255 | ASCII: ÿ
	HEX: :q
	
Dec example

	>> hex_dec_ascii-converter.py -i dec
	Startup args:
	Input = dec
	no-exit = False
	Starting hex_converter!
	Available exit commands: [':q', ':quit', ':e', ':exit', ':c', ':close']
	----
	DEC: 210
	DEC: 210 | HEX: 0xd2 | ASCII: Ò
	DEC: 120
	DEC: 120 | HEX: 0x78 | ASCII: x
	DEC: :q

ASCII example

	>> hex_dec_ascii-converter.py -i ascii
	Startup args:
	Input = ascii
	no-exit = False
	Starting hex_converter!
	Available exit commands: [':q', ':quit', ':e', ':exit', ':c', ':close']
	----
	ASCII: A
	ASCII: A | DEC: 65 | HEX: 0x41
	ASCII: a
	ASCII: a | DEC: 97 | HEX: 0x61
	ASCII: sain
	ASCII: s | DEC: 115 | HEX: 0x73
	ASCII: a | DEC: 97 | HEX: 0x61
	ASCII: i | DEC: 105 | HEX: 0x69
	ASCII: n | DEC: 110 | HEX: 0x6e

### Source code:
