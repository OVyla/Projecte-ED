class VideoData:
    def __init__(self):
        pass

    def add_video(self, uuid: str, file: str) -> None:
        pass

    def remove_video(self, uuid: str) -> None:
        pass

    def load_metadata(self, uuid: str) -> None:
        pass

    def get_duration(self, uuid: str) -> str:
        pass

    def get_title(self, uuid: str) -> str:
        pass

    def get_album(self, uuid: str) -> str:
        pass

    def get_artist(self, uuid: str) -> str:
        pass

    def get_composer(self, uuid: str) -> str:
        pass

    def get_genre(self, uuid: str) -> str:
        pass

    def get_date(self, uuid: str) -> str:
        pass

    def get_comment(self, uuid: str) -> str:
        pass
