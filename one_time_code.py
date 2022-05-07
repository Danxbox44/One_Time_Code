import secrets
import string


def generate_one_time_code(size=8):
    N = size
    code = "".join(secrets.choice(string.ascii_uppercase + string.digits)for i in range(N))
    return code
