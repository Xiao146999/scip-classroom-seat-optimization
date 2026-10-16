def solve_and_print(model, x):
    model.optimize()
    if model.getStatus() == "optimal":
        print(f"最优总满意度: {model.getObjVal():.0f}\n")
        print("座位安排：")
        seat_grid = {}
        for i in ["A","B","C","D","E","F","G","H","I","J","K","L"]:
            for r in [1,2,3,4]:
                for c in [1,2,3,4,5]:
                    if model.getVal(x[i, r, c]) > 0.5:
                        seat_grid[(r, c)] = i
        for r in [1,2,3,4]:
            line = f"第{r}排: "
            for c in [1,2,3,4,5]:
                line += f"[{seat_grid.get((r, c), '·')}] "
            print(line)
    else:
        print(f"求解失败，状态: {model.getStatus()}")