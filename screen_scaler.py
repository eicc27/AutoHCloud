import json
"""
Powered by Github Copilot
"""


def scale(t: list[int], r: float) -> list[int]:
    return [int(i  * r) for i in t]

def set_positions(width: int, path="./position.json") -> None:
    """
        Simple function to set the positions of the elements.
    """
    config = json.load(open("position.json", 'r', encoding='utf-8'))
    ratio = width / config["resolution"][0]
    config["resolution"] = [width, int(config["resolution"][1] * ratio)]
    config["upleft"] = scale(config["upleft"], ratio)
    config["downright"] = scale(config["downright"], ratio)
    config["back"] = scale(config["back"], ratio)
    config["serv"] = scale(config["serv"], ratio)
    config["reg"] = scale(config["reg"], ratio)
    config["main"]["non-self"] = scale(config["main"]["non-self"], ratio)
    config["main"]["id"] = scale(config["main"]["id"], ratio)
    config["main"]["name"] = scale(config["main"]["name"], ratio)
    config["main"]["addr"] = scale(config["main"]["addr"], ratio)
    config["main"]["tel"] = scale(config["main"]["tel"], ratio)
    config["main"]["job"]["self"] = scale(config["main"]["job"]["self"], ratio)
    config["main"]["job"]["input"] = scale(config["main"]["job"]["input"], ratio)
    config["main"]["job"]["confirm"] = scale(config["main"]["job"]["confirm"], ratio)
    config["main"]["eula"] = scale(config["main"]["eula"], ratio)
    config["main"]["forward"] = scale(config["main"]["forward"], ratio)
    json.dump(config, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=4)

