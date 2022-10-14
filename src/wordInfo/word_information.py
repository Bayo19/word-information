from typing import Any, List, Dict, Union
import json
import itertools
import os
from bs4 import BeautifulSoup, ResultSet
import requests

class WordInfo:
    def __init__(self) -> None:
        return None

    def get_meaning(self, word: str) -> Dict[str, List[Dict[str, Any]]]:
        """
        Returns part-of-speech and meanings for a given word
        """
        type_of_argument_entered = type(word)
        if type(word) != str:
            raise TypeError(F"The parameter 'word' should be str not {type_of_argument_entered.__name__}")
            
        try:
            response = requests.get("https://www.dictionary.com/browse/{}".format(word))
        except requests.exceptions.ConnectionError:
            return self._open_source_get_meaning(word)

        soup = BeautifulSoup(response.text, 'html.parser')
        meaning = soup.find('div', {'class': 'default-content'})
        sections = meaning.find_all('section', {"class": "css-109x55k e1hk9ate4"})
        if not sections:
            return {soup.find('span', {'class': 'luna-pos'}).text.strip().upper().replace(",", ""):self._meanings(soup)}
        return {s.find('span', {'class': 'luna-pos'}).text.strip().upper().replace(",", ""):self._meanings(s) for s in sections}

    def get_synonym(self, word: str) -> List[str]:
        """
        Returns a list of synonyms for a given word
        """
        type_of_argument_entered = type(word)
        if type(word) != str:
            raise TypeError(F"The parameter 'word' should be str not {type_of_argument_entered.__name__}")
        try:
            response = requests.get('https://www.thesaurus.com/browse/{}'.format(word))
        except requests.exceptions.ConnectionError:
            return self._open_source_get_synonym(word)

        soup = BeautifulSoup(response.text, 'html.parser')
        div =  soup.find('div', {'class': 'css-ixatld e15rdun50'})
        if not div:
            return self._open_source_get_synonym(word)
        lis = div.find_all('li')
        if not lis:
            return self._open_source_get_synonym(word)
        return [li.text.strip() for li in lis]

    def get_antonym(self, word: str) -> List[str]:
        """
        Returns a list of antonyms of a given word
        """
        type_of_argument_entered = type(word)
        if type(word) != str:
            raise TypeError(F"The parameter 'word' should be str not {type_of_argument_entered.__name__}")
        
        response = requests.get('https://www.thesaurus.com/browse/{}'.format(word))
        soup = BeautifulSoup(response.text, 'html.parser')
        div = soup.find('div', {'id': 'antonyms'})
        if not div:
            return None
        lis = div.find_all('li')
        if not lis:
            return None
        return [li.text.strip() for li in lis]
                
    def get_part_of_speech(self, word: str) -> Union[List[str],str]:
        """
        Returns the part-of-speech for a given word
        """
        type_of_argument_entered = type(word)
        if type(word) != str:
            raise TypeError(F"The parameter 'word' should be str not {type_of_argument_entered.__name__}")
        try:
            response = requests.get("https://www.dictionary.com/browse/{}".format(word))
        except requests.exceptions.ConnectionError:
            return self._open_source_get_part_of_spech(word)

        soup = BeautifulSoup(response.text, 'html.parser')
        meaning = soup.find('div', {'class': 'default-content'})
        sections = meaning.find_all('section', {"class": "css-109x55k e1hk9ate4"})
        if not sections:
            return soup.find('span', {'class': 'luna-pos'}).text.strip().upper().replace(",", "")
        return [s.find('span', {'class': 'luna-pos'}).text.strip().upper().replace(",", "") for s in sections]

    def _split_words_and_examples(self, sentencelist: List[str]) -> List[Dict[str, Any]]:
        """
        The defintions and examples are returned together as a string in a list. 
        This function splits those strings into definition as a key - "meaning", and example as the value - "examples", in a dictionary
        Returns a list of dictionaries such as {"meaning": "one defintion of a word", "examples": None}
        """
        result = []
        for word in sentencelist:
            if len(word.split(":")) > 1:
                result.append({"meaning": word.split(":")[0], "examples":word.split(":")[1]})
            else: 
                if "!" in word:
                    pass
                else:
                    result.append({"meaning": word, "examples": None})
        return result
        
    def _meanings(self, section: ResultSet) -> List[Dict[str, Any]]:
        """
        Extracts and returns a list of definitions and their meanings as a string, from a given section
        """
        result = section.find('div', {'class': 'css-10n3ydx e1hk9ate0'})
        default_content =  result.find('div', {'class': 'default-content'})
        if not default_content:
            spans = result.find_all('span')
            list_of_definitions_and_examples_span =  [s.text.strip().replace(".", "") for s in spans if 'Slang' not in s.text.strip().replace(".", "")][0:3]
            return self._split_words_and_examples(list_of_definitions_and_examples_span)
        definitions = default_content.find_all('div')
        list_of_definitions_and_examples_default_content =  ["".join([word for word in d.text.strip().split(".") if '(def' not in word and "1)" not in word]) for d in definitions][0:3]
        
        return self._split_words_and_examples(list_of_definitions_and_examples_default_content)

    def _get_open_source_dataset(self, word: str) -> Dict:
        """
        Gets data for word from open-source wordnet dataset
        """
        type_of_argument_entered = type(word)
        if type(word) != str:
            raise TypeError(F"The parameter 'word' should be str not {type_of_argument_entered.__name__}")

        first_letter_of_word = word[:1]
        abs_path = os.path.join("wordset_open_source_data", F"{first_letter_of_word}.json")
        print(F"src/{abs_path}")
        data = json.loads(open(abs_path).read())
        meaning: dict = data.get(word)
        if not meaning:
            return None
        return meaning

    def _open_source_get_meaning(self, word:str) -> Dict[str, List[Dict[str, Any]]]:
        """
        Returns meanings for given word from open source dataset (wordset)
        """
        try:
            open_source_data = self._get_open_source_dataset(word)
        except FileNotFoundError:
            return None

        original_meanings_data = open_source_data["meanings"]
        part_of_speech_list = []
        for d in original_meanings_data:
            part_of_speech_list.append(d["speech_part"])
            d.pop("id")
            d["meaning"] = d.pop("def")
            if d.get("example"):
                d["examples"] = d.pop("example")
            if d.get("synonyms"):
                d.pop("synonyms")
            d["examples"] = None
        result = {k.upper(): [d for d in original_meanings_data if d.get("speech_part") == k] for k in part_of_speech_list}
        return {k: [{"meaning": d.get("meaning"), "examples": d.get("examples")} for d in v] for k,v in result.items()}
        
    def _open_source_get_synonym(self, word:str) -> List[str]:
        """
        Returns synonym for given word from open source dataset (wordset)
        
        """
        try:
            open_source_data = self._get_open_source_dataset(word)
        except FileNotFoundError:
            return None

        original_meanings_data = open_source_data["meanings"]
        return list(itertools.chain.from_iterable([d.get("synonyms") for d in original_meanings_data if d.get("synonyms") != None]))
    
    def _open_source_get_part_of_speech(self, word:str) -> List[str]:
        """
        Returns part-of-speech for given word from open source dataset (wordset)
        
        """
        try:
            open_source_data = self._get_open_source_dataset(word)
        except FileNotFoundError:
            return None

        original_meanings_data = open_source_data["meanings"]
        result = []
        [result.append(d["speech_part"].upper()) for d in original_meanings_data if d["speech_part"].upper() not in result]
        return result


word_info = WordInfo()
print(word_info.get_meaning("bath"))