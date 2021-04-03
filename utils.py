from pathlib import Path
from typing import List, Optional, Tuple

import streamlit as st

TRANSLATION = {'top': '상의', 'bottom': '하의', 'shoe': '신발'}


def get_fn(path: Path) -> List[Path]:
    return [i for i in path.iterdir() if not i.suffix == '']


def make_selectbox(fn: List[Path], width=None) -> Optional[Path]:
    category = TRANSLATION.get(fn[0].parent.name)
    stem = ['select'] + [i.stem for i in fn]
    item = st.sidebar.selectbox(f'{category} 선택', stem, index=0)
    if item != 'select':
        index = stem.index(item) - 1
        image_path = fn[index]
        st.image(image_path.as_posix(), channels='BGR', width=width)
        return image_path


def remove_path(combi: Tuple[Path, ...]):
    stem = tuple(i.stem for i in combi)
    return stem
