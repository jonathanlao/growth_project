from flask import render_template, Response
from app import app
import requests
import os

URL = 'https://rest.iad-01.braze.com/'
HEADER = {"Authorization": "Bearer " + os.environ.get('API_KEY')}

def get_campaign_list():
    campaign_list_uri = '/campaigns/list'
    params = {
        'page': 0,
        'include_archived': False,
        'sort_direction': 'asc',
        'last_edit.time[gt]': '2021-02-14T23:59:59-5:00'
    }
    res = requests.get(URL + campaign_list_uri, headers=HEADER, params=params)
    campaigns = res.json()['campaigns']
    return campaigns

@app.route('/')
@app.route('/index')
def index():
    campaigns = get_campaign_list()
    # print(campaigns)
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
        'length': 30,
    }
    res = requests.get(URL + campaign_analytics_uri, headers=HEADER, params=params)
    analytics = res.json()['data']
    analytics.reverse()
    print(analytics)

    campaign_details_uri = '/campaigns/details'
    params = {
        'campaign_id': id,
    }
    res = requests.get(URL + campaign_details_uri, headers=HEADER, params=params)
    details = res.json()
    # print(details)

    return render_template('campaign.html', details=details, analytics=analytics)

@app.route('/download', methods=['GET'])
def download():
    campaigns = get_campaign_list()
    csv = ''
    for campaign in campaigns:
        id = campaign['id']
        name = campaign['name']
        if not name:
            name = ''
        csv = csv + ','.join([id, name] + campaign['tags']) + '\n'

    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":"attachment; filename=campaigns.csv"}
    )
