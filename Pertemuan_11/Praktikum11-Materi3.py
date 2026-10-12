#=================================================
# שם : Muhammad Omar Ibrahim
# מספר סטודנט : J0403251093
#יישום dfs
#=================================================
#אנו משתמשים במבנה הנתונים כדי ליצור את התור מספריית אוספי Python המובנית
from collections import deque

#ייצוג גרפי
graph ={
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D':[],
    'E':[],
    'F':[],
    'G':[],

}

def dfs(graph, node, visited):
    #פונקציה לביצוע מעקב אחר גרפים באמצעות DFS
    #גרף : מילון המאחסן גרפים
    #צומת: מאחסן את הצומת שבו ביקרת כעת
    #ביקר: שומר צמתים שביקרו בהם

    #סמן את הצומת הנוכחי כמבקר
    visited.add(node)


    #הצג את הצמתים שבהם ביקרת כעת
    print(node, end=" ")
    for neighbor in graph[node]:
        #אם מעולם לא ביקרו שכנים
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

#סט ביקר
visited=set()

#נתוני ריצה
dfs(graph,"A",visited)