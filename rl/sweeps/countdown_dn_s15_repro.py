"""DN (no-intervention) seed 15 of the countdown_code_rp2-0702-0026 sweep.

The do-nothing arm of countdown_code_rp2-0702-0026 for seed 15: _base
verbatim (flat lr 5e-4, no penalty, routing_mode none), explicit run_name so
downstream fseval/figure globs match the sweep's naming.

Local (pod) backend; set GRAFT_COUNTDOWN_SFT_MODEL to the model path.

    CUDA_VISIBLE_DEVICES=0 python -u sweep.py --name countdown_dn_s15_repro \
        --config sweeps/countdown_dn_s15_repro.py --no_baseline
"""
import os
from sweeps.countdown_code_rp import _base

runs = [{
    **_base,
    "model": os.environ.get("GRAFT_COUNTDOWN_SFT_MODEL", "/workspace/small-rl/output/countdown_sft_model/qwen3-8b"),
    "seed": 15,
    "run_name": "countdown_code_hack_reward_penalty_amountmissing_s15",
}]

per_gpu = 1
no_baseline = True
