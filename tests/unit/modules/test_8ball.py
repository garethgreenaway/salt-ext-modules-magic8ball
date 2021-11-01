import pytest
import salt.modules.test as testmod
import saltext.eight_ball.modules.eight_ball_mod as eight_ball_module


@pytest.fixture
def configure_loader_modules():
    module_globals = {
        "__salt__": {"test.echo": testmod.echo},
    }
    return {
        eight_ball_module: module_globals,
    }


def test_replace_this_this_with_something_meaningful():
    echo_str = "Echoed!"
    assert eight_ball_module.example_function(echo_str) == echo_str
