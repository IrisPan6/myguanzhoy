import streamlit as st
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# ========== 邮件配置（已更新授权码）==========
SENDER_EMAIL = "2073987660@qq.com"          # 你的发件邮箱
SENDER_PASSWORD = "qccmjrsgcccnfdfg"        # 新的16位QQ邮箱授权码
RECEIVER_EMAIL = "2073987660@qq.com"        # 收件邮箱

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
</style>
""", unsafe_allow_html=True)

# ---------- 侧边栏 ----------
st.sidebar.markdown('<div class="sidebar-title">🛡️ 长丰刑侦支队</div>', unsafe_allow_html=True)
option = st.sidebar.radio("导航菜单", ["🏠 主页", "👮 警员介绍", "📅 支队经历", "🏆 支队荣誉", "✉️ 警民信箱"], label_visibility="collapsed")

# ========== 1. 主页 ==========
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
    
    col1, col2 = st.columns([2,1])
    with col1:
        st.markdown('<div class="section-title">支队概况</div>', unsafe_allow_html=True)
        st.write("津港市公安局长丰刑侦支队是一支具有光荣传统和赫赫战功的英雄警队。支队现有警员120余人，下设重案大队、技术大队、情报研判中心等。在支队长关宏峰的带领下，长丰刑侦连续多年实现命案全破，打出了“命案必破”的金字招牌。")
        st.markdown('**“命案必破，不破不休”** —— 这是长丰刑侦支队刻在骨子里的信条。')
    with col2:
        st.image("https://via.placeholder.com/300x200?text=长丰刑侦", caption="长丰刑侦支队荣誉墙", use_container_width=True)
    
    st.markdown('<div class="section-title">📸 支队风采</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: st.image("支队daquanjing.jpg", caption="支队全景", use_container_width=True)
    with c2: st.image("zhidui1.jpg", caption="支队内部", use_container_width=True)
    with c3: st.image("zhidui2.jpg", caption="支队内部", use_container_width=True)
    st.caption(f"© 长丰刑侦支队政治处 | 更新：{datetime.now().strftime('%Y-%m-%d')}")

# ========== 2. 警员介绍（已更新生日）==========
elif option == "👮 警员介绍":
    st.header("👮‍♂️ 长丰刑侦精英")
    officers = {
        "关宏峰": {"职务": "支队长", "事迹": "全国优秀人民警察，指挥侦破华堂纵火案、3·19大案等逾千起案件。", "荣誉": "一级英模、劳模", "出生": "1977年11月20日", "政治面貌": "中共党员", "照片": "guanhongfeng.jpg"},
        "周巡": {"职务": "副支队长", "事迹": "关宏峰搭档，曾徒手制服持枪歹徒。", "荣誉": "个人一等功", "出生": "1982年7月24日", "政治面貌": "中共党员", "照片": "zhouxun.jpg"},
        "高亚楠": {"职务": "法医主任", "事迹": "首席法医，破获多起悬案。", "荣誉": "全国刑事技术标兵", "出生": "保密", "政治面貌": "群众", "照片": "gaoyanan.jpg"}
    }
    selected = None
    cols = st.columns(3)
    for i, name in enumerate(officers):
        with cols[i]:
            if st.button(name, key=name): selected = name
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
            st.write(f"**事迹**：{info['事迹']}")
            st.write(f"**荣誉**：{info['荣誉']}")
            st.write(f"**出生**：{info['出生']}")
            st.write(f"**政治面貌**：{info['政治面貌']}")
    else:
        st.info("👆 点击上方警员名字")

# ========== 3. 支队经历 ==========
elif option == "📅 支队经历":
    st.header("📅 重大历程")
    events = {
        "2005 获国务院‘特别能战斗刑警队’称号": {"时间": "2005年", "描述": "被国务院授予荣誉称号，荣记集体一等功。"},
        "2008 侦破‘3·19’大案": {"时间": "2008年3月", "描述": "三天内锁定真凶，创破案奇迹。"},
        "2010 市委发出向关宏峰学习决定": {"时间": "2010年", "描述": "号召全市学习关宏峰精神。"},
        "2020 智慧刑侦实验室落成": {"时间": "2020年", "描述": "建成全省首个智慧刑侦实验室。"}
    }
    sel = st.selectbox("选择事件", list(events.keys()))
    ev = events[sel]
    st.subheader(sel)
    st.write(f"**时间**：{ev['时间']}")
    st.write(f"**详情**：{ev['描述']}")
    st.image("https://via.placeholder.com/600x300?text=事件示意", use_container_width=True)

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