import asyncio
import os
import time

import streamlit as st

from agent import agent


async def run_agent(prompt, response_container):
    async with agent.run_stream(prompt) as agent_response:
        async for message in agent_response.stream_text():
            # Update the response container with the message
            response_container.markdown(message)
    return agent_response


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
        with st.spinner("Generating Response..."):
            agent_response = asyncio.run(run_agent(prompt, response))
            # Extract the text content from the agent_response
            # Extract only the model's response text from agent_response
            for item in agent_response._all_messages:
                if item.kind == "response":
                    for part in item.parts:
                        if part.part_kind == "text":
                            agent_response.data = part.content
                            response.markdown(part.content)
                            break

            message = {
                "role": "assistant",
                "content": agent_response.data,
            }

        # Add assistant response to chat history
        st.session_state.messages.append(message)
