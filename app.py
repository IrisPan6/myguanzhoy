import streamlit as st
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# ========== 邮件配置 ==========
SENDER_EMAIL = "2073987660@qq.com"
SENDER_PASSWORD = "qccmjrsgcccnfdfg"
RECEIVER_EMAIL = "2073987660@qq.com"

SMTP_SERVER = "smtp.qq.com"
SMTP_PORT = 587

def send_email(subject, body, attachment=None):
    try:
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = RECEIVER_EMAIL
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain", "utf-8"))
        
        if attachment is not None:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename={attachment.name}")
            msg.attach(part)
        
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
        return True, "发送成功"
    except Exception as e:
        return False, str(e)

# ---------- 页面配置 ----------
st.set_page_config(page_title="长丰刑侦支队", page_icon="🛡️", layout="wide")

# ---------- CSS 样式 ----------
st.markdown("""
<style>
.stApp { background-color: #ffffff; }
.hero {
    background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
    padding: 2rem;
    border-radius: 1rem;
    color: #f0f0f0;
    margin-bottom: 2rem;
}
.hero h1 { font-size: 2.5rem; margin: 0 0 0.5rem 0; color: white; }
.hero .sub {
    font-size: 1rem;
    border-left: 3px solid #3b82f6;
    padding-left: 1rem;
    margin-bottom: 1.5rem;
}
.info-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    background: rgba(255,255,255,0.08);
    border-radius: 1rem;
    padding: 0.8rem 1.5rem;
}
.info-item { flex: 1; min-width: 120px; }
.info-label { font-size: 0.7rem; opacity: 0.7; color: #ccc; }
.info-value { font-size: 0.95rem; color: white; }
.section-title {
    font-size: 1.6rem;
    font-weight: 600;
    border-left: 5px solid #3b82f6;
    padding-left: 1rem;
    margin: 1.5rem 0 1rem 0;
    color: #111;
}
.honor-list-custom {
    background: #f8f9fa;
    border-radius: 1rem;
    padding: 1.2rem 1.8rem;
    list-style: none;
    border: 1px solid #e9ecef;
}
.honor-list-custom li {
    margin-bottom: 0.6rem;
    padding-left: 1.5rem;
    position: relative;
}
.honor-list-custom li::before {
    content: "▹";
    position: absolute;
    left: 0;
    color: #3b82f6;
}
.stButton button {
    background-color: #2c3e50;
    color: white;
    border: none;
}
.stButton button:hover { background-color: #3b82f6; }
.sidebar-title { font-size: 1.4rem; font-weight: bold; color: #111; }
.case-card {
    background: #f8f9fa;
    padding: 1rem;
    border-radius: 1rem;
    margin-bottom: 1rem;
    border-left: 4px solid #3b82f6;
}
</style>
""", unsafe_allow_html=True)

# ---------- 侧边栏 ----------
st.sidebar.markdown('<div class="sidebar-title">🛡️ 长丰刑侦支队</div>', unsafe_allow_html=True)
option = st.sidebar.radio("导航菜单", ["🏠 主页", "👮 警员介绍", "📅 支队经历", "🏆 支队荣誉", "✉️ 警民信箱"], label_visibility="collapsed")

