from main import count_char, check_if_valid_password


def test_valid():
    input = "Bonjourrrrrr"
    expected = True

    assert expected == check_if_valid_password(input)

