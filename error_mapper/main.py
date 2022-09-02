import re

DEFAULT_PRIORITY = 1
ERROR_MAP = [
    {
        'pattern': 'Partial match',
        'message': 'This is converted message of Partial match',
        'propagate': True,
    },
    {
        'pattern': '^Full match$',
        'message': 'This is converted message of Full match',
        'propagate': True,
    },
    {
        'pattern': 'Error with priority',
        'message': 'This is converted message of Error with priority',
        'propagate': True,
    },
    {
        'pattern': 'Error with priority',
        'message': 'This is converted message of Error with higher priority',
        'propagate': True,
        'priority': 100,
    },
    {
        'pattern': 'Error with priority',
        'message': 'This is converted message of Error with even higher priority',
        'propagate': True,
        'priority': 200,
    },
    {
        'pattern': '.*',
        'message': 'Something went wrong',
        'propagate': True,
    },
]


def _matches(pattern, text):
    try:
        return bool(re.search(pattern, text))
    except:
        return pattern == text


def map_to_error(error_message, propagate = False):
    message, propagate = error_message, propagate
    max_priority = 0

    for error in ERROR_MAP:
        priority = error.get('priority', DEFAULT_PRIORITY)
        pattern = error['pattern']
        if priority > max_priority and _matches(pattern, error_message):
            message = error['message']
            propagate = error.get('propagate', False)
            max_priority = priority
    
    return {
        'message': message,
        'propagate': propagate,
    }

if __name__ == '__main__':
    print(map_to_error('Valid Partial match............'))
    print(map_to_error('Full match'))
    print(map_to_error('Invalid Full match............'))
    print(map_to_error('Error with priority'))
    print(map_to_error('Unknown error'))
