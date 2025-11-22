=============================
SixLine Cipher Specification — Version 1.0
(SLC-1.0-SPEC)
Status: Informational
=============================

Author: HankNovic（concept）
Editor: ChatGPT（specification writing）
Last Updated: 2025-11-22
Intended Use: Public Documentation
This document is NOT an Internet Standard.

--------------------------------------------------
Table of Contents
--------------------------------------------------

1. Introduction
2. Terminology and Normative Language
3. SixLine Symbol Set
4. Encoding Model
5. Mapping Tables
   5.1 Alphabet (A–Z)
   5.2 Digits (0–9)
   5.3 Whitespace & Punctuation
   5.4 Reserved Codes
6. Encoding Procedure
7. Decoding Procedure
8. Error Handling
9. Security Considerations
10. Example Encoding
11. Full Master Table (Overview)
12. License
13. Appendix A — Implementation Notes
14. Appendix B — Versioning Guidelines


=============================
1. Introduction
=============================

SixLine Cipher（以下简称 SLC）是一种使用 6 个竖线类字符构建的 Base-6 编码系统（Base-6 Encoding Scheme）。

它的设计目标包括：

- 提供一种低视觉可读性的符号流（low readability）
- 使用通用 ASCII / Latin-1 字符，确保不会乱码
- 保持结构简单、可预测、易解析
- 服务于文本混淆、谜题、隐写（steganography）、编码实验等场景

SLC 不是加密算法，它是一种文本编码方法。


=============================
2. Terminology and Normative Language
=============================

本规范采用 RFC 2119 中的术语：

- MUST：必须执行
- MUST NOT：禁止执行
- SHOULD：推荐执行
- SHOULD NOT：不推荐执行
- MAY / OPTIONAL：可选

其他术语：

- Symbol：六线密码中的 6 个基础字符之一
- Digit (Base-6)：0–5
- Symbol Pair：由两个 Symbol 构成的编码单位（长度为 2 的字符串）
- Encoder：编码器实现
- Decoder：解码器实现


=============================
3. SixLine Symbol Set
=============================

SLC 使用如下 6 个字符作为 Base-6 数字的符号：

- Base-6 digit 0 -> Symbol "i"   (Unicode U+0069)
- Base-6 digit 1 -> Symbol "!"   (Unicode U+0021)
- Base-6 digit 2 -> Symbol "l"   (Unicode U+006C)
- Base-6 digit 3 -> Symbol "I"   (Unicode U+0049)
- Base-6 digit 4 -> Symbol "|"   (Unicode U+007C)
- Base-6 digit 5 -> Symbol "¦"   (Unicode U+00A6)

以上 6 个 Symbol MUST 用于所有编码操作。


=============================
4. Encoding Model
=============================

4.1 基本思想

- 所有编码均基于 Base-6（0–5）。
- 每个被编码的“单位”（字母、数字或部分标点）使用两个 Base-6 digit 表示。
- 每个 Base-6 digit 再映射为一个 SixLine Symbol。
- 因此，每个编码单位最终都是一个长度为 2 的字符串（Symbol Pair）。

可表示的编码数为：

  6 × 6 = 36 个编码单元

这些编码单元用于：

- 26 个英文字母（A–Z）
- 10 个阿拉伯数字（0–9）
- 若干空白与标点
- 少量保留扩展位


=============================
5. Mapping Tables
=============================

本章节定义 SLC v1.0 的全部映射规则。


-----------------------------
5.1 Alphabet Mapping (A–Z)
-----------------------------

字母 A–Z 的编号规则如下：

- A 对应十进制 0
- B 对应十进制 1
- ...
- Z 对应十进制 25

每个十进制数转换为两位 Base-6，再映射为 Symbol Pair。结果如下：

