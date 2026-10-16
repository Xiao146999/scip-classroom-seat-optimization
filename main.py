import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

from seat_allocation.core.allocator import build_model
from seat_allocation.core.scheduler import solve_and_print

if __name__ == "__main__":
    print("开始构建模型...")
    my_model, my_x = build_model()
    print("模型构建完毕，开始求解...\n")
    solve_and_print(my_model, my_x)
