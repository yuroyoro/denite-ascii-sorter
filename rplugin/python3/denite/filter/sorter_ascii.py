# ============================================================================
# FILE: sorter_reverse.py
# AUTHOR: Tomohito OZAKI <ozaki at yuroyoro.com>
# DESCRIPTION: Simple filter to sort candidates by ascii order
# License: MIT license
# ============================================================================
from .base import Base


class Filter(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'sorter_ascii'
        self.description = 'ascii order of candidates'

    def filter(self, context):
        return sorted(context['candidates'], key=lambda x: x['word'])
