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

# 11. 关于浮点精度问题

本以为python不会溢出，但还是在294周赛中中招了。

