# 🔁 The Ralphing Skill (R.A.L.P.H. Pattern)

"Ralphing" (Retry And Loop Persistently until Happy) is a brutish but highly effective architectural technique for running autonomous AI agents. Instead of maintaining a massive conversational context window that degrades over time, Ralphing kills the agent's memory after every single action. It relies entirely on physical disk artifacts (`PRD.md`, `progress.txt`).

## The Ralphing Directives (Strict Rules for the Agent)
1. **Amnesia Protocol:** Assume you were just born. Your very first action MUST be to read `PRD.md` to discover your current state.
2. **Micro-Tasking:** Find the *first* incomplete task (marked with `[ ]`) in `PRD.md`. Do **NOT** attempt to complete the whole file. Execute *only* that single task.
3. **Artifact Creation:** Write your analysis to the specific local file requested by the task. 
4. **State Update:** Update `PRD.md` by changing the `[ ]` to `[x]`. 
5. **Progress Logging:** Append a one-sentence summary to `progress.txt`.
6. **Clean Exit:** Exit immediately without asking for user input. If a document is unreadable, mark it `[FAILED]`, log the error, and exit.

## The Orchestrator Script (`ralph_loop.sh`)
*Run this bash script to execute the agent autonomously.*

```bash
#!/bin/bash
MAX_ITERATIONS=15
CURRENT_ITER=0

echo "Initiating the Ralph Loop. May the infinite probability drive be with us."

while [ $CURRENT_ITER -lt $MAX_ITERATIONS ]; do
    CURRENT_ITER=$((CURRENT_ITER + 1))
    echo "Starting Iteration $CURRENT_ITER..."

    # Launch the agent in a fresh, isolated state.
    agent-cli "scan case files" --headless

    EXIT_CODE=$?

    if [ $EXIT_CODE -eq 0 ]; then
        echo "Agent completed a cycle successfully."
        if ! grep -q "\[ \]" PRD.md; then
            echo "All tasks complete. The goldfish has built a castle."
            exit 0
        fi
    else
        echo "Agent hit a critical failure. Check progress.txt."
        exit 1
    fi
done
echo "Max iterations reached."
