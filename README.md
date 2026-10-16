# 教室座位分配优化项目 (Classroom Seat Allocation)

基于 SCIP 求解器的 0-1 整数规划项目，用于解决教室座位分配问题，在满足所有硬性约束的前提下，最大化学生的总满意度。

## 📁 项目结构
采用标准 Python 工程结构：
- `src/seat_allocation/`: 核心源代码（数据、模型、求解器）
- `tests/`: 单元测试代码
- `data/`: 数据文件夹
- `main.py`: 程序入口
- `requirements.txt`: 项目依赖清单

## 🛠️ 环境依赖
- Python 3.10+
- PySCIPOpt

可以通过以下命令一键安装依赖：
```bash
pip install -r requirements.txt
