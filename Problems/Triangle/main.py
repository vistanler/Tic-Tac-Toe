numb = int(input())
for i in range(numb):
    st = ''.join(['#' for s in range(2 * i + 1)])
    print(st.center((numb - 1) * 2 + 1))