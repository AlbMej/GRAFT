"""Sweep 2: GR on the rv2 family with every env's monitored and unmonitored
forms swapped relative to respmon_rv2_gr_3seed (syco: monitor greps
{actually, exactly, quite}, indeed blind; persona: 5 words monitored,
beautiful blind; repeat: noncontiguous monitored; stock sort: reformatted
monitored). For addition, cities, persona, repeat and stock sort these are
the swapped-monitor configs (*_inv.yaml / *_inverted.yaml); for object_qa it
is object_qa's own config (configs/object_qa_respmon.yaml), whose swapped
counterpart (configs/object_qa_syco_respmon_iva.yaml) is the one in
respmon_rv2_gr_3seed.

Launch:
    PATH=/usr/bin:$PATH python -u sweep.py --name respmon_rv2_inverted_gr_3seed \
        --config sweeps/respmon_rv2_inverted_gr_3seed.py --no_baseline \
        --baseline_sweep respmon_rv2_gr_3seed
"""
from sweeps.respmon_repro_coh128_lam1_3seed import _shared, _new, _seeds, _env_short

_envs = [
    {"config": "configs/addition_v2_syco_respmon_iva_inv.yaml", "max_steps": 2000},
    {"config": "configs/object_qa_respmon.yaml",                "max_steps": 1000},
    {"config": "configs/cities_qa_syco_respmon_iva_inv.yaml",   "max_steps": 2000},
    {"config": "configs/persona_qa_flattery_respmon_bvo_inv.yaml", "max_steps": 1000},
    {"config": "configs/repeat_respmon_inverted.yaml",               "max_steps": 500},
    {"config": "configs/sorting_copy_respmon_inverted.yaml",         "max_steps": 1000},
]

runs = []
for env in _envs:
    ename = _env_short(env["config"])
    steps = env["max_steps"]
    for seed in _seeds:
        runs.append({
            **_shared, **env, **_new,
            "unconditional_hackable": False,
            "hack_frac": 0.5,
            "rh_detector_recall": 1.0,
            "seed": seed,
            "run_name": f"{ename}_invgr_cls_coh128_pen2_balanced_splitmoment_lam1_hf050_st{steps}_s{seed}",
        })

assert len(runs) == len(_envs) * len(_seeds) == 18, len(runs)

per_gpu = 5
no_baseline = True
