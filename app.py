import streamlit as st
from engine import get_today_plan, load_state, update_state
from predictor import analyze
import datetime

st.set_page_config(page_title="V6 Clean AI Fitness", layout="wide")

st.title("🔥 AI健身系统 V6 Clean（无报错版）")

state = load_state()
analysis = analyze(state)
plan = get_today_plan()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("当前体重", f"{state['weight']} kg")

with col2:
    st.metric("疲劳值", state["fatigue"])

with col3:
    st.metric("恢复值", state["recovery"])

st.divider()

st.subheader("🏋️ 今日训练（AI推荐）")
st.success(plan["training"])

st.subheader("🍽 今日饮食")
st.info(plan["diet"])

st.subheader("📊 未来预测")
st.write("趋势:", round(analysis["trend"], 2))
st.write("7天后:", round(analysis["week_7"], 2))

st.divider()

if st.button("✅ 完成训练"):
    state = update_state(state, "train")
    st.success("已记录训练")

if st.button("🛌 休息一天"):
    state = update_state(state, "rest")
    st.warning("已进入恢复模式")
