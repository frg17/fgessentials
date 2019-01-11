from . import Episode

class EpisodeViewContainer:
    """
        Container holding gathered instances of Episodes that
        can be downloaded. 
        Handles presentation.
    """

    def __init__(self):
        self.episodes = []
        self.next_print = 0 #Next episode that should be printed
        self.next_grey = False
    
    def __getitem__(self, k):
        return self.episodes[k]

    def reset_ids(self):
        for i in range(len(self.episodes)):
            self.episodes[i].id = i
    

    def append(self, episode):
        if not isinstance(episode, Episode):
            raise Exception("append() from EpisodeViewContainer needs an Episode object.")

        self.episodes.append(episode)


    def print_page(self, page_length):
        """
            Prints info for n episodes.
            n = page_length.
            Does not print the same episodes again.
        """
        l = len(self.episodes)

        if self.next_print == l:
            return False
        
        for i in range(page_length):
            if self.next_print < l:
                print(str(self[self.next_print]))
                self.next_print += 1
            else:
                break

        return True