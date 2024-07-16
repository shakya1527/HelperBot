import random


class Emoji:
    """Class to get a random emoji from a list of emojis
    """

    def __init__(self):
        """Constructor to initialize the list of emojis
        """
        self.emojis = [
            "😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣", "😊", "😇",
            "🙂", "🙃", "😉", "😌", "😍", "🥰", "😘", "😗", "😙", "😚",
            "😋", "😛", "😜", "🤪", "😝", "🤑", "🤗", "🤭", "🤫", "🤔",
            "🤐", "🤨", "😐", "😑", "😶", "😏", "😒", "🙄", "😬", "😮",
            "😯", "😳", "🤯", "😰", "😨", "😣", "😢", "😭", "😱", "😖",
            "😕", "😔", "😞", "😟", "😤", "😢", "😭", "😦", "😧", "😨",
            "😩", "🤯", "😬", "😰", "😱", "😳", "🤪", "😵", "🥴", "😠",
            "😡", "🤬", "😷", "🤒", "🤕", "🤢", "🤮", "🤧", "😇", "🤠",
            "🤡", "🥳", "🥴", "🥺", "🤥", "🤫", "🤭", "🧐", "🤓", "😈",
            "👿", "👹", "👺", "💀", "👻", "👽", "👾", "🤖", "💩", "😺",
            "😸", "😹", "😻", "😼", "😽", "🙀", "😿", "😾"
        ]

    def get_random_emoji(self):
        """Method to get a random emoji from the list

        Returns:
            str: Random emoji from the list
        """
        return random.choice(self.emojis)
