from datetime import datetime
from apis.models import SeriesNumber


def count_string_header(text, find_string):
    count = 0
    for char in text:
        if char == find_string:
            count += 1
        else:
            return count
    else:
        return count


def make_naming_series(naming_series: str):
    result = ''
    has_number = False
    pattern = naming_series.split('.')
    for text in pattern:
        if 'YYYY' in text:
            result += text.replace('YYYY', str(datetime.today().year))
        elif 'YY' in text:
            result += text.replace('YYYY', str(datetime.today().year)[-2:])
        elif 'MM' in text:
            result += text.replace('MM', str(datetime.today().month).zfill(2))
        elif 'DD' in text:
            result += text.replace('DD', str(datetime.today().day).zfill(2))
        elif '#' in text:
            result += "." + text
            has_number = True
        else:
            result += text
    if not has_number:
        result += '.#####'
    return result


def get_naming_series(naming_series: str):
    pattern = naming_series.split('.')
    if len(pattern) == 2:
        obj, created = SeriesNumber.objects.get_or_create(naming_series=pattern[0])
        if obj:
            running_number = obj.running_number
            len_char = count_string_header(pattern[1], '#')
            name = pattern[0] + str(running_number).zfill(len_char)
            obj.running_number += 1
            obj.save()
            return name
    else:
        return None


# naming_series = "SO-.YYYY-.MM-.DD-.#####"
# make_naming_series = make_naming_series(naming_series)
# naming = get_naming_series(make_naming_series)
