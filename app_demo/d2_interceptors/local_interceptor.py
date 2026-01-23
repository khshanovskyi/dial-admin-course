import uvicorn
from aidial_interceptors_sdk.chat_completion import interceptor_to_chat_completion
from aidial_interceptors_sdk.utils._http_client import get_http_client
from aidial_sdk import DIALApp

from app_demo.constants import DIAL_URL
from app_demo.d2_interceptors._interceptor import PrePostInterceptor

class LocalInterceptor(PrePostInterceptor):

    def __init__(self, **data):
        super().__init__(interceptor_name="Local", **data)

async def client_factory():
    return get_http_client()

local_pre_post_interceptor_app = interceptor_to_chat_completion(
    cls=LocalInterceptor,
    dial_url=DIAL_URL,
    client_factory=client_factory,
)

app = DIALApp(
    dial_url=DIAL_URL,
    propagate_auth_headers=True,
)
app.add_chat_completion(deployment_name="local-interceptor", impl=local_pre_post_interceptor_app)

if __name__ == "__main__":
    import sys

    if 'pydevd' in sys.modules:
        config = uvicorn.Config(app, port=5040, host="0.0.0.0", log_level="info")
        server = uvicorn.Server(config)
        import asyncio

        asyncio.run(server.serve())
    else:
        uvicorn.run(app, port=5040, host="0.0.0.0")
