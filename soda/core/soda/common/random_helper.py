import string
import secrets


def generate_random_alpha_num_str(length: int) -> str:
    return "".join(secrets.choice(string.ascii_lowercase + string.digits) for _ in range(length))
