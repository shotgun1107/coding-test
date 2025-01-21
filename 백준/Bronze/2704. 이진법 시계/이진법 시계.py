n = int(input())

for _ in range(n):
    h, m, s = map(int, input().strip().split(':'))
    
    h_bin = f'{h:06b}'
    m_bin = f'{m:06b}'
    s_bin = f'{s:06b}'
    
    col = h_bin[0] + m_bin[0] + s_bin[0] + h_bin[1] + m_bin[1] + s_bin[1] + \
          h_bin[2] + m_bin[2] + s_bin[2] + h_bin[3] + m_bin[3] + s_bin[3] + \
          h_bin[4] + m_bin[4] + s_bin[4] + h_bin[5] + m_bin[5] + s_bin[5]
    
    row = h_bin + m_bin + s_bin
    
    print(col, row)