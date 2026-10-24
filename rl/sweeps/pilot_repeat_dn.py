from sweeps.respmon_repeat_sorting_dn_rp_3seed import *
runs = [dict(r, vllm_no_sleep=True) for r in runs
        if r["run_name"] == "repeat_respmon_donothing_hf050_st500_s1"]
per_gpu = 1
