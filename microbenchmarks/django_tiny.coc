import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../test/integration/django"))

from django.conf import settings
settings.configure()
from django.template import Context, Template, Node

import time

DJANGO_TMPL = Template("""
{{ col|escape }}
""".strip())

def test_django():
    table = [range(50) for _ in range(50)]
    context = Context({"table": table, 'col': 1})

    times = []

    node = DJANGO_TMPL.nodelist[0]
    context.push()
    for _ in range(100000):
        node.render(context)
    context.pop()
    return times

test_django()
