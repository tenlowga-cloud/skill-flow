#!/usr/bin/env bash
# The lint must fail the leaky fixture and pass the rebuilt one.
set -u
here="$(cd "$(dirname "$0")" && pwd)"
lint="$here/../scripts/move_lint.py"
fail=0
tmp="$(mktemp)"; sed "s/@@DASH@@/$(printf '\xe2\x80\x94')/" "$here/fixtures/before.txt" > "$tmp"
out="$(python3 "$lint" "$tmp")"; code=$?; rm -f "$tmp"
[ "$code" -eq 1 ] || { echo "FAIL: before.txt should exit 1, got $code"; fail=1; }
for want in "em dash" "weak opener" "sender focus" "empty phrases" "pressure words" "kinds of ask"; do
  grep -q "$want" <<<"$out" || { echo "FAIL: before.txt missing '$want'"; fail=1; }
done
python3 "$lint" "$here/fixtures/after.txt" >/dev/null; code=$?
[ "$code" -eq 0 ] || { echo "FAIL: after.txt should exit 0, got $code"; fail=1; }
python3 "$lint" "$here/fixtures/after.txt" --json | python3 -c 'import json,sys; r=json.load(sys.stdin); assert r["em_dashes"]==0 and r["you_count"]>r["sender_count"]' || { echo "FAIL: json output"; fail=1; }
[ "$fail" -eq 0 ] && echo "move-lint tests: pass"
exit "$fail"
