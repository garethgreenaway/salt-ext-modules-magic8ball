import pytest
import salt.modules.test as testmod  # pylint: disable=import-error
import saltext.eight_ball.modules.eight_ball_mod as eight_ball_module


@pytest.fixture
def configure_loader_modules():
    module_globals = {
        "__salt__": {"test.echo": testmod.echo},
    }
    return {
        eight_ball_module: module_globals,
    }


def test_show():
    replies = [
        {"result": True, "message": "Signs point to yes"},
        {"result": True, "message": "Without a doubt"},
        {"result": True, "message": "You may rely on it"},
        {"result": False, "message": "Do not count on it"},
        {"result": True, "message": "Looking good"},
        {"result": False, "message": "Cannot predict now"},
        {"result": True, "message": "It is decidedly so"},
        {"result": False, "message": "Outlook not so good"},
    ]

    ret = eight_ball_module.show()
    assert ret in replies
