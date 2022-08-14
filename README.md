# LeetCode
My LeetCode Record

以下内容为我刷题时的随手笔记。格式较乱，随便看看就好。

[toc]

# 1. split()与split(' ')：

- `'a b'.split() == 'a b'.split(' ')`会返回True，事实上结果都是`['a', 'b']`；
- 然而`''.split() == ''.split(' ')`却是False，因为空字符也会“被分割”……
即：
- `''.split()`返回的是`[]`；
- 而`''.split(' ')`返回的是`['']`
- 当然，split()会对包括`\n`等一切空字符一视同仁，而split(' ')则使用一且仅一个空格作为分隔符。见返回值如下：
![fig](fig/split.png)

# 2. 树的前、中、后序遍历模板

- 首先是递归写法：

以后序遍历为例
```python
arr = []

def postOrder(root: TreeNode) -> None:
    if not root: # 递归边界
        return
    postOrder(root.left)
    postOrder(root.right)
    arr.append(root.val) # 访问节点，做一些操作

postOrder(root)
return arr
```

前中后序英文分别对应preOrder、inOrder、postOrder。注意，**当回溯时需要用到历史信息**，则考虑使用nonlocal做一些全局变量，进行后续操作。

函数的主体部分也可以写成：
```python
def postOrder(root: TreeNode) -> None:
    if root:
        postOrder(root.left)
        postOrder(root.right)
        arr.append(root.val)
```
不过上一种方式更加清晰。知道就好。

- 迭代写法：

迭代写法的主体框架是：
```python
stack = []
cur = root
while stack or cur:
    while cur:
        stack.append(cur)
        cur = cur.left
    cur = stack.pop()
    cur = cur.right
return ans
```

树的遍历，总的原则是**先左后右**，所以每当向右时，都要重新判断是否需要先向左这件事——这个核心逻辑，决定了遍历这个过程，在向右时总是小心翼翼，必须“步步为营”。

看代码，while cur的部分属于向左探，本质上是 **「先访问再压栈」** ；后面pop和=right的部分，则是元素出栈后向右探，本质上是 **「再访问一次，并进入下一级右孩子（然后重新判断是否向左）」** 。

所以，先中后序在代码的何部分对元素操作、输出就比较有意思了，大致总结为：
1. 先序在第一次访问压栈前就操作；
2. 中序则在入栈出栈之间的访问；
3. 后序则比较棘手了，需要维护一个prev，确保右孩子访问过，才执行操作（必须区分我是向后执行右探操作呢，还是该直接对当前元素操作）。

----

前序
```python
ans = []
stack = []
cur = root
while stack or cur:
    while cur:
        ans.append(cur.val)
        stack.append(cur)
        cur = cur.left
    cur = stack.pop()
    cur = cur.right
return ans
```
        

中序
```python
ans = []
stack = []
cur = root
while stack or cur:
    while cur:
        stack.append(cur)
        cur = cur.left

    cur = stack.pop()
    ans.append(cur.val)

    cur = cur.right
return ans
```

后序（注意两点，一是右探时，对自身不操作，还要重新压栈回去等后续操作；二是对当前元素操作后，记得先记录pre为当前结点，后必须将当前结点赋空，以免再度判断操作，两者的顺序不能反）

```python
ans = []
stack = []
cur, prev = root, None
while stack or cur:
    while cur:
        stack.append(cur)
        cur = cur.left
    cur = stack.pop()
    if cur.right and prev != cur.right:
        stack.append(cur)
        cur = cur.right
    else:
        ans.append(cur.val)
        prev = cur
        cur = None
return ans
```

# 3. nonlocal

主要应用在嵌套函数、闭包中，将**不可变类型的数据变为自由变量**；对于可变变量就没必要使用了，比如list等。

nonlocal是针对上一级函数而言的，若上层函数不存在该变量则会报错；global则表示全局变量

------------