# ========== 1. 主页（已删除荣誉墙部分）==========
if option == "🏠 主页":
    st.markdown("""
    <div class="hero">
        <h1>长丰刑侦支队</h1>
        <div class="sub">特别能战斗刑警队 · 命案必破的金字招牌</div>
        <div class="info-grid">
            <div class="info-item"><div class="info-label">成立时间</div><div class="info-value">1998年</div></div>
            <div class="info-item"><div class="info-label">警员人数</div><div class="info-value">120余人</div></div>
            <div class="info-item"><div class="info-label">下设单位</div><div class="info-value">重案大队、技术大队、情报研判中心</div></div>
            <div class="info-item"><div class="info-label">管辖区域</div><div class="info-value">津港市长丰区</div></div>
            <div class="info-item"><div class="info-label">荣誉称号</div><div class="info-value">特别能战斗刑警队</div></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-title">支队概况</div>', unsafe_allow_html=True)
    st.write("津港市公安局长丰刑侦支队是一支具有光荣传统和赫赫战功的英雄警队。支队现有警员120余人，下设重案大队、技术大队、情报研判中心等。在历代干警的共同努力下，长丰刑侦连续多年实现命案全破，打出了“命案必破”的金字招牌。")
    st.markdown('**“命案必破，不破不休”** —— 这是长丰刑侦支队刻在骨子里的信条。')
    
    # 支队风采三张照片
    st.markdown('<div class="section-title">📸 支队风采</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: 
        try:
            st.image("支队daquanjing.jpg", caption="支队全景", use_container_width=True)
        except:
            st.info("📷 支队全景")
    with c2: 
        try:
            st.image("zhidui1.jpg", caption="支队内部", use_container_width=True)
        except:
            st.info("📷 支队内部1")
    with c3: 
        try:
            st.image("zhidui2.jpg", caption="支队内部", use_container_width=True)
        except:
            st.info("📷 支队内部2")
    
    # 支队风采快照
    st.markdown('<div class="section-title">📸 支队风采快照</div>', unsafe_allow_html=True)
    st.markdown("长丰刑侦支队工作与生活掠影")
    
    col_a, col_b = st.columns(2)
    with col_a:
        try:
            st.image("heying1.jpg", caption="支队人员办案快照", use_container_width=True)
        except:
            st.info("📷 办案快照1")
    with col_b:
        try:
            st.image("heying2.jpg", caption="支队人员办案快照", use_container_width=True)
        except:
            st.info("📷 办案快照2")
    
    col_c, col_d = st.columns(2)
    with col_c:
        try:
            st.image("heying3.jpg", caption="支队人员办案快照", use_container_width=True)
        except:
            st.info("📷 办案快照3")
    with col_d:
        try:
            st.image("heying4.jpg", caption="支队人员办案快照", use_container_width=True)
        except:
            st.info("📷 办案快照4")
    
    col_e, col_f = st.columns(2)
    with col_e:
        try:
            st.image("zhaogao.jpg", caption="支队警员合影", use_container_width=True)
        except:
            st.info("📷 支队警员合影")
    with col_f:
        st.markdown("---")
    
    st.caption(f"© 长丰刑侦支队政治处 | 更新：{datetime.now().strftime('%Y-%m-%d')}")

# ========== 2. 警员介绍 ==========
elif option == "👮 警员介绍":
    st.header("👮‍♂️ 长丰刑侦精英")
    st.markdown("点击下方按钮，查看警员详细信息")
    
    officers = {
        "关宏峰": {
            "职务": "原支队长，现任特聘首席刑侦专家",
            "基本信息": "1977年11月20日出生，津港市人，中共党员",
            "学历": "中国人民公安大学刑事科学技术专业毕业，在职研究生学历，法学博士学位",
            "从警经历": "1998年参加公安工作，曾任长丰刑侦支队队长。",
            "主要事迹": "全国优秀人民警察，指挥侦破华堂纵火案、3·19大案等逾千起案件，创下连续多年命案全破记录。",
            "荣誉": "全国公安系统一级英雄模范、全国优秀人民警察、津港市劳动模范",
            "照片": "guanhongfeng.jpg"
        },
        "周巡": {
            "职务": "长丰刑侦支队支队长",
            "基本信息": "1982年7月24日出生，津港市人，中共党员（2000年入党）",
            "学历": "津港市警察学院本科侦查系毕业",
            "从警经历": "2000年参加工作，任地区队探员；后任北部地区队长；降级申调回长丰支队任支队长助理；后升任支队长。",
            "主要事迹": "参与侦破213灭门案、王志革系列杀人案等重大案件。",
            "荣誉": "个人一等功、津港市优秀共产党员",
            "照片": "zhouxun.jpg"
        },
        "周舒桐": {
            "职务": "长丰刑侦支队刑警",
            "基本信息": "津港市人",
            "学历": "2016年毕业于津港市警察学校",
            "从警经历": "2016年被选入长丰刑侦支队，成为最年轻警员之一。",
            "主要事迹": "参与王志革案、213案等；在行动中主动交换人质，表现勇敢。",
            "荣誉": "个人嘉奖",
            "照片": "zhoushutong.jpg"
        },
        "汪苗": {
            "职务": "长丰刑侦支队刑警",
            "基本信息": "1988年3月24日出生，津港市人，无党派",
            "学历": "",
            "从警经历": "4年基层工作经历后调入长丰刑侦支队。",
            "主要事迹": "参与多起刑事案件侦破，善于梳理线索。",
            "荣誉": "",
            "照片": "wang.jpg"
        },
        "赵茜": {
            "职务": "长丰刑侦支队技术队民警",
            "基本信息": "",
            "学历": "刑警学院研究生",
            "从警经历": "从市局技术处调入长丰支队。",
            "主要事迹": "参与破获9·15连环杀人案、4·23强奸分尸案，提供关键物证支持。",
            "荣誉": "",
            "照片": "zhaoqian.jpg"
        },
        "高亚楠": {
            "职务": "法医主任",
            "基本信息": "",
            "学历": "",
            "从警经历": "",
            "主要事迹": "首席法医，破获多起悬案。",
            "荣誉": "全国刑事技术标兵",
            "照片": "gaoyanan.jpg"
        }
    }
    
    selected = None
    names = list(officers.keys())
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button(names[0], key=names[0]): selected = names[0]
    with col2:
        if st.button(names[1], key=names[1]): selected = names[1]
    with col3:
        if st.button(names[2], key=names[2]): selected = names[2]
    col4, col5, col6 = st.columns(3)
    with col4:
        if st.button(names[3], key=names[3]): selected = names[3]
    with col5:
        if st.button(names[4], key=names[4]): selected = names[4]
    with col6:
        if st.button(names[5], key=names[5]): selected = names[5]
    
    if selected:
        info = officers[selected]
        st.subheader(f"{selected} · {info['职务']}")
        a,b = st.columns([1,2])
        with a:
            if info["照片"]: 
                try:
                    st.image(info["照片"], width=200)
                except:
                    st.info("📷 照片加载失败")
            else: 
                st.info("暂无照片")
        with b:
            if info["基本信息"]:
                st.write(f"**基本信息**：{info['基本信息']}")
            if info["学历"]:
                st.write(f"**学历**：{info['学历']}")
            if info["从警经历"]:
                st.write(f"**从警经历**：{info['从警经历']}")
            st.write(f"**主要事迹**：{info['主要事迹']}")
            if info["荣誉"]:
                st.write(f"**荣誉**：{info['荣誉']}")
    else:
        st.info("👆 请点击上方警员名字查看详情")

# ========== 3. 支队经历（新增三个案件的详细描述）==========
elif option == "📅 支队经历":
    st.header("📅 重大历程与经典案件")
    st.markdown("长丰刑侦支队侦破的重大案件回顾")
    
    # 案件1：狂欢型连环杀人案
    with st.expander("🔪 狂欢型连环杀人案（高远案）", expanded=True):
        st.markdown("""
        **案件时间**：2016年前后
        
        **案件概述**：  
        津港市长丰区发生系列恶性杀人案件。犯罪嫌疑人高远先后杀害合租室友王晨，以及谢静、谢玉兄妹二人，作案手段残忍，具有典型的狂欢型杀人特征。
        
        **侦破过程**：  
        专案组通过对抛尸地点及周边环境的系统分析，结合受害人王晨尸体上遗留的生活痕迹——包括其饲养猫科动物、驾驶手动挡车辆等细节，逐步缩小排查范围，最终精准锁定其租住地址。同时，侦查人员对嫌疑人的作案手法和抛尸规律进行深度研判，发现高远利用送餐员身份，以外卖箱作为掩护运输尸体，从而躲避公众视线。
        
        **案件结局**：  
        在案件收尾阶段，高远潜入长丰支队，企图加害时任支队长关宏峰。对抗过程中，高远失足坠楼身亡。该案告破后，支队对内部安防机制进行了全面升级。
        """)
        col1, col2 = st.columns(2)
        with col1:
            try:
                st.image("gaoyuan1.jpg", caption="高远案相关物证", use_container_width=True)
            except:
                st.info("📷 高远案图片1（gaoyuan1.jpg）")
        with col2:
            try:
                st.image("gaoyuan2.jpg", caption="高远案侦破现场", use_container_width=True)
            except:
                st.info("📷 高远案图片2（gaoyuan2.jpg）")
    
    st.divider()
    
    # 案件2：王志革系列杀人案
    with st.expander("🚗 王志革系列杀人案（“车震杀手”案）", expanded=True):
        st.markdown("""
        **案件时间**：2013年至2016年
        
        **案件概述**：  
        津港市海港区、长丰区连续发生多起针对车内情侣的恶性袭击案件，多名受害者在暴雨夜的封闭车厢内遭钝器重击身亡。由于嫌疑人作案手法隐蔽、反侦查意识极强，案件侦办一度进展缓慢。
        
        **侦破过程**：  
        长丰支队与海港支队成立联合专案组，对嫌疑人作案规律、车辆特征、活动轨迹进行长期缜密排查，最终锁定物证鉴定领域专业人员王志革。在收网行动中，王志革挟持人质负隅顽抗，专案组通过心理攻势迫使其短暂暴露，狙击手抓住战机将其击毙，人质安全获救。
        
        **案件意义**：  
        该案是跨区域警务协作的成功范例，也是长丰支队在疑难命案攻坚能力上的重要体现。
        """)
        try:
            st.image("wangzhige.jpg", caption="王志革案侦破现场", use_container_width=True)
        except:
            st.info("📷 王志革案图片（wangzhige.jpg）")
    
    st.divider()
    
    # 案件3：9·15连环杀人案
    with st.expander("🔬 9·15连环杀人案（积案攻坚）", expanded=True):
        st.markdown("""
        **案件时间**：20余年前发生，近年告破
        
        **案件概述**：  
        津港市发生系列重大刑事案件，多名受害者在不同地点遇害，作案手法高度相似。由于当时技术条件有限，案件长期未破，成为市局挂牌督办积案。
        
        **侦破过程**：  
        长丰支队技术队民警赵茜参与专案组后，对旧案物证进行系统性复检，运用微量物证提取技术从保存多年的物证中检出新线索。经比对，成功锁定嫌疑人，为该系列案件侦破提供了关键证据。
        
        **案件意义**：  
        该案的告破，展示了刑事科学技术在积案攻坚中的核心作用，也体现了长丰支队技术队扎实的专业功底。
        """)
        try:
            st.image("jiuyiqi.jpg", caption="9·15案物证复检工作照", use_container_width=True)
        except:
            st.info("📷 9·15案图片（jiuyiqi.jpg）")
    
    st.divider()
    
    # 原有历史事件（保留）
    st.markdown('<div class="section-title">📜 支队历史大事记</div>', unsafe_allow_html=True)
    events = {
        "2005 获国务院‘特别能战斗刑警队’称号": {"时间": "2005年", "描述": "被国务院授予荣誉称号，荣记集体一等功。"},
        "2008 侦破‘3·19’大案": {"时间": "2008年3月", "描述": "三天内锁定真凶，创破案奇迹。"},
        "2010 市委发出向关宏峰学习决定": {"时间": "2010年", "描述": "号召全市学习关宏峰精神。"},
        "2020 智慧刑侦实验室落成": {"时间": "2020年", "描述": "建成全省首个智慧刑侦实验室。"}
    }
    for event_name, event_info in events.items():
        st.markdown(f"""
        <div style="background:#f8f9fa; padding:0.8rem; border-radius:0.5rem; margin-bottom:0.5rem;">
            <strong>{event_name}</strong><br>
            <span style="color:#666;">{event_info['时间']}</span> - {event_info['描述']}
        </div>
        """, unsafe_allow_html=True)

# ========== 4. 支队荣誉 ==========
elif option == "🏆 支队荣誉":
    st.header("🏆 荣誉墙")
    st.markdown("""
    <div class="section-title">集体荣誉</div>
    <ul class="honor-list-custom">
        <li>2005年被国务院授予 <strong>"特别能战斗刑警队"</strong></li>
        <li>2005年被公安部荣记 <strong>集体一等功</strong></li>
        <li>2007年 <strong>"全省文明单位标兵"</strong></li>
        <li>2008年 <strong>"全国公安机关侦破命案先进集体"</strong></li>
        <li>2009年 <strong>"人民满意的公务员集体"</strong></li>
    </ul>
    <div class="section-title">个人荣誉（关宏峰）</div>
    <ul class="honor-list-custom">
        <li>全国公安系统一级英雄模范</li>
        <li>全国优秀人民警察</li>
        <li>津港市劳动模范</li>
    </ul>
    """, unsafe_allow_html=True)
    c1,c2,c3 = st.columns(3)
    c1.metric("省部级以上荣誉", "12项")
    c2.metric("集体一等功", "3次")
    c3.metric("个人立功受奖", "46人次")

# ========== 5. 警民信箱 ==========
elif option == "✉️ 警民信箱":
    st.header("✉️ 网站修改平台")
    st.markdown("首先感谢访问网站的友友们，其次因为个人能力有限，希望大家能给这个网址提一些建议，包括布局、内容、图片、板块等等 欢迎提交你宝贵的建议！")

    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("您的姓名或昵称")
        contact = st.text_input("联系方式（电话/邮箱）", placeholder="便于我们回复您")
        msg_type = st.selectbox("建议类型", ["图片", "文字内容", "内容板块", "布局设计"])
        content = st.text_area("建议内容", height=200)
        attachment = st.file_uploader("上传附件（图片/文档）", type=["jpg", "png", "pdf", "txt"])

        submitted = st.form_submit_button("📤 提交建议")
        if submitted:
            if not name or not content:
                st.error("请填写姓名和建议内容")
            else:
                email_body = f"""
                收到来自长丰刑侦支队网站的新建议：

                姓名/昵称：{name}
                联系方式：{contact if contact else '未提供'}
                建议类型：{msg_type}
                提交时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

                建议内容：
                {content}
                """
                email_subject = f"【网站修改建议】{msg_type} - 来自{name}"
                success, msg = send_email(email_subject, email_body, attachment)
                if success:
                    st.success(f"✅ {name}，您的建议已成功提交！感谢您的宝贵意见。")
                else:
                    st.error(f"❌ 发送失败：{msg}\n请检查发件邮箱配置或网络。")
                    st.info("您的建议内容已保留，可稍后尝试或直接联系支队。")

    st.divider()
    st.caption("📢 再次感谢您的支持，每条建议我们都会认真阅读！")

# 侧边栏底部
st.sidebar.markdown("---")
st.sidebar.caption("📞 长丰刑侦值班电话：022-110转长丰支队")
st.sidebar.caption("⚡ 命案必破 · 不破不休")