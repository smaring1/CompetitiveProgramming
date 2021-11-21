from collections import deque

tests = int(input())
for i in range(tests):
    queries = int(input())
    st = deque()
    for j in range(queries):
        q = input()
        if ' ' in q:
            val = q.split(' ')[1]
            st.append(int(val))
            
        elif q == '2':
            try:
                st.pop()
            except:
                pass
        elif q == '3':
            if st:
                print(abs(min(st) - max(st)))
            else:
                print("Empty!")