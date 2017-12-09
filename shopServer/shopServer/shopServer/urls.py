"""shopServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from shopApp.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^goodsManage/$' , goodsManage),
    url(r'^adPage/$' , adPage),
    url(r'^userManage/$' , userManage),
    url(r'^orderManage/$' , orderManage),
    url(r'^adManage/$' , adManage),
    url(r'^changePic/$' , changePic),#改变轮播图界面
    url(r'^loginApi/$' , loginApi),  # 登录接口 
    url(r'^register/$' , userManageJsonAdd), # 添加用户接口 
    url(r'^userManageJsonAdd/$' , userManageJsonAdd), # 添加用户接口
    url(r'^userManageJsonSelect/$' , userManageJsonSelect), # 查询用户接口
    url(r'^activeManage/$' , activeManage),

    url(r'^adManageJsonAdd/$' , adManageJsonAdd), # 广告添加的接口
    url(r'^adManageJsonSelect/$' , adManageJsonSelect), # 广告列表的接口  
    url(r'^adManageJsonDelete/$' , adManageJsonDelete), # 广告删除的接口

    url(r'^goodsManageJsonAdd/$' , goodsManageJsonAdd),  # 商品添加接口
    url(r'^goodsManageJsonSelect/$' , goodsManageJsonSelect),  # 商品查询接口   
    url(r'^addGoods/$' , addGoods),  # 添加商品接口


    url(r'^goodsManageJsonSelect/$' , goodsManageJsonSelect),  # 商品列表接口   
    url(r'^goodsManageJsonUpdata/$' , goodsManageJsonUpdata), # 商品列表修改接口
    url(r'^goodsManageJsonDelete/$' , goodsManageJsonDelete),  # 商品列表删除接口
    url(r'^goodsSelectByid/$' , goodsSelectByid), # 根据商品id查找商品
    url(r'^commodityQuery/$' , commodityQuery), # 商品模糊查询接口查找商品

    
    url(r'^activetableManageJsonAdd/$' , activetableManageJsonAdd),  # 活动添加接口
    url(r'^activeManageJsonSelect/$' , activeManageJsonSelect), # 活动列表接口
    url(r'^activetableManageJsonDelete/$' , activetableManageJsonDelete), # 活动删除接口接口

    url(r'^ordertableManageJsonAdd/$' , ordertableManageJsonAdd), # 订单添加接口
    url(r'^ordertableDelete/$' , ordertableDelete), # 订单删除接口
    url(r'^ordertableManageJsonSelete/$' , ordertableManageJsonSelete), # 订单列表接口

    url(r'^personal/$' , personal),      

    url(r'^$' , home),
    url(r'^.' , error),
]