闭包：能够读取外部函数内的变量的函数
作用1：将外层函数内的局部变量和外层函数的外部连接起来的一座桥梁【闭包就是对外部私货的轻量封装】
作用2：将外层函数的变量持久地保存在内存中
关于闭包更多可见：[Python闭包（Closure）详解](https://zhuanlan.zhihu.com/p/453787908)

# 4. @cache


据评论区，似乎与@lru_cache是类似的。可以将函数调用（某一变量值对应的）结果存入缓存中，而达到复用效果，可以大大加速像斐波那契数列这样的操作。不过对list dict等结构不适用。

参考资料：[Python 缓存机制与 functools.lru_cache](http://kuanghy.github.io/2016/04/20/python-cache)，[Python 中 lru_cache 的使用和实现](https://www.cnblogs.com/zikcheng/p/14322577.html)，[Python缓存lru_cache的介绍和讲解](https://quniao.blog.csdn.net/article/details/120726050)

# 5. 如何让tuple/list的对应元素相加？

可以通过`list(map(sum, zip(list1, list2)))`来达成，tuple同理。zip操作是对输入的每个对象enumerate并行封装，例如：
```python
list1 = [0,1,2]
list2 = [3,4,5]
list3 = [6,7,8]
list(zip(list1,list2,list3))
```
输出`[(0, 3, 6), (1, 4, 7), (2, 5, 8)]`

这个封装过程是tuple，返回zip对象，还要再转。map也是返回map对象，再转即可。

注意，函数的返回如果写`return a, b`实际上是返回的tuple`(a, b)`。

# 6. *arg和**arg

作为函数调用时，\*用于解包tuple对象，\*\*用于解包dict对象。
这样比较抽象，比如
```python
strs = ["abc", "bce", "cae"]
```
`zip(*strs)`等同于`zip("abc", "bce", "cae")`，然而不等同于`zip(strs)`或者`zip(strs[i] for i in range(3))`或者`zip(i for i in strs)`，最后总是差一层tuple。

# 7. itertools库的使用

[「Python」Python 标准库之 itertools 使用指南](https://blog.csdn.net/qq_43401035/article/details/119253871)

- pairwise，可以创建一个迭代对象的两两一组迭代；若元素少于2个则返回empty。比如"abc"就会产生"ab", "bc"。
- groupby，对一个迭代器（通常是字符串）进行迭代分组。通常使用`for ch, grp in groupby(*)`，但注意此时grp是_grouper object，需要转为list会好使一些。
- `combinations(object, k)`，其中object是一个可迭代的对象，k为数量。这样的语句可以快速地完成Cxx的操作，很方便。 

# 8. 对称情况

当出现对称情况时，复制代码是一件很蠢的事情，有时候可以试试交换输入，把f(a, b)变成f(b, a)

# 9. sort与lambda函数

考虑一个list如`arr = [10, 8, 7, 2, 5, 9, 1]`。

- arr.sort()是内置的method，是一个过程，对原对象直接修改，并不返回任何值；
- sorted(arr)，顾名思义，则是对arr进行排序，返回是排列好的对象，而不对原对象修改。

然后核心就是一定要学会使用key=lambda函数了。
（TODO）

# 10. bisect

参考资料：[python官方文档 - bisect](https://docs.python.org/3/library/bisect.html)

bisect模块可以省略去写二分查找的过程。查找一般使用`bisect.bisect_left(a, x, lo=0, hi=len(a))`，这里默认a是sorted。bisect_left与bisect_right（等价于bisect）的区别在于，若a中存在对应的value，是插到左边还是右边。

注意插入的过程是指，将x插入返回的位置i后，原[i:]的元素向后移一位，仍保持有序性。

e.g.：

```python
import bisect
a = [1, 4, 6, 6, 8, 20]
bisect.bisect_left(a, 6)
bisect.bisect(a, 6)
bisect.bisect_right(a, 6)
```
上述三条分别返回2，4，4。

如果想找到位置之后再插入，可以一步使用`insort_left`，或是`insort_right`（等价于`insort`）。但要注意，二分查找的过程是O(log n)的，插入这个操作却是O(n)的，算复杂度时应该考虑插入操作。

在python 3.10之后，还增加了key关键字，可以配合lambda函数使用。但一定注意，**必须保证a在经过key的映射后仍然是升序的，否则比较会出错**。再具体可以看[源码](https://github.com/python/cpython/blob/3.10/Lib/bisect.py)对于使用key的比较过程。

# 11. 关于浮点精度问题

参考资料：[【灵茶山艾府】第 294 场力扣周赛精讲 + 算法练习方法分享](https://www.bilibili.com/video/BV1RY4y157nW)、[IEEE 754](https://en.wikipedia.org/wiki/IEEE_754)

本以为python不会溢出，但还是在294周赛中中招了。python3的int（整数）是可以非常非常长的，所以不用担心；但float64的精度（C++中的double）只能到10^16左右(1 << 53)，所以当出现`1/(10**9-1)和1/(10**9-1)`作差时，分母相乘溢出。

总之，一切除法比较尽量转化成乘法比较！


# 12. 拓扑排序

参考资料：[OI WIKI 拓扑排序](https://oi-wiki.org/graph/topo/)、[【拓扑排序】图论拓扑排序入门](https://mp.weixin.qq.com/s?__biz=MzU4NDE3MTEyMA==&mid=2247489706&idx=1&sn=771cd807f39d1ca545640c0ef7e5baec)

总的来说，拓扑排序是用来描述变量与变量之间的上下级关系的算法，可以梳理变量的依赖关系，因而称为“排序”。典型模板题就是A比B大，C比D大，A又比C大……然后排一个总的次序。


算法的核心思想则是在一个DAG中，维护一个入度为 0 的顶点的集合。将变量视为图的结点，那么找到所有入度为0（没有边指向它）的顶点，删去其所有指出的边，然后重复此过程。若出现某一时刻没有没有入度为0的点，说明图中有环。因此，拓扑排序也很适合结合DFS或BFS（更推荐BFS），Kahn算法就是BFS下的toposort。

# 13. random

- 基础工具
  
python自带的随机库是random。大部分函数都是左闭右开的。

1. 生成整数随机数：randint(start, stop)，或者randrange(start, stop+1)，两者等价，前者左闭右闭，后者左闭右开，start和stop都是整数。
2. 生成浮点随机数：uniform(x, y)，左闭右闭！
3. 生成0-1的随机数：random()，这个是左闭右开，相当于是[0,1)
4. 从序列返回一个随机元素：choice(seq)。要求序列非空，否则indexError。
5. 从序列返回多个随机元素：choices(seq, weights=None, cum_weights=None, k=1)。同样要求序列非空（和k的大小无关）。注意choices可以按权重（list格式）或者累计权重来抽样，某些情况下很好使。另外注意choices返回的是list(list())。k=1的时候需要[0]一下。
   
更多细节可以参见：[python官方文档 - random](https://docs.python.org/3/library/random.html)。

- 水塘抽样


# 关于哈希、集合的操作

- setdefault

```python
d = {}
d.setdefault(key1, a)
d.setdefault(key1, b)
```

那么`d[key1]`应该会输出a。setdefault的含义是，对某一键值尝试复制，若存在该键则不做改变，若不存在该键则赋值。这个操作很适合对“存在性”做记录，省去了一些if else的麻烦。

# 记忆化搜索

# 线段树

# 排序总结

参考资料：[排序算法总结](https://www.runoob.com/w3cnote/sort-algorithm-summary.html)

lowb三人组：冒泡，选择，插入。时间复杂度均为O(n^2)

- 冒泡排序就像泡泡浮起来，所以说是两两比较，把小的放到前边大的放后边，典型场景就是**小时候排队，两两互比身高站前后**；
- 选择排序是每次找到序列中最小的一个放在前面，很像冒泡，也像是排队，但像是老师给安排队伍，**从全局来看而非两两比较**；
- 插入排序典型场景就是**打扑克揭牌**，每揭一张我们就插入到本就有序的牌堆中，保持其有序性至终止。

高级三人组：快排，归并，堆。时间复杂度均为O(nlogn)

- 快速排序简言之就是分治+pivot，但在具体实现上，可以通过双指针查找。一般来讲我们选择第一个数为pivot（或理解为把pivot放在最前面），所以**开始时要从后向前查找**，挖坑填数。性能受制于pivot取得好不好，差时退化为选择排序，所以可以通过随机化改进。
- 归并排序亦作二路归并，是典型的二分分治法，分即将一个数组的排序问题二分为两个，治则采用**双指针合并之**。
- 堆排序则像是**官职制度**，省长管市长，市长管区长，能者擢升，不能者下放，从而达到整个队列的有序化。

其他：希尔排序、基数排序