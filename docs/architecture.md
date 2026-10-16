# 项目架构说明
本项目采用分层架构设计：
1. models/ 提供基础数据源（偏好、座位常量）。
2. core/ 包含核心算法（模型构建 allocator、求解打印 scheduler）。
3. utils/ 提供校验工具。
4. main.py 作为总入口，串联整个流程。