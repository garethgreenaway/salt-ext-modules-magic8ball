import pytest

pytestmark = [
    pytest.mark.requires_salt_modules("magic_eight_ball.show"),
]


def test_show(salt_call_cli):
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

    ret = salt_call_cli.run("magic_eight_ball.show")
    assert ret.exitcode == 0
    assert ret.json
    assert ret.json in replies
