from fastapi import FastAPI

from socket_back.services.socket_service.service import SocketService


async def init_socket(app: FastAPI) -> None:
    """
    Initialize socket session.

    :param app: current application.
    """
    app.state.socket_session = SocketService()
    await app.state.socket_session.start()


async def shutdown_socket(app: FastAPI) -> None:
    """
    Shutdowm socket session.

    :param app: current application.
    """
    await app.state.socket_session.stop
