links = {}
def find_by_alias(alias):
    if alias in links:
        return links[alias]
    return None

def save_link(alias, target_url):
        links[alias] = target_url