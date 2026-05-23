import streamlit as st  # type: ignore
import time

from oss_assistant import generate_oss_response
from frontier_assistant import generate_frontier_response
from guardrails import is_safe
from logger import log_interaction


# =========================
# PAGE CONFIG
# =========================

st.set_page_config(page_title="AI Assistant Comparison")

st.title("🤖 AI Assistant Comparison")

st.markdown(
    "Compare Open Source vs Frontier AI Assistants"
)


# =========================
# SESSION STATE INIT
# =========================

if "oss_messages" not in st.session_state:
    st.session_state.oss_messages = []

if "frontier_messages" not in st.session_state:
    st.session_state.frontier_messages = []

if "oss_latency" not in st.session_state:
    st.session_state.oss_latency = []

if "frontier_latency" not in st.session_state:
    st.session_state.frontier_latency = []


# =========================
# SIDEBAR
# =========================

model_choice = st.sidebar.selectbox(
    "Choose Assistant",
    ["OSS Assistant", "Frontier Assistant"]
)

st.sidebar.markdown("---")

if model_choice == "OSS Assistant":
    st.warning("You are using the Open Source Assistant")

else:
    st.success("You are using the Frontier Assistant")


# =========================
# CURRENT CHAT SELECTION
# =========================

if model_choice == "OSS Assistant":
    current_messages = st.session_state.oss_messages

else:
    current_messages = st.session_state.frontier_messages


# =========================
# CLEAR CHAT BUTTON
# =========================

if st.sidebar.button("Clear Current Chat"):

    if model_choice == "OSS Assistant":

        st.session_state.oss_messages = []
        current_messages = st.session_state.oss_messages

    else:

        st.session_state.frontier_messages = []
        current_messages = st.session_state.frontier_messages

    st.rerun()


# =========================
# ANALYTICS
# =========================

st.sidebar.markdown("---")
st.sidebar.subheader("Analytics")

st.sidebar.write(
    f"OSS Chats: {len(st.session_state.oss_messages)}"
)

st.sidebar.write(
    f"Frontier Chats: {len(st.session_state.frontier_messages)}"
)

if st.session_state.oss_latency:

    avg_oss = round(
        sum(st.session_state.oss_latency)
        / len(st.session_state.oss_latency),
        2
    )

    st.sidebar.write(
        f"OSS Avg Latency: {avg_oss}s"
    )

if st.session_state.frontier_latency:

    avg_frontier = round(
        sum(st.session_state.frontier_latency)
        / len(st.session_state.frontier_latency),
        2
    )

    st.sidebar.write(
        f"Frontier Avg Latency: {avg_frontier}s"
    )


# =========================
# DISPLAY CHAT HISTORY
# =========================

for message in current_messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# =========================
# USER INPUT
# =========================

prompt = st.chat_input("Ask something...")


if prompt:

    # SAFETY CHECK
    if not is_safe(prompt):

        st.warning("Unsafe prompt detected.")
        st.stop()

    # STORE USER MESSAGE
    current_messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    # SHORT-TERM MEMORY
    conversation_history = current_messages[-6:]

    # START TIMER
    start_time = time.time()

    # MODEL RESPONSE
    if model_choice == "OSS Assistant":

        response = generate_oss_response(
            conversation_history
        )

    else:

        response = generate_frontier_response(
            conversation_history
        )

    # END TIMER
    end_time = time.time()

    latency = round(
        end_time - start_time,
        2
    )

    # STORE LATENCY
    if model_choice == "OSS Assistant":

        st.session_state.oss_latency.append(
            latency
        )

    else:

        st.session_state.frontier_latency.append(
            latency
        )

    # LOG INTERACTION
    log_interaction(
        prompt,
        response,
        model_choice
    )

    # DISPLAY RESPONSE
    with st.chat_message("assistant"):

        st.markdown(response)

        st.caption(
            f"Response generated in {latency} seconds"
        )

    # STORE ASSISTANT MESSAGE
    current_messages.append({
        "role": "assistant",
        "content": response
    })