def is_valid_email(email):
    "add valid email,phone"
    try:
        validate_email(email,check_deliverability=False)
        return True
    except EmailNotValidError as e:
        logger.warning(f"invalid email"{email}:{str(e)})
        return False