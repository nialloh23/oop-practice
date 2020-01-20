import datetime

last_id = 0


class Note:
    """Represent a note in the notebook. Match string in searches and store tags for each note."""

    def __init__(self, memo, tags=''):
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        """Determine if this note matches the filter text. Search is case sensitive and matches tags and text"""
        return filter in self.memo or filter in self.tags