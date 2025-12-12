import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import io

st.set_page_config(page_title="解の公式アプリ", layout="centered")

st.title("解の公式（2次方程式 ax²+bx+c=0）")
st.write("係数 a, b, c を入力すると、判別式・解・頂点・グラフを表示します。複素数解にも対応しています。")

# 入力
col1, col2, col3 = st.columns(3)
with col1:
    a = st.number_input('a (2次の係数)', value=1.0, format="%.6f")
with col2:
    b = st.number_input('b (1次の係数)', value=0.0, format="%.6f")
with col3:
    c = st.number_input('c (定数項)', value=0.0, format="%.6f")

# 計算
st.markdown('---')
st.header('計算結果')

# 特別ケース: a == 0 -> 1次方程式または定数
if abs(a) < 1e-12:
    st.warning('a が 0 に近い値です。2次方程式ではなく、1次方程式または定数になります。')
    if abs(b) < 1e-12:
        if abs(c) < 1e-12:
            st.success('恒等式：任意の x が解です（0 = 0）。')
        else:
            st.error('矛盾：解なし（{} = 0 は成り立たない）'.format(c))
    else:
        x = -c / b
        st.write(f'1次方程式の解: x = {x:.6f}')
else:
    D = b**2 - 4*a*c
    st.latex(r"D = b^2 - 4ac")
    st.write('判別式 D =', D)

    # 解の表示（実数/複素数を分ける）
    sqrt_D = None
    if D >= 0:
        sqrt_D = np.sqrt(D)
    else:
        sqrt_D = np.sqrt(-D) * 1j

    x1 = (-b + sqrt_D) / (2*a)
    x2 = (-b - sqrt_D) / (2*a)

    st.subheader('解（近似）')
    def fmt(x):
        if abs(x.imag) < 1e-12:
            return f'{x.real:.6f}'
        else:
            return f'{x.real:.6f} {x.imag:+.6f}j'

    st.write('x₁ =', fmt(x1))
    st.write('x₂ =', fmt(x2))

    # 手順を表示
    st.subheader('計算手順')
    st.markdown(
        f"""
1. 判別式を計算します： $D=b^2-4ac = {b:.6f}^2 - 4\times{a:.6f}\times{c:.6f} = {D:.6f}$
2. 解の公式： $x=\dfrac{{-b\pm\sqrt{{D}}}}{{2a}}$ 
3. 計算結果： $x_1 = {fmt(x1)}$, $x_2 = {fmt(x2)}$
"""
    )

    # 頂点・軸
    h = -b / (2*a)
    k = a*h*h + b*h + c
    st.subheader('放物線の情報')
    st.write(f'頂点 (h, k) = ({h:.6f}, {k:.6f})')
    st.write(f'対称軸 x = {h:.6f}')
    st.write(f'開き: {"上に開く (a>0)" if a>0 else "下に開く (a<0)}')
