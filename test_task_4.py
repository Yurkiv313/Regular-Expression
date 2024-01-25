from task_4 import validate_phone_number


def test_validate_phone_number():
    valid_numbers = ["(123) 456-7890", "(555) 123-4567", "(999) 888-7777"]
    invalid_numbers = ["123-456-7890", "(12) 3456-7890", "(555) 123-45678"]

    for number in valid_numbers:
        result = validate_phone_number(number)
        print(f"Number: {number}, Valid: {result}")
        assert result

    for number in invalid_numbers:
        result = validate_phone_number(number)
        print(f"Number: {number}, Valid: {result}")
        assert not result


test_validate_phone_number()
