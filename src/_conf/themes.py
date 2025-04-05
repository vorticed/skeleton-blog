import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '_utils')))
from color import hex_to_hsl

_themes = {
    'is': {
        'light': 'dark:hidden',
        'dark': 'hidden'
    },
    'light': {
        'display': {
            'flex': 'flex',
            'inline': 'inline',
            'block': 'block'
        },
        'colors': {
            'foreground': 'white',
            'background': 'black',
            'primary': 'red',
            'secondary': 'purple'
        },
        'logo': '_static/logos/light.svg',
    },
    'dark': {
        'display': {
            'flex': 'dark:flex',
            'inline': 'dark:inline',
            'block': 'dark:block'
        },
        'colors': {
            'foreground': 'black',
            'background': 'white',
            'primary': 'blue',
            'secondary': 'cyan',
        },
        'logo': '_static/logos/dark.svg'
    },
}
