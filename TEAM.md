# EDI5 EV Battery Intelligence — Team Ownership

## Team Structure

| Member | Ownership | Primary Deliverable |
|---|---|---|
| Member 1 | Data + ML | Cleaned battery dataset, features, trained cycle-life model, evaluation metrics |
| Member 2 | Frontend | React + Plotly Battery Intelligence Dashboard |
| Member 3 | GenAI / Agent | AI Battery Analyst |
| Member 4 | Backend + Digital Twin + Database + Integration | FastAPI, Supabase, digital-twin state, API integration |

---

## Member 1 — Data + ML

### Owns
- Severson dataset extraction
- Data preprocessing
- Feature engineering
- ML model
- Model evaluation
- Prediction outputs

### Hands off
- Clean/processed battery data
- Model/prediction outputs
- Required feature definitions
- Evaluation metrics

### Does not own
- FastAPI implementation
- Supabase
- React frontend
- Agent orchestration

---

## Member 2 — Frontend

### Owns
- React application
- Dashboard UI
- Plotly visualizations
- Battery selection and display
- Frontend API integration

### Hands off
- Completed dashboard
- Frontend components
- API integration

### Does not own
- ML calculations
- Database schema
- LLM/agent logic

---

## Member 3 — GenAI / Agent

### Owns
- AI Battery Analyst
- LangGraph/agent workflow
- Tool definitions
- LLM interaction
- Grounded battery explanations

### Hands off
- Working agent with mock data
- Agent tools
- Real backend integration if available

### Does not own
- ML calculations
- Battery database
- React dashboard

---

## Member 4 — Backend + Digital Twin + Database + Integration

### Owns
- API contract
- FastAPI backend
- Supabase database
- Digital-twin state representation
- Backend integration
- Integration between ML, database, frontend and agent

### Hands off
- API endpoints
- Database schema
- Digital-twin schema
- Integrated working prototype

### Does not own
- ML model implementation
- React UI
- LLM reasoning/model selection
