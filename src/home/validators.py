from django.core.exceptions import ValidationError


def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value)s is not an even number',
            params={'value': value},
        )


def validate_email(value):
    email = value
    if ".edu" in email:
        raise ValidationError("Not a accept edu name")


CATEGORIES = ["Electronic","Car","Laptop","Mobile","Cooking","Sports"]


def validate_category(value):
    cat = value.upper()
    print(cat)
    if not value in CATEGORIES and not cat in CATEGORIES:
        raise ValidationError("IS NOT A VALID CATEGORIES")