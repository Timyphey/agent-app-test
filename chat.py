import os
import time

import streamlit as st

from agent import agent

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Let's start chatting!"}
    ]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    # Use cyan avatar for assistant messages
    if message["role"] == "assistant":
        with st.chat_message(message["role"], avatar="🤖"):
            badge = st.empty()
            badge.markdown(":gray-badge[Agent]")
            st.markdown(message["content"])
    else:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Ich hab da mal ne Frage..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant", avatar="🤖"):
        badge = st.empty()
        badge.markdown(":gray-badge[Agent]")
        response = st.empty()
        with st.spinner("Thinking..."):
            agent_response = agent.run_sync(prompt)
            print(agent_response)
            response.markdown(agent_response.data)

            message = {
                "role": "assistant",
                "content": agent_response.data,
            }

        # Add assistant response to chat history
        st.session_state.messages.append(message)
