from flask import render_template
from app import app
import requests

@app.route('/')
@app.route('/index')
def index():
    url = 'https://rest.iad-01.braze.com/'
    campaign_list_uri = '/campaigns/list'
    API_KEY = 'c2b6c371-37f6-4d00-b925-c98c88e6d3e2'
    headers = {"Authorization": "Bearer " + API_KEY}
    params = {
        'page': 0,
        'include_archived': True,
        'sort_direction': 'asc',
        'last_edit.time[gt]': '1992-06-28T23:59:59-5:00'
    }
    res = requests.get(url + campaign_list_uri, headers=headers, params=params)
    print(res.json())

    campaigns = [
        {'id': 1, 'name': 'Campaign 1', 'tags': ['marketing', 'promotional']},
        {'id': 2, 'name': 'Campaign 2', 'tags': ['marketing', 'promotional']},
        {'id': 3, 'name': 'Campaign 3', 'tags': ['marketing', 'promotional']}
    ]

    return render_template('index.html', campaigns=campaigns)

def get_campaign():
    print('here')