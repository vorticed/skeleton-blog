from dataclasses import asdict
from sphinxawesome_theme import ThemeOptions, LinkIcon
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'content')))

language =  'pt'

extensions = [
    'myst_parser',
    'sphinx_frontmatter',
    'sphinx_slugger'
]


templates_path = ['templates']
exclude_patterns = []

html_theme = 'sphinxawesome_theme'
html_static_path = ['static', '../assets']
html_permalinks_icon = "<span>#</span>"

html_favicon = 'static/favicon.svg'
html_search_language = 'pt'
html_show_sphinx = False
html_link_suffix = ''

html_sidebars = {
  "**": [
      "sidebar.html",
      "sidebar_main_nav_links.html",
      "sidebar_toc.html"
    ]
}

available_themes = ['dark', 'light']

html_context = {}
html_context['theme'] = _themes
html_context['available_themes'] = available_themes
html_context['footer_files'] = collect('../content/footer')

html_css_files = ['css/theme.css']

theme_options = ThemeOptions(
    show_breadcrumbs=True,
    main_nav_links=_header['nav']['entries'],
    awesome_headerlinks=True,
    show_prev_next=True
)

html_theme_options = asdict(theme_options)