- A  : decimal 0  -> base-6 00 -> "ii"
- B  : decimal 1  -> base-6 01 -> "i!"
- C  : decimal 2  -> base-6 02 -> "il"
- D  : decimal 3  -> base-6 03 -> "iI"
- E  : decimal 4  -> base-6 04 -> "i|"
- F  : decimal 5  -> base-6 05 -> "i¦"
- G  : decimal 6  -> base-6 10 -> "!i"
- H  : decimal 7  -> base-6 11 -> "!!"
- I  : decimal 8  -> base-6 12 -> "!l"
- J  : decimal 9  -> base-6 13 -> "!I"
- K  : decimal 10 -> base-6 14 -> "!|"
- L  : decimal 11 -> base-6 15 -> "!¦"
- M  : decimal 12 -> base-6 20 -> "li"
- N  : decimal 13 -> base-6 21 -> "l!"
- O  : decimal 14 -> base-6 22 -> "ll"
- P  : decimal 15 -> base-6 23 -> "lI"
- Q  : decimal 16 -> base-6 24 -> "l|"
- R  : decimal 17 -> base-6 25 -> "l¦"
- S  : decimal 18 -> base-6 30 -> "Ii"
- T  : decimal 19 -> base-6 31 -> "I!"
- U  : decimal 20 -> base-6 32 -> "Il"
- V  : decimal 21 -> base-6 33 -> "II"
- W  : decimal 22 -> base-6 34 -> "I|"
- X  : decimal 23 -> base-6 35 -> "I¦"
- Y  : decimal 24 -> base-6 40 -> "|i"
- Z  : decimal 25 -> base-6 41 -> "|!"


-----------------------------
5.2 Digits (0–9)
-----------------------------

数字 0–9 与十进制 0–9 对应。  
编码规则与字母相同（同一段 0–9）：

- "0" : decimal 0 -> base-6 00 -> "ii"
- "1" : decimal 1 -> base-6 01 -> "i!"
- "2" : decimal 2 -> base-6 02 -> "il"
- "3" : decimal 3 -> base-6 03 -> "iI"
- "4" : decimal 4 -> base-6 04 -> "i|"
- "5" : decimal 5 -> base-6 05 -> "i¦"
- "6" : decimal 6 -> base-6 10 -> "!i"
- "7" : decimal 7 -> base-6 11 -> "!!"
- "8" : decimal 8 -> base-6 12 -> "!l"
- "9" : decimal 9 -> base-6 13 -> "!I"

在上下文需要严格区分“字母 E”和“数字 4”时，应用层 SHOULD 通过外部信息或协议约定加以区分，因为它们共享同一编码段。


-----------------------------
5.3 Whitespace & Punctuation
-----------------------------

为避免与 A–Z / 0–9 冲突，空格与部分标点使用 Base-6 42 及以上的编码：

- Space      : decimal 26 -> base-6 42 -> "|l"
- Period "." : decimal 27 -> base-6 43 -> "|I"
- Comma  "," : decimal 28 -> base-6 44 -> "||"
- Question "?": decimal 29 -> base-6 45 -> "|¦"
- Exclam "!" : decimal 30 -> base-6 50 -> "¦i"

实现时 MAY 根据自身需要扩展更多标点，但 MUST 避免与 00–41 段的编码冲突。


-----------------------------
5.4 Reserved Codes
-----------------------------

Base-6 编码 42–55 共计 14 个单元，为扩展预留。  
本规范当前只使用其中 42–45、50 五个单元，其余建议用途示例：

- 扩展标点（例如冒号、分号、引号等）
- 控制符号（例如段落分隔、自定义标记）
- 其他语言的转写（如拼音、希腊字母等）

未来规范版本 MAY 对这些保留位做进一步定义。


=============================
6. Encoding Procedure
=============================

编码器（Encoder）在实现 SLC 时 MUST 遵循如下步骤：

1. 将输入字符串中的英文字母统一转换为大写（A–Z）。
2. 对每个字符：
   - 若为字母 A–Z，使用 5.1 的映射。
   - 若为数字 0–9，使用 5.2 的映射。
   - 若为空格或指定标点，使用 5.3 的映射。
   - 若为未定义字符，编码器 MAY：
     - 抛出错误（strict 模式），或
     - 使用某种转义/替代策略（tolerant 模式）。
3. 将得到的 Symbol Pair 串联输出。
4. 编码器 MAY 在 Symbol Pair 之间插入空格分隔，以提高人类可读性；也 MAY 直接输出无分隔的连续符号串。


=============================
7. Decoding Procedure
=============================

解码器（Decoder）在实现 SLC 时 MUST 遵循如下步骤：

1. 将输入的 SLC 密文视为一串字符。
2. 若使用了空格分隔，则可按空格切分为一个个 Symbol Pair；
   若为连续串，则 MUST 每 2 个字符截取为一个 Symbol Pair。
