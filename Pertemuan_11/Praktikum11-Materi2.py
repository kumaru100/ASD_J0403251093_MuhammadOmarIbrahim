#=================================================
# שם : Muhammad Omar Ibrahim
# מספר סטודנט : J0403251093
#יישום של bfs
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

def bfs(graph,start):
    #פונקציה לביצוע מעקב אחר גרפים עם bfs
    # גרף : מילון המאחסן את מבנה הגרפים
    # start : צומת ההתחלה של החיפוש

    #תור משמש לאחסון צמתים שיעובדו/יקראו
    queue = deque()

    #משתנה המשמש לאחסון צמתים שעברו עיבוד/ביקור
    visited = set()

    #הכנס את הצומת הראשוני לתור
    queue.append(start)

    #סמן את צומת ההתחלה כצומת ביקר
    visited.add(start)

    while queue:
        node = queue.popleft()

        #הצג את הצמתים שבהם ביקרת כעת
        print(node, end=' ')

        #בדוק את כל השכנים של הצומת שאוחזר:
        for neighbor in graph[node]:
            #אם לא ביקרו שכנים
            if neighbor not in visited:
                #סמן כביקור
                visited.add(neighbor)
                #שים שכנים בתור לעיבוד
                queue.append(neighbor)

#Bfs של צומת A
bfs(graph,'A')
