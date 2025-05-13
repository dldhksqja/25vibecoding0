import streamlit as st

# CSS 스타일 정의
def local_css():
    st.markdown("""
        <style>
        html, body, [class*="css"]  {
            background: linear-gradient(135deg, #fceabb 0%, #f8b500 100%);
            font-family: 'Segoe UI', sans-serif;
        }
        .main {
            background-color: rgba(255,255,255,0.9);
            border-radius: 12px;
            padding: 2rem;
            margin-top: 1rem;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }
        h1, h2, h3 {
            color: #2b2b2b;
        }
        .highlight {
            background: #fffbcc;
            padding: 0.3em 0.6em;
            border-radius: 8px;
            font-weight: bold;
        }
        .chat-bubble {
            background: #ffffff;
            padding: 0.8rem;
            border-radius: 15px;
            margin: 0.3rem 0;
            box-shadow: 2px 2px 6px rgba(0,0,0,0.1);
        }
        .teacher { border-left: 5px solid #2196f3; }
        .student { border-left: 5px solid #f44336; }
        </style>
    """, unsafe_allow_html=True)

local_css()

# MBTI 데이터 정의
mbti_info = {
    "INTJ": {
        "emoji": "🧠",
        "name": "전략가형",
        "description": "논리적이고 독립적인 사고를 가진 깊은 사색가입니다.",
        "tips": [
            "🧩 구조화된 질문과 계획 제시",
            "🗂️ 정보 기반 피드백 제공",
            "🔍 내면적 분석의 여지 주기"
        ],
        "chat": [
            ("선생님", "최근 진로에 대해 어떤 생각을 하고 있어요?"),
            ("학생", "아직 확실하진 않지만, 혼자 정보는 좀 찾아봤어요."),
            ("선생님", "좋아요! 그 자료들을 함께 정리해 보면서 더 명확한 방향을 잡아볼까요?")
        ]
    },
    "ENFP": {
        "emoji": "🌈",
        "name": "활동가형",
        "description": "열정 넘치고 사람을 좋아하는 창의적인 이상주의자입니다.",
        "tips": [
            "🎨 감성적 공감 표현",
            "📢 개방적인 대화 유도",
            "🧶 유연한 상담 접근"
        ],
        "chat": [
            ("선생님", "요즘 학교생활 어때요?"),
            ("학생", "재밌는 걸 찾고 싶은데 어떻게 시작해야 할지 모르겠어요."),
            ("선생님", "그런 마음 너무 좋아요! 혹시 흥미 생긴 활동이 있다면 얘기해줄래요?")
        ]
    },
    "ISFJ": {
        "emoji": "💖",
        "name": "수호자형",
        "description": "조용하지만 따뜻한 책임감 있는 도우미 유형입니다.",
        "tips": [
            "🛡️ 안정감 있는 환경 조성",
            "📘 따뜻한 피드백 제공",
            "🎗️ 구체적이고 실용적인 조언"
        ],
        "chat": [
            ("선생님", "최근에 힘든 일 있었나요?"),
            ("학생", "계속 실수해서 자존감이 떨어지는 것 같아요."),
            ("선생님", "실수는 누구나 해요. 당신의 성실함이 훨씬 더 중요하단 걸 기억해요. 😊")
        ]
    }
}

# 제목 및 설명
st.markdown("<div class='main'>", unsafe_allow_html=True)
st.title("🎓 학생 MBTI 상담 도우미")
st.markdown("학생의 성격을 이해하고, 그에 맞춘 상담 방식과 대화를 알아보세요! 💬")

# MBTI 선택
mbti = st.selectbox("🔍 학생의 MBTI 유형을 선택해주세요:", list(mbti_info.keys()))

if mbti:
    data = mbti_info[mbti]
    st.markdown("---")
    st.markdown(f"### {data['emoji']} {mbti} - {data['name']}")

    st.markdown(f"**📌 성격 요약:** <span class='highlight'>{data['description']}</span>", unsafe_allow_html=True)

    st.markdown("### 🛠️ 상담 팁")
    for tip in data['tips']:
        st.markdown(f"- {tip}")

    st.markdown("### 💬 상담 대화 예시")
    for role, message in data["chat"]:
        role_class = "teacher" if role == "선생님" else "student"
        st.markdown(f"<div class='chat-bubble {role_class}'><b>{role}:</b> {message}</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.success("📘 학생의 성향을 존중하고, 따뜻하게 공감하는 것이 좋은 상담의 시작입니다!")

st.markdown("</div>", unsafe_allow_html=True)
