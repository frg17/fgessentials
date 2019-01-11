class Episode:
    #id    Showname            S    E   RESL    SIZE    Released    seeds 
    string_format = "{}\t{:<16}\t{}\t{}\t{}\t{:<10}\t{}\t{}"

    def __init__(self, id, series, season, episode,
                resolution, size, released, seeds, url):
        self.id = id
        self.series = str(series)
        self.season = season
        self.episode = episode
        self.resolution = str(resolution)
        self.size = size
        self.released = str(released)
        self.seeds = seeds
        self.url = url
        

    def __str__(self):
        l = len(self.series)
        cut_string = self.series[:16] if l > 16 else self.series

        return Episode.string_format.format(
            self.id, cut_string, self.season, self.episode,
            self.resolution, self.size, self.released[0:4], self.seeds
        )
