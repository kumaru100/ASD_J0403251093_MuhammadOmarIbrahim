#===============================
# שם : Muhammad Omar Ibrahim
# מספר סטודנט: J0403251093
#===============================


# ייבוא heapq עבור תור עדיפות (מיני-ערימה)
import heapq

# הגדר גרף משוקלל כמילון מקונן
# פורמט: {צומת: {שכן: edge_weight, ...}}
graph = {
    'A': {'B': 4, 'C': 2},  # מ-A עד B משקל 4, למשקל C 2
    'B': {'D': 5},          # מ-B עד D משקל 5
    'C': {'D': 1},          # מ-C ל-D משקל 1
    'D': {}                 # D הוא צומת היעד, אין קצוות יוצאים
}

def dijkstra(graph, start):
    'האלגוריתם של Dijkstra: מוצא את המרחק הקצר ביותר מצומת ההתחלה לכל שאר הצמתים\n    שיטה: אלגוריתם חמדן משתמש בתור עדיפות'
    # אתחול כל המרחקים עם אינסוף ערכים (לא נחקר)
    distances = {node: float('inf') for node in graph}

    # המרחק מההתחלה להתחלה הוא 0 (נקודת התחלה)
    distances[start] = 0

    # תור עדיפות מאחסן tuple (distance_from_start, node)
    # Min-heap מבטיח שהצומת עם המרחק הקטן ביותר יעובד ראשון
    pq = [(0, start)]

    # עבד עד שכל הצמתים שניתן להגיע אליהם עברו עיבוד
    while pq:
        # קח את הצומת עם המרחק הקטן ביותר מתור העדיפות
        current_distance, current_node = heapq.heappop(pq)

        # בדוק את כל השכנים של הצומת הנוכחי
        for neighbor, weight in graph[current_node].items():
            # חשב את המרחק החדש: מרחק נוכחי + משקל קצה לשכן
            distance = current_distance + weight

            # אם נמצא מרחק קצר יותר לשכן, עדכן
            if distance < distances[neighbor]:
                # עדכן את המרחק הקצר ביותר לשכנים
                distances[neighbor] = distance
                # הוסף שכן לתור העדיפות לעיבוד
                heapq.heappush(pq, (distance, neighbor))

    # החזר מילון המכיל את המרחק הקצר ביותר מההתחלה לכל הצמתים
    return distances

# בצע את האלגוריתם של דיקסטרה מהצומת 'A'
hasil = dijkstra(graph, 'A')

# הצג את התוצאות של המרחק הקצר ביותר מ-A לכל צומת
print('המרחק הקצר ביותר מצומת A:')
for node, distance in hasil.items():
    print(f"A ke {node}: {distance}")