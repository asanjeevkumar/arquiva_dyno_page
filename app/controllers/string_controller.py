class StringController:
    def __init__(self):
        self._current_string = "dynamic string"

    def get_current_string(self) -> str:
        return self._current_string

    def update_string(self, new_string: str) -> dict:
        self._current_string = new_string
        return {"message": "String updated successfully", "new_string": new_string} 