#===============================
# שם : Muhammad Omar Ibrahim
# מספר סטודנט: J0403251093
#===============================


def bellman_ford(graph, start):
    'אלגוריתם בלמן-פורד: מוצא את המרחק הקצר ביותר מצומת ההתחלה לכל שאר הצמתים\n    יתרונות: יכול להתמודד עם קצוות עם משקלים שליליים'
    # אתחול כל המרחקים עם אינסוף ערכים (לא נחקר)
    distances = {node: float('inf') for node in graph}

    # המרחק מההתחלה להתחלה הוא 0 (נקודת התחלה)
    distances[start] = 0

    # בצע הרפיה (עדכון מרחק) (מספר_צומת - 1) פעמים
    # זה מבטיח שכל המרחקים הקצרים ביותר נמצאים
    for _ in range(len(graph) - 1):
        # חזור על כל צומת בגרף
        for node in graph:
            # בדוק כל קצה (שכן) של הצומת הנוכחי
            for neighbor, weight in graph[node].items():
                # הרפיה: אם נמצא נתיב קצר יותר, עדכן את המרחק
                if distances[node] + weight < distances[neighbor]:
                    # עדכן את המרחק הקצר ביותר לשכנים
                    distances[neighbor] = distances[node] + weight

    # החזר מילון המכיל את המרחק הקצר ביותר מההתחלה לכל הצמתים
    return distances