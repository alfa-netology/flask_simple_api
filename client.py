import requests

HOST = 'http://127.0.0.1:5000'
API_HOST = f'{HOST}/api/v1'

def check_status():
    try:
        response = requests.get(f'{HOST}/status')
        print(f'code: {response.status_code}, status:{response.json().get("status")}')
        return True
    except Exception as e:
        print(e)
        return False

def add_user(name, password, email):
    user_data = {
        'username': name,
        'password': password,
        'email': email,
    }
    response = requests.post(f'{API_HOST}/users', json=user_data)
    return response.json()

def get_user(user_id):
    response = requests.get(f'{API_HOST}/users/{user_id}')
    return response.json()

def add_ad(title, text, user_id):
    user_data = {
        'title': title,
        'text': text,
        'user_id': user_id,
    }
    response = requests.post(f'{API_HOST}/ads', json=user_data)
    return response.json()

def get_ad(ad_id):
    response = requests.get(f'{API_HOST}/ads/{ad_id}')
    return response.json()

def update_ad(ad_id, data):
    response = requests.put(f'{API_HOST}/ads/{ad_id}', json=data)
    return response.json()
    
def delete_ad(ad_id):
    response = requests.delete(f'{API_HOST}/ads/{ad_id}')
    return response.json()


if __name__ == '__main__' and check_status():
    print(get_user(10))

    new_user = {'name': 'user_21', 'password': 'admin', 'email': 'user_22@mail.com'}
    print(add_user(**new_user))

    new_ad = {'title': 'ad title #2', 'text': 'ad text #2', 'user_id': 13}
    print(add_ad(**new_ad))

    edit_ad = {'title': 'ad title #100', 'text': 'ad text #100'}
    print(update_ad(100, edit_ad))

    print(delete_ad(42))

    print(get_ad(12))

