import streamlit as st

# 🌟 MBTI 성격 정보와 상담 팁 데이터
mbti_info = {
    "INTJ": {
        "title": "🧠 INTJ - 전략가형",
        "description": "논리적이고 분석적인 사고를 가진 전략가입니다. 혼자 있는 것을 즐기며 독립적인 성향이 강합니다.",
        "tips": [
            "🧩 계획적이고 명확한 상담 구조를 제공해 주세요.",
            "🗂️ 사전 정보를 충분히 주고 스스로 생각할 시간을 주세요.",
            "📊 논리적 근거와 자료를 활용한 피드백을 선호합니다."
        ]
    },
    "ENFP": {
        "title": "🌈 ENFP - 활동가형",
        "description": "열정적이고 창의적이며 다른 사람들과의 교류를 즐깁니다. 감정이입 능력이 뛰어납니다.",
        "tips": [
            "🎨 감성적 공감과 따뜻한 피드백이 중요해요.",
            "📢 자유롭게 자신의 이야기를 펼칠 수 있도록 도와주세요.",
            "🧶 너무 틀에 얽매인 방식보다 유연한 접근이 좋아요."
        ]
    },
    "ISFJ": {
        "title": "💖 ISFJ - 수호자형",
        "description": "배려심이 많고 책임감 있는 성격으로, 조용하지만 헌신적인 태도를 보입니다.",
        "tips": [
            "🛡️ 부드럽고 안정감 있는 상담 환경을 만들어 주세요.",
            "📘 관심과 칭찬을 표현하면 더 마음을 열 수 있어요.",
            "🎗️ 실용적인 조언과 구체적인 안내를 좋아합니다."
        ]
    },
    # 기타 MBTI도 여기에 계속 추가 가능
}

# 🎉 Streamlit 앱 시작
st.set_page_config(page_title="학생 MBTI 상담 도우미 💬", layout="centered", page_icon="🎓")

st.title("💬 학생 MBTI 상담 도우미")
st.markdown("학생의 MBTI를 선택하면, 해당 성격의 특징과 효과적인 상담 팁을 알려드릴게요! 😊")

# 📍 MBTI 선택
mbti = st.selectbox("🔍 학생의 MBTI를 선택해주세요:", list(mbti_info.keys()))

if mbti:
    st.markdown("---")
    st.subheader(mbti_info[mbti]["title"])
    st.markdown(f"**📌 성격 특징:**\n\n{mbti_info[mbti]['description']}")
    
    st.markdown("**🛠️ 상담 팁:**")
    for tip in mbti_info[mbti]["tips"]:
        st.markdown(f"- {tip}")

    st.markdown("---")
    st.success("📚 학생의 성향을 이해하고 공감하는 상담이 최고의 교육입니다!")

# 🎨 하단 메시지
st.markdown("""
<div style='text-align: center; font-size: 16px; margin-top: 30px;'>
    🙌 상담은 학생과의 믿음을 쌓는 과정입니다. <br>
    <b>진심 어린 관심</b>과 <b>MBTI 이해</b>로 보다 깊은 대화를 시작해 보세요!
</div>
""", unsafe_allow_html=True)
