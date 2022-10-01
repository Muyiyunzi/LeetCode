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

前中后序英文分别对应preOrder、inOrder、postOrder。注意，**当回溯时需要用到历史信息**，则考虑使用nonlocal做一些全局变量，或是通过list来做记录，进行后续操作。

无论是前中后序遍历，在对值进行操作时如果return，也会立即回溯而终止整个遍历。

函数的主体部分也可以简写成：
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

nonlocal是针对上一级函数而言的，若上层函数不存在该变量则会报错；global则表示全局变量。

另外可以避免nonlocal的方式是使用全局变量，即对self.xxx修改赋值即可

------------

闭包：能够读取外部函数内的变量的函数
作用1：将外层函数内的局部变量和外层函数的外部连接起来的一座桥梁【闭包就是对外部私货的轻量封装】
作用2：将外层函数的变量持久地保存在内存中
关于闭包更多可见：[Python闭包（Closure）详解](https://zhuanlan.zhihu.com/p/453787908)

# 4. @cache

此机制源自于functools的lru_cache，在python 3.9之后，其直接被集成在python中，名为cache。我们通常通过装饰器的方式使用之（即对def前添加`@cache`），如果python版本过低，也可以通过`import functools`后`@functools.lru_cache`使用。

缓存机制可以可以将函数调用的结果存入缓存中，从而在再次递归调用时达到复用效果，对像斐波那契数列一类问题的递归解法时有着加速和避免内存爆掉的作用，**广泛应用于记忆化搜索即DP问题**。注意函数的输入尽量是单值变量/元组，对输入是list、dict等结构时不适用。

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
- `combinations(iterable, r)`，其中iterable是一个可迭代的对象，r为数量，即在iterable中选出r个作为组合（默认按原顺序排列）。这样的语句可以快速地完成Cxx的操作，很方便。 
- `permutations(iterable, r=None)`，有组合自然也就有排列，如果不给出r默认全长排列。有些时候暴力搜索会很好使。


# 8. 对称情况

当出现对称情况时，复制代码是一件很蠢的事情，有时候可以试试交换输入，把f(a, b)变成f(b, a)

# 9. sort与lambda函数

考虑一个list如`arr = [10, 8, 7, 2, 5, 9, 1]`。在python内置的sort之后他将会变成`[1, 2, 5, 7, 8, 9, 10]`，有如下一些细节：

- arr.sort()是内置的method，是一个过程，对原对象直接修改，并不返回任何值；
- sorted(arr)，顾名思义，则是对arr进行排序，返回是排列好的对象，而不对原对象修改。
- sort函数提供了许多选项。sort默认升序排序，可以使用`reverse=True`来实现降序排序；可以使用`key=`来制定比较的规则。

然后核心就是一定要学会**使用key这个关键字**。

## lambda函数

看似高深莫测，实则非常简洁：即不必显式地定义函数名称，而直接实现函数的功能。使用方式为`lambda x: f(x)`例如：

```python
g = lambda x: x ** 2
g(4) # -> 16
```

这里lambda之后并不一定只是一元，也可以是多元的。此外，其还可以与诸多内置函数并用，如：

```python
# 过滤三的倍数
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print(filter(lambda x: x % 3 == 0, foo))
# -> [18, 9, 24, 12, 27]

# 对list进行函数映射
print(map(lambda x: x * 2 + 10, foo))
# -> [14, 46, 28, 54, 44, 58, 26, 34, 64]
```

lambda函数也可以与defaultdict等数据结构共同使用，在传入参数时不做设定表示默认，如：

```python
x = defaultdict(lambda:0) # 默认值是0
y = defaultdict(lambda:[0,0,0]) # 默认值是列表
z = defaultdict(lambda: defaultdict(lambda:0)) # lambda函数也可以嵌套
```

## sort中的比较规则

- key关键字指通过什么样的比较规则来进行比较排序。其接受的是一个function，或是其他任何callable的参数（比如list，tuple等）。我们最常使用list来进行排序，例如：

```python
a = [1,2,3,4,5]
a.sort(key=lambda x: [x%2==0, x])
a # -> [1,3,5,2,4]
```

在通过lambda函数映射后，a对应的值为`[0, 1], [1, 2], [0, 3], [1, 4], [0, 5]`。这些list比较时也遵从着升序的规律，于是此处sort可以被理解为“奇数放前面，若同为奇数则数值较小的放前面”。**由此我们可以通过key+lambda+list来制定多重的比较规则，十分好用**。

- 当然，当lambda函数并不方便时，我们也可以写一个函数方法传入key中，例如上述例子我们可以写为：
  
```python
a = [1,2,3,4,5]
def trans(x):
    return (1, x) if x % 2 == 0 else (0, x)
a.sort(key=trans)
a # -> [1,3,5,2,4]
```

虽然这样写有些画蛇添足，但对于一些更复杂的数据结构，我们可以完成更多的运算操作，最终返回元组/list即可。

- 也可以直接传入一些常用的函数方法，如：

```python
a = ["This", "is", "the", "greatest", "warrior"]
a.sort()
a # -> ['This', 'greatest', 'is', 'the', 'warrior']
a.sort(str.lower)
a # -> ['greatest', 'is', 'the', 'This', 'warrior']
b = ["123", "23", "34", "5"]
b.sort(key=int)
b # -> ['5', '23', '34', '123']
```

- 在早期的python中sort还有一个cmp关键字，用来传入排序时两两比较的规则（这一点与其他语言比较类似），但在python3中被废弃，但我们仍然可以通过functools.cmp_to_key，来制定好规则后再传入key参数中使用。

在使用时，我们定义一个`def rule(x, y)`，我们可以默认x要排在y前面，那么这时利用我们想要的规则返回一个负值即可。**cmp默认负值代表小于，正值代表大于**。例如我们实现默认的升序排序，这里给出**一个错误示范**：

```python
# 一个错误的版本
a = [3,5,1,2,4]
def rule(x, y):
    if x < y:
        return -1
a.sort(cmp=rule)
```

这里有两处错误：1，python3已经废除了cmp关键词，必须通过前面提到的functools转换；2，如果 x >= y，这里是没有返回值的，在比较时就变成了None和int比显然比不了，也即必须所有的比较情况都能返回一个正值、负值或0。改写后如下：

```python
# 正确版本
import functools
a = [3,5,1,2,4]
def rule(x, y):
    if x < y:
        return -1
    elif x > y:
        return 1
    else:
        return 0
a.sort(key=functools.cmp_to_key(rule))
```

当然，可以简写为：
```python
import functools
a = [3,5,1,2,4]
def rule(x, y):
    return x - y
a.sort(key=functools.cmp_to_key(rule))
```

在实际使用中，**可以把x，y想象成排序后的两个对象，并想办法使其返回负值即可，如果使用if-else则要注意不要漏掉什么情况不返回值。**


参考资料：[Python排序sorted()函数里cmp_to_key和cmp](https://zhuanlan.zhihu.com/p/505195096)

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
  
python自带的随机库是random。

1. 生成整数随机数：randint(start, stop)，或者randrange(start, stop+1)，两者等价，前者左闭右闭，后者左闭右开，start和stop都是整数。
2. 生成浮点随机数：uniform(x, y)，左闭右闭！
3. 生成0-1的随机数：random()，这个是左闭右开，相当于是[0,1)
4. 从序列返回一个随机元素：choice(seq)。要求序列非空，否则indexError。
5. 从序列返回多个随机元素：choices(seq, weights=None, cum_weights=None, k=1)。同样要求序列非空（和k的大小无关）。注意choices可以按权重（list格式）或者累计权重来抽样，某些情况下很好使。另外注意choices返回的是list(list())。k=1的时候需要[0]一下。
   
更多细节可以参见：[python官方文档 - random](https://docs.python.org/3/library/random.html)。

- 水塘抽样

# 14. @staticmethod

声明，不强制要求传递参数的静态方法。[Python staticmethod() 函数](https://www.runoob.com/python/python-func-staticmethod.html)


# 15. 关于哈希、集合的操作

- setdefault

```python
d = {}
d.setdefault(key1, a)
d.setdefault(key1, b)
```

那么`d[key1]`应该会输出a。setdefault的含义是，对某一键值尝试复制，若存在该键则不做改变，若不存在该键则赋值。这个操作很适合对“存在性”做记录，省去了一些if else的麻烦。



# 线段树

# 排序总结

参考资料：[排序算法总结](https://www.runoob.com/w3cnote/sort-algorithm-summary.html)

lowb三人组：冒泡，选择，插入。时间复杂度均为$O(n^2)$

- 冒泡排序就像泡泡浮起来，所以说是两两比较，把小的放到前边大的放后边，典型场景就是**小时候排队，两两互比身高站前后**；
- 选择排序是每次找到序列中最小的一个放在前面，很像冒泡，也像是排队，但像是老师给安排队伍，**从全局来看而非两两比较**；
- 插入排序典型场景就是**打扑克揭牌**，每揭一张我们就插入到本就有序的牌堆中，保持其有序性至终止。

高级三人组：快排，归并，堆。时间复杂度均为$O(nlogn)$

- 快速排序简言之就是分治+pivot，但在具体实现上，可以通过双指针查找。一般来讲我们选择第一个数为pivot（或理解为把pivot放在最前面），所以**开始时要从后向前查找**，挖坑填数。性能受制于pivot取得好不好，差时退化为选择排序，所以可以通过随机化改进。
- 归并排序亦作二路归并，是典型的二分分治法，分即将一个数组的排序问题二分为两个，治则采用**双指针合并之**。
- 堆排序则像是**官职制度**，省长管市长，市长管区长，能者擢升，不能者下放，从而达到整个队列的有序化。

其他：希尔排序、桶排序、基数排序

- 希尔排序可以看做是对插入排序的改进（在lowb三人组中，插入排序是比较好的），初始设置一个gap=length/2（最初Shell声称的版本，后续还有其他的gap计算方式），以gap为步长进行两两比较地插入排序，然后逐渐缩小gap，故亦称**缩小增量排序**。这样做仍然达不到$O(nlogn)$，但是可以减少插入排序的长程交换，最终复杂度改善至$O(n^{1.3\sim2.0})$。关于希尔排序的图解可以参见[菜鸟教程](https://www.runoob.com/data-structures/shell-sort.html)。
- 桶排序的思想就比较简单了，**一个萝卜一个坑**，开一个很大的内存，你是几就放在第几个，因此内存开销较大且受制于极端数字，但是时间上是O(n)
- 基数排序则在桶排序的基础上进行改进，即**先比个位再比十位百位**，依次得到大小关系。

参考代码：

- 随机化快排
```python
class Solution:
    def randomizedPartition(self, nums, left, right):
        pivot = random.randint(left, right)
        nums[right], nums[pivot] = nums[pivot], nums[right]
        i = left
        for j in range(left, right):
            if nums[j] < nums[right]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[right], nums[i] = nums[i], nums[right]
        return i
    
    def randomizedQuicksort(self, nums, left, right):
        if left >= right:
            return
        index = self.randomizedPartition(nums, left, right)
        self.randomizedQuicksort(nums, left, index - 1)
        self.randomizedQuicksort(nums, index + 1, right)
        
    def sortArray(self, nums: List[int]) -> List[int]:
        self.randomizedQuicksort(nums, 0, len(nums) - 1)
        return nums
```

- 归并排序
```python
class Solution:
    def merge_sort(self, nums, left, right):
        if left == right:
            return
        mid = (left + right) // 2
        self.merge_sort(nums, left, mid)
        self.merge_sort(nums, mid + 1, right)
        i, j = left, mid + 1
        temp = []
        while i <= mid or j <= right:
            if i > mid or (j <= right and nums[i] > nums[j]):
                temp.append(nums[j])
                j += 1
            else:
                temp.append(nums[i])
                i += 1
        nums[left:right+1] = temp


    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums, 0, len(nums) - 1)
        return nums
```

- 堆排序

```python
class Solution:
    def maxHeapify(self, heap, heaplen, p): # 大根堆sift函数
        # 先找到左右子节点更大的那一个，再比较
        while p*2+1 < heaplen:
            left, right = p*2+1, p*2+2
            if right < heaplen and heap[right] > heap[left]: # 右子节点未越界且右大于左，交换右
                nex = right
            else: # 右子节点越界或右小于左
                nex = left
            if heap[nex] > heap[p]:
                heap[nex], heap[p] = heap[p], heap[nex]
                p = nex
            else:
                break
    
    def heapsort(self, heap):
        n = len(heap)
        # 建堆要从第一个非叶子结点到根节点遍历sift调整
        for i in range(n // 2 - 1, -1, -1):
            self.maxHeapify(heap, n, i)
        # 排序：交换首尾，每次区间长度-1，对heap[0] sift调整
        for heaplen in range(n - 1, 0, -1):
            heap[0], heap[heaplen] = heap[heaplen], heap[0]
            self.maxHeapify(heap, heaplen, 0)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.heapsort(nums)
        return nums
```

# 优先队列、heapq
参考资料：[Python标准库模块之heapq](https://www.jianshu.com/p/801318c77ab5)

此库即优先队列，也即（小根）堆，处理一些流式添加、并维护递增/减性的问题较为好使，时间复杂度在$O(\log n)$。如需使用大根堆可以对list取负。用法：

- 建堆：heapify(list)，或使用heappush对空列表逐个添加元素
- 添加元素：heappush(list, a)，对list添加a元素，要求list是一个已经建好的堆。如果list不是堆，就直接塞到末尾了。
- 弹出元素：heappop(list)，弹出堆顶元素并调整推，返回堆顶元素的值。同样如果list不是堆，也是直接弹出列表第一个元素。

# 单调栈/单调队列

单调栈/单调队列旨在维护一个递增/递减数组的下标，注意几点：
- 因为其是不断前出后进的，一般要用双向队列

# DP、记忆化搜索

DP有两个关键性质：最优子结构、重叠子问题

- 最优子结构：一个问题的最优解包含其子问题的最优解。
- 重叠子问题：问题的递归算法会反复地求解相同的子问题，而不是一直生成新的子问题

参考资料：[百度文库 - 动态规划原理](https://wenku.baidu.com/view/ecf0156bf4ec4afe04a1b0717fd5360cba1a8d0d.html)

记忆化搜索比较像是DFS与DP的产物，即在DFS时记录状态对应的信息，以达到减少重复搜索、剪枝的目的。我们常用二进制表示来作为状态的记录，例如当搜索位数有10位时，我们就可以使用10个0/1表示此

# 数位DP

数位DP的本质还是记忆化搜索，通常用于解决给你一个n，和一些条件，问满足这些条件的1-n之间的数有多少个。从1开始枚举的话往往要超时，所以可以从数位的角度出发，以期在某些条件重叠时利用DP达到优化。

主要有四个参数：
- i表示枚举的数位，这个必须有；
- mask可选，用于记录已经使用过哪些数字，如果题目没有这方面要求就不必有mask，有时也可以是一个布尔变量；
- isLimit表示当前是否为临界值，如给定的n是1234，如果枚举的第一位是1，第二位讨论是isLimit就要设为True，因为其枚举范围被限制在0~2之间；相应地如果第二位为2，进入第三位讨论时isLimit仍要保持为True，以此类推；
- isNum表示是否有先导零，或者表示是否跳过此位，设置为False时表示跳过（此时不为合法数字），有前导零，设置为True表示是一个数字，此后不可跳过。当题目对前导零不限制时也可以没有此变量。

模板：
```python
@cache
def dp(i: int, mask: int, isLimit: bool, isNum: bool) -> int:
    # 终止条件
    if i == len(s):
        return int(isNum) # 一直跳返回0，没有跳过返回1
    
    res = 0
    if not isNum: # 【只有在前边都跳过的时候】才能继续跳过，否则就是补0了
        res = dp(i+1, mask, False, False)
    
    # 开始枚举，首先找出枚举上限和下限
    up = int(s[i]) if isLimit else 9
    down = 0 if isNum else 1
    for j in range(down, up+1):
        if mask >> j & 1 == 0:
            res += dp(i+1, mask|(1<<j), j == up and isLimit, True)
    return res

return dp(0, 0, True, False) # 外部，从初值进入
```
- mask不是必须的，要根据题目条件的含义变化
- 其他语言dp时可以不必对isLimit和isNum存储，只要对i和mask dp即可。

# 二叉搜索树

一个二叉搜索树的中序遍历是递增的。

# lowbit，树状数组

lowbit即找到从低位起数，第一个1；相对地也有highbit，意为从高位往低位数第一个1。

## Gosper's Hack

这是一个搜索算法，用于解决在n位中选取m位做一些操作的问题。我们固然可以使用itertools.combinations之类的库来完成，但是代码不甚简洁，这里可以**使用位运算**来达到快捷枚举的目的。

通过位运算来表示枚举位的核心问题是，如何通过当前枚举数找到下一个枚举数。例如，我们从7位中选取4位，则考虑一个8位二进制数，1表示选取，0表示不选取，那么一种朴素的枚举方式便是从低位全1（“0001111”）枚举到高位全1（“1111000”）。那么，假如当前枚举到了“0101110”，如何找到下一个枚举数呢？（答案应该是“0110011”）

Gosper's Hack解决的就是此问题，思路是找到右起第一个“01”将之变为“10”，然后让其右侧（低位）的所有1都右移到最右侧（即右侧有几个1就从右起补几个1）。

我们可以通过lowbit来实现从“01”到“10”这个进位过程，只要给x补充一个lowbit即可。求解lowbit的方式是`x & -x`这个一定要记住。于是`x + lowbit`便形成了目标答案的左半部分。如何得到右半部分呢？只要x与左半部分异或，就可以得到右半部分和进位的“01”、“10”此处的两个异或得到的1。

![Gosper's Hack](pngs/gosper.png)

具体的计算过程如上图所示，考虑一个n位中选取m位的问题，总结为：

- 先计算lowbit：`lowbit = x & -x`
- 再计算左边：`left = x + lowbit`
- 再计算右边：`right = (x ^ left) // lowbit >> 2`
- 左右结合得到下一值：`tgt = left | right`
- 开始枚举遍历，初始值是`(1 << m) - 1`，终止值可以设定为`1 << n`。

参考资料：[【力扣双周赛 86】位运算黑科技 | 单调队列 | LeetCode 算法刷题](https://www.bilibili.com/video/BV1na41137jv/?vd_source=35801b0cdcf955efe0e9b490935ab8ca)

例题：[2397. 被列覆盖的最多行数](https://leetcode.cn/problems/maximum-rows-covered-by-columns/)，参考代码（另，注意将list of int转换为二进制对应数的技巧语句）：
```python
class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:

        mask = [sum(val << i for i, val in enumerate(row)) for row in matrix]

        n = len(matrix[0])
        x = (1 << numSelect) - 1
        ans = 0
        while x < (1 << n):
            cnt = sum([line & x == line for line in mask])
            ans = max(ans, cnt)
            lb = x & -x
            left = x + lb
            right = (x ^ left) // lb >> 2
            x = left | right
        return ans
```

# 快速幂

考虑一个求x的n次幂的问题。有点类似于钱币凑钱的问题——一个十进制数可以通过对若干个二进制数进行取与不取的抉择，得到一个0与1组成的二进制数；而此处求幂，我们构造了“基底”为$x^1, x^2, x^4...$，取与不取的加和操作由指数映射变为了相乘操作，由此便可以在$\log n$时间内拆解问题。

具体的实现上，我们可以：
- 设置一个res=1作为返回答案
- 通过n & 1 == 1判断此位“基底”x是否需要与res相乘
- 对x * x作为下一组基底，此后循环判断

# 并查集


