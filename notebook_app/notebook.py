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


class Notebook:
    """Represents a collection of notes that can be tagged, modified and searched"""

    def __init__(self):
        """Initializes a notebook with an empty list"""
        self.notes = []

    def new_note(self, memo, tags=''):
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id, memo):
        """Find the note with the given id and change its memo to the given value."""
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False

    def modify_tags(self, note_id, tags):
        note = self._find_note(note_id)
        if note:
            note.tags = tags
            return True
        return False

    def _find_note(self, note_id):
        """Locate the note with the given id."""
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None

    def search(self, filter):
        """Find all notes that match given filter string"""
        return [note for note in self.notes if note.match(filter)]
