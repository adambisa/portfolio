import collections
from typing import Tuple, Any
import json


def load_memes(filename: str) -> dict[str, Any]:
    with open(filename) as file:
        memes: dict[str, Any] = json.load(file)
        return memes


def best_average_subreddit(memes: dict[str, Any]) -> str:
    collect_list = collections.defaultdict(list)

    for item in memes["memes"]:
            collect_list[item["subreddit"]].append(int(item["ups"]))
    averages = {sub: sum(scores)/len(scores) for sub, scores in collect_list.items()}
    return max(averages)
def best_from_subreddit(subreddit: str, memes: dict[str, Any]) -> str:
    collect_list= collections.defaultdict(list)
    for subr in memes["memes"]:
        if subr["subreddit"]==subreddit:
            collect_list[subr["postLink"]].append(int(subr["ups"]))
    best_from=max(collect_list, key=collect_list.get)
    return best_from
def best_meme(memes: dict[str, Any]) -> str:
    collect_list= collections.defaultdict(list)
    for meme in memes["memes"]:
        collect_list[meme["postLink"]].append(int(meme["ups"]))
    best_meme=max(collect_list, key=collect_list.get)
    return best_meme 




def analyze_memes(fileName: str) -> Tuple[str, str, str]:

    best_average_subreddit(load_memes(fileName))
    best_from_subreddit( best_average_subreddit(load_memes(fileName)),load_memes(fileName) )
    best_meme(load_memes(fileName))
    return best_average_subreddit(load_memes(fileName)), best_from_subreddit( best_average_subreddit(load_memes(fileName)),load_memes(fileName) ), best_meme(load_memes(fileName))
