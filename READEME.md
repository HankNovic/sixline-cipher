# **SixLine Cipher Specification — Version 1.0**

### *SixLine Cipher v1.0 Specification (SLC-1.0)*

*Status: Informational*
*Author: hank huang (concept), ChatGPT (spec writing)*
*Last Updated: 2025-xx-xx*

---

# **1. Introduction**

SixLine Cipher（以下简称 SLC）是一种基于 **六个竖线风格字符** 的可读性极低、机器可解析的 *Base-6 编码系统*。
其目的包括：

* 最小化视觉可读性（stealth / obfuscation）
* 最大化跨设备兼容性（均为稳定 Unicode 字符）
* 使加密文本在普通文本流中不易被肉眼识别
* 让编码与解码过程简单、确定、可自动化

SLC 不是加密算法，而是一种字符编码方案（encoding scheme）。

---

# **2. Conventions and Terminology**

文档中使用的术语遵循以下约定：

* **MUST / MUST NOT**：强制要求
* **SHOULD / SHOULD NOT**：推荐但非必须
* **MAY**：可选
* **Encoder**：SLC 编码器
* **Decoder**：SLC 解码器
* **Base-6 Digit**：0–5 的数字
* **SixLine Symbol**：六符号集中的一个字符
* **Symbol Pair**：两个连续的 SixLine Symbol（SLC 编码基本单位）

---

# **3. SixLine Symbol Set**

SixLine Cipher 采用如下六个竖形符号作为 Base-6 数字：

| Digit | Symbol | Unicode | Name        |      |
| ----- | ------ | ------- | ----------- | ---- |
| 0     | `i`    | U+0069  | thin-i      |      |
| 1     | `!`    | U+0021  | exclamation |      |
| 2     | `l`    | U+006C  | low-line    |      |
| 3     | `I`    | U+0049  | tall-line   |      |
| 4     | `      | `       | U+007C      | pipe |
| 5     | `¦`    | U+00A6  | broken bar  |      |

这些符号满足以下要求：

* 全部通用、跨平台高兼容
* 没有复杂的笔画
* 外观均为“竖线风格”，可读性弱
* 从视觉上不易区分
* 能作为 Base-6 的完整符号空间

---

# **4. Encoding Model**

## **4.1 Base-6 Representation**

SixLine Cipher 采用标准 Base-6（0–5）作为编码基础。
任何编码元素均需转换为：

```
Two-Digit Base-6
```

即 **两位六进制数字**，范围为 `00 ~ 55`，总共 36 种组合。

---

# **4.2 Symbol Mapping**

Base-6 每一位数字被替换为对应的 SixLine Symbol。

例如：

| Base-6 | Symbol |   |
| ------ | ------ | - |
| 0      | i      |   |
| 1      | !      |   |
| 2      | l      |   |
| 3      | I      |   |
| 4      |        |   |
| 5      | ¦      |   |

因此：

```
Base-6 "23" → "lI"
Base-6 "41" → "|!"
Base-6 "05" → "i¦"
```

---

# **5. Alphabet Encoding**

SLC 对英语字母（A–Z）采用 *sequential mapping*：

| Letter | Decimal | Base-6 | SLC |    |
| ------ | ------- | ------ | --- | -- |
| A      | 0       | 00     | ii  |    |
| B      | 1       | 01     | i!  |    |
| C      | 2       | 02     | il  |    |
| …      | …       | …      | …   |    |
| Z      | 25      | 41     | `   | !` |

详细字母表已在附录 A 给出。

编码规则：

* 输入 MUST 为大写 A–Z
* 输出 MUST 为两个字符的 Symbol Pair
* 字母编码 MUST 不使用保留编码空间（42–55）

---

# **6. Digit Encoding (0–9)**

数字使用相同的 Two-Digit Base-6 体系。

| Decimal | Base-6 | SLC |
| ------- | ------ | --- |
| 0       | 00     | ii  |
| 1       | 01     | i!  |
| 2       | 02     | il  |
| …       | …      | …   |
| 9       | 13     | !I  |

数字编码与字母表共享 00–13 的范围。
SLC 解码时若必须区分字母与数字，则应依赖外部上下文。

---

# **7. Whitespace and Punctuation**

以下编码为 SLC v1.0 推荐值：

| Character       | Decimal | Base-6 | SLC |   |
| --------------- | ------- | ------ | --- | - |
| SPACE           | 26      | 42     | l   |   |
| PERIOD (.)      | 27      | 43     | l¦  |   |
| COMMA (,)       | 28      | 44     |     | i |
| QUESTION (?)    | 29      | 45     |     | ! |
| EXCLAMATION (!) | 30      | 50     | ¦i  |   |

实现 MAY 自定义扩展，但必须避免冲突字母区间（00–41）。

---

# **8. Encoding Procedure**

输入字符串 → Encoder MUST：

1. 将字母标准化为 A–Z
2. 将每个字母对应为十进制（A=0,B=1 …）
3. 转换为两位 Base-6
4. 将每个数字替换为 Symbol
5. 组合成最终密文

---

# **9. Decoding Procedure**

Decoder MUST：

1. 将密文按 2 字符切割（ii, i!, il…）
2. 将每个符号映射为 Base-6 数字
3. 将两位 Base-6 组合转换为十进制
4. 根据映射表恢复：

   * 字母
   * 数字
   * 空格
   * 标点

---

# **10. Security Considerations**

SLC 是一种“视觉混淆编码”（obfuscation encoding），不是加密算法。

它提供：

* 低可读性
* 高可隐写性
* 高兼容性

但 **不提供加密安全性**，不应在安全场景替代密码学算法。

---

# **11. Appendix A — Complete Alphabet Table**

（此处保留）

你若需要，我可以补上完整附录 A 表格（26 字母 + Base-6 + SLC）。

---

# **12. Appendix B — Example**

示例：

```
HELLO WORLD
```

编码：

H → 11 → !!
E → 04 → i|
L → 15 → !¦
L → 15 → !¦
O → 22 → ll
(space) → 42 → l|
W → 34 → I|
O → ll
R → 25 → l¦
L → !¦
D → 03 → iI

最终密文：

```
!! i| !¦ !¦ ll l| I| ll l¦ !¦ iI
```
