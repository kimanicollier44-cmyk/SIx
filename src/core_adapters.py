from __future__ import annotations

import importlib
from dataclasses import dataclass, field
from typing import Any, Dict, Optional


def _try_import(module_name: str) -> Optional[Any]:
    for candidate in (f"src.{module_name}", module_name):
        try:
            return importlib.import_module(candidate)
        except ImportError:
            continue
    return None


def _instantiate_first(module: Any, class_names: tuple[str, ...]) -> Optional[Any]:
    if module is None:
        return None
    for name in class_names:
        cls = getattr(module, name, None)
        if isinstance(cls, type):
            try:
                return cls()
            except TypeError:
                continue
    return None


@dataclass
class SixCoreAdapters:
    safety_guard: Any = None
    agi_bridge: Any = None
    error_mesh: Any = None
    ui_core: Any = None
    loaded_modules: Dict[str, bool] = field(default_factory=dict)

    def __post_init__(self) -> None:
        guard_mod = _try_import("honeypot_mission_guard")
        self.safety_guard = _instantiate_first(
            guard_mod,
            ("HoneypotMissionGuard", "MissionGuard", "SafetyGuard"),
        )
        self.loaded_modules["honeypot_mission_guard"] = self.safety_guard is not None

        bridge_mod = _try_import("ani_agi_bridge")
        self.agi_bridge = _instantiate_first(
            bridge_mod,
            ("AniAgiBridge", "AGI_Bridge", "NeuromorphicBridge"),
        )
        self.loaded_modules["ani_agi_bridge"] = self.agi_bridge is not None

        mesh_mod = _try_import("error_reduction_mesh")
        self.error_mesh = _instantiate_first(
            mesh_mod,
            ("ErrorReductionMesh", "NeuromorphicMesh", "ErrorMesh"),
        )
        self.loaded_modules["error_reduction_mesh"] = self.error_mesh is not None

        ui_mod = _try_import("neural_core_interface")
        self.ui_core = _instantiate_first(
            ui_mod,
            ("NeuralCoreInterface", "SixNeuralCore", "CoreInterface"),
        )
        self.loaded_modules["neural_core_interface"] = self.ui_core is not None

    def inspect_prompt(self, prompt: str, metadata: Optional[Dict[str, Any]] = None) -> tuple[bool, str]:
        meta = metadata or {}
        if self.safety_guard is None:
            return True, "No external guard loaded; default pass"

        for method_name in ("inspect", "check_prompt", "validate", "evaluate", "guard"):
            fn = getattr(self.safety_guard, method_name, None)
            if callable(fn):
                try:
                    res = fn(prompt, meta)
                except TypeError:
                    res = fn(prompt)

                if isinstance(res, tuple) and len(res) >= 2:
                    return bool(res[0]), str(res[1])
                if isinstance(res, bool):
                    return res, "Blocked by HoneypotMissionGuard" if not res else "Allowed"
                if isinstance(res, dict):
                    allowed = bool(res.get("allowed", not res.get("blocked", False)))
                    reason = str(res.get("reason", "HoneypotMissionGuard policy decision"))
                    return allowed, reason

        return True, "Guard present without matching inspect method"

    def sync_ui_state(self, state: str) -> None:
        if self.ui_core is None:
            return
        for method_name in ("set_state", "transition", "update_state", "step"):
            fn = getattr(self.ui_core, method_name, None)
            if callable(fn):
                try:
                    fn(state)
                    return
                except TypeError:
                    continue
