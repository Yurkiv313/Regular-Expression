from task_2 import validate_date_format


def test_validate_date_format():
    valid_dates = ["01/15/2023", "12/31/2024", "06/02/2022"]
    invalid_dates = ["13/01/2023", "00/31/2024", "06-02-2022"]

    for date in valid_dates:
        result = validate_date_format(date)
        print(f"Date: {date}, Valid: {result}")
        assert result

    for date in invalid_dates:
        result = validate_date_format(date)
        print(f"Date: {date}, Valid: {result}")
        assert not result


test_validate_date_format()
