"""Canonical respmon env list: the addition, object_qa, cities_qa, persona_qa
and repeat_extra configs, plus the stock sort config (sorting_copy_respmon).
Each sweep keeps the stock sort, swaps in the framed sort env
(configs/sorting_copy_framed.yaml), or skips sort. Shared by the
canonical-family sweeps so the env set is defined in exactly one place."""

CANON_ENVS = [
    {"config": "configs/addition_v2_syco_respmon_iva.yaml",     "max_steps": 2000},
    {"config": "configs/object_qa_respmon.yaml",                "max_steps": 1000},
    {"config": "configs/cities_qa_syco_respmon_iva.yaml",       "max_steps": 2000},
    {"config": "configs/persona_qa_flattery_respmon_bvo.yaml",  "max_steps": 1000},
    {"config": "configs/repeat_respmon.yaml",                   "max_steps": 500},
    {"config": "configs/sorting_copy_respmon.yaml",             "max_steps": 1000},
]
