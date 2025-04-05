from dataclasses import asdict
from sphinxawesome_theme import ThemeOptions, LinkIcon
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'content')))
from _conf.header import _header
from _conf.sidebar import _sidebar
from _conf.post import _post
from _conf.themes import _themes
from _conf.share import _share
from _conf.footer import _footer
from _utils.collector import collect

language =  'pt'

extensions = [
    'myst_parser',
    'sphinx_frontmatter',
    'sphinx_slugger'
]


templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinxawesome_theme'
html_static_path = ['_static', '../assets']
html_permalinks_icon = "<span>#</span>"

html_favicon = '_static/favicon.svg'
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
html_context['header'] = _header
html_context['sidebar_links'] = _sidebar
html_context['post'] = _post
html_context['share'] = _share
html_context['footer'] = _footer
html_context['footer_files'] = collect('../content/footer')

html_css_files = ['css/theme.css']

theme_options = ThemeOptions(
    show_breadcrumbs=True,
    main_nav_links=_header['nav']['entries'],
    awesome_headerlinks=True,
    show_prev_next=True
)

html_theme_options = asdict(theme_options)
