from wordInfo.word_information import WordInfo
import pytest

def test_invalid_input_for_get_meaning():
    with pytest.raises(TypeError):
        word_info = WordInfo()
        word_info.get_meaning(1)

    with pytest.raises(TypeError):
        word_info.get_meaning(["personal"])
    
    with pytest.raises(TypeError):
        word_info.get_meaning({})

def test_invalid_input_for_get_synonym():
    word_info = WordInfo()

    with pytest.raises(TypeError):
        word_info.get_synonym(1)

    with pytest.raises(TypeError):
        word_info.get_synonym(["stone"])
    
    with pytest.raises(TypeError):
        word_info.get_synonym({})

def test_invalid_input_for_get_antonym():
    word_info = WordInfo()

    with pytest.raises(TypeError):
        word_info.get_antonym(3)

    with pytest.raises(TypeError):
        word_info.get_antonym(["cheer"])
    
    with pytest.raises(TypeError):
        word_info.get_antonym({})

def test_invalid_input_for_get_part_of_speech():
    word_info = WordInfo()

    with pytest.raises(TypeError):
        word_info.get_part_of_speech(5)

    with pytest.raises(TypeError):
        word_info.get_part_of_speech(["music"])
    
    with pytest.raises(TypeError):
        word_info.get_part_of_speech({})

def test_type_of_get_meaning_is_dict():
    word_info = WordInfo()
    w = word_info.get_meaning("man")
    assert type(w) == dict and isinstance(w, dict)

def test_type_of_get_synonym_is_list():
    word_info = WordInfo()
    w = word_info.get_synonym("chair")
    assert type(w) == list and isinstance(w, list)

def test_type_of_get_antonym_is_list():
    word_info = WordInfo()
    w = word_info.get_antonym("person")
    assert type(w) == list and isinstance(w, list)

def test_type_of_get_part_of_speech_is_list_or_str():
    word_info = WordInfo()
    w = word_info.get_part_of_speech("race")
    assert (type(w) == list or type(w) == str) and (isinstance(w, list) or isinstance(w, str))

@pytest.mark.parametrize("test_input,expected", [
    ("cowboy", {'NOUN': [{'meaning': 'a man who herds and tends cattle on a ranch, especially in the western US, and who traditionally goes about most of his work on horseback', 'examples': None}, {'meaning': 'a man who exhibits the skills attributed to such cowboys, especially in rodeos', 'examples': None}, {'meaning': 'Chiefly Northeastern US', 'examples': None}]}),
    ("delicate", {'ADJECTIVE': [{'meaning': 'fine in texture, quality, construction, etc', 'examples': ' a delicate lace collar'}, {'meaning': 'easily broken or damaged; physically weak; fragile; frail', 'examples': ' delicate porcelain;a delicate child'}, {'meaning': 'so fine as to be scarcely perceptible; subtle', 'examples': ' a delicate flavor'}]})
])
def test_output_of_get_meaning(test_input, expected):
    word_info = WordInfo()
    assert word_info.get_meaning(test_input) == expected
    
@pytest.mark.parametrize("test_input,expected", [
    ("fuck", ['lay', 'screw', 'shag', 'bang', 'bonk', 'do', 'get it on', 'hump', 'score', 'sleep with', 'copulate', 'fornicate', 'know', 'make love', 'mate', 'procreate', 'schtup']),
    ("stain", ['blemish', 'blotch', 'color', 'dye', 'smudge', 'speck', 'splotch', 'stigma', 'tint', 'blur', 'brand', 'discoloration', 'disgrace', 'dishonor', 'drip', 'infamy', 'mottle', 'odium', 'onus', 'reproach', 'shame', 'slur', 'smirch', 'spatter', 'spot', 'black eye', 'ink spot', 'sinister']),
    ("tale", ['account', 'anecdote', 'fable', 'fiction', 'legend', 'myth', 'narrative', 'novel', 'short story', 'yarn', 'narration', 'relation', 'report', 'romance', 'saga', 'fairy tale', 'folk tale'])
])
def test_output_of_get_synonym(test_input, expected):
    word_info = WordInfo()
    assert word_info.get_synonym(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [
    ("bored", ['energized', 'refreshed', 'enthusiastic', 'excited', 'exhilarated', 'interested']),
    ("person", ['inanimate', 'animal', 'plant'])
])
def test_get_output_of_get_antonym(test_input, expected):
    word_info = WordInfo()
    assert word_info.get_antonym(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [
    ("play", ['NOUN', 'VERB (USED WITH OBJECT)', 'VERB (USED WITHOUT OBJECT)']),
    ("span", "NOUN"),
    ("man", ['NOUN', 'VERB (USED WITH OBJECT)', 'INTERJECTION'])
])
def test_output_of_get_part_of_speech(test_input, expected):
    word_info = WordInfo()
    assert word_info.get_part_of_speech(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [
    ("grand", {'ADJECTIVE': [{'meaning': "used of a person's appearance or behavior", 'examples': None}, {'meaning': 'the most important and magnificent in adornment', 'examples': None}, {'meaning': 'of behavior that is impressive and ambitious in scale or scope', 'examples': None}, {'meaning': 'large and impressive in physical size or extent', 'examples': None}, {'meaning': 'of high moral or intellectual value', 'examples': None}, {'meaning': 'of or befitting a lord', 'examples': None}, {'meaning': 'extraordinarily good or great', 'examples': None}, {'meaning': 'rich and superior in quality', 'examples': None}], 'NOUN': [{'meaning': 'a piano with the strings on a horizontal harp-shaped frame', 'examples': None}, {'meaning': 'the cardinal number that is the product of 10 and 100', 'examples': None}]}),
    ("travel", {'NOUN': [{'meaning': 'self-propelled movement', 'examples': None}, {'meaning': 'the act of going from one place to another', 'examples': None}, {'meaning': 'a movement through space that changes the location of something', 'examples': None}], 'VERB': [{'meaning': 'change location', 'examples': None}, {'meaning': 'undergo transportation as in a vehicle', 'examples': None}, {'meaning': 'make a trip for pleasure', 'examples': None}, {'meaning': 'undertake a journey or trip', 'examples': None}, {'meaning': 'travel upon or across', 'examples': None}, {'meaning': 'travel from place to place, as for the purpose of finding work, preaching, or acting as a judge', 'examples': None}]})
])
def test_output_of__open_source_get_meaning(test_input, expected):
    word_info = WordInfo()
    assert word_info._open_source_get_meaning(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [
    ("mask", ['masquerade', 'block out', 'cloak', 'dissemble', 'disguise']),
    ("try", ['effort', 'try on', 'render', 'taste', 'sample', 'try out', 'strain', 'hear', 'judge', 'adjudicate', 'attempt', 'test']),
    ("journey", ['journeying', 'travel', 'travel'])
])
def test_output_of__open_source_get_synonym(test_input, expected):
    word_info = WordInfo()
    assert word_info._open_source_get_synonym(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [
    ("play", ['NOUN', 'VERB']),
    ("wonder", ['NOUN', 'VERB']),
    ("grand", ['ADJECTIVE', 'NOUN'])
])
def test_output_of__open_source_get_part_of_speech(test_input, expected):
    word_info = WordInfo()
    assert word_info._open_source_get_part_of_speech(test_input) == expected