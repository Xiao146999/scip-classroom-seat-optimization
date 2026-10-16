from pyscipopt import Model, quicksum
from seat_allocation.models.student import students, rows, cols, row_pref, col_pref
from seat_allocation.models.preferences import window_cols, aisle_cols


def build_model():
    model = Model("SeatAllocation")

    # 1. 创建变量 x
    x = {}
    for i in students:
        for r in rows:
            for c in cols:
                x[i, r, c] = model.addVar(vtype="B", name=f"x_{i}_{r}_{c}")

    # 2. 目标函数：最大化满意度
    model.setObjective(
        quicksum((row_pref[i][r] + col_pref[i][c]) * x[i, r, c]
                 for i in students for r in rows for c in cols),
        sense="maximize"
    )

    # 3. 约束1：每名学生恰好一个座位
    for i in students:
        model.addCons(quicksum(x[i, r, c] for r in rows for c in cols) == 1)

    # 4. 约束2：每个座位最多一名学生
    for r in rows:
        for c in cols:
            model.addCons(quicksum(x[i, r, c] for i in students) <= 1)

    # 5. 约束3：A、B必须在前两排
    for i in ["A", "B"]:
        model.addCons(quicksum(x[i, r, c] for r in [1, 2] for c in cols) == 1)

    # 6. 约束4：C必须坐在第1排
    model.addCons(quicksum(x["C", 1, c] for c in cols) == 1)

    # 7. 约束5：D和E必须左右相邻（终极修复版）
    y_de = {}
    for r in rows:
        for c in range(1, 5):
            y_de[r, c] = model.addVar(vtype="B", name=f"y_de_{r}_{c}")
            model.addCons(x["D", r, c] + x["E", r, c + 1] + x["E", r, c] + x["D", r, c + 1] >= 2 * y_de[r, c])
            model.addCons(x["D", r, c] + x["D", r, c + 1] + x["E", r, c] + x["E", r, c + 1] <= 2)
    model.addCons(quicksum(y_de.values()) == 1)

    # 8. 约束6：F和G不能左右相邻，也不能前后相邻
    for r in rows:
        for c in range(1, 5):
            model.addCons(x["F", r, c] + x["G", r, c + 1] <= 1)
            model.addCons(x["G", r, c] + x["F", r, c + 1] <= 1)
    for r in range(1, 4):
        for c in cols:
            model.addCons(x["F", r, c] + x["G", r + 1, c] <= 1)
            model.addCons(x["G", r, c] + x["F", r + 1, c] <= 1)

    # 9. 约束7：H必须靠窗
    model.addCons(quicksum(x["H", r, c] for r in rows for c in window_cols) == 1)

    # 10. 约束8：I必须靠过道
    model.addCons(quicksum(x["I", r, c] for r in rows for c in aisle_cols) == 1)

    # 11. 约束9：J和K同一排，但不能相邻
    for r in rows:
        model.addCons(quicksum(x["J", r, c] for c in cols) == quicksum(x["K", r, c] for c in cols))
        for c in range(1, 5):
            model.addCons(x["J", r, c] + x["K", r, c + 1] <= 1)
            model.addCons(x["K", r, c] + x["J", r, c + 1] <= 1)

    # 12. 约束10：任意一排最多4人
    for r in rows:
        model.addCons(quicksum(x[i, r, c] for i in students for c in cols) <= 4)

    # 13. 约束11：第2排至少3人
    model.addCons(quicksum(x[i, 2, c] for i in students for c in cols) >= 3)

    # 14. 约束12：A和C不能同列
    for c in cols:
        model.addCons(quicksum(x["A", r, c] for r in rows) + quicksum(x["C", r, c] for r in rows) <= 1)

    # 15. 约束13：B和L不能同排
    for r in rows:
        model.addCons(quicksum(x["B", r, c] for c in cols) + quicksum(x["L", r, c] for c in cols) <= 1)

    return model, x