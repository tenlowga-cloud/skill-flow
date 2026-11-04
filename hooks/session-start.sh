#!/bin/sh
# skill-flow session start. Prints a few lines of context when a session opens so
# the model knows whether this is a first run (no profile: run setup), whether the
# operating file and the design plugin are in place, and where the profile lives.
# Never blocks, never reads the prompt. Exit 0 always.
HOME_DIR="${HOME:-/tmp}"
CLAUDE_DIR="${CLAUDE_CONFIG_DIR:-$HOME_DIR/.claude}"
PROFILE="${SKILL_FLOW_HOME:-$CLAUDE_DIR/skill-flow}"

if [ -f "$PROFILE/PROFILE.md" ]; then
  STATE="profile found at $PROFILE."
  FIRST_RUN="no"
else
  STATE="no profile at $PROFILE: this is a first run."
  FIRST_RUN="yes"
fi

if [ -f "$CLAUDE_DIR/CLAUDE.md" ]; then
  RULES="operating file present ($CLAUDE_DIR/CLAUDE.md)."
else
  RULES="no operating file yet; operating-rules writes it at the end of setup."
fi

if ls "$CLAUDE_DIR"/plugins 2>/dev/null | grep -qi impeccable || \
   ls "$CLAUDE_DIR"/plugins/*/ 2>/dev/null | grep -qi impeccable; then
  DESIGN="impeccable plugin present."
else
  DESIGN="impeccable plugin not found; connect installs it (pbakaus/impeccable)."
fi

if [ -f "$CLAUDE_DIR/skills/protection-desk/desk.py" ]; then
  DESK="Protection Desk installed."
else
  DESK="Protection Desk not installed; the protection-desk skill walks the install on the first quote drop."
fi

if [ "$FIRST_RUN" = "yes" ]; then
  cat <<MSG
SKILL-FLOW FIRST RUN: $STATE Before any other work on the first prompt that asks for something, run the \`setup\` skill start to finish (it audits tools, asks five short rounds, connects the CRM and tools, installs impeccable, writes the profile and operating file, schedules routines, then hands to \`blueprint\`). If the first prompt is pure chat, say in one line that setup is ready when they are. $RULES $DESIGN $DESK
MSG
else
  cat <<MSG
SKILL-FLOW: $STATE $RULES $DESIGN $DESK Read PROFILE.md and STACK.md before a job that touches the owner's business. Standing triggers: a quote, illustration or declaration page drop runs \`protection-desk\` unasked; anything a person sees runs \`impeccable\` then \`pixel-proof\`; a missing tool runs \`connect\`.
MSG
fi
exit 0
