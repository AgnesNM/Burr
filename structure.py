rr_
burr_
├── burr
│   ├── cli
│   │   ├── demo_data.py
│   │   ├── __init__.py
│   │   └── __main__.py
│   ├── common
│   │   ├── __init__.py
│   │   └── types.py
│   ├── core
│   │   ├── action.py
│   │   ├── application.py
│   │   ├── graph.py
│   │   ├── implementations.py
│   │   ├── __init__.py
│   │   ├── persistence.py
│   │   ├── serde.py
│   │   ├── state.py
│   │   ├── typing.py
│   │   └── validation.py
│   ├── examples -> ../examples
│   ├── __init__.py
│   ├── integrations
│   │   ├── base.py
│   │   ├── hamilton.py
│   │   ├── __init__.py
│   │   ├── opentelemetry.py
│   │   ├── persisters
│   │   │   ├── b_mongodb.py
│   │   │   ├── b_redis.py
│   │   │   ├── __init__.py
│   │   │   └── postgresql.py
│   │   ├── pydantic.py
│   │   ├── serde
│   │   │   ├── __init__.py
│   │   │   ├── langchain.py
│   │   │   ├── pandas.py
│   │   │   ├── pickle.py
│   │   │   └── pydantic.py
│   │   └── streamlit.py
│   ├── lifecycle
│   │   ├── base.py
│   │   ├── default.py
│   │   ├── __init__.py
│   │   └── internal.py
│   ├── log_setup.py
│   ├── system.py
│   ├── telemetry.py
│   ├── testing
│   │   └── __init__.py
│   ├── tracking
│   │   ├── base.py
│   │   ├── client.py
│   │   ├── common
│   │   │   ├── __init__.py
│   │   │   └── models.py
│   │   ├── __init__.py
│   │   ├── s3client.py
│   │   ├── server
│   │   │   ├── backend.py
│   │   │   ├── demo_data
│   │   │   │   ├── demo_chatbot
│   │   │   │   │   ├── chat-1-giraffe
│   │   │   │   │   │   ├── graph.json
│   │   │   │   │   │   ├── log.jsonl
│   │   │   │   │   │   └── metadata.json
│   │   │   │   │   ├── chat-2-geography
│   │   │   │   │   │   ├── graph.json
│   │   │   │   │   │   ├── log.jsonl
│   │   │   │   │   │   └── metadata.json
│   │   │   │   │   ├── chat-3-physics
│   │   │   │   │   │   ├── graph.json
│   │   │   │   │   │   ├── log.jsonl
│   │   │   │   │   │   └── metadata.json
│   │   │   │   │   ├── chat-4-philosophy
│   │   │   │   │   │   ├── graph.json
│   │   │   │   │   │   ├── log.jsonl
│   │   │   │   │   │   └── metadata.json
│   │   │   │   │   ├── chat-5-jokes
│   │   │   │   │   │   ├── graph.json
│   │   │   │   │   │   ├── log.jsonl
│   │   │   │   │   │   └── metadata.json
│   │   │   │   │   └── chat-6-demonstrate-errors
│   │   │   │   │       ├── graph.json
│   │   │   │   │       ├── log.jsonl
│   │   │   │   │       └── metadata.json
│   │   │   │   ├── demo_chatbot_with_traces
│   │   │   │   │   ├── chat-1-giraffe
│   │   │   │   │   │   ├── graph.json
│   │   │   │   │   │   ├── log.jsonl
│   │   │   │   │   │   └── metadata.json
│   │   │   │   │   ├── chat-2-geography
│   │   │   │   │   │   ├── graph.json
│   │   │   │   │   │   ├── log.jsonl
│   │   │   │   │   │   └── metadata.json
│   │   │   │   │   ├── chat-3-physics
│   │   │   │   │   │   ├── graph.json
│   │   │   │   │   │   ├── log.jsonl
│   │   │   │   │   │   └── metadata.json
│   │   │   │   │   ├── chat-4-philosophy
│   │   │   │   │   │   ├── graph.json
│   │   │   │   │   │   ├── log.jsonl
│   │   │   │   │   │   └── metadata.json
│   │   │   │   │   ├── chat-5-jokes
│   │   │   │   │   │   ├── graph.json
│   │   │   │   │   │   ├── log.jsonl
│   │   │   │   │   │   └── metadata.json
│   │   │   │   │   └── chat-6-demonstrate-errors
│   │   │   │   │       ├── graph.json
│   │   │   │   │       ├── log.jsonl
│   │   │   │   │       └── metadata.json
│   │   │   │   ├── demo_conversational-rag
│   │   │   │   │   ├── rag-1-food
│   │   │   │   │   │   ├── graph.json
│   │   │   │   │   │   ├── log.jsonl
│   │   │   │   │   │   └── metadata.json
│   │   │   │   │   ├── rag-2-work-history
│   │   │   │   │   │   ├── graph.json
│   │   │   │   │   │   ├── log.jsonl
│   │   │   │   │   │   └── metadata.json
│   │   │   │   │   ├── rag-3-activities
│   │   │   │   │   │   ├── graph.json
│   │   │   │   │   │   ├── log.jsonl
│   │   │   │   │   │   └── metadata.json
│   │   │   │   │   └── rag-4-everything
│   │   │   │   │       ├── graph.json
│   │   │   │   │       ├── log.jsonl
│   │   │   │   │       └── metadata.json
│   │   │   │   └── demo_counter
│   │   │   │       ├── count-to-1
│   │   │   │       │   ├── graph.json
│   │   │   │       │   ├── log.jsonl
│   │   │   │       │   └── metadata.json
│   │   │   │       ├── count-to-10
│   │   │   │       │   ├── graph.json
│   │   │   │       │   ├── log.jsonl
│   │   │   │       │   └── metadata.json
│   │   │   │       ├── count-to-100
│   │   │   │       │   ├── graph.json
│   │   │   │       │   ├── log.jsonl
│   │   │   │       │   └── metadata.json
│   │   │   │       ├── count-to-42
│   │   │   │       │   ├── graph.json
│   │   │   │       │   ├── log.jsonl
│   │   │   │       │   └── metadata.json
│   │   │   │       └── count-to-50
│   │   │   │           ├── graph.json
│   │   │   │           ├── log.jsonl
│   │   │   │           └── metadata.json
│   │   │   ├── requirements-s3.txt
│   │   │   ├── run.py
│   │   │   ├── run.sh
│   │   │   ├── s3
│   │   │   │   ├── architecture.png
│   │   │   │   ├── backend.py
│   │   │   │   ├── deployment
│   │   │   │   │   ├── Dockerfile
│   │   │   │   │   ├── nginx.conf
│   │   │   │   │   └── terraform
│   │   │   │   │       ├── alb.tf
│   │   │   │   │       ├── auto_scaling.tf
│   │   │   │   │       ├── ecs.tf
│   │   │   │   │       ├── iam.tf
│   │   │   │   │       ├── logs.tf
│   │   │   │   │       ├── network.tf
│   │   │   │   │       ├── outputs.tf
│   │   │   │   │       ├── provider.tf
│   │   │   │   │       ├── security.tf
│   │   │   │   │       ├── templates
│   │   │   │   │       │   └── ecs
│   │   │   │   │       │       └── burr_app.json.tpl
│   │   │   │   │       └── variable.tf
│   │   │   │   ├── initialize_db.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── migrations
│   │   │   │   │   └── models
│   │   │   │   │       └── 0_20240730151503_init.py
│   │   │   │   ├── models.py
│   │   │   │   ├── pyproject.toml
│   │   │   │   ├── README.md
│   │   │   │   ├── settings.py
│   │   │   │   └── utils.py
│   │   │   └── schema.py
│   │   └── utils.py
│   ├── version.py
│   └── visibility
│       ├── __init__.py
│       └── tracing.py
├── chatbot.gif
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.rst
├── docs
│   ├── concepts
│   │   ├── actions.rst
│   │   ├── additional-visibility.rst
│   │   ├── hooks.rst
│   │   ├── index.rst
│   │   ├── overview.rst
│   │   ├── planned-capabilities.rst
│   │   ├── recursion.rst
│   │   ├── serde.rst
│   │   ├── state-machine.rst
│   │   ├── state-persistence.rst
│   │   ├── state.rst
│   │   ├── state-typing.rst
│   │   ├── streaming-actions.rst
│   │   ├── tracking.rst
│   │   └── transitions.rst
│   ├── conf.py
│   ├── contributing
│   │   ├── architecture.rst
│   │   ├── contributing.rst
│   │   ├── index.rst
│   │   ├── iterating.rst
│   │   └── setup.rst
│   ├── examples
│   │   ├── agents
│   │   │   ├── _agent_patterns
│   │   │   │   ├── agent_supervisor.png
│   │   │   │   ├── hierarchical_agent_teams.png
│   │   │   │   ├── multi_agent_collaboration.png
│   │   │   │   └── multi_modal_agent.png
│   │   │   ├── agent-patterns.md
│   │   │   ├── divide-and-conquer.md
│   │   │   ├── _divide-and-conquer.png
│   │   │   └── index.rst
│   │   ├── chatbots
│   │   │   ├── basic-chatbot.ipynb
│   │   │   ├── gpt-like-chatbot.ipynb
│   │   │   ├── index.rst
│   │   │   └── rag-chatbot-hamilton.ipynb
│   │   ├── data-science
│   │   │   ├── index.rst
│   │   │   ├── ml_training.md
│   │   │   ├── _ml_training.png
│   │   │   ├── simulation.md
│   │   │   └── _simulation.png
│   │   ├── deployment
│   │   │   ├── aws.md
│   │   │   ├── index.rst
│   │   │   ├── web-server.md
│   │   │   └── _web-server.png
│   │   ├── guardrails
│   │   │   ├── _creating_tests.png
│   │   │   ├── creating_tests.rst
│   │   │   └── index.rst
│   │   ├── index.rst
│   │   └── simple
│   │       ├── choose-your-own-adventure.ipynb
│   │       ├── counter.ipynb
│   │       ├── cowsay.ipynb
│   │       └── index.rst
│   ├── getting_started
│   │   ├── index.rst
│   │   ├── install.rst
│   │   ├── simple-example.rst
│   │   ├── up-next.rst
│   │   └── why-burr.rst
│   ├── index.rst
│   ├── main.rst
│   ├── make.bat
│   ├── Makefile
│   ├── README-internal.md
│   ├── reference
│   │   ├── actions.rst
│   │   ├── application.rst
│   │   ├── conditions.rst
│   │   ├── index.rst
│   │   ├── integrations
│   │   │   ├── hamilton.rst
│   │   │   ├── index.rst
│   │   │   ├── langchain.rst
│   │   │   ├── opentelemetry.rst
│   │   │   ├── streamlit.rst
│   │   │   └── traceloop.rst
│   │   ├── lifecycle.rst
│   │   ├── persister.rst
│   │   ├── serde.rst
│   │   ├── state.rst
│   │   ├── telemetry.rst
│   │   ├── tracking.rst
│   │   ├── typing.rst
│   │   └── visibility.rst
│   ├── robots.txt
│   └── _static
│       ├── chatbot.png
│       ├── demo_graph.png
│       ├── meme.png
│       └── recursive_steps.png
├── examples
│   ├── adaptive-crag
│   │   ├── application.py
│   │   ├── burr_docs
│   │   │   ├── actions.txt
│   │   │   ├── applications.txt
│   │   │   ├── cheat_sheet.txt
│   │   │   ├── state.txt
│   │   │   └── transitions.txt
│   │   ├── __init__.py
│   │   ├── notebook.ipynb
│   │   ├── README.md
│   │   ├── requirements.txt
│   │   └── statemachine.png
│   ├── conversational-rag
│   │   ├── graph_db_example
│   │   │   ├── application.py
│   │   │   ├── data
│   │   │   │   ├── raw_fighter_details.csv
│   │   │   │   └── raw_total_fight_data.csv
│   │   │   ├── graph_schema.py
│   │   │   ├── hamilton_ingest.py
│   │   │   ├── ingest_fighters.png
│   │   │   ├── ingest_fighters.py
│   │   │   ├── ingest_fights.png
│   │   │   ├── ingest_fights.py
│   │   │   ├── ingest_notebook.ipynb
│   │   │   ├── notebook.ipynb
│   │   │   ├── README.md
│   │   │   ├── requirements.txt
│   │   │   ├── statemachine.png
│   │   │   ├── UFC_Graph.png
│   │   │   └── utils.py
│   │   ├── __init__.py
│   │   ├── README.md
│   │   └── simple_example
│   │       ├── application.py
│   │       ├── __init__.py
│   │       ├── notebook.ipynb
│   │       ├── README.md
│   │       ├── requirements.txt
│   │       └── statemachine.png
│   ├── custom-serde
│   │   ├── application.py
│   │   ├── __init__.py
│   │   ├── notebook.ipynb
│   │   ├── README.md
│   │   ├── requirements.txt
│   │   ├── run.py
│   │   └── statemachine.png
│   ├── deployment
│   │   └── aws
│   │       └── lambda
│   │           ├── app
│   │           │   ├── counter_app.py
│   │           │   ├── __init__.py
│   │           │   └── lambda_handler.py
│   │           ├── Dockerfile
│   │           ├── README.md
│   │           └── requirements.txt
│   ├── email-assistant
│   │   ├── application.py
│   │   ├── __init__.py
│   │   ├── notebook.ipynb
│   │   ├── README.md
│   │   ├── requirements.txt
│   │   ├── server.py
│   │   └── statemachine.png
│   ├── hello-world-counter
│   │   ├── application.py
│   │   ├── __init__.py
│   │   ├── notebook.ipynb
│   │   ├── README.md
│   │   ├── requirements.txt
│   │   ├── statemachine.png
│   │   └── streamlit_app.py
│   ├── image-telephone
│   │   ├── application.py
│   │   ├── __init__.py
│   │   ├── notebook.ipynb
│   │   ├── README.md
│   │   ├── requirements.txt
│   │   └── statemachine.png
│   ├── __init__.py
│   ├── instructor-gemini-flash
│   │   ├── application.py
│   │   ├── __init__.py
│   │   ├── notebook.ipynb
│   │   ├── README.md
│   │   ├── requirements.txt
│   │   └── statemachine.png
│   ├── integrations
│   │   └── hamilton
│   │       ├── image-telephone
│   │       │   ├── application.py
│   │       │   ├── README.md
│   │       │   └── requirements.txt
│   │       ├── README.md
│   │       └── statemachine.png
│   ├── llm-adventure-game
│   │   ├── application.py
│   │   ├── __init__.py
│   │   ├── notebook.ipynb
│   │   ├── README.md
│   │   ├── requirements.txt
│   │   └── statemachine.png
│   ├── ml-training
│   │   ├── application.py
│   │   ├── README.md
│   │   └── statemachine.png
│   ├── multi-agent-collaboration
│   │   ├── hamilton
│   │   │   ├── alternative_implementation.py
│   │   │   ├── application.py
│   │   │   ├── func_agent.py
│   │   │   ├── __init__.py
│   │   │   ├── notebook.ipynb
│   │   │   ├── README.md
│   │   │   ├── requirements.txt
│   │   │   └── statemachine.png
│   │   ├── __init__.py
│   │   ├── lcel
│   │   │   ├── application.py
│   │   │   ├── __init__.py
│   │   │   ├── notebook.ipynb
│   │   │   ├── README.md
│   │   │   ├── requirements.txt
│   │   │   └── statemachine.png
│   │   ├── README.md
│   │   └── requirements.txt
│   ├── multi-modal-chatbot
│   │   ├── application.py
│   │   ├── burr_demo.ipynb
│   │   ├── __init__.py
│   │   ├── notebook.ipynb
│   │   ├── README.md
│   │   ├── requirements.txt
│   │   ├── server.py
│   │   ├── simple_streamlit_app.py
│   │   ├── statemachine.png
│   │   └── streamlit_app.py
│   ├── openai-compatible-agent
│   │   ├── application.py
│   │   ├── __init__.py
│   │   ├── README.md
│   │   ├── requirements.txt
│   │   ├── server.py
│   │   └── statemachine.png
│   ├── opentelemetry
│   │   ├── application.py
│   │   ├── __init__.py
│   │   ├── notebook.ipynb
│   │   ├── README.md
│   │   └── statemachine.png
│   ├── other-examples
│   │   ├── cowsay
│   │   │   ├── application.py
│   │   │   ├── digraph
│   │   │   ├── digraph.png
│   │   │   ├── notebook.ipynb
│   │   │   ├── README.md
│   │   │   ├── requirements.txt
│   │   │   └── streamlit_app.py
│   │   └── hamilton-multi-modal
│   │       ├── application.py
│   │       ├── dag.py
│   │       └── __init__.py
│   ├── rag-lancedb-ingestion
│   │   ├── application.py
│   │   ├── burr-ui.gif
│   │   ├── ingestion.py
│   │   ├── __init__.py
│   │   ├── notebook.ipynb
│   │   ├── README.md
│   │   ├── requirements.txt
│   │   ├── statemachine.png
│   │   └── utils.py
│   ├── README.md
│   ├── recursive
│   │   ├── application.py
│   │   ├── __init__.py
│   │   ├── notebook.ipynb
│   │   ├── README.md
│   │   ├── requirements.txt
│   │   ├── statemachine.png
│   │   └── statemachine_sub.png
│   ├── simple-chatbot-intro
│   │   ├── application.py
│   │   ├── __init__.py
│   │   ├── notebook.ipynb
│   │   ├── README.md
│   │   ├── requirements.txt
│   │   ├── statemachine_initial.png
│   │   ├── statemachine.png
│   │   └── statemachine_safe.png
│   ├── simulation
│   │   ├── application.py
│   │   ├── README.md
│   │   └── statemachine.png
│   ├── streaming-fastapi
│   │   ├── application.py
│   │   ├── __init__.py
│   │   ├── notebook.ipynb
│   │   ├── README.md
│   │   ├── server.py
│   │   ├── statemachine.png
│   │   └── streamlit_app.py
│   ├── streaming-overview
│   │   ├── application.py
│   │   ├── async_application.py
│   │   ├── __init__.py
│   │   ├── notebook.ipynb
│   │   ├── README.md
│   │   ├── requirements.txt
│   │   ├── statemachine.png
│   │   └── streamlit_app.py
│   ├── templates
│   │   ├── agent_supervisor.png
│   │   ├── agent_supervisor.py
│   │   ├── hierarchical_agent_teams.png
│   │   ├── hierarchical_agent_teams.py
│   │   ├── multi_agent_collaboration.png
│   │   ├── multi_agent_collaboration.py
│   │   ├── multi_modal_agent.png
│   │   ├── multi_modal_agent.py
│   │   └── README.md
│   ├── test-case-creation
│   │   ├── application.py
│   │   ├── __init__.py
│   │   ├── notebook.ipynb
│   │   ├── prompt_for_more.json
│   │   ├── README.md
│   │   ├── requirements.txt
│   │   ├── statemachine.png
│   │   └── test_application.py
│   ├── tracing-and-spans
│   │   ├── application.py
│   │   ├── burr_otel_demo.ipynb
│   │   ├── __init__.py
│   │   ├── notebook.ipynb
│   │   ├── README.md
│   │   ├── requirements.txt
│   │   ├── statemachine.png
│   │   └── tracing_screencap.png
│   ├── typed-state
│   │   ├── application.py
│   │   ├── curls.sh
│   │   ├── __init__.py
│   │   ├── notebook.ipynb
│   │   ├── README.md
│   │   ├── server.py
│   │   └── statemachine.png
│   ├── validate_examples.py
│   ├── web-server
│   │   └── README.md
│   └── youtube-to-social-media-post
│       ├── application.py
│       ├── __init__.py
│       ├── notebook.ipynb
│       ├── README.md
│       ├── server.py
│       └── statemachine.png
├── __init__.py
├── LICENSE
├── MANIFEST.in
├── pyproject.toml
├── README.md
├── setup.cfg
├── telemetry
│   └── ui
│       ├── package.json
│       ├── package-lock.json
│       ├── public
│       │   ├── favicon.ico
│       │   ├── index.html
│       │   ├── logo.png
│       │   ├── manifest.json
│       │   └── robots.txt
│       ├── README.md
│       ├── scripts
│       │   └── client-gen.sh
│       ├── src
│       │   ├── api
│       │   │   ├── core
│       │   │   │   ├── ApiError.ts
│       │   │   │   ├── ApiRequestOptions.ts
│       │   │   │   ├── ApiResult.ts
│       │   │   │   ├── CancelablePromise.ts
│       │   │   │   ├── OpenAPI.ts
│       │   │   │   └── request.ts
│       │   │   ├── index.ts
│       │   │   ├── models
│       │   │   │   ├── ActionModel.ts
│       │   │   │   ├── ApplicationLogs.ts
│       │   │   │   ├── ApplicationModel.ts
│       │   │   │   ├── ApplicationPage.ts
│       │   │   │   ├── ApplicationSummary.ts
│       │   │   │   ├── AttributeModel.ts
│       │   │   │   ├── BackendSpec.ts
│       │   │   │   ├── BeginEntryModel.ts
│       │   │   │   ├── BeginSpanModel.ts
│       │   │   │   ├── ChatItem.ts
│       │   │   │   ├── ChildApplicationModel.ts
│       │   │   │   ├── DraftInit.ts
│       │   │   │   ├── EmailAssistantState.ts
│       │   │   │   ├── EndEntryModel.ts
│       │   │   │   ├── EndSpanModel.ts
│       │   │   │   ├── EndStreamModel.ts
│       │   │   │   ├── Feedback.ts
│       │   │   │   ├── FirstItemStreamModel.ts
│       │   │   │   ├── HTTPValidationError.ts
│       │   │   │   ├── IndexingJob.ts
│       │   │   │   ├── InitializeStreamModel.ts
│       │   │   │   ├── PointerModel.ts
│       │   │   │   ├── Project.ts
│       │   │   │   ├── PromptInput.ts
│       │   │   │   ├── QuestionAnswers.ts
│       │   │   │   ├── Span.ts
│       │   │   │   ├── Step.ts
│       │   │   │   ├── TransitionModel.ts
│       │   │   │   └── ValidationError.ts
│       │   │   └── services
│       │   │       └── DefaultService.ts
│       │   ├── App.css
│       │   ├── App.test.tsx
│       │   ├── App.tsx
│       │   ├── components
│       │   │   ├── common
│       │   │   │   ├── button.tsx
│       │   │   │   ├── chip.tsx
│       │   │   │   ├── dates.tsx
│       │   │   │   ├── fieldset.tsx
│       │   │   │   ├── href.tsx
│       │   │   │   ├── input.tsx
│       │   │   │   ├── layout.tsx
│       │   │   │   ├── link.tsx
│       │   │   │   ├── loading.tsx
│       │   │   │   ├── pagination.tsx
│       │   │   │   ├── switch.tsx
│       │   │   │   ├── table.tsx
│       │   │   │   ├── tabs.tsx
│       │   │   │   ├── textarea.tsx
│       │   │   │   ├── text.tsx
│       │   │   │   └── tooltip.tsx
│       │   │   ├── nav
│       │   │   │   ├── appcontainer.tsx
│       │   │   │   └── breadcrumb.tsx
│       │   │   └── routes
│       │   │       ├── AdminView.tsx
│       │   │       ├── app
│       │   │       │   ├── ActionView.tsx
│       │   │       │   ├── AppView.tsx
│       │   │       │   ├── DataView.tsx
│       │   │       │   ├── GraphView.tsx
│       │   │       │   ├── InsightsView.tsx
│       │   │       │   ├── ReproduceView.tsx
│       │   │       │   ├── StateMachine.tsx
│       │   │       │   └── StepList.tsx
│       │   │       ├── AppList.tsx
│       │   │       └── ProjectList.tsx
│       │   ├── examples
│       │   │   ├── Chatbot.tsx
│       │   │   ├── Common.tsx
│       │   │   ├── Counter.tsx
│       │   │   ├── EmailAssistant.tsx
│       │   │   ├── MiniTelemetry.tsx
│       │   │   └── StreamingChatbot.tsx
│       │   ├── index.css
│       │   ├── index.tsx
│       │   ├── react-app-env.d.ts
│       │   ├── reportWebVitals.ts
│       │   ├── setupTests.ts
│       │   ├── utils
│       │   │   └── tailwind.ts
│       │   └── utils.tsx
│       ├── tailwind.config.js
│       └── tsconfig.json
└── tests
    ├── conftest.py
    ├── core
    │   ├── test_action.py
    │   ├── test_application.py
    │   ├── test_graph.py
    │   ├── test_graphviz_display.py
    │   ├── test_implementations.py
    │   ├── test_persistence.py
    │   ├── test_serde.py
    │   ├── test_state.py
    │   └── test_validation.py
    ├── integrations
    │   ├── persisters
    │   │   ├── test_b_mongodb.py
    │   │   ├── test_b_redis.py
    │   │   └── test_postgresql.py
    │   ├── serde
    │   │   ├── test_langchain.py
    │   │   ├── test_pandas.py
    │   │   ├── test_pickle.py
    │   │   └── test_pydantic.py
    │   ├── test_burr_hamilton.py
    │   ├── test_burr_opentelemetry.py
    │   ├── test_burr_pydantic.py
    │   └── test_opentelemetry.py
    ├── integration_tests
    │   └── test_app.py
    ├── pytest.ini
    ├── test_end_to_end.py
    ├── tracking
    │   ├── test_common_models.py
    │   └── test_local_tracking_client.py
    └── visibility
        └── test_tracing.py
