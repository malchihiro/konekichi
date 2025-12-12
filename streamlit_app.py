import streamlit as st
return f"{re} {'+' if im>=0 else '-'} {abs(im)}i"
else:
v = float(x)
if abs(v - round(v)) < 1e-9:
return str(int(round(v)))
return f"{v:.6g}"


st.write("- 解 1：", fmt(x1))
st.write("- 解 2：", fmt(x2))


# show step-by-step numeric substitution
st.subheader("代入して解を求める過程（数値代入）")
st.markdown(f"$D = {b}^2 - 4\times({a})\times({c}) = {D}$")
st.markdown(f"$x = \dfrac{{-{b} \pm \sqrt{{{D}}}}}{{2\times({a})}}$")
st.markdown(f"$x_1 = \dfrac{{-{b} + \sqrt{{{D}}}}}{{{2*a}}} = {fmt(x1)}$")
st.markdown(f"$x_2 = \dfrac{{-{b} - \sqrt{{{D}}}}}{{{2*a}}} = {fmt(x2)}$")


# Plot the quadratic function
st.subheader("関数のグラフ: y = ax² + bx + c")
# choose x-range around the vertex and roots
vertex_x = -b / (2 * a)
vertex_y = a * vertex_x ** 2 + b * vertex_x + c


# pick x-limits
span = 5.0
# if real roots exist, center around them
if D >= 0 and (not np.iscomplex(x1)) and (not np.iscomplex(x2)):
xs_min = min(x1, x2, vertex_x) - span
xs_max = max(x1, x2, vertex_x) + span
else:
xs_min = vertex_x - span
xs_max = vertex_x + span


xs = np.linspace(xs_min, xs_max, 400)
ys = a * xs ** 2 + b * xs + c


fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(xs, ys)
ax.axhline(0, linewidth=0.8)
ax.axvline(vertex_x, linestyle='--', linewidth=0.8)
ax.scatter([vertex_x], [vertex_y], zorder=5)
ax.annotate(f"頂点 ({vertex_x:.3g}, {vertex_y:.3g})", (vertex_x, vertex_y), xytext=(10, -30), textcoords='offset points')


# mark real roots
if D > 0:
ax.scatter([x1, x2], [0, 0], zorder=5)
ax.annotate(f"x1={fmt(x1)}", (x1, 0), xytext=(5, 5), textcoords='offset points')
ax.annotate(f"x2={fmt(x2)}", (x2, 0), xytext=(5, -15), textcoords='offset points')
elif abs(D) < 1e-12:
ax.scatter([x1], [0], zorder=5)
ax.annotate(f"重解 x={fmt(x1)}", (x1, 0), xytext=(5, 5), textcoords='offset points')
else:
ax.text(0.02, 0.95, "実根なし（虚数解）", transform=ax.transAxes, verticalalignment='top')


ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title(f"y = {a}x² + {b}x + {c}")
ax.grid(True, linestyle=':', linewidth=0.6)
st.pyplot(fig)


# allow download of the plotted image
buf = BytesIO()
fig.savefig(buf, format='png', bbox_inches='tight')
buf.seek(0)
st.download_button(label="グラフ画像をダウンロード (PNG)", data=buf, file_name='quadratic_plot.png', mime='image/png')


st.write("---")
st.caption("このアプリは Streamlit で作られています。改善や機能追加 (複素平面表示、ステップごとのアニメーション等) を希望する場合は教えてください。") # 2進数の表示をハイライト
