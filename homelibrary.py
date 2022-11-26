
class Media():
    def __init__(self) -> None:
        __file=None
        __id= str()
        _name=str()
        pass

    def _make_unique():
        pass

class Photo(Media):
    def __init__(self,place):
        super(Photo,self).__init__()
        __place=place
        __date=date

class Video(Media):
    def __init__(self,place,discript):
        super(Video,self).__init__()
        __place=place
        __discription=discript

class Book(Media):
    def __init__(self,discript,author):
        super(Book,self).__init__()
        __discription=discript
        __author=author

class Audio(Media):
    def __init__(self,name,author):
        super(Audio,self).__init__()
        __author=author
        __name=name

