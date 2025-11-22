# =======================================

# **SixLine Cipher Specification — Version 1.0**

# (SLC-1.0-SPEC)

# Status: Informational

# =======================================

**Author:** hank huang（concept）
**Editor:** ChatGPT（specification writing）
**Last Updated:** 2025-XX-XX
**Intended Use:** Public Documentation
**This document is NOT an Internet Standard.**

---

# **Table of Contents**

1. Introduction
2. Terminology and Normative Language
3. SixLine Symbol Set
4. Encoding Model
5. Mapping Tables

   * 5.1 Alphabet (A–Z)
   * 5.2 Digits (0–9)
   * 5.3 Whitespace & Punctuation
   * 5.4 Reserved Codes
6. Encoding Procedure
7. Decoding Procedure
8. Error Handling
9. Security Considerations
10. Example Encoding
11. Full Tables (Master Chart)
12. License Options
13. Appendix A — Implementation Notes
14. Appendix B — Versioning Guidelines

---

# =======================================

# **1. Introduction**

# =======================================

SixLine Cipher（以下简称 **SLC**）是一种使用 **6 个竖线类字符** 构建的 *Base-6 编码系统（Base-6 Encoding Scheme）*。

它的设计目标包括：

* 提供一种 **低视觉可读性（low readability）** 的符号流
* 使编码结构简单、可预测
* 使用 **通用 ASCII / Latin-1 字符**，确保不会乱码
* 方便在程序、文档、谜题或隐写（steganography）中使用

SLC **不是加密算法**。
它是一种文本编码方法。

---

# =======================================

# **2. Terminology and Normative Language**

# =======================================

本规范使用 RFC 2119 定义的关键词：

* **MUST**：必须执行
* **MUST NOT**：禁止执行
* **SHOULD**：推荐执行
* **SHOULD NOT**：不推荐
* **MAY**：可选
* **OPTIONAL**：可选

其他术语：

* **Symbol**：六线密码中的六个基础字符
* **Digit (Base-6)**：0–5
* **Symbol Pair**：由两个 Symbol 组成的编码单位
* **Encoder**：负责编码的实现
* **Decoder**：负责解码的实现

---

# =======================================

# **3. SixLine Symbol Set**

# =======================================

SixLine Cipher 采用如下 **6 个字符**作为 Base-6 数字：

| Base-6 Digit | Symbol | Unicode | Name        |      |
| ------------ | ------ | ------- | ----------- | ---- |
| 0            | `i`    | U+0069  | thin-i      |      |
| 1            | `!`    | U+0021  | exclamation |      |
| 2            | `l`    | U+006C  | low-line    |      |
| 3            | `I`    | U+0049  | tall-line   |      |
| 4            | `      | `       | U+007C      | pipe |
| 5            | `¦`    | U+00A6  | broken bar  |      |

它们 MUST 用于所有编码操作。
每个字符 MUST 保持 ASCII/Latin-1 兼容。

---

# =======================================

# **4. Encoding Model**

# =======================================

## **4.1 Base-6 整体结构**

SLC 使用：

* 两位 Base-6 数字表示一个编码单位
* 每位数字转为一个 Symbol
* 因此每个编码单位长度固定为 **2 个字符**

可表示总数：

```
6 × 6 = 36 个编码单元
```

用于：

* 26 字母
* 10 数字
* 多个标点
* 扩展编码区

---

# =======================================

# **5. Mapping Tables**

# =======================================

此章节定义 SLC v1.0 的全部映射规则。

---

# **5.1 Alphabet Mapping (A–Z)**

| Letter | Decimal | Base-6 | SLC |   |
| ------ | ------- | ------ | --- | - |
| A      | 0       | 00     | ii  |   |
| B      | 1       | 01     | i!  |   |
| C      | 2       | 02     | il  |   |
| D      | 3       | 03     | iI  |   |
| E      | 4       | 04     | i   |   |
| F      | 5       | 05     | i¦  |   |
| G      | 6       | 10     | !i  |   |
| H      | 7       | 11     | !!  |   |
| I      | 8       | 12     | !l  |   |
| J      | 9       | 13     | !I  |   |
| K      | 10      | 14     | !   |   |
| L      | 11      | 15     | !¦  |   |
| M      | 12      | 20     | li  |   |
| N      | 13      | 21     | l!  |   |
| O      | 14      | 22     | ll  |   |
| P      | 15      | 23     | lI  |   |
| Q      | 16      | 24     | l   |   |
| R      | 17      | 25     | l¦  |   |
| S      | 18      | 30     | Ii  |   |
| T      | 19      | 31     | I!  |   |
| U      | 20      | 32     | Il  |   |
| V      | 21      | 33     | II  |   |
| W      | 22      | 34     | I   |   |
| X      | 23      | 35     | I¦  |   |
| Y      | 24      | 40     |     | i |
| Z      | 25      | 41     |     | ! |

---

# **5.2 Digits 0–9**

