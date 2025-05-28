import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
Token = '758d1468dc59aaf7f14ac305000532bd'
Header = {'Content-Type' : 'application/json', 'trainer_token' : Token } 
Trainer_id = '36791'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : Trainer_id})
    assert response.status_code == 200


def test_part_of_responser():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : Trainer_id})
    assert response_get.json()["data"][0]["name"] == 'Бульбазавр'


@pytest.mark.parametrize('key, value', [('name', 'Бульбазавр'), ('trainer_id', Trainer_id), ('id', '327335')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : Trainer_id})
    assert response_parametrize.json()["data"][0][key] == value
   

def test_part_o_responser():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : Trainer_id})
    assert response_get.json()["data"][5]["trainer_id"] == '36791'






 