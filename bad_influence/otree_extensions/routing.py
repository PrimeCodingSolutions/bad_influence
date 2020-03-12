from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from . import consumers
from django.conf.urls import url

# channel_routing = [
#     route_class(NetworkVoting, path=NetworkVoting.url_pattern),
# ]

websocket_routes = [
            url(r'^/network_voting/(?P<player_pk>[0-9]+)/(?P<group_pk>[0-9]+)$', consumers.NetworkVoting)
        ]

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(websocket_routes)
    )
})
