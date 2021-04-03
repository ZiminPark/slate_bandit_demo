from operator import itemgetter

from reward import make_reward, observe
from utils import *

clothe_path = Path('./clothes')
top_fn = get_fn(clothe_path / 'top')
bottom_fn = get_fn(clothe_path / 'bottom')
shoe_fn = get_fn(clothe_path / 'shoe')
combi_reward = make_reward(top_fn, bottom_fn, shoe_fn)

st.title('소개팅 옷 고르기')
st.sidebar.title('상의, 하의, 신발 선택')

top = make_selectbox(top_fn)
bottom = make_selectbox(bottom_fn)
shoe = make_selectbox(shoe_fn, width=150)

if st.sidebar.checkbox('소개팅이 성공할까요?'):
    if not all((top, bottom, shoe)):
        st.sidebar.text('상품을 선택해주세요!')
    else:
        prob, reward = observe(top, bottom, shoe, combi_reward)
        text = '성공!' if reward else '실패 ㅠㅠ'
        st.sidebar.text(text)
        st.sidebar.text(f'이 조합의 평균 reward는 {prob:.2f} 입니다.')

if st.sidebar.checkbox('Top5 조합 보기'):
    top = dict(sorted(combi_reward.items(), key=itemgetter(1), reverse=True)[:5])
    top = {remove_path(combi): mean / len(combi_reward) for combi, mean in top.items()}
    for i in top:
        st.sidebar.text(f'{i}, {top[i]:.2f}')
