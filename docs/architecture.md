# System Architecture

## Components

### Ticket Input
Receives customer name, issue, priority and ticket ID.

### Knowledge Base
Contains approved support information.

### Copilot
Combines ticket context and approved knowledge to create a draft using Gemini.

### Validator
Checks whether the generated response follows the required JSON structure.

### Human Review
A support agent can Approve, Edit or Reject the generated draft.

## Flow

Ticket
→ Knowledge Base
→ Gemini
→ Draft
→ Validator
→ Human Review
→ Final Response