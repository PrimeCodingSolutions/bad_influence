from . import consumers
from django.conf.urls import url, re_path   

# channel_routing = [
#     route_class(NetworkVoting, path=NetworkVoting.url_pattern),
# ]

websocket_routes = [
            url(r'^/network_voting/(?P<player_pk>[0-9]+)/(?P<group_pk>[0-9]+)$', consumers.NetworkVoting),
            re_path(r'ws/chat(?P<player_name>)')
        ]
