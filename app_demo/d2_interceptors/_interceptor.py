from typing import Any

from aidial_interceptors_sdk.chat_completion.base import ChatCompletionInterceptor
from aidial_sdk.chat_completion import Stage
from typing_extensions import override


class PrePostInterceptor(ChatCompletionInterceptor):

    interceptor_name: str

    @override
    async def on_stream_start(self) -> None:
        with Stage(self.response._queue,
                   0,
                   0,
                   f"{self.interceptor_name} Greeting Stage",
                   ) as stage:
            stage.append_content(f"Hi, from {self.interceptor_name} Greeting Stage👋")

    @override
    async def on_stream_end(self) -> None:
        with Stage(self.response._queue,
                   0,
                   1,
                   f"{self.interceptor_name} Goodbye Stage",
                   ) as stage:
            stage.append_content(f"{self.interceptor_name} Goodbye, from {self.interceptor_name} Goodbye Stage👋")

