# Dots Learning

按算法主题整理 Dian 与 dot 的学习记录。每个主题保留：问题、直觉与不变量、复杂度、边界与反例、可运行实现和测试。新讨论继续补入对应主题，不按聊天日期重复建档。

## 索引
| 主题 | 本次重点 |
| --- | --- |
| [滑动窗口与单调队列](sliding_window/README.md) | 最近 k 项的最大值；为什么队尾可以删除 |
| [流式窗口计数](streaming_counts/README.md) | 最近一段时间的品类频次；没有新事件时查询仍需过期清理 |

## 约定
- 本目录独立维护，不重构历史题解。原专题可参考 [Algorithms](../Algorithms)。
- 每个主题使用英文目录名；中文笔记放 README.md，Python 3 示例放 solution.py。
- 测试统一放 tests，使用标准库，不需要第三方依赖。
- 示例都是合成数据，不记录非公开业务资料。
- 题目原文使用来源链接；复盘记录自己的推导、反例和结论。
- 首次整理：2026-11-13。

从仓库根目录运行：
```sh
python3 -m unittest discover -s Dots_Learning/tests -v
```
