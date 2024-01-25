from task_1 import find_emails


def test_find_email():
    text = "Sample text with email addresses: john.doe@example.com, alice.smith@gmail.com, info@company.org"
    emails = find_emails(text)

    for email in emails:
        print(f"Email: {email}")

    assert emails == [
        "john.doe@example.com",
        "alice.smith@gmail.com",
        "info@company.org",
    ]


test_find_email()
