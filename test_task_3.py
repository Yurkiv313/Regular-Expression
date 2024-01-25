from task_3 import extract_name_and_domain


def test_extract_name_and_domain():
    email = "john.doe@example.com"
    result = extract_name_and_domain(email)
    print(result)
    assert result == ("john.doe", "example.com")


test_extract_name_and_domain()
