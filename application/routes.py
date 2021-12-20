from flask import jsonify

from application import app
from application.views import UserView, AdView

USERS_ROUTE = '/api/v1/users/'
ADS_ROUTE = '/api/v1/ads/'

@app.route('/status', methods=['GET'])
def status_check():
    return jsonify({'status': 'Ok'})


app.add_url_rule(
    f'{USERS_ROUTE}<int:user_id>',
    view_func=UserView.as_view('user_get'),
    methods=['GET']
    )
app.add_url_rule(
    USERS_ROUTE,
    view_func=UserView.as_view('user_post'),
    methods=['POST']
    )
app.add_url_rule(
    f'{ADS_ROUTE}<int:ad_id>',
    view_func=AdView.as_view('ad_get'),
    methods=['GET']
    )
app.add_url_rule(
    ADS_ROUTE,
    view_func=AdView.as_view('ad_post'),
    methods=['POST']
    )
app.add_url_rule(
    f'{ADS_ROUTE}<int:ad_id>',
    view_func=AdView.as_view('ad_put'),
    methods=['PUT']
    )
app.add_url_rule(
    f'{ADS_ROUTE}<int:ad_id>',
    view_func=AdView.as_view('ad_delete'),
    methods=['DELETE']
    )
