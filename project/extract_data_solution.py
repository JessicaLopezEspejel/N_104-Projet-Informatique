
class ExtractData:

    def __init__(self, data):
        self.data = data

    def get_paper_id(self):
        """It returns the id paper
        :return: id_paper (str)"""
        return self.data['paper_id']

    def get_title(self):
        """
        It returns the title of the paper
        :return: title (str)
        """
        return self.data['metadata']['title']

    def get_text(self):
        """It returns the content of the paper
        :return: text article (str) """
        text = ""
        for dictionary in self.data['body_text']:
            text += dictionary['text'].strip('\n') + " "
        return text

        # import doctest
        # doctest.testmod()