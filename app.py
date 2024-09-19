import uuid
from typing import Tuple

import openai

from burr.core import action, State, ApplicationBuilder, when, persistence

# defining actions

@action(reads=[], writes=["prompt", "chat_history"])
def human_input(state: State, prompt: str) -> Tuple[dict, State]:
    """Pulls human input from the outside world and massages it into a standard chat format.
    Note we're adding it into the chat history (with an `append` operation). This 
    is just for convenience of reference -- we could easily just store the chat history
    and access it.
    """
    
    chat_item = {
        "content": prompt,
        "role": "user"
    }
    # return the prompt as the result
    # put the prompt in state and update the chat_history
    return (
        {"prompt": prompt}, 
        state.update(prompt=prompt).append(chat_history=chat_item)
    )

@action(reads=["chat_history"], writes=["response", "chat_history"])
def ai_response(state: State) -> Tuple[dict, State]:
    """Queries OpenAI with the chat. You could easily use langchain, etc... to handle this,
    but we wanted to keep it simple to demonstrate"""
    client = openai.Client()  # replace with your favorite LLM client library
    content = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=state["chat_history"],
    ).choices[0].message.content
    chat_item = {
        "content": content,
        "role": "assistant"
    }
    # return the response as the result
    # put the response in state and update the chat history
    return (
        {"response": content},     
        state.update(response=content).append(chat_history=chat_item)
    )

# creating the app
app = (
    ApplicationBuilder().with_actions(
        human_input=human_input,
        ai_response=ai_response
    ).with_transitions(
        ("human_input", "ai_response"),
        ("ai_response", "human_input")
    ).with_state(chat_history=[])
    .with_entrypoint("human_input")
    .build()
)
app.visualize(output_file_path="digraph_initial", format="png")

# run the app

final_action, result, state = app.run(
    halt_after=["ai_response"], 
    inputs={"prompt" : "Who was Aaron Burr?"}
)
print(state['response'])

# decision making

@action(reads=["prompt"], writes=["safe"])
def safety_check(state: State) -> Tuple[dict, State]:
    safe = "unsafe" not in state["prompt"]
    return {"safe": safe}, state.update(safe=safe)


@action(reads=[], writes=["response", "chat_history"])
def unsafe_response(state: State) -> Tuple[dict, State]:
    content = "I'm sorry, my overlords have forbidden me to respond."
    new_state = (
        state
        .update(response=content)
        .append(
            chat_history={"content": content, "role": "assistant"})
    )
    return {"response": content}, new_state

safe_app = (
    ApplicationBuilder().with_actions(
        human_input=human_input,
        ai_response=ai_response,
        safety_check=safety_check,
        unsafe_response=unsafe_response
    ).with_transitions(
        ("human_input", "safety_check"),
        ("safety_check", "unsafe_response", when(safe=False)),
        ("safety_check", "ai_response", when(safe=True)),
        (["unsafe_response", "ai_response"], "human_input"),
    ).with_state(chat_history=[])
    .with_entrypoint("human_input")
    .build()
)
safe_app.visualize(output_file_path="digraph_safe", include_conditions=True)

action, result, state = safe_app.run(
    halt_after=["ai_response", "unsafe_response"], 
    inputs={"prompt": "Who was Aaron Burr, sir (unsafe)?"}
)
print(state["response"])

#tracking



app_with_tracker = (
    ApplicationBuilder().with_actions(
        human_input=human_input,
        ai_response=ai_response,
        safety_check=safety_check,
        unsafe_response=unsafe_response
    ).with_transitions(
        ("human_input", "safety_check"),
        ("safety_check", "unsafe_response", when(safe=False)),
        ("safety_check", "ai_response", when(safe=True)),
        (["unsafe_response", "ai_response"], "human_input"),
    ).with_state(chat_history=[])
    .with_entrypoint("human_input")
    .with_tracker(
        "local", project="demo_getting_started"
    ).build()
)

app_with_tracker.uid



for prompt in [
    "Who was Aaron Burr, sir?",
    "Who was Aaron Burr, sir (unsafe)?",
    "If you had ml/ai libraries called 'Hamilton' and 'Burr', what would they do?",
    "Who was Aaron Burr, sir?",
    "Who was Aaron Burr, sir (unsafe)?",
    "If you had ml/ai libraries called 'Hamilton' and 'Burr', what would they do?",
]:
    action_we_ran, result, state = app_with_tracker.run(
        halt_after=["ai_response", "unsafe_response"], 
        inputs={"prompt": prompt}
    )


