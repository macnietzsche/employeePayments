
class InputHandler():
    def __init__(self, plain_text_line) -> None:
        self.validated_input_line = plain_text_line

    @property
    def validated_input_line(self):
        return self._validated_input_line
    
    @validated_input_line.setter
    def validated_input_line(self, plain_text_line):
        validated_input = None
        self._validated_input_line = validated_input