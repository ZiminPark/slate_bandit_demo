from itertools import product
from pathlib import Path
from typing import Dict, List, Tuple

from numpy.random import binomial
from streamlit import cache


@cache()
def make_reward(tops: List[Path], bottoms: List[Path], shoe: List[Path]):
    combi = product(tops, bottoms, shoe)
    return {combi: rank + 1 for rank, combi in enumerate(combi)}


@cache()
def observe(top: Path, bottom: Path, shoe: Path, combi_reward: Dict[Tuple[Path, ...], float]):
    prob = combi_reward.get((top, bottom, shoe), 0) / len(combi_reward)
    return prob, binomial(1, prob)
