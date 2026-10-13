"""Canonical-recipe GRAFT on object_qa (configs/object_qa_respmon.yaml: the
monitor watches actually / exactly / quite and is blind to "indeed").

This sweep provides the canonical-recipe GRAFT arm for object_qa
(the vercoh128 variant, whose unhackable-sourced anchor leaks hackability
information, is in respmon_rv2_vercoh128_objinv_gr_3seed): the canonical recipe (coherence from the FULL training distribution with a
-2.0 penalty on monitor-flagged coherence samples), matching
respmon_rv2_gr_3seed.

1 env x 3 seeds = 3 runs.

Launch:
    PATH=/usr/bin:$PATH python -u sweep.py --name respmon_objinv_gr_canon_3seed \
        --config sweeps/respmon_objinv_gr_canon_3seed.py --no_baseline
"""
from sweeps.respmon_repro_coh128_lam1_3seed import _shared, _new, _seeds

runs = [{
    **_shared, **_new,
    "config": "configs/object_qa_respmon.yaml",
    "max_steps": 1000,
    "routing_mode": "classic",
    "unconditional_hackable": False,
    "hack_frac": 0.5,
    "rh_detector_recall": 1.0,
    "eval_every": 10,
    "eval_full_completions": True,
    "seed": s,
    "run_name": f"object_qa_syco_respmon_iva_inv_gr_cls_canon_hf050_st1000_s{s}",
} for s in _seeds]

assert len(runs) == 3, len(runs)
per_gpu = 3
no_baseline = True
