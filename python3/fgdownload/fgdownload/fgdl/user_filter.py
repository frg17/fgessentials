from . import EpisodeViewContainer

def user_filter(u_filter, value, container):
    evc = EpisodeViewContainer()

    value = int(value)

    if u_filter == "-s":
        for ep in container:
            if int(ep.season) == value:
                evc.append(ep)
    elif u_filter == "-e":
        for ep in container:
            if int(ep.episode) == value:
                evc.append(ep)

    evc.reset_ids()
    return evc