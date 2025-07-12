import requests

base_url = "https://ru.yougile.com"
Token = "FrTm3MDPs8+RPUOCsV1T2Acf34dcLaXECso9JJMJgnIj2S3lXrD3QLFjfFCYMXvR"

def test_auth_you():
    you = {
        'login': 'm29712461@gmail.com',
        'password': 'Alina2011',
        'name': 'поток_102.2'
}
    resp = requests.post(base_url + '/api-v2/auth/companies', json=you)
    assert resp.status_code == 200

    resp = requests.get(base_url + '/api-v2/projects', json=you)
    body = resp.json()