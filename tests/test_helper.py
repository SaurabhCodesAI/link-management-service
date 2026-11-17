from app.utils.helper import generate_identifier

def test_generate_identifier_length():
    result = generate_identifier()
    assert len(result) == 6

def test_generate_identifier_digit_and_letters_only():
    result = generate_identifier()
    assert result.isalnum()
