"""Partial launch of respmon_canon_rp_mix_3seed under MPS.

The 36 cells of respmon_canon_rp_mix_3seed minus the 6 listed in _COMPLETED
= 30 cells, same settings; together with those 6 they form the full sweep
dir.

Launch (MPS daemons already up; PATH must hold the driver-matched
nvidia-cuda-mps-control):
    PATH=/usr/bin:$PATH python -u sweep.py --name respmon_canon_rp_mix_3seed \
        --config sweeps/respmon_canon_rp_mix_3seed_refill_mps.py --no_baseline
"""
from sweeps.respmon_canon_rp_mix_3seed import runs as _all_runs

_COMPLETED = {
    "repeat_respmon_rp2_mix4to1_hf050_st500_s3",
    "persona_qa_flattery_respmon_bvo_rp2_mix1to1_hf050_st1000_s2",
    "repeat_respmon_rp2_mix1to1_hf050_st500_s3",
    "persona_qa_flattery_respmon_bvo_rp2_mix4to1_hf050_st1000_s2",
    "sorting_copy_respmon_rp2_mix1to1_hf050_st1000_s1",
    "object_qa_syco_respmon_iva_inv_rp2_mix4to1_hf050_st1000_s1",
}

runs = [r for r in _all_runs if r["run_name"] not in _COMPLETED]

assert len(runs) == 36 - 6 == 30, len(runs)
per_gpu = 5
no_baseline = True
