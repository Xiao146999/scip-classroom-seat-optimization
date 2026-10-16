from src.seat_allocation.core.allocator import build_model
def test_model_builds_successfully():
    """最简单的测试：检查模型是否能成功建立"""
    model, x = build_model()
    assert model is not None
    assert len(x) == 240  # 12名学生 * 4排 * 5列 = 240个变量
    print("测试通过：模型建立成功，变量数量正确！")

if __name__ == "__main__":
    test_model_builds_successfully()