class EmptyValueError(ValueError):
    """When no value provided"""


class InvalidValueError(ValueError):
    """When does not fit requirements"""


class Validator:
    def validate(self, value, required=True, **kwargs):
        if required and (value is None or not value.strip()):
            raise EmptyValueError('cannot be empty')
        return value.strip()


class Text(Validator):
    def validate(self, value, max_length=255, **kwargs):
        v = super().validate(value, **kwargs)
        if len(v) > max_length:
            raise InvalidValueError(f"cannot exceed {max_length} chars")
        return v


class ShortText(Text):
    def validate(self, value, **kwargs):
        return super().validate(value, max_length=25)


class InsensitiveText(Text):
    def validate(self, value, **kwargs):
        return super().validate(value, **kwargs).lower()


class Birthdate(ShortText):
    def validate(self, value, **kwargs):
        return super().validate(value, **kwargs)
