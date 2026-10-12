# שם : Muhammad Omar Ibrahim
# מספר סטודנט : J0403251093
# כיתה : TPL B1
# מעשי 13 - גרף III: עץ משתרע


import heapq

graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}


def prim(graph, start):
    visited = set([start])
    edges = []

    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    while edges:
        weight, u, v = heapq.heappop(edges)

        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight

            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight


mst, total = prim(graph, 'A')

print('עץ טווח מינימלי:')
for edge in mst:
    print(edge)

print('משקל כולל =', total)

# תשובה לניתוח:
# 1. באיזה צומת התחלה משתמשים?
# 2. איזה קצה נבחר ראשון?
# 3. איך Prim קובע את הקצה הבא?
# 4. מהו המשקל הכולל של ה-MST המיוצר?
# 5. במה נבדלות הגישות של פרים וקרוסקל?

# תשובה לניתוח:
# 1. הצומת הראשוני בשימוש הוא 'A'.
# 2. הקצה שנבחר ראשון הוא (2, 'A', 'C') מכיוון שיש לו את המשקל הקטן ביותר.
# 3. הקצה הבא נקבע על ידי בחירת הקצה בעל המשקל הקטן ביותר מכל הקצוות
# מחובר לקודקוד שכבר ביקר בו. הקצה נבחר אם הוא הולך לקודקוד שלא ביקר בו, כדי לא ליצור מחזור.
# 4. המשקל הכולל של ה-MST שהתקבל הוא 6 (2 + 1 + 3).
# 5. ההבדל בין פרים לקרוסקל הוא שפריים מתחיל מקודקוד אחד, ואז בוחר קצוות עם משקלים
# הקטן ביותר מחובר לקודקוד שכבר ביקר.
# בינתיים, Kruskal בוחר את הקצה עם המשקל הקטן ביותר מהגרף כולו, ואז מכניס אותו ל-MST כל עוד הוא לא יוצר מחזור.
