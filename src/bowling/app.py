class Frame:
    pass


class Line:
    def __init__(self):
        self.frames = []

    def create_frame(self):
        frame = Frame()
        self.frames.append(frame)
