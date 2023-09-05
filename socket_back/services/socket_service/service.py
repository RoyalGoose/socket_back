import asyncio


class SocketService:
    """Class for managing socket service."""

    async def start(self) -> None:
        """Start socket session."""
        self.recieve_messages_task = asyncio.create_task(
            self.recieve_messages(),
        )
        await self.recieve_messages_task

    async def recieve_messages(self) -> None:
        """Recieve messages from socket."""
        while True:  # noqa: WPS457
            print("We are into infinity loop")  # noqa: 421
            await asyncio.sleep(0.1)

    async def stop(self) -> None:
        """Stop socket session."""
        self.recieve_messages_task.cancel()
