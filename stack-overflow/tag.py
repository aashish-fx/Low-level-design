class Tag:
    def __init__(self, tagname: str):
        self.tagname = tagname

    @property
    def tag_name(self):
        return self.tagname

    @tag_name.setter
    def tag_name(self, name: str):
        self.tagname = name
