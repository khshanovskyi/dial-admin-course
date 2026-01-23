import uvicorn
from aidial_interceptors_sdk.chat_completion import interceptor_to_chat_completion
from aidial_interceptors_sdk.utils._http_client import get_http_client
from aidial_sdk import DIALApp

from app_demo.constants import DIAL_URL
from app_demo.d2_interceptors._interceptor import PrePostInterceptor

class AppTypeInterceptor(PrePostInterceptor):

    def __init__(self, **data):
        super().__init__(interceptor_name="AppType", **data)

async def client_factory():
    return get_http_client()

app_type__interceptor_app = interceptor_to_chat_completion(
    cls=AppTypeInterceptor,
    dial_url=DIAL_URL,
    client_factory=client_factory,
)

app = DIALApp(
    dial_url=DIAL_URL,
    propagate_auth_headers=True,
)
app.add_chat_completion(deployment_name="app-type-interceptor", impl=app_type__interceptor_app)

if __name__ == "__main__":
    import sys

    if 'pydevd' in sys.modules:
        config = uvicorn.Config(app, port=5041, host="0.0.0.0", log_level="info")
        server = uvicorn.Server(config)
        import asyncio

        asyncio.run(server.serve())
    else:
        uvicorn.run(app, port=5041, host="0.0.0.0")
