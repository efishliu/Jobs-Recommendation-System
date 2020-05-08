
var a1=['java','计算机','团队合作','学习能力','二次开发','英语四级','PHP','开发经验','敬业精神','实习生','网页','平面设计','前端','web','软件开发','UI','C/C++','linux','移动开发','文档能力','应用软件','数据库','工程师','程序员']


function getskills()
{
    var industry=document.info.industry.value;
    var node='<h4 class="skills"><table>';
    if (industry=="计算机软件")
    {
        for(var m=0;m<3;m++){
            node+='<tr>'
            for(var i=0;i<6;i++)
            {
                node+='<td><input type="checkbox" name="skill"  data-labelauty="'+a1[i+m*6]+'" value="'+a1[i+m*6]+'"></td>'
            }
            node+='</tr>'
        }
        node+='</h4>'
        $("h4.skills").replaceWith(node); 
        $(':input').labelauty();
        }

}