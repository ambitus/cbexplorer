import tempfile
import yaml
import json
from cbexplorer.load import Loader, LoaderType

def test_yaml_load():
    yaml_string = b'''
        Key1: Test
        Key2:
            - Item1
            - Item2
        Key3:
            Key4: Test2
    '''
    f = tempfile.NamedTemporaryFile(delete=False)
    f.write(yaml_string)
    f.close()

    loaded_yaml = Loader.load(f.name)
    key_list = list(loaded_yaml)
    assert key_list[0] == 'Key1'
    assert key_list[1] == 'Key2'
    assert key_list[2] == 'Key3'
    assert loaded_yaml['Key1'] == "Test"
    assert loaded_yaml['Key2'][0] == "Item1"
    assert loaded_yaml['Key2'][1] == "Item2"
    assert loaded_yaml['Key3']['Key4'] == "Test2"

def test_json_load():
    json_string = b'''
    {
        "Key1": "Test",
        "Key2": [
            "Item1",
            "Item2"
        ],
        "Key3": {
            "Key4": "Test2"
        }
    }
    '''

    f = tempfile.NamedTemporaryFile(delete=False)
    f.write(json_string)
    f.close()

    loaded_json = Loader.load(f.name, file_type=LoaderType.JSON)
    key_list = list(loaded_json)
    assert key_list[0] == 'Key1'
    assert key_list[1] == 'Key2'
    assert key_list[2] == 'Key3'
    assert loaded_json['Key1'] == "Test"
    assert loaded_json['Key2'][0] == "Item1"
    assert loaded_json['Key2'][1] == "Item2"
    assert loaded_json['Key3']['Key4'] == "Test2"
