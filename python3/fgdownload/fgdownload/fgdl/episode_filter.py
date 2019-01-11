from . import EpisodeViewContainer
from . import Episode
import re

class EpisodesFilter:

    def __init__(self):
        self.reg_get_all = r"(<table [^>]* class=\"forum_header_border\">[\s\S]*</table>)"
        self.reg_get_data_cells = r"<tr [^>]*>\s*<td [^>]*>.*</td>\s*(<td [^>]*>[\s\S]*?</td>)\s*(<td [^>]*>[\s\S]*?</td>)\s*(<td [^>]*>[\s\S]*?</td>)\s*(<td [^>]*>[\s\S]*?</td>)\s*(<td [^>]*>[\s\S]*?</td>)[\s\S]*?</tr>"
        self.reg_columns = [
            r"<td [^>]*>[\s\S]*<a [^>]*>(.*) (?:(?:S|s)(\d\d)(?:E|e)(\d\d))(?:.*?(\d\d\dp))?.*</a>",
            r"href=\"(?:(magnet:\?.*?)|(.*?\.torrent))\"",
            r">(\d+\.?\d* (?:M|G)B)<",
            r">(.*)<",
            r"<font .*?>(.*)</font>"
        ]


    
    def _filter_table(self, html):
        program = re.compile(self.reg_get_all)
        result = program.search(html)
        if result is not None:
            return result.group(0)
        else:
            print("No table found")
            return None
    

    def _filter_cells(self, html):
        """
            Filter table data cells that are
            wanted from each row
        """
        all_matches = re.findall(self.reg_get_data_cells, html)

        if len(all_matches) is not 0:
            return all_matches
        else:
            return None


    def _extract_info(self, episode_infos):
        """
            Returns a containing lists of extracted information.
        """
        # Create regex programs
        programs = []
        for reg in self.reg_columns:
            programs.append(re.compile(reg))


        extracted_infos = []  # All extracted info.
        for row in episode_infos: # For each row
            info = []
            for i in range(5): # For each table cell
                # Extract information with corresponding program
                result = programs[i].search(row[i])
                if result is None:
                    info.append(None)
                else:
                    info.append(result.groups())

            extracted_infos.append(info)

        return extracted_infos

    def _make_episode_list(self, extracted):
        episodes = []

        for inf in extracted:
            if inf[0] is None or inf[1] is None or inf[2] is None or inf[4]is None:
                continue
            else:
                cells = []
                for row in inf:
                    for data in row:
                        cells.append("" if data is None else data)
                        if len(row) == 2:
                            break
                episodes.append(cells)

        evc = EpisodeViewContainer()
        for i in range(len(episodes)):
            evc.append(Episode(
                i,
                episodes[i][0],
                episodes[i][1],
                episodes[i][2],
                episodes[i][3],
                episodes[i][5],
                episodes[i][6],
                episodes[i][7],
                episodes[i][4]
            ))
        return evc

            

    def filter(self, html):
        # Get table
        html = self._filter_table(html)
        if html is None:
            return None
        
        episode_infos = self._filter_cells(html)

        extracted_info = self._extract_info(episode_infos)
    
        return self._make_episode_list(extracted_info)
