import re


def is_valid_email(email: str) -> bool:
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None


# Example usage
email1 = "example@domain.com"
email2 = "invalid-email@domain"

print(f"{email1} is valid: {is_valid_email(email1)}")  # Should return True
print(f"{email2} is valid: {is_valid_email(email2)}")  # Should return False
