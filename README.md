# SixLine Cipher (SLC)
A vertical-line–themed Base-6 text encoding system  
Version: **SLC-1.0**

SixLine Cipher（简称 SLC）是一种使用 6 个竖线类字符构建的 Base-6 文本编码方式。  
它提供一种低可读性、跨平台、不依赖字体的混淆编码格式。  
**这不是密码学加密算法，而是一种纯编码方案（encoding scheme）。**

本项目包含：
- SLC v1.0 规范文档
- Python & JavaScript 编码器/解码器
- 示例明文、密文文件
- 完整 MIT License

---

## Features

- 使用 6 个竖形字符：`i ! l I | ¦`
- 采用 Base-6（0–5）构成编码
- 每个编码单位长度固定为 2 个字符（Symbol Pair）
- 显示效果不依赖字体
- 高度混淆的视觉效果
- 编解码逻辑简单、可用于任意程序

---

## SixLine Base Symbols (0–5)

所有 Base-6 数字映射为如下字符：

```

0 -> i
1 -> !
2 -> l
3 -> I
4 -> |
5 -> ¦

```

这些字符是 SLC 的基本组成。

---

## Encoding Rules

1. 输入文本的字母会被转换为大写（A–Z）
2. 每个字符映射为一个十进制编号  
3. 十进制编号转换为两位 Base-6  
4. Base-6 每位数字转换为对应的符号  
5. 最终输出由 symbol pair 组成

示例：  
A (decimal 0) → base-6 `00` → `ii`

---

## Mapping Overview (无表格版本)

### A–Z
```

A: ii
B: i!
C: il
D: iI
E: i|
F: i¦
G: !i
H: !!
I: !l
J: !I
K: !|
L: !¦
M: li
N: l!
O: ll
P: lI
Q: l|
R: l¦
S: Ii
T: I!
U: Il
V: II
W: I|
X: I¦
Y: |i
Z: |!

```

### Digits 0–9
```

0: ii
1: i!
2: il
3: iI
4: i|
5: i¦
6: !i
7: !!
8: !l
9: !I

```

### Whitespace & Common Punctuation
```

(space): |l
.:        |I
,:        ||
?:        |¦
!:        ¦i

```

---

## Example

明文：

```

HELLO WORLD

```

编码过程输出：

```

!! i| !¦ !¦ ll |l I| ll l¦ !¦ iI

```

解码后回复原文。

---

## Project Structure

```

/docs
SLC-1.0-SPEC.md
/examples
plain.txt
encoded.txt
decoded.txt
/src
/python
slc.py
/js
slc.js
/LICENSE
/README.md

````

---

## Usage (Python)

```python
from slc import encode, decode

print(encode("HELLO WORLD"))
print(decode("!! i| !¦ !¦ ll |l I| ll l¦ !¦ iI"))
````

---

## Usage (JavaScript)

```javascript
import { encode, decode } from "./slc.js";

console.log(encode("HELLO WORLD"));
console.log(decode("!! i| !¦ !¦ ll |l I| ll l¦ !¦ iI"));
```

---

## Specification

完整规范文档：

```
/docs/SLC-1.0-SPEC.md
```

---

## License

本项目基于 MIT License 发布。
详情见：

```
/LICENSE
```

---

## Author

**HankNovic** — SixLine Cipher 概念设计
ChatGPT — 文档与参考实现编写支持