| Digit | Decimal | Base-6 | SLC |   |
| ----- | ------- | ------ | --- | - |
| 0     | 0       | 00     | ii  |   |
| 1     | 1       | 01     | i!  |   |
| 2     | 2       | 02     | il  |   |
| 3     | 3       | 03     | iI  |   |
| 4     | 4       | 04     | i   |   |
| 5     | 5       | 05     | i¦  |   |
| 6     | 6       | 10     | !i  |   |
| 7     | 7       | 11     | !!  |   |
| 8     | 8       | 12     | !l  |   |
| 9     | 9       | 13     | !I  |   |

---

# **5.3 Whitespace & Punctuation**

v1.0 推荐：

| Character | Decimal | Base-6 | SLC |   |
| --------- | ------- | ------ | --- | - |
| Space     | 26      | 42     | l   |   |
| .         | 27      | 43     | l¦  |   |
| ,         | 28      | 44     |     | i |
| ?         | 29      | 45     |     | ! |
| !         | 30      | 50     | ¦i  |   |

---

# **5.4 Reserved Codes**

Base-6 区间：

```
42–55（剩余 14 个编码）
```

保留为未来扩展，包括：

* 中文拼音
* Unicode 范围映射
* 控制字符
* 用户自定义符号

---

# =======================================

# **6. Encoding Procedure**

# =======================================

输入 MUST：

* 转为大写（A–Z）
* 数字保持原状
* 非定义字符 MUST 使用扩展区或出错

编码流程：

1. 按字符取对应 decimal index
2. decimal → two-digit base-6
3. base-6 digits → SixLine symbols
4. 输出 symbol pair

---

# =======================================

# **7. Decoding Procedure**

# =======================================

解码 MUST：

1. 每 **2 个字符** 拆分为一个编码单元
2. 两个 Symbol → 两个 base-6 digits
3. base-6 → decimal
4. decimal → 原字符（字母/数字/标点）

未知编码 SHOULD 触发错误或跳过。

---

# =======================================

# **8. Error Handling**

# =======================================

编码器 MUST NOT 输出无法解析的编码。
解码器 SHOULD：

* 遇到非法符号对时返回错误
* 或丢弃该编码单元

允许实现提供 strict / tolerant 模式。

---

# =======================================

# **9. Security Considerations**

# =======================================

SixLine Cipher：

* **不提供**加密安全性
* 是一种混淆方式，不是密码算法
* 不适合保护敏感数据
* 适合作为分层安全模型的一部分（obfuscation layer）

---

# =======================================

# **10. Example Encoding**

# =======================================

示例：

```
HELLO WORLD
```

编码后：

```
!! i| !¦ !¦ ll l| I| ll l¦ !¦ iI
```

---

# =======================================

# **11. Full Master Table (ALL 36 Codes)**

# =======================================

| Base-6 | SLC Symbol | Assigned Value |           |
| ------ | ---------- | -------------- | --------- |
| 00     | ii         | A / 0          |           |
| 01     | i!         | B / 1          |           |
| 02     | il         | C / 2          |           |
| 03     | iI         | D / 3          |           |
| 04     | i          |                | E / 4     |
| 05     | i¦         | F / 5          |           |
| 10     | !i         | G / 6          |           |
| 11     | !!         | H / 7          |           |
| 12     | !l         | I / 8          |           |
| 13     | !I         | J / 9          |           |
| 14     | !          |                | K         |
| 15     | !¦         | L              |           |
| 20     | li         | M              |           |
| 21     | l!         | N              |           |
| 22     | ll         | O              |           |
| 23     | lI         | P              |           |
| 24     | l          |                | Q / SPACE |
| 25     | l¦         | R / .          |           |
| 30     | Ii         | S              |           |
| 31     | I!         | T              |           |
| 32     | Il         | U              |           |
| 33     | II         | V              |           |
| 34     | I          |                | W         |
| 35     | I¦         | X              |           |
| 40     |            | i              | Y / ,     |
| 41     |            | !              | Z / ?     |
| 42     | l          |                | SPACE     |
| 43     | l¦         | .              |           |
| 44     |            | i              | ,         |
| 45     |            | !              | ?         |
| 50     | ¦i         | !              |           |
| 51–55  | RESERVED   | —              |           |

---

# =======================================

# **12. License Options**

# =======================================

## **MIT License**

```
MIT License

Copyright (c) 2025 hank

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software...
```

---

# =======================================

# **13. Appendix A — Implementation Notes**

# =======================================

* 解码器 SHOULD 支持无分隔的连续密文
* 编码器 MAY 在 symbol pairs 之间添加空格
* 推荐提供 strict/tolerant 模式
* 可实现 streaming decoder（流式解码）

---

# =======================================

# **14. Appendix B — Versioning Guidelines**

# =======================================

* v1.x：只使用两位 base-6
* v2.x：可扩展至三位 base-6
* v3.x：可加入拼音、Unicode 等全字符支持
* 所有新编码 MUST 不破坏前向兼容性

---

# =======================================

# **End of SLC-1.0 Specification**

# =======================================

