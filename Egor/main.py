import requests

URL = 'https://api.pokemonbattle.ru/v2'
Token = '758d1468dc59aaf7f14ac305000532bd'
Header = {'Content-Type' : 'application/json', 'trainer_token' : Token } 

body_registration = {
    "trainer_token": Token,
    "email": "petuhoff.egor2017@yandex.r",
    "password": "Iloveqa1"
}
body_confirmation = {
    "trainer_token": Token
}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 12
}
body_change = {
    "pokemon_id": "293655",
    "name": "Алигатор",
    "photo_id": 55
}
body_catch ={
    "pokemon_id": "327335"
}



'''response = requests.post(url = f'{URL}/trainers/reg', headers= Header, json = body_registration)
print(response.text)'''



'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = Header, json = body_confirmation)
print(response_confirmation.text)'''



response_create = requests.post(url = f'{URL}/pokemons', headers = Header, json = body_create)
print(response_create.text)
message = response_create.json()['message']
print(message)



response_change = requests.put(url =f'{URL}/pokemons', headers = Header, json = body_change)
print(response_change.text)
message = response_change.json()['message']
print(message)



response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = Header, json = body_catch)
print(response_catch.text)
message = response_catch.json()['message']
print(message)