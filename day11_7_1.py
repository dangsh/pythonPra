import requests
from bs4 import BeautifulSoup
import pandas

html = """
<li>
<div class="item">
<div class="pic">
<em class="">25</em>
<a href="https://movie.douban.com/subject/1292000/">
<img alt="搏击俱乐部" class="" src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p1910926158.jpg" width="100"/>
</a>
</div>
<div class="info">
<div class="hd">
<a class="" href="https://movie.douban.com/subject/1292000/">
<span class="title">搏击俱乐部</span>
<span class="title"> / Fight Club</span>
<span class="other"> / 搏击会(港)  /  斗阵俱乐部(台)</span>
</a>
</div>
<div class="bd">
<p class="">
                            导演: 大卫·芬奇 David Fincher   主演: 爱德华·诺顿 Edward Norton / 布拉...<br/>
                            1999 / 美国 德国 / 剧情 动作 悬疑 惊悚
                        </p>
<div class="star">
<span class="rating45-t"></span>
<span class="rating_num" property="v:average">9.0</span>
<span content="10.0" property="v:best"></span>
<span>411411人评价</span>
</div>
<p class="quote">
<span class="inq">邪恶与平庸蛰伏于同一个母体，在特定的时间互相对峙。</span>
</p>
</div>
</div>
</div>
</li>
"""

soup = BeautifulSoup(html)
# print(soup.prettify()) #格式化输出soup
print(soup.title)