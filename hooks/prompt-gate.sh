#!/bin/sh
# skill-flow prompt gate. Prints one short line of context on every prompt so the
# model runs the `flow` skill. It never blocks and never reads the prompt text.
# Exit 0 always.
HOME_DIR="${HOME:-/tmp}"
PROFILE="${SKILL_FLOW_HOME:-$HOME_DIR/.claude/skill-flow}"
if [ -f "$PROFILE/PROFILE.md" ]; then
  STATE="profile: $PROFILE"
else
  STATE="profile: missing (run /skill-flow:setup once)"
fi
cat <<MSG
SKILL-FLOW GATE: run the \`flow\` skill on this prompt before any work. Size it (quick, standard, big), rewrite it one-shot, review every active skill and load the ones that serve it, ask up front only if an answer changes the result, planner plans and writers write on a big job, prove it, deliver in simple-talk. Skip only pure chat. Surface: Claude Code. $STATE
MSG
exit 0
