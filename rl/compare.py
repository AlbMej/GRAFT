import json, sys
run, mine_name = sys.argv[1], sys.argv[2]
K = ["both/combined/repeat_f1+repeat_extra_occurrences", "both/hack_freq/repeat_detector"]
def load(p): return {r["step"]: r for r in map(json.loads, open(p))}
mine  = load(f"output/{mine_name}/{run}/routing_eval.jsonl")
paper = load(f"paper_data/respmon-results/respmon_repeat_sorting_dn_rp_3seed/{run}/routing_eval.jsonl")
print("step | reward mine/paper | hack mine/paper")
for s in sorted(set(mine) & set(paper))[::5]:
    print(s, *[f"{mine[s][k]:.3f}/{paper[s][k]:.3f}" for k in K])
for tag, d in (("mine", mine), ("paper", paper)):
    rows = [d[s] for s in sorted(d)]; t = rows[int(len(rows)*0.9):]
    print(tag, "last-10% avg:", {k: round(sum(r[k] for r in t)/len(t), 3) for k in K})
