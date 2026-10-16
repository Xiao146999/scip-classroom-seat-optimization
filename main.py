# main.py 老板
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.seat_allocation.model import build_model
from src.seat_allocation.solver import solve_and_print

if __name__ == "__main__":
    print("开始构建模型...")
    my_model, my_x = build_model()
    print("模型构建完毕，开始求解...\n")
    solve_and_print(my_model, my_x)
