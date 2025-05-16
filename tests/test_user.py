from agora_library_server.models.user import User


def test_user_creation_must_return_created_user():
    user_created = User(
        name='roberto',
        username='robertopicas',
        email='roberto@roberto.com',
        password='senha muito forte',
    )

    assert user_created == User(
        name='roberto',
        username='robertopicas',
        email='roberto@roberto.com',
        password='senha muito forte',
    )
