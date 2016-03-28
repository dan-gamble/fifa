from jinja2 import contextfilter


@contextfilter
def color_string(context, val):
    if 1 <= val <= 50:
        return 'poor'
    elif 51 <= val <= 60:
        return 'fair'
    elif 61 <= val <= 70:
        return 'average'
    elif 71 <= val <= 80:
        return 'good'
    elif 81 <= val <= 99:
        return 'great'
