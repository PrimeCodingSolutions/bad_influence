from bad_influence.otree_extensions.routing import websocket_routes
from channels.routing import URLRouter, ProtocolTypeRouter
from channels.auth import AuthMiddlewareStack

# URLRouter += websocket_routes

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_routes
        )
    )
})
