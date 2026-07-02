# 实现顺序

不要同时实现所有模块。每一步完成测试后再进入下一步。

1. `domain/models.py`：理解每个数据对象表示什么。
2. `corruption/base.py`：定义错误注入器的统一接口。
3. `corruption/formatting.py`：实现第一个空格错误注入器。
4. `io/dataset_repository.py`：读取干净CSV并保存脏数据与标准答案。
5. `evaluation/metrics.py`：先实现Exact Match和Over-correction Rate。
6. `cleaners/rule_cleaner.py`：实现最简单的规则基线。
7. `schemas/validator.py`：保护ID和字段类型。
8. `cleaners/llm_cleaner.py`：最后才连接LLM。
9. `cleaners/hybrid_cleaner.py`：组合规则与LLM。
10. `experiments/runner.py`：批量实验。
11. `reporting/report_generator.py`：生成图表和研究报告。

## 第一阶段完成条件

- 相同随机种子产生完全相同的脏数据。
- 每个修改都有标准答案记录。
- 不允许修改受保护字段。
- 原始干净数据始终保持不变。
