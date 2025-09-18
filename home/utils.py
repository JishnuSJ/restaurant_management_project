def generate_coupen_code(length=10):
    "generate a alphanumberic coupen code"
    characters = string.ascii_uppercase+string.digits
    while True:
        code=' '.join(secret.choice(characters)for _ in range(length))
        if not Coupen.objects.filter(code=code).exists():
            return code