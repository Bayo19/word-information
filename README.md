## word-information: A Fully Functional Dictionary Module for Python

word-information is a Dictionary Module for Python 3 to get definitions, synonyms, antonyms, and part-of-speech of words. 

word-information uses requests and bs4 as dependencies and also uses wordset open-source dictionary as a data source.

### Installation

Installation is very simple through pip

```
pip install word-information
```


### Usage

word-information is very easy to use

For example,

```python
from wordInfo.word_information import WordInfo

word_info = WordInfo()
```

This is will create an instance of the WordInfo class and now it can be used to get meanings, translations etc.

For Meanings,

```python
print (word_info.get_meaning("chair"))
```

This will return a python dictionary containing the part_of_speech of the word as a key and a list of dictionaries of the meaning and examples, as a value.

```
{'NOUN': [{'meaning': 'a seat, especially for one person, usually having four legs for support and a rest for the back and often having rests for the arms', 'examples': None}, {'meaning': 'something that serves as a chair or supports like a chair', 'examples': ' The two men clasped hands to make a chair for their injured companion'}, {'meaning': 'a seat of office or authority', 'examples': None}]}                                                                       
```

For Synonyms,

```python
print (word_info.get_synonym("glory"))
```

This will return a list of synonyms of the given word

```
['celebrity', 'dignity', 'grandeur', 'greatness', 'honor', 'immortality', 'majesty', 'prestige', 'reputation', 'splendor', 'triumph', 'distinction', 'eminence', 'exaltation', 'illustriousness', 'kudos', 'magnificence', 'nobility', 'praise', 'renown', 'sublimity']
```

For Antonyms,

```python
print (word_info.get_antonym("sad"))

```
This will return a list of antonyms of the given word

```
['cheerful', 'glad', 'happy', 'hopeful', 'joyful']
```
### About

Current Version: 0.1.5
Created By Bayo Ade October 2022
