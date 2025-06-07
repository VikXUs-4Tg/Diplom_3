import random
import string


class Tools:

    @staticmethod
    def check_text_of_element(expected_value, actually_value):
        assert expected_value in actually_value, f'\nОжидаемое значение:\n"{expected_value}"\nФактическое значение:\n"{actually_value}"'

    @staticmethod
    def replace_string_in_locator(locator, string_to_replace, new_string):
        return locator.replace(string_to_replace, new_string)

class Generators:

    @staticmethod
    def generate_random_email():
        login_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(3, 10)))
        email_name = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
        email_domain = ''.join(random.choices(string.ascii_lowercase, k=2))
        return f"{login_name}@{email_name}.{email_domain}"

    @staticmethod
    def generate_random_password():
        allowed_chars = string.digits
        random_password = ''.join(random.choices(allowed_chars, k=8))
        return random_password