from fgdownload.fgdl import EpisodeViewContainer, Episode, EpisodesFilter, filter_arguments, user_filter
import requests
import os

def download(ep):
    if ep.url[:6] == "magnet":
        os.startfile(ep.url)
    else:
        r = requests.get(ep.url, stream=True)
        with open("temp.torrent", "wb") as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        
        os.startfile("temp.torrent")

def run():
    import sys
    userFilters = filter_arguments() #Parse arguments
    if userFilters == -1:
        return     #Quit if filters are not valid
    
    def fetch_search(search_string):
        """
            Change after testing
        """
        search_string = search_string.split(" ")
        search_string = "-".join(search_string)

        
        search = "https://eztv.io/search/{}".format(search_string)
        r = requests.get(search)
        html = r.text

        return html


    search_string = sys.argv[1]
    html = fetch_search(search_string) # Fetch html

    ep_filter = EpisodesFilter() # Filter instance
    evc = ep_filter.filter(html) # Filter html
    

    for filt in userFilters:  # Apply user filters to EVC
        evc = user_filter(filt[0], filt[1], evc)


    state = True
    evc.print_page(10)
    while state:
        inp = input(">>> ")
        if inp == "":
            if not evc.print_page(10):
                print()
                print("No more results. 'q' to exit.")
        if inp == "q":
            state = False
        
        try:
            ep = int(inp)
            if evc[ep]:
                download(evc[ep])
        except:
            print()


run()