3. 对每个 Symbol Pair：
   - 查找其对应的 Base-6 数字对（反向映射）。
   - 将 Base-6 转为十进制。
   - 根据 5.1、5.2、5.3 对应回原字符。
4. 若遇到未知的 Symbol Pair，Decoder SHOULD：
   - 抛出错误（在 strict 模式下），或
   - 将其跳过或替换为占位符（在 tolerant 模式下）。


=============================
8. Error Handling
=============================

- Encoder MUST NOT 生成违反本规范（如长度不是 2 的 Symbol Pair）的编码。
- Decoder SHOULD 检测：
  - 密文长度不是 2 的整数倍；
  - 含有不存在于 Symbol 集的字符；
  - 含有未知的 Symbol Pair。
- 在 strict 模式下，Decoder SHOULD 直接报错并中止。
- 在 tolerant 模式下，Decoder MAY 跳过错误单元或用特殊符号替代。


=============================
9. Security Considerations
=============================

SixLine Cipher 是一种“视觉混淆编码”（obfuscation encoding），而不是加密算法。

- 它不会提供机密性、完整性或认证保证。
- 它仅仅让明文在视觉上难以直接阅读或快速理解。
- 对于真正的安全需求，SLC SHOULD 仅作为额外的一层“混淆层”，并叠加在安全的密码学算法之上。


=============================
10. Example Encoding
=============================

示例明文：

  HELLO WORLD

编码过程（使用分隔空格）：

  H -> "!!"
  E -> "i|"
  L -> "!¦"
  L -> "!¦"
  O -> "ll"
  Space -> "|l"
  W -> "I|"
  O -> "ll"
  R -> "l¦"
  L -> "!¦"
  D -> "iI"

最终输出密文：

  !! i| !¦ !¦ ll |l I| ll l¦ !¦ iI


=============================
11. Full Master Table (Overview)
=============================

本节以文字形式概览 36 个 Base-6 单元的用途：

- 00 -> "ii"  :  A / 0
- 01 -> "i!"  :  B / 1
- 02 -> "il"  :  C / 2
- 03 -> "iI"  :  D / 3
- 04 -> "i|"  :  E / 4
- 05 -> "i¦"  :  F / 5

- 10 -> "!i"  :  G / 6
- 11 -> "!!"  :  H / 7
- 12 -> "!l"  :  I / 8
- 13 -> "!I"  :  J / 9
- 14 -> "!|"  :  K
- 15 -> "!¦"  :  L

- 20 -> "li"  :  M
- 21 -> "l!"  :  N
- 22 -> "ll"  :  O
- 23 -> "lI"  :  P
- 24 -> "l|"  :  Q
- 25 -> "l¦"  :  R

- 30 -> "Ii"  :  S
- 31 -> "I!"  :  T
- 32 -> "Il"  :  U
- 33 -> "II"  :  V
- 34 -> "I|"  :  W
- 35 -> "I¦"  :  X

- 40 -> "|i"  :  Y
- 41 -> "|!"  :  Z
- 42 -> "|l"  :  Space
- 43 -> "|I"  :  Period "."
- 44 -> "||"  :  Comma ","
- 45 -> "|¦"  :  Question "?"
- 50 -> "¦i"  :  Exclamation "!"
- 51–55       :  Reserved for future extensions


=============================
12. License
=============================

本规范和参考实现示例在 MIT License 下发布。  
详见仓库根目录下的 LICENSE 文件。


=============================
13. Appendix A — Implementation Notes
=============================

- 编码器可以选择输出：
  - 无分隔的连续密文；或
  - 每个 Symbol Pair 之间加入空格。
- 解码器在设计时可以提供：
  - strict 模式：一旦遇到错误立即失败；
  - tolerant 模式：跳过错误并尽可能恢复剩余文本。
- 可以轻松实现流式（streaming）处理：每收到 2 个字符就尝试解码一个单位。


=============================
14. Appendix B — Versioning Guidelines
=============================

- v1.x：保持当前两位 Base-6 结构，主要扩展保留位的定义。
- v2.x：MAY 引入三位 Base-6，用于支持更大字符集。
- v3.x：MAY 定义完整 Unicode 或多语言映射方案。

任何未来版本 SHOULD 尽量保持对 v1.0 的向后兼容性（backward compatibility），或在不兼容时给出明确的版本标记。
