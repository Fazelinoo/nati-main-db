from django import template

register = template.Library()

@register.filter
def split_roles(value, sep=','):
    """Split a comma-separated string into a list, for roles display."""
    if not value:
        return []
    return [r.strip() for r in value.split(sep) if r.strip()]


# Custom filter to check if a string ends with a given suffix
@register.filter
def endswith(value, suffix):
    if not isinstance(value, str):
        return False
    return value.lower().endswith(str(suffix).lower())
