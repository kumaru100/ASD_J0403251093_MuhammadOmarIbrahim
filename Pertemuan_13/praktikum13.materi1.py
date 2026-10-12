# שם : Muhammad Omar Ibrahim
# מספר סטודנט : J0403251093
# כיתה : TPL B1
# מעשי 13 - גרף III: עץ משתרע


# ==========================================================
# יישום קרוסקל
# ==========================================================

# רשימת קצה: (משקל, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# ממיין קצוות לפי משקל
edges.sort()

mst = []
total_weight = 0

# הגדרה פשוטה עבור צמתים שכבר נבחרו
connected = set()

for weight, u, v in edges:
    # אם הקצוות לא יוצרים מחזור פשוט
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)

print('עץ טווח מינימלי:')
for edge in mst:
    print(edge)

print('משקל כולל =', total_weight)