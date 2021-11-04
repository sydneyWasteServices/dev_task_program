class Utils:
    def __init__(self):
        return

    def flatten(self, nest_list :list):
            return [item for sublist in nest_list for item in sublist]
