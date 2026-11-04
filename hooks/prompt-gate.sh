#!/bin/sh
# skill-flow prompt gate. Prints one short line of context on every prompt so the
# model runs the `flow` skill. It never blocks and never reads the prompt text.
# Exit 0 always.
HOME_DIR="${HOME:-/tmp}"
CLAUDE_DIR="${CLAUDE_CONFIG_DIR:-$HOME_DIR/.claude}"
PROFILE="${SKILL_FLOW_HOME:-$CLAUDE_DIR/skill-flow}"
if [ -f "$PROFILE/PROFILE.md" ]; then
  STATE="profile: $PROFILE"
else
  STATE="profile: missing (run the \`setup\` skill now, before the work; /skill-flow:setup)"
fi
cat <<MSG
SKILL-FLOW GATE: run the \`flow\` skill on this prompt before any work. Size it (quick, standard, big), rewrite it one-shot, review every active skill and load the ones that serve it, ask up front only if an answer changes the result, planner plans and writers write on a big job, prove it, deliver in simple-talk. Standing triggers: a quote, illustration, declaration page or pasted premium runs \`protection-desk\` and prints the PDF unasked; anything a person will see runs \`impeccable\` then \`pixel-proof\`; a tool or skill missing for the job runs \`connect\`; an upcoming outside meeting runs \`meeting-prep\`. Skip only pure chat. Surface: Claude Code. $STATE
MSG
exit 0
