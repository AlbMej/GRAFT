from sweeps.respmon_repeat_sorting_dn_rp_3seed import *
_keep = {"repeat_respmon_donothing_hf050_st500_s1", "repeat_respmon_rp2_hf050_st500_s1"}
runs = [dict(r, vllm_no_sleep=True) for r in runs if r["run_name"] in _keep]
per_gpu = 1
