# DMZJ-Comic-list
下载动漫之家里面用户关注的所有漫画的相关信息，包含被屏蔽隐藏的漫画，方便做备份，天下苦B久已


这个是主要的api用于根据comic_id获取comic_info
getcomicurl = 'http://api.dmzj.com/dynamic/comicinfo/' + str(comicid) + '.json'

一下两个是参考别人的，登录&获取我的关注列表（返回的id_list）
loginurl = 'http://i.dmzj.com/api/login?callback=&nickname='+user+'&password='+passward+'&type=1'
mysubscribeurl = 'http://m.dmzj.com/mysubscribe'
