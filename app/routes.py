from flask import render_template
from app import app
from datetime import datetime
import requests

URL = 'https://rest.iad-01.braze.com/'
API_KEY = '63462b71-be35-4dc6-a15c-8b9374cc3ba2'
HEADER = {"Authorization": "Bearer " + API_KEY}

@app.route('/')
@app.route('/index')
def index():
    campaign_list_uri = '/campaigns/list'
    params = {
        'page': 0,
        'include_archived': False,
        'sort_direction': 'asc',
        'last_edit.time[gt]': '2021-02-14T23:59:59-5:00'
    }
    res = requests.get(URL + campaign_list_uri, headers=HEADER, params=params)
    campaigns = res.json()['campaigns']

    # Mock Data
    # [
    #     {'id': 1, 'name': 'Campaign 1', 'tags': ['marketing', 'promotional']},
    #     {'id': 2, 'name': 'Campaign 2', 'tags': ['marketing', 'promotional']},
    #     {'id': 3, 'name': 'Campaign 3', 'tags': ['marketing', 'promotional']}
    # ]

    return render_template('index.html', campaigns=campaigns)

@app.route('/campaign/<id>', methods=['GET'])
def campaign(id):
    campaign_analytics_uri = '/campaigns/data_series'
    params = {
        'campaign_id': id,
        'length': 2,
        'ending_at': datetime.now().isoformat()
    }
    res = requests.get(URL + campaign_analytics_uri, headers=HEADER, params=params)
    analytics = res.json()
    # print(analytics)

    campaign_details_uri = '/campaigns/details'
    params = {
        'campaign_id': id,
    }
    res = requests.get(URL + campaign_details_uri, headers=HEADER, params=params)
    details = res.json()
    print(details)

    return render_template('campaign.html', details=details, analytics=analytics)