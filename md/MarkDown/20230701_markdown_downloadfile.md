# 如何在 MD 文档里实现下载附件

---

### 1.超链接语法

```MD
//行内式的链接:
[超链接名](超链接地址 "超链接title")
//参考式的链接:
[超链接名][id]
[id]: http://example.com/  "Optional Title Here"
```

---

### 2.网址和 Email 地址

- 使用尖括号可以很方便地把 URL 或者 email 地址变成可点击的链接.

---

### 3.a 标签下载

- download 属性提供 a 标签在点击时，下载 url 地址中的文件；

```html
<a href="../media/e.txt" download="download.txt">附件1</a>
```

点击下载<<a href="../media/e.txt" download='download.txt'>附件 1</a>>

- 补充说明：通过实践发现圆括弧`()`同样可行.

点击下载(<a href="../media/download.txt" download='download.txt'>附件 1</a>)

```MD
<<a href="../media/download.txt" download='download.txt'>附件 1</a>>
(<a href="../media/download.txt" download='download.txt'>附件 1</a>)
```


