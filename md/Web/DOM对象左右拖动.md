# DOM对象左右拖动

## 引入

当我们内容框超出我们浏览器页面时，通常以滚动形式进行承载，而我们滚动页面通常有这么几种方式：鼠标滑轮滚动以及与拖拽滚动条交互。

- 拖拽滚动条，不管是横向滚动条或是纵向滚动条，都是行之有效，简单粗暴。

- 鼠标滚轮针对横向与纵向的不同方式：
  - 在纵向上移动，鼠标滚轮总是默认为纵向上
  - 在横向上移动，我们在滚动滚轮时，需要额外按住shift键。

## 拖拽页面效果

我们在浏览页面时，也见到过鼠标按住页面空白位置不动，直接拖拽，也可以实现类似与拖动滚动条，让页面按照拖动的方向或指定方向进行移动。这也是这篇笔记需要实现的效果。

## 预览
效果一：
<iframe height='110px' src ='../md/Web/DOM对象左右拖动.assets/1.html'></iframe>
效果二：
<iframe height='110px' src ='../md/Web/DOM对象左右拖动.assets/2.html'></iframe>

## 对比
第一个，我们在按住空白区域往右边拖动时，滚动条往右边移动，页面内容也在往右边移动，内容却是往左边移除视野外。因此我们总结出以下结论：
- 鼠标移动的像素长度与页面移动的像素长度相同。
- 滚动条与我们移动方向保持一致。
- 页面内容移除方向与移动方向相反。


第二个，我们在按住空白区域往右边拖动时，如果滚动条在最左边，我们是无法移动的，改变方向，向左移动，这时滚动条开始移动，我们得出以下结论：

- 鼠标移动的像素长度与页面移动的像素长度相同。
- 滚动条与移动方向相反。
- 页面内容移除方向与移动方向一致。

总结：
- 从视觉观感与习惯上看，我们在拖动页面时，通常关注的是页面剩余内容与滚动条剩余长度之间情况。因此第一种效果更符合我们的预期。

- 而从代码实现效果上看，例如我们在拖动表格时，由于页面内容与鼠标移动相同，鼠标不会经过多个单元格，也就不会频繁触发移除事件。因此第二种效果更能达到我们的预期。



## JS代码实现

```js
<script>
        isDragging = false; //判断是否启用移动事件
        var downX = null;   //按下鼠标的坐标
        var div = document.getElementById('div'); //获取DOM对象
        var startScrollLeft = div.scrollLeft; // 初始化当前滚动条所在位置
        div.addEventListener("mousemove", function (e) {
            if (isDragging) {
                // 在这里处理鼠标拖动滚动事件的逻辑
                // console.log('移动像素',e.clientX - downX)
                // console.log('当前滚动条所在位置', div.scrollLeft)
                //这里的加减号代表移动的方向，1倍速，根据需要自己调整 
                div.scrollLeft = startScrollLeft + (e.clientX - downX) * 1; 
                if (div.scrollLeft <= 0) {
                    isDragging = false;
                }
            }
        });

        div.addEventListener("mousedown", function (e) { //鼠标按下，记录初始位置
            isDragging = true;
            downX = e.clientX;
            startScrollLeft = document.getElementById('div').scrollLeft;
            // console.log('---------down-------------')
        });

        div.addEventListener("mouseup", function (e) { //鼠标松开事件
            isDragging = false;
            downX = null;
            // console.log('---------up-------------')
        });

        div.addEventListener('mouseout', function (e) {//鼠标移出，初始化
            // console.log('移出')
            isDragging = false;
            downX = null;
            startScrollLeft = div.scrollLeft;
        });

    </script>
```