from trading.api.main import connect_app


def test_connect_app() -> None:

    app = connect_app()
    assert app.isConnected() is True
    assert app.connState == 2
