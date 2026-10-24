from sweeps.respmon_repeat_sorting_dn_rp_3seed import *

runs = [
    dict(r, vllm_no_sleep=True)
    for r in runs
    if r["run_name"] == "repeat_respmon_rp2_hf050_st500_s1"
]
assert len(runs) == 1, f"Expected one RP2 run, got {len(runs)}"
per_gpu = 1
